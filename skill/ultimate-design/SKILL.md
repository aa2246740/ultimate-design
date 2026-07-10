---
name: ultimate-design
description: "Contract-driven design workflow for durable visual work. Use for: DESIGN.md contracts, product UI, marketing pages, presentation decks, graphic/print assets, brand systems, content/UX writing, design critique, and rendered verification."
---

# Ultimate Design

Work like a professional designer-builder: frame the problem, shape the content, choose a visual system with reasons, make the artifact, critique the result, verify rendered output, and preserve the design contract for the next agent. Do not use this skill for purely functional frontend changes with no visual, UX, brand, layout, or design-system impact unless the user asks for design judgment.

The leading word for this skill is **contract**: every design choice should either come from the existing design contract or create/update it. The contract is usually `DESIGN.md`; for larger projects it may include `design-system/AGENT-RULES.md`, `TOKENS.md`, `COMPONENTS.md`, or equivalent files. A missing `DESIGN.md` is normal, not a blocker.

Treat content as the meaning layer of the contract. Content decides what the artifact must communicate; UI decides how users act; visual design directs attention; frontend implementation preserves semantics, accessibility, responsiveness, and consistency.

For every visible artifact, apply a lightweight **Taste Checkpoint** by default: name the design read, the category defaults being avoided or intentionally kept, the layout-family or slide-archetype budget, the intended visual memory feature, and the type personality. For polished visible artifacts, also apply a compact **Necessary Judgment** lens: necessity, inevitability, craft tolerance, care, material honesty, and scene fit. Load the full `taste-engine.md` when the artifact has meaningful style freedom, public-facing polish, multiple sections/slides/frames, or any risk of becoming generic card-based AI output. Load `necessary-design-judgment.md` when the work needs senior taste critique or risks surface minimalism, overdecoration, or template-like styling. For tiny fixes or strict existing-system UI work, keep the checkpoint brief and do not over-style.

For every meaningful visible design run, treat OKF as **preflight**, not post-rationalization. Before choosing a direction or making a new artifact, load the branch references and directly relevant OKF concept files, then bind each active concept to at least one concrete decision, artifact target, and verification hook. If a concept changes no decision, it was not active knowledge; remove it from the run. If no OKF concept is relevant, record why.

## Interaction Modes

Default to **YOLO mode**: do not interview the user by default. Infer from the prompt, existing files, screenshots, brand assets, code, and product context first. Ask only for blockers, make safe assumptions, and produce a complete first pass with contract, artifact, critique, repair, and verification.

Use **Pro mode** when the user includes `--pro`, asks to work "like a real pro", or explicitly wants to confirm details before execution. In Pro mode, build consensus before making high-impact choices: audience, deliverable, message hierarchy, content scope, brand posture, taste dials, color commitment, type personality, layout model, imagery/assets, interaction/export constraints, and acceptance criteria. Ask in compact batches, avoid open-ended interviews, skip harmless details, update the Request Anchor after each decision, and proceed only when the next design choice is sufficiently agreed.

After the user answers Pro mode questions or supplies a clear decision bundle, the next turn is a delivery turn. Read `references/pro-mode.md`, freeze a **Decision Snapshot**, and follow its bounded post-consensus gate. Re-open an agreed choice only when new evidence creates a true blocker.

### Proof Run Gate

Use a **proof run** when the agent is running in Pi, a local/weak/headless model, a non-interactive CLI, or any eval/debug run where the user is testing whether this skill was actually followed. A proof run is not a prettier final response; it is a machine-checkable route through the skill.

For HTML proof runs, read `references/proof-run-html.md` immediately after this file. Use its artifact-first order, sparse `data-ud-check` zones, coupled motion markers, OKF decision bindings, and unified proof command. A proof run passes only when the contract, OKF usage, rendered UI, and applicable motion reports have no active failures; otherwise repair and rerun or report the failed evidence honestly.

Classify missing information before asking:

- **Blocker:** proceeding would make the result unsafe, legally risky, production-invalid, or pointed at the wrong audience. Ask once.
- **Risky but defaultable:** choose a conservative default, proceed, and record the assumption.
- **Harmless:** proceed without mentioning it unless it affects the final artifact.

Typical blockers:

- The business/user goal cannot be inferred.
- The user asks for print-ready output but print size, bleed, color mode, or printer specs are missing.
- Brand assets, logo usage, likeness rights, image rights, or font licensing matter.
- The requested platform, stack, or deliverable format is impossible to infer.
- The user asks for an exact redesign of an unknown existing brand/product without source material.

