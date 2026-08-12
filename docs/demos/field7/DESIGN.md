---
version: 0.1
name: FIELD-7 Product Page
description: Industrial-functional product page for FIELD-7, a fictional pocket synthesizer by Norm Audio — schematic hero, knolled kit, monospace specs.
colors:
  primary: "#E85A1B"
  secondary: "#5C5C58"
  tertiary: "#C4C4BE"
  neutral: "#E6E6E1"
  surface: "#F5F5F2"
  on-surface: "#1A1A18"
  error: "#B42318"
typography:
  headline-lg:
    fontFamily: "IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: 72px
    fontWeight: 600
    lineHeight: 0.95
  body-md:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  label-md:
    fontFamily: "IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
rounded:
  none: 0px
  sm: 2px
  md: 4px
  lg: 8px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  primary-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
---

# Design System

## Overview

FIELD-7 is a fictional pocket synthesizer by fictional maker Norm Audio. This page is an industrial-functional product sheet: the device is drawn as a detailed top-view SVG schematic (pads, dual knobs, OLED, speaker grille, I/O marks, dimension arrows), not photographed. Spec tables and knolled accessory line drawings are first-class content. The read is workshop paperwork under cool shop light — near-white panel grays, ink lines, one industrial orange accent, flat hairline borders, matter-of-fact copy with dry wit.

## Colors

- Scene sentence: A musician comparing pocket instruments on a bright desk at midday — matte gray panels, ink drawings, a single orange index mark like a safety stripe on tooling.
- Color posture: **Restrained** — neutrals dominate; primary orange (`#E85A1B`) stays under ~10% (CTA fills, callout letters, pad index strips, power LED).
- `--surface` `#F5F5F2` / `--on-surface` `#1A1A18` for body reading (≥4.5:1).
- `--neutral` `#E6E6E1` and panel `#ECECE8` for schematic plates and tables.
- `--secondary` `#5C5C58` for muted labels (≥4.5:1 on surface).
- `--tertiary` `#C4C4BE` for soft structural fills inside drawings.
- `--error` `#B42318` reserved for true fault states (unused on this static demo).
- White text on primary orange only on large CTA fills; never orange small body text on gray.
- Anti-template locks: no purple/indigo SaaS gradients, no warm cream+terracotta luxury, no broadsheet newspaper layout, no soft multi-layer shadows or glow.

## Typography

- Brand/display: IBM Plex Mono 600 — technical product name as the memory feature (`FIELD-7`).
- Body/UI: IBM Plex Sans 400–600 — quiet industrial sans for pitch and feature prose.
- Labels/data: IBM Plex Mono 400–600 for nav, section ticks, dimension annotations, knoll captions, and the full spec table.
- YAML tokens stay scalar px; CSS may use `clamp()` for the hero product name only.
- Max two Google Font families with `display=swap` and system mono/sans fallbacks so layout survives blocked fonts.

## Layout

One scrolling English product page. Semantic zones on inner padded wraps: `navigation`, `hero-schematic`, `features`, `knolling`, `specs`, `buy`, `footer`. Adjacent marked zones keep ≥36px real gaps.

- Hero: brand-scale `FIELD-7`, one-line pitch, price, buy CTA, and the dominant schematic panel (full-bleed within the content column — not an inset media card).
- Features: four callouts A–D matching schematic pins (pad matrix, knobs, OLED, speaker).
- Knolling: four SVG line accessories in a flat grid (cable, case, strap, battery).
- Specs: monospace engineering table as primary content.
- Buy: visual-only purchase control plus shipping/warranty note.
- Footer: required demo attribution.
- Breakpoints: stack under ~720px; dimension arrows hide on small screens and reflow as a dimension list under the drawing (no information loss); knoll goes 2×2 then 4-up.

## Elevation & Depth

Flat industrial sheet. Depth is hairline borders (`1px`) and panel gray fills only — no shadows deeper than a 1px hairline, no blur, no parallax. Sticky nav uses a light translucent surface + 1px rule, not a cast shadow.

## Shapes

Near-rectilinear. `rounded.sm` (2px) on buttons and small controls; schematic body uses modest SVG radii for physical honesty of a machined pocket device. Callout markers are circles with mono letters. No pill clusters.

## Components

- Primary button: industrial orange fill, white label, mono uppercase, min-height 48px, 2px radius.
- Ghost button: transparent with ink hairline border.
- Sticky nav with 44px+ text targets and orange Buy chip.
- Schematic figure with desktop dimension annotations and mobile dimension list.
- Feature rows with A–D marks.
- Knoll figures (SVG + mono caption bar).
- Spec table in a focusable scroll region for narrow viewports.
- Skip link to `#main`.

