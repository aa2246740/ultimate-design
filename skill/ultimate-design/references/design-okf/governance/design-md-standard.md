---
type: Governance Concept
title: DESIGN.md Standard
description: Google-compatible DESIGN.md structure, token schema, prose sections, references, and extension boundary.
tags: [design-md, design-contract, tokens, schema, google-compatible]
---

# Purpose

Use this concept when creating, updating, auditing, or validating a root `DESIGN.md` for AI-assisted UI generation.

# Status

Treat Google Labs `design.md` as the primary compatibility target for `DESIGN.md` in AI UI work. It is not an ISO, W3C, or IETF standard; it is an open Google Labs format with a community/tooling ecosystem. Use current official sources when exact schema, CLI behavior, or export formats matter.

Primary sources:

- https://github.com/google-labs-code/design.md
- https://raw.githubusercontent.com/google-labs-code/design.md/master/docs/spec.md
- https://www.npmjs.com/package/@google/design.md

# File Shape

A Google-compatible `DESIGN.md` has two layers:

1. YAML front matter for machine-readable design tokens.
2. Markdown body for human and agent-readable rationale, guidance, usage rules, and examples.

Use this rule when priorities conflict: front matter token values are normative; prose explains how and when to apply them.

# Core Front Matter

Use official core keys first:

- `version`: optional; current format value is commonly `alpha`.
- `name`: design system name.
- `description`: optional, but strongly recommended for an agent-readable style anchor.
- `colors`: color tokens.
- `typography`: type tokens.
- `rounded`: radius tokens. Use `rounded`, not `radius` or `borderRadius`.
- `spacing`: spacing tokens.
- `components`: component token mappings.

Use semantic token names, not scale-only names such as `blue1`, `gray2`, `bigFont`, or `newButtonColor`.

# Token Types

Color values may be valid CSS colors. Prefer `#RRGGBB` when tool compatibility matters.

Typography tokens commonly use:

- `fontFamily`.
- `fontSize`.
- `fontWeight`.
- `lineHeight`.
- `letterSpacing`.
- `fontFeature`.
- `fontVariation`.

Dimensions should use `px`, `em`, or `rem` unless the official toolchain in the project accepts more.

# Token References

Use official token reference syntax:

```yaml
backgroundColor: "{colors.primary}"
typography: "{typography.label-md}"
rounded: "{rounded.md}"
padding: "{spacing.md}"
```

Do not use `$colors.primary`, `$radius.md`, `radius`, or `border-radius` as the canonical `DESIGN.md` syntax.

# Component Mapping

Prefer official component properties:

- `backgroundColor`.
- `textColor`.
- `typography`.
- `rounded`.
- `padding`.
- `size`.
- `height`.
- `width`.

Represent component states with named component keys when needed, for example `button-primary-hover`, `button-primary-disabled`, `input-focus`, or `input-error`.

# Markdown Body Order

When standard sections appear, keep them in this order:

1. `## Overview`.
2. `## Colors`.
3. `## Typography`.
4. `## Layout`.
5. `## Elevation & Depth`.
6. `## Shapes`.
7. `## Components`.
8. `## Do's and Don'ts`.

Some specs or tools accept aliases such as `Brand & Style`, `Layout & Spacing`, or `Elevation`. Prefer the canonical headings when creating new files.

# Extension Boundary

Unknown keys and sections may be useful for a project, but do not describe them as official core schema. Mark them as team extensions or move them into companion files.

Recommended extension placement:

- Put visual token values in official front matter.
- Put usage rationale in official Markdown sections.
- Put content model, IA, quality gates, assumptions, open questions, review log, and agent execution rules after the official sections, or in `design-system/AGENT-RULES.md`, `TOKENS.md`, `COMPONENTS.md`, or `AGENTS.md` when the file would become too heavy.
- If an official linter flags extensions, keep the Google-compatible `DESIGN.md` lean and move extended governance to companion files.

# Common Errors

- Using `radius` or `borderRadius` as official fields instead of `rounded`.
- Using `$colors.primary` instead of `{colors.primary}`.
- Writing only tokens without prose.
- Writing vague descriptors such as "modern, clean, premium" without concrete style anchors.
- Omitting component states.
- Omitting Do/Don't rules.
- Copying third-party brand marks or distinctive identity without permission.
- Skipping lint or diff when changing the contract.

# Done Check

The `DESIGN.md` standard pass is done when the file has a Google-compatible token layer, official body sections in order where present, clear extension boundaries, no broken token references, and an explicit path for validation.
