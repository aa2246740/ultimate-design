---
version: alpha
name: Maison Ombre Product Detail
description: Fictional quiet-luxury fragrance PDP for Eau de Parfum No.04 with CSS/SVG still-life, sensory accordion, sticky purchase bar, and editorial cross-sell.
colors:
  primary: "#3D4538"
  secondary: "#6B635A"
  tertiary: "#4F5A48"
  neutral: "#C9C2B6"
  surface: "#E8E2D8"
  on-surface: "#2A2F2A"
  error: "#8F3D35"
typography:
  headline-lg:
    fontFamily: "Newsreader, Iowan Old Style, Palatino Linotype, Palatino, Georgia, serif"
    fontSize: 60px
    fontWeight: 600
    lineHeight: 1.05
  body-md:
    fontFamily: "Source Sans 3, Source Sans Pro, Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.7
  label-md:
    fontFamily: "Source Sans 3, Source Sans Pro, Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
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

Maison Ombre is a fictional fragrance house product detail page for Eau de Parfum No.04 (Bois de Veille). The page sells through quiet certainty: bone and olive-ink neutrals, generous whitespace, a narrow reading measure, a composed CSS/SVG bottle still-life, long-form sensory copy in an accordion, a visual-only sticky purchase bar, and an editorial two-product “pairs with” row. No urgency, discounts, or exclamation.

Design Maturity: Candidate — one coherent direction implemented and verified against the Request Anchor; not owner-locked.

## Colors

- Scene sentence: late afternoon light on a limestone vanity; bone plaster, taupe shadow, olive-ink glass.
- Color posture: Restrained — bone field (~70%), olive-ink text, taupe labels, deep olive primary under ~10% for CTA.
- `surface` `#E8E2D8`: bone page field (cooler than cream `#F4F1EA`).
- `on-surface` `#2A2F2A`: olive-ink body and display (~10.6:1 on surface).
- `primary` `#3D4538`: CTA fill; text uses surface (~7.7:1).
- `secondary` `#6B635A`: taupe labels/kickers (~4.6:1 AA on surface).
- `tertiary` `#4F5A48`: olive support accents.
- `neutral` `#C9C2B6`: still-life stone and soft bands.
- `error` `#8F3D35`: reserved for future form errors.
- Muted body `#5A564E` (~5.7:1). Anti-template: no purple gradients, no cream+terracotta AI cluster, no neon glow, no discount badges.

## Typography

- Display: Newsreader (optical size) as quiet serif memory for brand and section titles; fallbacks Iowan Old Style / Palatino / Georgia.
- Body/UI: Source Sans 3 humanist sans for meta, accordion chrome, purchase controls; system sans fallbacks.
- Google Fonts: two families, `display=swap`, preconnect; YAML `fontSize` tokens stay scalar `px`.
- Narrow measure (~36rem / ~52ch) for sensory prose; kickers use small tracked uppercase sans.

## Layout

Single scrolling PDP:

1. Static top nav (brand + anchors).
2. Split hero: full-stage CSS/SVG still-life + brand-led product copy (gallery thumbnail crop).
3. Composition band: accordion — Notes (top/heart/base), Ingredients, How to wear.
4. Editorial pairs-with row (two fictional companions).
5. Footer attribution.
6. Fixed sticky purchase bar: size radios + Add to cart (demo only).

Composition choice: split-dialogue hero + narrative accordion + modular two-up cross-sell. Marked zones sit on inner padded content (`navigation`, `hero-product`, `notes`, `ingredients`, `how-to-wear`, `cross-sell`, `purchase-bar`, `footer`) with ≥36px gaps between siblings; end spacer keeps the sticky bar from covering footer samples.

## Elevation & Depth

Mostly flat bone field. Depth from soft radial washes, inset hairlines on the still-life stage, and a single paper-like purchase bar surface. No multi-layer card shadows, no glow stacks.

## Shapes

Near-rectilinear quiet luxury: `sm` radii on buttons, size chips, and still-life stage. Avoid pills and floating rounded media cards.

## Components

- Primary / ghost buttons.
- Keyboard accordion (`aria-expanded`, regions, `hidden` when closed).
- Size radio group (≥44×44 targets) and sticky purchase bar.
- Editorial cross-sell anchors with SVG thumbs (not promotional cards).
- Inline SVG bottle still-life with light/gloss gradients.

## Do's and Don'ts

- Do keep Maison Ombre as the hero-level brand signal beside the bottle still-life.
- Do write precise sensory English without exclamation, scarcity, or discount language.
- Do keep AA contrast on muted neutrals; darken taupe until small text passes.
- Do disable all animation under `prefers-reduced-motion`; force-reveal for print and post-load fallback.
- Do not clone Aesop (or any house) signature type, palette, bottle photography, or layout fingerprint — adopt mechanisms only.
- Do not use raster images, emoji, urgency badges, or card grids for storytelling sections.

## Request Anchor