If the missing detail is not a blocker, do not interrupt the user in YOLO mode. Record it under `Open Questions` or `Assumptions` when persistence matters.

## Operating Loop

1. **Orient.** Determine the surface: product UI, marketing website, presentation/PPT deck, graphic/print collateral, brand system, audit/polish, or design-system work. Read any existing `DESIGN.md`, design-system files, CSS/theme/tokens, representative components, screenshots, slide masters/templates, and relevant assets.
   Completion: you can state the user, task, surface, constraints, existing visual language, and what artifact you are expected to change or create.

2. **Complete the brief.** Fill the smallest useful design brief: audience, primary task, success criteria, brand tone, platform, accessibility target, technical stack, assets, optional user-supplied reference images, and output format. For presentation decks, also state audience role, meeting or reading mode, decision or action requested, duration, delivery format, brand/template constraints, and compliance risks. For product, feature, flow, dashboard, onboarding, pricing, or validation-page work, also state the product problem, user situation, desired behavior or outcome, success signal, and main tradeoff. Reference images are optional input: use them when supplied; in Pro mode ask once in a compact way whether the user has any; in YOLO mode do not block or generate one by default when none is supplied. Create a compact **Request Anchor** with the original user request, latest user override, deliverable, primary audience, core job to be done, success criteria, non-goals, must-preserve constraints, and validation checks. Use existing evidence before asking.
   Completion: blockers were asked once, assumptions were written down and safe enough to proceed, and the Request Anchor is available in `DESIGN.md`, a compact review note, or the run trace.

3. **Build the content contract.** Define the user intent, message hierarchy, primary action meaning, voice/tone, terminology rules, state-language rules, and content risks before choosing layout or styling. Content may shape IA and component needs, but it should not directly prescribe layout mechanics.
   Completion: the artifact can answer what this is, why it matters, what the user can do next, what happens after action, and which words/states must stay consistent.

