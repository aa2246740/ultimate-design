# Quality Gates

Read this before final delivery. Apply the gates relevant to the artifact. Fix issues before handing off when practical.

## Request Anchor

- The artifact matches the deliverable named in the Request Anchor.
- The primary user-facing view supports the core job to be done.
- The latest user override is reflected in scope, style, priority, and constraints.
- User-specific success criteria are checked before final delivery.
- Non-goals are respected; the artifact does not spend effort on excluded work.
- Must-preserve source facts, data, copy, brand constraints, assets, or behavior are not lost.
- Any mismatch with the Request Anchor is fixed, or explicitly reported with the reason.

## Visual

- The strongest visual element maps to the most important communication element, or the exception is intentional.
- The intended first focus, reading path, and action/decision endpoint can be named.
- The page or graphic has one primary focal point.
- Information hierarchy is clear through size, weight, spacing, position, and contrast.
- Alignment is intentional.
- Spacing follows the contract or a documented scale.
- Layout has an explicit composition model, grid/type-area logic, dominant alignment, and spacing rhythm when the artifact is more than a tiny one-off.
- Type hierarchy is established through size, weight, space, position, color, or typeface contrast without stacking every emphasis lever on one element.
- Important image/caption, chart/legend, table/source, heading/body, and CTA/supporting-copy relationships are spaced and aligned as intentional groups.
- Optical alignment is checked for icons, large punctuation, display type, mixed-script baselines, and numbers/units when visible polish matters.
- Major semantic zones such as titles, lead copy, cards, charts, tables, controls, and footers do not overlap, touch, or feel visually tangled. Use a documented minimum gap, commonly 36 px in design coordinates for adjacent major zones, unless the contract intentionally groups them tighter.
- Color roles are stable and not merely decorative.
- Color has a scene, mood, or brand reason; it does not fall back to category-default blue/green/gray unless that is intentional.
- Typography is readable at the final size and viewport.
- Letter spacing is `0` by default for UI/body/display text; nonzero or negative tracking requires an existing brand rule, logo/wordmark need, or a recorded typographic reason.
- Important text zones state their expected line behavior when wrapping would change the design, such as max lines, no-wrap, or acceptable truncation.
- Icons, photos, illustrations, and textures share one visual language.
- Color, photography, illustration, iconography, symbols, texture, type, layout, and motion speak the same concept rather than acting as isolated decoration.
- At least one owned visual feature remains recognizable when the logo is removed, when brand distinction matters.
- Decorative elements pass a deletion test: removing them would weaken meaning, identity, hierarchy, or system coherence.
- No text overflows its container.
- Generated HTML or app UI includes `data-ud-check` semantic zones on major user-visible regions so visual verification can inspect intent, not only raw geometry.
- The final rendered screenshot set or contact sheet has been inspected; passing a DOM/canvas bounds check alone is not enough.
- No obvious AI-default decoration: generic glass, gradient text, identical icon-card grids, decorative side stripes, over-rounded cards, or stock-looking placeholder art.

## Taste And Anti-Template

- For visible artifacts with style freedom, a Taste Signature or equivalent note records design read, taste dials, anti-default locks, layout families or slide archetypes, visual memory feature, and asset/reference policy.
- The result names the category default it avoids or intentionally keeps.
- The chosen taste dials match the audience, scene, brand posture, and medium; high variance does not weaken usability, accessibility, or the Request Anchor.
- A long page, deck, carousel, report, or multi-frame graphic has a layout-family or slide-archetype audit; repetition is intentional rather than default.
- Cards are used because elevation or modular scanning carries meaning, not because every idea needs a rounded container.
- At least one owned visual memory feature remains after removing logo and generic copy when brand distinction matters.
- Visual assets prove, clarify, or create the world of the artifact; they are not generic placeholders, fake screenshots, or decorative filler.
- References are translated into rules rather than copied as surface style.
- The final critique asks what still looks AI-generated and fixes obvious default-gradient, equal-card, fake-proof, fake-screenshot, decorative-badge, stock-image, or over-rounded-panel tells.

## Content

- The artifact has one primary message, supported by secondary explanation, evidence/trust, and a clear action when action is expected.
- Critical, Important, Useful, and Optional information are visually treated at appropriate priority.
- The first screen answers what this is, why it matters, and what the user can do next.
- Content is ordered by the user's task or decision path, not by internal structure.
- CTAs state action plus result when the action has consequence.
- Labels are visible; placeholders do not replace labels.
- Error states explain the problem and how to fix it.
- Empty states explain the current state and next step.
- Loading, success, disabled, confirmation, undo, permission, and partial-data states have useful copy when relevant.
- Same concept uses the same term across the artifact.
- Critical meaning is not carried only by color, image, tooltip, hover, truncation, or hidden text.
- Long text, mixed language, numbers, dates, currencies, localization expansion, and RTL are considered when relevant.
- Chinese text follows one paragraph system; line-start/line-end punctuation, unbroken ellipses/dashes, simplified/traditional punctuation, and vertical writing assumptions are checked when relevant.
- Mixed Chinese-English text checks visual size, baseline, spacing, number/unit treatment, full-width/half-width punctuation, font coverage, and rights.

