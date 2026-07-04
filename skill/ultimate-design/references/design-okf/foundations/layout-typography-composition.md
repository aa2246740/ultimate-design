---
type: Design Foundation
title: Layout Typography And Composition
description: Coordinates composition, grid, alignment, spacing rhythm, typography, Chinese typesetting, mixed Chinese-English text, editorial layout, Swiss Style, and medium-specific output checks.
tags: [layout, typography, composition, grid, spacing, cjk, editorial, swiss-style]
---

# Purpose

Use this concept when the design quality depends on how information is arranged on the surface, how text is read, or how space creates rhythm: posters, graphics, decks, reports, long-form pages, dashboards, brand manuals, editorial layouts, and Swiss Style directions.

This concept is the layout coordination layer. Use `gestalt-composition.md` for grouping and reading-path mechanics, `typography-system.md` for type tokens and readability defaults, and `production/graphic-print.md` for print production caveats.

# Core Model

Good layout turns information into a readable visual system:

```text
content structure
-> medium and reading scene
-> composition model
-> grid and type area
-> typography hierarchy
-> spacing rhythm
-> alignment and optical correction
-> language-specific typesetting
-> medium output check
```

Use this leading sentence while designing:

```text
Composition creates visual order; grid creates structural order; typography creates reading order; spacing creates rhythm.
```

# Composition

Before styling, answer:

- What is the primary focus?
- What is the second read?
- Which elements support the message?
- Which elements should recede or be removed?
- What path should the eye follow?

Choose a composition model by task, not habit:

- Center axis: stable, ceremonial, cover-like, short message.
- Rule of thirds: natural balance for image-led layouts.
- Diagonal: movement, conflict, urgency, events.
- Asymmetry: modern tension, Swiss/editorial/brand work.
- Z path: simple advertising, hero, poster, single-screen flow.
- F path: scan-heavy text, lists, articles, admin surfaces.
- Modular collage: multi-image or multi-topic editorial systems.

Completion: focus, visual weight, and path can be named without explaining the decoration.

# Grid And Type Area

Grid is the hidden spatial rule. It should answer where elements sit, how wide text is, how images span, and how multiple pages or screens stay related.

Select the lightest grid that fits the work:

- Single column: long reading, simple reports, essays.
- Two column: main + support, teaching, documentation.
- Multi-column: magazines, newspapers, annual reports, dense editorial.
- 6/12 column: responsive web and product UI.
- Modular grid: posters, data stories, thumbnails, catalogs, dashboards.
- Baseline grid: long text, multi-column editorial, reports, decks with many text blocks.
- Hierarchical grid: landing pages, feature pages, complex one-off compositions.

Define only what the artifact needs:

- Page or viewport size.
- Type area or container.
- Margins and safe area.
- Columns and gutters.
- Rows or modules when useful.
- Baseline or vertical rhythm unit when text alignment matters.
- Breakpoints or crop rules for digital/social formats.

For editorial or print-adjacent work, remember that classic margin ratios are starting points. Binding, trim, spine loss, spread images, paper, and vendor requirements override visual theory.

# Alignment

Alignment creates relationships, not merely neatness.

Pick one dominant alignment logic, then use exceptions deliberately:

- Left aligned: stable, readable, default for most body text, web, UI, and reports.
- Centered: ceremonial, short, cover-like, title-led.
- Right aligned: special use, captions, numbers, marginalia, edge tension.
- Justified: print/editorial only when hyphenation, language, and spacing quality can be controlled.
- Optical alignment: use when geometric alignment looks wrong.

Use optical correction for:

- Round or triangular icons that look off-center.
- Large punctuation, quotes, or display type that visually dents an edge.
- Chinese punctuation that benefits from hanging or compression.
- Mixed Chinese-English baselines, numbers, and units.

Completion: important edges, baselines, captions, image bounds, and controls align to a visible logic.

# Spacing Rhythm

Spacing is layout grammar. Use it to show grouping, separation, breathing room, and reading pace.

Work across levels:

- Micro: letter, word, punctuation, number/unit spacing.
- Inline: line-height and inline rhythm.
- Paragraph: paragraph gap, indentation, heading relation.
- Module: title/body, image/caption, card/list/chart groups.
- Page: margins, type area, major whitespace.
- System: 4/8 point scale, modular scale, or tokenized spacing.

Rules:

- Related content should be closer than unrelated content.
- Headings usually sit closer to the content they introduce than to the previous section.
- Image and caption belong together.
- Page-level gaps should be visibly larger than module-level gaps.
- Avoid undocumented one-off spacing unless the composition intentionally breaks the system.

For digital work, the design must tolerate user text spacing overrides and zoom without losing content or functionality.

# Typography

Typography solves four jobs:

- Legibility: individual characters can be recognized.
- Readability: continuous reading is comfortable.
- Hierarchy: users know what to read first.
- Tone: type carries the correct voice.

Use type hierarchy before decorative styling:

```text
Display -> H1 -> H2 -> H3 -> Body -> Caption -> Footnote
```

Build hierarchy in this order:

1. Size.
2. Weight.
3. Space.
4. Position.
5. Color.
6. Typeface contrast.

Do not make one heading large, bold, saturated, shadowed, and differently typed at the same time. Usually two emphasis levers are enough.

