---
version: 0.1
name: SYSTEMA 2026
description: Swiss International Style landing page for a fictional one-day design systems conference at Meridian Hall on 16 October 2026.
colors:
  primary: "#E30613"
  secondary: "#000000"
  tertiary: "#5A5A5A"
  neutral: "#D0D0D0"
  surface: "#FFFFFF"
  on-surface: "#000000"
  error: "#B00020"
typography:
  headline-lg:
    fontFamily: "Inter Tight, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 700
    lineHeight: 0.86
  body-md:
    fontFamily: "Inter Tight, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: "Inter Tight, Helvetica Neue, Helvetica, Arial, sans-serif"
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
    textColor: "{colors.surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
---

# Design System

## Overview

SYSTEMA 2026 is a fictional one-day design systems conference landing page in English. The design read is **Swiss International Style as method**: a visible modular grid (hairline column rules), oversized flush-left ragged-right Helvetica-class sans (Inter Tight with Helvetica Neue / Arial fallbacks), black/white with exactly one red accent (`#E30613`), one diagonal poster type block, a schedule designed as a table, and a functional footer. No decoration that is not typographic or grid-derived. The first viewport must read as a festival poster at gallery thumbnail scale (~1280×800).

## Colors

- Scene sentence: A design-systems practitioner scanning a conference site on a bright desk lamp — paper white, ink black, one signal red for year/CTA marks only.
- Color posture: **Restrained** — neutrals dominate; primary red stays under ~10% of surface (year numeral, kickers, CTA fills, talk ticks).
- `--surface` `#FFFFFF` / `--on-surface` `#000000` for body reading (≥4.5:1).
- `--primary` `#E30613` for CTAs, year, section kickers, talk ticks; white text on red fills for buttons (≥4.5:1 for large UI labels).
- `--tertiary` / mute `#5A5A5A` for secondary meta (≥4.5:1 on white).
- `--neutral` `#D0D0D0` for soft grid hairlines / scrollbar.
- Anti-template locks: no purple/indigo SaaS gradients, no warm cream+terracotta luxury default, no broadsheet dense newspaper costume beyond intentional Swiss grid/table craft, no glow, no emoji.

## Typography

- Single Google family: **Inter Tight** (400/500/600/700) as Helvetica-class display and UI; stack `"Inter Tight", "Helvetica Neue", Helvetica, Arial, sans-serif`.
- Display: oversized uppercase brand (`headline-lg` token 96px; CSS `clamp` for responsive). Flush-left, ragged-right.
- Body 17px; labels 12px bold tracked uppercase for kickers and table heads.
- YAML tokens stay scalar px; responsive sizing lives in CSS only.
- Fallback stack must preserve Swiss read if fonts fail.

## Layout

One scrolling page: sticky nav, poster hero, speakers index, schedule table, venue/travel, register band, footer.

- Hero: brand-first poster — SYSTEMA + red 2026, date/venue meta, one lead, CTA pair, one −12° diagonal type block (“Design systems · in public”).
- Speakers: modular hairline list (name / role / talk) — not a card grid.
- Schedule: bordered table (time / session / speaker) with break rows; mobile uses a labeled horizontal scroller.
- Venue: address + travel + access + schematic SVG plan.
- Register: inverted black band with red CTA (visual/mailto only).
- Grid: 12-column hairline rules on hero/speakers/venue shells; max content 1120px; section padding ≥48px; marked zones sit on inner padded wraps with ≥36px gaps.
- Breakpoints: stack under ~720–900px; no page-level horizontal overflow at 320–1440.

## Elevation & Depth

Flat paper. Depth comes only from 1px black rules, section borders, and the single diagonal type slab. No shadows, blur, or parallax.

## Shapes

`rounded.none` on all surfaces and controls — International Style rectangles. Focus is a 3px red outline with offset. Talk ticks are 12px red squares.

## Components

- Primary button: red fill, white label, 48px min height, verb+object copy.
- Ghost button: white fill, 1px black border.
- Sticky nav with 44px+ text targets and red Register chip.
- Speaker index rows; schedule table; venue schematic SVG; footer link row.
- Scroll reveals (`.rise`) via IntersectionObserver with ~700ms force-reveal and print/reduced-motion fallbacks.

## Do's and Don'ts

