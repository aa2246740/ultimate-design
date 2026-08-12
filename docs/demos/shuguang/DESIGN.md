---
version: alpha
name: 拾光书房 2026 年度阅读报告
description: Fictional Chinese reading-app annual report as a one-page data story — giant hook number, one conclusion per screen, hand-drawn SVG/CSS charts, warm stone paper with high-saturation data colors.
colors:
  primary: "#C0392B"
  secondary: "#1F6F5B"
  tertiary: "#B8751A"
  neutral: "#8A847A"
  surface: "#EFEBE3"
  on-surface: "#221E1A"
  error: "#A12828"
typography:
  headline-lg:
    fontFamily: "Noto Serif SC, Songti SC, STSong, SimSun, Georgia, serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.02
  body-md:
    fontFamily: "Noto Sans SC, PingFang SC, Microsoft YaHei, Helvetica Neue, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.7
  label-md:
    fontFamily: "Noto Sans SC, PingFang SC, Microsoft YaHei, Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  primary-button:
    backgroundColor: "{colors.primary}"
    textColor: "#FBF7F2"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
---

# Design System

## Overview

「拾光书房」2026 年度阅读报告是一页中文数据故事站：用巨号阅读时长开场，随后每屏只讲一个结论，图表全部 SVG/CSS 手绘（横向条形、环形、52×7 夜读热力、Top 5 书单），结尾为「生成我的报告」视觉 CTA 与分享语。全部数据虚构但自洽，页脚诚实标注演示性质。

Design Maturity: Candidate — direction implemented and validator-gated; not owner-locked.

Visual memory: 石纸灯下的巨号朱红「186」+ 书房书脊色标（墨绿 / 朱红 / 灯琥珀）。

## Colors

- Scene sentence: 冬夜台灯下翻开纸质年报——浅石纸底、近墨正文、高饱和数据色只用来标结论。
- Color posture: Restrained field + committed data accents — surface dominates; primary/secondary/tertiary carry charts and the hero number.
- `--color-surface` `#EFEBE3` stone paper (cooler than AI-default cream `#F4F1EA`).
- `--color-on-surface` `#221E1A` ink body (≥4.5:1 on surface).
- `--color-muted` `#5C564E` annotations; `--color-neutral` `#8A847A` footnotes.
- `--color-primary` `#C0392B` hero hours + evening ring slice + deep heat cells (large text / graphics; labels stay dark).
- `--color-secondary` `#1F6F5B` category bars, CTA secondary, mid heat.
- `--color-tertiary` `#B8751A` morning slice / lamp accent.
- Extra chart hues `#3A6B8C` / `#6B5B7A` only for bar/ring differentiation with adjacent text labels (never color-only).
- Anti-template locks: no purple/indigo SaaS gradients; no cream+terracotta editorial default; no broadsheet hairline-dense columns; no neon glow.

## Typography

- Display / conclusions: **Noto Serif SC** (Songti voice) — memory feature for brand, hero numeral unit, section conclusions.
- Body / chart labels / UI: **Noto Sans SC** — clear data labels and Chinese UI chrome.
- Google Fonts: two families, `display=swap`, preconnect; system Songti / PingFang / YaHei / Arial fallbacks required.
- Hero numeral is tabular display scale (clamp to ~168px); conclusions larger than footnotes and legends.
- Chinese measure ~25–40 characters for notes where practical.

## Layout

- Sticky minimal header: brand + year chip (not a dashboard nav).
- Section order (locked by request): hero giant number → duration/days → category bars → time donut → night heatmap → Top 5 → closing CTA.
- One composition per viewport: brand + one hook number + one lead + one CTA in the first screen; no stats strip in the hero.
- Each later section: kicker → conclusion (largest text in section) → 1–2 notes → chart/list → small honest footnote.
- Heatmap scrolls horizontally inside its own container on narrow viewports; page itself must not overflow 320–1440.
- `data-ud-check` on inner padded content zones only: `hero-number`, `duration`, `categories`, `time-ring`, `heatmap`, `top-books`, `closing` (≥36px real gap between marked regions).

## Elevation & Depth

- Flat paper field with soft radial lamp washes (opacity ≤11%). Hairline rules separate sections.
- No card chrome for charts or ranks; type, rules, and ink bars carry structure.
- Buttons are the only filled interactive surfaces.

## Shapes

- Controls use `sm`–`md` radii (4–8px). Heat cells `rx=2`. Avoid pill clusters and rounded-full marketing chips.
- Bars and donut are rectangular/circular SVG/CSS geometry — hand-drawn marks, not chart-library skins.

## Components

- Primary button: primary fill, light ink `#FBF7F2`, min-height 48px, verb+object（生成我的报告）.
- Ghost button: hairline border for 复制分享语.
- Secondary hero CTA: secondary teal fill（查看完整故事）.
- Stat trio, labeled bar rows, donut + legend list, heatmap SVG, rank list rows, share blockquote.

## Do's and Don'ts

