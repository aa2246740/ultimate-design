# Visual Verification

Use this reference before final delivery for screenshotable visual artifacts: HTML pages, HTML decks, product UI, dashboards, presentation previews, PDFs, images, and exported graphics.

## Failure To Catch

Do not treat "nothing overflowed the canvas" as visual verification. A design can pass geometry bounds while still failing because text, cards, charts, controls, or panels are too close, visually tangled, clipped, hidden, or covered by fixed UI.

Treat these as P1 unless the overlap is deliberate and documented:

- Text overlaps, touches, or visually competes with cards, charts, panels, navigation, or controls.
- Major semantic zones have too little separation for the medium.
- Sticky or fixed controls cover content or navigation.
- Absolute or floating callouts exist in the DOM but are hidden behind cards, charts, screenshots, or decorative layers.
- Reveal, animation, opacity, transform, or z-index choices make meaningful content invisible in the rendered output.
- Text is clipped, truncated unintentionally, or too dense to scan.
- A slide, page, or state was generated but not inspected.

## Rendered Integrity

Rendered integrity means a marked semantic zone is actually readable in the pixels a user receives, not merely present in the DOM. It has three parts:

- **Box integrity:** the zone has a nonzero rendered box inside the page/slide/frame.
- **Visibility integrity:** the zone is not hidden by `display`, `visibility`, near-zero `opacity`, or an unfinished reveal state.
- **Occlusion integrity:** sampled points inside the zone return the zone itself or its descendants from `document.elementsFromPoint`; unrelated top layers covering the samples are failures.

Use rendered integrity for all readable semantic zones. Intentional overlaps must be documented in `DESIGN.md` and marked with an explicit allow attribute rather than left ambiguous.

## Rendered UI Audit

Rendered UI Audit is the non-visual browser measurement gate for generated HTML. It lets any model audit structured browser facts instead of relying on screenshot interpretation. The default implementation is `scripts/validate_html_visual.mjs`; it writes `schemaVersion: "ultimate-design.rendered-ui-audit.v1"`, `status`, `summary`, `facts`, and normalized `findings[]`, while keeping older `results[]` and `failures[]` fields for compatibility.

The audit checks marked `data-ud-check` zones plus minimal page-level facts: horizontal overflow, visible interactive target size, and obvious missing accessible names. A finding with active `severity: "fail"` fails the command; warn/info findings remain visible in the report and do not fail the command. Allowances reduce or contextualize findings; they do not remove evidence from the report.

Evidence must also be fresh. The unified proof runner removes prior generated audit output before launch and records `reportFresh`; only `reportFresh: true` may support a pass, repair brief, or finding summary. If a browser process fails before writing a report, report the launch failure and do not reuse old JSON or screenshots.

Use `data-ud-allow="<rule-id>"` with `data-ud-allow-reason`, `data-ud-allow-owner`, and `data-ud-allow-expires` for intentional exceptions. Legacy `data-ud-allow-occlusion` and `data-ud-allow-invisible` still work, but the structured allowance form is preferred.

## Required Pass

1. Render every final page, slide, frame, or key responsive state that the user will see. Do not rely on a sampled screenshot when the artifact has multiple slides/pages.
2. Save screenshots or rendered previews in an output folder. For decks or PDFs, create a contact sheet or screenshot set that makes every page visible.
3. Inspect the full screenshot set once as a human visual pass. Look for collisions, too-tight spacing, hidden controls, clipped text, awkward line breaks, and density mismatch.
4. Run available deterministic checks for the artifact type:
   - HTML/HTML deck: use `scripts/validate_html_visual.mjs` when the pinned Playwright runtime is available. Never launch the user's system Chrome as a headless fallback. It runs the Rendered UI Audit: geometry, visibility, and occlusion sampling for marked zones, plus page-level horizontal overflow and visible interactive-control basics.
   - Motion contracts: use `scripts/validate_motion_contract.mjs` when the artifact claims scroll-linked SVG drawing, reveal no-flash behavior, or reduced-motion animation behavior. It samples rendered motion state in a browser and writes a motion-validation report.
   - PPT/PDF: render every slide/page with the relevant presentation/PDF tools and scan the image set.
   - Static image/graphic: inspect the final bitmap at intended output size.
