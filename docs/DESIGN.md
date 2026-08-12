---
version: 1.0
name: Ultimate Design Official Site
description: Bilingual showcase homepage that proves the skill's design capability with the page itself - a gallery of complete demo pages designed by agents running the skill, a searchable knowledge explorer, and honest repository-sourced numbers.

colors:
  primary: "#DF3A22"
  secondary: "#0E6E6B"
  tertiary: "#D7DE49"
  neutral: "#F2F3EE"
  surface: "#10120E"
  on-surface: "#F2F3EE"
  error: "#FF8A70"

typography:
  headline-lg:
    fontFamily: "Fraunces, Noto Serif SC, Songti SC, STSong, Georgia, serif"
    fontSize: 84px
    fontWeight: 600
    lineHeight: 1.04
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

This is the bilingual official showcase homepage for Ultimate Design, served from `docs/` on GitHub Pages. Version 0.9 replaces the quiet editorial page (0.7) with a capability showcase: the page must demonstrate design range, not only describe it. The proof devices are a demo gallery of twelve complete pages under `docs/demos/` - each designed by a worker agent running this very skill and shipped with its own `DESIGN.md` contract - plus a searchable OKF knowledge explorer, an interactive five-step run record, and a meta strip that points back to this contract. Chinese is the default language; English is a parallel expression.

The direction is a **studio desk at night**: a deep ink field (the desk), light paper sheets carrying the run artifacts, red annotation marks, and restrained teal/chartreuse instrument accents. This keeps the 0.7 brand genes (ink, paper, signal red, teal, chartreuse, editorial serif) while flipping the value: dark field, light artifacts.

## Colors

- `--desk` `#10120E`: page field. `--desk-raised` `#181B15`: panels, cards on desk. Hairlines on desk: `rgba(242,243,238,0.14)`.
- `--paper` `#F2F3EE`: artifact sheets (run record, contract snippets). Ink on paper: `#10120E`.
- `--red` `#DF3A22`: annotation marks, rules, display accents, large numerals. Contrast on desk is about 3.6:1, so red is reserved for large text (at least 24px bold) and graphics; never body-size text on the desk.
- Small-text emphasis on the desk uses `--chartreuse` `#D7DE49` or `--teal-light` `#7FC8C3` (a lightened instrument variant of `#0E6E6B` for dark-field legibility).
- Body text on desk: `#E9EBE3`; muted text on desk: `#A9AEA1` (both at or above 4.5:1). On paper, muted ink: `#5B5F55`.
- No purple/blue SaaS gradients, no neon glow, no aurora backgrounds. The only permitted texture is a blueprint grid on the desk at 4% alpha or lower.

## Typography

Display type is a serif pair chosen as art direction: Fraunces for Latin, Noto Serif SC for Chinese, loaded from Google Fonts with `display=swap`, at most two weights per family, and full system fallbacks (Songti SC, STSong, Georgia, serif) that must keep the layout intact if the network fails. Body and UI text use the system sans stack. Monospace is reserved for file paths, stats, prompts, install commands, and small process labels. Display type appears in the hero, section openers, and gallery card names; everything else stays quiet.

## Layout

One bilingual scrolling homepage with a sticky top bar (brand, four anchors, language switch, GitHub link).

- Hero: display claim and lead on the left; an auto-cycling run-record paper card on the right; a six-item mono stat strip below. Stats come only from the Real Inventory table in `CONTENT.md`.
- Why: three plain observations, one row.
- Outputs: three paper artifact cards (Request Anchor, `DESIGN.md`, Rendered review), each with a real sample fragment.
- Workflow: five clickable steps; the active step reveals one miniature artifact. No scroll hijacking.
- Knowledge explorer: search input, nine domain filter chips, result counter, and a card grid of all 54 entries (35 OKF concepts plus 19 branch playbooks) with real file paths and faithful one-line summaries. This is the only high-density zone on the page.
- Demo gallery: twelve cards for the complete demo pages under `docs/demos/<slug>/`, one per design language and surface (marketing, brand site, product UI, landing, HTML deck, portfolio, conference, e-commerce PDP, hardware product, publication, data report, exhibition). Each card shows a live scaled-iframe thumbnail (lazy, `aria-hidden`, non-interactive), name, category chip, style line, language tag, and three actions: open the page in a new tab, copy the reproducing prompt, open that demo's `DESIGN.md`. A one-line note states the demos were designed by agents running this skill and that all brands are fictional.
- Modes and routes: three collaboration modes, four task-route chips.
- Start: three host install tabs with copy buttons; two prompts (default and `--pro`) with copy buttons.
- Delivery checklist plus one GitHub CTA.
- Meta strip: the self-bootstrap statement linking to `docs/DESIGN.md` and `docs/CONTENT.md` on GitHub.
- Footer: license, repository, npm, integrations, language switch.

