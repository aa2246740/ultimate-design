#!/usr/bin/env node
// Export every .canvas[data-canvas] element on a page as its own PNG, at the canvas's exact pixel size.
// Social cards, carousels, posters, and slides are designed as HTML (kit/canvas.css) and delivered as images.
//
//   node scripts/export_canvas.mjs --input cards.html --out ./png [--scale 2]
//
// Files are named 01-<data-name or canvas>.png in page order. The run fails when a canvas renders at a
// size other than its declared canvas (usually content forcing the box to grow) or when fonts never load.
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";
import { pathToFileURL } from "node:url";
import { launchPinnedChromium } from "./pinned_playwright.mjs";

const SIZES = { xhs: [1080, 1440], square: [1080, 1080], story: [1080, 1920], poster: [1200, 1600], slide: [1920, 1080] };

const args = {};
const argv = process.argv.slice(2);
for (let i = 0; i < argv.length; i += 1) {
  if (!argv[i].startsWith("--")) continue;
  const next = argv[i + 1];
  if (!next || next.startsWith("--")) args[argv[i].slice(2)] = true;
  else { args[argv[i].slice(2)] = next; i += 1; }
}
if (!args.input) {
  console.error("Usage: node scripts/export_canvas.mjs --input cards.html --out ./png [--scale 1|2]");
  process.exit(2);
}
const input = path.resolve(String(args.input));
const outDir = path.resolve(String(args.out || path.join(path.dirname(input), "export")));
const scale = Number(args.scale || 1);
mkdirSync(outDir, { recursive: true });

const browser = await launchPinnedChromium();
const problems = [];
const files = [];
try {
  const context = await browser.newContext({ viewport: { width: 2200, height: 1400 }, deviceScaleFactor: scale });
  const page = await context.newPage();
  await page.goto(pathToFileURL(input).href, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  const fontsLoaded = await page.evaluate(() => [...document.fonts].filter((f) => f.status === "loaded").map((f) => f.family));
  const canvases = await page.$$("[data-canvas]");
  if (!canvases.length) {
    console.error("No [data-canvas] elements found. Wrap each card or slide in <section class=\"canvas\" data-canvas=\"xhs\">.");
    process.exit(1);
  }
  const used = new Set();
  for (const [i, handle] of canvases.entries()) {
    const info = await handle.evaluate((el) => {
      const r = el.getBoundingClientRect();
      return { kind: el.dataset.canvas, name: el.dataset.name || "", w: Math.round(r.width), h: Math.round(r.height) };
    });
    const want = SIZES[info.kind];
    if (want && (Math.abs(want[0] - info.w) > 1 || Math.abs(want[1] - info.h) > 1)) {
      problems.push(`canvas ${i + 1} (${info.kind}) renders at ${info.w}x${info.h}, expected ${want[0]}x${want[1]}`);
    }
    let base = `${String(i + 1).padStart(2, "0")}-${(info.name || info.kind || "canvas").replace(/[^\w一-鿿-]+/g, "-")}`;
    while (used.has(base)) base += "x";
    used.add(base);
    const file = path.join(outDir, `${base}.png`);
    await handle.screenshot({ path: file });
    files.push({ file, canvas: info.kind, size: `${info.w * scale}x${info.h * scale}` });
  }
  writeFileSync(path.join(outDir, "export.json"), `${JSON.stringify({ input, scale, fontsLoaded: [...new Set(fontsLoaded)], files, problems }, null, 2)}\n`);
  await context.close();
} finally {
  await browser.close();
}

for (const f of files) console.log(`${f.size}  ${f.file}`);
for (const p of problems) console.log(`FAIL ${p}`);
process.exit(problems.length ? 1 : 0);
