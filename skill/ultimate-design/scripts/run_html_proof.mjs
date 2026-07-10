#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const parsed = { flags: new Set() };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (!arg.startsWith("--")) continue;
    const eq = arg.indexOf("=");
    if (eq >= 0) {
      parsed[arg.slice(2, eq)] = arg.slice(eq + 1);
    } else {
      const key = arg.slice(2);
      const next = argv[i + 1];
      if (next && !next.startsWith("--")) {
        parsed[key] = next;
        i += 1;
      } else {
        parsed.flags.add(key);
        parsed[key] = true;
      }
    }
  }
  return parsed;
}

function tail(text, max = 4000) {
  const value = String(text || "");
  return value.length > max ? value.slice(value.length - max) : value;
}

function commandText(command, args) {
  return [command, ...args].map((part) => (/\s/.test(part) ? JSON.stringify(part) : part)).join(" ");
}

function runStep({ id, label, command, args, cwd, timeoutMs, reportPath }) {
  const startedAtMs = Date.now();
  const startedAt = new Date().toISOString();
  const result = spawnSync(command, args, {
    cwd,
    encoding: "utf8",
    timeout: timeoutMs,
    maxBuffer: 1024 * 1024 * 8,
  });
  const timedOut = result.error?.code === "ETIMEDOUT";
  let exitCode = timedOut ? 124 : result.status ?? (result.error ? 127 : 1);
  let stderrTail = tail(result.stderr || result.error?.message || "");
  let reportFresh = null;
  if (reportPath) {
    reportFresh = existsSync(reportPath) && statSync(reportPath).mtimeMs >= startedAtMs - 1000;
    if (exitCode === 0 && !reportFresh) {
      exitCode = 1;
      stderrTail = tail(`${stderrTail}\nValidator exited 0 without a fresh report: ${reportPath}`);
    }
  }
  return {
    id,
    label,
    status: exitCode === 0 ? "pass" : "fail",
    exitCode,
    timedOut,
    command: commandText(command, args),
    reportPath,
    reportFresh,
    startedAt,
    endedAt: new Date().toISOString(),
    stdoutTail: tail(result.stdout),
    stderrTail,
  };
}

function readJson(filePath) {
  if (!filePath || !existsSync(filePath)) return null;
  try {
    return JSON.parse(readFileSync(filePath, "utf8"));
  } catch {
    return null;
  }
}

function summarizeVisual(report) {
  const findings = Array.isArray(report?.findings) ? report.findings : [];
  return findings.slice(0, 12).map((finding) => ({
    ruleId: finding.ruleId,
    severity: finding.severity,
    viewport: finding.viewport?.name || finding.viewport || "",
    selector: finding.selector || finding.zone || "",
    message: finding.message || "",
  }));
}

function summarizeMotion(report) {
  const results = Array.isArray(report?.results) ? report.results : [];
  const motionFindings = results
    .filter((result) => !result.passed)
    .slice(0, 12)
    .map((result) => {
      const failedSample = Array.isArray(result.samples) ? result.samples.find((sample) => !sample.passed) : null;
      const triggerRange = result.triggerRange || {};
      const focus = result.focusComplete || {};
      const sampleReason = failedSample
        ? `sample ${failedSample.expectedProgress} observed ${failedSample.observedProgress} (delta ${failedSample.delta})`
        : "";
      const focusReason = focus && !focus.passed
        ? `focus-complete observed ${focus.observedProgress}; ${focus.focusTiming?.reason || "focus timing failed"}; for short subjects use data-ud-motion-end="bottom 100%" and keep later boundaries as exit guards`
        : "";
      const visibilityReason = Number.isFinite(triggerRange.initialVisibilityRatio)
        ? `initial visibility ${triggerRange.initialVisibilityRatio}`
        : "";
      return {
        id: result.id,
        viewport: result.viewport || "",
        reason: result.reason || sampleReason || focusReason || result.focusComplete?.focusTiming?.reason || "motion contract failed",
        triggerSelector: result.triggerSelector || triggerRange.triggerSelector || "",
        subjectSelector: triggerRange.subjectSelector || "",
        triggerModel: triggerRange.triggerModel || "",
        focusRule: triggerRange.focusRule || "",
        visibility: visibilityReason,
      };
    });
  const reduced = Array.isArray(report?.reducedMotionResults) ? report.reducedMotionResults : [];
  const reducedFindings = [];
  for (const viewportResult of reduced) {
    for (const check of viewportResult.checks || []) {
      if (!check.passed) {
        reducedFindings.push({
          id: check.id,
          viewport: viewportResult.viewport || "",
          reason: `reduced motion expected visible complete state, observed reveal ${check.reveal}`,
          triggerSelector: "",
          subjectSelector: "",
        });
      }
    }
  }
  return [...motionFindings, ...reducedFindings].slice(0, 12);
}

