---
version: 0.7
name: Ultimate Design Official Site
description: Bilingual official homepage that explains Ultimate Design through concrete design work, not abstract claims or template-like product copy.

colors:
  primary: "#DF3A22"
  secondary: "#0E6E6B"
  tertiary: "#D7DE49"
  neutral: "#10120E"
  surface: "#F2F3EE"
  on-surface: "#10120E"
  error: "#B3261E"

typography:
  headline-lg:
    fontFamily: "Songti SC, STSong, Hiragino Mincho ProN, Georgia, serif"
    fontSize: 88px
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

This is the bilingual official homepage for Ultimate Design. It explains what a user gets from one design run: a clear request, a real artifact, a rendered review, and a record that can be continued. Chinese is written from Chinese intent; English is a parallel expression rather than a sentence-by-sentence translation.

## Colors

Use a cool off-white field, carbon ink, signal red, restrained teal, and a small chartreuse accent. The page should feel like a working design notebook: clear enough to read for several minutes, with color used to mark decisions rather than decorate empty space. Avoid beige paper nostalgia, gradients, glows, and multicolor competition.

## Typography

Chinese display headings use Songti for an editorial, deliberate voice; body and UI text use a durable sans-serif. English headings use a serif voice with a direct, short sentence structure. Monospace is reserved for prompts, small labels, file names, and compact process markers. Most type stays quiet; display type appears only where the reading path needs a real pause.

## Layout

The page is a single, bilingual scrolling homepage with a compact top language switch.

- Hero: a short promise on the left and one concrete run record on the right.
- Problem: three plain observations about where a seemingly finished design breaks down.
- Handoff: request anchor, `DESIGN.md`, and rendered review as three visible outputs.
- Workflow: five numbered actions, not a ceremonial eight-step rail.
- Capability list: a quiet matrix of media and jobs.
- Prompt area: one normal prompt and one `--pro` prompt.
- Final handoff: a compact list of what leaves the run and a single CTA.

No decorative strip, duplicate workflow rail, faux dashboard, or repeated framed-card section. Each section changes the reader's understanding or is removed.

## Elevation & Depth

Use flat rules, one lightly offset working sheet, and a single image thumbnail for optional reference input. Depth should clarify layers of work, not create a collage.

## Shapes

Mostly square, with thin rules and modest radii for controls. Use larger empty space between sections than inside components.

## Components

Header, language switch, hero run record, observation list, handoff trio, five-step workflow, capability matrix, prompt console, delivery checklist, and footer.

## Do's and Don'ts

- Do make Chinese copy concrete, idiomatic, and willing to name limits.
- Do let English be independently written, not mechanically translated.
- Do show the artifacts a run leaves, not only the ideals behind them.
- Do keep optional reference input visibly optional.
- Do keep prompts short enough to copy and adapt.
- Do not use “不是……而是……” as the page's recurring rhythm.
- Do not rely on “体系、升级、赋能、专业、品质、重要” without a concrete consequence.
- Do not repeat the same claim in hero, process, proof, and CTA.
- Do not use a generated image as proof of a product capability.

## Agent Execution Rules

- Preserve `CONTENT.md` as the content source and this file as the contract.
- Treat `assets/imagegen-homepage-reference.png` as an optional reference-input thumbnail only; it must not dominate the hero or imply a required image-generation step.
- Major user-visible zones must keep sparse `data-ud-check` markers.
- `index.html` supports language switching; `index-en.html` opens `index.html?lang=en`.
- Run strict contract validation and rendered HTML visual validation before delivery.

## Request Anchor

- Original user request: Improve the Ultimate Design official website, which feels cluttered and has AI-sounding copy; learn from the supplied Chinese editing research.
- Latest user override: Remove vague, performative, and self-congratulatory language. Keep the public homepage simple and clear.
- Deliverable: Revised static bilingual homepage with updated `CONTENT.md`, `DESIGN.md`, `index.html`, `index-en.html`, screenshots, and validation report.
- Primary audience: People evaluating whether to use Ultimate Design with an AI coding agent.
- Core job to be done: Understand the practical difference between a one-off generated page and a design run that can be inspected, revised, and handed off; start with an appropriate prompt.
- Success criteria: A reader can state what Ultimate Design leaves behind, see how a run moves, copy a prompt, and read Chinese or English without generic AI-product language.
- Non-goals: Do not create a documentation portal, claim expert credentials, compare against other skills, or turn the page into a visual manifesto.
- Must preserve: Bilingual switch, `DESIGN.md` continuity, default and `--pro` modes, optional reference input, critique/repair, rendered review, accessible static HTML.
- Validation must check against: Request Anchor, bilingual semantic parity, copy actions, desktop/mobile reading path, semantic zones, clipping/overflow, and contract validation.

