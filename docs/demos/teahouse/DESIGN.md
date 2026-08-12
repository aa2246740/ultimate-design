---
version: alpha
name: 山声茶事 Brand Homepage
description: Fictional mountain-spring teahouse homepage with store story, three signature teas, and seat booking — oriental editorial paper feel, Songti display, vertical accents.
colors:
  primary: "#7A2E28"
  secondary: "#3D5A4C"
  tertiary: "#8A8578"
  neutral: "#D0CBC0"
  surface: "#E4E0D6"
  on-surface: "#1F2420"
  error: "#9B2F2F"
typography:
  headline-lg:
    fontFamily: "Noto Serif SC, Songti SC, STSong, SimSun, serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.05
  body-md:
    fontFamily: "Noto Serif SC, Songti SC, STSong, SimSun, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.75
  label-md:
    fontFamily: "Noto Serif SC, Songti SC, STSong, SimSun, serif"
    fontSize: 14px
    fontWeight: 600
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
    textColor: "#F5F1E8"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
---

# Design System

## Overview

「山声茶事」是虚构山泉茶馆品牌官网首页：用东方编辑感与纸感底色讲述门店、三款招牌茶与茶席预约。视觉记忆是宋体大字品牌名压在墨线山形之上，竖排「山泉煮茶」点缀，朱红印章作角标。气质克制、具体、有画面，不做营销腔。

Design Maturity: Candidate — one coherent direction implemented and validated against the Request Anchor; not owner-locked.

## Colors

- Scene sentence: 午后坐在山泉茶屋窗边，纸页微黄偏冷灰，墨色近松烟，点缀一枚朱红印章。
- Color posture: Restrained — ash paper field, ink text, pine secondary, seal red under 10% for CTA and seal.
- `--color-surface` `#E4E0D6`: paper field (cooler ash paper, not warm cream `#F4F1EA`).
- `--color-on-surface` `#1F2420`: ink body and display.
- `--color-primary` `#7A2E28`: seal cinnabar for primary CTA and seal strokes (not terracotta-on-cream pairing).
- `--color-secondary` `#3D5A4C`: pine / tea leaf for kickers, steam, accents.
- `--color-tertiary` `#8A8578`: stone muted labels.
- `--color-neutral` `#D0CBC0`: aged band / borders support.
- `--color-error` `#9B2F2F`: form errors.
- `--color-muted` `#5A5E56`: secondary body (AA on surface).
- Anti-template: no purple SaaS gradients, no cream+terracotta AI default, no neon glow.

## Typography

- Brand / headline: Noto Serif SC (Songti voice) with Songti SC, STSong, SimSun, serif fallbacks. Display is the memory feature.
- Body and labels stay in the same Songti family for editorial unity; form controls inherit it.
- Google Fonts: one family, weights 400/600/700, `display=swap`, preconnect only.
- Chinese measure ~25–40 characters where practical; prices use tabular nums.
- Vertical accent 「山泉煮茶」 uses `writing-mode: vertical-rl` on wide screens; collapses to horizontal rule-label under 900px.

## Layout

One scrolling homepage: sticky nav → full-bleed mountain hero → store story → three teas as editorial list (not card grid) → booking form → footer.

- Hero (first viewport / gallery thumbnail): brand name as dominant type, one lead sentence, CTA pair, ink-line mountains edge-to-edge, seal + vertical accent. No stats or secondary promos.
- Story: prose + sparse meta (address, seats, hours) and small ink cup SVG.
- Teas: three rows with name, origin, flavor, price.
- Booking: copy left, form right (stack on mobile): name, phone, time slots, party size, optional tea.
- Layout families: statement-led hero, prose+aside story, ruled editorial list, split booking panel.

## Elevation & Depth

Mostly flat paper. Depth from paper grain noise at ~3.5% opacity, hairline rules, and a light form panel wash. No multi-layer shadows, no floating cards, no glow.

## Shapes

Near-rectilinear: `sm` radius on buttons and inputs. Seal is a square SVG with slight rotation. Avoid pills and heavy rounding.

## Components

- Sticky navigation with brand mark and three anchors.
- Primary button (seal red) and ghost button.
- Tea list rows (name / description / price).
- Booking form: text, tel, radio slot chips, selects, live status.
- Decorative inline SVG: mountains, steam, seal, ink cup.

