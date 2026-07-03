---
type: Design System Concept
title: Typography System
description: Type scale, line length, mixed Chinese/English checks, tabular figures, and readability defaults.
tags: [typography, readability, mixed-language, data]
---

# Purpose

Use this concept when selecting fonts, defining type tokens, improving readability, or designing dense content.

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

# Contract Fields

Record:

- Font families.
- Type scale.
- Line heights.
- Weights.
- Line-length guidance.
- Data/table number treatment.
- Localization and mixed-language notes.

# Done Check

The typography pass is done when hierarchy, readability, mixed-language behavior, and overflow handling are explicit.
