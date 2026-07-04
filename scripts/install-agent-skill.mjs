#!/usr/bin/env node
import { cpSync, existsSync, mkdirSync, rmSync, symlinkSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const sourceSkill = path.join(repoRoot, "skill", "ultimate-design");

function usage() {
  console.log(`Usage:
  node scripts/install-agent-skill.mjs --target codex [--scope user|project|legacy-codex] [--link]
  node scripts/install-agent-skill.mjs --target claude-code [--scope user|project] [--link]
  node scripts/install-agent-skill.mjs --target pi-agent [--scope user|shared|project] [--link]
  node scripts/install-agent-skill.mjs --target all [--link]

Examples:
  node scripts/install-agent-skill.mjs --target codex --scope user
  node scripts/install-agent-skill.mjs --target claude-code --scope project --link
  node scripts/install-agent-skill.mjs --target pi-agent --scope shared
`);
}

function parseArgs(argv) {
  const args = { target: "", scope: "", link: false, force: true };
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (token === "--help" || token === "-h") args.help = true;
    else if (token === "--link") args.link = true;
    else if (token === "--copy") args.link = false;
    else if (token === "--no-force") args.force = false;
    else if (token === "--target") args.target = argv[++i] || "";
    else if (token === "--scope") args.scope = argv[++i] || "";
    else throw new Error(`Unknown argument: ${token}`);
  }
  return args;
}

function destination(target, scope) {
  const home = os.homedir();
  if (target === "codex") {
    if (scope === "project") return path.resolve(".agents", "skills", "ultimate-design");
    if (scope === "legacy-codex") return path.join(home, ".codex", "skills", "ultimate-design");
    return path.join(home, ".agents", "skills", "ultimate-design");
  }
  if (target === "claude-code") {
    if (scope === "project") return path.resolve(".claude", "skills", "ultimate-design");
    return path.join(home, ".claude", "skills", "ultimate-design");
  }
  if (target === "pi-agent") {
    if (scope === "project") return path.resolve(".pi", "skills", "ultimate-design");
    if (scope === "shared") return path.join(home, ".agents", "skills", "ultimate-design");
    return path.join(home, ".pi", "agent", "skills", "ultimate-design");
  }
  throw new Error(`Unsupported target: ${target}`);
}

function installOne(target, scope, { link, force }) {
  const dest = destination(target, scope);
  mkdirSync(path.dirname(dest), { recursive: true });
  if (existsSync(dest)) {
    if (!force) throw new Error(`Destination exists: ${dest}`);
    rmSync(dest, { recursive: true, force: true });
  }
  if (link) {
    symlinkSync(sourceSkill, dest, "dir");
  } else {
    cpSync(sourceSkill, dest, { recursive: true });
  }
  return { target, scope, mode: link ? "symlink" : "copy", destination: dest };
}

const args = parseArgs(process.argv.slice(2));
if (args.help || !args.target) {
  usage();
  process.exit(args.help ? 0 : 2);
}
if (!existsSync(path.join(sourceSkill, "SKILL.md"))) {
  throw new Error(`Cannot find skill source at ${sourceSkill}`);
}

const installs = [];
if (args.target === "all") {
  installs.push(installOne("codex", "user", args));
  installs.push(installOne("claude-code", "user", args));
  installs.push(installOne("pi-agent", "user", args));
} else {
  installs.push(installOne(args.target, args.scope || "user", args));
}

console.log(JSON.stringify({ installed: installs }, null, 2));
