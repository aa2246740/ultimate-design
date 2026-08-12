---
version: alpha
name: 街巷创刊号
description: Fictional independent urban-observation zine inaugural issue page — newsprint masthead, TOC, three multi-column article excerpts, subscribe bar, copyright footer.
colors:
  primary: "#1A4B7C"
  secondary: "#2A2A28"
  tertiary: "#6B6B66"
  neutral: "#C8C6BE"
  surface: "#E8E6DF"
  on-surface: "#161616"
  error: "#8B2E2E"
typography:
  headline-lg:
    fontFamily: "Noto Serif SC, Songti SC, STSong, SimSun, serif"
    fontSize: 96px
    fontWeight: 700
    lineHeight: 0.92
  body-md:
    fontFamily: "Noto Serif SC, Songti SC, STSong, SimSun, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.75
  label-md:
    fontFamily: "Noto Serif SC, Songti SC, STSong, SimSun, serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
rounded:
  none: 0px
  sm: 2px
  md: 4px
  lg: 8px
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
    textColor: "#F4F3EE"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
---

# Design System

## Overview

「街巷」是虚构独立城市观察刊物的创刊号网页：报头、本期目录、三篇多栏报纸排版摘录、邮件订阅栏与报纸版权页脚。视觉读法是新闻纸编辑风——超大宋体刊名作最强资产，细规则线分栏，首字下沉与跨栏抽排引文，黑白为主加一枚专色蓝（`#1A4B7C`）服务栏目编号与强调。气质具体、有街巷画面，不做营销腔。

Design Maturity: Candidate — one coherent newsprint direction implemented and validated against the Request Anchor; not owner-locked.

## Colors

- Scene sentence: 傍晚在旧报刊亭的灯下翻开一份独立小刊，纸面微灰偏冷，油墨近黑，栏目号用一滴专色蓝点亮。
- Color posture: Restrained — newsprint field + ink text; spot blue under ~10% for column numbers, links, and subscribe CTA.
- `--color-surface` `#E8E6DF`: cool newsprint (not warm cream `#F4F1EA`).
- `--color-on-surface` `#161616`: body and display ink.
- `--color-primary` `#1A4B7C`: spot blue for 01/02/03, links, CTA.
- `--color-secondary` `#2A2A28`: strong secondary ink (bylines, issue line).
- `--color-tertiary` / muted `#6B6B66` / `#5C5C58`: captions and quieter meta.
- `--color-neutral` `#C8C6BE`: support borders / aged band.
- `--color-error` `#8B2E2E`: form errors.
- Anti-template: no purple SaaS gradients; no cream+terracotta pairing; no glow; broadsheet density is intentional per brief (mechanism adoption), not generic AI broadsheet costume.

## Typography

- Single Songti voice: Noto Serif SC with Songti SC / STSong / SimSun / serif fallbacks — masthead memory feature.
- Google Fonts: one family, weights 400/600/700, `display=swap`, preconnect only.
- Hierarchy: masthead display → article titles → lede → multi-column body → labels/TOC nums.
- Chinese measure: ~25–40 characters per column on desktop; single column on narrow screens.
- Paragraph system: spacing between paragraphs (modern web), drop cap on first body paragraph; pull quotes use larger serif spanning columns.
- Vertical accent 「观察城市」 uses `writing-mode: vertical-rl` above 720px; collapses to horizontal rule-label on narrow screens.

## Layout

Composition search (preflight): statement-led masthead vs modular TOC index vs pure multi-column narrative. Chosen hybrid: **statement-led masthead** (gallery thumbnail) + **modular ruled TOC** + **multi-column narrative document** for articles + subscribe strip + copyright footer.

- Reading scene: long-form editorial on phone and desktop; first viewport must prove the masthead.
- Grid: desktop article bodies use CSS `column-count: 3` (2 mid, 1 narrow) with 1px column rules; gutters ~28px.
- Section order: Masthead → TOC (7 entries) → Article 01/02/03 → Subscribe → Footer.
- Separators: double/thick-thin rules between articles; TOC hairlines; footer double rule as newspaper copyright bar.
- Marked zones (`data-ud-check`) on inner padded containers: `masthead`, `toc`, `article-1`, `article-2`, `article-3`, `subscribe`, `footer`; shells keep ≥36px gaps.
- Layout families: cover masthead, ruled index, multi-column feature, subscribe panel, copyright bar.

## Elevation & Depth

Flat newsprint. Depth from paper grain noise (~4% opacity), hairline/double rules, and a light subscribe wash. No card chrome, no multi-layer shadows, no glow.

## Shapes

Near-rectilinear. `sm` radius only on email input and primary button for touch affordance. No pills.

## Components

- Masthead with issue meta, brand name, vertical accent, issue/date/price line.
- TOC list rows (number / title+column+author / page).
- Article module: column badge, title, byline, lede, multi-column body, pull quote.
- Subscribe form: email + primary button + live status.
- Newspaper copyright footer grid + demo attribution line.