## Do's and Don'ts

- Do keep the inline SVG schematic as the hero visual memory — precise enough to read at gallery thumbnail scale (~1280×800 crop).
- Do treat the monospace spec table as content, not decoration.
- Do allow dry wit in copy; forbid hype adjectives ("revolutionary", "seamless", "magical").
- Do honor `prefers-reduced-motion` by disabling reveals and leaving all content visible; force-reveal within ~700ms and on print.
- Do not clone teenage engineering (or any real brand) wordmarks, exact product silhouettes, signature colorways, or proprietary layout fingerprints — adopt mechanisms only (schematic hero, dimension arrows, knolling line kit, mono specs, restrained gray+one accent).
- Do not use raster images, emoji, purple gradients, soft card elevation, or scroll-linked incomplete drawing of the schematic.
- Do not let interactive targets drop below 44×44 CSS px.

## Request Anchor

- Original user request: Design the product page for FIELD-7, a fictional pocket synthesizer by Norm Audio. Industrial functionalism. English. Adopt TE-class industrial-functional mechanisms (schematic SVG hero, dimension annotations, knolling accessories, mono specs, gray+one orange, flat hairlines, dry matter-of-fact copy) without cloning a real brand signature. Content: hero schematic + pitch + price + buy; 4 feature callouts; knolling grid; full spec table; shipping/warranty; footer. Deliver only `index.html` and `DESIGN.md` under `docs/demos/field7/`.
- Latest user override: None — execute the prompt as given (Build route, YOLO, proof-run HTML, wave-1 hard constraints).
- Deliverable: `/workspace/docs/demos/field7/index.html` and `/workspace/docs/demos/field7/DESIGN.md`.
- Primary audience: Musicians and hardware browsers evaluating a pocket instrument’s honesty and craft in under a minute; secondary: gallery visitors viewing a scaled iframe thumbnail.
- Core job to be done: Immediately recognize FIELD-7 as a precise physical product, scan features and specs, and understand price plus how to “buy” (visual demo).
- Success criteria: Schematic hero reads at thumbnail scale; all requested sections present; AA contrast; keyboard/focus/44px targets; reduced-motion safe with 700ms force-reveal; 320–1440 no horizontal overflow; annotations reflow on mobile; validators pass; file ≤160KB; fictional footer line exact.
- Non-goals: Real checkout, CMS, multi-page catalog, raster photography, dark/light theme toggle, scroll-scrubbed SVG drawing as the hero story.
- Must preserve: Fictional Norm Audio / FIELD-7 framing; required footer attribution string; `data-ud-check` on named zones; Google Fonts only as external (≤2 families); vanilla single-file CSS/JS; no writes outside the demo folder (except `/tmp` audits).
- Validation must check against: Request Anchor fit; `validate_design_contract.py --strict-ultimate --require-frontmatter`; `validate_okf_usage.py`; `validate_html_visual.mjs` pass with 0 fails/0 warnings; HTML parse; JS `node --check`; no emoji; byte size ≤160KB.

## Content Model

- User intent: Decide whether this pocket synth is concrete, credible, and worth the listed price.
- Business intent: Convert interest into a buy intent (demo button) after specs and kit clarity.
- Message hierarchy: 1) Product identity + schematic. 2) Price and buy. 3) Part callouts. 4) Kit contents. 5) Full specs. 6) Shipping/warranty.
- First-screen answers: What (FIELD-7 pocket synth), who (Norm Audio), next action (Buy FIELD-7 / read drawing).
- Primary action meaning: Buy FIELD-7 — visual-only; status text clarifies no payment.
- Voice and tone: Matter-of-fact industrial English; dry wit allowed; no hype adjectives.
- Terminology rules: Prefer “schematic,” “pad matrix,” “engine,” “kit,” “drawing”; avoid “magical,” “seamless,” “next-gen,” “revolutionary."
- State language rules: Buy click updates a live status region stating demo-only checkout.
- Trust/risk content: Fictional maker disclosed in specs and footer; warranty copy is plainly fictional demo policy.
- Content risks: Accidental real-brand cloning; overselling engines; hiding that buy is non-functional.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: industrial-functional design read; anti-default locks; schematic as visual memory; layout-family budget across sheet sections.
- `design-okf/systems/type-personality.md`: mono-led technical voice (Plex Mono display + Plex Sans body); two-family WebFont budget.
- `design-okf/systems/color-system.md`: restrained gray panel climate with one industrial orange accent; AA roles.
- `design-okf/content/message-model.md`: first viewport answers product, pitch, price, buy; section order follows decision path.
- `design-okf/content/ux-writing.md`: verb+object CTAs; dry matter-of-fact copy; ban hype adjectives.
- `design-okf/foundations/visual-communication-hierarchy.md`: schematic dominates once; single-job sections.
- `design-okf/foundations/necessary-design-judgment.md`: drawing is necessary evidence; cut decorative chrome; material honesty of line art.
- `design-okf/systems/motion-language.md`: opacity/transform section reveals ≤400ms; static schematic; reduced-motion off.
- `design-okf/systems/motion-contract.md`: IntersectionObserver reveals + ~700ms force-reveal + print force-reveal; no scroll-linked incomplete schematic.
- `design-okf/digital/accessibility-usability.md`: WCAG AA, keyboard, focus-visible, 44px targets, labeled regions.
- `design-okf/digital/responsive-interaction.md`: schematic viewBox scales; annotations hide/list on mobile; no page overflow 320–1440.