4. **Run OKF preflight.** Read only the references that match the work before choosing a direction or making a new artifact. Convert them into concrete constraints instead of leaving them as background knowledge:
   - `references/principles.md` when bootstrapping `DESIGN.md` from zero, when no existing design system exists, when the user asks for senior/professional design judgment, or when the design direction lacks a clear rationale. This is a router into `references/design-okf/index.md`; read the OKF index, then only the relevant concept files.
   - `references/design-okf/methods/product-sense.md` only when product judgment can still change the solution: the problem, user outcome, success signal, scope, prioritization, business/user tradeoff, validation plan, or whether the requested solution is right remains open. Do not load it solely because the artifact is product UI, a dashboard, onboarding, pricing, or a feature flow; when those decisions are already clear, spend the OKF budget on the concrete content, accessibility, responsive, interaction, data, or implementation risk instead.
   - `references/design-okf/governance/request-integrity.md` when the task is long, content-heavy, multi-file, likely to exceed short-term attention, or when final validation must prove the artifact still answers the user's original request.
   - `references/design-okf/systems/taste-engine.md` for the full Taste Engine when a visible artifact has meaningful style freedom, public-facing polish, multiple sections/slides/frames, or risk of generic card-based AI output. Tiny fixes and strict existing-system UI only need the lightweight Taste Checkpoint.
   - `references/design-okf/foundations/necessary-design-judgment.md` when the user asks for design philosophy, taste, Apple/Jony Ive/Rams/Hara-style judgment, or senior critique, and when a visible artifact feels styled-but-not-inevitable, fake-minimal, overdecorated, template-like, surface-premium, or when final critique must judge necessity, care, craft tolerance, material honesty, and scene fit.
   - `references/design-okf/systems/type-personality.md` when selecting or changing font families, type is a visual memory feature, the Chinese/English family voice or pairing is itself an art-direction decision, the user asks for stronger typography, or font licensing, CJK WebFont size, fallback, or deliverable portability may affect the result. Do not load it for mixed-script mechanics alone; use `typography-system.md` for scale, line length, line height, wrapping, overflow, optical sizing, and user text scaling.
   - `references/design-okf/systems/motion-language.md` when a visible artifact includes meaningful animation, microinteractions, page transitions, scroll storytelling, animated HTML decks, or when motion depth is above static. Do not load it for ordinary static layouts or tiny hover-only polish.
   - `references/design-okf/systems/motion-contract.md` when animation is a requested feature or delivery claim, especially SVG line/border drawing, scroll-linked or scrubbed motion, page-level reveal choreography, GSAP/ScrollTrigger work, reduced-motion behavior, or when browser evidence must prove animation correctness.
   - `references/proof-run-html.md` when the run is in Pi, a weak/local/headless model, a non-interactive CLI, or an eval/debug mode and the requested artifact is HTML. It is the compact execution branch for artifact-first output, semantic-zone marking, coupled motion markers, and unified browser proof.
   - `references/content-model.md` when the artifact has meaningful text, UX writing, report visualization, dense content, forms, component states, localization, or when bootstrapping `DESIGN.md`.
   - `references/branch-presentation.md` for PowerPoint, Keynote, Google Slides, business presentations, investor/board/executive decks, sales or pitch decks, training decks, read-alone decks, slide redesigns, and PPTX/PDF deck delivery.
   - `references/branch-web-product.md` for dashboards, app UI, product flows, components, forms, tables, and frontend implementation.
   - `references/branch-marketing-site.md` for landing pages, marketing sites, content sites, portfolios, campaign pages, and website redesigns.
   - `references/graphic-print.md` for posters, social graphics, banners, brand collateral, packaging, brochures, print, and image-generation art direction.
   - `references/branch-brand-system.md` for brand systems, visual identity, logo usage rules, art direction, palette/type systems, and reusable brand guidance.
   - `references/audit-polish.md` for critique, redesign diagnosis, visual polish, anti-AI-slop passes, and design QA without building a new artifact.
   - `references/tokens-components.md` when creating or changing tokens, component systems, UI kits, or shared design rules.
   - `references/design-contract.md` when creating or updating `DESIGN.md`. Its lean template is normally sufficient. Load `references/design-okf/governance/design-md-standard.md` only when schema compatibility, token syntax, or official tooling is unresolved; load `references/design-okf/governance/design-md-agent-governance.md` only when persistent multi-agent governance is in scope. Treat these as support references unless they change a concrete artifact decision, and do not automatically spend the active OKF budget on them.
   - `references/visual-verification.md` before final delivery for screenshotable visual artifacts: HTML pages/decks, product UI, dashboards, presentation previews, PDFs, graphics, and exported images. It defines the required rendered-output pass and optional HTML semantic-zone checks.
   - `references/monitoring.md` only for development/testing evidence: when the user asks for proof, evals, repeatability, traceability, or monitoring. Do not load it during ordinary design work.
   - `references/quality-gates.md` before final delivery, always.
   Completion: the preflight records active references, constraints, deliberate exceptions, verification hooks, and an **OKF Decision Bindings** table with `Reference | Decision | Artifact target | Verification`. Every active OKF concept has at least one non-empty binding before artifact work; unrelated concepts are removed. In Pro post-consensus or monitored eval mode, extra reading that changes no decision is a failed preflight.

5. **Bootstrap the contract.** For any non-trivial design artifact, create or update `DESIGN.md` by default. Use a compact contract or review note only for one-off, low-risk artifacts such as a tiny copy, color, or spacing adjustment. Create the contract from the user's prompt, repository context, product copy, existing UI/code, assets, safe defaults, content contract, and OKF Preflight. For UI/web work, make root `DESIGN.md` Google-compatible when practical: YAML front matter holds official token fields and Markdown holds rationale and agent-readable constraints. Do not ask the user to supply `DESIGN.md`. Mark inferred items as assumptions and unresolved items as open questions. In Pro post-consensus or monitored eval mode, bootstrap only the minimum contract needed to build and verify the artifact; when a visible artifact is requested, create the artifact skeleton after OKF Preflight and before expanding or polishing `DESIGN.md`.
   Completion: the contract contains enough Google-compatible token, project, user, content-model, OKF Preflight, IA, visual-system, component, quality-gate, assumption, and review-log material for another agent to continue.

6. **Choose a direction.** Commit to one primary design strategy from the Request Anchor, content contract, and OKF Preflight. Produce alternatives only when the user asked for variants or when two directions are genuinely plausible and cheap to compare. Name the chosen strategy in practical terms: message hierarchy, information density, taste dials, color commitment, color posture, type personality, layout model, layout-family budget, imagery style, motion purpose, motion budget, interaction model, anti-default locks, and the intended visual memory feature. For polished visible artifacts, also name the necessary judgment: what is necessary, what can be removed or demoted, which relationships must feel inevitable, which care states matter, which craft tolerances matter, and where material honesty or scene fit could fail. If no expressive style is needed, explicitly choose clarity-first taste and name what will stay quiet.
   Completion: the design direction traces each major choice to the Request Anchor or an OKF decision binding, explains why it fits this user and task, and names which defaults it rejects or intentionally keeps.