- Do keep 「拾光书房」 as a hero-level brand signal above the hook number.
- Do make each section’s conclusion larger than legends and footnotes.
- Do label every chart mark with real Chinese text and numeric values.
- Do force-reveal charts within ~700ms so values never wait forever on scroll; honor `prefers-reduced-motion` and print.
- Do keep the fictional-data disclaimer in footnotes and the required footer line.
- Do not clone any third-party year-in-review visual signature (Spotify Wrapped neon stacks, WeChat report stickers, etc.) — adopt mechanisms only.
- Do not use raster images, emoji, or color-only encoding.
- Do not put secondary marketing clutter in the first viewport.

## Request Anchor

- Original user request: 为虚构阅读 App「拾光书房」设计 2026 年度阅读报告页：数据故事式一页站。中文。所有数据虚构但要自洽，页脚注明数据为虚构演示。机制：巨号数字开场；每屏一个结论；SVG/CSS 条形/环形/热力/Top5；浅暖底 + 2–3 高饱和数据色；诚实脚注；结尾 CTA + 分享语。
- Latest user override: Deliver exactly `docs/demos/shuguang/index.html` and `DESIGN.md`; vanilla self-contained HTML; Google Fonts ≤2; no raster/emoji; wave-1 hard constraints (zones, motion fallback, 44px targets, AA, ≤160KB, gallery thumbnail).
- Deliverable: Single-file annual report page plus this design contract under `docs/demos/shuguang/`.
- Primary audience: Showcase gallery viewers and product designers evaluating a Chinese data-story annual report pattern; secondary fictional app readers receiving a yearly summary.
- Core job to be done: Feel the year’s reading in one scroll — notice the hook number, understand four charted conclusions, leave with a shareable line.
- Success criteria: Section order matches the brief; charts have labels+values; AA contrast; keyboard/focus; reduced-motion/static charts; validators pass; thumbnail reads the giant number; footer attribution exact.
- Non-goals: Real user data, login, backend report generation, dark mode toggle, English locale, chart libraries, multi-page archive.
- Must preserve: Fictional honesty; Chinese-only copy; mechanism set from reference study (no signature clone); self-contained static HTML; required footer sentence.
- Validation must check against: Strict DESIGN.md contract; OKF usage bindings; rendered UI audit 0 fail/0 warn; HTML parse; JS syntax; no emoji; file ≤160KB.

## Content Model

- User intent: Relive the year of reading and optionally share a quiet summary line.
- Business intent (demo): Prove a warm, credible annual-report storytelling pattern for a reading app.
- Message hierarchy: 1) Brand + total hours 2) Duration/days 3) Category preference 4) Time-of-day mix 5) Night heat 6) Top books 7) CTA + share.
- First-screen answers: What — 拾光书房 2026 报告; Hook — 186 小时; Next — 查看完整故事.
- Primary action meaning: 生成我的报告 is visual/demo (scrolls home); 复制分享语 copies the quote.
- Voice and tone: 有温度、不煽情；像安静的年终信，不用鸡汤口号。
- Terminology: 阅读时长、有阅读日、类目、夜读、年度书单；avoid 燃爆/刷屏/沉浸式狂欢.
- State language: Share button reports 已复制 or 无法自动复制.
- Trust / risk: Every chart footnote names the measurement rule; global footer states fiction.
- Content risks: Invented books must stay clearly fictional; do not imply real user telemetry.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: stone-paper lamp-read annual report; anti-defaults on cream+terracotta, purple glow, card dashboards.
- `design-okf/systems/type-personality.md`: Songti conclusions + Sans data labels; two Google families with CJK fallbacks.
- `design-okf/systems/color-system.md`: role-first stone/ink + three data hues; AA for text; color never sole encoding.
- `design-okf/production/data-viz-i18n-legal.md`: chart-type match, labeled marks, zh-CN locale, fictional rights disclaimer.
- `design-okf/foundations/visual-communication-hierarchy.md`: one conclusion per screen; conclusion > legend; hero number dominates thumbnail.
- `design-okf/systems/motion-language.md`: short scroll reveals; static-first; reduced motion full static.
- `design-okf/systems/motion-contract.md`: IntersectionObserver reveals + 700ms force-reveal + print/beforeprint; no forever-hidden chart values.
- `design-okf/digital/accessibility-usability.md`: AA, focus-visible, ≥44px targets, skip link, keyboard share control.
- `design-okf/content/message-model.md`: locked section order and first-screen brand+hook+next.

### Support References

- `references/branch-marketing-site.md`
- `references/reference-study.md` (mechanism extraction from excellent annual-report / year-in-review pages; no signature cloning)
- `references/proof-run-html.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/visual-verification.md`
- `references/quality-gates.md`

### Decision Record

