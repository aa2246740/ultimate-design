---
type: Design System Concept
title: Typography System
description: Type scale, line length, mixed Chinese/English checks, tabular figures, and readability defaults.
tags: [typography, readability, mixed-language, data]
---

# Purpose

Use this concept when selecting fonts, defining type tokens, improving readability, or designing dense content.

This concept owns readable type mechanics: scale, line length, line height, weights, mixed-language behavior, and overflow. Use `type-personality.md` when the work depends on font voice, display typography, CJK/Latin family selection, type as a memory feature, WebFont strategy, fallback, or font licensing.

# Defaults

Defaults are starting points, not law:

- Web body text usually starts at 16 px or equivalent.
- English long-form line length usually works around 45 to 75 characters.
- Chinese long-form line length usually works around 25 to 40 characters.
- Body line-height often falls between 1.45 and 1.8.
- Heading line-height often falls between 1.1 and 1.3.
- One or two type families are usually enough.
- Use tabular figures for data, prices, counters, and tables.

# Rules

- Body text prioritizes readability.
- Heading and body scales need clear proportional contrast.
- Avoid similar-but-not-identical font pairings.
- Do not use all-caps body copy.
- Long URLs, product names, and legal text need overflow handling.
- Check mixed Chinese/English baseline, weight, punctuation, numbers, units, and spacing.
- Do not choose font families by taste labels alone. Route font voice, fallback, and licensing decisions to `type-personality.md`.

# Contract Fields

Record:

- Font families.
- Type roles and personality when they affect the visible direction.
- Type scale.
- Line heights.
- Weights.
- Line-length guidance.
- Data/table number treatment.
- Localization and mixed-language notes.
- Link to type-personality decisions when font voice, fallback, WebFont loading, or rights affect delivery.

# Done Check

The typography pass is done when hierarchy, readability, mixed-language behavior, overflow handling, and any type-personality or font-delivery decisions are explicit.