## Layout, Typography, And Composition

- The layout still reads in grayscale or low fidelity before color and decoration.
- Grid choice fits the medium: single column, multi-column, modular, baseline, responsive 6/12-column, or hierarchical grid.
- Type area, margins, columns, gutters, safe areas, and baseline or vertical rhythm are defined when the artifact is persistent, multi-page, dense, editorial, or print-adjacent.
- Body line length, line height, paragraph rhythm, heading spacing, captions, footnotes, and legal copy are readable at the final medium and viewing distance.
- Editorial or multi-page artifacts define page rhythm, headers/footers, page numbers, section markers, figure/caption/table/source rules, and density variation.
- Swiss Style is used as grid-led clarity and asymmetry, not as a Helvetica/whitespace costume.
- Digital text supports zoom/reflow/text-spacing overrides without hidden content or controls; truncation has a full-view path for critical text.

## Accessibility

- Normal text contrast is at least 4.5:1.
- Large text contrast is at least 3:1.
- UI components and meaningful non-text graphics are at least 3:1.
- Focus states are visible.
- Keyboard navigation reaches every interactive element in a logical order.
- Inputs have labels.
- Icon-only controls have accessible names.
- Images have useful alt text; decorative images use empty alt.
- Color is not the only way to communicate state.
- Reduced motion is supported when motion exists.

## Responsive

- No page-level horizontal scroll at 320 px.
- Check small phone, large phone, tablet, and desktop when practical.
- Navigation has a mobile strategy.
- Tables have a mobile strategy: horizontal scroll, cards, column priority, or another documented approach.
- Images and media reserve dimensions and scale predictably.
- Sticky or fixed elements do not cover content.

## Interaction

- Actions provide feedback within a perceptible time.
- Primary actions state what happens next; risk, cost, consequence, or trust information is close to high-consequence decisions.
- Async actions have loading, success, and failure states.
- Destructive actions require confirmation or undo.
- Errors identify the problem and recovery path.
- Disabled controls are semantically disabled and visually distinct.
- Popovers, dropdowns, dialogs, and sheets escape clipping and manage focus.

## Product UI

- The design states or preserves the product problem, target user, core job, and intended user outcome.
- The primary task path maps to a success signal, metric, or observable user behavior when the work is product-oriented.
- Scope is deliberate: v1, prototype, dashboard, or landing page does not imply unrelated features or unvalidated commitments.
- Tradeoffs and non-goals are explicit when the design optimizes for speed, trust, conversion, efficiency, learning, or business outcome.
- The primary task path is clear.
- State coverage includes loading, empty, error, partial, permission, and success where relevant.
- Navigation preserves orientation and return paths.
- Forms include labels, validation, errors, required-field treatment, and recovery paths.
- Data tables or charts include accessible labels, readable numbers, and responsive behavior.

## Marketing Site

- The first viewport identifies the offer or subject, audience relevance, and next action.
- The page flow answers likely user objections.
- Trust, proof, specificity, or credibility elements are present when useful.
- CTAs are placed where the page naturally creates intent.
- The design avoids category-default aesthetics and repeated card scaffolds.
- Layout families vary across the page unless strict repetition is a stated brand or campaign rule.

## Presentation Deck

- The deck has a clear audience, delivery mode, business goal, and decision or action request.
- The narrative chain is coherent: title-only reading tells the story.
- Every core slide has one claim, evidence that supports it, and an action or implication.
- Slide archetypes vary by narrative job; the deck is not a sequence of identical title-plus-card pages.
- Density matches mode: live, read-alone, executive/board, sales/pitch, training, or internal execution.
- Slide titles are unique and preferably conclusion/action titles.
- Every final slide/page has been rendered or screenshot. Do not inspect only representative slides when delivering a deck or HTML deck.
- Charts state the insight, use the right chart type, show source/unit/period when needed, and avoid misleading visual encodings.
- Master/template rules are consistent: logo, footer, page number, typography, colors, and chart style.
- Export and accessibility checks are addressed: PDF stability, font embedding or safe fonts, reading order, alt text, contrast, and color-independent meaning.
- External-sharing risks are confirmed or flagged: confidential data, financial numbers, legal claims, brand approval, and font/image/icon rights.

## Brand System

- The visual direction is specific, not generic.
- Color, type, imagery, shape, motion, and copy voice reinforce one coherent direction.
- Rules are practical enough for future agents to apply.
- Guardrails include do and do-not examples.
- Logo and asset constraints are preserved or clearly marked unknown.
- Three to five recognition anchors are named when the task is brand-oriented.
- Core identity rules, application rules, and production rules are separated when a brand system must survive multiple media.

## Visual Language And Style System

