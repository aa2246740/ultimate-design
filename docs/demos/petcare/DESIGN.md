---
version: 0.1
name: 毛茸茸研究所预约落地页
description: Fictional pet grooming brand booking landing page with three packages, care process, and a static store booking form in a playful cream rounded system.
colors:
  primary: "#B4533C"
  secondary: "#3F7A6A"
  tertiary: "#E8B84A"
  neutral: "#F3E4D3"
  surface: "#FFF7EE"
  on-surface: "#2B211C"
  error: "#B42318"
typography:
  headline-lg:
    fontFamily: "Nunito, Noto Sans SC, PingFang SC, Microsoft YaHei, Hiragino Sans GB, sans-serif"
    fontSize: 52px
    fontWeight: 800
    lineHeight: 1.12
  body-md:
    fontFamily: "Noto Sans SC, PingFang SC, Microsoft YaHei, Hiragino Sans GB, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.7
  label-md:
    fontFamily: "Noto Sans SC, PingFang SC, Microsoft YaHei, Hiragino Sans GB, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
rounded:
  none: 0px
  sm: 10px
  md: 18px
  lg: 28px
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
    textColor: "{colors.surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md}"
---

# Design System

## Overview

「毛茸茸研究所」是虚构宠物洗护品牌的预约落地页：一屏讲清品牌与预约入口，再给三档套餐、到店流程、门店预约表单。视觉方向是**奶油实验室**——浅奶油底、大圆角、几何猫狗 SVG、珊瑚主色与鼠尾草绿辅色；俏皮但不幼稚，价格与流程写具体以建立可信感。

## Colors

- Scene: 家长在家里傍晚用手机预约周末洗护，需要温暖安心，又要看清价格与规则。
- Posture: full palette with cream field dominance (~60%), coral action (~10–15%), sage trust accents, butter yellow tertiary marks.
- `primary` `#B4533C`: CTAs and featured package; paired with cream/`surface` text for AA.
- `secondary` `#3F7A6A`: trust marks, process numbers, checked radios.
- `tertiary` `#E8B84A`: soft highlight on package three and hero atmosphere only.
- `surface` `#FFF7EE` / `neutral` `#F3E4D3`: page field and soft bands.
- `on-surface` `#2B211C` and muted `#5C4B42`: body and supporting text on cream (AA).
- `error` `#B42318`: inline validation example on the date field.
- Anti-template: no purple SaaS gradients; cream avoids serif+terracotta AI cluster by using rounded sans + coral/sage instead.

## Typography

Chinese-first. Display/brand uses Nunito (rounded Latin) stacked with Noto Sans SC for CJK voice of friendly competence. Body and labels stay Noto Sans SC / system CJK sans. At most two Google Font families, `display=swap`, full system fallbacks. Headline tokens stay scalar `px` in YAML; viewport `clamp` is page CSS only.

## Layout

Single scrolling landing page:

1. Sticky nav with brand mark and jump links.
2. Split hero: brand-led claim + CTA left; geometric cat/dog SVG stage right (stacks art-first on small screens).
3. Three package columns (choice containers, not decorative card wallpaper).
4. Four-step vertical process list.
5. Booking split: trust notes + static form.
6. Demo footer line.

Breakpoints roughly 820/900 for nav and grids; readable from 320–1440 with no horizontal overflow. Gallery thumbnail: first screen must read brand, claim, pets, and primary CTA at ~1280 scaled preview.

## Elevation & Depth

Mostly flat cream field with soft radial washes. Raised surfaces: hero art panel and form card use one soft shadow (`0 10px 28px` warm brown at ~8% alpha). No multi-layer glow stacks. Featured package uses border emphasis rather than heavy elevation.

## Shapes

Large radii throughout (`md`/`lg`/`full`) to match playful brand. Pills for nav CTA, primary buttons, and radio chips. Package and form panels use `lg` rounded rectangles. SVG pets are geometric circles/ellipses/paths—no raster, no emoji.

## Components

- Sticky navigation with mobile disclosure menu.
- Primary and secondary pill buttons.
- Package choice panels with icon, price, duration, inclusion list, CTA.
- Numbered process steps.
- Booking form: labeled selects, date, radios/chips, text/tel, textarea; one pre-styled invalid date hint; submit shows demo notice only.
- Inline geometric SVG brand mark and hero illustration.