Each section changes the reader's understanding or is removed. The hero dominates once; no later section may compete with it.

## Elevation & Depth

The desk is flat and uses hairlines. Paper sheets are the only elevated objects: a soft shadow (`0 12px 32px rgba(0,0,0,0.35)` or lighter) and at most 0.6 degrees of rotation on at most two sheets. Specimens sit in flat frames with hairline borders and a mono caption bar. No stacked glows, no floating blobs.

## Shapes

Mostly rectangular with `sm`-`md` radii on controls and cards. Red annotation strokes (underlines, circles, margin ticks) are hand-placed accents, used at most once per section. Filter chips use `full` radius. Thin rules separate sections; empty space between sections is larger than any padding inside components.

## Components

Sticky header, language switch (`aria-pressed`), hero run-record card (5 phases, clickable, auto-advance with pause on hover, static under reduced motion), mono stat strip, observation list, artifact trio, workflow stepper, OKF explorer (search + chips + counter + cards + empty state), demo gallery (12 cards with live iframe thumbnails and view/copy-prompt/contract actions), mode cards, route chips, install tabs with copy buttons, prompt console with copy buttons, delivery checklist, meta strip, footer.

## Do's and Don'ts

- Do keep every page number traceable to the Real Inventory table in `CONTENT.md`.
- Do present demos honestly: fictional brands, designed-by-an-agent-running-this-skill caption, live iframe thumbnails rather than doctored screenshots, and a visible link to each demo's own `DESIGN.md`.
- Do keep the explorer summaries faithful to their source files.
- Do keep Chinese copy concrete and idiomatic; English is parallel, not literal.
- Do keep red for large marks and graphics; body-size emphasis on the desk uses chartreuse or light teal.
- Do not use purple/blue gradient heroes, glow cards, emoji icons, or stock illustration.
- Do not fabricate metrics, customers, demos, or testimonials.
- Do not add scroll hijacking, parallax storytelling, or motion longer than 400ms.
- Do not clone the reference site's visual signature (its fonts, palette, glow-card system); only its proven mechanisms (stat strip, searchable database, pipeline demo, copyable commands) are adapted.

## Agent Execution Rules

- `CONTENT.md` is the content source and this file is the contract; update both when the page changes.
- Major user-visible zones keep sparse `data-ud-check` markers: `navigation`, `hero-title`, `hero-lead`, `hero-run-record`, `stat-strip`, `observations`, `artifact-trio`, `workflow`, `okf-explorer`, `demo-gallery`, `modes`, `install-tabs`, `prompt-console`, `delivery`, `meta-strip`, `footer`.
- Animated zones carry `data-ud-motion` markers coupled to their implementation selectors.
- `index.html` supports language switching; `index-en.html` opens `index.html?lang=en`; `<html lang>` updates on switch.
- The OKF explorer data is inlined as JSON inside the page; no runtime network requests beyond Google Fonts.
- Run strict contract validation, OKF usage validation, and rendered visual review before delivery.

## Request Anchor

