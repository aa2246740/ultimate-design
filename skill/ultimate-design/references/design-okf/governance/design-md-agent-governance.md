---
type: Governance Concept
title: DESIGN.md Agent Governance
description: How coding agents should create, read, apply, extend, validate, and update DESIGN.md.
tags: [design-md, agents, governance, self-check, ci]
---

# Purpose

Use this concept when a coding agent must create a `DESIGN.md`, consume one before UI generation, update a visual system, or write project-level agent rules for design consistency.

# Creation Flow

Use the lightest complete flow:

1. Determine the scope: whole product, web app, marketing site, dashboard, mobile, print-adjacent assets, dark mode, or component library.
2. Collect evidence: brand assets, screenshots, existing CSS variables, Tailwind/theme config, components, fonts, typical screens, target users, accessibility target, and product constraints.
3. Write the Google-compatible front matter first: `version`, `name`, `description`, `colors`, `typography`, `rounded`, `spacing`, and `components`.
4. Write official Markdown sections in order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.
5. Add only necessary team extensions: agent rules, content model, IA, quality gates, assumptions, open questions, and review log.
6. Validate token references, section order, component state coverage, and extension boundaries.
7. Update code or component docs only after the design contract reflects the intended visual change.

# Agent Usage Rules

When generating or modifying UI:

- Read the root `DESIGN.md` before changing visual, layout, typography, component, or content-state behavior.
- Use defined `colors`, `typography`, `rounded`, and `spacing` tokens before inventing values.
- Reuse defined `components` before creating a new pattern.
- Do not introduce raw hex colors, new font families, arbitrary spacing, arbitrary radii, unapproved gradients, or repeated decorative patterns unless the contract is updated first.
- If a user asks for a visual change that conflicts with `DESIGN.md`, decide whether it is a one-off override or a contract change. For persistent changes, update `DESIGN.md` first.
- Implement relevant hover, focus, active, disabled, loading, empty, error, success, and long-text states.
- Preserve semantic HTML, keyboard access, focus visibility, and contrast.
- Return a short self-check when the design task is complete.

# Agent Self-Check

Before delivery, check:

- All colors come from `colors.*` or are recorded as a contract update.
- Typography comes from `typography.*` or is recorded as a contract update.
- Spacing comes from `spacing.*` or is recorded as a contract update.
- Radius values come from `rounded.*`.
- Components reuse `components.*` where possible.
- Interactive elements have visible focus states.
- Important states are covered: hover, focus, disabled, loading, error, empty, success, and long text when relevant.
- Text/background contrast is acceptable.
- No forbidden visual pattern was introduced.
- `DESIGN.md` and any companion design-system files were updated when persistent rules changed.

# AGENTS.md Integration

When a project uses `AGENTS.md`, add a compact rule block:

```md
## UI Generation Rules

- Always read `DESIGN.md` before generating or modifying UI.
- Do not introduce visual tokens not defined in `DESIGN.md`.
- If a needed token or component is missing, ask whether to update `DESIGN.md` or make a local one-off.
- Run the available `DESIGN.md` validation after changing the file.
```

# Separation Of Concerns

- `README.md`: what the project is and how to run it.
- `AGENTS.md`: how coding agents should work in the repository.
- `DESIGN.md`: what the UI should look and feel like, including design tokens and visual rationale.
- PRD or `SPEC.md`: what the product or feature should do.
- ADR: why a major technical or architectural decision was made.

Keep `DESIGN.md` focused on visual identity, tokens, component rules, content-state rules, and design rationale. Do not turn it into a product requirements document or backend architecture document.

# Tooling

Use official tooling when available:

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md diff DESIGN.md DESIGN-v2.md
npx @google/design.md export --format css-tailwind DESIGN.md > theme.css
```

If official tooling is not installed or network access is inappropriate, run the bundled `scripts/validate_design_contract.py` as a local structural fallback.

# Caveats

- Official linting can catch structure, references, section order, and some contrast issues; it does not prove full accessibility.
- Keyboard navigation, semantic HTML, ARIA behavior, screen reader experience, and reduced motion still require implementation checks.
- Community DESIGN.md samples are not brand licenses. Do not copy logos, marks, or distinctive brand identity without permission.
- The format is still evolving. Pin tool versions in CI when reproducibility matters.

# Done Check

The agent governance pass is done when the project tells agents to read `DESIGN.md`, token changes are traceable to the contract, visual changes are validated, and self-check evidence is recorded.
