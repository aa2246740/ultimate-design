---
version: alpha
name: Finlytics Marketing Landing
description: Dark, data-forward marketing landing for Finlytics, a fictional real-time revenue analytics platform for subscription B2B SaaS Finance and RevOps leaders.

colors:
  primary: "#E8A317"
  secondary: "#2EC4A8"
  tertiary: "#6B8CFF"
  neutral: "#8A93A6"
  surface: "#070B12"
  on-surface: "#E7EDF6"
  error: "#FF6B6B"

typography:
  headline-lg:
    fontFamily: "Sora, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
  body-md:
    fontFamily: "Sora, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
  label-md:
    fontFamily: "IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 14px
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
    textColor: "#14110A"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
---

# Design System

## Overview

Finlytics is a fictional real-time revenue analytics platform. This demo is a single self-contained marketing landing page aimed at heads of Finance and RevOps at B2B SaaS companies. The visual direction is a **night operations console**: graphite field, amber revenue signal, teal telemetry, and a believable product surface drawn entirely in CSS/SVG. The first viewport must read as one composition and remain striking when scaled as a ~1280×800 gallery iframe thumbnail.

## Colors

- Scene sentence: Finance and RevOps leaders review this after hours under cool monitor light, needing calm precision rather than startup flash.
- Color posture: restrained dark field with amber primary under ~10% of the surface for CTAs and key marks; teal secondary for live data; cool blue tertiary for recognition bridge graphics.
- `--surface` `#070B12` page field; raised panels `#0F1622` / `#141C2B`.
- `--on-surface` `#E7EDF6` body text; muted `#A3ADC0`; neutral labels `#8A93A6`.
- Primary amber `#E8A317` on dark for CTAs and “Today” marks; button label ink `#14110A`.
- Secondary teal `#2EC4A8` for live indicators and chart strokes; error `#FF6B6B` for churn/contraction.
- Anti-template locks: no purple/indigo SaaS gradients, no neon glow stacks, no warm-cream editorial palette, no generic flat white-card dashboard look.

## Typography

- Brand/display and body share **Sora** (Google Fonts, `display=swap`) for a geometric, confident voice without Inter/Roboto defaults.
- Data labels, tabs, and instrument captions use **IBM Plex Mono**.
- Full system fallbacks required on both stacks. At most two families; two weights on Mono (400/500), up to four on Sora (400–700).
- Hero brand name is the largest type signal; the headline supports it and must not overpower the wordmark.

## Layout

- Sticky navigation with brand, three anchors, and primary demo CTA.
- Hero (evidence-stage + split): left claim column (eyebrow, **Finlytics** brand, headline, lead, CTA pair); right/dominant SVG product console.
- Features as a mechanism rail (icon + title + proof label + copy), not a card grid.
- Pricing: three plans with Growth featured.
- Closing demo CTA panel with practical attendance details.
- Footer with required fictional-brand attribution line.
- Breakpoints: stack under ~800–980px; no horizontal overflow from 320 to 1440.

## Elevation & Depth

- Depth comes from layered dark surfaces, hairline borders, and one soft product shadow. No multi-layer colored glows.
- Product console is the only elevated object; feature and pricing sections stay flatter.

## Shapes

- Controls and panels use `sm`–`lg` radii (4–14px). Avoid pill clusters and oversized rounded-full chrome.
- Charts and icons are rectangular/linear SVG geometry to reinforce the console read.

## Components

- Primary button: amber fill, dark ink, 48px min height, verb+object labels.
- Ghost button: hairline border, hover border shifts toward teal.
- Sticky nav CTA mirrors primary action.
- Product surface: chrome tabs, live lag label, MRR area chart, recognition bridge, ledger event feed.
- Pricing plans: list with SVG checks; featured Growth plan with badge.
- Focus-visible ring using primary on surface.

## Do's and Don'ts

- Do keep **Finlytics** as the hero-level brand signal.
- Do keep fabricated metrics inside the clearly fictional product UI mock only.
- Do keep motion to transform/opacity ≤400ms with a hard `prefers-reduced-motion` off switch.
- Do keep touch targets ≥44px and WCAG AA contrast on text roles.
- Do not use raster images, emoji, lorem ipsum, or real company/people names.
- Do not use card grids in the hero or as the default section structure.
- Do not add external requests beyond the two Google Fonts families.

## Request Anchor