- Original user request: Build a showcase page for this repository similar to ui-ux-pro-max-skill.nextlevelbuilder.io, demonstrating design capability, servable as the GitHub Pages site; the orchestrator plans, Kimi K3 workers implement.
- Latest user override: Expand the gallery to twelve demos with maximally distinct style families and scenarios; new directions come from mechanism extraction of well-designed reference archetypes (Study route, no signature cloning); workers run this skill end to end and every demo keeps its own `DESIGN.md`.
- Deliverable: Redesigned static bilingual homepage - `docs/index.html`, six demo pages with contracts under `docs/demos/`, updated `docs/CONTENT.md` and `docs/DESIGN.md`, validation results, and rendered screenshots.
- Primary audience: Developers and design engineers evaluating whether to install the skill into their coding agent; GitHub visitors arriving from the README or npm.
- Core job to be done: Within about a minute, understand what the skill does, what a run leaves behind, and how to install it - and see evidence of design capability on the page itself.
- Success criteria: A reader can name the three outputs and five steps, copy an install command and a prompt, filter the 54-entry knowledge explorer, open any of the six demos and its contract, and read either language; homepage and demos pass contract and OKF validation plus rendered review at mobile and desktop widths.
- Non-goals: No documentation portal, no cloning of the reference site's visual identity, no fabricated numbers or demos, no build toolchain, no dark/light theme toggle.
- Must preserve: Bilingual switch mechanism (`index-en.html` opens `?lang=en`), GitHub Pages `docs/` publishing path, MIT and repository links, brand claim and color genes (ink, paper, signal red, teal, chartreuse), framework-free static HTML.
- Validation must check against: Request Anchor fit, stat accuracy against the repository inventory, bilingual semantic parity, copy rules, semantic zones, dark-field contrast, reduced-motion behavior, mobile reading path, and the bundled validators.

## Content Model

- User intent: Judge quickly whether this skill improves their agent's design output, then install it.
- Business intent: Show capability with evidence the repository can back - knowledge inventory, method, and in-page craft.
- Message hierarchy: 1. What the skill builds and keeps (claim plus run record). 2. Proof inventory (stats). 3. Why unreviewed pages fail. 4. The three outputs. 5. The five steps. 6. The knowledge base itself. 7. Complete demo pages. 8. Modes and routes. 9. Install and prompts. 10. Delivery and self-bootstrap proof.
- First-screen answers: What it is, what a run leaves behind, how to install, and the true size of the bundled knowledge.
- Primary action meaning: Copy the install command for your host; secondarily, copy a starter prompt.
- Voice and tone: Confident, concrete, editorial; willing to name limits; never salesy.
- Terminology rules: Ultimate Design, `DESIGN.md`, Request Anchor, OKF, rendered review are used consistently and explained in plain language on first use.
- State language rules: Copy buttons report success or failure briefly in the active language; the explorer reports its live result count and a clear empty state.
- Trust, risk, and help content: The meta strip names the page's own contract files; the demo gallery states that its pages were designed by agents running this skill, that thumbnails are live renders, and that all brands are fictional; stats cite countable inventory only.
- Content risks: Fabricated numbers, over-claiming ("world-class"), literal translation, decorating with the competitor's signature, and letting the explorer summaries drift from source files.

## OKF Preflight

### Active OKF Concepts

- `design-okf/content/message-model.md`: lead with what a run leaves behind and order sections value, proof, method, library, range, start.
- `design-okf/content/ux-writing.md`: concrete nouns, verb CTAs, honest stat labels, bilingual parallel writing.
- `design-okf/systems/taste-engine.md`: one coherent studio-desk-at-night direction with explicit anti-default locks.
- `design-okf/systems/type-personality.md`: serif display pairing as art direction with safe CJK fallback.
- `design-okf/systems/color-system.md`: dark-field contrast roles; red restricted to large marks.
- `design-okf/systems/motion-language.md`: entry-play reveals and micro-interactions with a hard reduced-motion fallback.
- `design-okf/foundations/visual-communication-hierarchy.md`: one dominant hero, one high-density zone, single-job sections.
- `design-okf/foundations/necessary-design-judgment.md`: every showcase element must demonstrate a named capability or be removed.
- `design-okf/digital/accessibility-usability.md`: WCAG AA on a dark field, focus states, target sizes, language attributes.
- `design-okf/digital/responsive-interaction.md`: the explorer and gallery must degrade to a clean single column.

### Support References

- `references/branch-marketing-site.md`
- `references/reference-study.md` (mechanism extraction from the competitor site; no signature transfer)
- `references/composition-search.md`
- `references/content-model.md`
- `references/design-contract.md`
- `references/multi-agent-mode.md` (this run: Integrator plans, worker agents implement)
- `references/visual-verification.md`
- `references/quality-gates.md`

### Decision Record

