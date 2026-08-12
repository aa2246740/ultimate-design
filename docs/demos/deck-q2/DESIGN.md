---
version: 0.1
name: MoNote Q2 Growth Review Deck
description: Self-contained Chinese HTML presentation deck for fictional subscription notebook product 墨记 MoNote, covering 2026 Q2 growth, retention, revenue, insights, and Q3 plan.
colors:
  primary: "#0F5C4C"
  secondary: "#2A3A45"
  tertiary: "#C47820"
  neutral: "#E6EBEF"
  surface: "#F3F5F7"
  on-surface: "#1A2220"
  error: "#B33A2B"
typography:
  headline-lg:
    fontFamily: "Noto Serif SC, Songti SC, STSong, Georgia, serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.25
  body-md:
    fontFamily: "Noto Sans SC, PingFang SC, Microsoft YaHei, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  label-md:
    fontFamily: "Noto Sans SC, PingFang SC, Microsoft YaHei, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  primary-button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
---

# Design System

## Overview

This contract governs the HTML demo deck at `docs/demos/deck-q2/index.html`: a live-meeting Q2 growth review for the fictional subscription notebook product **墨记 MoNote**. The deck is Chinese-first, executive-density, and title-driven — a skim of slide titles alone should tell the story. Visual direction is **cool mineral paper + deep teal ink**: a projection-friendly light stage, serif brand display on the cover, quiet sans for body and data, one amber accent for cautionary numbers. It deliberately rejects purple SaaS gradients, warm cream/terracotta report kits, broadsheet newspaper grids, and card-stacked slide templates.

## Colors

- `--surface` `#F3F5F7`: cool paper stage (not warm cream).
- `--on-surface` `#1A2220`: primary ink for titles and body.
- `--primary` `#0F5C4C`: brand teal for rules, active marks, positive deltas, chart fills.
- `--secondary` `#2A3A45`: slate for secondary chart series and chrome labels.
- `--tertiary` `#C47820`: amber for caution (ARPU lag, year-plan discount risk), used sparingly.
- `--neutral` `#E6EBEF`: bar tracks and soft rules.
- `--error` `#B33A2B`: reserved for true negatives; unused on most slides.
- `--muted` `#5A6562`: supporting copy at AA contrast on surface.
- Cover uses a deep teal-to-slate field with ivory type; body slides stay light for meeting-room projection.

## Typography

Cover and section brand use **Noto Serif SC** (Songti voice: editorial notebook authority). Body, labels, chart text, and navigation use **Noto Sans SC**. At most two Google Font families, `display=swap`, with full system fallbacks so layout survives network failure. Display type is large on the cover for gallery thumbnail strength; body slides keep conclusion titles around 22–34px and supporting copy around 14–17px. Data numerals use tabular lining where practical. Letter-spacing stays near zero except small uppercase kickers.

## Layout

A letterboxed 16:9 stage inside the viewport; slides never cause page-level horizontal overflow from 320px to 1440px. Each slide is a full-bleed `section.slide` with a fixed rhythm: kicker → conclusion title → one lead sentence → evidence body. Archetypes vary by job: cover brand field, agenda list, metric+chart data pages, insight split, lesson list, plan two-column, close decision list. No recurring title-plus-card grids. Bottom chrome holds brand, prev/next (44px+), and `n / total` counter. URL hash `#n` deep-links each slide.

## Elevation & Depth

Flat paper. Depth comes from hairline rules, a single left accent on callouts, and a soft stage shadow in screen mode only. No stacked card shadows, glows, or floating badges. Cover is a flat color field with one gold rule.

## Shapes

Mostly rectangular. Controls use `sm` radius (4px). Bars and metric top-rules are square-edged or lightly rounded (`sm`). No pill clusters. Decorative marks are short rules or 6px square bullets, not emoji.

## Components

- **Stage + slides**: one visible slide; keyboard and button navigation; hash sync.
- **Primary button (nav)**: consumes surface/on-surface/label-md/sm radius tokens; 44px minimum target; visible `:focus-visible`.
- **Metric block**: label, large value, delta line.
- **Charts**: CSS bars with numeric labels; inline SVG line and column charts with text values.
- **Agenda / lesson lists**: ruled rows, not cards.
- **Callout**: left amber rule + judgment sentence.
- **Print**: `@media print` shows one slide per page and hides chrome.

## Do's and Don'ts