- Do keep **SYSTEMA** as the hero-level brand signal; year in red.
- Do keep the modular grid visible and the schedule as a real table.
- Do keep exactly one red accent role; everything else black/white/gray.
- Do keep one diagonal type gesture only; contain rotation inside the hero clip.
- Do not clone a real festival brand signature (names, logos, exact poster layouts).
- Do not use cards in the hero, raster images, emoji, purple gradients, or soft shadows.
- Do not add external requests beyond one Google Fonts family.

## Request Anchor

- Original user request: Design the landing page for SYSTEMA 2026, a fictional one-day design systems conference (Meridian Hall; Oct 16, 2026); Swiss International Style; English; adopt Swiss festival/poster mechanisms (visible modular grid, oversized flush-left sans, B/W + one red, one diagonal type block, schedule as table, functional footer) without cloning a real brand signature; content = poster hero, 6–8 speakers, full-day schedule, venue/travel, register CTA (visual only).
- Latest user override: Deliver only `/workspace/docs/demos/systema/index.html` and `DESIGN.md`; hard HTML/contract constraints; gallery thumbnail striking at ~1280 top ~800; pass strict contract, OKF usage, and rendered visual audit with 0 fails and 0 warnings; no git/installs; write only inside the demo folder (except `/tmp`).
- Deliverable: Self-contained `index.html` plus this `DESIGN.md` contract.
- Primary audience: Design-systems practitioners and product designers deciding whether to attend a one-day conference.
- Core job to be done: In one scroll, recognize the event, scan speakers and schedule, understand venue/travel, and hit Register.
- Success criteria: First viewport reads as a Swiss poster (brand, date, CTA, diagonal gesture); eight fictional speakers; full-day table; venue note; register CTA; validators pass; ≤160KB; a11y and reduced-motion hold.
- Non-goals: No real tickets backend, no multi-page site, no raster photography, no second accent color, no card-grid marketing template.
- Must preserve: Fictional brand honesty; Swiss mechanism set; footer attribution line; `data-ud-check` on navigation/hero/speakers/schedule/venue/register/footer; English copy.
- Validation must check against: Request Anchor fit, OKF bindings, contrast/focus/44px targets, reduced motion, 320–1440 overflow, file size, both Python validators, rendered UI audit pass with zero warnings, HTML parse and JS syntax checks.

## Content Model

- User intent: Decide whether SYSTEMA 2026 is worth attending and how to register.
- Business intent: Drive registration interest via clear schedule and speaker credibility (demo mailto only).
- Message hierarchy: 1) Brand + date + place. 2) What the day is about. 3) Speakers. 4) Schedule. 5) Venue/travel. 6) Register.
- First-screen answers: What (SYSTEMA 2026), when/where (16 Oct, Meridian Hall), why (design systems conference), next (Register / View schedule).
- Primary action meaning: Request registration (mailto demo); secondary is view schedule.
- Voice and tone: Neutral, precise, institutional-modern; concrete nouns; no hype adjectives.
- Terminology rules: design systems, tokens, components, governance, library used consistently; SYSTEMA always uppercase in brand contexts.
- State language rules: Static marketing page; register is visual/mailto with honesty note; no form error states.
- Trust, risk, and help content: Access notes, travel specifics, capacity/price, fictional mailto disclaimer.
- Content risks: Cloning a real conference identity; burying the schedule; letting headline overpower brand; inventing real people.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: Swiss poster read; anti-default locks; layout-family budget (poster / modular index / table / inverted CTA).
- `design-okf/systems/type-personality.md`: Inter Tight as Helvetica-class memory feature; single family + system fallbacks.
- `design-okf/systems/color-system.md`: Restrained B/W + one red; AA contrast roles.
- `design-okf/foundations/layout-typography-composition.md`: Visible modular grid, asymmetry, flush-left rag, Swiss method (not costume).
- `design-okf/content/message-model.md`: First-screen brand → claim → CTA; section order speakers → schedule → venue → register.
- `design-okf/content/ux-writing.md`: Verb+object CTAs; specific talk titles and travel copy.
- `design-okf/systems/motion-language.md`: Entry opacity/transform reveals ≤320ms; static-first; reduced-motion hard stop.
- `design-okf/systems/motion-contract.md`: Reveal choreography with IO + 700ms force-reveal + print/reduced-motion completion.
- `design-okf/foundations/necessary-design-judgment.md`: Cut non-typographic ornament; schedule table is the craft centerpiece.
- `design-okf/digital/accessibility-usability.md`: Landmarks, focus-visible, ≥44px targets, AA contrast, skip link.
- `design-okf/digital/responsive-interaction.md`: Stack under 720–900; schedule internal scroller with affordance; no page overflow; rotated block clipped.
- `design-okf/governance/request-integrity.md`: Request Anchor nine fields drive critique and delivery checks.

