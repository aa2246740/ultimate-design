---
version: 0.1
name: GRID&NOISE Portfolio
description: One-page neo-brutalist portfolio for a fictional independent design studio — manifesto, selected works ledger, services, and contact.
colors:
  primary: "#FFE500"
  secondary: "#FF3355"
  tertiary: "#00C8F0"
  neutral: "#D8D4CC"
  surface: "#F6F5F2"
  on-surface: "#0B0B0B"
  error: "#B00020"
typography:
  headline-lg:
    fontFamily: "Syne, Arial Black, Helvetica Neue, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 800
    lineHeight: 0.88
  body-md:
    fontFamily: "IBM Plex Sans, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.55
  label-md:
    fontFamily: "IBM Plex Sans, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
rounded:
  none: 0px
  sm: 0px
  md: 0px
  lg: 0px
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
    textColor: "{colors.on-surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
---

# Design System

## Overview

GRID&NOISE is a fictional independent design studio portfolio: one scrolling English page that sells attitude with discipline. The visual read is **print-shop neon-brutalism** — hazard yellow, ink black, hot coral, and electric cyan on a cool near-white field; 3px borders; solid offset shadows; raw CSS grid texture in the hero. Aggressive Syne display type carries the brand memory; IBM Plex Sans keeps body and UI readable. The page must punch when shown as a scaled gallery iframe (~1280px render, top ~800px visible): brand name first, one lead, two CTAs, and a hard black snapshot panel.

## Colors

- Scene sentence: A design director scanning a studio site on a bright midday laptop — fluorescent print-shop energy, stamped rubber shadows, type that reads like a protest poster without becoming illegible.
- Color posture: **Committed** — primary yellow owns large surface blocks and CTAs; secondary coral and tertiary cyan rotate as section accents; ink (`on-surface`) is the structural constant.
- `--surface` / paper `#F6F5F2` with `--on-surface` `#0B0B0B` for body reading (≥4.5:1).
- `--primary` `#FFE500` for CTAs, hero brand highlight, works year labels on dark; always paired with ink text.
- `--secondary` `#FF3355` for manifesto quote block and service tile; ink text only (no white-on-coral small text).
- `--tertiary` `#00C8F0` for section ticks, focus ring, and one service tile; ink text on cyan fills.
- `--neutral` `#D8D4CC` for footer and quieter service tile.
- Works section inverts to ink field with paper text; muted paper at ~78% alpha for secondary lines.
- Anti-template locks: no purple/indigo SaaS gradients, no warm cream+terracotta luxury default, no broadsheet hairline newspaper layout, no soft glow elevation.

## Typography

- Display: Syne 700/800 — geometric, loud, ownable; scales with `clamp()` in CSS while YAML tokens stay scalar px.
- Body/UI: IBM Plex Sans 400–700 — industrial clarity for manifesto, works outcomes, form labels.
- Labels: same body family at 12px bold, tracked uppercase for section ticks and meta.
- Fallback stack must preserve weight and wrapping if Google Fonts fail (`Arial Black` / system sans).
- Aggressive sizes wrap via `clamp()` and `text-wrap: balance`; no single-line overflow at 320px.

## Layout

One page, sticky nav, six semantic zones: navigation, hero, manifesto, works, services, contact, plus footer.

- Hero: statement-led typographic poster with raw grid backdrop; brand is the largest signal; supporting panel is a black slab with stripe graphic and three mono-adjacent stats.
- Manifesto: split editorial — section head left, coral quote + rules right.
- Works: modular text index on ink (year / name / client type / outcome); not a card grid.
- Services: two-by-two catalog strip with hard borders and alternating filled tiles.
- Contact: split workbench — studio desk meta + labeled form.
- Footer: sparse chrome with required demo attribution line.
- Breakpoints: stack under ~720–860px; max content width 1120px; page padding 16px minimum.

## Elevation & Depth

Depth is print-shop, not glass. Elevation comes only from **solid offset shadows** (`4–6px 4–6px 0 #0B0B0B`) and 3px ink borders. No blur, no multi-layer soft shadows, no parallax. Hover may translate the control by 2px while growing the shadow so layout does not shift.

## Shapes

`rounded.none` everywhere on surfaces and controls — neo-brutalist rectangles only. Focus uses a 3px cyan outline with offset; decorative ticks are 12px squares with a 2px ink border.

## Components