- Do write conclusion titles so a title-only skim narrates the deck.
- Do keep claim / evidence / action on every content slide.
- Do label chart values in real text, not color alone.
- Do honor `prefers-reduced-motion` with instant slide changes.
- Do keep the cover brand dominant at iframe-thumbnail scale.
- Do not use raster images or emoji.
- Do not invent a second brand palette mid-deck.
- Do not turn every slide into metric cards.
- Do not use motion longer than 400ms or non-transform/opacity slide transitions.
- Do not present fictional data as real; the cover footnote discloses fiction.

## Request Anchor

- Original user request: `$ultimate-design` 把「2026 Q2 增长复盘」做成一个 HTML 演示 deck，给虚构订阅制笔记产品「墨记 MoNote」：8–10 页，含封面、议程、Q2 三个关键数据页（增长、留存、收入，CSS/SVG 图表）、两页洞察与教训、下季度计划页、结尾页；键盘左右翻页、底部页码、可打印；数据虚构但自洽；中文，汇报语气直接有判断。
- Latest user override: Deliver exactly `docs/demos/deck-q2/index.html` and `docs/demos/deck-q2/DESIGN.md`; follow ultimate-design Build-route YOLO proof-run HTML order; pass both design-contract and OKF-usage validators; no files outside that folder (except `/tmp` scratch).
- Deliverable: Single self-contained HTML deck plus this design contract.
- Primary audience: Internal leadership / growth partners in a live Chinese business review (also printable handout).
- Core job to be done: Align on Q2 results, shared judgments, and Q3 bets without wading through raw tables.
- Success criteria: 8–10 slides with required sections; keyboard + on-screen nav + hash + print; charts labeled; AA contrast; reduced motion; file ≤160KB; validators pass; cover reads strongly in gallery thumbnail.
- Non-goals: Real product data, editable PPTX, speaker-notes app, dark/light theme toggle, multi-file asset pipeline.
- Must preserve: Fictional brand honesty footnote on cover; Chinese report tone; vanilla single-file constraints; `section.slide` + `data-ud-check` markers.
- Validation must check against: Slide count 8–10; every slide has `class="slide"` and `data-ud-check`; nav/hash/print/reduced-motion; chart text labels; file size; both Python validators; HTML parse and JS syntax check.

## Content Model

- User intent: Understand what worked in Q2 and what to fund in Q3.
- Business intent: Lock budget shift from paid acquisition to template supply and team plan.
- Message hierarchy: 1) Brand/context → 2) Agenda → 3) Growth → 4) Retention → 5) Revenue → 6) Insight → 7) Lessons → 8) Q3 plan → 9) Decisions to close.
- Primary action meaning: Approve the Q3 budget reallocation and year-plan discount reset.
- Voice and tone: Direct Chinese report speech; judgments named; no filler slogans.
- Terminology rules: MAU, MRR, ARPU, Day-7 激活（写满 3 条笔记）, 付费 D30, 净收入留存 — used consistently.
- State language rules: Nav disabled at ends; counter announces `n / total`; no loading/empty states in this static deck.
- Content risks: Fictional metrics must stay internally consistent and disclosed as fiction; no emoji; no overclaiming beyond the invented dataset.

## OKF Preflight

### Active OKF Concepts

- `design-okf/production/presentation-deck.md`: live-meeting density, What–So What–Now What spine, claim/evidence/action per slide, conclusion titles.
- `design-okf/systems/taste-engine.md`: mineral-paper + teal-ink read; anti-default locks; slide-archetype budget instead of card repetition.
- `design-okf/systems/type-personality.md`: Songti display for brand memory; Heiti/sans for body and data; two-family Google Fonts ceiling with fallbacks.
- `design-okf/systems/motion-language.md`: short slide continuity only; transform/opacity ≤280ms; reduced-motion instant.
- `design-okf/production/data-viz-i18n-legal.md`: chart type from question; direct labels; fiction disclosure; zh-CN locale.
- `design-okf/governance/request-integrity.md`: nine-field Request Anchor; delivery checked against user slide list and interaction constraints.

### Support References

- `references/branch-presentation.md`
- `references/proof-run-html.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/quality-gates.md`
- `references/visual-verification.md` (browser audit unavailable in this worker; structural self-checks recorded)

### Decision Record

