---
version: alpha
name: TaskFlow Dashboard
description: Light, calm system-UI mock of TaskFlow's main project board — sidebar, metrics, kanban, and activity feed for a fictional project management product.
colors:
  primary: "#0B6E6A"
  secondary: "#3A4556"
  tertiary: "#B86A2D"
  neutral: "#E6E9EF"
  surface: "#F5F6F8"
  on-surface: "#1A2030"
  error: "#C0392B"
typography:
  headline-lg:
    fontFamily: "system-ui, -apple-system, Segoe UI, Helvetica Neue, sans-serif"
    fontSize: 16px
    fontWeight: 650
    lineHeight: 1.2
  body-md:
    fontFamily: "system-ui, -apple-system, Segoe UI, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
  label-md:
    fontFamily: "system-ui, -apple-system, Segoe UI, Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
rounded:
  none: 0px
  sm: 6px
  md: 10px
  lg: 14px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
components:
  primary-button:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
---

# Design System

## Overview

TaskFlow is a fictional project-management product. This deliverable is a static high-fidelity mock of the main dashboard: left navigation, sprint summary metrics, a four-column kanban (Backlog / In progress / Review / Done), and a right-hand activity feed. The visual direction is a **quiet daylight work surface** — cool fog fields, slate ink, one restrained sea-teal accent — so the board reads as a real system UI at gallery thumbnail scale without looking like a SaaS marketing template.

## Colors

- Scene: cool indoor daylight desk tool, not a marketing hero and not a dark cockpit.
- Posture: restrained — neutrals dominate; primary teal (`#0B6E6A`) stays under ~10% of the surface for nav current, CTA, and In-progress signal.
- `surface` `#F5F6F8` is the page field; raised panels and cards use white with soft hairlines (`#D5DAE3` / `#E8EBF1`).
- `on-surface` `#1A2030` for primary text; muted `#5A6478` for secondary labels (both ≥ 4.5:1 on surface/white).
- Semantic: success `#1F7A4D`, warn/tertiary `#B86A2D`, error `#C0392B`, info `#2F5F8A` — always paired with label or icon, never color-alone.
- Anti-defaults: no purple/indigo gradients, no warm cream + terracotta brochure look, no neon glow, no broadsheet rules.

## Typography

Utility-first system stack only (no webfont): `system-ui, -apple-system, Segoe UI, Helvetica Neue, sans-serif`. Screen title sits at 16px semibold; task titles 13.5px semibold; body/UI 13–14px; labels/metrics captions 11–12px. Tabular figures on counts, metrics, and due dates. Letter-spacing stays near 0; slight negative tracking only on denser titles. Type must survive user zoom without clipping controls.

## Layout

Desktop (1024+): fixed sidebar (~232px) + main column; main splits into board pane and activity feed (~292px). Top bar holds location, search, and primary CTA. Summary metrics sit above the board. Board columns share equal width with a 1000px min track so mid widths scroll **inside** `.board-scroll`, never the page. At ≤1024px the sidebar becomes an off-canvas drawer; activity stacks under the board; board remains horizontally scrollable in its container. At ≤640px metrics go 2×2; search hides behind the denser top bar.

## Elevation & Depth

Nearly flat. Cards and metrics use a 1px soft border plus `0 1px 2px` shadow; hover lifts to a slightly deeper soft shadow and 1px translateY. No stacked glows, glassmorphism, or fake 3D. Column wells are tinted neutrals, not nested cards.

## Shapes

`sm` (6px) on controls and chips; `md` (10px) on cards, columns, and metrics; `full` only on count pills and filter chips. Avatars are circles for recognition, not decoration. Corners stay calm and product-like — no oversized radii.

## Components

Sidebar (brand, nav with counts, project switcher, account chip), top bar (menu toggle, crumb, search, notifications, filter, New task), summary metric tiles, board/list segmented control, filter chips, kanban columns with counts and add affordance, task cards (tags, title, id, assignees, due), empty Review column with next-step CTA, activity feed rows, status footer. Primary button consumes `{colors.primary}` / `{typography.label-md}` / `{rounded.sm}`.

## Do's and Don'ts

