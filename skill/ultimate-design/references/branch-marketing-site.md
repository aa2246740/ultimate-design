# Marketing Site Branch

Use this branch for landing pages, campaign pages, brand websites, content sites, portfolios, homepages, pricing pages, and marketing redesigns.

Read `design-okf/systems/taste-engine.md` by default when the site has style freedom, and especially when it needs distinctive taste, stronger style confidence, anti-AI-slop cleanup, visual assets, layout variety, or when the page risks becoming a centered hero followed by repeated card grids.

Read `design-okf/systems/type-personality.md` when the hero, brand, pricing, proof, article, or campaign typography needs a clearer voice, when Chinese/English mixed text matters, or when WebFont performance, fallback, or font licensing can affect the site.

Read `design-okf/systems/motion-language.md` when the site uses hero animation, scroll storytelling, page transitions, parallax, section reveals, animated product mechanisms, or a motion-depth taste dial above static. Do not load it for a static marketing page with only ordinary hover states.

Read `design-okf/systems/motion-contract.md` when animation is part of the user's explicit request or final delivery claim, especially SVG line/border drawing, scroll-linked motion, GSAP/ScrollTrigger behavior, or no-flash reveal choreography.

## First Decisions

Settle:

- Audience and buying/reading context.
- Primary offer or message.
- Content contract: first-screen answers, proof points, terminology, and action meaning.
- Primary conversion action.
- Trust signals needed.
- Content sections and scan order.
- Brand register: quiet, editorial, bold, premium, technical, playful, institutional, or another explicit direction.
- Type posture: utility-first, editorial, technical, premium, friendly, campaign display, or another concrete voice.
- Taste dials: visual variance, information density, motion depth, brand distinction, and experiment risk.
- Anti-default locks: category looks, color families, card patterns, fake screenshots, or stock imagery to reject.

Marketing surfaces sell, explain, recruit, or express identity. The first viewport must make the subject and next action obvious.

## Above The Fold

- The brand/product/place/object must be visible immediately, not only as tiny nav text.
- The headline should name the thing or literal offer. Put value props in supporting copy.
- The primary CTA should be concrete.
- Show a hint of the next section on common mobile and desktop viewports.
- Use real or generated bitmap assets when visual inspection matters. Avoid generic placeholder illustration.

## Visual Direction

Avoid category reflexes. Before choosing colors, write a concrete scene sentence: who sees this, where, under what light, with what urgency or mood. Choose the palette from that scene and the brand, not from the category alone.

Pick a color commitment:

- Restrained: neutrals plus one accent under 10 percent of the surface.
- Committed: one saturated color carries 30 to 60 percent of the surface.
- Full palette: three or four deliberate roles.
- Drenched: the surface is the color.

Use OKLCH when authoring new web tokens unless the existing system uses another color format.

## Page Flow

- Sections should answer user objections in a deliberate order.
- Use specificity, proof, examples, screenshots, or concrete outcomes instead of vague claims.
- Avoid endless identical card grids.
- Cards are not the default structure for every section.
- Use rhythm: vary section density, media, type scale, and whitespace.
- Keep a layout-family budget for long pages; six or more sections normally need at least four composition families unless strict repetition is intentional.
- Keep body copy readable and scannable.

## Copy

- CTAs use verb plus object.
- Link text makes sense out of context.
- Avoid generic marketing filler when specific product language is available.
- Do not repeat the heading in the first sentence.
- Proof, risk reduction, and trust copy should sit near the decision they support.
- Error, empty, or unavailable states still need useful copy when the site includes interactive elements.

## Responsive And Performance

- No page-level horizontal scroll at 320 px.
- Hero text must not overflow.
- Media should reserve space and load responsibly.
- Decorative effects must not undermine scrolling, input, or Core Web Vitals.
- Reduced motion is required when motion exists.
- Do not hijack scroll; static reading and conversion must still work when motion is reduced or disabled.
- When the site claims scroll-linked SVG or line animation, validation must sample motion progress in the browser; static screenshots alone are not enough.