- Original user request: Design a product detail page for "Maison Ombre - Eau de Parfum No.04", a fictional fragrance house. Quiet luxury. English. Adopt Aesop-class quiet-luxury commerce mechanisms without cloning a real brand signature.
- Latest user override: Proof-run HTML deliverables only at `docs/demos/maison/index.html` and `DESIGN.md`; self-contained vanilla file; Google Fonts ≤2 families; CSS/SVG still-life; accordion + sticky purchase bar + pairs-with row; validators must pass; gallery thumbnail must read luxury at ~1280×800.
- Deliverable: Single-file PDP plus this design contract under `docs/demos/maison/`.
- Primary audience: Fragrance buyers evaluating a quiet-luxury juice online; showcase gallery viewers judging craft.
- Core job to be done: Understand the scent, read composition detail, choose a size, and feel purchase-ready without pressure.
- Success criteria: First screen shows brand + still-life + product identity; accordion covers notes/ingredients/how-to-wear; sticky bar with sizes; two companions; AA contrast; keyboard accordion; reduced motion; validators pass; file ≤160KB.
- Non-goals: Real checkout, accounts, reviews module, dark mode toggle, photography, multi-page catalog.
- Must preserve: Fictional brand honesty; footer demo attribution line; no emoji/raster; no urgency/discount patterns; mechanism adoption without brand cloning.
- Validation must check against: Request Anchor nine fields; OKF bindings; HTML parse; JS syntax; no emoji; file size; rendered UI audit with zone gaps/occlusion; contrast/motion/responsive gates.

## Content Model

- User intent: Decide whether No.04 fits their skin and evening, then choose a size.
- Business intent: Present quiet-luxury credibility and a calm path to add-to-cart (demo).
- Message hierarchy: 1) Brand and juice identity 2) Sensory notes 3) Ingredients 4) How to wear 5) Companions 6) Size/purchase.
- First-screen answers: What — Maison Ombre No.04; Why — quiet woody-amber for evening; Next — choose a size / read the notes.
- Primary action meaning: Add to cart → demo confirmation only (no payment).
- Voice and tone: Precise, sensory, unhurried; like an atelier note, not a campaign.
- Terminology: Eau de parfum, notes (top/heart/base), drydown, companions; avoid “bestseller”, “limited”, “must-have”.
- State language: Cart button briefly shows “Added (demo)” then restores; size choice updates price label.
- Content risks: Do not imply a real fragrance house or clinical claims; keep INCI-style list clearly fictional/demo.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: quiet-luxury bone/olive-ink read; anti-default locks against purple SaaS, cream+terracotta, urgency commerce chrome.
- `design-okf/systems/type-personality.md`: Newsreader display + Source Sans 3 humanist support as memory pair.
- `design-okf/systems/color-system.md`: restrained bone/taupe/olive-ink roles with verified AA pairs.
- `design-okf/systems/typography-system.md`: narrow measure, readable body 17px, scalar YAML sizes.
- `design-okf/content/message-model.md`: first screen brand + juice + next action; accordion progressive disclosure.
- `design-okf/content/ux-writing.md`: precise CTAs (Choose a size, Add to cart, Read the notes); no exclamation.
- `design-okf/systems/motion-language.md`: bottle entry + section reveals; transform/opacity ≤400ms; reduced-motion off.
- `design-okf/digital/accessibility-usability.md`: AA, focus-visible, 44px targets, accordion ARIA, keyboard.
- `design-okf/digital/responsive-interaction.md`: sticky bar clearance, 320–1440 no horizontal overflow, stacked hero.
- `design-okf/foundations/necessary-design-judgment.md`: still-life replaces photography honestly; remove urgency chrome.
- `design-okf/governance/request-integrity.md`: Request Anchor fields drive critique and delivery checks.

### Support References

- `references/branch-marketing-site.md`
- `references/branch-web-product.md` (commerce sticky bar / control states)
- `references/reference-study.md` (Aesop-class mechanism extraction; no signature clone)
- `references/composition-search.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/proof-run-html.md`
- `references/visual-verification.md`
- `references/quality-gates.md`

### Decision Record