- Do keep density calm: hairlines and spacing group content before extra boxes.
- Do show reachable product states: hover, selected filters, overdue/soon due, badges, empty Review with a next step.
- Do keep page overflow vertical-only down to 320px; board scroll stays local.
- Do use initials avatars and inline SVG icons only.
- Don't use emoji, raster images, or external assets beyond an optional system font stack.
- Don't nest cards in cards or turn the summary row into a marketing stat strip.
- Don't rely on color alone for status, priority, or overdue meaning.
- Don't add motion longer than 400ms or animate properties other than transform/opacity.

## Request Anchor

- Original user request: Design the main dashboard screen for TaskFlow with sidebar navigation, project board (Backlog / In progress / Review / Done), activity feed, and summary metrics; light calm system-UI feel; production-quality states; English; static high-fidelity product mock.
- Latest user override: Deliver only `/workspace/docs/demos/taskflow/index.html` and `DESIGN.md`; self-contained vanilla HTML; Google Fonts optional (system UI preferred here); no raster/emoji; gallery thumbnail readable; both validators must pass.
- Deliverable: Static TaskFlow dashboard mock plus its design contract under `docs/demos/taskflow/`.
- Primary audience: Product designers and engineers judging Ultimate Design demos; secondary, PMs scanning a believable board.
- Core job to be done: Instantly read project status and task flow on a calm production-like board, including one empty column state.
- Success criteria: Zones present and marked; realistic copy; AA contrast; keyboard/focus; responsive board scroll without page overflow; file ≤160KB; validators pass.
- Non-goals: Real backend, drag-and-drop persistence, auth, dark theme, marketing landing, multi-page app.
- Must preserve: Fictional TaskFlow identity; English copy; light calm system UI; required layout regions; demo footer line; `data-ud-check` markers.
- Validation must check against: Request Anchor fit, OKF bindings, contrast/focus/targets, reduced motion, 320–1440 overflow behavior, file size, both Python validators.

## Content Model

- User intent: See where Atlas Launch work stands and what moved recently.
- Business intent: Prove the skill can ship a dense product UI that still feels calm and real.
- Message hierarchy: 1) Where am I (Atlas Launch / Sprint 24). 2) Health (metrics). 3) Work (columns/cards). 4) Recent changes (activity).
- Primary action meaning: New task creates work on the active board (visual only).
- Voice and tone: Plain product English; specific task titles; no hype.
- Terminology: Board, Backlog, In progress, Review, Done, task, sprint; avoid "tickets" or "tickets queue".
- State language: Empty Review explains absence and offers "Pull from In progress"; overdue/soon dues use label + color; selected nav/filters use `aria-current` / `aria-pressed`.
- Content risks: Placeholder lorem, emoji, fake stock photos, vague "Manage" CTAs.

## OKF Preflight

### Active OKF Concepts

- `design-okf/foundations/information-architecture.md`: board is the primary task surface; sidebar orients; metrics and feed are secondary.
- `design-okf/content/state-language.md`: empty Review column plus hover/selected/overdue/badge states are designed, not decorative.
- `design-okf/content/ux-writing.md`: realistic task titles, verb CTAs, empty-state next step.
- `design-okf/systems/color-system.md`: restrained teal-on-fog palette with semantic status roles and AA pairs.
- `design-okf/systems/typography-system.md`: system-ui utility scale with tabular counts and zoom-safe UI type.
- `design-okf/systems/taste-engine.md`: quiet product taste; lock out purple SaaS, cream/terracotta, and card-stack slop.
- `design-okf/digital/accessibility-usability.md`: semantic controls, focus-visible, 44px targets, AA contrast, reduced motion.
- `design-okf/digital/responsive-interaction.md`: local board horizontal scroll; no page-level overflow to 320px.
- `design-okf/governance/request-integrity.md`: nine-field Request Anchor guards multi-constraint delivery.

### Support References

- `references/branch-web-product.md`
- `references/proof-run-html.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/visual-verification.md`
- `references/quality-gates.md`
- `SKILL.md` Operating Loop (Build route, YOLO)

### Decision Record