- Primary button: yellow fill, ink text, 3px border, solid offset shadow, min-height 48px; hover translates without reflow.
- Secondary button: paper fill, same border/shadow language.
- Sticky nav with 44px+ text targets.
- Works rows as full-width focusable anchors (list semantics).
- Service tiles as articles (color blocks, not soft cards).
- Contact form with visible labels, native validation, live status region.
- Skip link to `#main`.

## Do's and Don'ts

- Do keep GRID&NOISE as the hero-scale brand signal, larger than the supporting headline in the black panel.
- Do use the works section as a text ledger — year, client type, one-line outcome — not image cards.
- Do honor `prefers-reduced-motion` by disabling reveal transitions and hover translates.
- Do keep WCAG AA pairs: ink on paper/yellow/coral/cyan; paper on ink.
- Do not use emoji, raster images, purple gradients, soft glows, or rounded pill clusters.
- Do not let display type overflow horizontally; wrap or clamp.
- Do not ship hover effects that push siblings (shadow/transform only).
- Do not claim GRID&NOISE is a real studio; keep the demo attribution footer.

## Request Anchor

- Original user request: Design a one-page portfolio for GRID&NOISE, a fictional independent design studio: manifesto, text-based selected-works list (6-8 fictional projects with year, client type, one-line outcome), services, and contact. Neo-brutalist: hard borders, offset solid shadows, aggressive typography, raw grid — readable, accessible, deliberate. English copy with attitude but no profanity. Deliver `index.html` and `DESIGN.md` only under `docs/demos/gridnoise/`.
- Latest user override: None — execute the prompt as given (Build route, YOLO, proof-run HTML constraints).
- Deliverable: `/workspace/docs/demos/gridnoise/index.html` (single self-contained HTML) and `/workspace/docs/demos/gridnoise/DESIGN.md`.
- Primary audience: Design leads and founders evaluating a studio’s taste and craft in under a minute; secondary: gallery visitors viewing a scaled iframe thumbnail.
- Core job to be done: Immediately recognize the studio’s neo-brutalist voice, scan credible work outcomes, understand services, and know how to start a brief.
- Success criteria: First viewport punches at thumbnail scale with brand-first hierarchy; 6–8 works with year/client/outcome; manifesto + services + contact present; AA contrast; keyboard/focus/44px targets; reduced-motion safe; 320–1440 responsive without horizontal overflow; validators pass; file ≤160KB.
- Non-goals: CMS, real backend form submit, dark/light theme toggle, multi-page site, raster photography, animation as a primary story.
- Must preserve: Fictional studio framing; required footer attribution line; `data-ud-check` on major zones; Google Fonts only as external requests (≤2 families); vanilla inline CSS/JS.
- Validation must check against: Request Anchor fit; both contract validators; HTML parse; JS syntax; no emoji; file size; semantic zones; contrast/motion/responsive constraints in this contract.

## Content Model

- User intent: Judge whether this studio’s taste and rigor fit a high-visibility brand/product brief.
- Business intent: Convert curiosity into a brief email using attitude that still feels professional.
- Message hierarchy: 1) Brand + stance. 2) Manifesto rules. 3) Proof via works ledger. 4) Services. 5) Contact path.
- First-screen answers: Who (GRID&NOISE), what (independent studio; systems with hard edges), next action (see works / start a brief).
- Primary action meaning: Start a brief — opens contact; form captures an outline locally and points to email for real send.
- Voice and tone: Confident, sharp, slightly confrontational; no profanity; specific nouns and outcomes.
- Terminology rules: Prefer “brief,” “system,” “ledger,” “ops,” “outcome”; avoid “synergy,” “delight,” “seamless.”
- State language rules: Form invalid → explain missing fields and focus first invalid; success → local capture note + real email path.
- Trust/risk content: Fictional clients labeled by type; footer discloses demo/fictional status.
- Content risks: Over-chaos neo-brutalism harming readability; invented metrics presented as real case studies — keep outcomes plausible and clearly portfolio fiction via footer.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: high experiment-risk neo-brutalist dials, anti-default locks, layout-family budget, thumbnail memory feature.
- `design-okf/systems/type-personality.md`: Syne display as brand memory; Plex Sans for readable utility/content roles; two-family WebFont budget with fallbacks.
- `design-okf/systems/color-system.md`: committed hazard palette with role-first AA pairs on bold blocks.
- `design-okf/digital/accessibility-usability.md`: WCAG AA, keyboard, focus-visible, 44px targets, reduced motion, labeled form.

### Support References

