#!/usr/bin/env node
import { existsSync, mkdirSync, readdirSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import path from "node:path";
import process from "node:process";

function parseArgs(argv) {
  const args = {
    selector: "[data-ud-motion], [data-motion-contract]",
    wait: 700,
    viewports: "desktop=1440x900,mobile=390x844",
    samples: "0,0.25,0.5,0.75,1",
    tolerance: 0.12,
    focusAt: "auto",
    focusMin: 0.95,
    focusWindow: 64,
    entryMin: 0.5,
    exitAt: "bottom 60%",
    exitMin: 0.95,
    operationTimeout: 15000,
    hardTimeout: 90000,
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

function parseSamples(value) {
  return String(value)
    .split(",")
    .map((n) => Number.parseFloat(n))
    .filter((n) => Number.isFinite(n))
    .map((n) => Math.max(0, Math.min(1, n)));
}

async function loadPlaywright() {
  const runtimePlaywright = path.resolve(
    path.dirname(process.execPath),
    "..",
    "node_modules",
    "playwright",
    "index.mjs",
  );
  const nodePathPlaywright = String(process.env.NODE_PATH || "")
    .split(path.delimiter)
    .filter(Boolean)
    .map((entry) => path.resolve(entry, "playwright", "index.mjs"));
  const codexRuntimePlaywright = [];
  const codexRuntimeRoot = path.resolve(homedir(), ".cache", "codex-runtimes");
  const primaryRuntimePlaywright = path.resolve(
    codexRuntimeRoot,
    "codex-primary-runtime",
    "dependencies",
    "node",
    "node_modules",
    "playwright",
    "index.mjs",
  );
  codexRuntimePlaywright.push(primaryRuntimePlaywright);
  try {
    for (const name of readdirSync(codexRuntimeRoot)) {
      const candidate = path.resolve(
        codexRuntimeRoot,
        name,
        "dependencies",
        "node",
        "node_modules",
        "playwright",
        "index.mjs",
      );
      if (existsSync(candidate)) codexRuntimePlaywright.push(candidate);
    }
  } catch {
    // Codex runtime dependencies are optional outside Codex Desktop/CLI.
  }
  const candidates = [
    process.env.PLAYWRIGHT_MODULE,
    "playwright",
    path.resolve(process.cwd(), "node_modules", "playwright", "index.mjs"),
    runtimePlaywright,
    ...nodePathPlaywright,
    ...codexRuntimePlaywright,
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
    "Usage: node scripts/validate_motion_contract.mjs --input artifact.html [--out out-dir] [--viewports desktop=1440x900,mobile=390x844] [--samples 0,0.25,0.5,0.75,1] [--wait 700]",
  );
  process.exit(2);
}

const inputPath = path.resolve(String(args.input));
const outputDir = path.resolve(String(args.out || path.join(path.dirname(inputPath), "ultimate-design-motion-check")));
const reportPath = path.join(outputDir, "motion-validation-report.json");
const screenshotsDir = path.join(outputDir, "screenshots");
const viewports = parseViewports(args.viewports);
const defaultSamples = parseSamples(args.samples);
const defaultTolerance = Number(args.tolerance || 0.12);
const defaultFocusAt = String(args.focusAt || args["focus-at"] || "auto");
const defaultFocusMin = Number(args.focusMin || args["focus-min"] || 0.95);
const defaultFocusWindow = Number(args.focusWindow || args["focus-window"] || 64);
const defaultEntryMin = Number(args.entryMin || args["entry-min"] || 0.5);
const defaultExitAt = String(args.exitAt || args["exit-at"] || "bottom 60%");
const defaultExitMin = Number(args.exitMin || args["exit-min"] || 0.95);
const sampleWaitMs = Number(args.wait || args["wait-ms"] || 700);
const operationTimeoutMs = Number(args.operationTimeout || args["operation-timeout"] || 15000);
const hardTimeoutMs = Number(args.hardTimeout || args["hard-timeout"] || 90000);

mkdirSync(screenshotsDir, { recursive: true });

const { chromium } = await loadPlaywright();
const browser = await launchChromium(chromium, args.browserPath);

const report = {
  inputPath,
  checkedAt: new Date().toISOString(),
  selector: args.selector,
  defaultSamples,
  defaultTolerance,
  defaultFocusAt,
  defaultFocusMin,
  defaultFocusWindow,
  defaultEntryMin,
  defaultExitAt,
  defaultExitMin,
  sampleWaitMs,
  viewports,
  results: [],
  reducedMotionResults: [],
};

const watchdog = setTimeout(() => {
  report.passed = false;
  report.runtimeError = {
    type: "hard-timeout",
    message: `Motion validation exceeded ${hardTimeoutMs}ms.`,
  };
  try {
    writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
  } catch {
    // Best-effort report write before forced exit.
  }
  void browser.close().finally(() => process.exit(124));
}, hardTimeoutMs);

async function preparePage(page) {
  page.setDefaultTimeout(operationTimeoutMs);
  page.setDefaultNavigationTimeout(operationTimeoutMs);
  await page.addInitScript(() => {
    window.__udMotionFrames = [];
    const sample = () => {
      const nodes = Array.from(
        document.querySelectorAll(
          '[data-ud-motion-type="reveal"][data-ud-motion-no-flash="true"], [data-motion-type="reveal"][data-motion-no-flash="true"]',
        ),
      );
      window.__udMotionFrames.push({
        t: performance.now(),
        nodes: nodes.map((el, index) => {
          const r = el.getBoundingClientRect();
          const style = getComputedStyle(el);
          return {
            index,
            id: el.getAttribute("data-ud-motion") || el.getAttribute("data-motion-contract") || `reveal-${index}`,
            opacity: Number.parseFloat(style.opacity || "1"),
            visibility: style.visibility,
            display: style.display,
            visibleBox: r.width > 0 && r.height > 0,
          };
        }),
      });
      if (performance.now() < 1400) requestAnimationFrame(sample);
    };
    requestAnimationFrame(sample);
  });
  await page.goto(`file://${inputPath}`, { waitUntil: "domcontentloaded", timeout: operationTimeoutMs });
  await page.addStyleTag({
    content: "html, body { scroll-behavior: auto !important; }",
  });
  await page.waitForTimeout(sampleWaitMs);
}

async function readSvgReveal(page, selector, contract) {
  return page.evaluate(
    ({ selector, contract }) => {
      const target = Array.from(document.querySelectorAll(selector))[contract.index];
      if (!target) return { passed: false, reason: "Motion target not found" };
      const style = getComputedStyle(target);
      const dashArrayRaw = style.strokeDasharray || target.getAttribute("stroke-dasharray") || "";
      const dashOffsetRaw = style.strokeDashoffset || target.getAttribute("stroke-dashoffset") || "";
      const dashArray = Number.parseFloat(String(dashArrayRaw).split(/[,\s]+/)[0]);
      const dashOffset = Number.parseFloat(String(dashOffsetRaw).split(/[,\s]+/)[0]);
      const fallbackLength = typeof target.getTotalLength === "function" ? target.getTotalLength() : 1;
      const length = Number.isFinite(dashArray) && dashArray > 0 ? dashArray : fallbackLength;
      if (!Number.isFinite(dashOffset)) {
        return {
          passed: false,
          reason: "Could not read strokeDashoffset",
          dashArrayRaw,
          dashOffsetRaw,
        };
      }
      const reveal = Math.max(0, Math.min(1, 1 - dashOffset / length));
      return { passed: true, reveal, dashArray: length, dashOffset, dashArrayRaw, dashOffsetRaw };
    },
    { selector, contract },
  );
}

for (const viewport of viewports) {
  const page = await browser.newPage({ viewport });
  await preparePage(page);

  const contracts = await page.evaluate(
    ({ selector, defaultSamples, defaultTolerance, defaultFocusAt, defaultFocusMin, defaultFocusWindow, defaultEntryMin, defaultExitAt, defaultExitMin }) => {
      const nodes = Array.from(document.querySelectorAll(selector));

      function attr(el, names, fallback = "") {
        for (const name of names) {
          const value = el.getAttribute(name);
          if (value !== null && value !== "") return value;
        }
        return fallback;
      }

      function numberAttr(el, names, fallback) {
        const value = attr(el, names, "");
        const parsed = Number.parseFloat(value);
        return Number.isFinite(parsed) ? parsed : fallback;
      }

      function samplesAttr(el) {
        const raw = attr(el, ["data-ud-motion-samples", "data-motion-samples"], "");
        if (!raw) return defaultSamples;
        return raw
          .split(",")
          .map((n) => Number.parseFloat(n))
          .filter((n) => Number.isFinite(n))
          .map((n) => Math.max(0, Math.min(1, n)));
      }

      return nodes.map((el, index) => {
        const rawTriggerModel = attr(el, ["data-ud-motion-trigger-model", "data-motion-trigger-model"], "scroll");
        const triggerModel =
          rawTriggerModel === "load" ? "entry-play" :
          rawTriggerModel === "view" ? "view-entry" :
          rawTriggerModel === "responsive-entry" ? "entry-or-view" :
          rawTriggerModel;
        return {
        index,
        id: attr(el, ["data-ud-motion", "data-motion-contract"], `motion-${index}`),
        type: attr(el, ["data-ud-motion-type", "data-motion-type"], "svg-draw"),
        triggerModel,
        triggerSelector: attr(el, ["data-ud-motion-trigger", "data-motion-trigger"], ""),
        endTriggerSelector: attr(el, ["data-ud-motion-end-trigger", "data-motion-end-trigger"], ""),
        subjectSelector: attr(el, ["data-ud-motion-subject", "data-motion-subject"], ""),
        start: attr(el, ["data-ud-motion-start", "data-motion-start"], "top 80%"),
        end: attr(el, ["data-ud-motion-end", "data-motion-end"], "bottom 20%"),
        focusComplete: attr(el, ["data-ud-motion-focus-complete", "data-motion-focus-complete"], "true") !== "false",
        focusAt: attr(el, ["data-ud-motion-focus-at", "data-motion-focus-at"], defaultFocusAt),
        focusMin: numberAttr(el, ["data-ud-motion-focus-min", "data-motion-focus-min"], defaultFocusMin),
        focusWindow: numberAttr(el, ["data-ud-motion-focus-window", "data-motion-focus-window"], defaultFocusWindow),
        entryMin: numberAttr(el, ["data-ud-motion-entry-min", "data-motion-entry-min"], defaultEntryMin),
        exitComplete: attr(el, ["data-ud-motion-exit-complete", "data-motion-exit-complete"], "true") !== "false",
        exitAt: attr(el, ["data-ud-motion-exit-at", "data-motion-exit-at"], defaultExitAt),
        exitMin: numberAttr(el, ["data-ud-motion-exit-min", "data-motion-exit-min"], defaultExitMin),
        samples: samplesAttr(el),
        tolerance: numberAttr(el, ["data-ud-motion-tolerance", "data-motion-tolerance"], defaultTolerance),
        reduced: attr(el, ["data-ud-motion-reduced", "data-motion-reduced"], "complete"),
        noFlash: attr(el, ["data-ud-motion-no-flash", "data-motion-no-flash"], "") === "true",
        };
      });
    },
    { selector: args.selector, defaultSamples, defaultTolerance, defaultFocusAt, defaultFocusMin, defaultFocusWindow, defaultEntryMin, defaultExitAt, defaultExitMin },
  );

  if (contracts.length === 0) {
    report.results.push({
      viewport: viewport.name,
      passed: false,
      reason: `No motion contract markers found for selector ${args.selector}`,
    });
  }

  const revealFrames = await page.evaluate(() => window.__udMotionFrames || []);
  const revealFailures = await page.evaluate(() => {
    const frames = window.__udMotionFrames || [];
    const byId = new Map();
    for (const frame of frames) {
      for (const node of frame.nodes) {
        const visible =
          node.display !== "none" &&
          node.visibility !== "hidden" &&
          node.opacity > 0.05 &&
          node.visibleBox;
        if (!byId.has(node.id)) byId.set(node.id, []);
        byId.get(node.id).push(visible);
      }
    }
    const failures = [];
    for (const [id, states] of byId.entries()) {
      let sawVisible = false;
      let sawHiddenAfterVisible = false;
      let sawVisibleAfterHidden = false;
      for (const visible of states) {
        if (visible && !sawHiddenAfterVisible) sawVisible = true;
        if (!visible && sawVisible) sawHiddenAfterVisible = true;
        if (visible && sawHiddenAfterVisible) sawVisibleAfterHidden = true;
      }
      if (sawVisibleAfterHidden) failures.push({ id, states });
    }
    return failures;
  });

  for (const contract of contracts) {
    if (contract.type === "reveal") {
      const failed = revealFailures.find((entry) => entry.id === contract.id);
      report.results.push({
        viewport: viewport.name,
        id: contract.id,
        type: contract.type,
        passed: !failed,
        framesSampled: revealFrames.length,
        failures: failed ? [failed] : [],
      });
      continue;
    }

    if (contract.type !== "svg-draw") {
      report.results.push({
        viewport: viewport.name,
        id: contract.id,
        type: contract.type,
        passed: false,
        reason: `Unsupported motion contract type: ${contract.type}`,
      });
      continue;
    }

    const setup = await page.evaluate(
      ({ selector, contract }) => {
        const target = Array.from(document.querySelectorAll(selector))[contract.index];
        if (!target) return { passed: false, reason: "Motion target not found" };
        const trigger = contract.triggerSelector ? document.querySelector(contract.triggerSelector) : target;
        if (!trigger) {
          return {
            passed: false,
            reason: "Trigger target not found",
            triggerSelector: contract.triggerSelector,
          };
        }

        function pointOffset(keyword, size) {
          if (keyword === "top" || keyword === "left") return 0;
          if (keyword === "center") return size / 2;
          if (keyword === "bottom" || keyword === "right") return size;
          if (keyword.endsWith("%")) return (Number.parseFloat(keyword) / 100) * size;
          const parsed = Number.parseFloat(keyword);
          return Number.isFinite(parsed) ? parsed : 0;
        }

        function viewportOffset(keyword) {
          const height = window.innerHeight;
          if (keyword === "top") return 0;
          if (keyword === "center") return height / 2;
          if (keyword === "bottom") return height;
          if (keyword.endsWith("%")) return (Number.parseFloat(keyword) / 100) * height;
          const parsed = Number.parseFloat(keyword);
          return Number.isFinite(parsed) ? parsed : 0;
        }

        function parsePosition(value) {
          const parts = String(value || "").trim().split(/\s+/);
          return { triggerPoint: parts[0] || "top", viewportPoint: parts[1] || "bottom" };
        }

        function absoluteScrollFor(value, element = trigger) {
          if (String(value).startsWith("+=")) {
            return null;
          }
          const parsed = parsePosition(value);
          const rect = element.getBoundingClientRect();
          const absoluteTop = rect.top + window.scrollY;
          return absoluteTop + pointOffset(parsed.triggerPoint, rect.height) - viewportOffset(parsed.viewportPoint);
        }

        function absoluteScrollForElementPosition(element, value) {
          const parsed = parsePosition(value);
          const rect = element.getBoundingClientRect();
          const absoluteTop = rect.top + window.scrollY;
          return absoluteTop + pointOffset(parsed.triggerPoint, rect.height) - viewportOffset(parsed.viewportPoint);
        }

        function focusScrollForSubject(element, value) {
          if (value && value !== "auto") {
            return {
              y: absoluteScrollForElementPosition(element, value),
              rule: value,
            };
          }
          const rect = element.getBoundingClientRect();
          const absoluteTop = rect.top + window.scrollY;
          if (rect.height <= window.innerHeight) {
            return {
              y: absoluteTop + rect.height - window.innerHeight,
              rule: "first-full-frame",
            };
          }
          return {
            y: absoluteTop + rect.height / 2 - window.innerHeight / 2,
            rule: "center-focus",
          };
        }

        const endTrigger = contract.endTriggerSelector ? document.querySelector(contract.endTriggerSelector) : trigger;
        if (!endTrigger) {
          return {
            passed: false,
            reason: "End trigger target not found",
            endTriggerSelector: contract.endTriggerSelector,
          };
        }

        let startY = absoluteScrollFor(contract.start, trigger);
        let endY = String(contract.end).startsWith("+=")
          ? startY + Number.parseFloat(String(contract.end).slice(2))
          : absoluteScrollFor(contract.end, endTrigger);
        const maxScroll = Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
        startY = Math.max(0, Math.min(maxScroll, startY));
        endY = Math.max(0, Math.min(maxScroll, endY));
        if (endY <= startY) endY = Math.min(maxScroll, startY + Math.max(1, trigger.getBoundingClientRect().height));
        const subject = contract.subjectSelector
          ? document.querySelector(contract.subjectSelector)
          : target.ownerSVGElement || target.closest?.("svg") || target;
        if (!subject) {
          return {
            passed: false,
            reason: "Visual subject not found",
            subjectSelector: contract.subjectSelector,
          };
        }
        const subjectRect = subject.getBoundingClientRect();
        const focus = focusScrollForSubject(subject, contract.focusAt);
        let focusCompleteY = Math.max(0, Math.min(maxScroll, focus.y));
        const initialVisiblePx = Math.max(
          0,
          Math.min(subjectRect.height, window.innerHeight - Math.max(0, subjectRect.top + window.scrollY)),
        );
        const initialVisibilityRatio = subjectRect.height > 0
          ? Math.max(0, Math.min(1, initialVisiblePx / subjectRect.height))
          : 0;
        const effectiveTriggerModel = contract.triggerModel === "entry-or-view"
          ? initialVisibilityRatio >= contract.entryMin ? "entry-play" : "view-entry"
          : contract.triggerModel;
        const focusDelta = endY - focusCompleteY;
        const focusTiming = effectiveTriggerModel === "scroll"
          ? {
              delta: focusDelta,
              tolerance: contract.focusWindow,
              passed: Math.abs(focusDelta) <= contract.focusWindow,
              reason: focusDelta < 0 ? "range ends before focus" : "range ends after focus",
            }
          : {
              delta: null,
              tolerance: contract.focusWindow,
              passed: true,
              reason: "not scroll-linked",
            };
        const entryPlayVisibleOnArrival = effectiveTriggerModel !== "entry-play" ||
          initialVisibilityRatio >= contract.entryMin;
        let exitCompleteY = absoluteScrollForElementPosition(subject, contract.exitAt);
        exitCompleteY = Math.max(0, Math.min(maxScroll, exitCompleteY));
        return {
          passed: true,
          startY,
          endY,
          maxScroll,
          triggerSelector: contract.triggerSelector || "motion target",
          triggerModel: contract.triggerModel,
          effectiveTriggerModel,
          endTriggerSelector: contract.endTriggerSelector || contract.triggerSelector || "motion target",
          subjectSelector: contract.subjectSelector || "nearest svg",
          subjectBox: {
            top: subjectRect.top + window.scrollY,
            height: subjectRect.height,
          },
          initialVisibilityRatio,
          entryMin: contract.entryMin,
          entryPlayVisibleOnArrival,
          focusCompleteY,
          focusAt: contract.focusAt,
          focusRule: focus.rule,
          focusTiming,
          endBeforeFocusComplete: effectiveTriggerModel !== "scroll" || endY <= focusCompleteY + 1,
          exitCompleteY,
          exitAt: contract.exitAt,
          endBeforeExitComplete: endY <= exitCompleteY + 1,
        };
      },
      { selector: args.selector, contract },
    );

    if (!setup.passed) {
      report.results.push({
        viewport: viewport.name,
        id: contract.id,
        type: contract.type,
        ...setup,
      });
      continue;
    }

    const samples = [];
    if (setup.effectiveTriggerModel === "scroll") {
      let lastObserved = -Infinity;
      for (const progress of contract.samples) {
        const scrollY = setup.startY + (setup.endY - setup.startY) * progress;
        await page.evaluate((y) => window.scrollTo(0, y), scrollY);
        await page.waitForTimeout(sampleWaitMs);
        const observed = await readSvgReveal(page, args.selector, contract);
        const delta = observed.passed ? Math.abs(observed.reveal - progress) : Number.POSITIVE_INFINITY;
        const sample = {
          expectedProgress: progress,
          scrollY,
          observedProgress: observed.reveal,
          delta,
          passed: observed.passed && delta <= contract.tolerance && observed.reveal + contract.tolerance >= lastObserved,
          observed,
        };
        if (observed.passed) lastObserved = Math.max(lastObserved, observed.reveal);
        samples.push(sample);
      }
    } else {
      await page.evaluate((y) => window.scrollTo(0, y), setup.focusCompleteY);
      await page.waitForTimeout(sampleWaitMs);
      const observed = await readSvgReveal(page, args.selector, contract);
      samples.push({
        expectedProgress: 1,
        scrollY: setup.focusCompleteY,
        observedProgress: observed.reveal,
        delta: observed.passed ? Math.abs(observed.reveal - 1) : Number.POSITIVE_INFINITY,
        passed: observed.passed && observed.reveal >= contract.focusMin,
        observed,
        triggerModel: contract.triggerModel,
        effectiveTriggerModel: setup.effectiveTriggerModel,
      });
    }

    let focusComplete = null;
    if (contract.focusComplete) {
      await page.evaluate((y) => window.scrollTo(0, y), setup.focusCompleteY);
      await page.waitForTimeout(sampleWaitMs);
      const observed = await readSvgReveal(page, args.selector, contract);
      focusComplete = {
        boundary: setup.focusRule,
        scrollY: setup.focusCompleteY,
        requiredProgress: contract.focusMin,
        observedProgress: observed.reveal,
        observed,
        focusTiming: setup.focusTiming,
        triggerModel: contract.triggerModel,
        effectiveTriggerModel: setup.effectiveTriggerModel,
        entryPlayVisibleOnArrival: setup.entryPlayVisibleOnArrival,
        initialVisibilityRatio: setup.initialVisibilityRatio,
        passed:
          observed.passed &&
          observed.reveal >= contract.focusMin &&
          setup.focusTiming.passed &&
          setup.entryPlayVisibleOnArrival,
      };
    }

    let exitComplete = null;
    if (contract.exitComplete) {
      await page.evaluate((y) => window.scrollTo(0, y), setup.exitCompleteY);
      await page.waitForTimeout(sampleWaitMs);
      const observed = await readSvgReveal(page, args.selector, contract);
      exitComplete = {
        boundary: contract.exitAt,
        scrollY: setup.exitCompleteY,
        requiredProgress: contract.exitMin,
        observedProgress: observed.reveal,
        observed,
        rangeEndBeforeBoundary: setup.effectiveTriggerModel !== "scroll" || setup.endBeforeExitComplete,
        triggerModel: contract.triggerModel,
        effectiveTriggerModel: setup.effectiveTriggerModel,
        passed:
          observed.passed &&
          observed.reveal >= contract.exitMin &&
          (setup.effectiveTriggerModel !== "scroll" || setup.endBeforeExitComplete),
      };
    }

    const screenshotPath = path.join(screenshotsDir, `${viewport.name}-${contract.id}.png`);
    let screenshotError = null;
    try {
      await page.screenshot({ path: screenshotPath, fullPage: true, timeout: operationTimeoutMs });
    } catch (error) {
      screenshotError = error.message;
    }

    report.results.push({
      viewport: viewport.name,
      id: contract.id,
      type: contract.type,
      triggerRange: setup,
      tolerance: contract.tolerance,
      samples,
      focusComplete,
      exitComplete,
      screenshotPath: screenshotError ? null : screenshotPath,
      screenshotError,
      passed:
        samples.every((sample) => sample.passed) &&
        (!focusComplete || focusComplete.passed) &&
        (!exitComplete || exitComplete.passed),
    });
  }

  await page.close();

  const reducedPage = await browser.newPage({ viewport, reducedMotion: "reduce" });
  await preparePage(reducedPage);
  const reducedChecks = await reducedPage.evaluate(
    ({ selector }) => {
      const nodes = Array.from(document.querySelectorAll(selector));
      return nodes.map((target, index) => {
        const id = target.getAttribute("data-ud-motion") || target.getAttribute("data-motion-contract") || `motion-${index}`;
        const type = target.getAttribute("data-ud-motion-type") || target.getAttribute("data-motion-type") || "svg-draw";
        const style = getComputedStyle(target);
        const visible =
          style.display !== "none" &&
          style.visibility !== "hidden" &&
          Number.parseFloat(style.opacity || "1") > 0.05 &&
          target.getBoundingClientRect().width > 0 &&
          target.getBoundingClientRect().height > 0;
        if (type !== "svg-draw") {
          return { id, type, visible, passed: visible };
        }
        const dashArray = Number.parseFloat(String(style.strokeDasharray || "").split(/[,\s]+/)[0]);
        const dashOffset = Number.parseFloat(String(style.strokeDashoffset || "").split(/[,\s]+/)[0]);
        const length = Number.isFinite(dashArray) && dashArray > 0
          ? dashArray
          : typeof target.getTotalLength === "function"
            ? target.getTotalLength()
            : 1;
        const reveal = Number.isFinite(dashOffset) ? Math.max(0, Math.min(1, 1 - dashOffset / length)) : null;
        return {
          id,
          type,
          visible,
          reveal,
          passed: visible && reveal !== null && reveal >= 0.95,
        };
      });
    },
    { selector: args.selector },
  );
  report.reducedMotionResults.push({
    viewport: viewport.name,
    checks: reducedChecks,
    passed: reducedChecks.length > 0 && reducedChecks.every((check) => check.passed),
  });
  await reducedPage.close();
}

await browser.close();
clearTimeout(watchdog);

report.passed =
  report.results.length > 0 &&
  report.results.every((result) => result.passed) &&
  report.reducedMotionResults.every((result) => result.passed);

writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
console.log(JSON.stringify({ passed: report.passed, reportPath }, null, 2));
process.exit(report.passed ? 0 : 1);