## Do's and Don'ts

- Do keep brand name hero-scale; headline must not overpower 「毛茸茸研究所」.
- Do write concrete Chinese package items, durations, and prices.
- Do keep form labels visible; placeholders never replace labels.
- Do honor `prefers-reduced-motion` (static pets, no fade choreography).
- Do not use photos, emoji, or external assets beyond Google Fonts.
- Do not invent real store availability or submit real bookings.
- Do not add purple gradients, glow cards, or terracotta-serif cream clichés.
- Do not put stats, promo chips, or secondary marketing blocks in the first viewport.

## Request Anchor

- Original user request: 为虚构宠物洗护品牌「毛茸茸研究所」设计预约落地页：三档服务套餐（名称、包含项目、时长、价格）、洗护流程说明、门店预约表单（门店、日期时段、宠物类型与体型、联系方式）；风格活泼、圆角、奶油色系，可以俏皮但必须专业可信；中文文案，具体、有温度、不油腻；宠物形象用简洁的内联 SVG 插画（几何风格的猫和狗），不要照片。
- Latest user override: Proof-run Build/YOLO; deliver only `docs/demos/petcare/index.html` and `DESIGN.md`; self-contained HTML with Google Fonts only; static booking form; `data-ud-check` zones; validators must pass.
- Deliverable: Single-file Chinese booking landing page plus this design contract under `docs/demos/petcare/`.
- Primary audience: Pet parents booking a store wash/groom slot on mobile or desktop.
- Core job to be done: Understand packages and process quickly, then fill a store booking form with confidence.
- Success criteria: First screen identifies brand and booking CTA; three packages and process are specific; form shows proper labels/states plus one validation hint and demo submit notice; AA contrast, keyboard focus, reduced motion, 320–1440 responsive; both contract validators pass; file ≤160KB.
- Non-goals: Real backend booking, payment, live inventory, photo shoots, multi-page site, dark mode toggle.
- Must preserve: Fictional brand honesty footer; cream rounded playful-but-credible tone; inline SVG pets only; Chinese copy specificity; visual-only form.
- Validation must check against: Request Anchor fit; package/process/form completeness; WCAG AA on cream; `data-ud-check` markers; no emoji/raster; reduced-motion; HTML/JS parse checks; `validate_design_contract.py --strict-ultimate --require-frontmatter`; `validate_okf_usage.py`.

## Content Model

- User intent: Choose a wash package and reserve a store time for their dog or cat.
- Business intent: Convert interest into a booking intention while proving care quality and price clarity.
- Message hierarchy: 1) Brand + offer. 2) Packages with inclusions/time/price. 3) Process reassurance. 4) Booking form with trust rules.
- First-screen answers: What it is (pet wash lab), why it matters (clear packages, gentle timing), what next (预约门店时段).
- Primary action meaning: Submit booking intention → demo notice only (no real send).
- Voice and tone: Warm, concrete, lightly playful; avoid hype adjectives and oily marketing.
- Terminology: 套餐 names stay fixed（基础清爽浴 / 深度舒缓浴 / 造型精修浴）; 门店 / 时段 / 体型 consistent.
- State language: Demo notice after submit; one date-field error hint example; radios show checked styles.
- Trust content: Cancellation window, early arrival for first visit, large-dog note beside the form.
- Content risks: Overclaiming medical treatment; keep skin issues as “建议先就医”.

## OKF Preflight

### Active OKF Concepts

- `design-okf/systems/taste-engine.md`: cream-lab playful direction with anti-default locks and layout-family budget.
- `design-okf/systems/color-system.md`: cream surface roles with coral/sage/butter tokens and AA text pairs.
- `design-okf/systems/type-personality.md`: rounded Nunito + Noto Sans SC Chinese-first friendly voice.
- `design-okf/content/message-model.md`: first-screen brand/offer/CTA; packages → process → booking order.
- `design-okf/content/ux-writing.md`: concrete warm Chinese CTAs, labels, and validation copy.
- `design-okf/content/semantic-binding.md`: labeled controls, `aria-describedby` hints, semantic form structure.
- `design-okf/digital/accessibility-usability.md`: AA contrast, focus-visible, 44px targets, reduced motion.
- `design-okf/systems/motion-language.md`: short transform/opacity entry and float; static under reduced motion.

### Support References