## Content Model

- User intent: Understand the skill quickly and decide how to start using it.
- Business intent: Explain a concrete working method without exaggerated product positioning.
- Message hierarchy: 1. What a completed run leaves behind. 2. Why a visually finished page can still be incomplete. 3. The three working artifacts. 4. The five actions. 5. Where it applies. 6. How to start. 7. What handoff contains.
- First-screen answers: Ultimate Design helps an Agent make the design and preserve the judgement behind it.
- Primary action meaning: Copy a short starter prompt in the active language.
- Voice and tone: Precise, calm, editorial, and specific. Chinese may be conversational where it improves clarity; English is plain and uninflated.
- Terminology rules: Use Ultimate Design and `DESIGN.md` consistently. Explain Request Anchor and rendered review in ordinary language before using their labels.
- State language rules: Copy controls report success or failure in the active language, briefly.
- Trust, risk, and help content: State what is saved, what is optional, and what cannot be claimed without rendered evidence.
- Content risks: Repeated contrast formulas, moralizing about “AI taste”, generic nouns, unsupported expertise claims, literal translation, and invented proof.

## OKF Preflight

### Active OKF Concepts

- `design-okf/content/message-model.md`: put the reader's concrete job and the resulting artifacts ahead of feature taxonomy.
- `design-okf/content/ux-writing.md`: replace abstract labels and product-speak with short, useful UI and CTA language.
- `design-okf/systems/taste-engine.md`: reduce recurring section patterns and create one coherent reading rhythm rather than a collage of visual ideas.
- `design-okf/foundations/necessary-design-judgment.md`: remove visual and verbal elements that do not clarify trust, task, or identity.

### Support References

- `references/branch-marketing-site.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/visual-verification.md`
- `references/quality-gates.md`
- User-supplied editing research on reducing template-like, abstract non-fiction copy.

### Decision Record