## Do's and Don'ts

- Do keep 「街巷」 as the dominant first-viewport signal (thumbnail-legible).
- Do use spot blue only for column system, links, and CTA emphasis.
- Do collapse multi-column and vertical text on narrow screens; keep drop caps readable.
- Do write concrete urban Chinese copy; no marketing slogans.
- Do not clone any real newspaper masthead, nameplate, or signature layout.
- Do not add raster images or emoji.
- Do not wrap articles in floating cards.

## Request Anchor

- Original user request: 为虚构独立城市观察刊物「街巷」设计创刊号网页：报头、本期目录、三篇文章的多栏报纸排版摘录、订阅栏。中文，新闻纸编辑风；采用新闻纸/独立刊物机制（超大宋体报头、多栏网格、首字下沉、双细线分隔、专色蓝栏目号、抽排引文、报纸版权栏），不克隆真实刊物签名。
- Latest user override: Proof-run deliverables only at `docs/demos/jiexiang/index.html` and `DESIGN.md`; self-contained vanilla HTML; Google Fonts ≤2 families; no raster; gallery thumbnail must read masthead; validators must pass; write nothing outside the demo folder (except `/tmp`).
- Deliverable: Single-file inaugural issue page plus this design contract under `docs/demos/jiexiang/`.
- Primary audience: Readers of independent urban writing; gallery viewers judging craft on the Ultimate Design showcase.
- Core job to be done: Recognize the zine, scan this issue’s contents, read three excerpts, optionally leave an email for demo subscribe.
- Success criteria: Masthead dominates first screen; TOC has 6–8 numbered entries; three articles with title/author/lede/body/pull-quote; subscribe + copyright footer; AA contrast; keyboard/focus; reduced motion; validators pass; file ≤160KB.
- Non-goals: Real CMS, print PDF, payments, English locale, photography, dark-mode toggle.
- Must preserve: Fictional brand honesty; footer demo attribution line exactly as specified; Songti/newsprint/spot-blue mechanisms; Chinese-only copy; no emoji/raster.
- Validation must check against: Request Anchor fields; OKF bindings; HTML parse; JS syntax; no emoji; file size; rendered UI audit (zones, overflow, targets); contrast/motion/responsive gates in this contract.

## Content Model

- User intent: Understand what 「街巷」 is and read urban observation excerpts from the inaugural issue.
- Business intent (demo): Express editorial identity and invite a demo email subscribe.
- Message hierarchy: 1) Masthead identity 2) Issue TOC 3) Three feature excerpts 4) Subscribe 5) Copyright.
- First-screen answers: What — 街巷；Why — 独立城市观察；Issue meta — 创刊号 / 日期 / 定价.
- Primary action meaning: 订阅创刊号提醒 → demo status only (no real send).
- Voice and tone: 具体、有画面、像编辑写给读者的纸刊；拒绝畅享/沉浸式等营销腔。
- Terminology: 刊名、栏目号（01 街角经济等）、抽排、目录页码感、创刊号.
- State language: Invalid email → problem + fix; success → restates demo-only behavior.
- Content risks: Do not imply a real registered publication; keep authors and address fictional.

## OKF Preflight

### Active OKF Concepts

- `design-okf/foundations/layout-typography-composition.md`: multi-column newsprint grid, drop caps, pull quotes, CJK measure, vertical accent degrade.
- `design-okf/systems/taste-engine.md`: newsprint editorial read; anti-default locks vs purple glow and cream+terracotta; intentional broadsheet mechanisms from brief.
- `design-okf/systems/type-personality.md`: Songti display as masthead memory; Noto Serif SC + system Songti fallbacks.
- `design-okf/systems/color-system.md`: cool newsprint / ink / spot blue `#1A4B7C` roles with AA contrast.
- `design-okf/content/message-model.md`: first screen = masthead identity; order TOC → articles → subscribe.
- `design-okf/content/ux-writing.md`: concrete Chinese urban copy; verb CTA 订阅创刊号提醒.
- `design-okf/systems/motion-language.md`: scroll reveals ≤380ms transform/opacity; static-first; reduced-motion force-visible.
- `design-okf/digital/accessibility-usability.md`: AA, focus-visible, 44px targets, labels, skip link.
- `design-okf/governance/request-integrity.md`: Request Anchor nine fields drive critique and delivery checks.

### Support References

- `references/branch-marketing-site.md`
- `references/reference-study.md` (mechanism extraction; no signature cloning)
- `references/composition-search.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/proof-run-html.md`
- `references/visual-verification.md`
- `references/quality-gates.md`

### Decision Record

