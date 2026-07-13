# Design Contract

The design contract is the single source of truth for project design decisions. Prefer `DESIGN.md` at the project root. For UI and web design work, make root `DESIGN.md` Google-compatible whenever practical: YAML front matter carries machine-readable design tokens, and the Markdown body carries rationale, usage guidance, and agent-readable constraints. If the project already has an equivalent file, use it and do not create a duplicate. For a one-off graphic, quick critique, or small polish pass, a compact assumptions/review note may be enough; do not create a heavyweight design-system tree unless future reuse needs it.

A missing contract is expected in many projects. Create a professional first draft yourself from the user prompt, repository context, existing copy, screenshots, visual assets, technology stack, and safe defaults. Do not ask the user to provide a `DESIGN.md`.

## Compatibility Target

When the file is named `DESIGN.md`, treat Google Labs `design.md` as the primary compatibility target:

- Use official front matter keys first: `version`, `name`, `description`, `colors`, `typography`, `rounded`, `spacing`, and `components`.
- Use `rounded`, not `radius` or `borderRadius`, for the official radius scale.
- Use token references such as `{colors.primary}`, not `$colors.primary`.
- Keep official Markdown sections in order when present: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.
- Treat request anchor, content model, IA, quality gates, assumptions, open questions, review log, motion, shadow, breakpoints, z-index, and agent rules as team extensions unless the current official spec says otherwise.
- Put extensions after the official sections, or move them to `design-system/AGENT-RULES.md`, `TOKENS.md`, `COMPONENTS.md`, `AGENTS.md`, or equivalent companion files if `DESIGN.md` would become too heavy or official tooling flags them.

Read `design-okf/governance/design-md-standard.md` and `design-okf/governance/design-md-agent-governance.md` when creating, auditing, or validating a root `DESIGN.md`.

## When To Create Or Update

Create or update the contract when:

- There is no existing design source of truth.
- You introduce or change visual language, tokens, components, layout systems, page structure, interaction states, or accessibility targets.
- You introduce or change content model, terminology, CTA rules, state language, content hierarchy, or high-risk copy.
- You make assumptions that future work must inherit.
- You discover open questions that are not blockers.

Do not turn the contract into an essay. Keep decisions, tokens, rules, and open questions. Move long theory or component catalogs into `design-system/` files when needed.

Create `design-system/AGENT-RULES.md`, `TOKENS.md`, `COMPONENTS.md`, or similar files only when the project has reusable tokens/components, multiple screens, a brand system, or multiple future agents who need shared rules.

## Bootstrap From Zero

When creating `DESIGN.md` from scratch:

- Infer project type, platform, audience, and primary task from the prompt and codebase.
- Inspect existing UI, CSS, theme files, copy, assets, and route structure before inventing a direction.
- If brand assets exist, preserve them and derive the system around them.
- If no brand exists, create a provisional art direction with clear assumptions.
- Write a Google-compatible YAML front matter token layer when the artifact is a web or UI design system.
- Typography `fontSize` tokens use a single `px`, `rem`, or `em` value. Do not put `clamp()`, `vw`, `vh`, or viewport-scaled type in the YAML token layer; responsive type decisions belong in page/component specs and must not make text scale directly with viewport width.
- Write official Markdown sections before ultimate-design extension sections.
- Fill every section with useful first-pass decisions, not placeholders, where evidence supports it.
- Create a Request Anchor before detailed styling so the original user need stays visible through critique, verification, and final delivery.
- Build a content model before visual direction: user intent, message hierarchy, primary action meaning, voice/tone, terminology, and state-language rules.
- Record OKF Preflight before visual direction, then bind every active OKF concept to a decision, artifact target, and verification hook. A reference that changes no decision is not active knowledge.
- Put uncertain but non-blocking decisions under `Assumptions`.
- Put unresolved decisions that should change future work under `Open Questions`.
- Add a review-log entry explaining that the contract was bootstrapped.

## Google-Compatible Lean Template

Use this template when creating a new `DESIGN.md`:

```md
---
version: alpha
name:
description:

colors:
  primary:
  secondary:
  tertiary:
  neutral:
  surface:
  on-surface:
  error:

typography:
  headline-lg:
    fontFamily:
    fontSize:
    fontWeight:
    lineHeight:
  body-md:
    fontFamily:
    fontSize:
    fontWeight:
    lineHeight:
  label-md:
    fontFamily:
    fontSize:
    fontWeight:
    lineHeight:

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
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
---

# Design System

## Overview

Write a concrete style anchor, not only adjectives. State the product, audience, emotional tone, density, and what the UI must avoid.

## Colors

Explain each color token's role and constraints. Do not introduce new hex colors without updating the token layer.

## Typography

Explain type roles, hierarchy, readability constraints, type personality, data-number treatment, mixed-language behavior, fallback stack, WebFont assumptions, and font-rights status when relevant.

## Layout

Define spacing rhythm, grid/container behavior, density, responsive rules, and table/media strategies.

## Elevation & Depth

Define borders, tonal layering, shadows if used, and when not to add depth.

## Shapes

Explain how `rounded` values map to controls, cards, pills, avatars, and overlays.

## Components

For each component, define purpose, anatomy, variants, sizes, states, behavior, content rules, accessibility, responsive behavior, token mapping, do, and do not.

## Do's and Don'ts

List concrete, enforceable rules and forbidden patterns.

## Agent Execution Rules

- Read this file before generating or modifying UI.
- Use defined colors, typography, rounded, spacing, and components first.
- Do not invent persistent visual tokens without updating this file.
- Return a short self-check for meaningful UI changes.

## Request Anchor

- Original user request:
- Latest user override:
- Deliverable:
- Primary audience:
- Core job to be done:
- Success criteria:
- Non-goals:
- Must preserve:
- Validation must check against:

## Content Model

- User intent:
- Message hierarchy:
- First-screen answers:
- Primary action meaning:
- Voice and tone:
- Terminology rules:
- State language rules:
- Trust, risk, and help content:
- Content risks:

## OKF Preflight

Record this before choosing visual direction or making a new artifact:

### Active OKF Concepts

- List only task-facing `design-okf/` concepts that change a concrete decision.

### Support References

- List branch, workflow, index, governance, contract, and verification files read for execution or traceability. These are not active OKF unless promoted into the section above.

### Decision Record

- Constraints extracted:
- Deliberate exceptions:
- Verification hooks:

## OKF Decision Bindings

Add one row for every active `design-okf/` concept. Branch and verification references may remain in Preflight without a row.

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/...` | Concrete choice changed by this concept | Page, component, slide, asset, token, copy, or interaction | Rendered check, contract check, test, or review evidence |