function enrichStep(step) {
  if (step.id === "rendered-ui-audit") {
    const findings = step.reportFresh ? summarizeVisual(readJson(step.reportPath)) : [];
    if (findings.length) step.firstFindings = findings;
  }
  if (step.id === "motion-contract") {
    const findings = step.reportFresh ? summarizeMotion(readJson(step.reportPath)) : [];
    if (findings.length) step.firstFindings = findings;
  }
}

function writeRepairBrief(report, filePath) {
  const lines = [
    "# Ultimate Design Repair Brief",
    "",
    `Status: ${report.status}`,
    `HTML: ${report.htmlPath}`,
    `DESIGN: ${report.designPath}`,
    "",
  ];
  for (const step of report.steps) {
    lines.push(`## ${step.label}`);
    lines.push(`- Status: ${step.status}`);
    lines.push(`- Exit code: ${step.exitCode}`);
    if (step.reportPath) lines.push(`- Report: ${step.reportPath}`);
    if (step.reportFresh !== null && step.reportFresh !== undefined) lines.push(`- Fresh report: ${step.reportFresh}`);
    if (step.stderrTail) lines.push(`- Error: ${String(step.stderrTail).split("\n").slice(-4).join(" ")}`);
    if (step.stdoutTail && step.status === "fail") {
      lines.push(`- Output: ${String(step.stdoutTail).split("\n").slice(-6).join(" ")}`);
    }
    if (Array.isArray(step.firstFindings) && step.firstFindings.length) {
      lines.push("- First findings:");
      for (const finding of step.firstFindings) {
        const where = [finding.viewport, finding.selector || finding.id].filter(Boolean).join(" ");
        const message = finding.message || finding.reason || "";
        lines.push(`  - ${finding.ruleId || finding.id || "finding"} ${where}: ${message}`);
      }
    }
    lines.push("");
  }
  lines.push("Repair the failing layer, rerun the same proof command, and do not claim success while status is fail.");
  writeFileSync(filePath, `${lines.join("\n")}\n`);
}

const args = parseArgs(process.argv.slice(2));
const htmlPath = path.resolve(String(args.html || "index.html"));
const cwd = path.dirname(htmlPath);
const designPath = path.resolve(cwd, String(args.design || "DESIGN.md"));
const outDir = path.resolve(cwd, String(args.out || ".ultimate-design/proof"));
const viewports = String(args.viewports || "desktop=1440x1000,tablet=768x1000,mobile=390x844");
const spacing = String(args.spacing || "36");
const pageSpacing = String(args["page-spacing"] || args.pageSpacing || "12");
const samples = String(args.samples || "0,0.25,0.5,0.75,1");
const wait = String(args.wait || "500");
const motionWait = String(args["motion-wait"] || "300");
const hardTimeout = String(args["hard-timeout"] || "60000");
const skipDesign = Boolean(args["skip-design"]);
const requireOkfUsage = Boolean(args["require-okf-usage"]);
const timeoutMs = Number(args.timeout || 120000);

mkdirSync(outDir, { recursive: true });

const report = {
  schemaVersion: "ultimate-design.html-proof.v1",
  checkedAt: new Date().toISOString(),
  htmlPath,
  designPath,
  outDir,
  steps: [],
  status: "fail",
};

if (!existsSync(htmlPath)) {
  report.steps.push({
    id: "artifact",
    label: "Visible artifact exists",
    status: "fail",
    exitCode: 1,
    command: "file exists check",
    stderrTail: `Missing HTML artifact: ${htmlPath}`,
  });
} else {
  report.steps.push({
    id: "artifact",
    label: "Visible artifact exists",
    status: "pass",
    exitCode: 0,
    command: "file exists check",
  });
}

if (skipDesign) {
  report.steps.push({
    id: "design-contract",
    label: "Design contract validation",
    status: "skipped",
    exitCode: 0,
    command: "--skip-design",
  });
} else if (!existsSync(designPath)) {
  report.steps.push({
    id: "design-contract",
    label: "Design contract validation",
    status: "fail",
    exitCode: 1,
    command: "file exists check",
    stderrTail: `Missing DESIGN.md: ${designPath}`,
  });
} else {
  report.steps.push(runStep({
    id: "design-contract",
    label: "Design contract validation",
    command: "python3",
    args: [path.join(scriptDir, "validate_design_contract.py"), designPath],
    cwd,
    timeoutMs,
  }));
}