- Constraints extracted: page numbers must be countable in the repository; demo thumbnails must be live renders of the actual pages under `docs/demos/`, with fictional brands and per-demo `DESIGN.md` contracts; dark field must hold WCAG AA for text roles; single static HTML file with inline data; Google Fonts is the only external dependency; motion must be transform/opacity, 400ms or less, and fully removable.
- Deliberate exceptions: Google Fonts breaks the 0.7 "no external fonts" rule because display type is a core showcase device here; the fallback stack must keep the layout usable. The explorer is allowed higher density than any other zone because it demonstrates the real knowledge inventory.
- Verification hooks: strict contract validation; OKF usage validation; rendered screenshots at 375, 768, and 1440 widths in both languages; reduced-motion pass; copy-button behavior; explorer count equals 54 and filters correctly; stat strip cross-checked against `ls` counts.

## OKF Decision Bindings

| Reference | Decision | Artifact target | Verification |
|---|---|---|---|
| `design-okf/content/message-model.md` | Hero answers what the skill builds and keeps; sections run value, proof, method, library, range, start | Hero, stat strip, section order, `CONTENT.md` | First viewport answers what/for-whom/how-to-start; section order matches the declared hierarchy in both languages |
| `design-okf/content/ux-writing.md` | Stat labels name countable objects; CTAs are verbs; no product-speak; English written in parallel | Stat strip, CTAs, i18n dictionary, prompts | Copy review against `CONTENT.md` rules; every number traced to the Real Inventory table |
| `design-okf/systems/taste-engine.md` | Studio-desk-at-night direction: ink field, paper artifacts, red marks; locks against gradient-glow SaaS defaults and competitor signature | Global theme tokens, hero composition, gallery plates | Screenshots show a distinct identity; anti-default locks and the no-clone rule hold |
| `design-okf/systems/type-personality.md` | Fraunces plus Noto Serif SC display pairing with two weights each and full system fallback | Font loading, headings, gallery card names | Page renders acceptably with fonts blocked; FOUT controlled via `display=swap`; weights limited |
| `design-okf/systems/color-system.md` | Red reserved for large marks and graphics; small emphasis uses chartreuse or light teal; muted roles defined for desk and paper | CSS custom properties, text roles | Contrast checks: body 4.5:1 or better, large display 3:1 or better, on both desk and paper |
| `design-okf/systems/motion-language.md` | Entry-play reveals, run-record auto-cycle with hover pause, micro-interactions only; static-first; hard reduced-motion fallback | `data-ud-motion` zones, IntersectionObserver script | Reduced-motion audit shows no animation; durations 400ms or less; transform/opacity only |
| `design-okf/foundations/visual-communication-hierarchy.md` | One dominant hero; the explorer is the only dense zone; each section has a single job | Layout rhythm, section scaffolding | Full-page screenshots show no section competing with the hero and no duplicate section jobs |
| `design-okf/foundations/necessary-design-judgment.md` | Twelve complete demos maximum, each shipping its own `DESIGN.md` and claiming a distinct style family; any gallery element that demonstrates nothing is deleted | Demo gallery, hero desk texture, ornament budget | Critique pass names what was cut and confirms every remaining element demonstrates a capability |
| `design-okf/digital/accessibility-usability.md` | Semantic landmarks, `aria-pressed` language switch, focus-visible styles, 44px targets, real text everywhere | Header, controls, explorer, tabs | Keyboard walkthrough plus contrast pass; zones visible and unoccluded in rendered audit |
| `design-okf/digital/responsive-interaction.md` | Explorer chips wrap and cards stack on mobile; gallery cards go single column; hero paper card moves below the claim | Grid rules, breakpoints at 375/768/1024/1280 | Rendered checks at 375, 768, 1440 in both languages show a clean reading path and no horizontal overflow |

## Information Architecture

- Core user tasks: Understand the method, verify the inventory is real, judge design range, choose a mode, copy install command and prompt.
- Page or screen inventory: One bilingual homepage plus the English entry redirect.
- Navigation model: Sticky anchors for method, knowledge, range, start; language switch; GitHub link.
- Content hierarchy: Hero with run record and stats, observations, outputs, workflow, explorer, range, modes, start, delivery, meta strip.
- Primary CTA rules: Copy actions state what they copy; the GitHub CTA appears once in the header and once at delivery.

