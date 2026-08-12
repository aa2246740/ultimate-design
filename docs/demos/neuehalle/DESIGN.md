---
version: 0.1
name: 新厅美术馆 — 形式与功能
description: Fictional museum exhibition page for「形式与功能：包豪斯百年」— Bauhaus-poster geometry, three wayfinding halls, visit info, and ticket stubs in Chinese.
colors:
  primary: "#E30613"
  secondary: "#FFD100"
  tertiary: "#0057B8"
  neutral: "#E6E6E6"
  surface: "#FFFFFF"
  on-surface: "#111111"
  error: "#B00020"
typography:
  headline-lg:
    fontFamily: "Space Grotesk, Noto Sans SC, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.02
  body-md:
    fontFamily: "Noto Sans SC, PingFang SC, Microsoft YaHei, Segoe UI, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
  label-md:
    fontFamily: "Space Grotesk, Noto Sans SC, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
rounded:
  none: 0px
  sm: 0px
  md: 0px
  lg: 0px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  primary-button:
    backgroundColor: "{colors.on-surface}"
    textColor: "{colors.surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
---

# Design System

## Overview

「新厅美术馆」展览页演示一次包豪斯构成主义读法：严格的红 / 黄 / 蓝 + 黑白色彩预算，圆 / 三角 / 方同时承担海报拼贴与展区导视，超大日期数字与旋转文字条作为信息图形，票务做成虚线撕裂的几何票根。页面是中文单页营销 / 展览信息页，第一屏必须以海报尺度在 gallery iframe（约 1280px 渲染、顶部约 800px）立刻成立。品牌名「新厅美术馆」是 hero 级信号，展名「形式与功能」次之。

## Colors

- Scene sentence: 白天在明亮画廊手机上扫一眼展览海报——印刷油墨的原色块、黑线网格、黄底黑字，没有柔光与渐变。
- Color posture: **Full palette** with a hard budget — only primary red `#E30613`, secondary yellow `#FFD100`, tertiary blue `#0057B8`, ink `#111111`, paper `#FFFFFF`, and quiet neutral `#E6E6E6`. No other hues.
- Text on yellow is always ink (`#111111`); never light text on yellow (WCAG).
- Red / blue carries large fills and hall wayfinding; body text stays ink on paper or paper on ink/blue/red heads at large sizes.
- Anti-template locks: no purple/indigo SaaS gradients, no warm cream + terracotta luxury default, no broadsheet hairline newspaper layout, no soft glow elevation.

## Typography

- Display / numerals: Space Grotesk 500/700 — geometric Latin memory for mega dates, section ticks, ticket prices.
- Body / Chinese UI: Noto Sans SC 400/700/900 — institutional clarity for exhibition copy.
- YAML tokens stay scalar px; page CSS may use `clamp()` for responsive display.
- Fallback stacks (`PingFang SC`, `Microsoft YaHei`, system sans) must keep hierarchy if Google Fonts fail.
- Strong weight contrast (900/700 vs 400); letter-spacing near zero except small uppercase labels.

## Layout

One scrolling Chinese exhibition page with sticky nav.

- Composition search (2–3 hypotheses): (1) Statement-led full-bleed poster hero + modular halls — chosen. (2) Split dialogue type-left / geometry-right only — rejected for thumbnail weakness if geometry collapses. (3) Uniform modular grid all sections — rejected as monotonous card rhythm.
- Hero: brand → title → subtitle with date chip → dual CTAs; geometric collage + mega date `2026/03` + clipped −7° text strip (展期 / 口号).
- Intro: lede + meta panel (dates, curator, keywords).
- Halls: three equal columns bound to circle / triangle / square wayfinding.
- Visit: three info columns + blue notice band.
- Tickets: three geometric stubs with dashed tear edges.
- Footer: brand trio + required demo attribution.
- Breakpoints: stack under ~900px; max width 1120px; page padding ≥12–16px.

## Elevation & Depth

Flat print depth only: 3px ink borders, solid color blocks, optional 2px hover translate on halls. No blur shadows, no glass, no parallax. Overlapping geometry in the hero is figure/ground collage, not elevation.

## Shapes

`rounded.none` on UI chrome. Circles, triangles, and squares are the only decorative vocabulary — and each must carry wayfinding or brand meaning (hall binding, footer trio, poster collage). Ticket stubs use dashed tear lines and side notches as functional ticket language, not stickers.

## Components

- Primary button: ink fill, paper text, 3px border, min-height 48px; yellow alternate CTA with ink text.
- Sticky nav with 44px+ text targets and red square brand mark.
- Hall articles with shape-bound icon tiles.
- Ticket stubs (general / student / member) with dashed perforation and notch motif.
- Skip link to `#main`; focus-visible 3px blue ring.

