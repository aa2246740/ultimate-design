---
version: alpha
name: ultimate-design-xhs-english-carousel
description: English-first Xiaohongshu 9-frame carousel promoting the Ultimate Design skill.

colors:
  primary: "#111111"
  secondary: "#f6f1e6"
  tertiary: "#2457ff"
  neutral: "#fffaf1"
  surface: "#f6f1e6"
  on-surface: "#111111"
  error: "#ff3b30"

typography:
  headline-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: "76px-116px"
    fontWeight: "700-900"
    lineHeight: "0.92-1.0"
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: "24px-34px"
    fontWeight: "610-790"
    lineHeight: "1.16-1.34"
  label-md:
    fontFamily: "SF Mono, Menlo, Consolas, Liberation Mono, monospace"
    fontSize: "17px-24px"
    fontWeight: "750-850"
    lineHeight: "1.0-1.32"

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 8px
  full: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 54px

components:
  carousel-frame:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
---

# Design System

## Overview

This is a 9-frame English-language carousel for Xiaohongshu-style vertical reading. The goal is to explain Ultimate Design as a design skill that avoids generic AI-template output by combining content hierarchy, design contracts, taste governance, OKF branch routing, typography art direction, critique, and rendered proof.

The design should feel closer to an English maker/design launch carousel than a translated Chinese poster series. It uses direct English hooks, explanatory modules, and diagrams rather than slogan-only big type.

## Colors

The series uses one shared nine-color palette: ink, warm paper, blue, red, lime, pink, cyan, violet, amber, plus one green verification accent. Color is used as a page-level art-direction signal, not only decoration.

Rules:

- Keep the palette strip on every frame to preserve series continuity.
- Use strong accent fields for page identity; do not make all nine frames share the same background logic.
- Preserve high contrast between text and surface.
- Avoid generic AI-purple gradient as the default excitement device. Gradients may appear only as a deliberate launch/closing treatment.

## Typography

Type is the primary visual memory feature. The system uses available system fonts for portability:

- Display and core copy: system sans for clarity and platform compatibility.
- Editorial accent: Georgia for frames that need a more essay-like English voice.
- Metadata and process labels: system monospace for agent/workflow credibility.
- Large display is expressive; explanatory text remains readable.

Line heights are tight for headlines and looser for explanatory modules. Letter spacing is intentionally `0`; the layout relies on scale, weight, position, and composition instead of tracking tricks.

## Layout

Format is 1080 x 1440 px, a 3:4 vertical carousel size commonly used for Xiaohongshu image posts. Safe area is 54 px on all sides, with a bottom metadata area and palette strip.

Composition varies by message role:

- Frame 1: warning poster with template fingerprints.
- Frame 2: dark system map with four conceptual modules.
- Frame 3: blueprint contract sheet.
- Frame 4: editorial reading-path explainer.
- Frame 5: anti-default rule wall.
- Frame 6: type specimen.
- Frame 7: OKF routing map.
- Frame 8: verification workflow proof panel.
- Frame 9: launch/CTA manifesto.

## Elevation & Depth

Depth is mostly graphic: borders, hard shadows, overlapping planes, and strong color fields. Avoid soft glass shadows. Hard shadows are allowed only when they reinforce poster/campaign energy.

## Shapes

Most containers use 8 px radius or square corners. Pills are reserved for metadata/chip-like statements. Do not introduce oversized rounded card UI.

## Components

- Topbar: series label and page number.
- Palette strip: series identity and cross-frame continuity.
- Footer note: medium constraints or conceptual framing.
- Panel: explanation block, max 8 px radius.
- Node/check/path-step: content modules chosen by message role.

## Do's and Don'ts

Do:

- Keep each frame readable as an English product/design carousel.
- Make every frame answer one specific communication job.
- Vary layout families across the nine frames.
- Use typography as a memory feature without sacrificing clarity.
- Render and inspect every exported PNG.

Don't:

- Reuse the previous Chinese big-character poster logic.
- Fill every slide with identical rounded cards.
- Use decorative badges that do not carry meaning.
- Let taste drift away from the actual explanation of the skill.
- Claim final publication readiness beyond a screen/social draft.

