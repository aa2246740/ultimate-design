# Slop Fingerprints

The patterns that make an artifact read as generated from a template. Use this catalog twice: when choosing a direction, so the first draft avoids them, and when critiquing the rendered result, by scanning the screenshots and counting what you find. `craft-core.md` holds the positive rules; this file is the detection side.

## How To Use It

No single entry is wrong in itself. The problem is **clustering**: a page reads as generated when several of these appear together, because together they are the average of every landing page a model has seen. Judge density, not individual bans.

- **0-2 distinct fingerprints in a view**, each justified by the content: fine.
- **3 or more in the first viewport, or 6 or more on the page**: the artifact reads as a template. Rework the structure of that view (`craft-core.md` §2 and §5), not just its colors. Swapping purple for amber does not remove a fingerprint; the dark-navy-and-amber page is the same template.
- A fingerprint stays only with a **content reason** you can state in one sentence. "Users compare three plans with the same attributes" justifies a comparison layout; it does not justify the floating-cards-with-badge execution. "Adds memory", "looks premium", and "feels modern" are not content reasons.
- A requested style does not license every symbol of that style (see I3).
- The density rule guards against templates; it is not a score to push to zero. Stripping a page until nothing registers produces the opposite failure, covered under Sterile below. A page with zero fingerprints and no identity has failed too.

Each entry: what it looks like, then what to do instead. IDs are stable so critiques and `scripts/detect_slop.mjs` can refer to them. **[M]** marks signals the script detects on generated HTML; everything else needs eyes on the screenshot.

## Structure

- **S1 Section template [M].** Every section is eyebrow, heading, one-line lede, then a grid of equal items; the page outline reads like one form filled in five times. *Instead:* shape each section from its content; let one be a single sentence, one a table, one long prose.
- **S2 Equal card grid [M].** Three or four identical boxes, each an icon, a title, and two lines. *Instead:* a list with strong titles, a table, or one item given real space with the rest demoted.
- **S3 Hero formula.** Eyebrow, big headline, subline, filled button, ghost button, small trust line, product mock on the right; every element predictable before you see it. *Instead:* decide the one job of the first view and build only that: the product itself, one claim, one piece of evidence, or the working interface.
- **S4 Stat strip [M].** A row of big numbers with tiny captions ("12 cases · 35 concepts · 3 hosts", "99.9% · 24/7 · 10x"). *Instead:* put a number next to the claim it proves, in a sentence or beside the evidence. Remove invented numbers.
- **S5 Reflex pricing trio.** Three floating cards, the middle one highlighted with "Most popular" or 最常选, check-mark lists. *Instead:* a comparison table with aligned rows when comparison matters; a plain price where the decision happens when it does not.
- **S6 Decorative numbering [M].** 01/02/03 on sections, principles, or cards whose order means nothing. *Instead:* number only real sequences such as steps, ranks, or contents.
- **S7 Closing CTA box.** A rounded panel near the end with a big "Ready to...?" heading, a glow, and two buttons. *Instead:* end with the specific next step in the page's normal rhythm, or let the persistent CTA do the job.
- **S8 Card inside card [M].** Containers inside containers; text that could sit on the page is wrapped in a bordered box. *Instead:* remove the outer container and group with space and rules.
- **S9 Dead half [M].** Content fills one half of a wide section and the other half is empty because the grid expected something. *Instead:* narrow the container on purpose, bring a related element into the space, or reflow.
- **S10 Edge drift [M].** Blocks off the container edge, text touching the viewport edge, headings at a different left edge from their paragraphs. Always a defect, never a style.

## Type