## Do's and Don'ts

- Do keep 「山声茶事」 as the hero-level brand signal.
- Do write concrete Chinese copy with sensory detail; no marketing slogans.
- Do degrade vertical text and keep 320–1440 readable without horizontal overflow.
- Do disable all animation under `prefers-reduced-motion: reduce`.
- Do not use raster images or emoji.
- Do not wrap teas in card chrome; rules and type carry the list.
- Do not use purple gradients, cream+terracotta defaults, or broadsheet-dense columns.

## Request Anchor

- Original user request: 为虚构茶馆品牌「山声茶事」设计品牌官网首页：山泉煮茶的门店故事、三款招牌茶（各有名字、风味描述、价格）、茶席预约（时段与人数）。东方编辑感、纸感底色、宋体标题、竖排文字点缀。中文文案，要求具体、克制、有画面感，不用营销腔。
- Latest user override: Proof-run HTML deliverables only at `docs/demos/teahouse/index.html` and `DESIGN.md`; self-contained vanilla file; Google Fonts at most two families; no raster images; gallery thumbnail must read at ~1280×800 crop; validators must pass.
- Deliverable: Single-file homepage plus this design contract under `docs/demos/teahouse/`.
- Primary audience: Visitors deciding whether to book a quiet mountain-spring tea seat; also gallery viewers judging craft on the Ultimate Design showcase.
- Core job to be done: Understand the place, choose a tea, and reserve a time slot with party size.
- Success criteria: First screen shows brand + atmosphere + next action; story, three priced teas, and booking are complete; AA contrast; keyboard/focus; reduced motion; validators pass; file ≤160KB.
- Non-goals: Multi-page site, real payments, CMS, dark mode toggle, English locale, photography.
- Must preserve: Fictional brand honesty; footer demo attribution line; Songti/paper/editorial direction; Chinese-only copy; no emoji/raster.
- Validation must check against: Request Anchor sections present; OKF bindings; HTML parse; JS syntax; no emoji; file size; contrast/motion/responsive constraints in contract gates.

## Content Model

- User intent: Find a quiet tea seat, know what is poured, book a slot.
- Business intent: Express brand identity and convert to a booking request (demo).
- Message hierarchy: 1) Brand and place 2) Store story 3) Three teas 4) Book seat.
- First-screen answers: What — 山声茶事; Why — 山泉煮茶、安静六席; Next — 预约茶席 / 看茶单.
- Primary action meaning: 提交预约 → demo confirmation status (no real SMS).
- Voice and tone: 克制、具体、有画面；像店主写给熟客的说明，不是广告。
- Terminology: 茶席、招牌、每壶、时段、人数；avoid 畅享/臻选/沉浸式.
- State language: Form errors name missing fields or bad phone; success restates slot and party count as demo.
- Content risks: Do not invent real addresses as real businesses; keep fictional Qingcheng-adjacent place name.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: oriental editorial paper read; anti-default locks against cream+terracotta, purple gradients, card grids.
- `design-okf/systems/type-personality.md`: Songti display as brand memory; Noto Serif SC + system Songti fallbacks.
- `design-okf/systems/color-system.md`: ash paper / ink / pine / seal roles with AA contrast.
- `design-okf/content/message-model.md`: first screen brand+place+CTA; section order story→teas→booking.
- `design-okf/content/ux-writing.md`: restrained Chinese CTAs and form copy; no marketing filler.
- `design-okf/systems/motion-language.md`: entry-play mountain ink, steam opacity, short reveals; static-first.
- `design-okf/systems/motion-contract.md`: mountain SVG `entry-play` with reduced-motion complete stroke.
- `design-okf/digital/accessibility-usability.md`: AA, focus-visible, 44px targets, labels, reduced motion.
- `design-okf/governance/request-integrity.md`: Request Anchor fields drive critique and delivery checks.

### Support References

- `references/branch-marketing-site.md`
- `references/branch-brand-system.md` (brand posture only; no VI manual)
- `references/composition-search.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/proof-run-html.md`
- `references/visual-verification.md`
- `references/quality-gates.md`

### Decision Record