- `references/branch-marketing-site.md`
- `references/proof-run-html.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/quality-gates.md`
- `references/visual-verification.md`
- `SKILL.md` (Build route, YOLO)

### Decision Record

- Constraints extracted: Single-file vanilla HTML; ≤2 Google Font families with `display=swap`; no rasters/emoji; neo-brutalist borders/shadows/type/grid without chaos; manifesto + 6–8 text works + services + contact; footer attribution; `data-ud-check` zones; motion ≤400ms transform/opacity with reduced-motion; AA contrast; 320–1440 no overflow; ≤160KB; DESIGN.md must pass both validators.
- Deliberate exceptions: Services use filled bordered tiles (border+shadow language) rather than pure text because color blocking is part of the neo-brutalist brand read — still not soft elevated cards. The hero black panel is a CSS/SVG-free graphic slab (copy + stripe), not a soft media card, so the first viewport keeps brand + lead + CTAs + one dominant hard visual.
- Verification hooks: `validate_design_contract.py --strict-ultimate --require-frontmatter`; `validate_okf_usage.py`; `html.parser` parse; extract JS + `node --check`; emoji scan; byte size ≤160KB; manual checklist for zones, focus, reduced-motion CSS, clamp wrapping.

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Print-shop neo-brutalism with dials variance 8 / density 5 / motion 2 / distinction 9 / type 8 / experiment 8; ban purple gradients, cream-terracotta luxury, card-grid works, soft glows; four layout families across six sections | Hero grid+brand slam, works ledger, services strip, manifesto split | Thumbnail-scale brand readable; adjacent sections change family; no banned defaults in CSS |
| `design-okf/systems/type-personality.md` | Syne 800 carries GRID&NOISE memory; IBM Plex Sans recedes for body/UI; max two Google families + system fallbacks | Font links, `.hero-brand`, `.section-title`, body copy | Fonts blocked still layout-intact; clamp wraps at 320px; no Inter/Roboto/Arial-only display |
| `design-okf/systems/color-system.md` | Committed yellow/coral/cyan/ink roles; ink text on saturated fills; works section inverted ink field | `:root` tokens, hero/manifesto/services fills, works section | Contrast AA for body and UI; no white small text on coral/yellow |
| `design-okf/digital/accessibility-usability.md` | Semantic landmarks, skip link, focus-visible cyan ring, 44px+ targets, labeled form, reduced-motion reveals off | Nav, buttons, form, `.reveal` script/CSS | Keyboard tab order works; reduced-motion shows content immediately; targets ≥44px |

## Information Architecture

- Core user tasks: Understand studio stance → scan proof → pick a service mental model → contact.
- Page inventory: Single `index.html` portfolio.
- Navigation model: Sticky primary anchors (Manifesto, Works, Services, Contact) + footer mirrors.
- Content hierarchy: Hero → Manifesto → Selected works (8) → Services (4) → Contact → Footer.
- Primary CTA rules: “See selected works” and “Start a brief” / “Send brief outline” use verb + object.

## Quality Gates

- Request Anchor fit: all requested sections present with neo-brutalist constraints honored.
- Contract validators: both ultimate-design scripts pass with zero errors.
- Content: English attitude copy, no profanity, fictional but specific project outcomes.
- Accessibility: AA contrast pairs, keyboard, focus-visible, labels, reduced motion.
- Responsive: 320–1440, no horizontal overflow, clamp type.
- Performance/size: single file ≤160KB; only Google Fonts external.
- Proof markers: `data-ud-check` on navigation, hero, manifesto, works, services, contact, footer (plus sparse child zones where useful).

## Assumptions

- Gallery iframe is ~1280×800 crop; hero brand+lead+CTA+panel must read when scaled down.
- Form is demo-only; success copy must redirect users to the mailto for real contact.
- “Candidate” maturity is appropriate — direction verified by validators/self-checks, not owner-locked.
- Cool near-white `#F6F5F2` is acceptable vs warm cream ban (not terracotta pairing).

## Open Questions

- Should a future pass add a printable PDF leave-behind using the same tokens?
- Is Portland PT the preferred fictional studio locale for later multi-demo consistency?

## Review Log

- 2026-08-12: Bootstrapped contract and artifact for GRID&NOISE neo-brutalist portfolio (Build/YOLO/proof-run). Active OKF: taste-engine, type-personality, color-system, accessibility-usability. Removed hero stats to protect first-viewport budget. Self-checks and both validators pass.

## Design Maturity

- Status: Candidate
