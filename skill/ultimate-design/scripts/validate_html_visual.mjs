#!/usr/bin/env node
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";

function parseArgs(argv) {
  const args = {
    selector: "[data-ud-check], [data-check]",
    slideSelector: ".slide",
    thumbSelector: ".thumb",
    spacing: 36,
    viewports: "desktop=1440x900,mobile=390x844",
  };
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (!token.startsWith("--")) continue;
    const key = token.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith("--")) {
      args[key] = true;
    } else {
      args[key] = next;
      i += 1;
    }
  }
  return args;
}

function parseViewports(value) {
  return String(value)
    .split(",")
    .filter(Boolean)
    .map((entry) => {
      const [name, size] = entry.split("=");
      const [width, height] = size.split("x").map((n) => Number.parseInt(n, 10));
      if (!name || !width || !height) throw new Error(`Invalid viewport: ${entry}`);
      return { name, width, height };
    });
}

async function loadPlaywright() {
  const runtimePlaywright = path.resolve(
    path.dirname(process.execPath),
    "..",
    "node_modules",
    "playwright",
    "index.mjs",
  );
  const candidates = [
    process.env.PLAYWRIGHT_MODULE,
    "playwright",
    path.resolve(process.cwd(), "node_modules", "playwright", "index.mjs"),
    runtimePlaywright,
  ].filter(Boolean);
  const errors = [];
  for (const candidate of candidates) {
    try {
      return await import(candidate);
    } catch (error) {
      errors.push(`${candidate}: ${error.message}`);
    }
  }
  throw new Error(`Could not import Playwright. Tried:\n${errors.join("\n")}`);
}

async function launchChromium(chromium, browserPath) {
  const candidates = [
    browserPath,
    process.env.CHROME_PATH,
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  ].filter(Boolean);
  for (const executablePath of candidates) {
    try {
      return await chromium.launch({ headless: true, executablePath });
    } catch {
      // Try the next local browser path.
    }
  }
  return chromium.launch({ headless: true });
}

const args = parseArgs(process.argv.slice(2));
if (!args.input) {
  console.error(
    "Usage: node scripts/validate_html_visual.mjs --input artifact.html [--out out-dir] [--viewports desktop=1440x900,mobile=390x844] [--spacing 36]",
  );
  process.exit(2);
}

const inputPath = path.resolve(String(args.input));
const outputDir = path.resolve(String(args.out || path.join(path.dirname(inputPath), "ultimate-design-visual-check")));
const reportPath = path.join(outputDir, "visual-validation-report.json");
const screenshotsDir = path.join(outputDir, "screenshots");
const minSpacingDesignPx = Number(args.spacing || 36);
const viewports = parseViewports(args.viewports);

mkdirSync(screenshotsDir, { recursive: true });

const { chromium } = await loadPlaywright();
const browser = await launchChromium(chromium, args.browserPath);

const report = {
  inputPath,
  checkedAt: new Date().toISOString(),
  selector: args.selector,
  minSpacingDesignPx,
  viewports,
  results: [],
};

