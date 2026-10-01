#!/usr/bin/env node
// Rendered craft-defect and slop-fingerprint scan for generated HTML.
//
// Defects are objective render problems (text touching the viewport edge, clipped
// text, invisible content, heading orphans, ASCII punctuation in CJK text, edge drift).
// Fingerprints are the taste signals catalogued in references/slop-fingerprints.md.
// Fingerprints never fail the run on their own: they inform the critique, they do
// not replace looking at the screenshots.
import { existsSync, mkdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";
import { pathToFileURL } from "node:url";
import { launchPinnedChromium } from "./pinned_playwright.mjs";

function parseArgs(argv) {
  const args = {
    viewports: "desktop=1440x900,mobile=390x844",
    profile: "auto",
    wait: 800,
    step: 300,
    stepWait: 160,
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

const args = parseArgs(process.argv.slice(2));
if (!args.input) {
  console.error(
    "Usage: node scripts/detect_slop.mjs --input artifact.html|http(s)://url [--out out-dir] [--viewports desktop=1440x900,mobile=390x844] [--profile auto|landing|product|report|canvas] [--style style.tokens.json] [--strict] [--json]",
  );
  process.exit(2);
}

const inputArg = String(args.input);
const isUrl = /^https?:\/\//i.test(inputArg);
const target = isUrl ? inputArg : pathToFileURL(path.resolve(inputArg)).href;
const outputDir = path.resolve(
  String(args.out || (isUrl ? "ultimate-design-slop-scan" : path.join(path.dirname(path.resolve(inputArg)), "ultimate-design-slop-scan"))),
);
let viewports = parseViewports(args.viewports);
const waitMs = Number(args.wait);
const stepPx = Number(args.step);
const stepWaitMs = Number(args.stepWait);
// auto | landing | product | report | canvas. Report and product surfaces do not need a first-screen call to action.
const profile = String(args.profile);
// --style: style.tokens.json from make_style.mjs (or its folder / style.css). Enables the system-adherence lint.
let styleTokens = null;
if (args.style) {
  let p = path.resolve(String(args.style));
  if (existsSync(p) && statSync(p).isDirectory()) p = path.join(p, "style.tokens.json");
  else if (p.endsWith(".css")) p = path.join(path.dirname(p), "style.tokens.json");
  styleTokens = JSON.parse(readFileSync(p, "utf8"));
}
const viewportsDefault = !process.argv.includes("--viewports");
const canvasPage = profile === "canvas"
  || (styleTokens && styleTokens.canvas && styleTokens.canvas.name && styleTokens.canvas.name !== "web")
  || (!isUrl && existsSync(path.resolve(inputArg)) && /data-canvas\s*=/.test(readFileSync(path.resolve(inputArg), "utf8")));
if (canvasPage && viewportsDefault) viewports = [{ name: "canvas", width: 2200, height: 1400 }];

const FINGERPRINT_NAMES = {
  S1: "Section template",
  S2: "Equal card grid",
  S4: "Stat strip",
  S6: "Decorative numbering",
  S8: "Card inside card",
  T1: "Eyebrow system",
  T2: "Translated eyebrow",
  T3: "Two-tone headline",
  T4: "Gradient text",
  T5: "Mono as seasoning",
  C3: "Multi-hue gradient surface",
  C4: "Glow or blob",
  C5: "Glass panel",
  C6: "Hard offset shadows",
  C8: "Texture by default",
  K1: "Pill everything",
  K2: "Icon tiles",
  K3: "Hover lift",
  K5: "Emoji as icons",
  W1: "Contrast formula copy",
  W3: "Empty verbs",
  W7: "Dash habit",
  M1: "Fade-up everything",
  M2: "Marquee or ticker",
  Z1: "Wireframe look",
  Z2: "Placeholder hero",
  Z3: "Brief leakage",
};

// ---------------------------------------------------------------- in-page code

function tagTextElements() {
  const SKIP = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEMPLATE", "TITLE", "OPTION"]);
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let next = 0;
  const hidden = [];
  const opacityOf = (el) => {
    let v = 1;
    for (let a = el; a && a !== document.documentElement; a = a.parentElement) {
      const s = getComputedStyle(a);
      if (s.display === "none") return 0;
      v *= Number.parseFloat(s.opacity);
    }
    return v;
  };
  for (let node = walker.nextNode(); node; node = walker.nextNode()) {
    if (!node.nodeValue || !node.nodeValue.trim()) continue;
    const el = node.parentElement;
    if (!el || SKIP.has(el.tagName) || el.closest("svg, select")) continue;
    if (el.hasAttribute("data-ud-slop-id")) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;
    const id = String(next);
    next += 1;
    el.setAttribute("data-ud-slop-id", id);
    const s = getComputedStyle(el);
    if (s.visibility !== "hidden" && opacityOf(el) <= 0.05 && !el.closest("[aria-hidden='true'], [inert]")) hidden.push(id);
  }
  window.__udSeen = new Set();
  return hidden;
}

function markSeen() {
  const vh = window.innerHeight;
  for (const el of document.querySelectorAll("[data-ud-slop-id]")) {
    const id = el.getAttribute("data-ud-slop-id");
    if (window.__udSeen.has(id)) continue;
    const r = el.getBoundingClientRect();
    if (r.bottom < 0 || r.top > vh || r.width < 1) continue;
    let v = 1;
    for (let a = el; a && a !== document.documentElement; a = a.parentElement) {
      v *= Number.parseFloat(getComputedStyle(a).opacity);
      if (v <= 0.05) break;
    }
    if (v > 0.05) window.__udSeen.add(id);
  }
}

function analyzePage({ hiddenAtLoad, profileArg, tokens }) {
  const vw = document.documentElement.clientWidth;
  const vh = window.innerHeight;
  // Fixed-size canvases (social cards, posters, slides) are judged per canvas, not as a scrolling page.
  const canvasEls = [...document.querySelectorAll("[data-canvas]")];
  if (canvasEls.length && profileArg === "auto") profileArg = "canvas";
  const sx = window.scrollX;
  const sy = window.scrollY;
  const desktop = vw >= 1024;
  const minGutter = vw >= 768 ? 16 : 12;
  const CJK = /[㐀-鿿豈-﫿]/;
  const SKIP = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEMPLATE", "TITLE", "OPTION"]);

  const styleCache = new Map();
  const st = (el) => {
    let s = styleCache.get(el);
    if (!s) {
      s = getComputedStyle(el);
      styleCache.set(el, s);
    }
    return s;
  };
  const opacityCache = new Map();
  const effOpacity = (el) => {
    if (!el || el === document.documentElement) return 1;
    if (opacityCache.has(el)) return opacityCache.get(el);
    const s = st(el);
    let v = s.display === "none" ? 0 : Number.parseFloat(s.opacity) * effOpacity(el.parentElement);
    if (s.visibility === "hidden" || s.visibility === "collapse") v = 0;
    opacityCache.set(el, v);
    return v;
  };
  const parseColor = (c) => {
    const m = String(c).match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[\s,/]+/).filter(Boolean).map(Number.parseFloat);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const isTransparent = (c) => {
    const p = parseColor(c);
    return !p || p.a < 0.04;
  };
  const colorDist = (a, b) => {
    const x = parseColor(a);
    const y = parseColor(b);
    if (!x || !y) return 999;
    return Math.abs(x.r - y.r) + Math.abs(x.g - y.g) + Math.abs(x.b - y.b);
  };
  const hsl = ({ r, g, b }) => {
    const R = r / 255;
    const G = g / 255;
    const B = b / 255;
    const max = Math.max(R, G, B);
    const min = Math.min(R, G, B);
    const l = (max + min) / 2;
    if (max === min) return { h: 0, s: 0, l };
    const d = max - min;
    const s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    let h;
    if (max === R) h = (G - B) / d + (G < B ? 6 : 0);
    else if (max === G) h = (B - R) / d + 2;
    else h = (R - G) / d + 4;
    return { h: h * 60, s, l };
  };
  const snippet = (s, n = 60) => {
    const t = String(s).replace(/\s+/g, " ").trim();
    return t.length > n ? `${t.slice(0, n - 1)}…` : t;
  };
  const describe = (el) => {
    const tag = el.tagName.toLowerCase();
    const id = el.id ? `#${el.id}` : "";
    const cls = typeof el.className === "string" && el.className.trim()
      ? `.${el.className.trim().split(/\s+/).slice(0, 2).join(".")}`
      : "";
    return `${tag}${id}${cls}`;
  };
  const pageBox = (r) => ({
    x: Math.round(r.left + sx),
    y: Math.round(r.top + sy),
    w: Math.round(r.right - r.left),
    h: Math.round(r.bottom - r.top),
  });
  const union = (rects) => rects.reduce(
    (u, r) => ({
      left: Math.min(u.left, r.left),
      top: Math.min(u.top, r.top),
      right: Math.max(u.right, r.right),
      bottom: Math.max(u.bottom, r.bottom),
    }),
    { left: Infinity, top: Infinity, right: -Infinity, bottom: -Infinity },
  );
  const sample = (el, text, box) => ({
    selector: describe(el),
    text: snippet(text ?? el.textContent ?? ""),
    box: pageBox(box ?? el.getBoundingClientRect()),
  });
  const px = (v) => {
    const n = Number.parseFloat(v);
    return Number.isFinite(n) ? n : 0;
  };
  const isSrOnly = (el) => {
    for (let a = el, i = 0; a && a !== document.body && i < 5; a = a.parentElement, i += 1) {
      const r = a.getBoundingClientRect();
      const s = st(a);
      if ((r.width <= 2 || r.height <= 2) && (s.overflow !== "visible" || s.clip !== "auto")) return true;
      if (s.position === "absolute" && s.clip && s.clip !== "auto") return true;
    }
    return false;
  };

  // ---- collect text blocks (element -> its direct text nodes)
  const range = document.createRange();
  const blocks = new Map();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let node = walker.nextNode(); node; node = walker.nextNode()) {
    const raw = node.nodeValue;
    if (!raw || !raw.trim()) continue;
    const el = node.parentElement;
    if (!el || SKIP.has(el.tagName) || el.closest("svg, select")) continue;
    range.selectNodeContents(node);
    const rects = [...range.getClientRects()].filter((r) => r.width > 0.5 && r.height > 0.5);
    if (!rects.length) continue;
    let b = blocks.get(el);
    if (!b) {
      b = { el, rects: [], text: "" };
      blocks.set(el, b);
    }
    b.rects.push(...rects);
    b.text += raw;
  }
  const allBlocks = [];
  for (const b of blocks.values()) {
    if (isSrOnly(b.el)) continue;
    b.u = union(b.rects);
    b.op = effOpacity(b.el);
    b.fs = px(st(b.el).fontSize);
    b.text = b.text.replace(/\s+/g, " ").trim();
    allBlocks.push(b);
  }
  const vis = allBlocks.filter((b) => b.op > 0.05);

  const defects = [];
  const addDefect = (id, severity, message, samples) => defects.push({ id, severity, message, samples });
  const fp = {};
  const addFp = (id, count, samples, note) => {
    fp[id] = { id, name: null, count, samples: samples.slice(0, 6), note };
  };

  // ---- animated elements (marquees are clipped by design)
  const animated = new Set();
  for (const anim of document.getAnimations()) {
    const t = anim.effect && anim.effect.target;
    if (t && t.nodeType === 1) animated.add(t);
  }
  const hasAnimatedAncestor = (el, stop) => {
    for (let a = el; a && a !== stop; a = a.parentElement) if (animated.has(a)) return true;
    return false;
  };

  // ---- clipping and edge checks
  const clipped = [];
  const truncated = [];
  const marquee = [];
  const edge = [];
  const tightEdge = [];
  for (const b of vis) {
    let scroller = false;
    let clipHit = null;
    const tolY = Math.max(2, b.fs * 0.25);
    const tolX = Math.max(2, b.fs * 0.08);
    for (let a = b.el.parentElement; a && a !== document.documentElement; a = a.parentElement) {
      const s = st(a);
      const ox = s.overflowX;
      const oy = s.overflowY;
      // Content inside a scroll container (a kanban row, a wide table) is reachable, not clipped.
      if ((ox === "auto" || ox === "scroll") && a.scrollWidth > a.clientWidth + 1) scroller = true;
      if ((oy === "auto" || oy === "scroll") && a.scrollHeight > a.clientHeight + 1) scroller = true;
      if (scroller) break;
      const cp = s.clipPath && s.clipPath !== "none";
      const clipX = ox === "hidden" || ox === "clip" || cp;
      const clipY = oy === "hidden" || oy === "clip" || cp;
      if (!clipX && !clipY) continue;
      const r = a.getBoundingClientRect();
      if (r.width < 3 || r.height < 3) continue;
      const intersects = b.u.right > r.left && b.u.left < r.right && b.u.bottom > r.top && b.u.top < r.bottom;
      if (!intersects) {
        clipHit = "outside";
        break;
      }
      const overX = clipX && (b.u.left < r.left - tolX || b.u.right > r.right + tolX);
      const overY = clipY && (b.u.top < r.top - tolY || b.u.bottom > r.bottom + tolY);
      if (overX || overY) {
        clipHit = { a };
        break;
      }
    }
    if (clipHit === "outside") continue;
    if (clipHit) {
      const ell = st(b.el).textOverflow === "ellipsis" || st(clipHit.a).textOverflow === "ellipsis";
      if (hasAnimatedAncestor(b.el, clipHit.a)) marquee.push(sample(b.el, b.text, b.u));
      else if (ell) truncated.push(sample(b.el, b.text, b.u));
      else clipped.push({ ...sample(b.el, b.text, b.u), clippedBy: describe(clipHit.a) });
      continue;
    }
    if (scroller) continue;
    if (b.u.right <= 0 || b.u.left >= vw) continue;
    const gap = Math.min(b.u.left, vw - b.u.right);
    if (gap < 7.5) edge.push(sample(b.el, b.text, b.u));
    else if (gap < minGutter - 0.5) tightEdge.push(sample(b.el, b.text, b.u));
  }
  if (clipped.length) addDefect("clipped-text", "fail", "Text is cut by an overflow or clip-path container.", clipped);
  if (edge.length) addDefect("edge-touch", "fail", "Text sits within 8px of the viewport edge (S10 edge drift).", edge);
  if (tightEdge.length) {
    addDefect("edge-tight", "warn", `Text sits closer than the ${minGutter}px minimum gutter to the viewport edge.`, tightEdge);
  }
  if (truncated.length) addDefect("truncated-text", "info", "Text is truncated with an ellipsis; confirm the full value is reachable.", truncated);
  if (marquee.length) addFp("M2", marquee.length, marquee);

  // ---- heading edge drift (desktop)
  const headings = [...document.querySelectorAll("h1, h2")].filter((h) => {
    const r = h.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && effOpacity(h) > 0.05 && !isSrOnly(h);
  });
  const headingLeft = (h) => {
    const inside = vis.filter((b) => h === b.el || h.contains(b.el));
    return inside.length ? union(inside.map((b) => b.u)) : null;
  };
  if (desktop) {
    const lefts = [];
    for (const h of headings) {
      const align = st(h).textAlign;
      if (align === "center" || align === "right" || align === "end") continue;
      const u = headingLeft(h);
      if (!u || u.left < 0 || u.left > vw) continue;
      lefts.push({ h, x: Math.round(u.left), u });
    }
    const clusters = [];
    for (const item of lefts) {
      const c = clusters.find((k) => Math.abs(k.x - item.x) <= 4);
      if (c) c.items.push(item);
      else clusters.push({ x: item.x, items: [item] });
    }
    clusters.sort((a, b) => b.items.length - a.items.length);
    if (clusters.length > 1 && clusters[0].items.length >= 2) {
      const main = clusters[0];
      const outliers = [];
      for (const c of clusters.slice(1)) {
        const d = Math.abs(c.x - main.x);
        if (d > 8 && d <= 320 && c.items.length < main.items.length) {
          for (const item of c.items) outliers.push({ ...sample(item.h, item.h.textContent, item.u), offsetFromMainEdge: c.x - main.x });
        }
      }
      if (outliers.length) {
        addDefect("heading-edge-drift", "warn", `Headings leave the dominant left edge (x=${main.x + sx}).`, outliers);
      }
    }
  }

  // ---- heading orphans and ugly last lines
  const blockAncestor = (el, root) => {
    for (let a = el; a && a !== root; a = a.parentElement) {
      const d = st(a).display;
      if (d !== "inline" && d !== "contents") return a;
    }
    return root;
  };
  const orphanRoots = new Set(headings);
  for (const h of document.querySelectorAll("h3")) orphanRoots.add(h);
  for (const b of vis) if (b.fs >= 28 && !b.el.closest("h1, h2, h3")) orphanRoots.add(b.el);
  const orphans = [];
  for (const root of orphanRoots) {
    if (effOpacity(root) <= 0.05) continue;
    const segs = [[]];
    let lastBlock = null;
    const tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT);
    for (let n = tw.nextNode(); n; n = tw.nextNode()) {
      if (n.nodeType === 1) {
        if (n.tagName === "BR") segs.push([]);
        continue;
      }
      const parent = n.parentElement;
      if (!parent || parent.closest("svg")) continue;
      const blk = blockAncestor(parent, root);
      if (lastBlock && blk !== lastBlock && segs[segs.length - 1].length) segs.push([]);
      lastBlock = blk;
      const t = n.nodeValue;
      for (let i = 0; i < t.length; i += 1) {
        const ch = t[i];
        if (/\s/.test(ch)) {
          segs[segs.length - 1].push({ ch: " ", top: null });
          continue;
        }
        range.setStart(n, i);
        range.setEnd(n, i + 1);
        const r = range.getClientRects()[0];
        if (!r || r.width === 0) continue;
        segs[segs.length - 1].push({ ch, top: r.top, h: r.height });
      }
    }
    for (const seg of segs) {
      const lines = [];
      let cur = null;
      for (const c of seg) {
        if (c.top === null) {
          if (cur) cur.text += " ";
          continue;
        }
        if (!cur || c.top > cur.top + c.h * 0.5) {
          cur = { top: c.top, text: "" };
          lines.push(cur);
        }
        cur.text += c.ch;
      }
      if (lines.length < 2) continue;
      const full = lines.map((l) => l.text).join("").trim();
      const last = lines[lines.length - 1].text.trim();
      const core = (s) => s.replace(/[\s\p{P}\p{S}]/gu, "");
      let orphan = false;
      if (CJK.test(full)) {
        orphan = core(full).length >= 6 && core(last).length <= 2;
      } else {
        const words = full.split(/\s+/).filter((w) => core(w).length);
        const lastWords = last.split(/\s+/).filter((w) => core(w).length);
        orphan = words.length >= 4 && lastWords.length === 1;
      }
      if (orphan) {
        const r = root.getBoundingClientRect();
        orphans.push({ ...sample(root, full, r), lastLine: last });
      }
    }
  }
  if (orphans.length) addDefect("heading-orphan", "warn", "A heading or display line ends with a lone word or one or two CJK characters (T7).", orphans);

  // ---- ASCII punctuation inside CJK text
  const punct = [];
  const asciiPunct = /[㐀-鿿][,;!?:](?!\/\/)|[,;!?](?=[㐀-鿿])|"[^"\n]{0,40}[㐀-鿿][^"\n]{0,40}"/;
  for (const b of vis) {
    if (b.el.closest("code, pre, kbd, samp, script")) continue;
    const m = b.text.match(asciiPunct);
    if (!m) continue;
    const at = m.index ?? 0;
    punct.push({ ...sample(b.el, b.text, b.u), match: b.text.slice(Math.max(0, at - 8), at + 12) });
  }
  if (punct.length) addDefect("cjk-ascii-punctuation", "warn", "Chinese text uses ASCII commas, colons, question marks, or straight quotes.", punct);

  // ---- content hidden until scroll / never shown
  const seen = window.__udSeen || new Set();
  const hiddenSet = new Set(hiddenAtLoad);
  const revealed = [];
  const neverShown = [];
  for (const b of allBlocks) {
    const id = b.el.getAttribute("data-ud-slop-id");
    if (!id || !hiddenSet.has(id)) continue;
    if (b.op > 0.05 || seen.has(id)) revealed.push(sample(b.el, b.text, b.u));
    else if (st(b.el).visibility !== "hidden") neverShown.push(sample(b.el, b.text, b.u));
  }
  if (revealed.length >= 5) addFp("M1", revealed.length, revealed, "text blocks start invisible and appear on scroll");
  if (neverShown.length) addDefect("invisible-text", "warn", "Text stayed invisible through a full slow scroll.", neverShown);

  // ---- eyebrows (T1/T2)
  const eyebrows = [];
  const translated = [];
  for (const h of headings) {
    const hr = h.getBoundingClientRect();
    const hfs = px(st(h).fontSize);
    let best = null;
    for (const b of vis) {
      if (h.contains(b.el) || b.el.contains(h)) continue;
      const gap = hr.top - b.u.bottom;
      if (gap < -2 || gap > 64) continue;
      if (b.u.right < hr.left || b.u.left > hr.right) continue;
      if (!(b.fs <= 15 && b.fs <= hfs * 0.6)) continue;
      if (b.text.length > 48) continue;
      const s = st(b.el);
      const ls = px(s.letterSpacing);
      const upper = s.textTransform === "uppercase" || (/[A-Z]{3}/.test(b.text) && b.text === b.text.toUpperCase());
      const tracked = ls / b.fs >= 0.05;
      const mono = /mono|menlo|consolas|courier/i.test(s.fontFamily);
      if (!(upper || tracked || mono)) continue;
      if (!best || gap < best.gap) best = { b, gap, latinUpper: upper && /[A-Za-z]/.test(b.text) && !CJK.test(b.text) };
    }
    if (!best) continue;
    const item = { ...sample(best.b.el, best.b.text, best.b.u), heading: snippet(h.textContent, 40) };
    eyebrows.push({ h, item });
    if (best.latinUpper && CJK.test(h.textContent)) translated.push(item);
  }
  if (eyebrows.length >= 3) addFp("T1", eyebrows.length, eyebrows.map((e) => e.item));
  if (translated.length) addFp("T2", translated.length, translated);

  // ---- two-tone headlines (T3)
  const twoTone = [];
  const displayRoots = new Set(headings);
  for (const b of vis) if (b.fs >= 40) displayRoots.add(b.el.closest("h1, h2") || b.el);
  for (const root of displayRoots) {
    const rootColor = st(root).color;
    for (const b of vis) {
      if (b.el === root || !root.contains(b.el)) continue;
      const s = st(b.el);
      const recolored = colorDist(s.color, rootColor) > 80;
      const highlighted = !isTransparent(s.backgroundColor) && colorDist(s.backgroundColor, st(root).backgroundColor) > 60;
      if ((recolored || highlighted) && !/\d/.test(b.text) && b.fs >= px(st(root).fontSize) * 0.75) {
        twoTone.push({ ...sample(root, root.textContent), accent: snippet(b.text, 24) });
        break;
      }
    }
  }
  if (twoTone.length) addFp("T3", twoTone.length, twoTone);

  // ---- all elements pass: gradients, glass, shadows, pills, tiles, radii
  const all = [...document.body.querySelectorAll("*")].filter((el) => {
    if (SKIP.has(el.tagName) || el.closest("svg") && el.tagName.toLowerCase() !== "svg") return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && effOpacity(el) > 0.05;
  });
  const bgOf = (el) => {
    for (let a = el; a; a = a.parentElement) {
      const c = st(a).backgroundColor;
      if (!isTransparent(c)) return c;
    }
    return "rgb(255, 255, 255)";
  };
  const fullBorder = (s) => ["Top", "Right", "Bottom", "Left"]
    .filter((k) => px(s[`border${k}Width`]) > 0 && s[`border${k}Style`] !== "none").length >= 3;
  const isCardish = (el) => {
    const s = st(el);
    if (/^(INPUT|SELECT|TEXTAREA|BUTTON|IMG|VIDEO|CANVAS|IFRAME)$/.test(el.tagName) || el.hasAttribute("data-canvas")) return false;
    const r = el.getBoundingClientRect();
    if (r.width < 120 || r.height < 72 || r.width >= vw * 0.9) return false;
    const shadow = s.boxShadow && s.boxShadow !== "none";
    const fill = !isTransparent(s.backgroundColor) && el.parentElement && colorDist(s.backgroundColor, bgOf(el.parentElement)) > 8;
    return fullBorder(s) || shadow || fill;
  };

  const glows = [];
  const gradients = [];
  const textures = [];
  const glass = [];
  const hardShadows = [];
  const gradientText = [];
  const pills = [];
  const tiles = [];
  const radii = new Map();
  for (const el of all) {
    const s = st(el);
    const r = el.getBoundingClientRect();
    if ((s.backgroundClip === "text" || s.webkitBackgroundClip === "text") && /gradient/.test(s.backgroundImage)) {
      gradientText.push(sample(el));
    }
    for (const pseudo of [null, "::before", "::after"]) {
      const ps = pseudo ? getComputedStyle(el, pseudo) : s;
      if (pseudo && (ps.content === "none" || ps.content === "normal")) continue;
      const bi = ps.backgroundImage;
      const w = pseudo ? (px(ps.width) || r.width) : r.width;
      const h = pseudo ? (px(ps.height) || r.height) : r.height;
      if (bi && bi !== "none") {
        const label = pseudo ? `${describe(el)}${pseudo}` : describe(el);
        const placeholder = /placeholder|占位|待替换|photo|照片|image slot/i.test(`${el.className} ${el.getAttribute("aria-label") || ""} ${(el.textContent || "").slice(0, 120)}`);
        const smallTile = /repeating-/.test(bi)
          || String(ps.backgroundSize).split(",").some((v) => /px/.test(v) && px(v) > 0 && px(v) <= 120);
        if (placeholder) {
          // labeled placeholder slot: hatching marks it as provisional
        } else if (/url\(/.test(bi) && /(noise|grain|turbulence|fractal)/i.test(bi)) {
          textures.push({ selector: label, box: pageBox(r), kind: "noise" });
        } else if (/gradient/.test(bi) && smallTile && w * h >= 60000) {
          textures.push({ selector: label, box: pageBox(r), kind: "pattern" });
        } else if (/radial-gradient/.test(bi) && w >= 150 && h >= 150 && /transparent|rgba\([^)]*,\s*0(\.\d+)?\)/.test(bi)) {
          glows.push({ selector: label, box: pageBox(r) });
        } else if (/(linear|conic)-gradient/.test(bi) && (w * h >= 40000 || /^(A|BUTTON)$/.test(el.tagName))) {
          const stops = (bi.match(/rgba?\([^)]*\)/g) || []).map(parseColor).filter((c) => c && c.a >= 0.3).map(hsl);
          const chroma = stops.filter((c) => c.s >= 0.25 && c.l > 0.08 && c.l < 0.92);
          const hues = chroma.map((c) => c.h);
          const spread = hues.length >= 2 ? Math.max(...hues) - Math.min(...hues) : 0;
          const purple = chroma.some((c) => c.h >= 240 && c.h <= 300);
          if ((chroma.length >= 2 && spread >= 25) || purple) gradients.push({ selector: label, box: pageBox(r), hueSpread: Math.round(spread) });
        }
      }
      const blur = String(ps.filter).match(/blur\(([\d.]+)px\)/);
      if (blur && Number(blur[1]) >= 20 && w >= 100 && h >= 100 && (!isTransparent(ps.backgroundColor) || (bi && bi !== "none"))) {
        glows.push({ selector: pseudo ? `${describe(el)}${pseudo}` : describe(el), box: pageBox(r), blur: Number(blur[1]) });
      }
    }
    const bf = s.backdropFilter || s.webkitBackdropFilter;
    if (bf && /blur/.test(bf) && !/^(fixed|sticky)$/.test(s.position) && !el.closest("header, nav")) glass.push(sample(el, ""));
    if (s.boxShadow && s.boxShadow !== "none") {
      const parts = s.boxShadow.split(/,(?![^()]*\))/);
      const hard = parts.some((p) => {
        if (/inset/.test(p)) return false;
        const nums = (p.replace(/rgba?\([^)]*\)/, "").match(/-?[\d.]+px/g) || []).map(px);
        return nums.length >= 3 && Math.abs(nums[0]) + Math.abs(nums[1]) >= 2 && nums[2] === 0;
      });
      if (hard) hardShadows.push(sample(el, ""));
    }
    const rad = s.borderTopLeftRadius;
    const radPx = /%/.test(rad) ? (px(rad) / 100) * Math.min(r.width, r.height) : px(rad);
    const boxed = !isTransparent(s.backgroundColor) || fullBorder(s);
    if (radPx > 0 && boxed) {
      const key = radPx >= r.height / 2 - 1 ? "pill/round" : `${Math.round(radPx)}px`;
      radii.set(key, (radii.get(key) || 0) + 1);
    }
    if (boxed && r.height >= 18 && r.height <= 64 && r.width >= r.height * 1.2 && radPx >= r.height / 2 - 1) pills.push(sample(el));
    const square = r.width >= 28 && r.width <= 72 && Math.abs(r.width - r.height) <= r.width * 0.15;
    if (square && radPx >= 4 && !isTransparent(s.backgroundColor) && el.parentElement
      && colorDist(s.backgroundColor, bgOf(el.parentElement)) > 8) {
      const glyph = el.querySelector("svg, img, i");
      const textLen = (el.textContent || "").trim().length;
      if (glyph && textLen <= 2) {
        const g = glyph.getBoundingClientRect();
        if (g.width > 0 && g.width <= r.width * 0.75) tiles.push(sample(el, ""));
      }
    }
  }
  if (gradientText.length) addFp("T4", gradientText.length, gradientText);
  if (gradients.length) addFp("C3", gradients.length, gradients);
  if (glows.length) addFp("C4", glows.length, glows);
  if (glass.length) addFp("C5", glass.length, glass);
  if (hardShadows.length >= 3) addFp("C6", hardShadows.length, hardShadows);
  if (textures.length || document.querySelector("feTurbulence")) {
    addFp("C8", Math.max(1, textures.length), textures.length ? textures : [{ selector: "feTurbulence", box: null }]);
  }
  if (pills.length >= 8 && !(tokens && tokens.spec && tokens.spec.surface === "S06")) addFp("K1", pills.length, pills);
  if (tiles.length >= 3) addFp("K2", tiles.length, tiles);

  // ---- mono seasoning (T5)
  // Mono is seasoning when it styles short decorative labels (caps or tracked, no data);
  // mono for timestamps, commands, IDs, and values is doing its job.
  const mono = vis.filter((b) => {
    if (b.el.closest("code, pre, kbd, samp, td, th, time, data")) return false;
    const s = st(b.el);
    if (!/mono|menlo|consolas|courier/i.test(s.fontFamily.split(",")[0])) return false;
    if (!/\p{L}{2}/u.test(b.text) || b.text.length > 60) return false;
    if (/[\d/$_=@{}<>]|--|\.\w/.test(b.text)) return false;
    const label = s.textTransform === "uppercase" || px(s.letterSpacing) / b.fs >= 0.05
      || (/[A-Z]{3}/.test(b.text) && b.text === b.text.toUpperCase());
    return label;
  });
  if (mono.length >= 6) addFp("T5", mono.length, mono.map((b) => sample(b.el, b.text, b.u)));

  // ---- repeated groups: card grids, section template, stat strips
  const groups = [];
  for (const p of all) {
    if (!/(grid|flex)/.test(st(p).display) || p.closest("header, nav, footer")) continue;
    const kids = [...p.children].filter((k) => {
      const r = k.getBoundingClientRect();
      return r.width >= 60 && r.height >= 40;
    });
    if (kids.length < 3) continue;
    // Tag plus first class: a featured variant ("plan plan--featured") still belongs to the group.
    const sig = kids.map((k) => `${k.tagName}.${k.classList[0] || ""}`);
    const counts = new Map();
    for (const x of sig) counts.set(x, (counts.get(x) || 0) + 1);
    const [modeSig, modeCount] = [...counts.entries()].sort((a, b) => b[1] - a[1])[0];
    if (modeCount < 3) continue;
    const members = kids.filter((_, i) => sig[i] === modeSig);
    const widths = members.map((k) => k.getBoundingClientRect().width);
    if (Math.max(...widths) / Math.min(...widths) > 1.2) continue;
    const tops = members.map((k) => Math.round(k.getBoundingClientRect().top));
    const perRow = Math.max(...tops.map((t) => tops.filter((u) => Math.abs(u - t) <= 4).length));
    groups.push({ p, members, perRow, cards: members.filter(isCardish).length });
  }
  const cardGrids = groups.filter((g) => g.cards >= 3 && (g.perRow >= 3 || vw < 768));
  if (cardGrids.length) {
    addFp("S2", cardGrids.length, cardGrids.map((g) => ({ ...sample(g.p, g.members[0].textContent), items: g.members.length })));
  }
  const numeric = /^[~≈<>+\-−$¥€£]?\s*\d[\d.,:\s]*\s*(%|x|×|k|m|b|\+|h|ms|s|小时|个|天|分钟|分|年|倍|万|亿)?\s*\+?$/i;
  // A stat strip is a row of big numbers with short captions, not a set of priced cards.
  const statStrips = groups.filter((g) => !g.p.closest(".segs, .chart, [data-visual]") && g.members.filter((m) => (m.textContent || "").trim().length <= 48
    && vis.some((b) => m.contains(b.el) && b.fs >= 28 && numeric.test(b.text))).length >= 3);
  const earlyData = profileArg === "report" || profileArg === "product" || (profileArg === "auto" && [...document.querySelectorAll("table, svg, canvas")].filter((el) => {
    const r = el.getBoundingClientRect(); return r.width >= 200 && r.height >= 120;
  }).length >= 2);
  if (statStrips.length && !earlyData) addFp("S4", statStrips.length, statStrips.map((g) => sample(g.p, g.p.textContent)));
  const templated = [];
  for (const e of eyebrows) {
    const box = e.h.closest("section, article") || (e.h.parentElement && e.h.parentElement.parentElement);
    if (!box) continue;
    const hb = e.h.getBoundingClientRect().bottom;
    if (groups.some((g) => box.contains(g.p) && g.p.getBoundingClientRect().top >= hb - 2)) templated.push({ ...e.item });
  }
  if (templated.length >= 3) addFp("S1", templated.length, templated, "eyebrow + heading + repeated grid");

  // ---- decorative numbering (S6)
  // Numbers inside ordered lists and tables are real sequences (ranks, contents, steps).
  const numbered = vis.filter((b) => /^0\d(\s|[·.\-—–:|/]|$)/.test(b.text) && b.text.length <= 40 && !b.el.closest("ol, table"));
  if (numbered.length >= 3) addFp("S6", numbered.length, numbered.map((b) => sample(b.el, b.text, b.u)), "keep only where order is real");

  // ---- card inside card (S8)
  const nested = [];
  for (const el of all) {
    if (!isCardish(el) || el.closest("figure, [role='img']") || el.querySelector("pre, table, canvas")) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 200 || r.height < 120) continue;
    const inner = [...el.querySelectorAll("*")].find((d) => {
      const dr = d.getBoundingClientRect();
      return dr.width >= r.width * 0.3 && dr.width < r.width - 4 && isCardish(d);
    });
    if (inner) nested.push({ ...sample(el, ""), inner: describe(inner) });
  }
  if (nested.length) addFp("S8", nested.length, nested);

  // ---- hover lift (K3)
  const lifts = [];
  const walkRules = (rules) => {
    for (const rule of rules) {
      if (rule.cssRules && !rule.selectorText) {
        if (rule.media && !window.matchMedia(rule.media.mediaText).matches) continue;
        walkRules(rule.cssRules);
        continue;
      }
      if (!rule.selectorText || !rule.selectorText.includes(":hover")) continue;
      const t = rule.style && rule.style.transform;
      if (!t || !/translate|scale/.test(t)) continue;
      for (const part of rule.selectorText.split(",")) {
        if (!part.includes(":hover")) continue;
        let matched = [];
        try {
          matched = [...document.querySelectorAll(part.replace(/:hover/g, "").trim() || "*")];
        } catch {
          matched = [];
        }
        const big = matched.filter((m) => {
          const r = m.getBoundingClientRect();
          return r.width >= 120 && r.height >= 72;
        });
        if (big.length) lifts.push({ selector: part.trim(), transform: t, elements: big.length });
      }
    }
  };
  for (const sheet of document.styleSheets) {
    try {
      walkRules(sheet.cssRules);
    } catch {
      // cross-origin stylesheet
    }
  }
  const liftCount = lifts.reduce((n, l) => n + l.elements, 0);
  if (liftCount >= 3) addFp("K3", liftCount, lifts);

  // ---- emoji (K5)
  const emoji = vis.filter((b) => /[\u{1F000}-\u{1FAFF}\u{2728}\u{2705}\u{274C}\u{26A1}\u{2B50}\u{2764}]/u.test(b.text));
  if (emoji.length) addFp("K5", emoji.length, emoji.map((b) => sample(b.el, b.text, b.u)));

  // ---- copy (W1, W3, W7)
  const bodyText = document.body.innerText || "";
  // Headline and lede tic only; quoted prose is left to the writer.
  const contrast = vis.filter((b) => (b.el.closest("h1, h2, h3") || b.fs >= 19 || /(lede|lead|sub|intro|hero|tagline|deck)/i.test(`${b.el.className} ${b.el.parentElement ? b.el.parentElement.className : ""}`))
    && !b.el.closest("blockquote, q, figure")
    && (/,\s+not\s+(a|an|the|another|just|only)?\s*\w+/i.test(b.text) || /不是[^，。！？]{0,24}[，,]?\s*而是|而非|不只是|不止是/.test(b.text)));
  if (contrast.length >= 2) addFp("W1", contrast.length, contrast.map((b) => sample(b.el, b.text, b.u)));
  const empty = /\b(seamless(ly)?|effortless(ly)?|powerful|unlock|elevate|supercharge|empower|streamline|next-gen|cutting-edge|game-?changer|revolutioni[sz]e|world-class|best-in-class|leverage)\b|赋能|一站式|全方位|沉浸式|打造|助力|极致|无缝|颠覆|引领/gi;
  const emptyHits = bodyText.match(empty) || [];
  if (emptyHits.length >= 3) {
    const tally = {};
    for (const w of emptyHits) tally[w.toLowerCase()] = (tally[w.toLowerCase()] || 0) + 1;
    addFp("W3", emptyHits.length, Object.entries(tally).map(([w, n]) => ({ text: w, count: n })));
  }
  const dashes = (bodyText.match(/——|—/g) || []).length;
  const chars = bodyText.replace(/\s/g, "").length || 1;
  if (dashes >= 4 && (dashes / chars) * 1000 >= 2.5) {
    addFp("W7", dashes, [{ text: `${dashes} dashes in ${chars} characters`, perThousand: Math.round((dashes / chars) * 10000) / 10 }]);
  }

  // ---- dead half sections (desktop)
  if (desktop) {
    const lefts = headings.map((h) => headingLeft(h)).filter(Boolean).map((u) => u.left).sort((a, b) => a - b);
    const rights = vis.filter((b) => b.u.right - b.u.left > 40 && b.u.right < vw).map((b) => b.u.right).sort((a, b) => a - b);
    if (lefts.length && rights.length) {
      const L = lefts[Math.floor(lefts.length / 2)];
      const R = rights[Math.floor(rights.length * 0.95)];
      const frame = R - L;
      const sections = new Set([...document.querySelectorAll("section, main > *, body > *")].filter((s) => {
        const r = s.getBoundingClientRect();
        return r.height >= 280 && r.width >= vw * 0.6 && !/^(HEADER|NAV|FOOTER|SCRIPT|STYLE)$/.test(s.tagName);
      }));
      const dead = [];
      for (const s of sections) {
        if ([...sections].some((o) => o !== s && s.contains(o))) continue;
        const boxes = vis.filter((b) => s.contains(b.el)).map((b) => b.u);
        for (const m of s.querySelectorAll("img, svg, video, canvas, iframe, input, select, textarea, button, hr")) {
          const r = m.getBoundingClientRect();
          if (r.width >= 24 && r.height >= 1) boxes.push(r);
        }
        for (const c of s.querySelectorAll("*")) {
          if (isCardish(c)) { boxes.push(c.getBoundingClientRect()); continue; }
          const cs = st(c);
          const ruled = (px(cs.borderTopWidth) > 0 && cs.borderTopStyle !== "none") || (px(cs.borderBottomWidth) > 0 && cs.borderBottomStyle !== "none");
          if (ruled) { const r = c.getBoundingClientRect(); if (r.width >= 200) boxes.push(r); }
        }
        if (!boxes.length) continue;
        const u = union(boxes);
        if (u.bottom - u.top >= 200 && u.left - L < frame * 0.15 && u.right < L + frame * 0.62) {
          dead.push({ ...sample(s, s.textContent, s.getBoundingClientRect()), contentRight: Math.round(u.right), frameRight: Math.round(R) });
        }
      }
      if (dead.length) addDefect("dead-half", "warn", "A section fills less than ~60% of the content frame and leaves the rest empty (S9).", dead);
    }
  }

  // ---- text drawn on top of other text (a region that overflowed into its neighbor)
  {
    const pinned = (el) => {
      for (let a = el; a && a !== document.body; a = a.parentElement) if (/^(fixed|sticky)$/.test(st(a).position)) return true;
      return false;
    };
    // clip each line box by every ancestor that clips overflow (closed accordions, scrollers, masked panels)
    const clipCache = new Map();
    const clipOf = (el) => {
      if (clipCache.has(el)) return clipCache.get(el);
      let box = { left: -Infinity, top: -Infinity, right: Infinity, bottom: Infinity };
      for (let a = el.parentElement; a && a !== document.documentElement; a = a.parentElement) {
        const s = st(a);
        if (s.overflowX !== "visible" || s.overflowY !== "visible" || s.contain.includes("paint")) {
          const r = a.getBoundingClientRect();
          box = { left: Math.max(box.left, r.left), top: Math.max(box.top, r.top), right: Math.min(box.right, r.right), bottom: Math.min(box.bottom, r.bottom) };
        }
      }
      clipCache.set(el, box);
      return box;
    };
    // Confirm at the overlap point that both texts are painted there and no opaque box sits between them.
    const opaque = (el) => { const c = parseColor(st(el).backgroundColor); return c && c.a > 0.9; };
    const paintedTogether = (A, B) => {
      const x = (Math.max(A.r.left, B.r.left) + Math.min(A.r.right, B.r.right)) / 2;
      const docY = (Math.max(A.r.top, B.r.top) + Math.min(A.r.bottom, B.r.bottom)) / 2 + sy;
      window.scrollTo(0, Math.max(0, docY - vh / 2));
      const y = docY - window.scrollY;
      const stack = document.elementsFromPoint(x, y);
      window.scrollTo(sx, sy);
      const at = (el) => stack.findIndex((e) => e === el || el.contains(e));
      const ia = at(A.b.el); const ib = at(B.b.el);
      if (ia < 0 || ib < 0) return false;
      const top = Math.min(ia, ib); const bottom = Math.max(ia, ib);
      const lower = ia > ib ? A.b.el : B.b.el;
      for (let k = top + 1; k < bottom; k += 1) if (opaque(stack[k]) && !stack[k].contains(lower)) return false;
      return true;
    };
    const R = [];
    const shown = (el) => (typeof el.checkVisibility === "function"
      ? el.checkVisibility({ contentVisibilityAuto: true, opacityProperty: true, visibilityProperty: true })
      : true) && !el.closest("details:not([open]) > :not(summary)");
    for (const b of vis) {
      if (pinned(b.el) || !shown(b.el)) continue;
      const clip = clipOf(b.el);
      // keep the middle of each line box: display type with tight leading has content boxes taller than its ink
      for (const r0 of b.rects) {
        const r = { left: Math.max(r0.left, clip.left), right: Math.min(r0.right, clip.right), top: Math.max(r0.top, clip.top), bottom: Math.min(r0.bottom, clip.bottom) };
        if (r.right - r.left <= 3 || r.bottom - r.top <= 3) continue;
        const inset = (r.bottom - r.top) * 0.2;
        R.push({ b, r: { left: r.left, right: r.right, top: r.top + inset, bottom: r.bottom - inset, width: r.right - r.left, height: r.bottom - r.top - 2 * inset } });
      }
    }
    R.sort((p, q) => p.r.top - q.r.top);
    const hits = [];
    const seen = new Set();
    for (let i = 0; i < R.length && hits.length < 12; i += 1) {
      const A = R[i];
      for (let j = i + 1; j < R.length; j += 1) {
        const B = R[j];
        if (B.r.top >= A.r.bottom) break;
        if (A.b === B.b) continue;
        const w = Math.min(A.r.right, B.r.right) - Math.max(A.r.left, B.r.left);
        const h = Math.min(A.r.bottom, B.r.bottom) - Math.max(A.r.top, B.r.top);
        if (w <= 0 || h <= 0) continue;
        const small = Math.min(A.r.width * A.r.height, B.r.width * B.r.height);
        if (w * h <= 0.3 * small) continue;
        const key = [A.b.text, B.b.text].sort().join("|");
        if (seen.has(key)) continue;
        seen.add(key);
        if (!paintedTogether(A, B)) continue;
        hits.push({ ...sample(A.b.el, `"${snippet(A.b.text, 30)}" overlaps "${snippet(B.b.text, 30)}"`, A.r) });
        break;
      }
    }
    if (hits.length) addDefect("text-overlap", "fail", "Text is drawn on top of other text; a block overflowed its region or was positioned over content.", hits);
  }

  // ---- unfinished-looking pages: no visual anchor, content stuck to one side, empty bands, hidden answers, repeated facts
  const pageBg = st(document.body).backgroundColor;
  const visualBoxes = (root, minArea, ground = pageBg) => [...root.querySelectorAll("img, svg, canvas, video, picture, [class], [style]")].filter((el) => {
    const r = el.getBoundingClientRect();
    if (r.width * r.height < minArea || r.width >= vw * 0.98) return false;
    if (el.closest("svg") && el.tagName.toLowerCase() !== "svg") return false;
    if (/^(IMG|SVG|CANVAS|VIDEO|PICTURE)$/i.test(el.tagName) || el.matches(".segs, .chart, .windows, [data-visual]")) return true;
    const s = st(el);
    const bg = s.backgroundColor;
    return !isTransparent(bg) && colorDist(bg, ground) > 40;
  }).map((el) => el.getBoundingClientRect());
  if (!canvasEls.length) {
    if (vw >= 1200) {
      const body = vis.filter((b) => b.u.top + sy > 120 && b.u.top + sy < vh * 3 && b.fs >= 12 && !b.el.closest("nav, header, footer, aside"));
      if (body.length > 8) {
        const left = Math.min(...body.map((b) => b.u.left)); const right = Math.max(...body.map((b) => b.u.right));
        if (vw - right > vw * 0.3 && left < vw * 0.22) {
          addDefect("narrow-content", "warn", "Content is stuck to one side with a wide empty area beside it; widen the layout or use the space.", [{ selector: "main content", text: `content spans ${Math.round(left)}–${Math.round(right)}px of ${vw}px` }]);
        }
      }
    }
    const spans = vis.map((b) => [b.u.top + sy, b.u.bottom + sy]).concat(visualBoxes(document.body, 4000).map((r) => [r.top + sy, r.bottom + sy]));
    spans.sort((a, b) => a[0] - b[0]);
    const gaps = [];
    let cursor = spans.length ? spans[0][1] : 0;
    for (const [t, bt] of spans) { if (t - cursor > vh * 0.45) gaps.push({ selector: "page", text: `${Math.round(t - cursor)}px empty band at y=${Math.round(cursor)}` }); cursor = Math.max(cursor, bt); }
    if (gaps.length) addDefect("empty-band", "warn", "Large empty vertical bands make the page look unfinished.", gaps);
  }
  {
    const det = [...document.querySelectorAll("details")].filter((d) => d.getBoundingClientRect().height > 0);
    if (det.length >= 3 && !det.some((d) => d.open)) {
      addDefect("hidden-answers", "warn", "Every accordion is closed, so screenshots and skimmers never see an answer; open the first one or show short answers.", [{ ...sample(det[0], det[0].textContent) }]);
    }
  }

  // ---- canvases: exact size, readable type at the delivered size, safe area, one idea per card
  if (canvasEls.length) {
    const SPEC = {
      xhs: { width: 1080, height: 1440, safe: 80, min_font: 30, max_chars: 140 },
      square: { width: 1080, height: 1080, safe: 72, min_font: 28, max_chars: 110 },
      story: { width: 1080, height: 1920, safe: 110, min_font: 32, max_chars: 120 },
      poster: { width: 1200, height: 1600, safe: 80, min_font: 22, max_chars: 220 },
      slide: { width: 1920, height: 1080, safe: 96, min_font: 24, max_chars: 450 },
    };
    const wrongSize = []; const tiny = []; const unsafe = []; const tight = []; const overflow = []; const heavy = []; const sprawl = []; const empty = []; let withVisual = 0; let coverTextOnly = false;
    canvasEls.forEach((c, idx) => {
      const spec = SPEC[c.dataset.canvas] || (tokens && tokens.canvas && tokens.canvas.width ? tokens.canvas : null);
      if (!spec) return;
      const cr = c.getBoundingClientRect();
      const label = `canvas ${idx + 1} (${c.dataset.canvas}${c.dataset.name ? ` ${c.dataset.name}` : ""})`;
      if (Math.abs(cr.width - spec.width) > 1 || Math.abs(cr.height - spec.height) > 1) {
        wrongSize.push({ ...sample(c, `${label} renders ${Math.round(cr.width)}x${Math.round(cr.height)}, expected ${spec.width}x${spec.height}`) });
      }
      const inside = vis.filter((b) => c.contains(b.el));
      let chars = 0;
      const sizes = new Set();
      for (const b of inside) {
        chars += b.text.replace(/\s+/g, "").length;
        sizes.add(Math.round(b.fs));
        if (b.fs < spec.min_font - 0.5) tiny.push({ ...sample(b.el, `${label} ${Math.round(b.fs)}px < ${spec.min_font}px: ${b.text}`, b.u) });
        const m = Math.min(b.u.left - cr.left, b.u.top - cr.top, cr.right - b.u.right, cr.bottom - b.u.bottom);
        if (m < -1) overflow.push({ ...sample(b.el, `${label}: ${b.text}`, b.u) });
        else if (m < spec.safe * 0.5) unsafe.push({ ...sample(b.el, `${label} ${Math.round(m)}px from edge: ${b.text}`, b.u) });
        else if (m < spec.safe * 0.85) tight.push({ ...sample(b.el, `${label} ${Math.round(m)}px from edge: ${b.text}`, b.u) });
      }
      for (const t of c.querySelectorAll("svg text")) {
        const svg = t.closest("svg");
        const vb = svg.viewBox && svg.viewBox.baseVal;
        const k = vb && vb.width ? svg.getBoundingClientRect().width / vb.width : 1;
        const size = px(st(t).fontSize) * k;
        if (t.textContent.trim() && size < spec.min_font - 0.5) tiny.push({ ...sample(t, `${label} chart text ${Math.round(size)}px < ${spec.min_font}px: ${t.textContent}`) });
      }
      // empty bands: project text, media, and filled boxes onto the vertical axis between the safe margins
      const spans = inside.map((b) => [b.u.top, b.u.bottom]);
      for (const el of c.querySelectorAll("img, svg, video, canvas, [class]")) {
        const r = el.getBoundingClientRect();
        if (r.width < 40 || r.height < 24 || el === c) continue;
        const s2 = st(el);
        const filled = /^(IMG|SVG|VIDEO|CANVAS)$/i.test(el.tagName) || (!isTransparent(s2.backgroundColor) && s2.backgroundColor !== st(c).backgroundColor) || fullBorder(s2);
        if (filled && r.height < cr.height * 0.9) spans.push([r.top, r.bottom]);
      }
      spans.sort((a, b) => a[0] - b[0]);
      let cursor = cr.top + spec.safe; let gap = 0;
      for (const [t, bt] of spans) { if (t > cursor) gap = Math.max(gap, t - cursor); cursor = Math.max(cursor, bt); }
      gap = Math.max(gap, cr.bottom - spec.safe - cursor);
      const cover = c.querySelector("h1") || /cover|title|封面/i.test(c.dataset.name || "");
      if (!cover && gap > cr.height * 0.28) empty.push({ ...sample(c, `${label}: ${Math.round(gap)}px empty band (${Math.round((gap / cr.height) * 100)}% of the height)`) });
      const cardVisuals = visualBoxes(c, cr.width * cr.height * 0.04, st(c).backgroundColor).filter((r) => r.width < cr.width * 0.98 || r.height < cr.height * 0.98);
      if (cardVisuals.length) withVisual += 1; else if (idx === 0) coverTextOnly = true;
      if (chars > spec.max_chars) heavy.push({ ...sample(c, `${label}: ${chars} characters (limit ${spec.max_chars})`), chars });
      if (sizes.size > 6) sprawl.push({ ...sample(c, `${label}: ${sizes.size} text sizes (${[...sizes].sort((a, b) => a - b).join(", ")})`) });
    });
    if (wrongSize.length) addDefect("canvas-size", "fail", "A canvas does not render at its declared pixel size; content is forcing the box to grow or the size is hand-set.", wrongSize);
    if (overflow.length) addDefect("canvas-overflow", "fail", "Text runs outside its canvas and will be cut off in the exported image.", overflow);
    if (tiny.length) addDefect("canvas-min-font", "fail", "Text is smaller than the canvas minimum; it will be unreadable on a phone feed or projector.", tiny);
    if (unsafe.length) addDefect("canvas-safe-area", "fail", "Text sits inside the outer half of the safe margin; platforms crop and overlay UI there.", unsafe);
    if (tight.length) addDefect("canvas-safe-tight", "warn", "Text is inside the safe margin.", tight);
    const hard = heavy.filter((h) => h.chars > 1.5 * (SPEC[canvasEls[0].dataset.canvas] || { max_chars: 1e9 }).max_chars);
    if (heavy.length) addDefect("canvas-text-load", hard.length ? "fail" : "warn", "A card carries more text than one idea needs; split it or cut it.", heavy);
    if (sprawl.length) addDefect("canvas-type-sprawl", "warn", "A single canvas uses more than six text sizes.", sprawl);
    if (empty.length) addDefect("canvas-empty-band", "warn", "A canvas has a large empty band; fill the card (bigger type, .cv-body--fill or --spread) or cut it to a smaller format.", empty);
  }

  // ---- system adherence: colors, sizes, and fonts must come from the chosen style tokens
  if (tokens) {
    const toLab = (c) => {
      const f = (v) => { const x = v / 255; return x <= 0.04045 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4; };
      const r = f(c.r); const g = f(c.g); const b = f(c.b);
      const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
      const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
      const s2 = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
      return [0.2104542553 * l + 0.793617785 * m - 0.0040720468 * s2, 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s2, 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s2];
    };
    const hexToC = (h) => ({ r: parseInt(h.slice(1, 3), 16), g: parseInt(h.slice(3, 5), 16), b: parseInt(h.slice(5, 7), 16) });
    const palette = [...Object.values(tokens.colors), "#ffffff", "#111111"].map((h) => toLab(hexToC(h)));
    const onSystem = (c) => { const x = toLab(c); return palette.some((p) => Math.hypot(p[0] - x[0], p[1] - x[1], p[2] - x[2]) <= 0.025); };
    const off = new Map();
    const note = (colorStr, el, where) => {
      const c = parseColor(colorStr);
      if (!c || c.a < 0.5) return;
      if (onSystem(c)) return;
      const key = `rgb(${Math.round(c.r)}, ${Math.round(c.g)}, ${Math.round(c.b)})`;
      if (!off.has(key)) off.set(key, { color: key, where, ...sample(el, "") });
    };
    for (const b of vis) note(st(b.el).color, b.el, "text");
    for (const el of all) {
      const s = st(el);
      if (el.closest("svg") && el.tagName.toLowerCase() !== "svg") {
        if (s.fill && s.fill !== "none") note(s.fill, el, "svg fill");
        if (s.stroke && s.stroke !== "none") note(s.stroke, el, "svg stroke");
        continue;
      }
      note(s.backgroundColor, el, "background");
      for (const side of ["Top", "Right", "Bottom", "Left"]) if (px(s[`border${side}Width`]) > 0 && s[`border${side}Style`] !== "none") note(s[`border${side}Color`], el, "border");
    }
    if (off.size) {
      addDefect("off-system-color", off.size >= 4 ? "fail" : "warn", `${off.size} color(s) are not in the chosen style's palette; use var(--role) tokens instead of hand-typed values.`, [...off.values()]);
    }
    const allowed = vw < 768 && tokens.fontSizes.mobile.length ? [...tokens.fontSizes.mobile, ...tokens.fontSizes.desktop] : tokens.fontSizes.desktop;
    const offSizes = new Map();
    for (const b of vis) {
      if (allowed.some((a) => Math.abs(a - b.fs) <= 1.01) || b.el.closest("svg")) continue;
      const k = Math.round(b.fs * 2) / 2;
      if (!offSizes.has(k)) offSizes.set(k, { size: k, ...sample(b.el, b.text, b.u) });
    }
    if (offSizes.size) {
      addDefect("off-scale-size", offSizes.size >= 4 ? "fail" : "warn", `${offSizes.size} font size(s) are off the generated type scale; use var(--fs-*) tokens.`, [...offSizes.values()]);
    }
    const fontNames = new Set(Object.values(tokens.fonts).map((f) => f.toLowerCase()));
    const offFonts = new Map();
    for (const b of vis) {
      const first = st(b.el).fontFamily.split(",")[0].replace(/["']/g, "").trim().toLowerCase();
      if (fontNames.has(first) || /^(-apple-system|system-ui|ui-monospace|sans-serif|serif|monospace)$/.test(first)) continue;
      if (!offFonts.has(first)) offFonts.set(first, { font: first, ...sample(b.el, b.text, b.u) });
    }
    if (offFonts.size) addDefect("off-system-font", "warn", "Text uses font families outside the chosen type pairing.", [...offFonts.values()]);
  }

  // ---- system discipline metrics
  const families = {};
  const sizes = {};
  const colors = {};
  for (const b of vis) {
    const f = st(b.el).fontFamily.split(",")[0].replace(/["']/g, "").trim();
    families[f] = (families[f] || 0) + b.text.length;
    const size = Math.round(b.fs * 2) / 2;
    sizes[size] = (sizes[size] || 0) + 1;
    const c = st(b.el).color;
    colors[c] = (colors[c] || 0) + 1;
  }
  const metrics = {
    fontFamilies: families,
    fontSizeCount: Object.keys(sizes).length,
    fontSizes: Object.keys(sizes).map(Number).sort((a, b) => a - b),
    textColorCount: Object.keys(colors).length,
    radii: Object.fromEntries([...radii.entries()].sort((a, b) => b[1] - a[1])),
  };
  if (Object.keys(families).length > 3) {
    addDefect("type-family-sprawl", "warn", `${Object.keys(families).length} font families render on the page.`, Object.keys(families).map((f) => ({ text: f })));
  }
  if (metrics.fontSizeCount > 10) {
    addDefect("type-scale-sprawl", "warn", `${metrics.fontSizeCount} distinct font sizes; a disciplined page usually needs 5-8.`, [{ text: metrics.fontSizes.join(", ") }]);
  }
  const radiusKinds = [...radii.keys()].filter((k) => k !== "pill/round");
  if (radiusKinds.length > 5) {
    addDefect("radius-sprawl", "warn", `${radiusKinds.length} distinct corner radii on boxed elements.`, [{ text: radiusKinds.join(", ") }]);
  }

  // ---- text contrast (WCAG 2.x), skipping text that sits over imagery we cannot sample
  const lum = ({ r, g, b }) => {
    const f = (c) => { const v = c / 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const blend = (fg, bg) => ({ r: fg.r * fg.a + bg.r * (1 - fg.a), g: fg.g * fg.a + bg.g * (1 - fg.a), b: fg.b * fg.a + bg.b * (1 - fg.a), a: 1 });
  const mediaRects = all.filter((el) => {
    const t = el.tagName;
    if (/^(IMG|VIDEO|CANVAS|PICTURE|IFRAME)$/.test(t) || t.toLowerCase() === "svg") return true;
    const bi = st(el).backgroundImage;
    return bi && bi !== "none";
  }).map((el) => ({ el, r: el.getBoundingClientRect() }));
  const overImagery = (b) => mediaRects.some(({ el, r }) => {
    if (b.el.contains(el)) return false;
    const w = Math.min(b.u.right, r.right) - Math.max(b.u.left, r.left);
    const h = Math.min(b.u.bottom, r.bottom) - Math.max(b.u.top, r.top);
    return w > 0 && h > 0 && w * h > 0.3 * (b.u.right - b.u.left) * (b.u.bottom - b.u.top);
  });
  const backgroundOf = (el) => {
    const layers = [];
    for (let a = el; a; a = a.parentElement) {
      const c = parseColor(st(a).backgroundColor);
      if (c && c.a > 0.02) {
        layers.push(c);
        if (c.a >= 0.99) break;
      }
    }
    let base = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = layers.length - 1; i >= 0; i -= 1) base = blend(layers[i], base);
    return base;
  };
  const lowContrast = [];
  const failContrast = [];
  for (const b of vis) {
    if (b.text.length < 2 || b.el.closest("[disabled], [aria-disabled='true'], [aria-hidden='true']") || overImagery(b)) continue;
    const fg0 = parseColor(st(b.el).color);
    if (!fg0) continue;
    const bg = backgroundOf(b.el);
    const fg = blend({ ...fg0, a: fg0.a * Math.min(1, b.op) }, bg);
    const l1 = lum(fg);
    const l2 = lum(bg);
    const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    const weight = Number.parseInt(st(b.el).fontWeight, 10) || 400;
    const large = b.fs >= 24 || (weight >= 700 && b.fs >= 18.66);
    const need = large ? 3 : 4.5;
    if (ratio >= need) continue;
    const item = { ...sample(b.el, b.text, b.u), ratio: Math.round(ratio * 100) / 100, need };
    if (ratio < 3) failContrast.push(item);
    else lowContrast.push(item);
  }
  if (failContrast.length) addDefect("contrast-fail", "fail", "Text contrast is below 3:1 against its background.", failContrast);
  if (lowContrast.length) addDefect("contrast-low", "warn", "Text contrast is below WCAG AA (4.5:1, or 3:1 for large text).", lowContrast);

  // ---- a visible, button-like primary action on the first screen
  const firstActions = [...document.querySelectorAll("a, button, [role='button'], input[type='submit']")].filter((el) => {
    const r = el.getBoundingClientRect();
    if (r.width < 40 || r.height < 28 || r.top + sy >= vh || r.bottom + sy <= 0 || effOpacity(el) <= 0.05) return false;
    const text = (el.textContent || el.value || "").trim();
    if (!text || text.length > 24) return false;
    const s = st(el);
    const filled = !isTransparent(s.backgroundColor) && el.parentElement && colorDist(s.backgroundColor, bgOf(el.parentElement)) > 30;
    return filled || fullBorder(s);
  });
  // A first screen led by tables or charts is a data surface (report, dashboard, settings), not a pitch.
  const dataBlocks = [...document.querySelectorAll("table, svg, canvas")].filter((el) => {
    const r = el.getBoundingClientRect();
    return r.width >= 200 && r.height >= 120 && r.top + sy < vh * 2;
  }).length;
  const dataSurface = profileArg === "report" || profileArg === "product" || profileArg === "canvas"
    || (profileArg === "auto" && dataBlocks >= 2);
  if (!firstActions.length && !dataSurface) {
    addDefect("no-first-screen-action", "warn", "The first screen has no visible button-style action; confirm the page does not need one.", [{ selector: "first screen", text: "" }]);
  }

  // ---- tables that hide columns behind a horizontal scroll on small screens
  if (vw < 768) {
    const hiddenCols = [];
    for (const el of all) {
      const s = st(el);
      if (s.overflowX !== "auto" && s.overflowX !== "scroll") continue;
      if (el.scrollWidth <= el.clientWidth + 8) continue;
      if (!(el.tagName === "TABLE" || el.querySelector("table, [role='table'], [role='grid']"))) continue;
      const hiddenShare = 1 - el.clientWidth / el.scrollWidth;
      if (hiddenShare > 0.2) hiddenCols.push({ ...sample(el, el.textContent), hiddenShare: Math.round(hiddenShare * 100) / 100 });
    }
    if (hiddenCols.length) {
      addDefect("mobile-hidden-columns", "warn", "On a phone this table hides columns behind a sideways scroll; restack rows or cut columns.", hiddenCols);
    }
  }

  // Figures (prices, counts, percentages) outside chrome, for the desktop/phone parity check.
  const figureRe = /[¥$€£]\s?\d[\d,.]*|\d[\d,.]*\s?(%|元|GB|TB|MB|万|亿|小时|分钟|\/mo|\/yr|\/月|\/年)/g;
  const figures = new Set();
  for (const b of vis) {
    if (b.el.closest("header, nav, footer, svg")) continue;
    for (const m of b.text.matchAll(figureRe)) figures.add(m[0].replace(/\s+/g, ""));
  }
  const allText = vis.map((b) => b.text).join(" ").replace(/\s+/g, "");

  // ---- sterile signals: the template removed and nothing put in its place
  const placeholderRe = /placeholder|占位|待替换|图片位|照片位|image slot|photo slot/i;
  // Generated content (::before/::after) is visible text too.
  const pseudoText = (el) => ["::before", "::after"].map((ps) => {
    const c = getComputedStyle(el, ps).content;
    return c && c !== "none" && c !== "normal" && /^["']/.test(c) ? c.slice(1, -1) : "";
  }).join(" ").trim();
  const phCandidates = [];
  for (const el of all) {
    const r = el.getBoundingClientRect();
    const top = r.top + sy;
    const visibleInFirst = Math.min(r.bottom + sy, vh) - Math.max(top, 0);
    if (visibleInFirst <= 0 || r.width * Math.min(r.height, visibleInFirst) < vw * vh * 0.1) continue;
    const own = (el.textContent || "").trim();
    const text = `${own.length <= 240 ? own : ""} ${pseudoText(el)} ${typeof el.className === "string" ? el.className : ""}`;
    if (!placeholderRe.test(text)) continue;
    phCandidates.push(el);
  }
  const phHero = phCandidates.filter((el) => !phCandidates.some((o) => o !== el && el.contains(o)));
  if (phHero.length) addFp("Z2", phHero.length, phHero.map((el) => sample(el)));

  const leakRe = /replace with|to be replaced|swap in|do not hotlink|hotlink|\bTODO\b|lorem ipsum|\bassumed\b|placeholder link|请替换|待替换|建议替换|请勿|外链|图床|待确认|请核对|样本数据|示意数据|示例数据|sample data|illustrative only/i;
  const leaks = vis.filter((b) => !b.el.closest("code, pre, script") && leakRe.test(b.text)).map((b) => sample(b.el, b.text, b.u));
  for (const el of all) {
    const t = pseudoText(el);
    if (t && leakRe.test(t)) leaks.push(sample(el, t));
  }
  if (leaks.length) addFp("Z3", leaks.length, leaks);

  const pageArea = Math.max(1, document.documentElement.scrollWidth * document.documentElement.scrollHeight);
  const chromatic = (c) => {
    const p = parseColor(c);
    if (!p || p.a < 0.5) return false;
    const h = hsl(p);
    return h.s >= 0.25 && h.l > 0.12 && h.l < 0.9;
  };
  let chromaArea = 0;
  for (const el of all) {
    if (!chromatic(st(el).backgroundColor)) continue;
    const r = el.getBoundingClientRect();
    chromaArea += r.width * r.height;
  }
  const totalChars = vis.reduce((n, b) => n + b.text.length, 0) || 1;
  const chromaChars = vis.filter((b) => chromatic(st(b.el).color)).reduce((n, b) => n + b.text.length, 0);
  const imagery = [...document.querySelectorAll("img, picture, video, canvas, svg")].filter((m) => {
    const r = m.getBoundingClientRect();
    return r.width >= 120 && r.height >= 80 && effOpacity(m) > 0.05;
  }).length;
  const chromaShare = chromaArea / pageArea;
  const chromaTextShare = chromaChars / totalChars;
  if (chromaShare < 0.03 && chromaTextShare < 0.03 && imagery === 0) {
    addFp("Z1", 1, [{ selector: "body", text: `color area ${(chromaShare * 100).toFixed(1)}%, colored text ${(chromaTextShare * 100).toFixed(1)}%, no imagery or charts`, box: { x: 0, y: 0, w: vw, h: vh } }]);
  }

  for (const f of Object.values(fp)) {
    f.firstViewport = f.samples.some((s) => s.box && s.box.y < vh);
  }
  return { viewport: { width: vw, height: vh }, defects, fingerprints: Object.values(fp), metrics, figures: [...figures], allText };
}

// ---------------------------------------------------------------- runner

async function scrollThrough(page) {
  const height = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < height + stepPx * 2; y += stepPx) {
    await page.mouse.wheel(0, stepPx);
    await page.waitForTimeout(stepWaitMs);
    await page.evaluate(markSeen);
  }
  // Pages with `scroll-behavior: smooth` would still be animating back up; force an instant return.
  await page.evaluate(() => {
    document.documentElement.style.scrollBehavior = "auto";
    if (document.body) document.body.style.scrollBehavior = "auto";
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });
  });
  await page.waitForFunction(() => window.scrollY === 0, null, { timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(500);
}

function verdictFor(result) {
  const page = result.fingerprints.length;
  const first = result.fingerprints.filter((f) => f.firstViewport).length;
  result.density = { page, firstViewport: first };
  if (first >= 3 || page >= 6) return "reads-as-template";
  if (page > 0) return "fingerprints-present";
  return "clean";
}

mkdirSync(path.join(outputDir, "screenshots"), { recursive: true });
const browser = await launchPinnedChromium();
const results = [];
try {
  for (const vp of viewports) {
    const context = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, deviceScaleFactor: 1 });
    const page = await context.newPage();
    await page.goto(target, { waitUntil: "load" });
    await page.waitForTimeout(waitMs);
    const hiddenAtLoad = await page.evaluate(tagTextElements);
    await page.evaluate(markSeen);
    await scrollThrough(page);
    const result = await page.evaluate(analyzePage, { hiddenAtLoad, profileArg: profile, tokens: styleTokens });
    for (const f of result.fingerprints) f.name = FINGERPRINT_NAMES[f.id] || f.id;
    result.name = vp.name;
    result.verdict = verdictFor(result);
    const firstShot = path.join(outputDir, "screenshots", `${vp.name}-first.png`);
    const fullShot = path.join(outputDir, "screenshots", `${vp.name}-full.png`);
    await page.screenshot({ path: firstShot });
    await page.screenshot({ path: fullShot, fullPage: true });
    result.screenshots = { first: firstShot, full: fullShot };
    results.push(result);
    await context.close();
  }
} finally {
  await browser.close();
}

// Figures a desktop reader sees that never render on the phone (for example prices dropped from a stacked table).
const desk = results.find((r) => r.viewport.width >= 1024);
const phone = results.find((r) => r.viewport.width < 768);
if (desk && phone) {
  const missing = desk.figures.filter((f) => !phone.allText.includes(f));
  if (missing.length) {
    phone.defects.push({
      id: "mobile-lost-content",
      severity: "warn",
      message: "Figures shown on desktop do not appear anywhere on the phone layout.",
      samples: missing.slice(0, 12).map((f) => ({ text: f })),
    });
  }
}
for (const r of results) {
  delete r.figures;
  delete r.allText;
}

const failCount = results.reduce((n, r) => n + r.defects.filter((d) => d.severity === "fail").length, 0);
const templated = results.some((r) => r.verdict === "reads-as-template");
const report = {
  tool: "detect_slop",
  input: isUrl ? inputArg : path.resolve(inputArg),
  generatedAt: new Date().toISOString(),
  catalog: "references/slop-fingerprints.md",
  note: "Defects are render facts. Fingerprints are taste signals for the critique; judge them against the content reason, then look at the screenshots.",
  results,
  summary: {
    status: failCount ? "fail" : templated ? "reads-as-template" : "pass",
    failDefects: failCount,
    verdicts: Object.fromEntries(results.map((r) => [r.name, r.verdict])),
  },
};
const reportPath = path.join(outputDir, "slop-report.json");
writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`);

if (args.json) {
  console.log(JSON.stringify(report, null, 2));
} else {
  console.log(`detect_slop: ${report.input}`);
  for (const r of results) {
    const fails = r.defects.filter((d) => d.severity === "fail").length;
    const warns = r.defects.filter((d) => d.severity === "warn").length;
    console.log(`\n[${r.name} ${r.viewport.width}x${r.viewport.height}] verdict: ${r.verdict} · defects: ${fails} fail, ${warns} warn · fingerprints: page ${r.density.page}, first viewport ${r.density.firstViewport}`);
    for (const d of r.defects) {
      const first = d.samples[0] || {};
      const where = first.box ? ` @(${first.box.x},${first.box.y})` : "";
      console.log(`  ${d.severity.toUpperCase().padEnd(4)} ${d.id.padEnd(22)} ×${d.samples.length} ${first.selector || ""} "${first.text || ""}"${where}${first.lastLine ? ` last line: "${first.lastLine}"` : ""}`);
    }
    for (const f of r.fingerprints) {
      const first = f.samples[0] || {};
      console.log(`  FP   ${`${f.id} ${f.name}`.padEnd(30)} ×${f.count}${f.firstViewport ? " (first viewport)" : ""} ${first.selector || ""} ${first.text ? `"${first.text}"` : ""}`);
    }
  }
  console.log(`\nreport: ${reportPath}`);
}

process.exit(failCount || (args.strict && templated) ? 1 : 0);
