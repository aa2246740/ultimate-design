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
- Use optical sizing when the selected variable font supports it, then verify the rendered result rather than assuming the axis improves every size.
- Treat tracking and leading as size- and script-dependent. Keep letter spacing at `0` by default; record a typographic reason for nonzero tracking and test it with real text at the delivery size.
- Let larger display sizes use tighter leading when glyphs remain clear; let body and small text use enough leading for sustained reading and script-specific marks.
- Respect browser/user text scaling. Layout, spacing, controls, and containers must survive larger text instead of holding typography inside fixed pixel boxes.

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
- Optical-sizing, tracking/leading, and user text-scaling decisions when they materially affect the artifact.

# Done Check

The typography pass is done when hierarchy, readability, mixed-language behavior, overflow handling, and any type-personality or font-delivery decisions are explicit.

# Source Notes

Optical sizing, variable-font behavior, size-specific tracking/leading, system fonts, and scalable layout are informed by Apple's official *The details of UI typography* guidance and general web typography practice. Apple platform defaults are examples; browser rendering, CJK behavior, brand rules, and real-content proof remain authoritative for the artifact.
