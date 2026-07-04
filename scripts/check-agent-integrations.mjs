#!/usr/bin/env node
import { existsSync, lstatSync, mkdirSync, mkdtempSync, readlinkSync, rmSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import process from "node:process";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const installer = path.join(repoRoot, "scripts", "install-agent-skill.mjs");

const cases = [
  {
    target: "codex",
    scope: "project",
    dest: [".agents", "skills", "ultimate-design"],
  },
  {
    target: "claude-code",
    scope: "project",
    dest: [".claude", "skills", "ultimate-design"],
  },
  {
    target: "pi-agent",
    scope: "project",
    dest: [".pi", "skills", "ultimate-design"],
  },
];

const keep = process.argv.includes("--keep");
const tempRoot = mkdtempSync(path.join(os.tmpdir(), "ultimate-design-integrations-"));
const results = [];

try {
  for (const item of cases) {
    const cwd = path.join(tempRoot, item.target);
    mkdirSync(cwd, { recursive: true });
    const run = spawnSync(
      process.execPath,
      [installer, "--target", item.target, "--scope", item.scope, "--link"],
      { cwd, encoding: "utf8" },
    );
    if (run.status !== 0) {
      throw new Error(
        `Install failed for ${item.target}\nstdout:\n${run.stdout}\nstderr:\n${run.stderr}`,
      );
    }

    const skillDir = path.join(cwd, ...item.dest);
    const skillFile = path.join(skillDir, "SKILL.md");
    if (!existsSync(skillFile)) {
      throw new Error(`Missing SKILL.md for ${item.target}: ${skillFile}`);
    }
    if (!lstatSync(skillDir).isSymbolicLink()) {
      throw new Error(`Expected symlinked skill directory for ${item.target}: ${skillDir}`);
    }

    results.push({
      target: item.target,
      scope: item.scope,
      destination: skillDir,
      pointsTo: readlinkSync(skillDir),
      hasSkillMd: true,
    });
  }

  console.log(JSON.stringify({ ok: true, tempRoot, results }, null, 2));
} finally {
  if (!keep) rmSync(tempRoot, { recursive: true, force: true });
}
