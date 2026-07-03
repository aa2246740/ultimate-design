---
type: Governance Concept
title: Design To Code Governance
description: Token-to-code, Storybook, visual regression, accessibility testing, and CI governance.
tags: [design-to-code, storybook, ci, tokens, visual-regression]
---

# Purpose

Use this concept when converting design decisions into code, creating tokens, updating components, or setting up design-system governance.

# Flow

Use the lightest flow the project needs:

1. Design contract.
2. Token definitions.
3. CSS variables, Tailwind theme, Style Dictionary output, or framework theme.
4. Component implementation.
5. Component examples or Storybook when the project uses it.
6. Accessibility and interaction tests.
7. Visual regression when available.
8. Contract changelog.

# Governance Rules

- New tokens need a named purpose.
- Modified tokens need impact notes.
- Deprecated tokens need a migration path.
- Component variants need state examples.
- Shared components should be reused before creating one-offs.
- Hard-coded visual values are acceptable only when no token system exists and the value is documented as provisional.
- Major visual changes should update `DESIGN.md` and, when present, `design-system/TOKENS.md` or `design-system/COMPONENTS.md`.

# Storybook And Examples

When a project uses Storybook or equivalent component docs, update examples for:

- Default.
- Hover/focus/active.
- Disabled.
- Loading.
- Error/invalid.
- Empty or no-data.
- Long text and localization.

# Done Check

The design-to-code pass is done when implementation values can be traced back to the contract or documented project conventions.