- `references/branch-marketing-site.md`
- `references/proof-run-html.md`
- `references/composition-search.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/visual-verification.md`
- `references/quality-gates.md`

### Decision Record

- Constraints extracted: Single self-contained HTML; ≤2 Google Font families; no raster/emoji; cream rounded playful-credible Chinese landing; three packages + process + static booking form; `data-ud-check` on navigation/hero/packages/process/booking-form/footer; motion ≤400ms transform/opacity with reduced-motion fallback; WCAG AA; 320–1440 no overflow; ≤160KB; footer demo disclaimer.
- Deliberate exceptions: Package panels use card-like containers because they are the choice interaction surface; soft cream field is requested by brief but deliberately avoids serif+terracotta AI default via rounded sans and coral/sage pairing; form is non-submitting by design.
- Verification hooks: HTML parse; extracted JS `node --check`; no-emoji scan; file size; strict design-contract validator; OKF usage validator; manual contrast/responsive/focus review notes for integrator rendered pass.

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/systems/taste-engine.md` | Cream-lab playful read; layout families split-hero / package choice / process sequence / booking workbench; ban purple glow and serif-terracotta cream cliché | Global theme, hero composition, section rhythm | Visual review: brand-first hero; distinct section shapes; anti-default locks hold |
| `design-okf/systems/color-system.md` | Role tokens: coral primary, sage secondary, butter tertiary on cream surface with dark warm text | CSS variables / YAML colors | Contrast check body ≥4.5:1; button cream-on-coral AA |
| `design-okf/systems/type-personality.md` | Rounded friendly display (Nunito) + Noto Sans SC body; two weights each max via Google Fonts | Font links, headings, body | Fonts blocked still readable via system fallbacks; `display=swap` present |
| `design-okf/content/message-model.md` | Order: brand offer → packages → process → booking | Section order in `index.html` | First viewport answers what/why/next; objections resolved before submit |
| `design-okf/content/ux-writing.md` | Verb+object CTAs; specific package lines; warm non-oily Chinese | Hero, packages, form microcopy | Copy review against concreteness and terminology rules |
| `design-okf/content/semantic-binding.md` | Visible labels; date hint via `aria-describedby`; native controls first | Booking form markup | Every input has associated label; invalid example announced by hint id |
| `design-okf/digital/accessibility-usability.md` | Focus-visible ring; 44px+ targets; skip link; reduced motion | Nav, buttons, radios, form | Keyboard walk + target size check; reduced-motion disables float/fade |
| `design-okf/systems/motion-language.md` | Entry fade-up + gentle pet float only; purpose = brand presence; ≤400ms / infinite float opacity-safe via transform | Hero animations + CSS media query | Reduced-motion shows static complete artwork; no non-opacity/transform motion |

## Information Architecture

- Core user tasks: Compare three packages; understand wash steps; submit booking intention.
- Page inventory: One landing page (`index.html`).
- Navigation model: Sticky anchors to 套餐 / 洗护流程 / 预约到店; brand returns to top.
- Content hierarchy: Hero → Packages → Process → Booking → Footer.
- Primary CTA rules: 「预约门店时段」 / 「提交预约意向」; package CTAs deep-link to form.

## Quality Gates

- Request Anchor fit for packages, process, form fields, cream playful tone, SVG pets.
- OKF bindings complete and validators green.
- Content clarity: specific prices/durations/inclusions; trust notes near form.
- Accessibility: AA text, labels, focus, targets, reduced motion.
- Responsive: 320–1440, no horizontal scroll; gallery-thumbnail-readable hero.
- Technical: vanilla HTML/CSS/JS; fonts-only external; ≤160KB; parse checks pass.

## Assumptions

- Fictional Shanghai store names are acceptable placeholders.
- Mid-size dog/cat pricing bands are illustrative starting prices.
- One intentional invalid date hint is enough to demonstrate error styling.
- Integrator will run rendered browser review; this worker has no browser.

## Open Questions

- Real brand palette or logo lockup if the fiction graduates to production.
- Whether large-dog surcharge should be quantified on-page later.
- Live slot inventory API if this becomes a real booking surface.

## Review Log

- 2026-08-12: Build-route YOLO proof run. Bootstrapped cream-lab direction, shipped `index.html` then this contract, bound eight active OKF concepts, ran structural validators and parse/size/emoji self-checks. Maturity remains Candidate pending owner/rendered review.