7. **Make the artifact.** Depending on the request, implement the UI, create the graphic asset, create or redesign the presentation deck, write the design spec, produce the prompt/art direction, or update the design system. Reuse existing project patterns and tokens first. For generated HTML or app UI, mark major semantic zones during implementation with `data-ud-check`, such as navigation, hero title/lead, primary content, card grid, chart area, slide, modal, form, footer, readable callouts, badges, annotations, sticky/fixed bars, and overlay panels, so verification can inspect layout intent rather than raw DOM boxes only. Mark the readable zones that should be checked, not both a broad parent and every child by habit. For motion, create the visible subject ids, `data-ud-motion` markers, and implementation selectors together so the evidence loop stays coupled. For one-off graphics or quick audits, a compact assumptions/review note may be enough. In Pro post-consensus or monitored eval mode, create a minimum complete artifact after OKF Preflight and before long rationale or polish; for HTML this means `index.html` exists before a full contract draft.
   Completion: the artifact is usable without the user filling in obvious missing states, breakpoints, labels, or component behavior, and its meaningful layout, style, content, motion, and interaction choices can be traced back to the contract or a deliberate exception.

8. **Critique and repair.** Before final delivery, critique the artifact against the Request Anchor, brief, product/problem framing when relevant, content contract, OKF Preflight, design contract, necessary judgment when relevant, taste dials and anti-default locks when relevant, selected OKF concepts, branch reference, and quality gates. Score or rank findings by user impact, business impact, accessibility risk, brand/theme fit, requirement drift, taste drift, OKF drift, necessity/care/material-honesty failure, and implementation effort. Fix all P0/P1 findings and easy P2 findings before proceeding; if a finding cannot be fixed in scope, record it with the reason. Treat failed contract validation, negative default tracking, un-updated monitoring trace, missing rendered evidence, unresolved necessary/care/material-honesty findings, missing OKF Preflight evidence, and obvious generic card/default-gradient output as repair items when they apply.
   Completion: a second pass finds no unresolved P0/P1 issues, no mismatch with the Request Anchor, no active OKF binding that failed to reach its artifact target, and no unresolved P0/P1 necessary/care/material-honesty failures. Remaining P2/P3 issues are fixed or accepted as follow-up risk.

9. **Verify.** Run the relevant quality gates: Request Anchor fit, OKF Preflight fit, content clarity, UX writing, visual hierarchy, contrast, responsive behavior, keyboard/focus, reduced motion, content states, text zoom/reflow, performance risk, slide title/reading order, export stability, print preflight, licensing notes, and contract consistency. For visual artifacts, do not rely only on DOM/canvas bounds or one sampled screenshot. Render every final page, slide, frame, or key responsive state; save screenshots/previews; inspect the full set for overlaps, cramped semantic spacing, hidden controls, clipping, awkward wraps, and density mismatch. For generated HTML proof runs, run `scripts/run_html_proof.mjs` when available; otherwise run the individual validators below. For generated HTML, run `scripts/validate_html_visual.mjs` as the **Rendered UI Audit** against the semantic zones created during implementation when a compatible pinned Playwright runtime is available; never launch the user's system Chrome as a headless fallback. It emits structured browser-measured findings for marked-zone integrity, page-level horizontal overflow, and visible interactive-control basics. Its rendered-integrity pass must include visibility and occlusion sampling unless explicitly not run with a reason. When a motion contract includes scroll-linked, SVG drawing, reveal no-flash, or reduced-motion claims, also run `scripts/validate_motion_contract.mjs` or report why motion validation was not run. For SVG drawing, the motion report must prove the drawing happens in the visual subject's display-window: entry-play only when the subject is visible on arrival, and scroll-linked completion near the fully framed or center-focused moment.
   Completion: failures are fixed or reported as not run with the reason; user success criteria and every active OKF decision binding were checked; visual artifacts have rendered evidence for every practical user-visible page/slide/state; the Rendered UI Audit has no active fail findings; readable marked zones are visible and not covered by unrelated layers. Run one relevant verification path after the artifact exists; inspect validator source only when debugging it.
   Browser fallback: when a compatible pinned runtime cannot launch, use the host Agent's approved browser, renderer, screenshot, or accessibility capability for the visible-review fallback in `references/visual-verification.md`. In a Codex environment where cmux plus Computer Use are available, that reference includes one implementation recipe. Preserve visible-review evidence separately; never convert it into `reportFresh: true` or a machine-audit pass.