- **T1 Eyebrow system [M].** Tiny uppercase or tracked labels, often mono, often with a dot or dash, above every heading. *Instead:* remove them; if a section truly needs a category label, use it once, in normal case, as real navigation or taxonomy.
- **T2 Translated eyebrow [M].** An English uppercase label above a Chinese or other non-English heading: "SERVICE PACKAGES" over 三档洗护套餐. *Instead:* delete it.
- **T3 Two-tone headline [M].** Part of a headline or brand name recolored or highlighted in the accent: "Finlyt**ics**", "形式**与**功能", "Build **faster**". *Instead:* let size and words carry it; keep the accent for what the user acts on.
- **T4 Gradient text [M].** `background-clip: text` with a gradient. *Instead:* solid color.
- **T5 Mono as seasoning [M].** Monospace on labels, tags, and captions to look technical on a page with no code or data. *Instead:* mono only for code, IDs, values, and tabular data.
- **T6 Reflex display face.** The first-reach font for a mood: Inter, Sora, or Plus Jakarta for SaaS; Space Grotesk for tech; a thin high-contrast serif with tiny tracked caps for luxury; a stretched wide grotesk for bold. Not banned, but a sign the choice was a reflex. *Instead:* choose from the subject's world and the reading scene (`design-okf/systems/type-personality.md`) and test with real copy.
- **T7 Ugly wraps [M].** A lone word or one or two CJK characters on the last line of a heading; a heading broken mid-phrase. *Instead:* `text-wrap: balance`, a width change, or rewording.
- **T8 Stacked emphasis.** Big, bold, colored, uppercase, and tracked on the same text. *Instead:* one lever.

## Color And Surface

- **C1 Dark SaaS default.** Near-black or navy ground, one amber, lime, or neon accent, a teal "live" dot, faint grid lines. *Instead:* decide the scene first; if dark is right, build a tinted neutral ramp and restrained accents (`craft-core.md` §3).
- **C2 Tasteful-cream default.** Beige, cream, or bone ground, serif headings, olive, terracotta, or coral accent, tiny tracked caps, applied by reflex to every "premium" or "friendly" brief. *Instead:* derive the palette from the subject's materials and imagery. When those materials really are warm (coffee, bread, paper, wood), warm neutrals are the right call and not a fingerprint; the tell is using them regardless of subject.
- **C3 Multi-hue gradient [M].** Purple, indigo, or blue gradients, mesh or aurora backgrounds, gradient buttons, two-hue diagonal washes. *Instead:* solid fills; use a gradient only when it depicts something (light, a material, a data scale).
- **C4 Glow and blob [M].** Radial glows in corners or behind the hero, blurred orbs, soft color washes, a spotlight behind a product. *Instead:* remove; if the area feels empty, fix the composition rather than adding light.
- **C5 Glass [M].** Frosted translucent content panels. *Instead:* opaque surfaces; blur only on a sticky bar over scrolling content.
- **C6 Neo-brutal kit [M].** Thick black borders, hard offset shadows, candy primaries, highlighter marks. *Instead:* if the brief wants raw and loud, get it from type scale, cropping, and color blocks without the offset-shadow costume.
- **C7 Rainbow data.** A different saturated hue per bar in a single series; sequential data mapped to unrelated hues (green to red). *Instead:* one hue with lightness steps; highlight only the item the story is about.
- **C8 Texture by default [M].** Grain overlays, grid-paper lines, dot patterns added "for depth". *Instead:* flat surfaces unless the texture is genuinely the brand's material.

## Components

- **K1 Pill everything [M].** Pill buttons, pill tags, pill badges, and pill toggles on one page. *Instead:* one radius family; pills only for true chips and filters.
- **K2 Icon tiles [M].** Every feature icon inside a tinted rounded square. *Instead:* bare icons at text size, or no icons.
- **K3 Hover lift [M].** Every card rises and grows its shadow on hover. *Instead:* hover feedback only on clickable things, and subtle (color, underline, border).
- **K4 Decorative status.** Pulsing "live" dots, "New" badges, and notification counts on static pages. *Instead:* show status only when it reflects real state.
- **K5 Emoji as icons [M].** Emoji as bullets, icons, or section markers. *Instead:* one consistent icon set, or plain text.

## Imagery

