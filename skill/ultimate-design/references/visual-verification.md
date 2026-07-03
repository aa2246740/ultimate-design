# Visual Verification

Use this reference before final delivery for screenshotable visual artifacts: HTML pages, HTML decks, product UI, dashboards, presentation previews, PDFs, images, and exported graphics.

## Failure To Catch

Do not treat "nothing overflowed the canvas" as visual verification. A design can pass geometry bounds while still failing because text, cards, charts, controls, or panels are too close, visually tangled, clipped, hidden, or covered by fixed UI.

Treat these as P1 unless the overlap is deliberate and documented:

- Text overlaps, touches, or visually competes with cards, charts, panels, navigation, or controls.
- Major semantic zones have too little separation for the medium.
- Sticky or fixed controls cover content or navigation.
- Text is clipped, truncated unintentionally, or too dense to scan.
- A slide, page, or state was generated but not inspected.

## Required Pass

1. Render every final page, slide, frame, or key responsive state that the user will see. Do not rely on a sampled screenshot when the artifact has multiple slides/pages.
2. Save screenshots or rendered previews in an output folder. For decks or PDFs, create a contact sheet or screenshot set that makes every page visible.
3. Inspect the full screenshot set once as a human visual pass. Look for collisions, too-tight spacing, hidden controls, clipped text, awkward line breaks, and density mismatch.
4. Run available deterministic checks for the artifact type:
   - HTML/HTML deck: use `scripts/validate_html_visual.mjs` when Playwright or Chrome is available.
   - PPT/PDF: render every slide/page with the relevant presentation/PDF tools and scan the image set.
   - Static image/graphic: inspect the final bitmap at intended output size.
5. Repair P0/P1 issues and easy P2 issues, then rerun the visual pass.
6. If visual verification could not run, say `Not run` in the final response and give the reason.

## Measurement Model

For HTML artifacts, `scripts/validate_html_visual.mjs` uses a real browser render, not static DOM guessing:

- It opens the final file in Chrome/Playwright at the configured viewports.
- It waits for the DOM to render, switches each `.slide` through `.thumb[data-slide]` when present, and saves screenshots.
- It measures rendered boxes with `getBoundingClientRect()`.
- It measures text clipping with `scrollWidth/clientWidth` and `scrollHeight/clientHeight` when overflow is not visible.
- It estimates rendered text line count from `Range.getClientRects()`.
- It scales spacing thresholds from the 1280 px design coordinate system to the actual rendered slide size.

This catches objective layout facts. It does not replace human/art-direction judgment about whether the design is beautiful, on-brand, or strategically right.

## HTML Semantic Zones

For generated HTML visual artifacts, mark top-level semantic zones that must not collide:

```html
<h1 data-ud-check="hero-title" data-ud-max-lines="2">...</h1>
<p data-ud-check="hero-lead" data-ud-max-lines="3" data-ud-align-left="hero-title">...</p>
<section data-ud-check="proof-cards" data-ud-align-left="hero-title">...</section>
```

Mark sibling zones, not every nested text node. Good zones include title blocks, lead copy, CTA rows, card grids, charts, tables, navigation, footers, slide bodies, and major panels.

Use at least 36 px of design-coordinate separation between adjacent major zones unless the design contract states a tighter system. When the artifact scales down, measure this as the equivalent scaled distance.

## Machine-Judged Standards

The HTML checker fails the artifact when any marked zone breaks these standards:

| Standard | How it is judged | Default |
|---|---|---|
| Missing markers | No `data-ud-check` / `data-check` zones found | fail |
| Slide navigation mismatch | `.slide` count differs from `.thumb` count when both exist | fail |
| Out of bounds | Marked zone sits outside the active slide/page bounds | fail |
| Clipping | overflow is not visible and `scrollWidth > clientWidth` or `scrollHeight > clientHeight` beyond tolerance | fail |
| Collision | Two sibling marked zones overlap by more than 4 px in both axes, scaled to slide size | fail |
| Tight spacing | Adjacent marked zones with meaningful axis overlap have less than the minimum gap | default 36 px design coordinates |
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
data-ud-align-left="other-zone-name"
data-ud-align-right="other-zone-name"
data-ud-align-top="other-zone-name"
data-ud-align-bottom="other-zone-name"
data-ud-align-center-x="other-zone-name"
data-ud-align-center-y="other-zone-name"
data-ud-align-tolerance="4"
```

If a design intentionally breaks a default, document the reason in `DESIGN.md` and either adjust the threshold or do not mark those zones as collision-checked siblings.

## What Cannot Be Fully Automated

The checker can prove rendered facts; it cannot prove the artifact is strategically well designed. These remain human or visual-model review items:

- Whether the hierarchy feels elegant rather than merely non-overlapping.
- Whether a line break is rhetorically good when no max-line intent was specified.
- Whether color, mood, and type personality match the brand or audience.
- Whether the composition feels balanced beyond measurable alignment and spacing.

For these, inspect the screenshot set or contact sheet and record the judgment.

## Done Signal

Visual verification is done only when:

- Every user-visible page/slide/state has a screenshot or rendered preview.
- The full set was inspected, not only one representative page.
- Semantic collision/spacing checks passed where available.
- Any remaining visual risk is documented as accepted or blocked.