## Do's and Don'ts

- Do keep「新厅美术馆」larger / earlier than the exhibition title as brand-first hero signal.
- Do bind 工坊→圆/红, 舞台→三角/黄, 课堂→方/蓝 and repeat that binding in copy (“导视”).
- Do put black text on yellow surfaces; verify AA.
- Do clip the rotated strip so transformed bounds stay inside the page.
- Do not add emoji, rasters, extra hues, soft cards, or pure decorative stickers.
- Do not let geometric collage cause horizontal overflow at 320px — reflow / scale the stage.
- Do not claim 新厅美术馆 is a real institution; keep the demo footer line.

## Request Anchor

- Original user request: 为虚构美术馆「新厅美术馆」设计展览页「形式与功能:包豪斯百年」:海报式几何 hero、展览介绍、三个展区、参观信息与票务。中文。Adopt Bauhaus poster + museum exhibition-page mechanisms (RGB+BW budget; circle/triangle/square collage; mega dates; rotated strip; shape wayfinding; ticket stubs; grid typography) without cloning any real museum identity.
- Latest user override: Deliver exactly `docs/demos/neuehalle/index.html` and `DESIGN.md`; proof-run HTML hard constraints (zones, motion, a11y, overflow, ≤160KB); self-verify with contract/OKF/visual validators.
- Deliverable: `/workspace/docs/demos/neuehalle/index.html` and `/workspace/docs/demos/neuehalle/DESIGN.md` only.
- Primary audience: Gallery visitors and design-interested public planning a visit; secondary: showcase iframe viewers judging craft at thumbnail scale.
- Core job to be done: Immediately recognize the exhibition and museum, understand three halls via shape wayfinding, find visit facts, and choose a ticket tier.
- Success criteria: Poster hero reads in ~800px thumbnail crop; all requested sections present in Chinese; AA contrast (esp. yellow+black); keyboard/focus/44px; reduced-motion static; 320–1440 no horizontal overflow; validators pass; file ≤160KB; footer attribution exact.
- Non-goals: Real ticketing checkout, CMS, multi-page site, raster photography, cloning Bauhaus-Archiv / any real museum VI, scroll-hijack storytelling.
- Must preserve: Fictional institution framing; mechanism adoption without signature transfer; `data-ud-check` zone names; Google Fonts ≤2 families; vanilla single file; required footer sentence.
- Validation must check against: Request Anchor fit; `validate_design_contract.py --strict-ultimate --require-frontmatter`; `validate_okf_usage.py`; `validate_html_visual.mjs` pass with 0 fails/warnings; HTML parse; JS `node --check`; no emoji; byte size.

## Content Model

- User intent: Decide whether to visit and which ticket to buy; orient to three halls.
- Business intent: Communicate exhibition thesis and practical visit/ticket info with memorable Bauhaus craft.
- Message hierarchy: 1) Museum + exhibition identity. 2) Thesis intro. 3) Three halls. 4) Visit logistics. 5) Ticket tiers. 6) Demo disclosure.
- First-screen answers: Who (新厅美术馆), what (形式与功能 / 包豪斯百年), when (2026.03.15–09.15 / mega 2026·03), next (进入展区 / 查看票价).
- Primary action meaning: Enter halls or view tickets — in-page anchors (demo has no payment backend).
- Voice and tone: Institutional, precise, teaching without academic fog; short concrete Chinese sentences.
- Terminology rules: 展区 / 导视 / 票根 / 构成; keep 包豪斯 as loanword; avoid empty 沉浸式 / 赋能.
- State language rules: Ticket CTAs are selection labels only; no fake success states.
- Trust / risk content: Footer states demo + fictional museum; visit phone marked 演示.
- Content risks: Cloning a real museum’s identity; decorative geometry without wayfinding meaning; yellow/light-text contrast failure.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: Bauhaus constructivist read; anti-default locks; layout-family budget; thumbnail memory = geometric poster.
- `design-okf/systems/type-personality.md`: Space Grotesk + Noto Sans SC pairing; mega numerals as memory; CJK body clarity.
- `design-okf/systems/color-system.md`: Strict RGB + BW role budget; yellow requires ink text.
- `design-okf/foundations/visual-communication-hierarchy.md`: Brand-first poster hierarchy; one job per section.
- `design-okf/foundations/gestalt-composition.md`: Overlapping circle/triangle/square as figure/ground collage serving hierarchy and wayfinding.
- `design-okf/foundations/necessary-design-judgment.md`: Every shape has an information duty; delete pure stickers.
- `design-okf/content/message-model.md`: First screen who/what/when/next; order intro→halls→visit→tickets.
- `design-okf/content/ux-writing.md`: Concrete Chinese CTAs and hall/visit copy.
- `design-okf/systems/motion-language.md`: Short scroll reveals; static-first; reduced-motion force visible.
- `design-okf/digital/accessibility-usability.md`: WCAG AA, focus-visible, 44px targets, skip link, keyboard.
- `design-okf/digital/responsive-interaction.md`: Collage reflow under 900/560; no page overflow 320–1440.
- `design-okf/governance/request-integrity.md`: Nine-field Request Anchor drives delivery checks.