### Support References

- `references/branch-marketing-site.md`
- `references/reference-study.md` (Swiss/International festival + poster archetype mechanisms; no signature transfer)
- `references/composition-search.md` (statement-led poster hero; modular index vs card grid; table as schedule family)
- `references/content-model.md`
- `references/design-contract.md`
- `references/proof-run-html.md`
- `references/visual-verification.md`
- `references/quality-gates.md`
- `SKILL.md` Operating Loop (Build route, YOLO)

### Decision Record

- Constraints extracted: single self-contained HTML; Google Fonts ≤2 families (using 1: Inter Tight) with `display=swap` + preconnect; no rasters/emoji; Swiss International Style; B/W + one red; visible modular grid; one diagonal type block; 6–8 speakers; schedule as table; venue/travel; register visual-only; English; footer attribution; `data-ud-check` on navigation/hero/speakers/schedule/venue/register/footer (inner padded containers); reduced-motion disables animation; motion transform/opacity ≤400ms; IntersectionObserver + ~700ms force-reveal + beforeprint/print reveal; WCAG AA; keyboard + focus-visible; ≥44px targets; 320–1440 no overflow; ≤160KB; gallery thumbnail striking.
- Deliberate exceptions: Mobile schedule uses an internal horizontal scroller (affordance + hint) so the table stays tabular instead of cardifying. Diagonal type is clipped by the hero shell so rotation never creates page overflow. Composition-search remains Support; chosen families are enforced via taste-engine + layout-typography bindings. Reference-study mechanisms adopted; no real festival brand cloned.
- Verification hooks:
  - `python3 skill/ultimate-design/scripts/validate_design_contract.py ... --strict-ultimate --require-frontmatter`
  - `python3 skill/ultimate-design/scripts/validate_okf_usage.py ...`
  - `node skill/ultimate-design/scripts/validate_html_visual.mjs --input docs/demos/systema/index.html --out /tmp/audit-systema` → status pass, 0 fails, 0 warnings
  - `html.parser` parse; `node --check` on extracted JS; emoji scan; `wc -c` ≤160KB

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Swiss International poster direction; reject purple gradients, cream+terracotta, glow, hero cards; memory = oversized SYSTEMA + red year + diagonal slab | Global CSS, hero, section families | Thumbnail read: brand + diagonal dominate; anti-default locks hold |
| `design-okf/systems/type-personality.md` | Inter Tight Helvetica-class display/UI; one Google family; system Helvetica/Arial fallbacks | Font `<link>`, `.hero-brand`, labels | Fonts blocked still Swiss-readable; display=swap present |
| `design-okf/systems/color-system.md` | Paper white, ink black, single red `#E30613` under 10%; mute gray for meta | `:root` tokens, CTAs, year, kickers | Body ≥4.5:1; white-on-red CTA readable |
| `design-okf/foundations/layout-typography-composition.md` | Visible 12-col hairline grid; flush-left rag; asymmetric hero; schedule as table craft | `.grid-shell`, hero, `.schedule` | Grid visible in screenshots; table not cardified |
| `design-okf/content/message-model.md` | First screen answers what/when/where/next; order speakers→schedule→venue→register | `[data-ud-check=hero]` and section order | Hero answers Request Anchor without scrolling past first viewport |
| `design-okf/content/ux-writing.md` | CTAs `Register for SYSTEMA` / `View the schedule` / `Request registration`; specific talk titles | Buttons, speakers, schedule, venue | No vague Learn more; terminology consistent |
| `design-okf/systems/motion-language.md` | Entry fade/rise opacity+transform ≤320ms; static works first; reduced-motion forces visible | `.rise`, `@media (prefers-reduced-motion)` | Reduced-motion shows full content; durations ≤400ms |
| `design-okf/systems/motion-contract.md` | View-entry reveals + hero entry-play; 700ms force-reveal; beforeprint + print CSS complete | Reveal script, print CSS | Captures never show hidden content; markers resolve |
| `design-okf/foundations/necessary-design-judgment.md` | Delete badge clusters/testimonials/stock art; keep poster, index, table, venue, CTA | Section inventory | Delete-test: each section earns a decision step |
| `design-okf/digital/accessibility-usability.md` | Landmarks, skip link, focus-visible, ≥44px controls, table headers, mailto honesty | Header/nav/main/footer, buttons, table | Keyboard path; focus ring; targets ≥44px |
| `design-okf/digital/responsive-interaction.md` | Stack under 720–900; schedule scroller isolated with hint; hero overflow clips diagonal | Breakpoints, `.schedule-scroll`, `.hero` | No page overflow 320–1440; scroller affordance visible |
| `design-okf/governance/request-integrity.md` | Freeze Request Anchor nine fields; validate delivery against them | `## Request Anchor`, QA | Every success criterion and must-preserve checked in Review Log |

