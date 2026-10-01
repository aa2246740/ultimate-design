# Style system

Taste you can execute. Instead of inventing CSS for every artifact, compose a **style spec** from a vetted catalog, generate tokens that already pass contrast, and build with a kit that only reads those tokens. The generator and the gate do the arithmetic (scales, contrast, spacing); you make the design decisions (which voice, which color posture, what the centerpiece is).

A style is a combination, not a template: 20 type pairings × 10 color strategies × any seed color × 6 surfaces × 3 densities × 6 canvases. Presets are worked examples of good combinations; treat them as starting points and change a dimension whenever the brief asks for it.

## Files

| File | What it holds |
|------|---------------|
| `catalog.json` | Type pairings T01–T20, color strategies C01–C10, surfaces S01–S06, densities, canvases. `node scripts/make_style.mjs --list` prints it. |
| `presets.json` | P01–P14: proven combinations with the layout (L) and moves (M) that suit them. |
| `selection.md` | Scene → recommended and banned choices, centerpiece options, layouts L01–L06, moves M01–M20. Read it before composing a spec. |
| `../scripts/make_style.mjs` | Spec → `style.css` (tokens as CSS custom properties, Google Fonts import, phone scale) + `style.tokens.json` (for the gate). |
| `../kit/base.css`, `../kit/components.html` | Web kit and its component catalog (responsive, tested at 390 px and 1440 px). |
| `../kit/canvas.css`, `../kit/canvas-xhs.html`, `canvas-slide.html`, `canvas-poster.html` | Fixed canvases: social card sets, slides, posters. |
| `../kit/chart.js` | Bar, horizontal bar, and line charts that read the palette; ticks computed, axes from zero, one highlighted series. |

## Workflow

1. **Name the scene** and read its row in `selection.md`. The subject's own world decides the voice: a bakery is not a SaaS product, a clinic is not a nightclub.
2. **Compose the spec.** Pick one option per dimension from the recommended set, or start from the nearest preset and change what the brief needs. Write a one-line reason for each choice into `DESIGN.md`.

   ```json
   { "type": "T02", "color": { "strategy": "C01", "seed": "#B4532A" }, "surface": "S01", "density": "regular", "canvas": "web" }
   ```

   - `seed` is the identity color. Take it from the subject (terracotta for a clay studio, the harbor's teal, the brand's red), never a default blue or purple.
   - `second` is required only for C06 duotone.
   - `canvas`: `web` for pages and product UI; `xhs` 1080×1440, `square` 1080×1080, `story` 1080×1920, `poster` 1200×1600, `slide` 1920×1080 for fixed pieces. Each canvas gets its own type scale, safe area, and minimum text size.
3. **Generate.** `node scripts/make_style.mjs --spec style.json --out ./` (or `--preset P05 --seed "#7A3B2E" --out ./`). Check the printed contrast line; the generator already fits every text role to AA against every ground it can sit on.
4. **Build with the kit.** Link `style.css` then `kit/base.css` (+ `kit/canvas.css` for canvases, `kit/chart.js` for charts), or inline them for a single-file deliverable. Copy markup from the catalogs, then replace every word with the brief's facts. Use `var(--...)` tokens and kit classes only: no hex values, no px font sizes, no new font families. Page-specific layout CSS is fine when it uses tokens.
5. **Gate.** `node scripts/detect_slop.mjs --input index.html --style ./` fails on off-system colors (four or more), text at the edge, clipped or overlapping text, low contrast, and, on canvases, wrong size, text under the minimum size, text in the safe margin, or text overflowing the card. Fix every fail, then look at the screenshots it saved.
6. **Export canvases.** `node scripts/export_canvas.mjs --input cards.html --out ./png` writes one PNG per `[data-canvas]` at its exact pixel size. Open every PNG before delivering.

## Brand and existing systems

- **Existing design system or product tokens win.** Use them and skip the generator; run the gate without `--style`.
- **Brand colors only:** use the primary as `seed`. Choose C03 when the brand should carry whole bands, C02 when it should appear only on actions and the centerpiece, C06 with `second` when the brand has two colors.
- **Brand fonts:** keep the pairing whose voice matches and override the families; CJK fallbacks, weights, and tracking stay:

  ```json
  { "type": "T06", "color": { "strategy": "C03", "seed": "#E4002B" }, "surface": "S03", "density": "regular",
    "fonts": { "display": "Manrope", "google": ["Manrope:wght@600;700;800"] } }
  ```

  Add `"serif": true` when the display override is a serif; omit `google` for self-hosted fonts and add the `@font-face` yourself.
- **A client-mandated value the catalog cannot express** (an exact brand neutral, say): add it as a named custom property in your page CSS and note it in `DESIGN.md`. The gate warns on up to three off-system colors and fails at four, so an exception stays an exception.

## What the system does not decide

The centerpiece, the copy, the order of sections, what to leave out, and whether the page has an identity. A perfectly tokenized page can still be a template; `references/craft-core.md` and the critique on the screenshots decide that.