## Taste Signature

- Design read: A working design studio photographed at night - dark desk, lit paper artifacts, red editor's marks - not a SaaS landing page.
- Necessary judgment: Every decorative candidate must demonstrate a named capability (type, color, motion, layout, data); otherwise it is cut.
- Taste dials: Visual variance 7, information density 6, motion depth 2, brand distinction 8, experiment risk 5.
- Category defaults avoided: Purple/blue gradient hero, glow cards, emoji icon rows, fake dashboard screenshots, testimonial walls, animated counters that fabricate scale.
- Layout families: Editorial display hero with instrument panel, paper artifact cards, stepper rail, filterable card grid, live demo plates, tabbed console.
- Visual memory feature: Light paper sheets with red annotation marks on a deep ink desk, and twelve live demo plates proving range.
- Type personality: Editorial serif display (Fraunces with Noto Serif SC) over quiet system sans, mono for instrument labels; Chinese-first optical pairing.
- Asset/reference policy: No raster imagery; everything is typeset or drawn with CSS. The retired `assets/imagegen-homepage-reference.png` stays in the repository but is no longer rendered.
- Anti-default locks: One main idea per section; no repeated full-width card bands; no claim without a countable source; no decorative animation; no competitor signature transfer.
- Intentional exceptions: Prompts and install commands sit on paper-inverse (near-black) code surfaces for copy affordance; the explorer runs denser than the rest of the page by design.

## Reference Study

Mechanisms adapted from ui-ux-pro-max-skill.nextlevelbuilder.io (Study route, no signature transfer): a hero stat strip that quantifies the bundled knowledge, a searchable database presented as an interactive section, a step-by-step "prompt to result" pipeline demo, copyable install commands, and a filterable gallery. Signature elements deliberately rejected: their dark blue/purple palette, Space Grotesk/DM Sans pairing, glow-edged cards, gradient CTAs, and emoji iconography. Their demo-gallery mechanism is adopted directly - but every demo here is a complete page designed by an agent running this skill, shipped with its own `DESIGN.md` contract and a reproducing prompt, with fictional brands and live iframe thumbnails instead of screenshots.

## Page Or Asset Specs

- Goal: Make the homepage itself the strongest evidence of the skill's design capability while staying honest.
- Primary user task: Understand the method and inventory, then copy an install command.
- Primary content: Claim, run record, stats, observations, three outputs, five steps, 54-entry explorer, twelve-demo gallery, modes and routes, install and prompts, delivery checklist, meta strip.
- Primary CTA: Copy install command (header CTA links to GitHub).
- Components or visual modules: As listed in Components.
- Required states: Chinese active, English active, copy success, copy failure, explorer filtered, explorer empty, workflow step active, reduced motion.
- Responsive notes: Desktop hero is a two-column composition; mobile stacks claim, run record, stats. Explorer chips wrap; cards become a single column. Specimens stack with captions intact. No horizontal overflow at 320px.
- Accessibility notes: Landmarks, heading order, `aria-pressed` on language buttons, `aria-live` for copy feedback and explorer count, focus-visible outlines, 44px minimum targets, real text, `lang` attribute switching, AA contrast on desk and paper.
- Analytics or success signal: A reader can restate the three outputs and five steps, and copies a command or prompt; no analytics scripts are added.

## Quality Gates

- Request Anchor fit: The page showcases capability, serves as the GitHub Pages homepage, and keeps every promise checkable.
- Content: Every section adds a fact, action, boundary, or visible artifact; stats match the Real Inventory table; explorer summaries stay faithful to sources.
- Copy: No invented metrics, customers, demos, or credentials; no literal translation; no recurring contrast formulas; terminology consistent.
- Visual: Hero dominates once; the explorer is the only dense zone; semantic zones do not overlap, clip, or overflow horizontally; demos read as deliberate, distinct design languages.
- Accessibility: Contrast roles hold on desk and paper; keyboard path covers switch, tabs, stepper, explorer, copy buttons; focus states visible; targets 44px or larger.
- Responsive: 375, 768, and 1440 render cleanly in both languages; 320 has no horizontal overflow.
- Interaction: Language switch, copy buttons, tabs, stepper, and explorer filter work; states announced via `aria-live`.
- Performance: One HTML file around 250KB or less including inline data; Google Fonts with `display=swap` is the only external request; no other scripts, no raster images; the twelve gallery thumbnails are same-origin iframes with `loading="lazy"` so they cost nothing until scrolled near.
- Print or export: Not applicable.
- Contract consistency: This file passes strict contract validation and OKF usage validation; `data-ud-check` zones match the Agent Execution Rules list.

