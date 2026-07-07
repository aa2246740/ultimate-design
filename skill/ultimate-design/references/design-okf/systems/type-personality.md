---
type: Design System Concept
title: Type Personality And Typography Art Direction
description: Operational font-selection model for deciding when type should recede or become memorable, with CJK/Latin voice maps, mixed-script checks, numeric/punctuation rules, WebFont performance, fallback, and licensing caveats.
tags: [typography, type-personality, art-direction, cjk, mixed-language, webfont, licensing]
---

# Purpose

Use this concept when selecting or changing font families, making type a brand or campaign memory feature, tuning display typography, handling consequential Chinese/English mixed typography, building a type-led deck/social/poster/marketing page, or auditing font licensing, WebFont performance, fallback, or cross-device portability.

This concept owns typography art direction. Use `typography-system.md` for type scale, line length, line height, token fields, and readability defaults. Use `layout-typography-composition.md` for composition, grid, type area, spacing rhythm, and language-specific layout mechanics.

# Principle

Font choice is not "pretty versus ugly." It is a decision about:

```text
task -> voice -> medium -> technical constraints -> real-content proof
```

When users need to complete a task, type should usually recede. When users need to form an impression, type can stand forward.

Do not treat type associations as universal psychological laws. Font meaning comes from history, form, category convention, culture, medium, and actual use. Test with the target audience and real content when the stakes are high.

# Core Model

```text
task mode
-> tone words
-> type role
-> script strategy
-> family class
-> hierarchy and pairing
-> numerals/punctuation
-> licensing/performance/fallback
-> rendered proof
-> contract record
```

# Task Mode

Conservative type lowers cognitive cost. Use it when the artifact is high-frequency, high-density, high-risk, long-reading, task-oriented, or cross-platform:

- Product UI, dashboards, forms, tables, admin tools, help docs, API docs.
- Finance, legal, medical, government, compliance, pricing, or operational surfaces.
- Long-form reading, dense reports, body copy, chart labels, buttons, and state text.

Expressive type creates memory. Use it when the artifact is low-frequency, low-density, high-reach, identity-led, campaign-led, or short-message:

- Logo or wordmark, hero display, key visual, poster, packaging, social cover, book/magazine cover.
- Campaign pages, event pages, brand launches, pitch covers, editorial feature openers.

Useful rule:

```text
high frequency / high density / high risk -> conservative
low frequency / low density / high reach -> expressive
```

Mature systems often use quiet type for 90 percent of text and reserve 10 percent for memory.

# Type Roles

Assign roles before choosing names:

| Role | Job | Typical posture |
|---|---|---|
| Utility type | Buttons, labels, forms, nav, UI states | clear, stable, unremarkable |
| Content type | Paragraphs, articles, reports, documentation | durable, comfortable, calm |
| Brand type | Hero, logo-adjacent display, campaign titles | memorable, ownable, controlled |
| Data type | Numbers, tables, metrics, IDs, prices | aligned, precise, tabular |
| Emotional type | Quotes, social hooks, posters, editorial accents | sparse, high-impact |

Do not make every role expressive. If every text style speaks loudly, nothing is memorable.

# CJK Voice Map

Use these as art-direction hypotheses, not hard laws:

| Chinese class | Common voice | Fits | Be careful with |
|---|---|---|---|
| Heiti / sans | modern, neutral, rational, efficient, technical | UI, web, decks, dashboards, enterprise, apps | large display may feel generic without another memory feature |
| Songti / serif | literary, editorial, authoritative, classical, refined | long-form, reports, culture, publishing, academia, legal, premium headings | small mobile UI, dense dashboards, pure tech surfaces |
| Fangsong | formal, official, archival, document-like | notices, rules, archival references, historical citations | commercial brand display, product UI, youth consumer brands |
| Kaiti | humanist, educational, traditional, warm | poetry, invitations, cultural scenes, short quotes, title accents | UI body, data, tables, large continuous reading |
| Rounded | friendly, soft, young, approachable | children, food, beauty, lifestyle, onboarding, light tips | finance, legal, medical, government, serious B2B |
| Handwritten | personal, emotional, handmade, human | posters, cafe/food, craft, invitations, social accents | body copy, UI, tables, legal/financial/medical content |
| Monospace | technical, coded, exact, machine-like | code, API, logs, IDs, timestamps, technical brand accents | long Chinese body text, warm consumer brands |

