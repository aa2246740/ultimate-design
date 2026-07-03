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

- The page or graphic has one primary focal point.
- Information hierarchy is clear through size, weight, spacing, position, and contrast.
- Alignment is intentional.
- Spacing follows the contract or a documented scale.
- Major semantic zones such as titles, lead copy, cards, charts, tables, controls, and footers do not overlap, touch, or feel visually tangled. Use a documented minimum gap, commonly 36 px in design coordinates for adjacent major zones, unless the contract intentionally groups them tighter.
- Color roles are stable and not merely decorative.
- Color has a scene, mood, or brand reason; it does not fall back to category-default blue/green/gray unless that is intentional.
- Typography is readable at the final size and viewport.
- Important text zones state their expected line behavior when wrapping would change the design, such as max lines, no-wrap, or acceptable truncation.
- Icons, photos, illustrations, and textures share one visual language.
- No text overflows its container.
- The final rendered screenshot set or contact sheet has been inspected; passing a DOM/canvas bounds check alone is not enough.
- No obvious AI-default decoration: generic glass, gradient text, identical icon-card grids, decorative side stripes, over-rounded cards, or stock-looking placeholder art.

## Content

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

## Presentation Deck

- The deck has a clear audience, delivery mode, business goal, and decision or action request.
- The narrative chain is coherent: title-only reading tells the story.
- Every core slide has one claim, evidence that supports it, and an action or implication.
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
- New assumptions are recorded.
- Open questions are not hidden.
- Tokens/components/page specs changed by this work are updated.
- The review log has a meaningful entry for significant changes.

## Final Reporting

Report verification honestly:

- "Verified" means you checked it.
- "Assumed" means you chose a default and recorded it.
- "Not run" means you did not check it and you state why.

If the environment lacks a browser, renderer, screenshot, export, or inspection tool, use the checklist as a fallback and mark visual verification as not run.
