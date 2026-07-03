---
type: Production Concept
title: Data Visualization I18n Legal
description: Data visualization, localization, RTL, legal, licensing, and asset-rights checks.
tags: [data-viz, i18n, legal, licensing, charts]
---

# Purpose

Use this concept when the design includes charts, metrics, tables, international users, regulated content, brand assets, generated assets, fonts, icons, or real people/places/products.

# Data Visualization

- Match chart type to data relationship: trend, comparison, distribution, part-to-whole, correlation, hierarchy, flow, or geography.
- Do not use pie/donut charts for many categories.
- Do not rely on color alone; use labels, patterns, symbols, or direct annotation.
- Include legends, axis labels, units, and tooltips where useful.
- Use accessible contrast for chart marks and labels.
- Provide a table or text summary for screen readers when charts carry key information.
- Avoid misleading scales, truncated axes without disclosure, decorative 3D, or gradients that obscure values.
- For dense data, aggregate, sample, or provide drill-down instead of rendering everything.

# Localization And I18n

- Record locale assumptions in the contract.
- Handle text expansion and longer translated labels.
- Define date, time, currency, number, unit, and pluralization behavior.
- Check mixed Chinese/English typography when relevant.
- Record RTL support as supported, unsupported, or not applicable.
- Avoid putting critical text into uneditable images unless localization is out of scope.

# Legal And Asset Rights

Verify or flag rights for:

- Fonts.
- Images.
- Icons.
- Logos.
- Brand assets.
- Likenesses.
- Generated imagery.
- Third-party screenshots.
- Claims, testimonials, statistics, or regulated content.

If rights are unclear, use placeholders or clearly mark the item as needing user confirmation.

# Done Check

This pass is done when chart integrity, localization assumptions, and rights risks are either verified or recorded as open questions.