10. **Govern.** Update the contract with changed OKF Preflight, content model, tokens, component rules, page/screen specs, necessary judgment when it materially shaped the work, assumptions, open questions, and review log entries. Keep the contract lean. Create `design-system/AGENT-RULES.md`, `TOKENS.md`, `COMPONENTS.md`, or similar files only for reusable systems, multi-screen products, brand systems, or multi-agent continuity.
   Completion: the next agent can continue from the contract without reverse-engineering your design choices. In monitored eval mode, the run trace has no applicable `pending` statuses before final response.

## Defaults

Use these defaults when evidence is absent and the assumption is low risk:

- Accessibility: WCAG 2.2 AA for web; prefer 44 by 44 CSS px touch targets for comfort even though WCAG AA has a smaller minimum with exceptions.
- Responsive checks: 320, 375, 768, 1024, 1280, and 1440 px when practical.
- Type: start body text at 16 px or equivalent; cap long-form English lines around 65 to 75 characters and Chinese around 25 to 40 characters.
- Spacing: use a 4 or 8 point scale; avoid undocumented one-off values.
- Tokens: primitive, semantic, then component tokens. Components should consume semantic or component tokens, not raw primitives.
- Motion: the static version works first; motion must explain feedback, continuity, hierarchy, navigation, story, or brand, remain interruptible, prefer transform/opacity, and support `prefers-reduced-motion`. For SVG line, border, route, graph, connector, or blueprint drawing, choose the trigger by the visual subject's **display-window**: use entry-play when the subject is already meaningfully visible on arrival, view-entry when it appears later but scroll progress is not the story, entry-or-view when responsive visibility differs by breakpoint, and scroll-linked only when progress itself carries meaning. Scroll-linked drawing must complete inside the display-window, near the fully framed or center-focused moment, not before the subject is readable and not after attention has moved away. Use a motion contract plus browser-sampled validation when scroll-linked, SVG drawing, reveal choreography, or reduced-motion behavior is requested.
- Theme: choose light/dark from the physical use scene, not category habit.
- Print: treat 3 mm bleed and 300 PPI as common placeholders, never as final production specs without printer confirmation.

## Professional Bar

Do not claim the artifact proves "10 years of design experience." Professional quality is observable behavior, not an identity claim:

- Frame the real problem before styling the surface.
- Shape content structure, message hierarchy, and state language before layout.
- Choose color, type, density, imagery, and motion from the audience, medium, scene, and brand posture.
- Preserve accessibility, responsiveness, production constraints, rights, and export stability.
- Critique and repair requirement drift, visual hierarchy, copy clarity, theme fit, spacing, overlaps, awkward wraps, and AI-default aesthetics before delivery.
- Leave a contract that explains what changed, why it changed, what assumptions remain, and how the next agent should continue.

The bundled OKF knowledge is descriptive context, not runtime truth. It can guide decisions and contract writing, but it does not override rendered output, accessibility tools, tests, print/vendor requirements, or user review.

## Development/Eval Monitoring

Monitoring is an optional add-on, not part of normal design execution. Use it only when the user asks to prove the workflow, run evals, debug the skill, or collect repeatable evidence. In that mode, read `references/monitoring.md` and use the bundled scripts before or after a test run. For ordinary page, UI, graphic, or polish requests, keep the workflow lightweight and do not create a trace unless it materially helps the deliverable.

## Research Ingestion

Research ingestion is a development task, not ordinary design execution. When absorbing deep research, building a wiki-like synthesis layer, auditing coverage, or promoting knowledge into OKF, read `references/design-okf/governance/research-digestion-llm-wiki.md`. Keep raw sources and long wiki notes out of runtime references; promote only stable, operational, checkable knowledge into OKF, then update the index, router, quality gates, coverage map, and flow proof when affected.

## External Capabilities

If a real `.pptx`, `.ppt`, Google Slides, or PowerPoint-compatible file must be created or edited, use the available Presentations capability for file operations and use this skill for deck strategy, visual system, slide-level critique, and delivery quality gates.

Use current official sources when a standard, browser behavior, framework API, platform guideline, or legal/printing requirement could have changed.

## Final Response

Keep the user-facing closeout short. Include:

- What was created or changed.
- The main design direction and any important assumptions.
- How the result maps back to the user's original request when the task was long, content-heavy, or drift-prone.
- What verification ran, and what could not be verified.
- Where the deliverable or contract lives.
- If development/eval monitoring was explicitly used, where the evidence report or run trace lives.

Do not dump the full checklist unless the user asks for it.
