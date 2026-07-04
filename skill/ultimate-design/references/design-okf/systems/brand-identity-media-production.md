---
type: Design System Concept
title: Brand Identity And Media Production
description: Bridges brand strategy and identity to guidelines, logo usage, tokens, asset libraries, screen, print, social, deck, packaging, licensing, rights, and governance.
tags: [brand-identity, brand-guidelines, logo, media-production, delivery, licensing, asset-governance]
---

# Purpose

Use this concept when the work involves brand identity, visual identity, VI manuals, logo usage, brand guidelines, cross-media brand kits, social kits, PPT templates, packaging, print collateral, asset libraries, licensing, rights registers, or long-term brand governance.

This is the delivery bridge: it explains how brand recognition survives real media. Use `visual-language-style-system.md` for expressive style, `tokens-components.md` for token/component mechanics, `production/graphic-print.md` for print caveats, `production/presentation-deck.md` for deck specifics, and `production/data-viz-i18n-legal.md` for legal/i18n/data risks.

Do not treat examples such as sizes, ratios, bleed, PPI, barcode rules, or platform specs as current production truth. Before final delivery, verify with official platform docs, vendor templates, printer requirements, packaging supplier, legal/compliance, font EULAs, and asset licenses.

# Core Chain

```text
brand strategy
-> brand identity
-> visual / language / behavior system
-> brand guidelines
-> design system / asset system
-> screen / print / social / deck / packaging delivery
-> licensing / rights / trademark records
-> governance and iteration
```

Brand identity answers "how people can keep recognizing us." Media production answers "how that identity reaches the real world without distortion."

# Recognition Mechanisms

A durable brand system uses five mechanisms:

- Consistency: color, type, logo, graphic language, voice, behavior, and media usage feel like the same sender.
- Repetition: key signals appear across site, app, packaging, ads, decks, social, video, and collateral.
- Distinctiveness: the brand has owned assets such as color combinations, type tone, motifs, composition, image style, packaging structure, voice, or sound.
- Contextual adaptation: the core remains stable while expression adapts to screen, social, print, deck, packaging, space, and product constraints.
- Governance: guidelines, asset libraries, templates, approvals, versioning, licenses, and misuse rules keep the system from depending on memory.

Name three to five recognition anchors. When brand distinction matters, at least one should remain recognizable after removing the logo.

# Identity Scope

Separate the layers:

- Brand: the total impression in the audience's mind.
- Brand identity: the system the organization intentionally creates.
- Brand image: what users actually perceive.
- Brand equity: accumulated recognition, trust, preference, and price power.

Identity may include:

- Strategy: mission, vision, values, positioning, promise, audience, competitors, personality, story.
- Visual: logo, color, type, graphic language, icons, illustration, photography, layout grid, motion.
- Language: voice, slogan, headline style, CTA rules, banned words, naming, multilingual rules, social copy style.
- Behavior/application: product experience, service behavior, packaging, spaces, templates, social, decks, video, commerce surfaces.

# Logo System

Treat a logo as a rule system, not a single file.

Define relevant variants:

- Primary mark.
- Horizontal lockup.
- Vertical or stacked lockup.
- Symbol or app/social avatar mark.
- Wordmark.
- Monochrome.
- Reversed.
- Small-size or simplified version.
- Motion/video version when relevant.

Define usage rules:

- Clear space based on a stable logo element, not a universal number.
- Minimum size per medium, tested in screen pixels, print dimensions, avatar contexts, packaging materials, and production methods.
- Color versions: full color, black, white/reversed, monochrome, spot color, light/dark/photo background rules.
- Background control: allowed backgrounds, forbidden backgrounds, contrast, image masks, holding shapes, and accessibility.
- Lockup rules for partner logos, taglines, campaign labels, and legal marks.
- Misuse examples: stretching, squashing, recoloring, shadowing, outlining, gradients, rotation, font changes, proportion changes, low-contrast placement, unauthorized separation, bitmap upscaling, and using the logo as random pattern.

# Brand Guidelines Model

Brand guidelines are an operating manual, not a portfolio.

Use three layers:

- Core guidelines: brand name, logo, core color, primary type, voice, trademark and legal rules. These are hard to change.
- Application guidelines: social templates, poster layouts, campaigns, ecommerce images, deck pages, UI examples. These can adapt within rules.
- Production guidelines: file formats, bleed, safe area, color mode, resolution, font handling, platform specs, packaging dielines, vendor preflight. These must be checked against supplier or platform truth.

Useful guideline sections:

- Brand introduction, strategy, personality, and voice.
- Logo system and logo usage.
- Color, typography, graphic language, icons, imagery, layout, and motion.
- Digital, print, social, deck, and packaging applications.
- Asset naming, asset library, licensing, trademark, approvals, versioning, and update process.
- Do/do-not examples clear enough for non-designers and suppliers.

# Design System To Delivery

Design tokens and assets must map to each medium:

- Web: HEX/RGB/CSS variables, SVG icons, WOFF2 fonts, responsive components.
- App: platform color resources, type styles, icons, density/DPR assets.
- Figma/design tools: variables, styles, components, libraries.
- PPT/decks: theme colors, theme fonts, masters, chart styles, placeholders.
- Print: CMYK, printer ICC profile, spot colors, paper, finishes, proofing.
- Packaging: dielines, material samples, spot colors, white underbase, barcode and regulatory zones.

Create an asset system when reuse matters:

- Asset library or DAM.
- Template library for decks, social, print, packaging, and repeated graphics.
- Naming rule such as `{brand}_{media}_{asset}_{variant}_{size}_{language}_{version}_{date}.{ext}`.
- Changelog, owner, approval path, deprecation path, and license records.
- Delivery package with final exports, source files, font list, linked images, color specs, usage guidelines, license receipts, changelog, and preflight report.

Do not include font files in a delivery package unless the font EULA permits redistribution or transfer.

# Media Delivery Matrix

## Screen

Check:

- RGB or sRGB is appropriate.
- SVG exists for logos, icons, and simple vector graphics.
- Bitmap assets have suitable pixel dimensions and DPR variants when needed.
- Responsive layout remains readable on mobile.
- Contrast follows the chosen WCAG target.
- Dark mode, alt text, reduced motion, performance, and webfont license are addressed.

Do not use "300 DPI" as the core screen rule. Screen delivery is about pixels, DPR, scaling, compression, loading, and accessibility.

## Print

Check:

- Trim size, bleed, safe area, color mode/profile, effective resolution, font embedding/outlining, linked images, and export format match printer requirements.
- Spot colors, overprint, trapping, rich black, K100 text/lines, foil, embossing, UV, die cuts, and paper/material effects are specified when relevant.
- Proofing method is recorded when final production matters.

Common values such as 3 mm bleed or 300 PPI are placeholders until the printer confirms them.

## Social

Check:

- Current platform specs, file sizes, safe zones, crop behavior, compression, ad rules, and accessibility expectations are verified before final export.
- Ratios are planned before design: 1:1, 4:5, 9:16, 16:9, or platform-specific variants.
- Critical text, subtitles, logos, and CTA stay within safe areas.
- Thumbnail and first frame are designed separately when they affect click or retention.
- Silent playback works for video.
- Music, footage, fonts, people, and generated assets are licensed for the platform and campaign.

Do not treat social as a resized poster.

## Decks

Check:

- Master, theme colors, theme fonts, title/body hierarchy, chart styles, icons, image placeholders, footer, page number, section pages, data pages, and conclusion pages are defined.
- Fonts are safe, embedded, licensed, or replaced with system-safe alternatives.
- Images and media are embedded or packaged; video/audio formats are tested when relevant.
- PDF/frozen version exists when fidelity matters.
- File size, aspect ratio, presenter notes, confidentiality labels, and approval needs are handled.

Brand decks must be editable by non-designers without breaking the system.

## Packaging

Check:

- Supplier dieline, cut lines, fold lines, glue areas, bleed, safe area, production layers, material, finish, and tolerance are respected.
- Text and logos avoid fold, trim, glue, and high-distortion zones.
- Barcode requirements come from GS1, local GS1 body, supplier, and actual scan tests.
- Regulatory labels are confirmed by legal/compliance for product category and jurisdiction.
- Spot colors, white underbase, varnish, foil, embossing, and material color are specified when needed.
- Physical proof or prototype is required before claiming final production readiness for serious packaging work.

Packaging is design plus engineering plus law.

# Licensing And Rights

Licensing asks "may we use it?" Rights ask "who owns it?"

Record or flag:

- Font license scope: desktop, webfont, app embedding, PDF/eBook, logo/trademark, broadcast, server generation, and client transfer.
- Image/video/illustration/icon/template/mockup license scope: commercial use, media, geography, duration, distribution, modification, resale, and extended license needs.
- Music rights: sync, public performance, ad use, platform, territory, duration, and edits.
- AI-generated asset assumptions and platform terms.
- Likeness/model/property releases for real people, places, and products.
- Copyright ownership, commissioned-work contract, work-made-for-hire assumptions, transfer terms, and trademark status.

Use a rights register with:

- Asset name.
- Source.
- Rights holder.
- Licensee.
- Usage scope: region, media, term, purpose.
- Commercial use, modification, sublicensing.
- Expiration.
- Proof documents.
- Risk notes.

Flag legal uncertainty; do not resolve legal questions by design intuition.

# Ask Or Proceed

Ask only when missing information would invalidate a final claim:

- The user needs final print-ready, packaging-ready, regulatory-ready, or platform-ready files.
- Official brand assets or logo rules are missing and exact brand compliance matters.
- Rights, licenses, trademarks, font transfer, or model releases affect publication.
- Vendor/platform/legal constraints are unknown and cannot be safely assumed.

Otherwise proceed with a design draft and include a preflight checklist or unresolved production notes.

# Done Check

This pass is done when another agent can answer:

1. What are the brand strategy, audience, and three to five recognition anchors?
2. Which identity elements are core, which are application-level, and which are production-specific?
3. What logo versions and misuse rules exist?
4. How do color, type, layout, imagery, voice, tokens, and assets map across screen, print, social, decks, and packaging?
5. Which platform, vendor, legal, barcode, packaging, font, and asset-license facts are verified, assumed, or still open?
6. What delivery package, naming rule, rights register, approval path, and versioning process preserve the system?

If the work cannot meet production requirements yet, label it as a design draft, template draft, or preflight package rather than final production-ready output.

# Source Notes

Research basis includes brand identity theory, brand-guideline practice, NASA Brand Center as a public governance example, W3C Design Tokens Community Group, WCAG 2.2, print vendor upload/preflight practices, Adobe PDF/X references, Microsoft PowerPoint export references, GS1 barcode references, WIPO copyright and trademark references, U.S. Copyright Office work-made-for-hire guidance, China Copyright Law and CNIPA trademark application references, and licensing/EULA practice. Treat platform specs, printer specs, packaging regulations, barcode values, font terms, and legal requirements as current-source checks, not timeless rules.