# Latin Voice Map

Use class labels as communication tools; modern families often mix traits.

| Latin class | Common voice | Fits | Be careful with |
|---|---|---|---|
| Grotesk | industrial, urban, early-modern, editorial, slightly raw | posters, culture, editorial, retro-modern brands | tiny UI or highly neutral systems |
| Neo-grotesk | neutral, corporate, international, rational, reliable | enterprise, SaaS, finance, product UI, B2B | can become too safe and forgettable |
| Humanist sans | warm, open, readable, service-oriented | education, health, public services, content products | may lack edge, luxury, or strong impact |
| Geometric sans | constructed, modern, future-facing, designed | logos, display, tech consumer, fashion-tech, minimal campaigns | small text, long-form, data-heavy UI |
| Serif | classic, literary, authoritative, formal, premium | publishing, media, academia, law, luxury, editorial display | small UI, dashboards, projected deck body |
| Slab serif | sturdy, industrial, confident, retro-advertising | posters, sports, tools, food, bars, outdoor | refined UI, long body text, delicate scenes |
| Mono | code, terminal, precise, systematic | code, IDs, parameters, logs, dashboards accents | ordinary body copy or emotional prose |

# Mixed Chinese-English Strategy

Start with the dominant script and content surface. In Chinese-first artifacts, choose the Chinese posture first because Chinese characters occupy more visual area. Then match or contrast the Latin family deliberately.

Choose **harmony** for UI, body copy, docs, decks, dashboards, and long reading:

- Heiti + neo-grotesk or humanist sans.
- Songti + serif.
- Rounded Chinese + rounded sans or friendly humanist.
- CJK mono or technical CJK sans + Latin mono for code-adjacent material.

Choose **contrast** for posters, key visuals, covers, packaging, editorial openers, or brand display:

- quiet Chinese with expressive Latin.
- Songti with geometric display.
- Heiti with Didone-like high contrast.
- handwritten Chinese with restrained grotesk.

Contrast is high-risk. Limit it to display, slogans, covers, or short emphasis unless the whole system is designed around it.

# Optical Pairing Checks

Do not align by numeric settings alone. Align by optical behavior:

- Chinese face size and inner counter.
- Latin x-height, cap height, ascenders, and descenders.
- Stroke weight and paragraph color.
- Width and rhythm.
- Apertures and clarity at small size.
- Roundness or squareness.
- Visual center and baseline.
- Numeral style and punctuation.

Test with real strings, not specimen text:

```text
字体 Typography 2026 数据增长 38.5%
AI Agent / Coding Agent / DESIGN.md
¥12,800.00 + 24h SLA
```

If English appears too light, adjust weight. If English appears too large or dense, adjust size, tracking, or family. Do not assume `Regular = Regular` across scripts.

# Numerals And Punctuation

Use tabular figures for tables, dashboards, prices, percentages, counters, IDs, time, and financial comparisons:

```css
font-variant-numeric: tabular-nums;
```

Use proportional numerals for ordinary prose unless alignment matters.

Punctuation follows the dominant language and context:

- Chinese sentence with short English phrase: usually Chinese punctuation.
- Complete English sentence: English punctuation.
- URL, code, command, API, file path: half-width technical punctuation.
- Technical writing may use more half-width punctuation, but consistency matters more than ideology.

Chinese-English spacing is contextual. Use normal spaces where prose readability benefits; omit or tighten when UI space is tight, brand names require official spelling, or typesetting engines handle spacing.

# Medium Presets