## Information Architecture

- Core user tasks: Identify event, scan speakers, read schedule, plan travel, register.
- Page inventory: One landing page (`index.html`).
- Navigation model: Sticky anchors Speakers / Schedule / Venue / Register.
- Content hierarchy: Hero → Speakers → Schedule → Venue → Register → Footer.
- Primary CTA rules: Register is primary everywhere; schedule is secondary.

## Quality Gates

- Request Anchor fit: Swiss conference landing with required content modules and mechanisms.
- Content: Specific fictional copy; eight speakers; full-day table; footer attribution present.
- Visual: Brand-first poster hero; visible grid; one red; one diagonal; table craft; no AI-default cards/gradients.
- Accessibility: AA contrast, keyboard, focus-visible, ≥44px targets, reduced motion, print reveals.
- Responsive: Clean at 320/375/768/1024/1280/1440; no page horizontal overflow; internal schedule scroller only.
- Performance: Single file ≤160KB; only Google Fonts external.
- Contract: Both ultimate-design Python validators pass; `data-ud-check` zones present.
- Rendered UI audit: `validate_html_visual.mjs` status `pass` with 0 failures and 0 warnings.

## Assumptions

- Meridian Hall is treated as the fictional venue/district name per brief.
- CHF pricing and `register@systema.example` are demo-honest placeholders.
- Gallery iframe scales near 1280px width; hero min-height preserves thumbnail impact.
- Reference study input is mechanism-only from Swiss/International festival+poster tradition; no specific real brand is cloned.

## Open Questions

- Whether Integrator wants a second Google family for mono tabular times (currently Inter Tight tabular nums).
- Whether a future pass should add a printable PDF poster using the same tokens.

## Review Log

- 2026-08-12 — Build-route YOLO proof run: artifact-first `index.html`, then this contract; bound Active OKF concepts including Swiss layout + reference-study no-clone boundary; ran design-contract, OKF-usage, and rendered visual audit; Candidate direction pending owner lock.

## Design Maturity

- Status: Candidate

## Reference Study

- Source mode: Brief-supplied mechanism extraction from Swiss/International-style festival sites and poster tradition (Study route input).
- Provenance/rights: Third-party archetype / Unknown specific brands — diagnosis and mechanism adoption only.
- Mechanisms adopted: visible modular grid with hairline column rules; oversized flush-left ragged-right sans; black/white + one red; one rotated/diagonal type block as poster gesture; schedule as crafted table; functional footer; typographic/grid-derived ornament only.
- Signature exclusions: Do not clone any real festival’s name, logo, exact poster composition, proprietary type customizations, or photographic identity.
- Evidence confidence: Mechanisms listed as Inferred from archetype description in the user brief (not observed from a live third-party URL in this run).
- Date: 2026-08-12 · Linked to Request Anchor above.

## Motion Strategy

- Motion id: `systema-section-rise`
- User-facing promise: Sections ease in lightly as they enter view; hero content settles on load.
- Purpose: Hierarchy / continuity
- Trigger model: hero `entry-play`; sections `view-entry`
- Implementation route: CSS transition + IntersectionObserver
- Timing: ≤320ms opacity + translateY; transform/opacity only
- Initial state: `.rise` starts at opacity 0; force-reveal at ~700ms; `beforeprint` and `@media print` force visible; `prefers-reduced-motion` disables all animation
- Validation: rendered audit after 1000ms wait; reduced-motion CSS/JS matchMedia parity