### Support References

- `references/branch-marketing-site.md`
- `references/proof-run-html.md`
- `references/reference-study.md` (mechanism extraction; no signature transfer)
- `references/content-model.md`
- `references/design-contract.md`
- `references/quality-gates.md`
- `references/visual-verification.md`
- `SKILL.md` (Build route, YOLO, artifact-first proof run)

### Decision Record

- Constraints extracted: Single self-contained HTML; ≤2 Google Font families with preconnect + `display=swap`; no rasters/emoji; industrial functionalism via schematic hero, dimension arrows, knolling SVGs, mono specs, gray+one orange, flat ≤1px depth; four pinned callouts; full fictional-but-plausible specs; shipping/warranty; exact footer line; `data-ud-check` on inner padded zones with ≥36px gaps; reveals with IO + 700ms + print fallback; schematic complete without scroll drawing; AA; 44px targets; ≤160KB; DESIGN.md must pass both Python validators and HTML visual audit.
- Deliberate exceptions: Hero uses a panel plate behind the drawing (hairline frame) because technical drawings need a sheet — this is not a soft elevated media card. Sticky nav uses light blur for legibility over the grid texture; blur is not a depth shadow. Dimension arrows hide below 720px and are replaced by an explicit list to avoid cramped overlapping labels.
- Verification hooks: strict contract validation; OKF usage validation; rendered UI audit to `/tmp/audit-field7`; HTML parse; JS syntax check; emoji scan; byte size.

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Industrial functionalism: workshop sheet read; dials variance 4 / density 6 / motion 2 / distinction 8 / experiment 4; ban SaaS purple, cream-terracotta, soft cards, glow | Global theme, hero schematic, knoll grid, spec sheet | Thumbnail shows precise drawing not generic cards; banned defaults absent in CSS |
| `design-okf/systems/type-personality.md` | IBM Plex Mono carries FIELD-7 memory and data; IBM Plex Sans recedes for prose; max two Google families + fallbacks | Font links, `.hero-brand`, `.spec-table`, labels | Fonts-blocked layout intact; no Inter/Roboto-only display; mono specs readable |
| `design-okf/systems/color-system.md` | Restrained gray panels + one orange accent for CTA/marks; ink on surface ≥4.5:1; white on orange only for CTA | `:root` tokens, buttons, callout letters | Contrast AA; orange area sparse; no orange body text on gray |
| `design-okf/content/message-model.md` | First screen: product name, pitch, price, buy, schematic evidence | `[data-ud-check=hero-schematic]` | First viewport answers what/price/next without scrolling past hero |
| `design-okf/content/ux-writing.md` | CTAs “Buy FIELD-7”; dry wit; no hype adjectives | Pitch, features, buy status, warranty | Copy review; status announces demo-only checkout |
| `design-okf/foundations/visual-communication-hierarchy.md` | Schematic is the sole dominant visual; later sections single-job | Hero panel vs features/knoll/specs | Screenshots show no section competing with the drawing |
| `design-okf/foundations/necessary-design-judgment.md` | Keep only evidence that clarifies the object (drawing, dims, kit, specs); cut decorative ornament | SVG budget, section list | Critique: every section answers a buyer question |
| `design-okf/systems/motion-language.md` | Reveal via opacity+translateY ≤360ms; schematic static/complete; reduced-motion disables animation | `.reveal`, `@media (prefers-reduced-motion)` | Reduced-motion shows full content; durations ≤400ms; transform/opacity only |
| `design-okf/systems/motion-contract.md` | Trigger model view-entry with 700ms force-reveal and beforeprint/print force-reveal; no svg-draw scroll contract for hero | Reveal script, print CSS | Content visible by 700ms; print styles force `.is-in` |
| `design-okf/digital/accessibility-usability.md` | Landmarks, skip link, focus-visible orange ring, ≥44px targets, SVG title/desc, live buy status | Nav, buttons, schematic, buy | Keyboard path; visual audit target-size; AA pairs |
| `design-okf/digital/responsive-interaction.md` | viewBox schematic scales; desktop dims hide on mobile replaced by list; table scrolls locally; no page overflow | Media queries, `.anno-mobile`, `.spec-table-wrap` | Audit at mobile/desktop; 320–1440 no horizontal overflow |