## Agent Execution Rules

- Read this file before editing the carousel.
- Preserve 1080 x 1440 export dimensions unless the platform target changes.
- If text changes, rerender all frames and inspect the contact sheet.
- Do not add external font files without checking license and portability.

## Request Anchor

- Original user request: Redesign the previous promotional image set using Xiaohongshu dimensions, make it more information-rich, write and lay it out in English context, allow all styles to change, then send the finished zip to Feishu.
- Latest user override: English-first design, richer content, do not keep Chinese layout habits.
- Deliverable: 9 PNG carousel frames plus source HTML, design contract, README, contact sheet, and zip package.
- Primary audience: English-reading builders/designers evaluating AI design skills.
- Core job to be done: Explain what Ultimate Design is, why template-looking AI design is a problem, and how Ultimate Design avoids it.
- Success criteria: Correct 3:4 vertical format; richer but readable English content; visibly varied compositions; coherent series identity; exported images verified and sent to Feishu.
- Non-goals: Real PPTX delivery; Chinese copy; exact imitation of any third-party skill visual style.
- Must preserve: Ultimate Design's real mechanisms: DESIGN.md, Request Anchor, content model, Taste Engine, type personality, OKF routing, critique/repair, visual verification.
- Validation must check against: dimensions, all 9 frames exported, readable contact sheet, no obvious overlaps/clipping, no old horizontal X-poster format.

## Content Model

- User intent: Quickly understand Ultimate Design's value and difference from template-like AI design skills.
- Message hierarchy:
  1. Many AI design outputs converge into recognizable templates.
  2. Rules are necessary but not enough; taste and proof matter.
  3. Ultimate Design uses a contract-driven process to preserve intent.
  4. Content, type, OKF routing, critique, and verification make the output more durable.
  5. Use it for artifacts that must communicate clearly and look intentionally made.
- Voice and tone: Confident, critical, builder-facing, practical, hype controlled by specificity.
- Terminology rules: Use "contract", "Request Anchor", "Taste Engine", "OKF router", "type personality", "rendered proof" consistently.
- Content risks: Avoid overstating that the skill guarantees perfect design. Present it as a disciplined workflow and quality system.

## Taste Signature

- Design read: English design/maker educational carousel for a social platform, consumed on mobile, selling a workflow concept rather than a finished SaaS product.
- Taste dials: visual variance 8, information density 6, motion depth 0, brand distinction 8, type expressiveness 8, experiment risk 6.
- Category defaults avoided: identical card grids, generic AI gradient/glass, slogan-only posters, fake UI proof, one-style carousel.
- Layout families or slide archetypes: warning poster, concept matrix, contract blueprint, editorial explainer, rule wall, type specimen, routing map, verification panel, launch manifesto.
- Visual memory feature: typography-led compositions with a consistent nine-color palette strip.
- Type personality: direct, sharp, maker-facing, technical where needed, editorial where explanatory.
- Asset/reference policy: CSS-generated graphic elements only; no third-party logos, screenshots, or stock imagery.
- Anti-default locks: no over-rounded card stack, no generic glassmorphism, no fake testimonials, no repeated slide skeleton.
- Intentional exceptions: Frame 9 uses a dramatic gradient field as a launch close, not a generic page default.

## Graphic Or Print Specs

- Size: 1080 x 1440 px.
- Aspect ratio: 3:4 vertical.
- Color mode: screen RGB/sRGB-oriented export.
- Bleed: none; social image draft.
- Safe area: 54 px internal frame, with bottom palette strip.
- Resolution: PNG screenshots at exact pixel size.
- Export format: PNG frames plus zip bundle.
- Font handling: system fonts only; no embedding.
- Image/font/logo license notes: no third-party imagery or fonts included.

## Review Log

- 2026-07-06: Bootstrapped English-first Xiaohongshu carousel contract and source HTML. Replaced previous X-poster logic with vertical 3:4 carousel, richer explanatory copy, more varied layout archetypes, and type-led art direction.