5. Repair P0/P1 issues and easy P2 issues, then rerun the visual pass.
6. If visual verification could not run, say `Not run` in the final response and give the reason.

## Cmux + Computer Use Fallback

Use this fallback only when the automated Rendered UI Audit cannot launch because of sandbox, Mach-port, runtime, or browser-process restrictions and both cmux and Computer Use are available. It is a visible-browser inspection path, not a substitute data source for machine geometry.

1. Start a loopback-only server for the final artifact and open a fresh cmux browser tab or pane. Do not reuse or disturb an unrelated browser task.
2. Inspect a desktop-width state and a narrow state created by resizing or splitting the pane. For fixed-canvas work, inspect the intended canvas plus any required scaled preview.
3. Inspect the first viewport, one dense middle region, and the final region. Scroll rather than judging only the first screen.
4. Exercise representative interactions: anchor navigation, tabs, slide controls, forms, menus, hover/focus behavior, or reduced-motion state when applicable.
5. Read the accessibility tree for headings, landmarks, control names, table/list structure, and reading order. Use the screenshot for visual judgment and the tree for semantic confirmation.
6. Save screenshots and a compact evidence JSON using `schemaVersion: "ultimate-design.computer-use-visual-fallback.v1"`, including checked states, pass/fail judgments, limitations, and artifact URL.
7. Restore the user's cmux workspace, close the temporary browser tab or split, and stop the local server after evidence is saved.

Evidence policy:

- This fallback may satisfy the human/visible inspection portion of the visual gate.
- It must not set `reportFresh`, overwrite a Rendered UI Audit report, or claim deterministic collision, occlusion, clipping, overflow, line-count, target-size, or alignment measurements.
- Keep the machine step `blocked` or `not run` when acceptance explicitly requires it. Report both outcomes separately, for example: `Computer Use visual fallback: pass; Rendered UI Audit: blocked by sandbox`.
- If the fallback finds a problem, repair it and repeat the affected visible states. Do not use the machine-audit blocker as a reason to ignore a visible defect.

## Measurement Model

For HTML artifacts, `scripts/validate_html_visual.mjs` uses a real browser render, not static DOM guessing:

- It opens the final file in the pinned Chromium Headless Shell at the configured viewports.
- It waits for the DOM to render, switches each `.slide` through `.thumb[data-slide]` when present, and saves screenshots.
- It measures rendered boxes with `getBoundingClientRect()`.
- It measures text clipping with `scrollWidth/clientWidth` and `scrollHeight/clientHeight` when overflow is not visible.
- It estimates rendered text line count from `Range.getClientRects()`.
- It scales fixed-canvas slide spacing thresholds from the 1280 px design coordinate system to the actual rendered slide size, while normal web pages use CSS-pixel spacing.
- It emits structured `findings[]` with `ruleId`, `severity`, `viewport`, selector/zone, bounding box, evidence, and allowance metadata so non-visual models can rank and explain issues without reading screenshots.

This catches objective layout facts. It does not replace human/art-direction judgment about whether the design is beautiful, on-brand, or strategically right.

## Motion Integrity

Motion integrity means the animation state a user receives matches the motion contract over time or scroll, not only at the final frame. Use it for scroll-linked SVG linework, page-level reveal choreography, progress-bound transitions, and reduced-motion fallbacks.

The motion evidence loop must stay coupled: the selectors named in `data-ud-motion-trigger`, `data-ud-motion-end-trigger`, and `data-ud-motion-subject` must resolve in the DOM, and the JavaScript/ScrollTrigger implementation must use those same selectors and progress boundaries. A path with contract attributes but hard-coded viewport math unrelated to those attributes is not a valid implementation.