- Constraints extracted: write for a skeptical reader; each section must add a fact, action, boundary, or visible artifact; no fictitious metrics, customer stories, or outcome claims.
- Deliberate exceptions: prompts and file names retain technical language; the optional reference thumbnail remains as a small, labelled example because it explains a real input path.
- Verification hooks: compare source and rewritten copy for abstract/template language; inspect Chinese and English states; run contract, OKF usage, rendered UI, and manual screenshot review.

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/content/message-model.md` | Lead with the usable outcome and organize the page around request, artifact, and handoff | Hero, handoff trio, workflow, delivery checklist, `CONTENT.md` | First viewport answers what the user gets; section order matches the declared hierarchy in both languages |
| `design-okf/content/ux-writing.md` | Use concrete nouns and actions, remove generic product claims, and shorten CTA/prompt copy | `data-i18n` dictionary, nav, CTA, prompts, labels | Manual copy review checks for repetition, abstract filler, unsupported claims, and literal translation |
| `design-okf/systems/taste-engine.md` | Use a quieter layout budget with one hero record, one observation band, one workflow, and one utility area | CSS layout families, section structure, type scale, color area | Desktop/mobile screenshots show clear dominance, no decorative repetition, and no card-stack sameness |
| `design-okf/foundations/necessary-design-judgment.md` | Delete duplicate strips, oversized statements, decorative layers, and claims that do not add trust or comprehension | Hero composition, section count, copy, optional image placement | Second critique names what was removed and confirms remaining elements have a task, trust, or identity reason |

## Information Architecture

- Core user tasks: Understand the method, assess fit, choose normal or `--pro` mode, copy a prompt, understand what arrives at handoff.
- Page or screen inventory: One bilingual homepage plus an English entry file.
- Navigation model: Compact anchors for method, uses, prompts, and handoff; top language switch.
- Content hierarchy: Hero, observations, outputs, workflow, uses, prompts, handoff, CTA.
- Primary CTA rules: Copy a prompt that describes the user's job, not the site's internal procedure.

## Taste Signature

Use only when the artifact has meaningful visible style freedom:
- Design read: A calm editorial workbench for an agent design method, not a campaign page or a software dashboard.
- Necessary judgment: Remove anything that explains the same idea twice; reserve emphasis for the reader's next decision.
- Taste dials: Visual variance 4, information density 5, motion depth 0, brand distinction 6, experiment risk 3.
- Category defaults avoided: Giant product slogan, stacked feature cards, faux product dashboard, purple gradient, code-terminal cosplay, decorative post-it notes, and anti-AI rhetoric as decoration.
- Layout families or slide archetypes: Editorial hero with run record, three-output list, numbered workflow, quiet capability matrix, prompt console, delivery checklist.
- Visual memory feature: A red edit mark beside a black-and-white run record on a cool field.
- Type personality: Editorial display with quiet utility text; Chinese-first optical pairing.
- Asset/reference policy: The supplied reference image appears once as an optional input thumbnail, not as a promise or product screenshot.
- Anti-default locks: One main idea per section; no repeated full-width card bands; no claim without a corresponding artifact or boundary; no decorative animation.
- Intentional exceptions: Prompt examples use a dark code surface because copying and scanning benefit from a stable contrast field.

## Optional Reference Asset

- Source path: `assets/imagegen-homepage-reference.png`
- Role: Small example of optional visual reference input.
- Implementation boundary: Never present it as a live product screenshot, a required asset, or proof of an image-generation workflow.

## Page Or Asset Specs

- Goal: Make the official site clearer, quieter, and more credible through concrete content and a focused reading path.
- Primary user task: Understand the method and copy a starting prompt.
- Primary content: Outcome, common breakdowns, three outputs, five actions, applicable work, prompts, delivery checklist.
- Primary CTA: Copy starter prompt in the active language.
- Components or visual modules: Header, language switch, hero run record, observation list, handoff trio, workflow, capability matrix, prompt console, delivery checklist, CTA.
- Required states: Chinese active, English active, copy success, copy failure.
- Responsive notes: Desktop uses a two-column hero and concise columns; mobile becomes a single reading column without losing hierarchy or making the prompt console cramped.
- Accessibility notes: High contrast, semantic headings/lists/buttons, real text, descriptive image alt, focus states, active language marked with `aria-pressed`, comfortable target sizes.
- Analytics or success signal: A reader can describe the three outputs and copies a prompt appropriate to their task.

## Quality Gates

- Request Anchor fit: The page addresses clutter and AI-sounding copy without introducing new claims.
- Content: Every section adds a concrete artifact, action, boundary, or consequence; duplicate explanations are removed.
- Copy: No invented metrics, customers, case studies, or model credentials; no literal Chinese-to-English translation; no repeated “not X but Y” framing.
- Visual: Hero dominates once; sections have distinct jobs; semantic zones do not overlap, clip, or create horizontal overflow.
- Accessibility: Contrast, focus states, language attributes, real text, alt text, readable type, and target sizing pass review.
- Responsive: Chinese and English desktop/mobile states have a coherent reading order and no awkward overflow or density spike.
- Interaction: Language switch and copy buttons work in the active language.
- Performance: Static HTML, one local image, no external dependencies, no decorative motion.
- Print or export: Not applicable.
- Contract consistency: `DESIGN.md` passes strict validation and active OKF concepts pass decision-binding validation.

## Implementation And Governance

- CSS architecture: One static `index.html` with CSS variables, semantic class names, and no external dependencies.
- Language implementation: Chinese default; JavaScript dictionary switches content; `index-en.html` opens `index.html?lang=en`.
- Token implementation: CSS variables mirror the front matter.
- Component naming: Names reflect content modules and semantic zones.
- State naming: `data-lang-button`, `data-copy`, copy status, and `data-ud-check` zones.
- Theme strategy: Cool editorial workbench with red intervention and restrained teal/chartreuse accents.
- Dark mode: Not required.
- Framework notes: None.
- Performance budget: One local image asset; no external scripts or fonts.
- Visual regression: Use bundled `validate_html_visual.mjs` and inspect the screenshot set.
- Accessibility testing: Rendered inspection plus semantic review.
- CI checks: Not configured.

## Assumptions

- The site remains a static GitHub Pages artifact.
- The editing research is used as an editorial lens, not as an AI-detector target or a source of universal numeric thresholds.
- English readers value a plain parallel explanation more than literal equivalence with Chinese wording.

## Open Questions

- None for this revision.

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| 0.7 | 2026-07-11 | Reframed the homepage around concrete outputs, five actions, and quieter editorial copy | User found the page cluttered and the copy AI-sounding; the new content contract removes repetition and abstract product language | Codex |
| 0.6 | 2026-07-10 | Updated the public knowledge lane for decision-bound OKF and verification | The official site should explain that routed knowledge must change the artifact and its checks | Codex |