- Constraints extracted: One-page Chinese data story; coherent fictional metrics; giant opening number; one conclusion per screen; SVG/CSS bars, donut, 52×7 heatmap, Top 5; warm stone paper + 2–3 saturated data colors; honest footnotes; closing CTA + share line; `data-ud-check` zones named in brief; motion fallbacks; AA; 320–1440 no page overflow; ≤160KB; exact footer string.
- Deliberate exceptions: Heatmap may scroll horizontally inside its container (page does not); donut uses four slices (≤4 categories, labeled); share CTA is front-end demo only.
- Verification hooks:
  - `validate_design_contract.py --strict-ultimate --require-frontmatter`
  - `validate_okf_usage.py`
  - `validate_html_visual.mjs` → status pass, 0 fails, 0 warnings
  - `html.parser` parse; `node --check` extracted JS; emoji scan; file size ≤160KB

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Stone-paper lamp annual-report read; ban cream+terracotta, purple glow, card grids | Global CSS, hero, sections | Thumbnail identity; anti-default critique |
| `design-okf/systems/type-personality.md` | Noto Serif SC for brand/conclusions; Noto Sans SC for body/data | Font links, `.conclusion`, labels | Fonts-blocked fallbacks; ≤2 families |
| `design-okf/systems/color-system.md` | Surface `#EFEBE3`, ink `#221E1A`, data `#C0392B`/`#1F6F5B`/`#B8751A` with dark labels | `:root` tokens, charts | Body ≥4.5:1; chart labels not color-only |
| `design-okf/production/data-viz-i18n-legal.md` | Bars for comparison, donut for part-to-whole (4 slices), heatmap for calendar intensity; zh-CN; fiction disclaimer | `#categories`, `#time-ring`, `#heatmap`, footnotes, footer | Labels+values present; locale `zh-CN`; footer line |
| `design-okf/foundations/visual-communication-hierarchy.md` | One conclusion per section; conclusion type larger than legends; hero number thumbnail-first | Section headings, hero numeral | Visual audit hierarchy; gallery crop read |
| `design-okf/systems/motion-language.md` | Reveal via opacity/transform ≤360ms; static works first | `.reveal` | Reduced-motion disables animation |
| `design-okf/systems/motion-contract.md` | IO reveals + 700ms force-reveal + beforeprint/print force | Reveal script | Charts visible without waiting on scroll |
| `design-okf/digital/accessibility-usability.md` | Skip link, focus-visible, 44px controls, labeled SVG | Header, CTAs, heatmap scrollport | Keyboard walkthrough; target sizes |
| `design-okf/content/message-model.md` | Order hero→duration→categories→ring→heat→top→closing | Section IDs and copy | IA matches Request Anchor |

## Reference Study

- Source mode: Mechanism extraction from excellent data annual-report / year-in-review archetypes (user-supplied mechanism list); provenance **Unknown / public reference for own brand** — diagnosis applied under Build, not a clone brief.
- Primary mechanisms adopted: giant hook metric; one conclusion per viewport with conclusion > legend; hand-marked charts with direct labels; warm paper + few saturated data colors; small honest footnotes; closing generate/share beat.
- Signature exclusions: Do not copy Spotify Wrapped neon gradients/stickers, any product’s mascot language, WeChat-style badge clutter, or another brand’s exact palette/type pairing.
- Evidence confidence: Mechanisms listed as **Observed** in the user brief; exact third-party pixels **Unknown** (intentionally not fetched for cloning).

## Information Architecture

- Core user tasks: Scan the year hook, understand four charted findings, note Top 5, share a line.
- Page inventory: One scrolling report (`index.html`).
- Navigation model: Brand home anchor; in-page CTA to `#duration`; no multi-level IA.
- Content hierarchy: Hero → Duration → Categories → Time ring → Heatmap → Top books → Closing → Footer.
- Primary CTA rules: Hero 查看完整故事 → `#duration`; Closing 生成我的报告 → `#top` (demo); 复制分享语 → clipboard status.

## Quality Gates

- Request Anchor fit: All seven content beats + fictional disclaimer present.
- Content: Warm non-sentimental Chinese; coherent fictional metrics.
- Visual: Giant number thumbnail-legible; no card-grid report; anti-default locks hold.
- Data viz: Every chart has text labels and values; heatmap contained scroll.
- Accessibility: AA text roles; focus-visible; ≥44px targets; reduced motion static.
- Responsive: 320–1440 no page-level horizontal overflow.
- Motion: transform/opacity ≤400ms; 700ms force-reveal; print reveal.
- Performance: ≤160KB; Google Fonts only external dependency; no rasters.
- Contract: Strict validators + rendered audit pass.

## Assumptions

- Gallery iframe renders ~1280px wide and crops roughly the top ~800px; hero brand + 186 must read immediately.
- Google Fonts may be blocked; Songti/PingFang/YaHei stacks keep hierarchy.
- “生成我的报告” is intentionally non-functional beyond returning to the hero (visual CTA).
- Heatmap intensities are seeded deterministic fiction aligned with “December deeper nights” narrative.

## Open Questions

- Whether a production app would export PNG/PDF of the report (out of scope).
- Whether real privacy copy would need a linked methodology page beyond footnotes.

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| alpha | 2026-08-12 | Bootstrapped 拾光书房 annual report page and contract (Build/YOLO proof-run) | Worker deliverable for showcase gallery data-report slot | Design worker agent |
