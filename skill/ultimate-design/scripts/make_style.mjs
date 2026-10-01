#!/usr/bin/env node
// Turn a small style spec (option ids + one seed color) into design tokens.
//
// The model chooses; this script computes. Every color role is derived in OKLCH and
// nudged until it meets its contrast target, the type scale comes from the density
// and canvas, and fonts come with CJK fallbacks. Output:
//   <out>/style.css          :root custom properties (+ font import) consumed by kit/*.css
//   <out>/style.tokens.json  the same values as data, used by detect_slop --style
//
// Usage:
//   node scripts/make_style.mjs --spec style.json --out ./dir
//   node scripts/make_style.mjs --list
//   node scripts/make_style.mjs --preset P03 --out ./dir [--seed "#hex"] [--canvas xhs]
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "..");
const catalog = JSON.parse(readFileSync(path.join(ROOT, "styles", "catalog.json"), "utf8"));
const presets = JSON.parse(readFileSync(path.join(ROOT, "styles", "presets.json"), "utf8"));

function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i += 1) {
    const t = argv[i];
    if (!t.startsWith("--")) continue;
    const n = argv[i + 1];
    if (!n || n.startsWith("--")) args[t.slice(2)] = true;
    else { args[t.slice(2)] = n; i += 1; }
  }
  return args;
}

// ---------------------------------------------------------------- color math (OKLab / OKLCH, WCAG)