- Constraints extracted: Single self-contained HTML; Google Fonts ≤2 families (using 1 Songti); no raster/emoji; masthead + TOC (6–8) + three multi-column excerpts + subscribe + newspaper footer; spot blue column system; `data-ud-check` on listed inner zones with ≥36px gaps; reveals with IO + 700ms force + print/reduced-motion static; WCAG AA; 320–1440 no horizontal overflow; ≤160KB; exact footer demo line.
- Deliberate exceptions: Broadsheet multi-column + hairline rules are adopted as requested mechanisms (not AI-default costume). Vertical text collapses under 720px. One Google Font family only.
- Reference-study mechanisms adopted: oversized Songti masthead; issue/date/price meta row; multi-column grid with thin rules; drop caps; double-rule article breaks; spot blue column numbering; spanning pull quotes; copyright-bar footer. Signature exclusions: no real newspaper nameplate, logo lockup, distinctive folio ornaments, or proprietary type customizations from any living publication.
- Verification hooks:
  - `validate_design_contract.py --strict-ultimate --require-frontmatter`
  - `validate_okf_usage.py`
  - `validate_html_visual.mjs` → pass, 0 fails, 0 warnings
  - `html.parser` parse; `node --check` on extracted JS; emoji scan; file size ≤160KB

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/foundations/layout-typography-composition.md` | 3-col desktop / 1-col mobile newsprint grid; drop caps; spanning pull quotes; vertical accent degrades | `.article-body`, `.pullquote`, `.vert-mark`, masthead | Rendered audit no overflow; columns collapse ≤720px; zones spaced ≥36px |
| `design-okf/systems/taste-engine.md` | Newsprint editorial read; ban purple glow / cream+terracotta; no real-paper clone | Global CSS, masthead composition | Thumbnail shows 「街巷」; anti-default + no-clone hold in critique |
| `design-okf/systems/type-personality.md` | Songti/Noto Serif SC as masthead memory with system Songti fallbacks | Font link, `.brand-name`, titles | Usable with fonts blocked; weights limited to 400/600/700 |
| `design-okf/systems/color-system.md` | Cool paper surface, ink text, spot blue `#1A4B7C` under 10% | `:root` tokens, `.toc-num`, `.col-badge`, CTA | Body ≥4.5:1 on surface; blue used for emphasis roles only |
| `design-okf/content/message-model.md` | First screen answers what/issue; order TOC→articles→subscribe | `#toc`, articles, `#subscribe` | First viewport masthead-led; IA order matches |
| `design-okf/content/ux-writing.md` | Concrete urban Chinese; CTA「订阅创刊号提醒」; form errors actionable | Article copy, form status | Copy review: no 营销腔; demo-only status honest |
| `design-okf/systems/motion-language.md` | IO reveals ≤380ms; 700ms force-reveal; print + reduced-motion static | `.reveal` script | Reduced-motion shows full content; durations ≤400ms; transform/opacity only |
| `design-okf/digital/accessibility-usability.md` | Landmarks, labels, focus-visible, 44px controls, skip link | Form, TOC links, button | Keyboard path; targets ≥44px in audit |
| `design-okf/governance/request-integrity.md` | Delivery checks against Request Anchor nine fields | This `DESIGN.md` + page sections | Strict contract validator Request Anchor pass |

## Information Architecture

- Core user tasks: Identify the zine, scan TOC, read three excerpts, optionally subscribe (demo).
- Page inventory: One inaugural issue page (`index.html`).
- Navigation model: In-page anchors from TOC to articles/subscribe; skip link to TOC.
- Content hierarchy: Masthead → TOC → 01/02/03 articles → Subscribe → Footer.
- Primary CTA rules: Subscribe button validates email and reports demo-only success.

## Quality Gates

- Request Anchor fit: Masthead, TOC 7 items, three excerpts with pull quotes, subscribe, copyright footer, newsprint mechanisms all present.
- Content: Specific Chinese urban scenes; fictional disclaimer in footer.
- Visual: Masthead dominates thumbnail crop; multi-column without card chrome; spot blue column system visible.
- Accessibility: AA contrast roles; keyboard; focus-visible; 44px+; reduced motion.
- Responsive: 320–1440; columns and vertical text degrade; no horizontal overflow.
- Interaction: Subscribe validation/status; TOC anchors work.
- Performance: ≤160KB; Google Fonts only external request; no rasters.
- Contract consistency: Both Python validators pass; rendered UI audit pass with 0 fails / 0 warnings; `data-ud-check` zones present.

## Assumptions

- Gallery iframe scales a ~1280px render and crops the top ~800px; masthead alone must carry recognition.
- Google Fonts may be blocked; Songti SC / STSong / SimSun / serif keep hierarchy intact.
- Subscribe is front-end demo only; no backend mailer.
- Broadsheet mechanisms are intentional per user brief; the generic anti-broadsheet AI-default lock does not apply when the Request Anchor asks for newsprint.

## Open Questions

- Whether a second quiet Heiti for UI chrome is worth a second font request in a production issue.
- Print PDF / imposition if a physical inaugural print run were commissioned.

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| alpha | 2026-08-12 | Bootstrapped 「街巷」创刊号 page and contract from Ultimate Design Build/YOLO proof-run | Worker deliverable for showcase gallery (newsprint zine) | Design worker agent |