- Constraints extracted: Single self-contained HTML; Google Fonts ≤2 families; no raster/emoji; paper+Songti+vertical accent; three named priced teas; booking with slots and party size; `data-ud-check` on navigation/hero/story/teas/booking/footer; motion transform/opacity ≤400ms with reduced-motion off; WCAG AA; 320–1440 no horizontal overflow; ≤160KB; footer attribution line required.
- Deliberate exceptions: Vertical text collapses horizontally below 900px (legibility over ornament). Form panel uses a light wash border instead of a floating card. One Google Font family only (Songti) rather than two.
- Verification hooks:
  - `validate_design_contract.py --strict-ultimate --require-frontmatter`
  - `validate_okf_usage.py`
  - `html.parser` parse; `node --check` on extracted JS
  - File size ≤160KB; emoji scan
  - Manual/Integrator review: thumbnail crop, contrast, keyboard, reduced motion

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Oriental editorial paper scene; ban cream+terracotta, purple glow, tea cards | Global CSS, hero, tea list | Thumbnail read; anti-default locks hold in critique |
| `design-okf/systems/type-personality.md` | Songti/Noto Serif SC as hero memory with system Songti fallbacks | Font link, `.hero-brand`, section titles | Renders with fonts blocked; weights limited |
| `design-okf/systems/color-system.md` | Ash paper surface, ink text, pine secondary, seal primary under 10% | `:root` tokens, CTA, seal SVG | Body text ≥4.5:1 on surface; CTA large enough for red |
| `design-okf/content/message-model.md` | Hero answers brand/place/next; order story→teas→booking | `#top`, `#story`, `#teas`, `#booking` | First viewport answers what/why/next; IA order matches |
| `design-okf/content/ux-writing.md` | Concrete restrained Chinese; CTAs 预约茶席 / 提交预约; form errors problem+fix | Hero lead, tea blurbs, form status | Copy review: no 营销腔; errors actionable |
| `design-okf/systems/motion-language.md` | Entry-play mountain, steam, ≤380ms reveals; static works first | `.reveal`, `.steam-line`, mountain path | `prefers-reduced-motion` disables animation |
| `design-okf/systems/motion-contract.md` | Mountain outline `entry-play`; reduced motion sets dashoffset 0 | `#mountain-outline` `data-ud-motion` attrs | Markers resolve; stroke complete under reduce |
| `design-okf/digital/accessibility-usability.md` | Landmarks, labels, focus-visible, 44px controls, skip link | Nav, form, buttons, slot radios | Keyboard tab order; targets ≥44px |
| `design-okf/governance/request-integrity.md` | Delivery checks against Request Anchor nine fields | This `DESIGN.md` + page sections | Strict contract validator Request Anchor pass |

## Information Architecture

- Core user tasks: Learn the place, compare three teas, book a seat with time and party size.
- Page inventory: One homepage (`index.html`).
- Navigation model: Sticky anchors 门店 / 茶单 / 预约; brand returns to top.
- Content hierarchy: Hero → Story → Teas → Booking → Footer.
- Primary CTA rules: Hero 预约茶席 scrolls to form; form 提交预约 validates and shows demo status.

## Quality Gates

- Request Anchor fit: Story, three teas with prices, booking slots+party, oriental editorial constraints all present.
- Content: Specific Chinese copy; fictional disclaimer in footer.
- Visual: Brand dominates first screen; no card tea grid; thumbnail-legible hero.
- Accessibility: AA contrast roles; keyboard; focus-visible; 44px+; reduced motion.
- Responsive: 320–1440; vertical text degrades; no horizontal overflow.
- Interaction: Booking validation and status; anchors work.
- Performance: ≤160KB; Google Fonts only external request; no rasters.
- Contract consistency: Both Python validators pass; `data-ud-check` zones present.

## Assumptions

- Gallery iframe scales a ~1280px render and crops the top ~800px; hero must carry the brand without relying on below-fold content.
- Google Fonts may be blocked; Songti SC / STSong / SimSun / serif keep layout intact.
- Booking is a front-end demo only; no backend.

## Open Questions

- Real reservation backend or WeChat integration if this brand were produced for a live shop.
- Whether a second font (e.g. quiet Heiti for UI chrome) is worth the extra request once production metrics exist.

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| alpha | 2026-08-12 | Bootstrapped teahouse demo page and contract from Ultimate Design Build/YOLO proof-run | Worker deliverable for showcase gallery | Design worker agent |
