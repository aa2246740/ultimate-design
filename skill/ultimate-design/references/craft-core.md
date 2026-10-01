# Craft Core

Read this for every visible artifact before choosing a direction, and again when critiquing the rendered result. It is the working judgment of a senior designer-builder, written as defaults and procedures. The rest of the skill decides *what* to make and records it; this file decides *how it looks* and how to tell whether it looks right.

These are defaults, not laws. Break one when the content gives you a reason you can say in one sentence. "It adds visual interest", "it makes the page memorable", and "it feels premium" are not reasons.

## 1. Stance

- Most good design is subtraction and precision. A first draft always has too many elements, too many containers, too many colors, and too few real words. Remove before you add. Subtraction removes noise, never identity.
- Distinction comes from the content, not from decoration. A page with this product's real numbers, names, and sentences already looks like nobody else. If the page would still work after swapping in a competitor's logo, fix the copy and the evidence before touching the styling.
- The enemy is the template, not any single pattern. One pill badge is fine. Eyebrow + heading + one-line lede + three cards, repeated five times, is a template even when each piece is well made.
- Restraint is not absence. A finished artifact has a point of view: a palette with a temperature that comes from the subject, a typographic voice, and a centerpiece made from the content. An all-gray page with one accent button and an empty image box reads as a wireframe, and a wireframe is a failure, not a safe result. How loud the voice is depends on the scene; whether there is a voice does not.
- Judge the pixels, not the intent. What you meant to build and what rendered are different things; only the render counts.

## 2. Work Order

1. **Real content first.** Write actual copy, labels, and numbers (or clearly marked sample data) before layout. The headline names the thing or the offer in plain words. Placeholder text hides structural problems. Keep the brief's exact words for rules, instructions, and promises (if it says "水沸后静置 30 秒再冲", do not shorten it to "水开就冲"); paraphrase only marketing voice.
2. **Shape from content, and pick the centerpiece.** For each block ask what shape the content has: one statement, a sequence, a set of peers, a comparison, reference data, a narrative, a single piece of evidence. Pick the form that matches (§5). Never start from "hero, feature grid, pricing, CTA". Decide the centerpiece (below) before any styling.
3. **Structure in grayscale.** Get hierarchy, spacing, and alignment working with black, grays, and one family. If it does not read in grayscale, color will not rescue it.
4. **Then the system** (§3), applied without exceptions.
5. **Then the identity**: palette temperature, type voice, and a well-executed centerpiece (§6). Every artifact gets these; the scene decides how loud they are.
6. **Render and look** (§8). Fix the biggest problem. Look again.

### The centerpiece

The strongest pages are built around one artifact made from the brief's own facts and placed in the first view. A template cannot have it, because it only exists for this content. For example:

- a bakery: today's bake schedule, with what has already sold out;
- a CI service: the last thirty builds as a strip, with the flaky one annotated;
- a quarterly sales review: one sentence stating the miss and its cause, next to the table of slipped deals;
- a clinic: this week's open appointment slots by doctor.

Find it by asking which fact in the brief the reader most needs, and what form lets them see it at a glance: a schedule, a ledger, a log, the key number charted with its story, a calculator, a map, a before/after. Build it for real in HTML, CSS, or SVG with plausible, internally consistent sample data. Record in notes.md which data is invented; never print prototype meta on the page (no "样本", "示意", "sample data", sample dates, or implementation notes such as file formats). Give it one story detail that makes it specific: the one failed night, the spike, the sold-out item, the slot that just opened. A photo slot, a feature list, or a brand name on a gradient is not a centerpiece.

## 3. A Small System, Strictly Applied

Consistency is the cheapest way to look professional; improvisation is the fastest way to look generated.

**Type**