for (const viewport of viewports) {
  const page = await browser.newPage({ viewport });
  await page.goto(`file://${inputPath}`);
  await page.waitForLoadState("domcontentloaded");
  await page.waitForTimeout(250);

  const slideCount = await page.locator(args.slideSelector).count();
  const thumbCount = await page.locator(args.thumbSelector).count();
  const frames = slideCount > 0 ? slideCount : 1;

  for (let frameIndex = 0; frameIndex < frames; frameIndex += 1) {
    if (slideCount > 0) {
      const thumb = page.locator(`${args.thumbSelector}[data-slide="${frameIndex}"]`);
      if ((await thumb.count()) > 0) {
        await thumb.click({ timeout: 5000 });
      } else {
        await page.evaluate(
          ({ selector, index }) => {
            const slides = Array.from(document.querySelectorAll(selector));
            slides.forEach((slide, i) => slide.classList.toggle("is-active", i === index));
          },
          { selector: args.slideSelector, index: frameIndex },
        );
      }
      await page.waitForTimeout(80);
    }

    const screenshotPath = path.join(
      screenshotsDir,
      `${viewport.name}-${String(frameIndex + 1).padStart(2, "0")}.png`,
    );
    await page.screenshot({ path: screenshotPath, fullPage: true });

    const checks = await page.evaluate(
      ({ slideSelector, markerSelector, minSpacingDesignPx }) => {
        const activeSlide =
          document.querySelector(`${slideSelector}.is-active`) ||
          document.querySelector(`${slideSelector}[aria-hidden="false"]`) ||
          document.querySelector(slideSelector);
        const scope = activeSlide || document.documentElement;
        const sr = scope.getBoundingClientRect();
        const scale = activeSlide && sr.width ? sr.width / 1280 : 1;
        const minGap = minSpacingDesignPx * scale;

        function numberAttr(el, names) {
          for (const name of names) {
            const value = el.getAttribute(name);
            if (value !== null && value !== "") {
              const parsed = Number(value);
              if (Number.isFinite(parsed)) return parsed;
            }
          }
          return null;
        }

        function stringAttr(el, names) {
          for (const name of names) {
            const value = el.getAttribute(name);
            if (value !== null && value !== "") return value;
          }
          return "";
        }

        function booleanAttr(el, names) {
          return names.some((name) => {
            const value = el.getAttribute(name);
            return value === "" || value === "true" || value === "1";
          });
        }

        function countTextLines(el) {
          const text = (el.innerText || el.textContent || "").trim();
          if (!text) return 0;
          const range = document.createRange();
          range.selectNodeContents(el);
          const rects = Array.from(range.getClientRects()).filter((rect) => rect.width > 1 && rect.height > 1);
          if (typeof range.detach === "function") range.detach();
          if (!rects.length) return 1;
          const threshold = Math.max(2, 3 * scale);
          const lines = [];
          for (const rect of rects.sort((a, b) => a.top - b.top)) {
            if (!lines.some((top) => Math.abs(top - rect.top) <= threshold)) lines.push(rect.top);
          }
          return lines.length || 1;
        }

        const nodes = Array.from(scope.querySelectorAll(markerSelector)).filter((el) => {
          const r = el.getBoundingClientRect();
          const style = getComputedStyle(el);
          return r.width > 0 && r.height > 0 && style.visibility !== "hidden" && style.display !== "none";
        });

        const boxes = nodes.map((el, index) => {
          const r = el.getBoundingClientRect();
          const style = getComputedStyle(el);
          const clipsX = style.overflowX !== "visible" && el.scrollWidth > el.clientWidth + 4 * scale;
          const clipsY = style.overflowY !== "visible" && el.scrollHeight > el.clientHeight + 4 * scale;
          const noWrap = booleanAttr(el, ["data-ud-nowrap", "data-nowrap"]);
          const maxLines =
            numberAttr(el, ["data-ud-max-lines", "data-max-lines"]) ??
            (noWrap ? 1 : null);
          return {
            index,
            label: el.getAttribute("data-ud-check") || el.getAttribute("data-check") || `${el.tagName}-${index}`,
            role: el.getAttribute("data-ud-role") || "",
            tag: el.tagName,
            text: (el.textContent || "").replace(/\s+/g, " ").trim().slice(0, 80),
            left: r.left,
            top: r.top,
            right: r.right,
            bottom: r.bottom,
            width: r.width,
            height: r.height,
            clipped: clipsX || clipsY,
            lineCount: countTextLines(el),
            specs: {
              minLines: numberAttr(el, ["data-ud-min-lines", "data-min-lines"]),
              maxLines,
              noWrap,
              alignLeft: stringAttr(el, ["data-ud-align-left", "data-align-left"]),
              alignRight: stringAttr(el, ["data-ud-align-right", "data-align-right"]),
              alignTop: stringAttr(el, ["data-ud-align-top", "data-align-top"]),
              alignBottom: stringAttr(el, ["data-ud-align-bottom", "data-align-bottom"]),
              alignCenterX: stringAttr(el, ["data-ud-align-center-x", "data-align-center-x"]),
              alignCenterY: stringAttr(el, ["data-ud-align-center-y", "data-align-center-y"]),
              tolerance: numberAttr(el, ["data-ud-align-tolerance", "data-align-tolerance"]) ?? 4,
            },
          };
        });

        const outside = boxes.filter(
          (box) =>
            box.left < sr.left - 2 ||
            box.top < sr.top - 2 ||
            box.right > sr.right + 2 ||
            box.bottom > sr.bottom + 2,
        );

        const clipped = boxes.filter((box) => box.clipped);
        const collisions = [];
        const tightSpacing = [];
        const lineFailures = [];
        const alignmentFailures = [];
        const byLabel = new Map(boxes.map((box) => [box.label, box]));

        for (const box of boxes) {
          if (box.specs.maxLines !== null && box.lineCount > box.specs.maxLines) {
            lineFailures.push({
              label: box.label,
              problem: "too-many-lines",
              lineCount: box.lineCount,
              maxLines: box.specs.maxLines,
              text: box.text,
            });
          }
          if (box.specs.minLines !== null && box.lineCount < box.specs.minLines) {
            lineFailures.push({
              label: box.label,
              problem: "too-few-lines",
              lineCount: box.lineCount,
              minLines: box.specs.minLines,
              text: box.text,
            });
          }
        }

        function addAlignmentFailure(box, targetLabel, axis, actual, expected, tolerance) {
          const delta = Math.abs(actual - expected);
          if (delta > tolerance) {
            alignmentFailures.push({
              label: box.label,
              target: targetLabel,
              axis,
              delta: Math.round(delta),
              tolerance: Math.round(tolerance),
              actual: Math.round(actual),
              expected: Math.round(expected),
            });
          }
        }

        for (const box of boxes) {
          const tolerance = box.specs.tolerance * scale;
          const alignmentChecks = [
            ["left", box.specs.alignLeft, box.left, (target) => target.left],
            ["right", box.specs.alignRight, box.right, (target) => target.right],
            ["top", box.specs.alignTop, box.top, (target) => target.top],
            ["bottom", box.specs.alignBottom, box.bottom, (target) => target.bottom],
            ["center-x", box.specs.alignCenterX, box.left + box.width / 2, (target) => target.left + target.width / 2],
            ["center-y", box.specs.alignCenterY, box.top + box.height / 2, (target) => target.top + target.height / 2],
          ];
          for (const [axis, targetLabel, actual, targetValue] of alignmentChecks) {
            if (!targetLabel) continue;
            const target = byLabel.get(targetLabel);
            if (!target) {
              alignmentFailures.push({ label: box.label, target: targetLabel, axis, problem: "missing-target" });
              continue;
            }
            addAlignmentFailure(box, targetLabel, axis, actual, targetValue(target), tolerance);
          }
        }

        for (let i = 0; i < boxes.length; i += 1) {
          for (let j = i + 1; j < boxes.length; j += 1) {
            const a = boxes[i];
            const b = boxes[j];
            const aNode = nodes[i];
            const bNode = nodes[j];
            if (aNode.contains(bNode) || bNode.contains(aNode)) continue;

            const xOverlap = Math.min(a.right, b.right) - Math.max(a.left, b.left);
            const yOverlap = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
            const xOverlapRatio = xOverlap / Math.max(1, Math.min(a.width, b.width));
            const yOverlapRatio = yOverlap / Math.max(1, Math.min(a.height, b.height));

            if (xOverlap > 4 * scale && yOverlap > 4 * scale) {
              collisions.push({ a, b, xOverlap: Math.round(xOverlap), yOverlap: Math.round(yOverlap) });
              continue;
            }

            if (xOverlapRatio > 0.2 && yOverlap <= 0) {
              const gap = Math.max(a.top, b.top) - Math.min(a.bottom, b.bottom);
              if (gap >= 0 && gap < minGap) {
                tightSpacing.push({ direction: "vertical", a, b, gap: Math.round(gap), minGap: Math.round(minGap) });
              }
            }

            if (yOverlapRatio > 0.2 && xOverlap <= 0) {
              const gap = Math.max(a.left, b.left) - Math.min(a.right, b.right);
              if (gap >= 0 && gap < minGap) {
                tightSpacing.push({ direction: "horizontal", a, b, gap: Math.round(gap), minGap: Math.round(minGap) });
              }
            }
          }
        }

        return {
          title: activeSlide?.dataset?.title || document.title || "",
          markerCount: boxes.length,
          outside,
          clipped,
          collisions,
          tightSpacing,
          lineFailures,
          alignmentFailures,
        };
      },
      { slideSelector: args.slideSelector, markerSelector: args.selector, minSpacingDesignPx },
    );

    report.results.push({
      viewport: viewport.name,
      frame: frameIndex + 1,
      slideCount,
      thumbCount,
      screenshotPath,
      ...checks,
    });
  }

  await page.close();
}

await browser.close();

report.failures = report.results.filter(
  (result) =>
    (result.slideCount > 0 && result.thumbCount > 0 && result.slideCount !== result.thumbCount) ||
    result.markerCount === 0 ||
    result.outside.length > 0 ||
    result.clipped.length > 0 ||
    result.collisions.length > 0 ||
    result.tightSpacing.length > 0 ||
    result.lineFailures.length > 0 ||
    result.alignmentFailures.length > 0,
);

writeFileSync(reportPath, JSON.stringify(report, null, 2));

const summary = {
  checked: report.results.length,
  failures: report.failures.length,
  reportPath,
  screenshotsDir,
  firstFailures: report.failures.slice(0, 8).map((failure) => ({
    viewport: failure.viewport,
    frame: failure.frame,
    title: failure.title,
    markerCount: failure.markerCount,
    outside: failure.outside.length,
    clipped: failure.clipped.length,
    collisions: failure.collisions.length,
    tightSpacing: failure.tightSpacing.length,
    lineFailures: failure.lineFailures.length,
    alignmentFailures: failure.alignmentFailures.length,
  })),
};

console.log(JSON.stringify(summary, null, 2));
process.exit(report.failures.length ? 1 : 0);