- Original user request: Design a marketing landing page for Finlytics, a fictional real-time revenue analytics platform for subscription businesses; audience heads of finance and RevOps at B2B SaaS; dark, data-forward, credible; believable product surface with charts in CSS/SVG; include pricing and a demo CTA; English copy.
- Latest user override: Deliver only `/workspace/docs/demos/finlytics/index.html` and `DESIGN.md` under hard HTML/contract constraints; gallery thumbnail must look striking at ~1280×800; pass both ultimate-design validators; no git/installs; no files outside the demo folder except `/tmp` scratch.
- Deliverable: Self-contained `index.html` plus this `DESIGN.md` contract.
- Primary audience: Heads of Finance and RevOps at B2B SaaS companies evaluating revenue analytics tools.
- Core job to be done: In one scroll path, understand what Finlytics reconciles, trust the product surface, compare pricing, and book a demo.
- Success criteria: First viewport identifies brand, offer, product evidence, and demo CTA; pricing and demo sections present; validators pass; file ≤160KB; a11y and reduced-motion constraints hold.
- Non-goals: No real backend, no light theme, no blog, no customer logos wall, no raster assets, no multi-page site.
- Must preserve: Fictional brand honesty, English copy, dark data-forward direction, SVG/CSS-only graphics, footer attribution line, `data-ud-check` zones.
- Validation must check against: Request Anchor fit, OKF bindings, contrast/focus/targets, reduced motion, 320–1440 overflow, file size, both Python validators, HTML parse and JS syntax checks.

## Content Model

- User intent: Decide whether Finlytics is credible enough to book a demo for Finance + RevOps.
- Business intent: Convert evaluators via a specific demo CTA after pricing clarity.
- Message hierarchy: 1) Brand + reconciled revenue claim. 2) Live product evidence. 3) Capability proof points. 4) Pricing. 5) Demo logistics.
- First-screen answers: What it is (Finlytics), why it matters (reconciled MRR before the board deck), what to do next (Book a product demo), credibility (streaming console + SOC 2 note).
- Primary action meaning: Book/request a live demo; secondary is compare plans.
- Voice and tone: Precise, operator-credible, specific dollars and controls; never hype-y.
- Terminology rules: MRR, expansion, contraction, churned, recognition, ASC 606, ledger, board pack used consistently.
- State language rules: Static marketing page; mailto demo request only; no form error states required.
- Trust, risk, and help content: SOC 2 note, fictional connector names (Billora/Ledgerly), pricing cancellation note, demo attendance expectations.
- Content risks: Inventing real customers; overclaiming AI magic; burying pricing; letting headline overpower brand.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: night-ops console read; anti-default locks; layout-family budget across hero/features/pricing/cta.
- `design-okf/systems/type-personality.md`: Sora brand/body + IBM Plex Mono instrument labels; two-family Google Fonts cap.
- `design-okf/systems/color-system.md`: restrained dark palette with amber/teal/blue roles and AA contrast pairs.
- `design-okf/content/message-model.md`: first-screen brand → claim → evidence → CTA order.
- `design-okf/content/ux-writing.md`: verb+object CTAs and specific Finance/RevOps language.
- `design-okf/systems/motion-language.md`: entry opacity/transform reveals only; static-first; reduced-motion hard stop.
- `design-okf/foundations/necessary-design-judgment.md`: delete non-essential chrome; product surface is the memory feature.
- `design-okf/digital/accessibility-usability.md`: landmarks, focus-visible, 44px targets, AA contrast.
- `design-okf/governance/request-integrity.md`: Request Anchor fields drive critique and delivery checks.

### Support References

- `references/branch-marketing-site.md`
- `references/composition-search.md` (evidence-stage + split-dialogue hero; mechanism rail vs card grid)
- `references/content-model.md`
- `references/design-contract.md`
- `references/proof-run-html.md`
- `references/visual-verification.md`
- `references/quality-gates.md`
- `SKILL.md` Operating Loop (Build route, YOLO)

### Decision Record

