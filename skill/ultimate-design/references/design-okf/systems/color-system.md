---
type: Design System Concept
title: Color System
description: Role-first color decisions, semantic colors, contrast, dark mode, and cultural caveats.
tags: [color, tokens, accessibility, dark-mode]
---

# Purpose

Use this concept when creating or changing palette, color tokens, states, themes, charts, or brand expression.

# Core Terms

Know the basic vocabulary before choosing a palette:

- Hue: the color family.
- Lightness: perceived brightness.
- Saturation/chroma: perceived color intensity.
- Temperature: warm/cool tendency in context.
- Complementary: colors across the wheel.
- Analogous: neighboring hues.
- Split complementary: one base hue plus two near-complements.
- 60-30-10: a simple dominance/support/accent proportion, useful as a starting point, not a law.

# Role Before Value

Define color roles before choosing values:

- Brand.
- Background.
- Surface.
- Text.
- Border.
- Action.
- Success.
- Warning.
- Error.
- Info.

# Expression Before Palette

Before choosing values, write a concrete scene sentence: who sees this, where, under what light, with what urgency, mood, or material world. Choose a color posture:

- Restrained: neutrals plus one accent under 10 percent of the surface.
- Committed: one saturated color carries 30 to 60 percent of the surface.
- Full palette: three or four deliberate roles.
- Drenched: the surface itself is the color.

Then run an anti-template check. Do not default to generic SaaS blue, AI purple, B2B green-gray, or white-card dashboard colors unless the brief, brand, or use scene justifies it.

# Rules

- Brand color is not a paint bucket.
- Color cannot be the only carrier of meaning.
- Semantic colors must remain stable across the product.
- Dark mode is not inverted light mode.
- Cultural color meanings vary; avoid mechanical color psychology.
- Use accessible foreground/background pairs.
- When creating new web palettes, prefer perceptual reasoning such as OKLCH where the stack supports it.

# Contrast Targets

Use WCAG 2.2 AA as the digital default unless the user specifies otherwise:

- Normal text: at least 4.5:1.
- Large text: at least 3:1.
- UI components and meaningful non-text graphics: at least 3:1.

# Contract Fields

Record:

- Color strategy.
- Color posture and scene sentence.
- Anti-reference or category-default risks.
- Brand colors.
- Neutral colors.
- Semantic colors.
- Light/dark mode behavior.
- Contrast notes and assumptions.

# Citations

[1] WCAG 2.2 Quick Reference: https://www.w3.org/WAI/WCAG22/quickref/
