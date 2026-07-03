---
type: Design System Concept
title: Tokens And Components
description: Token layers, component specs, state matrices, and design-to-code governance.
tags: [tokens, components, design-system, governance]
---

# Purpose

Use this concept when creating or changing reusable design systems, themes, component libraries, or implementation rules.

# Token Layers

- Primitive tokens hold raw values.
- Semantic tokens name roles.
- Component tokens map semantic roles to component parts.

Components should consume semantic or component tokens, not raw primitive values.

# Token Families

Define only what the project needs:

- Color.
- Typography.
- Spacing.
- Radius.
- Border.
- Shadow or elevation.
- Opacity.
- Motion.
- Z-index.
- Breakpoints.
- Layout.

# Stable Names

Prefer semantic or role-based names over appearance names:

- Good: `color.text.primary`, `color.background.surface`, `color.action.primary`.
- Bad: `blue1`, `gray2`, `bigFont`, `newButtonColor`, `random13px`.

Raw primitives may use appearance names when they are only values, but component code should consume semantic or component tokens.

# Component Spec

Each reusable component should define:

- Purpose.
- Anatomy.
- Variants.
- Sizes.
- States.
- Behavior.
- Content rules.
- Accessibility.
- Responsive rules.
- Token mapping.
- Do and do-not.
- Deprecation and migration notes when relevant.

# Interaction States

For interactive components, consider:

- Default.
- Hover when pointer devices apply.
- Focus.
- Active or pressed.
- Disabled.
- Loading when async action applies.
- Error or invalid when validation applies.

# Citations

[1] Design Tokens Community Group format draft: https://www.designtokens.org/tr/drafts/format/
[2] Style Dictionary token documentation: https://styledictionary.com/info/tokens/