- Constraints extracted: single HTML file; Google Fonts only (≤2 families, display=swap, preconnect); no rasters/emoji; dark data-forward credible tone; SVG/CSS charts; pricing + demo CTA; English; footer attribution; `data-ud-check` on navigation/hero/product-surface/features/pricing/cta/footer; reduced-motion disables animation; motion transform/opacity ≤400ms; WCAG AA; keyboard + focus-visible; ≥44px targets; 320–1440 no overflow; ≤160KB; gallery thumbnail striking at ~1280 top ~800.
- Deliberate exceptions: Fabricated product metrics appear only inside the labeled fictional console mock (demo honesty). Pricing plans use bordered containers because they are interactive choice units, not decorative cards. Composition-search remains a support reference; its chosen families are enforced via taste-engine bindings.
- Verification hooks:
  - `python3 .../validate_design_contract.py ... --strict-ultimate --require-frontmatter`
  - `python3 .../validate_okf_usage.py ...`
  - HTML parser tag balance; `node --check` on extracted JS
  - Grep for emoji; `wc -c` file size ≤160KB
  - Manual contrast/focus/reduced-motion review notes for Integrator rendered pass

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Night-ops console direction; reject purple gradients, glow cards, hero card grids; memory feature is the SVG revenue console | Global CSS theme, hero composition, feature rail | Thumbnail read: brand + console dominate; anti-default locks hold in critique |
| `design-okf/systems/type-personality.md` | Sora for brand/UI; IBM Plex Mono for instrument labels; system fallbacks; ≤2 Google families | Font `<link>`s, `.hero__brand`, `.panel__title`, labels | Fonts blocked still readable; no third family; display=swap present |
| `design-okf/systems/color-system.md` | Graphite surface, amber primary CTA, teal live data, blue recognition accents; AA text pairs | `:root` color tokens, buttons, charts | Body text ≥4.5:1 on surface; primary button ink readable on amber |
| `design-okf/content/message-model.md` | First screen answers what/why/next via brand, claim, product evidence, demo CTA | `[data-ud-check=hero]`, product surface, primary buttons | Hero answers Request Anchor without scrolling past first viewport |
| `design-okf/content/ux-writing.md` | CTAs are verb+object (`Book a product demo`, `Compare plans`); specific MRR/ASC 606 language | Buttons, feature copy, pricing, CTA band | No vague Learn more or Submit; terminology consistent |
| `design-okf/systems/motion-language.md` | Entry fade/rise via opacity+transform ≤320ms; product entry-play on load; reduced-motion forces static visible state | `[data-motion]`, `.product`, `@media (prefers-reduced-motion)` | Reduced-motion shows full content with no animation; durations ≤400ms |
| `design-okf/foundations/necessary-design-judgment.md` | Cut decorative badge clusters and fake testimonials; keep only console, capability rail, pricing, demo logistics | Section inventory | Delete-test: removing any section loses a decision step |
| `design-okf/digital/accessibility-usability.md` | Semantic landmarks, skip link, focus-visible, ≥44px controls, chart aria-labels | Header/nav/main/footer, buttons, SVG charts | Keyboard tab order works; focus ring visible; targets meet 44px |
| `design-okf/governance/request-integrity.md` | Freeze Request Anchor nine fields and validate delivery against them before closeout | `## Request Anchor`, final QA checklist | Every success criterion and must-preserve item checked in Review Log |

## Information Architecture

- Core user tasks: Identify offer, inspect product evidence, scan capabilities, compare pricing, book demo.
- Page inventory: One landing page (`index.html`).
- Navigation model: Sticky anchors to Product, Capabilities, Pricing; persistent Book a demo.
- Content hierarchy: Hero → Product surface → Features → Pricing → Demo CTA → Footer.
- Primary CTA rules: Demo is primary everywhere; pricing comparison is secondary.

## Quality Gates

- Request Anchor fit: Brand, dark data-forward marketing page, SVG product charts, pricing, demo CTA, English.
- Content: Specific copy; fictional metrics confined to product mock; footer attribution present.
- Visual: Brand-first hero; console as dominant evidence; varied section families; no purple/glow defaults.
- Accessibility: AA contrast roles, keyboard, focus-visible, ≥44px targets, reduced motion.
- Responsive: Clean at 320/375/768/1024/1280/1440; no horizontal overflow.
- Performance: Single file ≤160KB; only Google Fonts external.
- Contract: Both ultimate-design validators pass; `data-ud-check` zones present.
- Rendered review: Integrator should re-check iframe thumbnail crop, chart legibility at scale, and mobile stacking.

## Assumptions

- Billing connectors are fictional (Billora, Ledgerly) to avoid naming real vendors.
- Mailto `demo@finlytics.example` is sufficient for the demo CTA without a form backend.
- Gallery iframe scales the live page near 1280px width; hero min-height ~720px on desktop preserves thumbnail impact.
- Browser-rendered visual audit may be unavailable in this worker environment; machine validators + static checks are the local proof.

## Open Questions

- Whether a future pass should add a real booking form vs mailto.
- Whether Integrator wants a second language; current request is English only.
- Whether pricing dollars should be localized for non-US evaluators later.

## Review Log

- 2026-08-12 — Build-route YOLO proof run: created `index.html` then this contract; bound nine Active OKF concepts; ran design-contract and OKF-usage validators; ran HTML parse, JS syntax, emoji, and file-size self-checks; Candidate direction pending owner lock.