For HTML artifacts, `scripts/validate_motion_contract.mjs` can check elements marked with:

```html
<path
  data-ud-motion="hero-route"
  data-ud-motion-type="svg-draw"
  data-ud-motion-trigger-model="scroll"
  data-ud-motion-trigger="#hero"
  data-ud-motion-end-trigger="#hero-route-panel"
  data-ud-motion-subject="#hero-route-panel"
  data-ud-motion-start="top 80%"
  data-ud-motion-end="bottom 100%"
  data-ud-motion-focus-at="auto"
  data-ud-motion-samples="0,0.25,0.5,0.75,1"
  data-ud-motion-tolerance="0.12"
/>
```

For SVG draw checks, the validator reads `stroke-dasharray` and `stroke-dashoffset` after scrolling to each progress point. Prefer real path lengths from `getTotalLength()`; with a validated unit path, expected reveal progress is approximately `1 - strokeDashoffset`.

SVG drawing is checked against the watched subject's **display-window** and focus-complete point. Set `data-ud-motion-trigger-model` to `entry-play`, `view-entry`, `entry-or-view`, `scroll`, or `static`; set `data-ud-motion-subject="#subject-selector"` when the user watches a larger panel or media block. For scroll-linked drawing, the range must end near `auto -> reveal >= 0.95`: subjects shorter than the viewport complete near first full-frame visibility, and taller subjects complete near center-focus. Tune with `data-ud-motion-focus-at`, `data-ud-motion-focus-min`, and `data-ud-motion-focus-window` only when the contract deliberately uses a different focus moment. `data-ud-motion-exit-at` remains a late guard, not the primary completion point.

Use `entry-play` for a subject already meaningfully visible on arrival. Use `view-entry` for a later subject when scroll progress is not the story. Use `entry-or-view` when the same subject is initially visible on some breakpoints but below the fold on others. Use `scroll` only when the line represents a route, sequence, timeline, or other progress-bound meaning.

For reveal checks, mark readable reveal targets with `data-ud-motion-type="reveal"` and `data-ud-motion-no-flash="true"` when first-paint flash or duplicate reveal would violate the contract.

Reduced-motion checks should use the browser's `prefers-reduced-motion: reduce` emulation and confirm content remains visible and SVG drawing reaches the declared static state.

## HTML Semantic Zones

For generated HTML visual artifacts, mark top-level semantic zones that must not collide:

```html
<h1 data-ud-check="hero-title" data-ud-max-lines="2">...</h1>
<p data-ud-check="hero-lead" data-ud-max-lines="3" data-ud-align-left="hero-title">...</p>
<section data-ud-check="proof-cards" data-ud-align-left="hero-title">...</section>
```

Mark sibling zones, not every nested text node. Good zones include title blocks, lead copy, CTA rows, card grids, charts, tables, navigation, footers, slide bodies, major panels, readable floating notes, badges, chart annotations, overlay panels, sticky bars, and any absolute-positioned text that a user is meant to read.

Avoid marking both a broad parent container and all of its child text zones unless the parent itself has a readable boundary that must be checked. Over-marking creates noisy spacing and occlusion failures and hides the real repair target. Prefer one intentional hierarchy level per region, such as `hero-title`, `hero-lead`, and `hero-cta-row`, or a single `hero-panel` when the panel itself is the visual subject.

For normal web pages, the default hard minimum between sibling marked zones is 12 CSS px so intentional title/lead and label/value relationships do not become false failures; major page sections should usually use 24-36 px or more. Fixed-canvas slides keep a 36 px design-coordinate default, scaled with the canvas. When the design contract intentionally needs a different local rhythm, set `data-ud-min-gap` on either zone; the stricter explicit value wins for that pair.

For weak/headless proof runs, use the unified HTML proof command when available:

```bash
node <ultimate-design>/scripts/run_html_proof.mjs --html index.html --design DESIGN.md --out .ultimate-design/proof
```

## Machine-Judged Standards

The HTML checker fails the artifact when any marked zone breaks these standards:

| Standard | How it is judged | Default |
|---|---|---|
| Missing markers | No `data-ud-check` / `data-check` zones found | fail |
| Slide navigation mismatch | `.slide` count differs from `.thumb` count when both exist | fail |
| Horizontal overflow | Document or body scroll width exceeds viewport width beyond tolerance | fail, tiny subpixel overflow warns |
| Out of bounds | Marked zone sits outside the active slide/page bounds | fail |
| Clipping | overflow is not visible and `scrollWidth > clientWidth` or `scrollHeight > clientHeight` beyond tolerance | fail |
| Invisible | Marked zone has near-zero opacity or hidden display/visibility | fail unless allowed |
| Collision | Two sibling marked zones overlap by more than 4 px in both axes, scaled to slide size | fail |
| Occlusion | Sampled points inside a marked zone are topped by unrelated elements via `elementsFromPoint` | fail unless allowed |
| Missing accessible name | A visible interactive control has no obvious text, ARIA label, associated label, title, value, placeholder, or SVG title | fail for obvious cases |
| Small target | A visible interactive control is below 24 by 24 CSS px | fail; 24-43 px warns |
| Allowance governance | `data-ud-allow` is missing reason, owner, or expires; uses `all`; or has expired | warn or fail |
| Tight spacing | Adjacent marked zones with meaningful axis overlap have less than the applicable minimum gap | pages: 12 CSS px; fixed-canvas slides: 36 design px; explicit `data-ud-min-gap` overrides |
| Unexpected wrapping | `Range.getClientRects()` line count exceeds `data-ud-max-lines`, or `data-ud-nowrap` wraps past 1 line | explicit only |
| Unexpected unwrapping | line count is below `data-ud-min-lines` | explicit only |
| Misalignment | left/right/top/bottom/center differs from the named target by more than tolerance | explicit only, default 4 px design coordinates |

Use these attributes to state design intent:

```html
data-ud-check="unique-zone-name"
data-ud-role="title|lead|card-grid|chart|footer|nav|panel"
data-ud-max-lines="2"
data-ud-min-lines="1"
data-ud-nowrap
data-ud-min-gap="24"
data-ud-align-left="other-zone-name"
data-ud-align-right="other-zone-name"
data-ud-align-top="other-zone-name"
data-ud-align-bottom="other-zone-name"
data-ud-align-center-x="other-zone-name"
data-ud-align-center-y="other-zone-name"
data-ud-align-tolerance="4"
data-ud-allow="occlusion"
data-ud-allow-reason="Intentional sticky nav overlap during transition"
data-ud-allow-owner="ultimate-design"
data-ud-allow-expires="2026-09-30"
data-ud-allow-occlusion
data-ud-allow-invisible
```

If a design intentionally breaks a default, document the reason in `DESIGN.md` and either adjust the threshold or do not mark those zones as collision-checked siblings.

## What Cannot Be Fully Automated

The checker can prove rendered facts; it cannot prove the artifact is strategically well designed. These remain human or visual-model review items:

- Whether the hierarchy feels elegant rather than merely non-overlapping.
- Whether a line break is rhetorically good when no max-line intent was specified.
- Whether color, mood, and type personality match the brand or audience.
- Whether the composition feels balanced beyond measurable alignment and spacing.

For these, inspect the screenshot set or contact sheet and record the judgment.

Accessibility engines such as axe-core, Pa11y, or Lighthouse and screenshot diff tools such as Playwright baselines, BackstopJS, Percy, or Chromatic may enrich the report later when dependencies and failure policy are explicitly declared. They are optional enrichment, not the default Ultimate Design hard gate.

## Done Signal

Visual verification is done only when:

- Every user-visible page/slide/state has a screenshot or rendered preview.
- The full set was inspected, not only one representative page.
- Semantic geometry, visibility, and occlusion checks passed where available.
- Motion integrity checks passed for any declared motion contract where available.
- Any remaining visual risk is documented as accepted or blocked.
