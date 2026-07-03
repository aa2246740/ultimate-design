---
type: Governance Concept
title: Machine Verification And CI
description: DESIGN.md schema checks, token validation, and automated quality gates.
tags: [ci, validation, schema, qa, automation]
---

# Purpose

Use this concept when the user wants industrial-grade governance, reusable design systems, or machine-checkable design rules.

# Contract Shape Checks

For a root `DESIGN.md`, prefer Google-compatible shape checks before project extensions.

Check whether YAML front matter, when present, uses official core keys:

- `version`.
- `name`.
- `description`.
- `colors`.
- `typography`.
- `rounded`.
- `spacing`.
- `components`.

Flag official-schema mistakes:

- `radius` or `borderRadius` used instead of `rounded`.
- `$colors.primary` style references instead of `{colors.primary}`.
- Component properties such as `background` or `color` where `backgroundColor` or `textColor` is intended.
- Token names that describe scale only, such as `blue1`, `gray2`, `bigFont`, or `newButtonColor`.
- Broken token references.

Check whether standard Markdown sections, when present, follow this order:

1. Overview.
2. Colors.
3. Typography.
4. Layout.
5. Elevation & Depth.
6. Shapes.
7. Components.
8. Do's and Don'ts.

For the broader ultimate-design contract, check whether `DESIGN.md` or the equivalent contract includes:

- Metadata.
- Product and users.
- Design intent.
- Content model.
- Information architecture.
- Visual system.
- Tokens.
- Components.
- Page or asset specs.
- Accessibility requirements.
- Quality gates.
- Assumptions.
- Open questions.
- Review log.

# Token Checks

Check whether token definitions include relevant families:

- Color.
- Typography.
- Spacing.
- Rounded.
- Border.
- Shadow.
- Motion.
- Z-index.
- Breakpoints.

Treat border, shadow, motion, z-index, and breakpoints as project extensions unless the current official DESIGN.md spec says otherwise. Mark extensions clearly.

# DESIGN.md Tooling

Use official tooling when it is available and current enough for the project:

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md diff DESIGN.md DESIGN-v2.md
npx @google/design.md export --format css-tailwind DESIGN.md > theme.css
```

Use the bundled fallback validator when official tooling is unavailable, network access is inappropriate, or you need a deterministic local structural check:

```bash
python3 /path/to/ultimate-design/scripts/validate_design_contract.py DESIGN.md
```

# Automated Gates

Use what the project has:

- Typecheck, lint, and unit tests.
- DESIGN.md lint or fallback structural validation.
- Accessibility checks such as axe or equivalent.
- Lighthouse or Core Web Vitals checks when available.
- Playwright or browser interaction checks.
- Visual regression such as Chromatic, Percy, or screenshot diff.
- Stylelint/ESLint checks for hard-coded tokens when configured.

# Boundary

Automated checks are evidence, not taste. A clean automated run does not prove the design is strong; it only removes certain classes of defects.

# Done Check

This pass is done when available automated checks have run, or missing checks are named as not run with a reason.