### Support References

- `references/branch-marketing-site.md`
- `references/graphic-print.md` (poster craft for hero; screen draft only, not print-ready)
- `references/reference-study.md` (mechanism extraction; no museum signature cloning)
- `references/composition-search.md`
- `references/proof-run-html.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/visual-verification.md`
- `references/quality-gates.md`
- `SKILL.md` (Build route, YOLO)

### Decision Record

- Constraints extracted: Single-file vanilla HTML; ≤2 Google Font families with `display=swap` + preconnect; no rasters/emoji; RGB+BW only; shapes = collage + wayfinding; mega dates; rotated strip in-bounds; ticket stubs; Chinese copy; `data-ud-check` on navigation / poster-hero / intro / halls / visit / tickets / footer; marked-zone gaps ≥36px; reveals via IntersectionObserver + 700ms force + print force; reduced motion static; transform/opacity ≤400ms; 44px targets; AA; 320–1440 no overflow; ≤160KB; exact footer line.
- Deliberate exceptions: Hall and ticket blocks use 3px ink borders (print language) rather than borderless text — still not soft elevated cards. Hero strip is statically rotated (−7°) inside an overflow-hidden clip rather than continuously spinning, to keep motion budget for reveals only.
- Reference-study mechanisms adopted (no cloning): primary-color poster budget; constructivist circle/triangle/square collage; oversized typographic dates; diagonal/rotated information strip; shape-as-wayfinding; perforated ticket graphic; grid field + weight contrast. Signature exclusions: any real museum wordmark, Bauhaus-Archiv / Stiftung Bauhaus Dessau / MoMA exhibition identity, specific historical poster layouts as copyable compositions.
- Verification hooks: both Python validators; `validate_html_visual.mjs` to `/tmp/audit-neuehalle`; `html.parser`; extracted JS `node --check`; emoji scan; `wc -c` ≤160KB.

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Constructivist museum-poster read; dials variance 7 / density 5 / motion 3 / distinction 9 / type 8 / experiment 7; ban purple gradients, cream-terracotta, soft cards, glow | Global CSS, `.poster`, halls, tickets | Thumbnail shows brand+geometry+title; no banned defaults |
| `design-okf/systems/type-personality.md` | Space Grotesk for display/numerals; Noto Sans SC for Chinese body; max two Google families + system fallbacks | Font links, `.poster-title`, `.date-mega`, body | Fonts blocked still readable; clamp wraps at 320px |
| `design-okf/systems/color-system.md` | Only red/yellow/blue/ink/paper/neutral; ink text on yellow; hall colors bound to shapes | `:root` tokens, hall icons, ticket heads, yellow chips | Contrast AA; no light text on `#FFD100` |
| `design-okf/foundations/visual-communication-hierarchy.md` | Brand → title → date/sub → CTA; each section one job | `.poster-kicker` / `.poster-title` / sections | First viewport answers who/what/next; sections non-competing |
| `design-okf/foundations/gestalt-composition.md` | Overlapping RGB shapes + bar as poster figure/ground; similarity binds hall icons to hero shapes | `.poster-stage`, `.hall-icon` | Collage readable; hall shapes match hero vocabulary |
| `design-okf/foundations/necessary-design-judgment.md` | Shapes only if wayfinding/brand/ticket language; strip carries展期/口号; delete sticker-only ornaments | Hero strip, hall way lines, ticket notches | Critique: every geometry has an info duty |
| `design-okf/content/message-model.md` | Order poster→intro→halls→visit→tickets→footer | Section IDs and nav anchors | IA matches decision path |
| `design-okf/content/ux-writing.md` | CTAs「进入三个展区」「查看票价」「选择…票」; concrete visit facts | Hero CTAs, halls, visit, tickets | Chinese copy review; no filler |
| `design-okf/systems/motion-language.md` | Reveal opacity/translateY ≤360ms; IO + 700ms force + print/reduced-motion reveal | `.reveal` script/CSS | Reduced-motion shows content; durations ≤400ms |
| `design-okf/digital/accessibility-usability.md` | Landmarks, skip link, focus-visible, 44px+ targets, decorative `aria-hidden` | Nav, buttons, footer links | Keyboard order; targets ≥44px; AA pairs |
| `design-okf/digital/responsive-interaction.md` | Hero stacks; collage scales; 3-col grids → 1 col under 900px; overflow hidden on strip clip | Media queries, `.poster-stage` | Visual audit 320–1440 no horizontal overflow |
| `design-okf/governance/request-integrity.md` | Delivery gated on nine Request Anchor fields + mechanism list | This contract + page sections | Strict contract validator Request Anchor pass |

