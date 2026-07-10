#!/usr/bin/env node
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";
import { launchPinnedChromium } from "./pinned_playwright.mjs";

function parseArgs(argv) {
  const args = {
    selector: "[data-ud-check], [data-check]",
    slideSelector: ".slide",
    thumbSelector: ".thumb",
    spacing: 36,
    occlusion: true,
    occlusionSamples: 9,
    wait: 1000,
    pageSpacing: 12,
    viewports: "desktop=1440x900,mobile=390x844",
  };
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (!token.startsWith("--")) continue;
    const key = token.slice(2);
    const next = argv[i + 1];
    if (key === "no-occlusion") {
      args.occlusion = false;
    } else if (!next || next.startsWith("--")) {
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

const args = parseArgs(process.argv.slice(2));
if (!args.input) {
  console.error(
    "Usage: node scripts/validate_html_visual.mjs --input artifact.html [--out out-dir] [--viewports desktop=1440x900,mobile=390x844] [--spacing 36] [--page-spacing 12] [--wait 1000] [--no-occlusion]",
  );
  process.exit(2);
}

const inputPath = path.resolve(String(args.input));
const outputDir = path.resolve(String(args.out || path.join(path.dirname(inputPath), "ultimate-design-visual-check")));
const reportPath = path.join(outputDir, "visual-validation-report.json");
const screenshotsDir = path.join(outputDir, "screenshots");
const minSpacingDesignPx = Number(args.spacing || 36);
const pageMinSpacingPx = Number(args.pageSpacing || args["page-spacing"] || 12);
const occlusionEnabled = args.occlusion !== false && args.occlusion !== "false";
const occlusionSamples = Number(args.occlusionSamples || args["occlusion-samples"] || 9);
const renderWaitMs = Number(args.wait || args["wait-ms"] || 1000);
const viewports = parseViewports(args.viewports);

mkdirSync(screenshotsDir, { recursive: true });

const browser = await launchPinnedChromium(args.browserPath || args["browser-path"]);

const report = {
  schemaVersion: "ultimate-design.rendered-ui-audit.v1",
  auditKind: "rendered-ui-audit",
  status: "pending",
  inputPath,
  checkedAt: new Date().toISOString(),
  config: {
    selector: args.selector,
    minSpacingDesignPx,
    pageMinSpacingPx,
    occlusionEnabled,
    occlusionSamples,
    renderWaitMs,
  },
  selector: args.selector,
  minSpacingDesignPx,
  pageMinSpacingPx,
  occlusionEnabled,
  occlusionSamples,
  renderWaitMs,
  viewports,
  summary: {
    checkedZones: 0,
    findings: 0,
    failures: 0,
    warnings: 0,
    infos: 0,
    allowed: 0,
  },
  facts: {
    page: {
      horizontalOverflow: [],
    },
    interactive: {
      visibleCount: 0,
      smallTargets: 0,
      missingAccessibleNames: 0,
    },
  },
  findings: [],
  results: [],
};

for (const viewport of viewports) {
  const page = await browser.newPage({ viewport });
  await page.goto(`file://${inputPath}`);
  await page.waitForLoadState("domcontentloaded");
  await page.waitForTimeout(renderWaitMs);

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
      async ({ slideSelector, markerSelector, minSpacingDesignPx, pageMinSpacingPx, occlusionEnabled, occlusionSamples }) => {
        const activeSlide =
          document.querySelector(`${slideSelector}.is-active`) ||
          document.querySelector(`${slideSelector}[aria-hidden="false"]`) ||
          document.querySelector(slideSelector);
        const scope = activeSlide || document.documentElement;
        const sr = scope.getBoundingClientRect();
        const scale = activeSlide && sr.width ? sr.width / 1280 : 1;
        const defaultMinGap = activeSlide ? minSpacingDesignPx * scale : pageMinSpacingPx;

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

        function allows(el, names) {
          return names.some((name) => {
            const value = el.getAttribute(name);
            return value === "" || value === "true" || value === "1" || value === "allow" || value === "ignore";
          });
        }

        function splitTokens(value) {
          return String(value || "")
            .split(/[,\s]+/)
            .map((token) => token.trim())
            .filter(Boolean);
        }

        function parseAllowance(el) {
          const explicit = splitTokens(el.getAttribute("data-ud-allow") || el.getAttribute("data-allow"));
          const legacy = [];
          if (allows(el, ["data-ud-allow-occlusion", "data-allow-occlusion"])) legacy.push("occlusion");
          if (allows(el, ["data-ud-allow-invisible", "data-allow-invisible"])) legacy.push("invisible");
          return {
            tokens: Array.from(new Set([...explicit, ...legacy])),
            explicit,
            legacy,
            reason: stringAttr(el, ["data-ud-allow-reason", "data-allow-reason"]),
            owner: stringAttr(el, ["data-ud-allow-owner", "data-allow-owner"]),
            expires: stringAttr(el, ["data-ud-allow-expires", "data-allow-expires"]),
          };
        }

        function allowsRule(allowance, ruleId) {
          return allowance.tokens.includes(ruleId);
        }

        function selectorFor(el) {
          const udCheck = el.getAttribute("data-ud-check");
          if (udCheck) return `[data-ud-check="${udCheck}"]`;
          const check = el.getAttribute("data-check");
          if (check) return `[data-check="${check}"]`;
          const testId = el.getAttribute("data-testid");
          if (testId) return `[data-testid="${testId}"]`;
          if (el.id) return `#${el.id}`;
          const tag = el.tagName.toLowerCase();
          const parent = el.parentElement;
          if (!parent) return tag;
          const siblings = Array.from(parent.children).filter((node) => node.tagName === el.tagName);
          const index = siblings.indexOf(el) + 1;
          return `${tag}:nth-of-type(${Math.max(1, index)})`;
        }

        function rectJson(rect) {
          return {
            x: Math.round(rect.left),
            y: Math.round(rect.top),
            width: Math.round(rect.width),
            height: Math.round(rect.height),
            right: Math.round(rect.right),
            bottom: Math.round(rect.bottom),
          };
        }

        function isVisibleElement(el) {
          const r = el.getBoundingClientRect();
          const style = getComputedStyle(el);
          return (
            r.width > 0 &&
            r.height > 0 &&
            style.visibility !== "hidden" &&
            style.display !== "none" &&
            Number.parseFloat(style.opacity || "1") > 0.05
          );
        }

        function labelledByText(el) {
          const ids = splitTokens(el.getAttribute("aria-labelledby"));
          return ids
            .map((id) => document.getElementById(id)?.textContent || "")
            .join(" ")
            .replace(/\s+/g, " ")
            .trim();
        }

        function accessibleNameHeuristic(el) {
          const aria = (el.getAttribute("aria-label") || "").trim();
          if (aria) return aria;
          const labelled = labelledByText(el);
          if (labelled) return labelled;
          const labels = "labels" in el ? Array.from(el.labels || []).map((label) => label.textContent || "").join(" ") : "";
          if (labels.trim()) return labels.replace(/\s+/g, " ").trim();
          for (const attrName of ["alt", "value", "placeholder", "title"]) {
            const value = (el.getAttribute(attrName) || "").trim();
            if (value) return value;
          }
          const svgTitle = el.querySelector?.("svg title")?.textContent?.trim();
          if (svgTitle) return svgTitle;
          return (el.innerText || el.textContent || "").replace(/\s+/g, " ").trim();
        }

        function isInteractive(el) {
          const tag = el.tagName.toLowerCase();
          const role = (el.getAttribute("role") || "").toLowerCase();
          if (tag === "input" && (el.getAttribute("type") || "").toLowerCase() === "hidden") return false;
          return (
            ["a", "button", "input", "select", "textarea", "summary"].includes(tag) ||
            ["button", "link", "menuitem", "tab", "checkbox", "radio", "switch", "combobox", "option"].includes(role) ||
            (el.hasAttribute("tabindex") && el.getAttribute("tabindex") !== "-1")
          );
        }

        function waitForPaint() {
          return new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
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

        const nodes = Array.from(scope.querySelectorAll(markerSelector)).filter((el) => isVisibleElement(el));

        const boxes = nodes.map((el, index) => {
          const r = el.getBoundingClientRect();
          const style = getComputedStyle(el);
          const clipsX = style.overflowX !== "visible" && el.scrollWidth > el.clientWidth + 4 * scale;
          const clipsY = style.overflowY !== "visible" && el.scrollHeight > el.clientHeight + 4 * scale;
          const noWrap = booleanAttr(el, ["data-ud-nowrap", "data-nowrap"]);
          const maxLines =
            numberAttr(el, ["data-ud-max-lines", "data-max-lines"]) ??
            (noWrap ? 1 : null);
          const allowance = parseAllowance(el);
          return {
            index,
            label: el.getAttribute("data-ud-check") || el.getAttribute("data-check") || `${el.tagName}-${index}`,
            selector: selectorFor(el),
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
            invisible: Number.parseFloat(style.opacity || "1") <= 0.05,
            allowance,
            allowsOcclusion: allowsRule(allowance, "occlusion"),
            allowsInvisible: allowsRule(allowance, "invisible"),
            specs: {
              minLines: numberAttr(el, ["data-ud-min-lines", "data-min-lines"]),
              maxLines,
              noWrap,
              minGap: numberAttr(el, ["data-ud-min-gap", "data-min-gap"]),
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
        const invisible = boxes.filter((box) => box.invisible && !box.allowsInvisible);
        const collisions = [];
        const occluded = [];
        const tightSpacing = [];
        const lineFailures = [];
        const alignmentFailures = [];
        const allowanceGovernance = [];
        const byLabel = new Map(boxes.map((box) => [box.label, box]));

        const now = new Date();
        for (const box of boxes) {
          const allowance = box.allowance;
          if (!allowance.tokens.length) continue;
          if (allowance.tokens.includes("all")) {
            allowanceGovernance.push({
              label: box.label,
              selector: box.selector,
              ruleId: "allow-all-forbidden",
              severity: "fail",
              message: "`all` is not a valid Rendered UI Audit allowance; list exact rule ids.",
              allowance,
            });
          }
          if (allowance.legacy.length) {
            allowanceGovernance.push({
              label: box.label,
              selector: box.selector,
              ruleId: "legacy-allowance",
              severity: "warn",
              message: "Legacy allow attributes are supported for compatibility; prefer data-ud-allow with reason, owner, and expires.",
              allowance,
            });
          }
          for (const field of ["reason", "owner", "expires"]) {
            if (!allowance[field]) {
              allowanceGovernance.push({
                label: box.label,
                selector: box.selector,
                ruleId: `allowance-missing-${field}`,
                severity: "warn",
                message: `Rendered UI Audit allowance is missing ${field}.`,
                allowance,
              });
            }
          }
          if (allowance.expires) {
            const expires = new Date(`${allowance.expires}T23:59:59`);
            if (Number.isNaN(expires.getTime())) {
              allowanceGovernance.push({
                label: box.label,
                selector: box.selector,
                ruleId: "allowance-invalid-expires",
                severity: "fail",
                message: "Rendered UI Audit allowance has an invalid expires date.",
                allowance,
              });
            } else if (expires < now) {
              allowanceGovernance.push({
                label: box.label,
                selector: box.selector,
                ruleId: "allowance-expired",
                severity: "fail",
                message: "Rendered UI Audit allowance has expired.",
                allowance,
              });
            }
          }
        }

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

            const explicitMinGaps = [a.specs.minGap, b.specs.minGap].filter((value) => Number.isFinite(value));
            const pairScale = activeSlide ? scale : 1;
            const pairMinGap = explicitMinGaps.length
              ? Math.max(...explicitMinGaps) * pairScale
              : defaultMinGap;

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
              if (gap >= 0 && gap < pairMinGap) {
                tightSpacing.push({ direction: "vertical", a, b, gap: Math.round(gap), minGap: Math.round(pairMinGap) });
              }
            }

            if (yOverlapRatio > 0.2 && xOverlap <= 0) {
              const gap = Math.max(a.left, b.left) - Math.min(a.right, b.right);
              if (gap >= 0 && gap < pairMinGap) {
                tightSpacing.push({ direction: "horizontal", a, b, gap: Math.round(gap), minGap: Math.round(pairMinGap) });
              }
            }
          }
        }

        function samplePoints(rect, count) {
          const perAxis = Math.max(2, Math.round(Math.sqrt(Math.max(4, count || 9))));
          const points = [];
          for (let yi = 0; yi < perAxis; yi += 1) {
            for (let xi = 0; xi < perAxis; xi += 1) {
              const px = (xi + 1) / (perAxis + 1);
              const py = (yi + 1) / (perAxis + 1);
              points.push({
                x: rect.left + rect.width * px,
                y: rect.top + rect.height * py,
              });
            }
          }
          return points;
        }

        function elementName(el) {
          if (!el) return "";
          const cls = typeof el.className === "string" && el.className.trim()
            ? `.${el.className.trim().replace(/\s+/g, ".")}`
            : "";
          const check = el.getAttribute?.("data-ud-check") || el.getAttribute?.("data-check") || "";
          return `${el.tagName.toLowerCase()}${cls}${check ? `[${check}]` : ""}`;
        }

        if (occlusionEnabled) {
          const originalScroll = { x: window.scrollX, y: window.scrollY };

          for (let index = 0; index < nodes.length; index += 1) {
            const el = nodes[index];
            const box = boxes[index];
            if (box.invisible) continue;

            const absoluteTop = box.top + originalScroll.y;
            const absoluteLeft = box.left + originalScroll.x;
            const targetY = Math.max(0, absoluteTop - Math.max(24, (window.innerHeight - box.height) / 2));
            const targetX = Math.max(0, absoluteLeft - Math.max(24, (window.innerWidth - box.width) / 2));
            window.scrollTo(targetX, targetY);
            await waitForPaint();

            const rect = el.getBoundingClientRect();
            const coveredSamples = [];
            for (const point of samplePoints(rect, occlusionSamples)) {
              if (point.x < 0 || point.y < 0 || point.x > window.innerWidth || point.y > window.innerHeight) continue;
              const stack = document.elementsFromPoint(point.x, point.y);
              const top = stack[0];
              const ok = top === el || el.contains(top);
              if (!ok) {
                coveredSamples.push({
                  x: Math.round(point.x),
                  y: Math.round(point.y),
                  top: elementName(top),
                });
              }
            }

            if (coveredSamples.length > 0) {
              occluded.push({
                label: box.label,
                selector: box.selector,
                text: box.text,
                allowed: box.allowsOcclusion,
                allowance: box.allowsOcclusion ? box.allowance : null,
                rect: {
                  left: Math.round(rect.left),
                  top: Math.round(rect.top),
                  right: Math.round(rect.right),
                  bottom: Math.round(rect.bottom),
                  width: Math.round(rect.width),
                  height: Math.round(rect.height),
                },
                coveredSamples,
                sampleCount: samplePoints(rect, occlusionSamples).length,
              });
            }
          }

          window.scrollTo(originalScroll.x, originalScroll.y);
          await waitForPaint();
        }

        const overflowTolerance = 4;
        const doc = document.documentElement;
        const body = document.body;
        const overflowDelta = Math.max(
          0,
          doc.scrollWidth - doc.clientWidth,
          body ? body.scrollWidth - window.innerWidth : 0,
        );
        const overflowCandidates = Array.from(document.querySelectorAll("body *"))
          .filter((el) => isVisibleElement(el))
          .map((el) => {
            const rect = el.getBoundingClientRect();
            const style = getComputedStyle(el);
            return {
              selector: selectorFor(el),
              tag: el.tagName.toLowerCase(),
              text: (el.textContent || "").replace(/\s+/g, " ").trim().slice(0, 80),
              rect: rectJson(rect),
              position: style.position,
              zIndex: style.zIndex,
              pointerEvents: style.pointerEvents,
              overflowAmount: Math.max(0, rect.right - window.innerWidth, -rect.left),
            };
          })
          .filter((item) => item.overflowAmount > overflowTolerance)
          .sort((a, b) => b.overflowAmount - a.overflowAmount)
          .slice(0, 12);

        const interactiveElements = Array.from(document.querySelectorAll("body *"))
          .filter((el) => isInteractive(el) && isVisibleElement(el))
          .map((el) => {
            const rect = el.getBoundingClientRect();
            const name = accessibleNameHeuristic(el);
            return {
              selector: selectorFor(el),
              tag: el.tagName.toLowerCase(),
              role: el.getAttribute("role") || "",
              text: (el.textContent || "").replace(/\s+/g, " ").trim().slice(0, 80),
              accessibleName: name.slice(0, 120),
              rect: rectJson(rect),
              missingAccessibleName: !name,
              smallTargetFail: rect.width < 24 || rect.height < 24,
              smallTargetWarn: !(rect.width < 24 || rect.height < 24) && (rect.width < 44 || rect.height < 44),
            };
          });

        return {
          title: activeSlide?.dataset?.title || document.title || "",
          markerCount: boxes.length,
          pageFacts: {
            horizontalOverflow: overflowDelta > 0
              ? [{
                  delta: Math.round(overflowDelta),
                  severity: overflowDelta > overflowTolerance ? "fail" : "warn",
                  candidates: overflowCandidates,
                }]
              : [],
          },
          interactiveFacts: {
            visibleCount: interactiveElements.length,
            missingAccessibleNames: interactiveElements.filter((item) => item.missingAccessibleName),
            smallTargetsFail: interactiveElements.filter((item) => item.smallTargetFail),
            smallTargetsWarn: interactiveElements.filter((item) => item.smallTargetWarn),
          },
          outside,
          clipped,
          invisible,
          collisions,
          occluded,
          tightSpacing,
          lineFailures,
          alignmentFailures,
          allowanceGovernance,
        };
      },
      {
        slideSelector: args.slideSelector,
        markerSelector: args.selector,
        minSpacingDesignPx,
        pageMinSpacingPx,
        occlusionEnabled,
        occlusionSamples,
      },
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

let findingIndex = 0;

function roundRectFromBox(box) {
  if (!box) return null;
  if (box.rect) return box.rect;
  return {
    x: Math.round(box.left || 0),
    y: Math.round(box.top || 0),
    width: Math.round(box.width || 0),
    height: Math.round(box.height || 0),
    right: Math.round(box.right || 0),
    bottom: Math.round(box.bottom || 0),
  };
}

function targetFrom(item) {
  if (!item) return null;
  return {
    selector: item.selector || item.label || "",
    tagName: String(item.tag || item.tagName || "").toLowerCase(),
    role: item.role || "",
    text: item.text || "",
  };
}

function addFinding(result, ruleId, severity, message, details = {}) {
  const allowed = Boolean(details.allowed);
  const finding = {
    id: `${result.viewport}:${result.frame}:${ruleId}:${findingIndex += 1}`,
    ruleId,
    severity,
    message,
    viewport: {
      name: result.viewport,
      width: viewports.find((viewport) => viewport.name === result.viewport)?.width || null,
      height: viewports.find((viewport) => viewport.name === result.viewport)?.height || null,
    },
    frame: result.frame,
    selector: details.selector || details.zone || "",
    zone: details.zone || "",
    target: details.target || null,
    bbox: details.bbox || null,
    evidence: details.evidence || {},
    allowed,
    allowance: details.allowance || null,
  };
  report.findings.push(finding);
  return finding;
}

for (const result of report.results) {
  report.summary.checkedZones += result.markerCount || 0;
  for (const overflow of result.pageFacts?.horizontalOverflow || []) {
    report.facts.page.horizontalOverflow.push({ viewport: result.viewport, frame: result.frame, ...overflow });
    addFinding(result, "horizontal-overflow", overflow.severity, `Page has horizontal overflow of ${overflow.delta}px.`, {
      evidence: { actual: { delta: overflow.delta }, expected: { maxDelta: 4 }, candidates: overflow.candidates },
    });
  }

  const interactiveFacts = result.interactiveFacts || {};
  report.facts.interactive.visibleCount += interactiveFacts.visibleCount || 0;
  report.facts.interactive.smallTargets +=
    (interactiveFacts.smallTargetsFail?.length || 0) + (interactiveFacts.smallTargetsWarn?.length || 0);
  report.facts.interactive.missingAccessibleNames += interactiveFacts.missingAccessibleNames?.length || 0;

  for (const item of interactiveFacts.missingAccessibleNames || []) {
    addFinding(result, "missing-accessible-name", "fail", "Visible interactive control has no obvious accessible name.", {
      selector: item.selector,
      target: targetFrom(item),
      bbox: item.rect,
      evidence: { expected: { accessibleName: "non-empty" }, actual: { accessibleName: "" } },
    });
  }
  for (const item of interactiveFacts.smallTargetsFail || []) {
    addFinding(result, "target-size", "fail", "Visible interactive target is smaller than 24x24 CSS px.", {
      selector: item.selector,
      target: targetFrom(item),
      bbox: item.rect,
      evidence: { expected: { minWidth: 24, minHeight: 24 }, actual: { width: item.rect.width, height: item.rect.height } },
    });
  }
  for (const item of interactiveFacts.smallTargetsWarn || []) {
    addFinding(result, "target-size-comfort", "warn", "Visible interactive target is below the 44x44 comfort size.", {
      selector: item.selector,
      target: targetFrom(item),
      bbox: item.rect,
      evidence: { expected: { comfortWidth: 44, comfortHeight: 44 }, actual: { width: item.rect.width, height: item.rect.height } },
    });
  }

  if (result.slideCount > 0 && result.thumbCount > 0 && result.slideCount !== result.thumbCount) {
    addFinding(result, "slide-navigation-mismatch", "fail", "Slide count and thumbnail count differ.", {
      evidence: { actual: { slideCount: result.slideCount, thumbCount: result.thumbCount } },
    });
  }
  if (result.markerCount === 0) {
    addFinding(result, "missing-markers", "fail", "No data-ud-check or data-check semantic zones were found.", {
      evidence: { expected: { markerCount: "> 0" }, actual: { markerCount: 0 } },
    });
  }
  for (const box of result.outside || []) {
    addFinding(result, "out-of-bounds", "fail", `Marked zone ${box.label} is outside the active page or slide bounds.`, {
      selector: box.selector,
      zone: box.label,
      target: targetFrom(box),
      bbox: roundRectFromBox(box),
    });
  }
  for (const box of result.clipped || []) {
    addFinding(result, "clipping", "fail", `Marked zone ${box.label} clips rendered content.`, {
      selector: box.selector,
      zone: box.label,
      target: targetFrom(box),
      bbox: roundRectFromBox(box),
      evidence: { lineCount: box.lineCount, text: box.text },
    });
  }
  for (const box of result.invisible || []) {
    addFinding(result, "invisible-zone", "fail", `Marked zone ${box.label} is invisible.`, {
      selector: box.selector,
      zone: box.label,
      target: targetFrom(box),
      bbox: roundRectFromBox(box),
    });
  }
  for (const collision of result.collisions || []) {
    addFinding(result, "collision", "fail", `Marked zones ${collision.a.label} and ${collision.b.label} overlap.`, {
      zone: `${collision.a.label} / ${collision.b.label}`,
      bbox: roundRectFromBox(collision.a),
      evidence: {
        a: { selector: collision.a.selector, bbox: roundRectFromBox(collision.a), text: collision.a.text },
        b: { selector: collision.b.selector, bbox: roundRectFromBox(collision.b), text: collision.b.text },
        overlap: { x: collision.xOverlap, y: collision.yOverlap },
      },
    });
  }
  for (const item of result.occluded || []) {
    addFinding(
      result,
      "occlusion",
      item.allowed ? "warn" : "fail",
      `Marked zone ${item.label} is covered by another rendered element.`,
      {
        selector: item.selector,
        zone: item.label,
        bbox: item.rect,
        evidence: { coveredSamples: item.coveredSamples, sampleCount: item.sampleCount },
        allowed: item.allowed,
        allowance: item.allowance,
      },
    );
  }
  for (const spacing of result.tightSpacing || []) {
    addFinding(result, "tight-spacing", "fail", `Marked zones ${spacing.a.label} and ${spacing.b.label} are too close.`, {
      zone: `${spacing.a.label} / ${spacing.b.label}`,
      bbox: roundRectFromBox(spacing.a),
      evidence: {
        direction: spacing.direction,
        gap: spacing.gap,
        minGap: spacing.minGap,
        a: { selector: spacing.a.selector, bbox: roundRectFromBox(spacing.a), text: spacing.a.text },
        b: { selector: spacing.b.selector, bbox: roundRectFromBox(spacing.b), text: spacing.b.text },
      },
    });
  }
  for (const lineFailure of result.lineFailures || []) {
    addFinding(result, "line-count", "fail", `Marked zone ${lineFailure.label} violates declared line count.`, {
      zone: lineFailure.label,
      evidence: lineFailure,
    });
  }
  for (const alignmentFailure of result.alignmentFailures || []) {
    addFinding(result, "alignment", "fail", `Marked zone ${alignmentFailure.label} violates declared alignment.`, {
      zone: alignmentFailure.label,
      evidence: alignmentFailure,
    });
  }
  for (const allowanceIssue of result.allowanceGovernance || []) {
    addFinding(result, allowanceIssue.ruleId, allowanceIssue.severity, allowanceIssue.message, {
      selector: allowanceIssue.selector,
      zone: allowanceIssue.label,
      allowance: allowanceIssue.allowance,
      evidence: { allowance: allowanceIssue.allowance },
    });
  }
}

report.failures = report.results.filter(
  (result) =>
    (result.slideCount > 0 && result.thumbCount > 0 && result.slideCount !== result.thumbCount) ||
    result.markerCount === 0 ||
    (result.pageFacts?.horizontalOverflow || []).some((item) => item.severity === "fail") ||
    (result.interactiveFacts?.missingAccessibleNames || []).length > 0 ||
    (result.interactiveFacts?.smallTargetsFail || []).length > 0 ||
    result.outside.length > 0 ||
    result.clipped.length > 0 ||
    result.invisible.length > 0 ||
    result.collisions.length > 0 ||
    result.occluded.some((item) => !item.allowed) ||
    result.tightSpacing.length > 0 ||
    result.lineFailures.length > 0 ||
    result.alignmentFailures.length > 0 ||
    result.allowanceGovernance.some((item) => item.severity === "fail"),
);

report.summary.findings = report.findings.length;
report.summary.failures = report.findings.filter((finding) => finding.severity === "fail" && !finding.allowed).length;
report.summary.warnings = report.findings.filter((finding) => finding.severity === "warn").length;
report.summary.infos = report.findings.filter((finding) => finding.severity === "info").length;
report.summary.allowed = report.findings.filter((finding) => finding.allowed).length;
report.status = report.summary.failures > 0 ? "fail" : report.summary.warnings > 0 ? "warn" : "pass";

writeFileSync(reportPath, JSON.stringify(report, null, 2));

const summary = {
  schemaVersion: report.schemaVersion,
  auditKind: report.auditKind,
  status: report.status,
  checked: report.results.length,
  findings: report.summary.findings,
  failures: report.summary.failures,
  warnings: report.summary.warnings,
  allowed: report.summary.allowed,
  reportPath,
  screenshotsDir,
  firstFindings: report.findings.slice(0, 8).map((finding) => ({
    id: finding.id,
    ruleId: finding.ruleId,
    severity: finding.severity,
    viewport: finding.viewport.name,
    frame: finding.frame,
    selector: finding.selector,
    message: finding.message,
    allowed: finding.allowed,
  })),
  firstFailures: report.failures.slice(0, 8).map((failure) => ({
    viewport: failure.viewport,
    frame: failure.frame,
    title: failure.title,
    markerCount: failure.markerCount,
    outside: failure.outside.length,
    clipped: failure.clipped.length,
    invisible: failure.invisible.length,
    collisions: failure.collisions.length,
    occluded: failure.occluded.length,
    tightSpacing: failure.tightSpacing.length,
    lineFailures: failure.lineFailures.length,
    alignmentFailures: failure.alignmentFailures.length,
    horizontalOverflow: (failure.pageFacts?.horizontalOverflow || []).filter((item) => item.severity === "fail").length,
    missingAccessibleNames: failure.interactiveFacts?.missingAccessibleNames?.length || 0,
    smallTargetsFail: failure.interactiveFacts?.smallTargetsFail?.length || 0,
    allowanceGovernanceFailures: failure.allowanceGovernance?.filter((item) => item.severity === "fail").length || 0,
  })),
};

console.log(JSON.stringify(summary, null, 2));
process.exit(report.summary.failures > 0 ? 1 : 0);