Use defaults as starting points, not laws:

- Chinese body line height often starts around 1.5 to 1.8.
- English body line height often starts around 1.4 to 1.6.
- Chinese long-form measure often starts around 25 to 40 characters.
- English long-form measure often starts around 45 to 75 characters.
- One or two families and two or three weights are usually enough.

Always adjust for x-height, character face size, reading distance, medium, density, and brand tone.

# Chinese And Mixed-Language Typesetting

Do not treat Chinese as translated Western typography.

Chinese checks:

- Choose paragraph system deliberately: traditional first-line indent without large paragraph gaps, or modern paragraph spacing without first-line indent. Avoid mixing both casually.
- Check line-start and line-end punctuation. Closing punctuation, commas, periods, question marks, exclamation marks, right brackets, and right quotes should not begin a line when proper line breaking is required.
- Do not split two-cell marks such as ellipses or em dashes across lines.
- Treat simplified/traditional punctuation rules and vertical writing as project-specific, not interchangeable.
- Keep dense Chinese body text readable through line height, measure, and paragraph rhythm.

Mixed Chinese-English checks:

- Match visual size by x-height, cap height, face size, weight, and paragraph color, not fixed ratios.
- Check baseline and visual center.
- Handle Chinese-Western spacing intentionally. For web/Markdown, a normal space may be acceptable; professional typesetting may use engine-controlled spacing; brand display may require optical adjustment.
- Keep numbers, units, punctuation, and full-width/half-width conventions consistent.
- Verify font coverage and commercial rights.

# Editorial And Multi-Page Systems

For long or multi-page artifacts, design the system before individual pages:

- Format or viewport.
- Type area.
- Margins and safe areas.
- Column structure.
- Baseline or vertical rhythm.
- Running headers/footers, page numbers, section markers.
- Figure, caption, table, footnote, quote, and source rules.
- Dense page, image-led page, section page, and pause page rhythm.

Editorial rhythm should vary density without losing system:

```text
dense text -> image-led spread -> whitespace pause -> mixed text/image -> section marker
```

# Swiss Style

Use Swiss Style as a method, not a costume. Helvetica plus left alignment plus whitespace is not enough.

Swiss-informed work should show:

- Mathematical or visibly disciplined grid.
- Asymmetric composition.
- Clear sans-serif typography or another equally disciplined type choice.
- Flush-left ragged-right text when appropriate.
- Objective photography or imagery used as information, not decoration.
- Strong hierarchy and reduced ornament.
- Universal clarity over personal decoration.

Use it when clarity, neutrality, cultural portability, and systematic layout fit the brief. Avoid it when the brief needs warmth, craft, ceremony, expressive illustration, or emotional abundance.

# Digital And Print Implementation

Digital:

- Use CSS text and layout features intentionally: line-height, text-align, letter-spacing, word-spacing, hyphens, word-break, writing-mode, hanging-punctuation, grid, flex, and responsive container rules.
- Text zoom, 200 percent scaling, and text-spacing overrides must not hide content or controls.
- Truncation needs a way to see full critical content.
- Web fonts need fallback and loading strategy.

Print:

- Confirm trim size, bleed, safe area, image resolution, color profile, font embedding/outlining, PDF/export format, and binding effects before claiming final production readiness.
- Keep small text, captions, legal copy, QR codes, and page numbers legible at final output size.

# Workflow

1. Split content into title, subtitle, lead, body, images, captions, tables, notes, CTA, and metadata.
2. Define reading scene: distance, medium, pace, density, and output format.
3. Choose composition model and focal strategy.
4. Define grid, type area, margins, columns, gutters, and baseline/spacing rhythm.
5. Define type hierarchy and paragraph system.
6. Place content in grayscale or low fidelity first.
7. Tune alignment, optical alignment, spacing, image/caption relationships, and language-specific typesetting.
8. Add color, imagery, and expressive detail only after structure reads.
9. Verify with squint/grayscale tests, rendered screenshots, text zoom/reflow checks, print/export preflight, or human reading tests as practical.

# Contract Fields

Record:

- Reading scene and medium.
- Composition model and focal strategy.
- Grid, type area, margins, columns, gutters, and baseline/spacing rhythm.
- Type hierarchy, families, weights, line heights, and measure.
- Paragraph system.
- Chinese and mixed-language rules.
- Image/caption/table/footnote rules.
- Editorial or multi-page rhythm rules.
- Swiss Style or other method rationale when used.
- Digital text behavior or print/export constraints.

# Done Check

The pass is done when another agent can name the composition, grid, type hierarchy, spacing rhythm, alignment logic, language-specific rules, and output constraints without reverse-engineering the artifact.

If the layout only looks good because of color or decoration, return to grayscale structure and fix composition, grid, typography, or spacing first.

# Source Notes

Research basis includes W3C CLReq for Chinese typesetting and mixed-script spacing, WCAG 2.2 text contrast and text spacing behavior, MDN CSS Text for web text implementation, Bootstrap grid as a common responsive-grid reference, and Swiss Style references including grid, asymmetry, objective imagery, sans-serif typography, and International Typographic Style practice. Treat numeric values as starting points unless the source is an accessibility or production requirement.