## Information Architecture

- Core user tasks: Identify product → inspect drawing → scan callouts → check kit → read specs → buy (demo).
- Page inventory: Single `index.html` product page.
- Navigation model: Sticky anchors (Features, Kit, Specs, Buy) + footer chrome.
- Content hierarchy: Hero schematic → Features A–D → Knolled kit → Spec table → Buy/warranty → Footer.
- Primary CTA rules: “Buy FIELD-7” / “Buy FIELD-7 — $329” use verb + object; secondary “Read specs.”

## Reference Study

- Source mode: Prompt-supplied style-mechanism extraction (teenage-engineering-class industrial-functional product sites); provenance: third-party / signature-class references for learning only.
- Mechanisms adopted: device-as-detailed-inline-SVG technical schematic hero; dimension annotations with thin arrows and mono labels; knolling grid of accessories as SVG line drawings; monospace spec tables as first-class content; functional gray palette with one industrial orange accent; flat hairline elevation; matter-of-fact copy with dry wit.
- Signature exclusions (do not clone): real brand wordmarks, proprietary product silhouettes, exact signature color systems, distinctive store UI chrome, and any layout fingerprint that would read as a specific commercial brand.
- Evidence confidence: Mechanisms stated in the brief (Observed as instructions); no live URL fetch in this run (Unknown for pixel-exact reference values — intentionally not needed).
- Date: 2026-08-12 · Request Anchor: FIELD-7 product page.

## Quality Gates

- Request Anchor fit: all requested modules present under industrial-functional constraints with no-clone boundary recorded.
- Contract validators: both ultimate-design Python scripts pass with zero errors.
- Rendered UI audit: `validate_html_visual.mjs` status pass, 0 fails, 0 warnings.
- Content: English, dry, fictional-but-plausible specs; exact footer attribution.
- Accessibility: AA contrast, keyboard, focus-visible, 44px targets, reduced motion.
- Responsive: 320–1440, schematic scales, annotations reflow, no page-level horizontal overflow.
- Performance/size: single file ≤160KB; only Google Fonts external; schematic complete without scroll drawing.
- Proof markers: `data-ud-check` on navigation, hero-schematic, features, knolling, specs, buy, footer.

## Assumptions

- Gallery iframe crops ~1280 wide × ~800 tall from the top; hero brand + schematic must read when scaled.
- Buy is intentionally non-transactional; status copy must say so.
- “Candidate” maturity is appropriate — verified by validators, not owner-locked.
- Pocket-synth dimensions/engines are fictional but physically plausible for a jacket-pocket device.
- Cool near-white `#F5F5F2` is acceptable vs warm cream ban (no terracotta pairing).

## Open Questions

- Should a future pass add a side-view schematic sheet as a second drawing?
- Is $329 the right demo price band for later multi-demo consistency?

## Review Log

- 2026-08-12: Bootstrapped contract and artifact for FIELD-7 industrial-functional product page (Build/YOLO/proof-run). Active OKF bound for taste, type, color, message, UX writing, hierarchy, necessary judgment, motion language/contract, a11y, responsive. Reference-study mechanisms adopted with explicit no-clone boundary.
- 2026-08-12: Repaired mobile horizontal overflow (CSS grid `minmax(0,1fr)` on knoll/feature grids; skip-link no longer uses `left:-9999px`). Re-ran validators: contract PASS, OKF PASS (11/11), visual audit PASS (0 fails / 0 warnings), HTML parse + JS check ok, no emoji, `index.html` ~43KB.

## Design Maturity

- Status: Candidate

## Motion Contract

- Motion id: `section-reveal`
- User-facing promise: Sections ease in once; schematic is fully drawn on arrival.
- Purpose: Hierarchy / attention to next block.
- Trigger model: view-entry (IntersectionObserver); hero reveals entry-play on rAF.
- Timing band: 360ms opacity + translateY; properties transform/opacity only.
- Initial state: `.reveal` starts at opacity 0 / translateY(12px); forced complete by 700ms fallback.
- Reduced-motion fallback: all `.reveal` immediately visible; transitions none.
- No-flash rule: force-reveal timeout and print styles prevent blank captures.
- Do-not-move: schematic paths are static (no stroke-dash storytelling).
- Validation: visual audit + manual reduced-motion CSS presence; motion contract script optional (no svg-draw markers).