- One family is enough for most artifacts. Two when there is a real role split (display vs text, or text vs data). A third needs a reason.
- Five to seven sizes on a page. Product UI and dense tools use a gentle ratio (about 1.125-1.25). Marketing, editorial, decks, and posters use bigger jumps (about 1.33-1.6) and let the display size be decisively larger; timid heading sizes are a common failure.
- Two or three weights. Emphasis uses one lever at a time: size, or weight, or color.
- Body 16-18 px on screens. Line-height 1.5-1.7 for Latin body, 1.7-1.9 for CJK body, 1.05-1.25 for headings. Large Latin display may take slight negative tracking only when the face looks loose at that size; never letter-space CJK headings for "elegance".
- Measure: 45-75 characters for Latin reading text, 25-40 characters for CJK. Constrain it with `max-width` in `ch` or `em`.
- `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs; still check the render.
- Tabular figures wherever numbers align or update.

**Space**

- One base unit (4 or 8) and a short scale, for example 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
- Proximity does the grouping: inline gap < item gap < group gap < section gap, each step clearly larger (about 1.5-2x). A heading sits closer to the content it introduces than to the block above it.
- Section padding follows content. A two-line section does not get the same 160 px of air as a long one. Uniformly huge padding is a tell.

**Grid and edges**

- One container width and one side gutter per breakpoint (at least 16 px on phones, 24-48 px on desktop). Every block's left edge snaps to that container or to a declared column line.
- Consistent edges are the strongest single signal of care. Text touching the viewport edge, or a heading 40 px off the paragraph edge below it, reads as broken at a glance.
- Full-bleed is a deliberate choice for backgrounds and media, never for reading text.
- When a section uses only part of the width, the rest must be intentional (a measure limit, a margin note, a figure), not a void left by a grid expecting more items.

**Color**

- Neutrals carry structure; color carries identity. Build a neutral ramp of 8-10 steps tinted slightly toward the brand hue (in OKLCH: same hue, chroma around 0.005-0.02) so grays belong to the brand instead of looking dead.
- Take the palette's temperature from the subject: a roastery or bakery runs warm, an operations console can run cool with one sharp alert color, a legal practice can run ink-and-paper. Let the brand color appear in more than the buttons: a surface, a rule, the centerpiece. A gray page whose only color is one button reads as unfinished.
- One accent for action and selection, used sparingly. A second accent only when it has a separate job (data series, status).
- Status colors are functional, tuned to the palette, and never the only carrier of meaning.
- Secondary text is a lighter neutral with at least 4.5:1 contrast, not 50% opacity over a colored surface.
- Dark themes: a tinted near-black base (not `#000`, not navy by reflex); elevation by slightly lighter surfaces, not bigger shadows; body text around 85-92% lightness, not pure white; accents desaturated a step.
- Charts: one hue with lightness steps for ordered data; distinct hues only for unordered categories that must be told apart. Highlight the item the story is about and mute the rest.

**Surfaces**

- Pick one primary way to separate things on a surface: whitespace, hairline rules, a subtle fill change, or shadow. Border + shadow + fill + radius on the same box is the generic card.
- One small radius for controls and at most one larger for containers; nested radius = outer radius minus padding. Sharp suits precise or editorial work, soft suits friendly work; stay consistent either way.
- Shadows are low and tight, reserved for things that actually float: menus, dialogs, dragged items.

### Layout balance on wide screens

Two columns end at roughly the same height, or the shorter one gets more content; a tall empty gap under one column reads as unfinished. Table headers align with their column's content (numbers right, text left) and columns are sized to their content rather than spread evenly. Footers and toolbars sit on one baseline.

## 4. Hierarchy

- At a squint, or at a quarter-size thumbnail, each view has exactly one first read, an obvious second, and everything else quiet. If three things compete, demote two.
- Build emphasis with size and position first, weight second, color last. Color is for meaning and action.
- De-emphasize with lower contrast, not with small + light + uppercase + tracked all at once.
- One filled button per view. Secondary actions are text or outline. Two filled buttons side by side means the decision has not been made.

## 5. Content Shape Decides Layout

| Content | Good forms | Reflex to avoid |
|---|---|---|
| One big claim | Large type alone with room; maybe one piece of evidence | Claim + badge + two buttons + trust line + mock |
| Sequence / process | Numbered list, timeline, stepped narrative | Numbered circles inside cards |
| Peers to browse | List with strong item titles, index, table | Three-up icon card grid |
| Options to compare | Comparison table with aligned rows | Three floating price cards with a reflex "most popular" badge |
| Evidence | The actual screenshot, chart, photo, or attributed quote, given room | A dashboard assembled from rectangles |
| Reference data / specs | Definition list, spec table, tabular values | Cards with icons |
| Narrative | Continuous column, pull quote, figures | Every paragraph in its own box |

- Text can sit directly on the page. Containers are for things the user acts on as a unit: a product, a plan, a message, a file.
- Tables are underused and look expert. Use them for anything with repeated attributes.
- Asymmetry is fine and often better; a narrow label column beside a wide content column is a strong editorial default. Centering is for short, ceremonial content.
- Vary section form because the content varies, not to meet a quota.

## 6. Direction And Expression

