# Principles Router

Use this router when bootstrapping a design contract from zero, when no design system exists, when the user asks for professional or senior design judgment, or when the design direction needs stronger rationale.

Do not load the whole research base by default. Open `design-okf/index.md`, choose the relevant concepts, then read only those concept files.

The OKF bundle is descriptive knowledge, not runtime truth. It informs design decisions, but browser rendering, accessibility checks, tests, print specs, and user review remain authoritative.

Start here:

- `design-okf/index.md` for the bundle map.
- `design-okf/methods/senior-design-process.md` when creating a new `DESIGN.md` or design direction from scratch.
- `design-okf/methods/product-sense.md` only when product problem, user outcome, success signal, scope, prioritization, business/user tradeoff, or validation remains unresolved enough to change the design. Product UI alone is not a trigger.
- `design-okf/production/presentation-deck.md` when designing or auditing PPT/PowerPoint/Google Slides/Keynote decks, executive or board presentations, pitch decks, training decks, or slide templates.
- `design-okf/governance/request-integrity.md` when the task is long, content-heavy, multi-file, likely to exceed short-term attention, or when final validation must prove the artifact still answers the user's original request.
- `design-okf/governance/research-digestion-llm-wiki.md` when absorbing deep research, building a wiki-like synthesis layer, auditing coverage, or promoting raw knowledge into OKF. Do not load it during ordinary design execution.
- `design-okf/governance/design-md-standard.md` and `design-okf/governance/design-md-agent-governance.md` when the task creates, updates, audits, or validates a root `DESIGN.md`.
- `content-model.md` before layout or styling when the artifact has meaningful text, UX writing, reports, forms, component states, or localization.
- `design-okf/foundations/visual-communication-hierarchy.md` before choosing layout/style when the artifact must communicate a message, direct attention, explain data, guide reading, or drive action.
- `design-okf/foundations/layout-typography-composition.md` before detailed layout, type, grid, spacing, editorial, Swiss Style, Chinese typography, or mixed Chinese-English typesetting work.
- `design-okf/systems/brand-identity-media-production.md` when the task needs brand identity, logo rules, brand guidelines, VI manuals, cross-media brand kits, screen/print/social/PPT/packaging delivery, asset naming, licensing, rights, or brand governance.
- `design-okf/systems/visual-language-style-system.md` when the task needs art direction, recognizable visual style, color/image/icon/illustration/texture/symbol coherence, anti-template checks, or a reusable style guide.
- `design-okf/systems/taste-engine.md` as the default taste layer for visible artifacts with style freedom; load it fully when work risks looking generic, card-heavy, template-like, or AI-generated, or when the user asks for taste, originality, style confidence, layout variety, stronger color/type personality, or anti-slop critique.
- `design-okf/foundations/necessary-design-judgment.md` when the user asks for design philosophy, taste, Apple/Jony Ive/Rams/Hara-style judgment, or senior critique, and when a visible artifact feels styled-but-not-inevitable, fake-minimal, overdecorated, template-like, or surface-premium. Use it to test necessity, inevitability, craft tolerance, care, material honesty, and scene fit before styling hardens.
- `design-okf/systems/motion-language.md` when the artifact includes meaningful animation, microinteractions, page transitions, scroll storytelling, animated HTML decks, or a motion-depth taste dial above static.
- `design-okf/systems/motion-contract.md` when animation is a requested feature or delivery claim, especially SVG line/border drawing, scroll-linked or scrubbed animation, reveal choreography, GSAP/ScrollTrigger work, or motion validation requirements.
- `design-okf/systems/type-personality.md` when font choice or Chinese/English family pairing is part of the art direction, type carries visual memory, families are changing, or WebFont size, fallback, font rights, deck portability, or CJK coverage can affect delivery. Mixed-script layout mechanics alone route to `typography-system.md`.
- `design-okf/foundations/information-architecture.md` before designing any page, screen, or graphic.
- `design-okf/foundations/gestalt-composition.md` when grouping, focal path, alignment, figure/ground, or composition feels unclear.
- `design-okf/foundations/visual-hierarchy.md` when primary, secondary, and tertiary emphasis cannot be identified at a glance.
- `design-okf/systems/color-system.md` when creating or materially changing palette roles, themes, semantic color, or chart color.
- `design-okf/systems/typography-system.md` when type scale, line length, line height, overflow, optical sizing, or user text scaling needs explicit rules.
- `design-okf/digital/accessibility-usability.md` for interactive digital surfaces, forms, keyboard/focus work, accessibility review, or consequential states.
- `design-okf/digital/responsive-interaction.md` for multi-device layout, tables, sticky/fixed UI, gestures, or adaptive interaction states.
- `design-okf/production/data-viz-i18n-legal.md` when data, localization, RTL, claims, citations, or legal/licensing risk affects the artifact.
- `design-okf/governance/design-to-code-governance.md` when a design system must survive implementation, Storybook, regression tests, or CI.
- `design-okf/governance/machine-verification-ci.md` when contract/token checks or automated release gates are part of delivery.
- `design-okf/governance/senior-proxy-checklist.md` before claiming professional quality.