- Constraints extracted: single self-contained HTML; system fonts (no webfont); no raster/emoji; light calm system UI; sidebar + metrics + 4-column board + activity; empty Review state; footer attribution; `data-ud-check` zones; WCAG AA; focus-visible; 44px+ targets; board-local scroll; ≤160KB; English fictional copy.
- Deliberate exceptions: Interactions are visual-only (pressed filters, sidebar drawer) without persistence; Review empty state is intentional while other columns are populated; metrics use compact tiles that look like tool chrome, not marketing cards.
- Verification hooks:
  - `validate_design_contract.py --strict-ultimate --require-frontmatter`
  - `validate_okf_usage.py`
  - `html.parser` parse; `node --check` on extracted JS
  - file size ≤160KB; no emoji scan
  - manual responsive reasoning at 1440/1280/1024/768/375/320 for page overflow vs board scroll

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/foundations/information-architecture.md` | Primary path is the Sprint 24 board; sidebar for orientation; metrics summarize; activity is secondary | `data-ud-check="sidebar|topbar|summary-row|board|activity-feed"` | First view answers where/what/next; hierarchy readable at ~1280 thumbnail |
| `design-okf/content/state-language.md` | Review column ships a real empty state with next step; overdue/soon/high use text + color | `data-ud-check="empty-column"`, due labels, tags | Empty copy names state + next action; status not color-only |
| `design-okf/content/ux-writing.md` | Specific task titles and verb CTAs (`New task`, `Pull from In progress`); consistent Board terminology | Task cards, buttons, activity rows | No lorem/emoji; terms match Content Model |
| `design-okf/systems/color-system.md` | Fog surface + sea-teal primary; semantic success/warn/error; anti purple/cream defaults | CSS variables, status pips, CTA | Contrast ≥4.5:1 text; accent area stays restrained |
| `design-okf/systems/typography-system.md` | System-ui stack; 16px screen title; tabular nums on metrics/counts/dates | Type CSS, metric values, column counts | No webfont request; counts align; zoom does not clip controls |
| `design-okf/systems/taste-engine.md` | Quiet daylight product read; layout family = app chrome + kanban; memory = teal pip + empty Review | Global theme, board composition | No gradient glow, no card-in-card, no marketing hero |
| `design-okf/digital/accessibility-usability.md` | Buttons/landmarks, focus-visible ring, ≥40–44px controls, Escape closes drawer | Interactive controls, `:focus-visible`, menu toggle | Keyboard walkthrough; reduced-motion kills transforms |
| `design-okf/digital/responsive-interaction.md` | ≤1024 drawer + stacked feed; board scrolls inside `.board-scroll`; page never overflows X | `.board-scroll`, media queries | 320–1440: page `overflow-x` hidden; board min-width scrolls locally |
| `design-okf/governance/request-integrity.md` | Nine-field Request Anchor frozen before polish | `## Request Anchor` | Delivery checklist matches original dashboard ask |

## Information Architecture

- Core user tasks: Orient in Atlas Launch, scan sprint health, triage cards by column, skim recent activity, start a new task.
- Page or screen inventory: Single dashboard screen mock.
- Navigation model: Persistent sidebar (Overview / Board / Timeline / Reports + projects); mobile off-canvas with scrim.
- Content hierarchy: Topbar location → summary metrics → kanban → activity; footer attribution.
- Primary CTA rules: One primary `New task`; column add and empty CTA are secondary.
- Required states: Nav current, project pressed, filter pressed, task hover/focus, overdue/soon due, empty Review, sidebar open/closed, reduced motion.

## Quality Gates

- Request Anchor fit: All required regions present with calm light system UI and production-like states.
- OKF evidence: Active concepts bound; validators pass.
- Content: Realistic English; empty state actionable; terminology consistent.
- Visual: Dense-but-calm thumbnail read; no purple/cream/glow defaults.
- Accessibility: AA contrast, focus-visible, keyboard, targets, reduced motion.
- Responsive: Full layout 1440/1280/1024; board-local scroll or stack below; no page X-overflow to 320.
- Performance: Single HTML ≤160KB; no raster; no external requests.
- Contract consistency: This file matches `index.html` tokens and zones.

## Assumptions

- Gallery iframe renders near 1280px wide with roughly the top 800px visible — summary + column headers + first cards must read immediately.
- System fonts on Linux/macOS/Windows are acceptable substitutes for each other.
- Visual-only interactions satisfy the static mock brief; no persistence required.
- Browser rendered audit may be unavailable in this worker environment; structural self-checks substitute and Integrator re-checks visually.

## Open Questions

- Whether a later TaskFlow multi-screen system should lock these tokens or allow a darker ops theme.
- Whether drag-and-drop should become a verified motion contract in a follow-up.

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| alpha | 2026-08-12 | Bootstrapped TaskFlow dashboard artifact and contract (Build / YOLO / proof-run HTML) | Demo gallery worker request for product UI case | Design worker agent |
