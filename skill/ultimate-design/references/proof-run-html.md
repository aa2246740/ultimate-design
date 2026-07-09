# HTML Proof Run

Use this branch for Pi, weak/local/headless models, and evals that must prove an HTML artifact followed Ultimate Design. The goal is a small evidence loop: visible artifact, compact contract, coupled markers, proof command, repair, rerun.

## Required Reading

Read only this short branch plus:

- `SKILL.md`
- the relevant branch file: `branch-marketing-site.md` or `branch-web-product.md`
- `content-model.md`
- `design-contract.md`
- `visual-verification.md`
- `quality-gates.md`
- `design-okf/systems/motion-contract.md` only when animation is requested or claimed

Record these exact paths in `DESIGN.md` under `## OKF Preflight`.

## Execution Order

1. Write `index.html` first. It must contain real content, responsive structure, visible labels, and final-ish layout before the full contract.
2. Write a compact `DESIGN.md`. Keep typography token `fontSize` values scalar: `px`, `rem`, or `em`; do not use `clamp()`, `vw`, or viewport-scaled type tokens.
3. Add `data-ud-check` to intentional readable zones at one hierarchy level. Good examples: `hero-title`, `hero-lead`, `case-grid`, `services-list`, `contact-form`. Avoid marking both a parent section and all of its children.
4. Add motion markers only for behavior you implement. Every selector in `data-ud-motion-trigger`, `data-ud-motion-end-trigger`, and `data-ud-motion-subject` must resolve in the DOM.
5. Run the unified proof command:

```bash
node <ultimate-design>/scripts/run_html_proof.mjs --html index.html --design DESIGN.md --out .ultimate-design/proof
```

6. If the command fails, read `.ultimate-design/proof/repair-brief.md` first, then `.ultimate-design/proof/html-proof-report.json` only if more detail is needed. Repair the failing layer and rerun once before final response. A proof run that cannot pass must report `failed` and link the report path.

## Motion Choice

Choose the trigger from the watched visual subject:

- Subject already visible on first viewport: use `entry-play` or `static`.
- Subject enters later and scroll progress is not the story: use `view-entry`.
- Visibility differs by breakpoint: use `entry-or-view`.
- The line represents a process, route, timeline, or sequence: use `scroll`.

Hero artwork that is visible on page load should usually be `entry-play`, not fake scroll-linked motion. Scroll-linked drawing must complete near the subject's first fully framed moment, or center-focused moment for a tall subject.

For scroll-linked motion, the subject should not already be meaningfully visible at page load on any target viewport. If a desktop layout makes the subject visible while mobile keeps it below the fold, use `entry-or-view` or move the subject lower with real layout space. Do not keep `trigger-model="scroll"` when the 0% sample would already show a partially drawn path.

For a subject shorter than the viewport, default scroll-linked completion to first full-frame: `data-ud-motion-end="bottom 100%"`. Do not use `bottom 70%`, `bottom 60%`, or similar late viewport points as the main end; those belong to `data-ud-motion-exit-at` as a late guard. A route that completes only around `bottom 70%` fails focus-complete because the user has already passed the fully framed moment.

## Coupled SVG Draw Pattern

Use one source of truth for contract markers and JS progress. This plain browser pattern matches the validator's position math for common scroll-linked SVG draw work:

```html
<svg id="scope-map" viewBox="0 0 640 360" aria-label="Delivery path">
  <path
    data-ud-motion="scope-route"
    data-ud-motion-type="svg-draw"
    data-ud-motion-trigger-model="scroll"
    data-ud-motion-trigger="#scope-map"
    data-ud-motion-end-trigger="#scope-map"
    data-ud-motion-subject="#scope-map"
    data-ud-motion-start="top 80%"
    data-ud-motion-end="bottom 100%"
    data-ud-motion-focus-at="auto"
    data-ud-motion-samples="0,0.25,0.5,0.75,1"
    d="M40 290 C160 120 320 120 600 70" />
</svg>
```

```js
const clamp = (value, min, max) => Math.max(min, Math.min(max, value));
const pointOffset = (point, size) => point === "bottom" ? size : point === "center" ? size / 2 : point.endsWith("%") ? Number.parseFloat(point) / 100 * size : 0;
const viewportOffset = (point) => point === "bottom" ? innerHeight : point === "center" ? innerHeight / 2 : point.endsWith("%") ? Number.parseFloat(point) / 100 * innerHeight : 0;
function scrollYFor(el, expr) {
  const [triggerPoint = "top", viewportPoint = "bottom"] = String(expr).split(/\s+/);
  const rect = el.getBoundingClientRect();
  return rect.top + scrollY + pointOffset(triggerPoint, rect.height) - viewportOffset(viewportPoint);
}
function initDraw(path) {
  const length = path.getTotalLength();
  path.style.strokeDasharray = length;
  path.style.strokeDashoffset = length;
  return length;
}
function updateDraw(path, length) {
  const model = path.dataset.udMotionTriggerModel || "scroll";
  if (model !== "scroll") return;
  const trigger = document.querySelector(path.dataset.udMotionTrigger) || path.ownerSVGElement;
  const endTrigger = document.querySelector(path.dataset.udMotionEndTrigger) || trigger;
  const maxScroll = Math.max(0, document.documentElement.scrollHeight - innerHeight);
  const startY = clamp(scrollYFor(trigger, path.dataset.udMotionStart || "top 80%"), 0, maxScroll);
  const endY = clamp(scrollYFor(endTrigger, path.dataset.udMotionEnd || "bottom 100%"), 0, maxScroll);
  const progress = clamp((scrollY - startY) / Math.max(1, endY - startY), 0, 1);
  path.style.strokeDashoffset = String(length * (1 - progress));
}
const drawnPaths = [...document.querySelectorAll('[data-ud-motion-type="svg-draw"]')].map((path) => [path, initDraw(path)]);
function updateMotion() {
  drawnPaths.forEach(([path, length]) => updateDraw(path, length));
}
if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
  drawnPaths.forEach(([path]) => {
    path.style.strokeDashoffset = "0";
  });
} else {
  addEventListener("scroll", updateMotion, { passive: true });
  addEventListener("resize", updateMotion);
  updateMotion();
}
```

For `entry-play`, initialize the dash while hidden or before paint, then transition to zero once the subject is visible. Mark it as `data-ud-motion-trigger-model="entry-play"` so the validator checks completion at the focus moment rather than sampled scroll progress.

Reduced motion must leave SVG drawing visible and complete: set `strokeDashoffset` to `0`, keep the content readable, and avoid hidden reveal states.

## Done Signal

The run is done only when:

- `index.html` exists.
- `DESIGN.md` has `## Request Anchor` and `## OKF Preflight`.
- `run_html_proof.mjs` exits `0`, or the final response clearly says the proof run failed.
- The proof report path is recorded.
- If the proof failed, `.ultimate-design/proof/repair-brief.md` was read before deciding whether to repair or report failure.