## Implementation And Governance

- CSS architecture: One static `index.html` with CSS custom properties mirroring the front matter and semantic class names. Demo pages are separate self-contained files under `docs/demos/<slug>/index.html` with their own `DESIGN.md`, embedded in the homepage only as scaled, non-interactive, lazy iframes.
- Language implementation: Chinese default; a JS dictionary switches all `data-i18n` text; `?lang=en` and `index-en.html` preserved; `<html lang>` updated; choice persisted in `localStorage`.
- Token implementation: CSS variables mirror the front matter tokens plus derived dark-field roles documented in Colors.
- Component naming: Names reflect content modules and semantic zones.
- State naming: `data-lang-button`, `data-copy`, `data-tab`, `data-step`, `data-domain`, plus `data-ud-check` and `data-ud-motion` markers.
- Theme strategy: Single dark studio theme; no theme toggle.
- Dark mode: The page is the dark mode; demo pages choose their own themes and may be light inside their plates.
- Framework notes: None; vanilla HTML/CSS/JS.
- Performance budget: One HTML document, inline JSON data for 54 entries, two font families at two weights each, no raster images, no external JS.
- Visual regression: Bundled `validate_html_visual.mjs` when the pinned runtime is available; otherwise rendered screenshots reviewed manually and recorded in the run log.
- Accessibility testing: Rendered inspection plus keyboard and contrast review.
- CI checks: Not configured.

## Assumptions

- GitHub Pages continues to serve the `main` branch `docs/` folder; all asset paths stay relative.
- Google Fonts is reachable for most visitors; the system fallback stack is acceptable when it is not.
- The 54-entry inventory (35 concepts, 19 playbooks) is current at version 0.6.0; the explorer data must be regenerated if files are added or removed.
- The orchestrator (Integrator) remains the sole writer of this contract; worker agents implement `index.html` and the data extract against it. Demo pages are designed by worker agents running this skill end to end; each demo owns its own `DESIGN.md`, uses a fictional brand, stays self-contained (inline CSS/JS, Google Fonts only, no raster images), and carries `data-ud-check` zones so the rendered audit can run on it.

## Open Questions

- None for this revision.

## Review Log

| Version | Date | Change | Reason | Reviewer |
|---|---|---|---|---|
| 1.0 | 2026-08-12 | Expanded the demo gallery from six to twelve: Swiss-grid conference, quiet-luxury PDP, industrial hardware page, newsprint zine, data-story annual report, Bauhaus exhibition; stats updated to 12 | User wanted broader style range with clearly separated design languages, sourced by mechanism extraction from strong reference archetypes | Cursor (Integrator) |
| 0.9 | 2026-08-12 | Replaced the inline specimen section with a demo gallery: six complete pages under `docs/demos/`, each designed by a worker agent running this skill and shipped with its own `DESIGN.md`; stat strip now counts the demos | User asked to follow the reference site's real-case gallery approach, with workers installing this skill to design the cases (Grok 4.5 High workers) | Cursor (Integrator) |
| 0.8 | 2026-08-12 | Rebuilt the homepage as a dark studio showcase: live specimens, 54-entry OKF explorer, interactive run record, honest stat strip; Integrator-planned, worker-implemented | User asked for a capability-showcase page comparable to the UI UX Pro Max site, planned by the orchestrator and built by Kimi K3 workers | Cursor (Integrator) |
| 0.7 | 2026-07-11 | Reframed the homepage around concrete outputs, five actions, and quieter editorial copy | User found the page cluttered and the copy AI-sounding; the new content contract removes repetition and abstract product language | Codex |
| 0.6 | 2026-07-10 | Updated the public knowledge lane for decision-bound OKF and verification | The official site should explain that routed knowledge must change the artifact and its checks | Codex |
