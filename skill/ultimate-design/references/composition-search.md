# Composition Search

Open, neutral **search prior** for choosing how content is shaped on a surface. It is not a closed catalog of named templates, not a theme library, and not a fixed rotation schedule.

Use when a visible artifact has meaningful **style freedom** and composition (page shape, section rhythm, slide archetype, card/poster layout, or product surface organization) is still undecided. Skip when the contract is **Locked** on layout axes, the change is a tiny polish, or an existing system already dictates structure.

## Relation To Other References

- `design-okf/systems/taste-engine.md` **Layout-Family Audit** remains the post-pass variety check.
- This file is the **upstream search**: generate a few composition hypotheses, choose by fit, then implement.
- Composition hypotheses are **search inputs**, not pasteable templates.

## Family Contract

The ten families below are **non-exhaustive examples**, not a closed catalog. Prefer a listed family when it fits; when content or medium needs a shape none cover, **derive a new neutral family** with the same five fields and a generic name (no external product theme or macro brands).

Each family is a functional shape. Use generic names only.

For every family (listed or newly derived), the same fields apply:

- **Use when**
- **Avoid when**
- **Format / responsive collapse**
- **Variation axes**
- **Common failure**

### 1. Statement-led

- **Use when:** one claim or brand line must dominate; poster, manifesto, keynote open, or sparse marketing.
- **Avoid when:** users need multi-step tasks, dense data, or many equal choices.
- **Format / responsive collapse:** single column; statement stays first; secondary proof stacks under.
- **Variation axes:** alignment bias, measure width, rule/ornament presence, proof placement.
- **Common failure:** centering everything; statement without a next step when action is required.

### 2. Split dialogue

- **Use when:** claim vs evidence, product vs proof, before/after, or bilingual panels.
- **Avoid when:** one side is empty decoration or the content is a single linear story.
- **Format / responsive collapse:** stack with primary column first; keep pairing labels.
- **Variation axes:** ratio, which side leads, media vs type, sticky vs static secondary.
- **Common failure:** 50/50 habit with no hierarchy; decorative mock filling the secondary pane.

### 3. Narrative document

- **Use when:** long reading, editorial explanation, policy, case study, or letter-like voice.
- **Avoid when:** glanceable dashboard or single-CTA landing with little prose.
- **Format / responsive collapse:** continuous column; pull-quotes and figures full-width.
- **Variation axes:** chaptering, margin notes, figure cadence, TOC presence.
- **Common failure:** fake “magazine” labels on short SaaS blurbs; equal section padding with no editorial beat.

### 4. Modular index

- **Use when:** many peer items (features, products, docs, portfolio) need scan and compare.
- **Avoid when:** a single story arc or one primary decision matters more than browsing.
- **Format / responsive collapse:** one column list or 2-up cards; preserve item identity.
- **Variation axes:** density, sort/filter affordance, media ratio, metadata exposure.
- **Common failure:** identical icon-card grid for unrelated ideas; cards inside cards.

### 5. Process sequence

- **Use when:** steps, onboarding, pipeline, or timeline is the product truth.
- **Avoid when:** steps are marketing filler (“1. Sign up 2. Magic 3. Profit”) without real procedure.
- **Format / responsive collapse:** vertical stepper; numbers retained only if order is real.
- **Variation axes:** orientation, sticky progress, detail depth per step, branching.
- **Common failure:** decorative numbering; timeline that is only a row of icons.

### 6. Evidence stage

- **Use when:** demo, screenshot, chart, map, or live product must carry the argument.
- **Avoid when:** no real evidence exists (do not invent chrome or fake dashboards).
- **Format / responsive collapse:** evidence first or stacked after the claim; captions remain attached.
- **Variation axes:** crop, annotation density, device honesty, live vs static.
- **Common failure:** unlabeled mockups presented as product truth; re-drawn OS chrome as decoration.

### 7. Workbench utility

- **Use when:** tools, consoles, multi-panel product UI, or dense operator surfaces.
- **Avoid when:** marketing emotion is the job and density confuses first-time visitors.
- **Format / responsive collapse:** prioritize primary task pane; secondary panels become sheets/tabs.
- **Variation axes:** pane count, density, inspection vs edit, persistent nav.
- **Common failure:** dashboard ornament without a task path; sticky panels that obscure content.

### 8. Comparison matrix

- **Use when:** plans, options, specs, or alternatives must be judged side by side.
- **Avoid when:** only one honest option exists or rows are not comparable.
- **Format / responsive collapse:** stacked option cards with repeated attributes; keep difference highlights.
- **Variation axes:** row vs column emphasis, highlight strategy, mobile attribute order.
- **Common failure:** uneven criteria; visual noise that hides the decisive differences.

### 9. Atmospheric immersion

- **Use when:** mood, world-building, entertainment, or experiential brand is primary and content is sparse.
- **Avoid when:** regulated claims, dense forms, or accessibility-critical instructions dominate.
- **Format / responsive collapse:** reduce motion and layering; keep text contrast; preserve one clear action.
- **Variation axes:** depth, motion budget, type contrast strategy, media full-bleed.
- **Common failure:** illegible type on busy media; motion as the only hierarchy.

### 10. Spec / catalog strip

- **Use when:** parameters, SKUs, API surfaces, or technical inventories need authoritative listing.
- **Avoid when:** emotional persuasion is the only goal.
- **Format / responsive collapse:** definition list or stacked rows; keep units and labels.
- **Variation axes:** tabular vs list, grouping, monospaced data, filterability.
- **Common failure:** marketing adjectives replacing measurable attributes.

## Candidate Protocol

When style freedom warrants composition search:

1. **Generate 2–3 plausible composition hypotheses** from the example families, a justified hybrid, or a newly derived neutral family. Do not enumerate the whole set or invent a fixed catalog score.
2. **Compare each qualitatively** on Request Fit, content structure, scene/medium, and available evidence/assets. Prefer comparative reasons over arbitrary numeric self-scores.
3. **Choose one** primary composition. Record why the others lost in plain language.
4. **Ask the user** only when two high-impact options remain genuinely comparable and the wrong pick is expensive to reverse. Otherwise proceed (YOLO default).
5. If a **Locked** system or locked layout axes exist in `DESIGN.md`, constrain search to allowed variation; novelty does not override locked brand or layout axes.
6. After implementation, run the taste-engine **Layout-Family Audit** where multi-section variety matters.

## Repetition

- Detect same-family adjacency or project-history sameness via contract fingerprint, prior sections, or review.
- **Explain** repetition: pass when a functional or brand reason is recorded (system product, dense tool, intentional series).
- Do **not** mechanically ban repeating a family; ban unexplained default attractors that ignore content.

## Completion Criteria

Composition search is complete when:

- Either a primary composition is chosen with Request Fit rationale, or search was correctly skipped (locked axes / tiny change / no freedom).
- Hypotheses (if generated) are 2–3, not a catalog dump.
- Locked axes and intentional repetition reasons are recorded when relevant.
- Families used stay generic; no external product theme/macro name catalog is imported.
- Downstream layout-family audit still applies for multi-block variety.
