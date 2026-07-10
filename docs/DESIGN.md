---
version: alpha
name: Ultimate Design Official Site
description: Bilingual official homepage explaining Ultimate Design as a self-contained, content-first, contract-driven AI design workflow.

colors:
  primary: "#D9281E"
  secondary: "#121B4D"
  tertiary: "#C7F20E"
  neutral: "#0B0E12"
  surface: "#F4EFE4"
  on-surface: "#0B0E12"
  error: "#B3261E"

typography:
  headline-lg:
    fontFamily: "Songti SC, STSong, Hiragino Mincho ProN, Georgia, serif"
    fontSize: 96px
    fontWeight: 800
    lineHeight: 1
  body-md:
    fontFamily: "PingFang SC, Microsoft YaHei, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.72
  label-md:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.15

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px

components:
  primary-button:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
---

# Design System

## Overview

This is the bilingual official homepage for Ultimate Design. The Chinese page is written from Chinese first, not translated from English sentence structure. The English page is a parallel expression for English readers. The site must explain the workflow clearly, state that the skill is self-contained rather than dependent on legacy design skills, let the user switch languages at the top, and preserve the contract-driven design story.

## Colors

Use warm paper, carbon black, cinnabar red, deep indigo, acid chartreuse, and small ochre accents. Black carries contract authority. Red marks intervention, critique, and proof. Chartreuse is used sparingly for live state and validation signals. The palette should feel like an editorial design lab, not a generic SaaS page.

## Typography

Chinese major headings use a Chinese serif voice so the page feels native and editorial. English major headings use Georgia-like serif forms. Body copy uses system sans-serif for legibility. Monospace is reserved for workflow labels, prompt examples, file names, and proof markers. Letter spacing stays 0.

## Layout

The page remains a single long homepage with a top language switch:

- Sticky header with brand, navigation, language switch, and copy CTA.
- First viewport: product name, Chinese or English hero claim, support copy, CTAs, contract-sheet motif, optional reference board, and workflow rail.
- Below-hero proof strip to show the next section.
- Sections: problem diagnosis, four-system explanation, workflow, capabilities, prompt console, proof ledger, final CTA.
- Layout families vary across sections; avoid repeated card-only scaffolding.

## Elevation & Depth

Use paper layers, hard borders, stacked sheets, image panels, and strong section rules. Avoid soft glass, glow effects, and decorative blobs.

## Shapes

Mostly square and contract-like. Small controls may use limited rounding for affordance.

## Components

Components: header, language switch, hero, contract sheet, optional reference board, workflow rail, problem split, system lanes, capability matrix, prompt console, proof ledger, CTA footer.

## Do's and Don'ts

- Do default to Chinese and provide an English switch.
- Do make Chinese copy sound native, concrete, and direct.
- Do keep English as a parallel page, not a literal mirror.
- Do treat reference images as optional user input; do not imply image generation is a standard step.
- Do keep prompt examples copyable in the active language.
- Do not use generic SaaS filler, repeated cards, fake dashboards, purple-blue gradients, glass panels, or language implying dependence on another design skill.

## Agent Execution Rules

- Preserve `CONTENT.md` as the content source and this file as the contract.
- Preserve `assets/imagegen-homepage-reference.png` only as this demo's optional reference-board asset.
- Major user-visible zones must keep `data-ud-check` markers.
- `index.html` must support language switching; `index-en.html` must open the English view.
- Run strict contract validation and rendered HTML visual validation before delivery.

## Request Anchor

- Original user request: Build an official website that explains Ultimate Design from zero.
- Latest user override: The Chinese copy feels too much like translated English. Rewrite from Chinese first and include both Chinese and English pages with a top switch.
- Deliverable: Static bilingual official homepage with `CONTENT.md`, `DESIGN.md`, `index.html`, `index-en.html`, screenshots, and validation report.
- Primary audience: Chinese and English readers evaluating Ultimate Design: agent users, designers, developers, and skill maintainers.
- Core job to be done: Make the skill understandable, credible, and usable; show the workflow and prompt patterns without implying generated images are required.
- Success criteria: Chinese copy reads naturally; English page is available; language switch works; optional reference handling is clear; validators pass; user can review screenshots.
- Non-goals: Do not create a full documentation site, installation manual, or image-generation-first workflow.
- Must preserve: Contract-driven framing, YOLO/Pro mode distinction, optional reference input, critique/repair, rendered verification, DESIGN.md continuity.
- Validation must check against: Request Anchor, bilingual content, active-language copy buttons, visual semantic zones, desktop/mobile screenshots, contract validation.