## Information Architecture

- Core user tasks:
- Page or screen inventory:
- Navigation model:
- Content hierarchy:
- Primary CTA rules:

## Taste Signature

Use only when the artifact has meaningful visible style freedom:
- Design read:
- Necessary judgment:
- Taste dials:
- Category defaults avoided:
- Layout families or slide archetypes:
- Visual memory feature:
- Type personality:
- Asset/reference policy:
- Anti-default locks:
- Intentional exceptions:

## Motion Strategy

Use only when meaningful motion, page transitions, animated decks, scroll storytelling, or interactive state choreography are part of the work:
- Motion purpose:
- Motion budget:
- Primary motion focus:
- Do-not-move zones:
- Trigger model:
- Duration and easing rules:
- Direction and causality rules:
- Scroll behavior:
- Reduced-motion fallback:
- Performance risks:

## Motion Contract

Use when animation is a requested feature or final delivery claim, especially SVG line/border drawing, scroll-linked motion, GSAP/ScrollTrigger behavior, timeline sequencing, or no-flash reveal choreography:
- Motion ids and target selectors:
- User-facing promise:
- Implementation route:
- Trigger model and trigger range:
- Display-window:
- Timing band:
- Duration and easing tokens:
- End trigger selector:
- Progress mapping:
- Visual subject selector:
- Focus-complete boundary:
- Exit-complete guard:
- Acceptance samples and tolerance:
- Initial state:
- Reverse behavior:
- No-flash rule:
- Reduced-motion expected state:
- Validation command and report path:

## Motion Audit Summary

Use only for project-level, multi-route, or multi-component motion audits:
- Audit scope and exclusions:
- Stack, libraries, and existing motion tokens:
- Representative routes, components, and interactions:
- Frequency evidence and assumptions:
- Runtime baseline evidence:
- Static inventory report path:
- Evidence Gate status counts and blockers:
- Confirmed findings and selected repairs:
- Additive opportunities kept separate:
- Performance evidence:
- Reduced-motion evidence:
- Post-fix replay evidence:
- Detailed report or plan paths:
- Remaining risks:

## Page Or Asset Specs

For each page, screen, or graphic:
- Goal:
- Primary user task:
- Primary content:
- Primary CTA:
- Components or visual modules:
- Required states:
- Responsive notes:
- Accessibility notes:
- Analytics or success signal:

## Presentation Or Deck Specs

Use only when relevant:
- Deck mode:
- Audience:
- Decision or action request:
- One-sentence deck conclusion:
- Narrative spine:
- Slide inventory:
- Title-story rule:
- Slide claim/evidence/action rule:
- Density rule:
- Master/template rules:
- Data/chart source rules:
- Notes or script needs:
- Export package:
- Accessibility checks:
- Approval and compliance checks:

## Graphic Or Print Specs

Use only when relevant:
- Size:
- Color mode:
- Bleed:
- Safe area:
- Resolution:
- Paper or output material:
- Finish:
- Export format:
- Font handling:
- Image/font/logo license notes:

## Brand Identity And Media Production Specs

Use only when relevant:
- Brand strategy and recognition anchors:
- Core identity rules:
- Application rules:
- Production rules:
- Logo variants and misuse rules:
- Cross-media mapping:
- Asset naming and delivery package:
- Licensing and rights register:
- Approval, owner, versioning, and governance:
- Official platform, vendor, legal, or supplier checks:

## Data Visualization, I18n, And Legal

Use only when relevant:
- Chart palette:
- Chart accessibility:
- Axis, legend, tooltip, and unit rules:
- Data-density rules:
- Misleading-chart prohibitions:
- Locale:
- RTL support:
- Text expansion:
- Date/time format:
- Currency and number format:
- Font/image/icon/logo license notes:
- Brand asset permission:

## Quality Gates

- Request Anchor fit:
- Visual:
- Accessibility:
- Responsive:
- Interaction:
- Motion:
- Motion contract:
- Performance:
- Print or export:
- Data visualization:
- I18n/legal:
- Contract consistency:

## Implementation And Governance

- CSS architecture:
- Token implementation:
- Component naming:
- State naming:
- Theme strategy:
- Dark mode:
- Framework notes:
- Performance budget:
- Storybook or component docs:
- Visual regression:
- Rendered UI Audit:
- Accessibility testing:
- CI checks:

## Assumptions

- 

## Open Questions

- 

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| 0.1 |  | Initial draft |  |  |
```

## Contract Hygiene

- Record assumptions separately from facts.
- Version meaningful design changes.
- Add decisions rather than rewriting stable sections without reason.
- If a token is deprecated, provide a migration path.
- If a component rule changes, list affected pages/components.
- If a quality gate cannot be run, record why.