- Take the visual language from the subject's own world. A finance tool borrows from statements and ledgers; a tea house from its menu card, receipts, and the room; a synthesizer from its panel legends; a report from print editorial. That produces style that is specific and credible.
- Avoid **costume**: the most famous symbols of a style used as the whole identity. Bauhaus as red circle, yellow triangle, blue square. "Chinese" as ink mountains, red seal, vertical text. "Luxury" as beige, thin serif, tiny tracked caps. "Tech" as dark navy, neon accent, mono labels, grid lines. "Bold studio" as offset hard shadows, candy colors, a stretched display face. "Industrial" as orange, mono, and a technical drawing. When a style is requested, deliver its method (grid discipline, typographic logic, material honesty) with at most one or two signature moves, executed well.
- One memorable move is enough: a confident type scale, a specific color, a real photograph cropped with intent, a layout rhythm, a piece of live data. A second and third "memory feature" dilute all of them.
- Do not draw products, animals, people, or objects in CSS or hand-written SVG. They come out crude and are the loudest amateur signal. Use typography, real or generated bitmap imagery, a chart, a diagram, or the centerpiece. Simple geometric diagrams and icons are fine.
- When a real photo is missing, build that position from content you do have. A placeholder slot never occupies the hero or another primary position and never takes a large share of a view; where one is genuinely needed, keep it small, give it the right aspect ratio, and label what belongs there ("roastery photo"), not an instruction.
- Everything visible is for the page's reader. Notes to the client, assumptions, and reminders to yourself ("replace with real photography", "do not hotlink", "pricing assumed", sentences copied from the brief) go into notes.md or DESIGN.md, never into the page. A "sample data" label is the one allowed exception.
- A product mockup inside a marketing page must look like a real product: real density, plausible data, correct alignment, labeled when fictional. If you cannot make it credible, show the mechanism another way (a diagram, a log, a table of the actual steps) rather than a fake screen or an empty frame.
- Icons: one set, one stroke weight, sized to the text beside them. Not every item needs an icon, and icons do not need tinted rounded tiles.

## 7. Details That Separate Crafted From Generated

Check each on the render:

- **Edges**: text blocks align to the container or a column line; nothing touches the viewport edge; section headings share a left edge.
- **Wraps**: no lone word (Latin) or one or two characters (CJK) on the last line of a heading; no heading broken mid-phrase. Fix with `text-wrap: balance`, a width change, or rewording.
- **Punctuation**: curly quotes, en dash for ranges, real ellipsis and multiplication sign. Chinese text uses full-width punctuation (，。：；！？「」“”) and no ASCII commas; CJK-Latin spacing is consistent across the page.
- **Clipping**: no text cut by `overflow: hidden`, `clip-path`, or a rotated container; no truncated labels inside mockups.
- **Numbers**: aligned figures in tables and stat groups; consistent units; data that adds up (percentages, dates, month labels).
- **Charts**: axis ticks, gridlines, and labeled values agree. Read two plotted values off the render and check them against the data; bar axes start at zero; units are labeled; a highlighted series means the same thing everywhere it appears.
- **Controls**: buttons and inputs on one row share a height and a top edge; labels align; focus states are visible and designed.
- **Density**: section size follows content; no tall empty bands; no half-empty rows where a grid expected more items.
- **Consistency**: the same thing looks the same everywhere, and different things look different.

## 8. Look At The Render Like A Critic

Whoever wrote the code tends to see what they intended. Force a literal read of the pixels before judging.

1. Render full-page screenshots at desktop (1440) and phone (390) widths after scrolling slowly enough for every reveal to fire. For generated HTML, `scripts/detect_slop.mjs` does this and saves the screenshots.
2. **Describe before judging.** For the first viewport and each section, write one literal line: what sits at the top-left, what is largest, where the left edges fall, what is empty. Then evaluate.
3. **Thumbnail test.** At about 25% size, is there one clear first read? Does it look like this specific thing, or like "a landing page"?
4. **Edge test.** Trace left edges down the page. Every jump must be deliberate.
5. **Fingerprint scan.** Go through `slop-fingerprints.md` against the screenshots and count distinct fingerprints in the first viewport and on the page.
6. **Delete test** on every element that is not content: would anyone miss it?
7. **Identity test.** Cover the logo. Can you name this brand's color, type voice, and centerpiece? If the honest answer is "gray, a default sans, a list", the page is a wireframe: add identity before polishing details.
8. Fix the biggest problem first, which is usually structure or content rather than styling. Re-render and look again. Anything public-facing gets at least two full look-and-fix passes.
9. Machine reports inform the critique; they never replace it, and a fingerprint count is not a score to push to zero. A clean detector report on a bland page is still a failed page.

## 9. Chinese And Mixed-Script Pages

- Choose the Chinese face first; it sets the page's texture. Pair Latin by optical size and weight, not by name.
- No English uppercase eyebrows ("SERVICE PACKAGES") above Chinese headings. It adds nothing for a Chinese reader and is one of the clearest generated-page tells.
- Full-width punctuation, no ASCII commas in Chinese sentences, one quote style used consistently.
- No heavy letter-spacing on Chinese; tracking belongs to Latin caps, if anywhere.
- Chinese headings wrap per character and often strand one or two characters on the last line; check every heading at every width.
- Body line-height 1.7-1.9; on screens use paragraph spacing rather than first-line indents.

## 10. When Quiet Is Right

Product UI, dashboards, forms, documentation, and settings: clarity and density beat expression. Use one durable sans, tinted neutrals with one precise accent, tight consistent spacing, tables over cards, and no decoration. Quiet still needs a voice and a centerpiece: for a report or dashboard, lead with the conclusion as a sentence with its numbers, and put the decision or agenda beside it. The craft shows in alignment, states, and copy. See `branch-web-product.md` for the state matrix.