- Concept sentence, positive keywords, and anti-keywords are explicit when style is a deliverable.
- Visual vocabulary roles are defined: color, photography, illustration, icons, symbols, texture, type/layout, and motion.
- Photography, illustration, iconography, and texture rules include do/do-not examples or clear constraints when those assets are used.
- Color psychology, symbols, and imagery are checked for cultural and contextual meaning rather than treated as universal.
- Icons remain clear at target size and have labels or accessible names when meaning is not obvious.
- Texture does not harm readability, performance, or print reproduction.
- Anti-template check names category defaults avoided and owned visual features created.
- Asset rights, likeness rights, font/image/icon licensing, and generated-asset assumptions are recorded.
- Cross-medium applications stay coherent when the style is meant to persist.

## Brand Identity And Media Production

- Logo variants, clear-space logic, minimum-size assumptions, color/background rules, and misuse examples are defined or marked unknown when logo usage matters.
- Brand guidelines act as an operating manual: core rules, application rules, production rules, do/do-not examples, owner, approval path, and versioning are recorded when relevant.
- Design tokens and assets map to the intended media: web/app, design tools, deck, print, social, packaging, or other required surfaces.
- Screen delivery checks pixel/DPR strategy, SVG/bitmap format choice, sRGB/RGB, contrast, alt text, performance, dark mode, reduced motion, and webfont licensing when relevant.
- Print delivery does not claim final readiness until printer trim, bleed, safe area, color profile, effective resolution, font handling, PDF/export format, proofing, and special finishes are confirmed or flagged.
- Social delivery does not rely on stale memorized dimensions; current platform specs, safe zones, compression behavior, thumbnail/first-frame readability, subtitles, and music/media rights are verified or flagged.
- Brand deck delivery preserves master, theme colors, theme fonts, chart styles, placeholders, footer/page number, export fallback, and cross-device stability.
- Packaging delivery respects supplier dieline, material, layers, fold/glue/trim zones, barcode/GS1 checks, regulatory copy, legal review, proofing, and production tolerance.
- Licensing and rights register cover fonts, images, video, music, icons, templates, mockups, AI assets, likeness/model/property releases, copyright ownership, commissioned-work terms, trademarks, usage scope, term, territory, and proof documents when publication or transfer matters.
- If vendor, platform, supplier, legal, or license facts are missing, the output is labeled as a draft or preflight package rather than final production-ready work.

## Performance

- Reserve image/media space to avoid layout shift.
- Avoid heavy decorative effects that hurt scroll or input.
- Lazy-load below-fold media when appropriate.
- Avoid unnecessary client-side JavaScript for static content.
- For web apps, watch Core Web Vitals risk: LCP, INP, and CLS.

## Graphic And Print

- Final size/aspect ratio is correct.
- Copy is proofread and legible at output size.
- Bleed, safe area, color profile, resolution, and export format are confirmed or flagged.
- Font, image, logo, and icon rights are confirmed or flagged.
- Special finishes, spot colors, die cuts, overprint, and rich black are specified when relevant.

## Audit And Polish

- Findings are severity-ranked.
- Each recommendation maps to user, business, accessibility, or design-system impact.
- Fixes distinguish quick wins from structural changes.
- Proposed changes are concrete enough to implement.
- A critique pass compares the artifact to the Request Anchor and original user need, not only to generic rules.
- Content clarity, UX writing, terminology, and state language are checked before visual polish.
- P0/P1 findings are fixed before final delivery or explicitly reported as blocked.
- Requirement drift from the Request Anchor is treated as P0/P1 when it changes the requested deliverable or core job.
- Theme fit is checked: color, type, imagery, density, and tone support the intended audience and task.
- A second pass confirms the repair did not introduce new high-severity issues.

## Data Visualization, I18n, And Legal

- Charts use the right chart type for the data relationship.
- Chart meaning is not conveyed by color alone.
- Axis labels, legends, units, tooltips, and data summaries are present where useful.
- Locale-sensitive numbers, dates, currencies, and text expansion are considered.
- RTL support is recorded when relevant.
- Font, image, icon, logo, likeness, and generated-asset rights are verified or flagged.

## Contract

- `DESIGN.md` or equivalent exists when the project needs continuity.
- Request Anchor exists when the task is long, content-heavy, multi-file, or drift-prone.
- `DESIGN.md` passes the bundled contract validator when the validator is available and the work created or materially changed the contract.
- New assumptions are recorded.
- Open questions are not hidden.
- Tokens/components/page specs changed by this work are updated.
- The review log has a meaningful entry for significant changes.
- In monitored eval mode, the run trace has no applicable `pending` statuses and includes evidence for critique, repair, verification, and governance.

## Final Reporting

Report verification honestly:

- "Verified" means you checked it.
- "Assumed" means you chose a default and recorded it.
- "Not run" means you did not check it and you state why.

If the environment lacks a browser, renderer, screenshot, export, or inspection tool, use the checklist as a fallback and mark visual verification as not run.