- **I1 Objects drawn in code.** Products, animals, people, or food built from CSS shapes or naive SVG: a capsule-shaped bottle, a cartoon cat. *Instead:* real or generated bitmap imagery, an honest labeled slot with the right aspect ratio, or a typographic composition.
- **I2 Rectangle dashboard.** A "product screenshot" assembled from boxes and fake charts that no real product would show, often with truncated labels. *Instead:* a credible, dense, aligned UI with plausible data, labeled if fictional, or a placeholder slot.
- **I3 Style costume.** A style's most famous symbols used as the identity: primary circle, triangle, and square for Bauhaus; ink mountains, red seal, and vertical text for "Chinese"; orange, mono, and technical drawing for "industrial"; red, Helvetica, and grid lines for "Swiss". *Instead:* the style's method plus one well-executed signature move (`craft-core.md` §6).
- **I4 Filler shapes.** Abstract waves, floating geometry, sparkles, and blobs used to fill space. *Instead:* remove, or replace with real content.

## Copy

- **W1 Contrast formula [M].** "X, not Y." / "Built for A, not B." / 不是…而是… as a headline or lede pattern, especially when repeated. *Instead:* state the positive claim directly.
- **W2 Triplets.** "Fast. Simple. Powerful." and three parallel fragments in general. *Instead:* one concrete statement.
- **W3 Empty verbs [M].** seamless, effortless, powerful, unlock, elevate, supercharge, empower, streamline, next-gen, cutting-edge; 赋能、一站式、全方位、沉浸式、打造、助力、极致、无缝. *Instead:* what the thing does, with a noun and a number.
- **W4 Invented precision.** Metrics, customers, awards, or quotes with no source ("lifted conversion 19%"). *Instead:* real proof, a clearly marked sample, or no number. See Honest proof in `quality-gates.md`.
- **W5 Quip density.** Every label and caption tries to be witty. *Instead:* plain, useful microcopy, with voice in one or two places where it matters.
- **W6 Echo lede.** The subline restates the headline. *Instead:* the subline adds the next fact.
- **W7 Dash habit [M].** Em dashes (— or ——) in most sentences. *Instead:* periods and commas.

## Motion

- **M1 Fade-up everything [M].** Every block fades and slides in on scroll and is invisible until then. *Instead:* static content by default; motion for state changes and one intentional moment.
- **M2 Ticker and counters [M].** Marquee bands and count-up numbers. *Instead:* static text; if a number matters, show it.

## Sterile

The opposite failure: a page with the template removed and nothing put in its place.

- **Z1 Wireframe look [M].** Near-grayscale page, one accent used only on buttons, one default sans, no imagery, no centerpiece; it reads as unfinished. *Instead:* palette temperature from the subject, a type voice, and a centerpiece (`craft-core.md` §1, §2, §3).
- **Z2 Placeholder hero [M].** A labeled placeholder or empty frame occupying the hero or a large share of the first view. *Instead:* build that position from content you have; keep any real placeholder small and secondary.
- **Z3 Brief leakage [M].** Notes-to-self, instructions to the client, or brief wording shown on the page: "replace with real photography", "do not hotlink", "pricing assumed", "请替换", "请勿外链图床". *Instead:* move it to notes.md or DESIGN.md.
- **Z4 Chart that disagrees with itself.** Axis ticks that do not match the plotted values, bars not starting at zero, missing units, a highlight color that means something else elsewhere. *Instead:* read two values off the render and fix the scale.

## Reporting A Scan

One line per hit, most damaging first, then the density line:

```text
[S3 Hero formula] first viewport: eyebrow, two-tone brand, headline, two buttons, trust line, mock. Content reason: none. Fix: lead with the ledger itself; one CTA.
[T2 Translated eyebrow] x5 sections: English caps over Chinese headings. Fix: delete.
[S10 Edge drift] hero column starts at x=0 while the nav starts at x=160. Fix: restore the container width.
Density: first viewport 4, page 9 -> reads as template; restructure hero and features before polishing.
```