- Constraints extracted: Single self-contained HTML; ≤2 Google Font families; no raster/emoji; quiet-luxury mechanisms from reference study; accordion for notes/ingredients/how-to-wear; sticky purchase bar with sizes; two companion products; `data-ud-check` on named inner zones with ≥36px gaps; sticky bar must not occlude marked readable content; motion transform/opacity ≤400ms with IO + 700ms force-reveal + print reveal; WCAG AA; 320–1440 no overflow; ≤160KB; footer attribution required.
- Deliberate exceptions: Nav is static (not sticky) so the purchase bar is the only fixed chrome and occlusion risk stays single-edged. `hero-product` marks the title/lead block (not meta/CTAs or the tall still-life) so mobile first-viewport samples clear the sticky bar; the bottle remains the visual hero unmarked as decoration. Accent taupe values were darkened until small text meets AA rather than keeping a lighter decorative taupe for labels.
- Verification hooks:
  - `validate_design_contract.py --strict-ultimate --require-frontmatter`
  - `validate_okf_usage.py`
  - `validate_html_visual.mjs` → status pass, 0 fails, 0 warnings
  - `html.parser` parse; `node --check` on extracted JS; emoji scan; file size ≤160KB

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Quiet-luxury bone/olive scene; ban purple glow, cream+terracotta, urgency badges | Global CSS, hero still-life, purchase bar | Thumbnail read; anti-default locks in critique |
| `design-okf/systems/type-personality.md` | Newsreader + Source Sans 3 pair with system fallbacks | Font link, brand H1, section titles | Renders with fonts blocked; ≤2 families |
| `design-okf/systems/color-system.md` | Bone surface, olive-ink text, AA taupe secondary, olive primary CTA | `:root` tokens, buttons, labels | Contrast ≥4.5:1 body/muted; CTA ≥4.5:1 |
| `design-okf/systems/typography-system.md` | 17px body, ~36rem measure, scalar YAML sizes | Body/prose CSS, front matter | Long-form measure check; token validator |
| `design-okf/content/message-model.md` | Hero answers brand/juice/next; accordion discloses composition | `#top`, `#composition`, `#purchase` | First viewport what/why/next; IA order |
| `design-okf/content/ux-writing.md` | Precise CTAs; sensory copy; no exclamation or scarcity | Hero lead, accordion, cart label | Copy review against voice rules |
| `design-okf/systems/motion-language.md` | Bottle entry-play; IO reveals; 700ms force-reveal; print reveal; reduced-motion static | `.reveal`, `.bottle`, script | Reduced-motion disables animation; ≤400ms |
| `design-okf/digital/accessibility-usability.md` | Accordion ARIA, focus-visible, 44px controls, skip link | Accordion, size radios, nav, cart | Keyboard walkthrough; target audit |
| `design-okf/digital/responsive-interaction.md` | Stacked hero; sticky bar + end spacer; no overflow 320–1440 | Grid rules, `.scroll-end`, purchase bar | Rendered audit mobile/desktop |
| `design-okf/foundations/necessary-design-judgment.md` | CSS/SVG still-life as honest material; remove promo chrome | Still-life SVG, cross-sell row | Critique: no fake photo, no discount UI |
| `design-okf/governance/request-integrity.md` | Delivery checks against Request Anchor nine fields | This `DESIGN.md` + page modules | Strict contract validator Request Anchor pass |

## Information Architecture

- Core user tasks: Identify the juice, inspect notes/ingredients/wear guidance, choose size, add to cart (demo), glance at companions.
- Page inventory: One PDP (`index.html`).
- Navigation model: Brand → top; anchors Composition / Pairs with / Purchase.
- Content hierarchy: Hero → Composition accordion → Pairs with → Footer; purchase bar persistent.
- Primary CTA rules: Hero “Choose a size” focuses purchase; bar “Add to cart” is demo-only feedback.

## Quality Gates

- Request Anchor fit: Quiet-luxury PDP modules all present; English; fictional disclaimer.
- Content: Sensory precise copy; no urgency/discount language.
- Visual: Brand + still-life dominate first screen; thumbnail-legible; no card wallpaper.
- Accessibility: AA neutrals; keyboard accordion; focus-visible; ≥44px targets; reduced motion.
- Responsive: 320–1440; sticky bar clearance; no horizontal overflow.
- Interaction: Size syncs price; cart demo state; accordion expand/collapse.
- Performance: ≤160KB; Google Fonts only external; CSS/SVG only imagery.
- Contract consistency: Both Python validators pass; rendered UI audit pass with 0 fails/warnings.

## Assumptions

- Gallery iframe scales a ~1280px render and crops the top ~800px; hero still-life + brand must carry the luxury read without below-fold content.
- Google Fonts may be blocked; Georgia/Palatino + system sans keep hierarchy intact.
- Purchase is visual-only; no backend cart.
- Reference study provenance: third-party Aesop-class archetype — mechanisms only; no signature transfer.

## Open Questions

- Whether a real PDP would add batch/lot transparency or sample vial purchase as a second CTA.
- Whether production would replace the SVG still-life with licensed photography while keeping the same composition geometry.

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| alpha | 2026-08-12 | Bootstrapped Maison Ombre PDP and contract from Ultimate Design Build/YOLO proof-run with reference-study mechanisms | Worker deliverable for showcase gallery | Design worker agent |
| alpha | 2026-08-12 | Cleared mobile hero/purchase collision by compacting sticky bar and scoping `hero-product` mark; all validators green | Rendered UI audit repair | Design worker agent |

## Reference Study

- Source mode: Prompt-supplied style-mechanism extraction (Aesop-class quiet-luxury commerce archetype); no live URL fetch in this run.
- Provenance/rights: Third-party / signature work — diagnosis and transferable mechanisms only.
- Mechanisms adopted: muted warm neutrals; generous whitespace + narrow measure; refined serif display with humanist sans; composed still-life instead of lifestyle collage; long-form sensory accordion; sticky purchase chrome; editorial cross-sell row; anti-urgency.
- Signature exclusions: Do not copy Aesop (or any house) proprietary type, exact palette, bottle photography language, grid fingerprint, or verbal brand voice.
- Evidence confidence: Mechanisms listed as Inferred from the brief’s extraction; exact reference pixels Unknown (no image/URL attached).
- Request Anchor link: Quiet-luxury Maison Ombre PDP constraints above.