## Information Architecture

- Core user tasks: Identify exhibition → orient to three halls → read visit logistics → pick ticket tier.
- Page inventory: Single `index.html` exhibition page.
- Navigation model: Sticky anchors 展览 / 展区 / 参观 / 票务; brand returns to `#top`.
- Content hierarchy: Poster hero → Intro → Three halls → Visit → Tickets → Footer.
- Primary CTA rules: Verb + object Chinese CTAs; ticket buttons are in-page selection labels (demo).

## Quality Gates

- Request Anchor fit: poster hero, intro, three shape-bound halls, visit, tickets, Chinese, mechanisms, no cloning.
- Contract validators: `validate_design_contract.py --strict-ultimate --require-frontmatter` and `validate_okf_usage.py` pass.
- Rendered UI audit: `validate_html_visual.mjs` status pass, 0 fails, 0 warnings.
- Accessibility: AA (yellow+ink), keyboard, focus-visible, 44px, reduced motion.
- Responsive: 320–1440, collage reflow, no horizontal overflow, rotated strip clipped.
- Performance/size: ≤160KB; Google Fonts only external dependency.
- Proof markers: `data-ud-check` on navigation, poster-hero, intro, halls, visit, tickets, footer with ≥36px gaps.

## Assumptions

- Gallery iframe ~1280×800 crop; hero brand + title + geometry + strip must read without below-fold content.
- Ticket purchase is demo-only (anchor stays on `#tickets`).
- Design Maturity Candidate — verified by validators, not owner-locked.
- Mechanism sources are third-party / public Bauhaus poster traditions and generic museum exhibition-page patterns; provenance = public reference for own fictional brand; no signature transfer.

## Open Questions

- If produced for a live museum, confirm real ticketing API, accessibility services, and photography policy.
- Whether a printable A2 poster export should share the same tokens in a later graphic-print pass.

## Review Log

- 2026-08-12: Bootstrapped Bauhaus exhibition demo for 新厅美术馆 (Build/YOLO/proof-run). Active OKF bound for taste, type, color, hierarchy, gestalt, necessity, message, UX writing, motion, a11y, responsive, request integrity. Reference-study mechanisms recorded with no-cloning boundary. Artifact-first `index.html`, then contract.
- 2026-08-12: Critique pass — raised museum name above exhibition title for brand-first hierarchy; replaced CSS triangle with stroked SVG; thickened rotated strip; nav/poster zone gap ≥40px after tight-spacing fail.

## Design Maturity

- Status: Candidate

## Visual Fingerprint

- Surface / page shape: White paper field with ink rules and primary-color blocks; light gray grid in hero only.
- Entry / hero pattern: Statement-led constructivist poster — brand, title, date chip, dual CTAs, RGB collage, mega date, clipped diagonal strip.
- Section / content rhythm: Intro split → three hall modules → three visit columns → three ticket stubs.
- Navigation / footer / chrome: Sticky ink-border nav; black footer with RGB trio mark.
- Typography roles: Grotesk display/numerals; Sans SC body/UI; bold labels.
- Imagery / evidence strategy: CSS/SVG geometry only; no photography.
- Motion behavior: Short section reveals; static under reduced motion; strip is rotated placement not spin.
- Intentional repetition: Circle/triangle/square vocabulary repeated as wayfinding (functional reason).
- Locked axes: (none — Candidate)
- Allowed variation: Hall copy length, ticket prices, exact exhibition dates within fictional brief.

## Reference Study

- Source mode: Prompt-described mechanisms from Bauhaus poster tradition + excellent museum exhibition pages (no single URL clone).
- Provenance / rights: Third-party / public reference for fictional brand application; diagnosis + mechanism transfer only.
- Primary mechanisms adopted: RGB+BW budget; constructivist shape collage; mega typographic dates; rotated information strip; shape-as-wayfinding; perforated ticket graphic; grid + weight contrast.
- Signature exclusions: Real museum names/marks, specific historical poster compositions as pixel clones, protected exhibition campaign identities.
- Evidence confidence: Inferred from well-known Bauhaus graphic mechanisms and stated user brief (Observed in brief constraints; not traced to one URL).
- Date: 2026-08-12; links to Request Anchor above.