| Medium | Goal | Type strategy |
|---|---|---|
| Product UI | operation, clarity, trust | system or durable sans; type recedes; clear hierarchy; zoom and fallback proof |
| Dashboard | comparison, anomaly detection | neutral sans; tabular figures; mono for IDs/code/timestamps; restrained weight |
| Marketing site | trust plus memory | readable body and UI; expressive hero or brand display when useful; performance budget |
| Presentation deck | distance readability and story | strong titles allowed; body must be legible; avoid fragile thin strokes and complex display body |
| Poster / key visual | attention and memory | display type may be the main image; supporting text remains clear |
| Social cover | feed recognition and fast scanning | title can be bold, rounded, handwritten, or highly contrasted; body stays clear |
| Long-form | sustained reading | type recedes; measure, line-height, paragraph rhythm, contrast, and rendering quality matter more than category labels |
| Brand system | durable recognition | define type roles, do/do-not rules, fallback, licensing, and cross-medium examples |

# WebFont, Fallback, And Licensing

Font choices must survive production:

- Confirm font source and license before claiming publication readiness.
- Distinguish desktop, WebFont, app embedding, server generation, eBook/PDF, logo/trademark, and client-transfer rights.
- Do not copy or redistribute font files unless the license permits it.
- Prefer WOFF2 for web fonts.
- Load only required families, weights, styles, and scripts.
- Use CJK WebFonts carefully; full CJK families are often too heavy for ordinary pages.
- Prefer system body text plus a subset brand/display font when that preserves performance and identity.
- Use `font-display` and sensible fallback stacks.
- Test with WebFonts disabled.

Do not rely on memory for volatile licensing or platform rules. Check current official font vendor, platform, or legal sources when rights matter.

Example fallback patterns:

```css
font-family:
  "Brand Sans",
  -apple-system, BlinkMacSystemFont,
  "Segoe UI", Roboto, "Helvetica Neue",
  "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei",
  "Noto Sans CJK SC", "Source Han Sans SC",
  sans-serif;
```

```css
font-family:
  "Brand Serif",
  "Songti SC",
  "Noto Serif CJK SC",
  "Source Han Serif SC",
  serif;
```

```css
font-family:
  "JetBrains Mono",
  "SF Mono", Menlo, Consolas,
  "Noto Sans Mono CJK SC",
  monospace;
```

# Workflow

1. Name the user task: read, scan, compare, trust, decide, act, remember, or feel.
2. Write tone words before font names.
3. Assign type roles: utility, content, brand, data, emotional.
4. Choose dominant script strategy and family classes.
5. Pair Chinese and Latin by optical behavior, not fixed numeric ratios.
6. Test real content: headings, body, brand/product names, all-caps English, numbers, prices, percentages, punctuation, tables, dark mode, mobile, and fallback.
7. Check accessibility, zoom, wrapping, overflow, font coverage, file size, and rights.
8. Record the type system in the contract.

# Contract Fields

For durable work, record:

- Type role map: utility, content, brand, data, emotional.
- Type personality: quiet, neutral, editorial, technical, warm, premium, playful, official, archival, handmade, or another concrete voice.
- Family classes and actual families used.
- Chinese/Latin pairing rationale.
- Display/body/data/label hierarchy.
- Numeral treatment.
- Punctuation and mixed-language rules.
- Fallback stack.
- WebFont loading and performance assumptions.
- Font licensing status and unresolved risks.
- Intentional exceptions.

# Done Check

This concept is applied when another agent can answer:

1. Should type recede or stand forward for this artifact, and why?
2. Which type roles exist and which one, if any, carries memory?
3. Which Chinese and Latin family classes fit the tone, medium, and task?
4. How are mixed-script size, weight, baseline, punctuation, and numerals handled?
5. What happens if the preferred font fails to load or cannot be licensed?
6. Where are the type decisions recorded for future agents?

# Source Notes

Research basis includes the user's Type Personality / Typography Art Direction packet, Apple Human Interface Guidelines typography guidance, Noto font documentation, W3C CSS Fonts Level 4, W3C CLReq, MDN `font-variant-numeric`, WCAG 2.2 contrast and resize-text guidance, web.dev font best practices, Adobe Fonts licensing guidance, and common type-design practice. Treat font associations as contextual art-direction heuristics, not universal psychological facts.