## Content Model

- User intent: Understand Ultimate Design quickly and learn how to prompt it.
- Business intent: Present Ultimate Design as a durable self-contained design workflow rather than a style prompt, template library, or wrapper around other skills.
- Message hierarchy: 1. Product name and promise. 2. Why AI design fails without process. 3. What the workflow is. 4. How the loop runs. 5. What it can design. 6. How to prompt. 7. What evidence a good run leaves.
- First-screen answers: Ultimate Design turns AI design from generation into traceable, reviewable, verifiable delivery.
- Primary action meaning: Copy the starter prompt in the active language.
- Voice and tone: Chinese is concrete, native, and direct. English is plain, confident, and practical.
- Terminology rules: Use Ultimate Design, DESIGN.md, Request Anchor, Content Contract, Taste Engine, optional reference image, Critique and Repair, Verify and Govern.
- State language rules: Copy buttons briefly report copied or failed state in the active language.
- Trust, risk, and help content: Proof ledger lists the artifacts and checks that make a run reviewable.
- Content risks: Avoid claiming guaranteed expert-level taste. Avoid implying reference images or generated images are mandatory.

## OKF Preflight

### Active OKF Concepts

- `design-okf/content/message-model.md`: make the Chinese and English narratives parallel in meaning without forcing sentence-level translation.
- `design-okf/systems/taste-engine.md`: use varied editorial layout families and explicit anti-default locks so the design workflow is demonstrated rather than merely described.

### Support References

- `references/branch-marketing-site.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/visual-verification.md`
- `references/quality-gates.md`

### Decision Record