if (requireOkfUsage) {
  if (skipDesign || !existsSync(designPath)) {
    report.steps.push({
      id: "okf-usage",
      label: "OKF decision binding validation",
      status: "fail",
      exitCode: 1,
      command: "--require-okf-usage",
      stderrTail: "OKF usage validation requires an existing DESIGN.md.",
    });
  } else {
    report.steps.push(runStep({
      id: "okf-usage",
      label: "OKF decision binding validation",
      command: "python3",
      args: [path.join(scriptDir, "validate_okf_usage.py"), designPath],
      cwd,
      timeoutMs,
    }));
  }
} else {
  report.steps.push({
    id: "okf-usage",
    label: "OKF decision binding validation",
    status: "skipped",
    exitCode: 0,
    command: "enable with --require-okf-usage in proof/eval runs",
  });
}

if (existsSync(htmlPath)) {
  const visualOut = path.join(outDir, "rendered-ui-audit");
  rmSync(visualOut, { recursive: true, force: true });
  const visualArgs = [
    path.join(scriptDir, "validate_html_visual.mjs"),
    "--input", htmlPath,
    "--out", visualOut,
    "--viewports", viewports,
    "--spacing", spacing,
    "--page-spacing", pageSpacing,
    "--wait", wait,
  ];
  report.steps.push(runStep({
    id: "rendered-ui-audit",
    label: "Rendered UI Audit",
    command: process.execPath,
    args: visualArgs,
    cwd,
    timeoutMs,
    reportPath: path.join(visualOut, "visual-validation-report.json"),
  }));

  const html = readFileSync(htmlPath, "utf8");
  const hasMotionMarkers = /\bdata-(?:ud-motion|motion-contract)\s*=/.test(html);
  if (hasMotionMarkers) {
    const motionOut = path.join(outDir, "motion-audit");
    rmSync(motionOut, { recursive: true, force: true });
    const motionArgs = [
      path.join(scriptDir, "validate_motion_contract.mjs"),
      "--input", htmlPath,
      "--out", motionOut,
      "--viewports", viewports.replace(/tablet=[^,]+,?/, "").replace(/,,/g, ",").replace(/,$/, ""),
      "--samples", samples,
      "--wait", motionWait,
      "--hard-timeout", hardTimeout,
    ];
    report.steps.push(runStep({
      id: "motion-contract",
      label: "Motion Contract Audit",
      command: process.execPath,
      args: motionArgs,
      cwd,
      timeoutMs: Math.max(timeoutMs, Number(hardTimeout) + 10000),
      reportPath: path.join(motionOut, "motion-validation-report.json"),
    }));
  } else {
    report.steps.push({
      id: "motion-contract",
      label: "Motion Contract Audit",
      status: "skipped",
      exitCode: 0,
      command: "no data-ud-motion or data-motion-contract markers found",
    });
  }
}

const activeSteps = report.steps.filter((step) => step.status !== "skipped");
const passed = activeSteps.length > 0 && activeSteps.every((step) => step.status === "pass");
report.status = passed ? "pass" : "fail";
report.summary = {
  passed: report.steps.filter((step) => step.status === "pass").length,
  failed: report.steps.filter((step) => step.status === "fail").length,
  skipped: report.steps.filter((step) => step.status === "skipped").length,
};
report.steps.forEach(enrichStep);

const repairBriefPath = path.join(outDir, "repair-brief.md");
if (!passed) {
  report.repairBriefPath = repairBriefPath;
  writeRepairBrief(report, repairBriefPath);
} else if (existsSync(repairBriefPath)) {
  writeFileSync(
    repairBriefPath,
    [
      "# Ultimate Design Repair Brief",
      "",
      "Status: pass",
      "No repair needed. The latest proof run passed.",
      "",
    ].join("\n"),
  );
}

const reportPath = path.join(outDir, "html-proof-report.json");
writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`);

console.log(JSON.stringify({
  schemaVersion: report.schemaVersion,
  status: report.status,
  summary: report.summary,
  reportPath,
  repairBriefPath: report.repairBriefPath || null,
  steps: report.steps.map((step) => ({
    id: step.id,
    status: step.status,
    exitCode: step.exitCode,
    reportPath: step.reportPath,
    reportFresh: step.reportFresh,
    firstFindings: step.firstFindings,
  })),
}, null, 2));

process.exit(passed ? 0 : 1);