const toLinear = (c) => { const v = c / 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
const fromLinear = (c) => 255 * (c <= 0.0031308 ? 12.92 * c : 1.055 * c ** (1 / 2.4) - 0.055);
function hexToRgb(hex) {
  const h = hex.replace("#", "");
  const f = h.length === 3 ? h.split("").map((x) => x + x).join("") : h;
  return { r: parseInt(f.slice(0, 2), 16), g: parseInt(f.slice(2, 4), 16), b: parseInt(f.slice(4, 6), 16) };
}
function rgbToHex({ r, g, b }) {
  return `#${[r, g, b].map((v) => Math.round(Math.min(255, Math.max(0, v))).toString(16).padStart(2, "0")).join("")}`;
}
function rgbToOklch({ r, g, b }) {
  const lr = toLinear(r); const lg = toLinear(g); const lb = toLinear(b);
  const l = Math.cbrt(0.4122214708 * lr + 0.5363325363 * lg + 0.0514459929 * lb);
  const m = Math.cbrt(0.2119034982 * lr + 0.6806995451 * lg + 0.1073969566 * lb);
  const s = Math.cbrt(0.0883024619 * lr + 0.2817188376 * lg + 0.6299787005 * lb);
  const L = 0.2104542553 * l + 0.793617785 * m - 0.0040720468 * s;
  const a = 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s;
  const bb = 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s;
  return { L, C: Math.hypot(a, bb), h: ((Math.atan2(bb, a) * 180) / Math.PI + 360) % 360 };
}
function oklchToRgbRaw({ L, C, h }) {
  const a = C * Math.cos((h * Math.PI) / 180); const b = C * Math.sin((h * Math.PI) / 180);
  const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3;
  const m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3;
  const s = (L - 0.0894841775 * a - 1.291485548 * b) ** 3;
  return {
    r: fromLinear(4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s),
    g: fromLinear(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s),
    b: fromLinear(-0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s),
  };
}
// Reduce chroma until the color fits sRGB, then round.
function hex(c) {
  let C = Math.max(0, c.C);
  for (let i = 0; i < 60; i += 1) {
    const rgb = oklchToRgbRaw({ L: Math.min(1, Math.max(0, c.L)), C, h: c.h });
    if ([rgb.r, rgb.g, rgb.b].every((v) => v >= -0.5 && v <= 255.5)) return rgbToHex(rgb);
    C *= 0.92;
  }
  return rgbToHex(oklchToRgbRaw({ L: c.L, C: 0, h: c.h }));
}
const lum = (h) => { const { r, g, b } = hexToRgb(h); return 0.2126 * toLinear(r) + 0.7152 * toLinear(g) + 0.0722 * toLinear(b); };
function contrast(a, b) { const x = lum(a); const y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
// Move lightness away from the background until the contrast target is met.
function fit(c, bgHex, target) {
  const grounds = Array.isArray(bgHex) ? bgHex : [bgHex];
  const dark = lum(grounds[0]) > 0.18;
  let cur = { ...c };
  for (let i = 0; i < 120; i += 1) {
    if (grounds.every((g) => contrast(hex(cur), g) >= target)) return cur;
    cur = { ...cur, L: cur.L + (dark ? -0.01 : 0.01) };
    if (cur.L < 0.02 || cur.L > 0.99) break;
  }
  return cur;
}
const K = (L, C, h) => ({ L, C, h });
const onColor = (fillHex, ink, paper) => (contrast(ink, fillHex) >= contrast(paper, fillHex) ? ink : paper);

// ---------------------------------------------------------------- palette strategies

function palette(strategy, seedHex, secondHex) {
  const seed = rgbToOklch(hexToRgb(seedHex));
  const h = seed.h; const c = Math.min(seed.C, 0.2);
  const second = secondHex ? rgbToOklch(hexToRgb(secondHex)) : { ...seed, h: (h + 150) % 360 };
  let P;
  switch (strategy) {
    case "C01": P = { bg: K(0.975, 0.008, h), bgAlt: K(0.95, 0.012, h), surface: K(0.99, 0.004, h), ink: K(0.23, 0.02, h),
      accent: K(Math.min(Math.max(seed.L, 0.45), 0.6), Math.min(c, 0.16), h), band: K(0.24, 0.02, h), dark: false }; break;
    case "C02": P = { bg: K(0.985, 0.005, h), bgAlt: K(0.965, 0.008, h), surface: K(1, 0, h), ink: K(0.22, 0.012, h),
      accent: K(Math.min(Math.max(seed.L, 0.45), 0.62), c, h), band: K(0.955, 0.03, h), dark: false }; break;
    case "C03": P = { bg: K(0.985, 0.006, h), bgAlt: K(0.95, 0.03, h), surface: K(1, 0, h), ink: K(0.22, 0.015, h),
      accent: K(Math.min(Math.max(seed.L, 0.42), 0.58), Math.max(c, 0.1), h), band: K(Math.min(Math.max(seed.L, 0.38), 0.5), Math.max(c, 0.1), h), dark: false }; break;
    case "C04": P = { bg: K(0.93, Math.min(0.055, Math.max(c * 0.4, 0.03)), h), bgAlt: K(0.895, Math.min(0.07, Math.max(c * 0.5, 0.04)), h), surface: K(0.965, 0.025, h),
      ink: K(0.25, Math.min(0.06, c), h), accent: K(0.45, Math.min(Math.max(c, 0.12), 0.18), h), band: K(0.27, Math.min(0.06, c), h), dark: false }; break;
    case "C05": P = { bg: K(0.17, 0.015, h), bgAlt: K(0.205, 0.018, h), surface: K(0.235, 0.02, h), ink: K(0.94, 0.01, h),
      accent: K(0.78, Math.min(Math.max(c, 0.1), 0.15), h), band: K(0.26, 0.03, h), dark: true }; break;
    case "C06": P = { bg: K(0.98, 0.006, h), bgAlt: K(0.95, 0.02, second.h), surface: K(1, 0, h), ink: K(0.22, 0.015, second.h),
      accent: K(Math.min(Math.max(seed.L, 0.45), 0.6), Math.max(c, 0.1), h), band: K(0.33, Math.min(Math.max(second.C, 0.08), 0.12), second.h), dark: false }; break;
    case "C07": P = { bg: K(0.955, 0.018, 75), bgAlt: K(0.925, 0.025, 72), surface: K(0.975, 0.012, 78), ink: K(0.27, 0.025, 55),
      accent: K(0.5, Math.min(c, 0.1), h), band: K(0.38, 0.045, h), dark: false }; break;
    case "C08": P = { bg: K(0.995, 0, h), bgAlt: K(0.96, 0.04, (h + 110) % 360), surface: K(1, 0, h), ink: K(0.2, 0.02, h),
      accent: K(0.62, Math.max(c, 0.17), h), band: K(0.62, Math.max(c, 0.17), h), pop: K(0.8, 0.16, (h + 110) % 360), dark: false }; break;
    case "C09": P = { bg: K(0.985, 0.004, 250), bgAlt: K(0.96, 0.006, 250), surface: K(1, 0, 250), ink: K(0.21, 0.02, 255),
      accent: K(0.45, Math.min(Math.max(c, 0.1), 0.14), h), band: K(0.95, 0.012, 250), dark: false }; break;
    case "C10": P = { bg: K(0.2, 0.02, h), bgAlt: K(0.235, 0.024, h), surface: K(0.26, 0.026, h), ink: K(0.93, 0.025, 85),
      accent: K(0.74, Math.min(Math.max(c, 0.1), 0.15), h), band: K(0.28, 0.03, h), dark: true }; break;
    default: throw new Error(`Unknown color strategy ${strategy}`);
  }
  const bg = hex(P.bg);
  const grounds = [bg, hex(P.bgAlt), hex(P.surface)];
  const ink = hex(fit(P.ink, grounds, 11));
  const ink2 = hex(fit({ ...P.ink, L: P.dark ? 0.8 : 0.42 }, grounds, 6.5));
  const ink3 = hex(fit({ ...P.ink, L: P.dark ? 0.7 : 0.52, C: P.ink.C * 0.8 }, grounds, 4.6));
  const line = hex({ ...P.ink, L: P.dark ? P.bg.L + 0.1 : P.bg.L - 0.1, C: P.bg.C + 0.004 });
  const lineStrong = hex(fit({ ...P.ink, L: P.dark ? 0.5 : 0.62, C: P.bg.C + 0.01 }, bg, 3));
  const accent = hex(P.accent);
  const accentInk = hex(fit(P.accent, grounds, 4.6));
  const paperOn = hex(P.dark ? P.ink : P.bg);
  const inkOn = hex(P.dark ? P.bg : P.ink);
  // Accent fills must carry readable button text.
  let accentFill = P.accent;
  for (let i = 0; i < 40 && Math.max(contrast("#ffffff", hex(accentFill)), contrast(inkOn, hex(accentFill))) < 4.6; i += 1) {
    accentFill = { ...accentFill, L: accentFill.L + (accentFill.L > 0.6 ? 0.01 : -0.01) };
  }
  const accentHex = hex(accentFill);
  const onAccent = contrast("#ffffff", accentHex) >= contrast(inkOn, accentHex) ? "#ffffff" : inkOn;
  const accentSoft = hex(P.dark ? { ...P.accent, L: P.bg.L + 0.07, C: Math.min(P.accent.C, 0.05) } : { ...P.accent, L: 0.94, C: Math.min(P.accent.C * 0.35, 0.05) });
  const band = hex(P.band);
  const onBand = onColor(band, inkOn === "#ffffff" ? "#111111" : ink, "#ffffff") === "#ffffff" ? "#ffffff" : hex(fit(P.ink, band, 7));
  const bandInk2 = hex(fit({ ...(lum(band) > 0.18 ? P.ink : K(0.9, 0.02, P.band.h)), L: lum(band) > 0.18 ? 0.4 : 0.82 }, band, 4.6));
  const status = (hue) => {
    const base = K(P.dark ? 0.74 : 0.5, 0.13, hue);
    const soft = hex(P.dark ? K(P.bg.L + 0.06, 0.04, hue) : K(0.95, 0.035, hue));
    return { fill: hex(base), ink: hex(fit(base, [...grounds, soft], 4.6)), soft };
  };
  const positive = status(150); const warning = status(70); const danger = status(27);
  // Data series: the seed leads; others rotate around it at matched lightness, each at least 3:1 on the ground.
  const dataL = P.dark ? 0.74 : 0.55;
  const rot = strategy === "C06" ? [0, second.h - h, 60, 200, 300] : [0, 150, 60, 230, 300];
  const data = rot.map((d, i) => hex(fit(K(dataL + (i % 2 ? 0.05 : 0), i === 0 ? Math.max(c, 0.1) : 0.11, (h + d + 360) % 360), bg, 3)));
  const dataMuted = hex(fit({ ...P.ink, L: P.dark ? 0.45 : 0.78, C: 0.01 }, bg, 1.6));
  const roles = {
    bg, "bg-alt": hex(P.bgAlt), surface: hex(P.surface), ink, "ink-2": ink2, "ink-3": ink3, line, "line-strong": lineStrong,
    accent: accentHex, "accent-ink": accentInk, "on-accent": onAccent, "accent-soft": accentSoft,
    band, "on-band": onBand, "band-ink-2": bandInk2,
    positive: positive.fill, "positive-ink": positive.ink, "positive-soft": positive.soft,
    warning: warning.fill, "warning-ink": warning.ink, "warning-soft": warning.soft,
    danger: danger.fill, "danger-ink": danger.ink, "danger-soft": danger.soft,
    "data-1": data[0], "data-2": data[1], "data-3": data[2], "data-4": data[3], "data-5": data[4], "data-muted": dataMuted,
  };
  if (P.pop) roles.pop = hex(P.pop);
  if (strategy === "C09") { roles["data-1"] = accentInk; roles["data-2"] = hex(fit(K(0.55, 0.02, 250), bg, 3)); }
  void accent; void paperOn;
  return { roles, dark: P.dark };
}

// ---------------------------------------------------------------- type

const SYSTEM_SANS = "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial";
const SYSTEM_MONO = "ui-monospace, \"SF Mono\", Menlo, Consolas, \"Liberation Mono\"";
function stack(latin, cjk, kind) {
  const cjkStack = catalog.cjk_stacks[cjk] || `"${cjk}", ${catalog.cjk_stacks[kind === "serif" ? "serif" : "sans"]}`;
  if (latin === "system") return `${SYSTEM_SANS}, ${catalog.cjk_stacks.sans}, sans-serif`;
  if (latin === "system-mono") return `${SYSTEM_MONO}, monospace`;
  const fam = latin.replace(/ Expanded$/, "");
  const generic = kind === "serif" ? "serif" : kind === "mono" ? "monospace" : "sans-serif";
  return `"${fam}", ${cjkStack}, ${generic}`;
}
const isSerif = (name) => /serif|caslon|garamond|fraunces|spectral|bodoni|literata|young serif/i.test(name) && !/sans/i.test(name);

function scale(base, ratio, floor = 12) {
  const s = (n) => Math.round(base * ratio ** n);
  return { xs: Math.max(floor, s(-2)), sm: Math.max(floor + 1, s(-1)), base: s(0), md: s(1), lg: s(2), xl: s(3), "2xl": s(4), "3xl": s(5), display: s(6) };
}

// ---------------------------------------------------------------- surfaces

const SURFACES = {
  S01: { "card-bg": "transparent", "card-border": "1px solid var(--line)", "card-radius": "2px", "card-shadow": "none", "divider": "1px solid var(--line)", "radius-control": "3px" },
  S02: { "card-bg": "var(--bg-alt)", "card-border": "0", "card-radius": "4px", "card-shadow": "none", "divider": "0", "radius-control": "4px" },
  S03: { "card-bg": "var(--surface)", "card-border": "1px solid var(--line)", "card-radius": "12px", "card-shadow": "0 1px 2px rgb(0 0 0 / 0.05), 0 2px 8px rgb(0 0 0 / 0.04)", "divider": "1px solid var(--line)", "radius-control": "8px" },
  S04: { "card-bg": "var(--surface)", "card-border": "2px solid var(--ink)", "card-radius": "0", "card-shadow": "none", "divider": "2px solid var(--ink)", "radius-control": "0" },
  S05: { "card-bg": "transparent", "card-border": "0", "card-radius": "0", "card-shadow": "none", "divider": "0", "radius-control": "4px" },
  S06: { "card-bg": "var(--bg-alt)", "card-border": "0", "card-radius": "20px", "card-shadow": "none", "divider": "0", "radius-control": "999px" },
};

// ---------------------------------------------------------------- build

function build(spec) {
  const base0 = catalog.type[spec.type];
  if (!base0) throw new Error(`Unknown type pairing ${spec.type}. Run --list.`);
  // Brand override: {"fonts": {"display": "Brand Serif", "text": "Brand Sans", "google": ["Brand Serif:wght@600"], "serif": true}}
  // keeps the pairing's CJK fallbacks, weights, and tracking; google families are added to the import (omit for self-hosted fonts).
  const o = spec.fonts || {};
  const type = { ...base0, ...(o.display ? { display: o.display } : {}), ...(o.text ? { text: o.text } : {}),
    google: [...(o.replace_google ? [] : base0.google || []), ...(o.google || [])] };
  const strategy = spec.color?.strategy;
  if (!catalog.color[strategy]) throw new Error(`Unknown color strategy ${strategy}. Run --list.`);
  if (!/^#?[0-9a-f]{6}$/i.test(spec.color.seed || "")) throw new Error("color.seed must be a 6-digit hex color");
  const surface = SURFACES[spec.surface];
  if (!surface) throw new Error(`Unknown surface ${spec.surface}. Run --list.`);
  const densityName = spec.density || "regular";
  const density = catalog.density[densityName];
  if (!density) throw new Error(`Unknown density ${densityName}`);
  const canvasName = spec.canvas || "web";
  const canvas = catalog.canvas[canvasName];
  if (!canvas) throw new Error(`Unknown canvas ${canvasName}`);

  const seed = spec.color.seed.startsWith("#") ? spec.color.seed : `#${spec.color.seed}`;
  const { roles, dark } = palette(strategy, seed, spec.color.second);

  const fonts = {
    display: stack(type.display, type.cjk_display, (o.display && o.serif !== undefined ? o.serif : isSerif(type.display)) ? "serif" : "sans"),
    text: stack(type.text, type.cjk_text, isSerif(type.text) ? "serif" : "sans"),
    mono: stack(type.mono || "system-mono", "sans", "mono"),
  };
  if (type.accent_font) fonts.accent = `"${type.accent_font}", "${type.cjk_accent_font || "Ma Shan Zheng"}", ${catalog.cjk_stacks.kai}, cursive`;
  if (type.cjk_accent === "kai") fonts.accent = `${catalog.cjk_stacks.kai}, serif`;
  if (type.label) fonts.label = stack(type.label, "sans", "sans");

  const web = canvasName === "web";
  const base = web ? density.base_web : canvas.base;
  const ratio = web ? density.ratio : canvas.ratio;
  const desktop = web ? scale(base, ratio) : scale(base, ratio, canvas.min_font);
  const mobile = web ? scale(16, Math.min(ratio, 1.22)) : null;
  const sp = [4, 8, 12, 16, 24, 32, 48, 64, 96, 128].map((v) => Math.round((v * density.space) / 2) * 2 || v);
  const canvasScale = web ? 1 : canvas.base / 24;
  const space = web ? sp : sp.map((v) => Math.round(v * canvasScale));

  const googleFamilies = type.google || [];
  const importUrl = googleFamilies.length
    ? `https://fonts.googleapis.com/css2?${googleFamilies.map((f) => `family=${f.replace(/ /g, "+")}`).join("&")}&display=swap`
    : null;

  const vars = {
    "font-display": fonts.display, "font-text": fonts.text, "font-mono": fonts.mono,
    ...(fonts.accent ? { "font-accent": fonts.accent } : {}), ...(fonts.label ? { "font-label": fonts.label } : {}),
    "fw-display": String(type.display_weight), "fw-text": String(type.text_weight), "fw-strong": String(Math.max(600, type.text_weight + 200)),
    "tracking-display": type.tracking, "display-stretch": /Expanded$/.test(type.display) ? "125%" : "100%",
    ...Object.fromEntries(Object.entries(desktop).map(([k, v]) => [`fs-${k}`, `${v}px`])),
    "lh-tight": "1.12", "lh-snug": "1.3", "lh-text": "1.65", "lh-cjk": "1.8",
    ...Object.fromEntries(space.map((v, i) => [`sp-${i + 1}`, `${v}px`])),
    "sp-section": web ? `clamp(${space[6]}px, 8vw, ${space[8]}px)` : `${space[7]}px`,
    container: web ? (densityName === "dense" ? "1360px" : "1200px") : `${canvas.width}px`,
    measure: "34em", "measure-cjk": "36em",
    gutter: web ? "clamp(16px, 4vw, 48px)" : `${canvas.safe}px`,
    ...(web ? {} : { "canvas-w": `${canvas.width}px`, "canvas-h": `${canvas.height}px`, safe: `${canvas.safe}px`, "min-font": `${canvas.min_font}px` }),
    ...Object.fromEntries(Object.entries(surface).map(([k, v]) => [k, v])),
    ...roles,
  };
  const css = [
    "/* Generated by scripts/make_style.mjs. Do not edit values by hand: change the spec and regenerate. */",
    `/* spec: ${JSON.stringify(spec)} */`,
    importUrl ? `@import url("${importUrl}");` : "",
    `:root {\n  color-scheme: ${dark ? "dark" : "light"};\n${Object.entries(vars).map(([k, v]) => `  --${k}: ${v};`).join("\n")}\n}`,
    mobile ? `@media (max-width: 640px) {\n  :root {\n${Object.entries(mobile).map(([k, v]) => `    --fs-${k}: ${v}px;`).join("\n")}\n  }\n}` : "",
    web ? "" : `/* canvas ${canvasName}: ${canvas.width}x${canvas.height}, safe area ${canvas.safe}px, minimum text ${canvas.min_font}px */`,
  ].filter(Boolean).join("\n\n");

  const firstFamily = (s) => s.split(",")[0].replace(/"/g, "").trim();
  const tokens = {
    spec, dark, canvas: { name: canvasName, ...canvas },
    colors: roles,
    fontSizes: { desktop: Object.values(desktop), mobile: mobile ? Object.values(mobile) : [] },
    fonts: Object.fromEntries(Object.entries(fonts).map(([k, v]) => [k, firstFamily(v)])),
    space,
    contrast: {
      "ink/bg": +contrast(roles.ink, roles.bg).toFixed(2), "ink-2/bg": +contrast(roles["ink-2"], roles.bg).toFixed(2),
      "ink-3/bg": +contrast(roles["ink-3"], roles.bg).toFixed(2), "accent-ink/bg": +contrast(roles["accent-ink"], roles.bg).toFixed(2),
      "on-accent/accent": +contrast(roles["on-accent"], roles.accent).toFixed(2), "on-band/band": +contrast(roles["on-band"], roles.band).toFixed(2),
      "ink/bg-alt": +contrast(roles.ink, roles["bg-alt"]).toFixed(2), "ink-2/bg-alt": +contrast(roles["ink-2"], roles["bg-alt"]).toFixed(2),
    },
  };
  return { css, tokens };
}

// ---------------------------------------------------------------- CLI

const args = parseArgs(process.argv.slice(2));
if (args.list) {
  console.log("TYPE PAIRINGS");
  for (const [id, t] of Object.entries(catalog.type)) console.log(`  ${id}  ${t.name.padEnd(28)} ${t.voice}  | fits: ${t.fits}`);
  console.log("\nCOLOR STRATEGIES (+ a seed hex, optional second hex for C06)");
  for (const [id, c] of Object.entries(catalog.color)) console.log(`  ${id}  ${c.name.padEnd(28)} ${c.summary}`);
  console.log("\nSURFACES");
  for (const [id, s] of Object.entries(catalog.surface)) console.log(`  ${id}  ${s.name.padEnd(28)} ${s.summary}`);
  console.log(`\nDENSITY  ${Object.keys(catalog.density).join(" | ")}`);
  console.log(`CANVAS   ${Object.keys(catalog.canvas).join(" | ")}`);
  console.log("\nPRESETS");
  for (const [id, p] of Object.entries(presets.presets)) console.log(`  ${id}  ${p.name.padEnd(28)} ${p.type} ${p.color.strategy} ${p.color.seed} ${p.surface} ${p.density}  | ${p.for}`);
  process.exit(0);
}

let spec;
if (args.spec) spec = JSON.parse(readFileSync(String(args.spec), "utf8"));
else if (args.preset) {
  const p = presets.presets[String(args.preset)];
  if (!p) { console.error(`Unknown preset ${args.preset}. Run --list.`); process.exit(2); }
  spec = { type: p.type, color: { ...p.color }, surface: p.surface, density: p.density, canvas: "web" };
} else {
  console.error("Usage: node scripts/make_style.mjs --spec style.json --out <dir> | --preset P01 --out <dir> [--seed #hex] [--canvas xhs] | --list");
  process.exit(2);
}
if (args.seed) spec.color.seed = String(args.seed);
if (args.canvas) spec.canvas = String(args.canvas);
if (args.density) spec.density = String(args.density);

try {
  const { css, tokens } = build(spec);
  const out = path.resolve(String(args.out || "."));
  mkdirSync(out, { recursive: true });
  writeFileSync(path.join(out, "style.css"), `${css}\n`);
  writeFileSync(path.join(out, "style.tokens.json"), `${JSON.stringify(tokens, null, 2)}\n`);
  const low = Object.entries(tokens.contrast).filter(([k, v]) => v < (k.startsWith("on-") || k.startsWith("ink/") ? 4.5 : 4.5));
  console.log(`style.css + style.tokens.json -> ${out}`);
  console.log(`contrast: ${Object.entries(tokens.contrast).map(([k, v]) => `${k} ${v}`).join(", ")}`);
  if (low.length) console.log(`WARNING below 4.5:1: ${low.map(([k]) => k).join(", ")}`);
} catch (error) {
  console.error(String(error.message || error));
  process.exit(2);
}