- Constraints extracted: 8–10 Chinese slides with cover/agenda/three KPI pages/two insight-lesson pages/plan/close; vanilla single HTML; Google Fonts ≤2; no rasters/emoji; `section.slide` + `data-ud-check`; arrow keys + buttons + counter + hash; print one-slide-per-page; reduced motion; WCAG AA; ≤160KB; gallery-strong cover with fiction footnote.
- Deliberate exceptions: No pinned Playwright rendered audit in this worker environment — structural HTML/JS/validators substitute and Integrator must re-check pixels; motion markers omitted because motion is only slide opacity/translate, not SVG-draw storytelling.
- Verification hooks: `validate_design_contract.py --strict-ultimate --require-frontmatter`; `validate_okf_usage.py`; html.parser parse; extracted JS `node --check`; emoji/size/slide-marker shell checks.

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/production/presentation-deck.md` | What–So What–Now What spine; conclusion titles; live density; every content slide has claim/evidence/action | All 9 `section.slide` titles and bodies | Title-only skim narrates Q2→judgment→Q3; slide count 8–10 |
| `design-okf/systems/taste-engine.md` | Cool mineral paper + teal ink; ban purple gradients, cream/terracotta kits, broadsheet, card grids | CSS tokens, cover field, slide archetypes | Cover distinct at thumbnail; no banned default motifs |
| `design-okf/systems/type-personality.md` | Noto Serif SC brand display + Noto Sans SC body/data; swap + system fallbacks | Font links, `.brand`, titles, chrome | ≤2 families; layout intact if fonts blocked |
| `design-okf/systems/motion-language.md` | Slide change via opacity/translate 280ms; bars width 360ms; reduced-motion disables transitions | `.slide` transitions, `@media (prefers-reduced-motion)` | Durations ≤400ms; reduced-motion CSS present |
| `design-okf/production/data-viz-i18n-legal.md` | Trend/line for MAU; bars for rates; labeled MRR columns; cohort table; fiction footnote | Growth/retention/revenue charts + cover footnote | Every chart has numeric text labels; footnote present |
| `design-okf/governance/request-integrity.md` | Freeze user slide list and interaction constraints in Request Anchor before polish | `## Request Anchor` + delivered `index.html` | Validators + self-checks map 1:1 to requested pages and nav |

## Information Architecture

- Core user tasks: Follow the live narrative; jump via hash; print handout; decide Q3 bets.
- Page or screen inventory: 9 slides — cover, agenda, growth, retention, revenue, insight, lessons, plan, close.
- Navigation model: Left/right keys, on-screen prev/next, hash `#1`…`#9`, counter `n / 9`.
- Content hierarchy: Brand → agenda → three evidence chapters → judgment → plan → decisions.
- Primary CTA rules: Close slide lists three explicit decisions to approve.

## Quality Gates

- Request Anchor fit: Required pages, nav, print, Chinese tone, fiction honesty.
- Content: Self-consistent invented metrics; conclusion titles; no filler.
- Visual: One focal point per slide; archetype variety; cover strong in scaled iframe.
- Accessibility: AA contrast roles; focus-visible; 44px nav targets; chart text alternatives via labels/`aria-label`.
- Responsive: Stage letterboxes; stacks metric/chart columns under ~720px; no page horizontal overflow.
- Interaction: Keyboard and buttons; hash sync; disabled ends.
- Motion: ≤400ms; reduced-motion honored.
- Performance: Single file ≤160KB; fonts only external requests.
- Print: One slide per page; chrome hidden.
- Contract consistency: Both ultimate-design validators pass.

## Assumptions

- Audience is an internal Chinese business review; English labels appear only as product romanization “MoNote” and metric acronyms.
- Projection and laptop screens are the primary scene; print is secondary.
- Google Fonts may be blocked; Songti/PingFang/YaHei/system stacks remain acceptable.
- Integrator will run rendered review; this worker has no browser.

## Open Questions

- Whether a follow-up PPTX/PDF export is needed beyond HTML print.
- Whether team-plan pricing should be added to an appendix slide in a later revision.
- Whether the gallery host wants a lighter cover for mixed dark/light homepage plates.

## Review Log

- 2026-08-12: Bootstrapped contract and 9-slide HTML deck for 墨记 MoNote Q2 review under ultimate-design Build / YOLO / proof-run HTML order. Direction locked to mineral paper + teal ink. Validators and structural self-checks run before handoff; rendered pixel audit deferred to Integrator.