- Constraints extracted: content hierarchy leads styling; the page stays bilingual, self-contained, and clear that references are optional.
- Deliberate exceptions: prompt examples may use bordered panels because code-like text needs a stable scanning container.
- Verification hooks: switch both language states, inspect all marked semantic zones at desktop and mobile widths, and run the Rendered UI Audit with a fresh report.

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/content/message-model.md` | Write Chinese from Chinese intent and maintain a parallel English expression instead of literal translation | Hero, systems explanation, workflow, prompts, and the `data-i18n` dictionary | Review both language states for equivalent message hierarchy, native phrasing, CTA meaning, and complete keys |
| `design-okf/systems/taste-engine.md` | Use editorial hero, contract sheet, workflow rail, split diagnosis, system lanes, capability matrix, prompt console, and proof ledger instead of one repeated card family | Section layouts, CSS grid families, Taste Signature, and anti-default locks | Render desktop and mobile states; inspect semantic zones for repetition, collision, crowding, clipping, awkward wraps, and generic AI defaults |

## Information Architecture

- Core user tasks: Understand, compare modes, copy a prompt, inspect proof.
- Page or screen inventory: One bilingual homepage plus an English preview entry file.
- Navigation model: Top anchor navigation with language switch.
- Content hierarchy: Hero, proof strip, why, systems, workflow, capabilities, prompts, proof, CTA.
- Primary CTA rules: Copy prompt. CTA copy must describe the result, not only the action.

## Taste Signature

Use only when the artifact has meaningful visible style freedom:
- Design read: Official site for a design workflow. Audience is technical and design-literate. It needs credibility, clarity, and a visual memory feature without becoming a SaaS template.
- Taste dials: Visual variance 7, information density 7, motion depth 1, brand distinction 8, experiment risk 4.
- Category defaults avoided: Generic centered hero, three-card pitch, fake dashboard preview, purple gradient, glassmorphism, decorative badges.
- Layout families or slide archetypes: Editorial hero, contract sheet, workflow rail, split diagnosis, system lanes, capability matrix, prompt console, proof ledger.
- Visual memory feature: UD black mark plus contract sheet over an optional reference board, with red/chartreuse proof accents.
- Asset/reference policy: Reference images are optional user input. This demo keeps the generated visual only as a local reference-board asset; it is not a standard workflow dependency.
- Anti-default locks: No repeated card scaffold; no fake proof; no image-generation-first framing; no literal translated Chinese.
- Intentional exceptions: Prompt cards use framed panels because code examples need scannable containers.

## Optional Reference Asset

- Source path: `assets/imagegen-homepage-reference.png`
- Role: Experiment-specific visual reference-board asset only.
- Implementation boundary: Use it as a visual element in this demo. Do not describe image generation as required or default.

## Page Or Asset Specs

For each page, screen, or graphic:
- Goal: Bilingual official homepage introduction for Ultimate Design.
- Primary user task: Understand the workflow and copy a starter prompt.
- Primary content: Problem, four systems, workflow, capabilities, prompts, proof.
- Primary CTA: Copy starter prompt in the active language.
- Components or visual modules: Header, language switch, hero, contract sheet, workflow rail, problem split, system lanes, capability matrix, prompt console, proof ledger, CTA.
- Required states: Chinese active, English active, copy success or failure.
- Responsive notes: At mobile widths, hero stacks; language switch remains visible; prompt text wraps; proof ledger stays readable.
- Accessibility notes: High contrast, semantic HTML, alt text, focus states, no critical text only in images, active language marked with `aria-pressed`.
- Analytics or success signal: User can explain Ultimate Design in one sentence and has copied a prompt.

## Quality Gates

- Request Anchor fit: Page now has native Chinese expression and an English page.
- Visual: Semantic zones do not overlap or clip; first viewport shows product and next-section hint.
- Accessibility: Contrast, focus states, image alt, language attributes, real text.
- Responsive: Desktop and mobile screenshots pass validator.
- Interaction: Language switch updates copy and prompt text; copy buttons use active-language text.
- Performance: Single static HTML plus one local PNG; no external dependencies.
- Print or export: Not applicable.
- I18n/legal: Chinese and English both use readable sizes; mixed-language text does not overflow.
- Contract consistency: DESIGN.md must pass strict validator.

## Implementation And Governance

- CSS architecture: Single static `index.html` with CSS variables, semantic classes, and no external dependencies.
- Language implementation: Default Chinese; JavaScript dictionary switches visible copy to English; `index-en.html` opens `index.html?lang=en`.
- Token implementation: CSS variables mirror DESIGN.md.
- Component naming: Names reflect content modules.
- State naming: `data-lang-button`, `data-copy`, and copy status.
- Theme strategy: Light editorial lab theme.
- Dark mode: Not required.
- Framework notes: None.
- Performance budget: One local image asset; no external scripts.
- Visual regression: Use bundled `validate_html_visual.mjs`.
- Accessibility testing: Rendered inspection plus semantic review.
- CI checks: Not configured.

## Assumptions

- The site is a local static HTML proof, not a deployed production domain.
- English is for product-facing international readers, not a literal translation audit.

## Open Questions

- Whether the public version should include installation sections for Codex, Claude Code, and Pi Agent.

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| 0.6 | 2026-07-10 | Updated the public knowledge lane for 0.4 decision-bound OKF and verification | The official site should explain that routed knowledge must change the artifact and its checks | Codex |
| 0.5 | 2026-07-08 | Updated homepage copy for 0.2 necessary judgment, motion, type, and stricter rendered verification | Public site should reflect the released skill capabilities without redesigning the whole page | Codex |
| 0.4 | 2026-07-07 | Updated public positioning to say Ultimate Design is self-contained, not a wrapper around legacy design skills | Public homepage and package copy should match the cleaned skill architecture | Codex |
| 0.3 | 2026-07-04 | Reworked site into Chinese-first bilingual homepage with top language switch | User found previous copy too translation-like and requested Chinese/English pages | Codex |
| 0.2 | 2026-07-04 | Removed experimental generated-reference framing and clarified optional reference-image handling | Keep the demo from misrepresenting Ultimate Design's standard workflow | Codex |
| 0.1 | 2026-07-04 | Created official site contract from finalized content and an experiment-specific visual reference | Explore a content-first Ultimate Design website demo | Codex |
