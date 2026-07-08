---
type: Design System Concept
title: Motion Contract
description: Executable contract for animation behavior, implementation routing, and browser-sampled validation evidence.
tags: [motion, animation, gsap, scrolltrigger, svg, validation, reduced-motion]
---

# Purpose

Use this concept when animation is a requested feature, a visual memory device, or a meaningful part of an interactive artifact. It turns motion language into a checkable motion contract: what moves, which visual subject owns the display-window, how progress maps to user input, which implementation primitive fits, and which browser evidence proves it worked.

Do not use this concept for ordinary hover color changes, single CSS transitions, or purely static visual work.

# First Principle

Motion language explains why motion exists. A motion contract defines what must be true in the rendered browser. Keep those layers separate.

The contract is done only when another agent can implement and validate the motion without guessing the visual subject, display-window, trigger model, trigger range, progress mapping, focus-complete boundary, initial state, reduced-motion fallback, or acceptance samples.

Use **display-window** as the leading word for SVG drawing: the animation belongs to the interval where the watched subject becomes visible, readable, and focused. The drawing should not finish before the subject is sufficiently displayed, and should not keep running after attention has moved on.

Use **focus-complete** as the completion gate inside that window: the visible line, border, or path reaches its complete state when the watched subject first reaches its visual focus moment. For a subject shorter than the viewport, that focus moment is its first fully framed viewport state. For a subject taller than the viewport, it is center-on-center focus.

The exit-complete check is only a late guard. If a motion reaches completion only as the subject leaves attention, the contract fails design judgment even when the math is internally consistent.

# When To Create A Motion Contract

Create a motion contract when any of these appear in the request, design direction, or artifact:

- Scroll-linked, scrubbed, pinned, parallax, or viewport-progress animation.
- SVG line, border, path, graph, handwriting, connector, or blueprint drawing.
- Page-level reveal choreography, staggered section reveals, or animated hero mechanisms.
- Timeline sequencing where multiple elements must remain synchronized.
- Motion used as a brand or visual memory feature.
- Any animation that the final response should claim was implemented.

# Contract Fields

Record these fields in `DESIGN.md` under `## Motion Strategy` or a dedicated `## Motion Contract` section:

- Motion id: stable name used by code, validation report, and notes.
- User-facing promise: plain-language behavior the user asked for.
- Purpose: feedback, continuity, hierarchy, navigation, storytelling, or brand.
- Implementation route: CSS transition, GSAP core, GSAP ScrollTrigger, framework adapter, or custom browser API.
- Trigger model: entry-play, view-entry, entry-or-view, scroll, hover, focus, press, drag, route change, or explicit play.
- Display-window: when the watched subject first becomes meaningfully visible and when it becomes fully framed or center-focused.
- Timing band: expected duration range for non-scroll motion, chosen from the motion budget and context rather than one-off taste.
- Duration and easing tokens: named values or ranges used by implementation, for example `entry-fast: 180-260ms power2.out`.
- Progress mapping: for scroll-linked motion, define input progress and output progress, for example `visualSubjectFocusProgress -> strokeRevealProgress`.
- Trigger range: start and end in user terms and implementation terms.
- End trigger: separate selector for the end boundary when the start belongs to a section but completion belongs to the watched subject.
- Visual subject: selector for the thing the user watches, for example the SVG, chart, blueprint panel, or case-study media block.
- Focus-complete boundary: the visual focus moment where the watched subject must already be complete, usually `auto -> strokeRevealProgress >= 0.95`.
- Exit-complete guard: optional later guard, for example `subject bottom 60% -> strokeRevealProgress >= 0.95`.
- Acceptance samples: expected state at 0, 0.25, 0.5, 0.75, and 1 progress, with tolerance.
- Initial state: what the user sees before JavaScript initializes and after initialization.
- Reverse behavior: reversible, one-way, replayable, or sticky-complete.
- Do-not-move zones: text, forms, dense data, controls, or legal/risk content that must stay stable.
- Reduced-motion fallback: useful static or simplified behavior.
- No-flash rule: whether visible -> hidden -> visible or duplicate reveal is allowed. Default: not allowed.
- Performance budget: properties allowed to animate and concurrency limits.
- Validation command: script or manual evidence path required before delivery.

# Implementation Routing

Use the smallest primitive that can satisfy the motion contract:

| Need | Default route |
|---|---|
| Simple hover/focus/pressed transition | CSS transition |
| Coordinated DOM/SVG transforms, fades, staggers, runtime control | GSAP core |
| Timeline sequencing or synchronized multi-step choreography | GSAP timeline |
| Scroll-linked, scrubbed, pinned, or viewport progress motion | GSAP ScrollTrigger |
| React lifecycle, cleanup, or scoped selectors | GSAP React patterns |
| Complex SVG path drawing, morphing, or path following | GSAP SVG plugins or a documented stroke-dash primitive |

For GSAP work, use the GSAP skills as implementation reference. This OKF concept owns the contract and evidence, not the GSAP API manual.

Record any external runtime in the contract. GSAP is framework-agnostic and can be loaded by npm or script tag, but it is still a third-party runtime dependency and carries its own license terms.

# Timing Bands

There is no universal gold standard for duration, but there are usable bands. Choose the smallest band that lets the user perceive the state change without waiting on decorative motion:

| Motion situation | Default band |
|---|---:|
| Press or tap feedback | 80-150 ms |
| Hover or focus feedback | 120-200 ms |
| Small state change | 150-250 ms |
| Entry-play SVG drawing or small section reveal | 250-500 ms |
| Modal, drawer, sheet, or large component transition | 250-400 ms |
| Page, route, or slide transition | 300-600 ms |
| Hero storytelling | 600-1200 ms, only when skippable or non-blocking |

Scroll-linked motion is governed by display-window and scroll range, not a fixed clock duration. Entry-play and view-entry SVG drawing should usually feel deliberate, not instantaneous; for expressive linework, start around 350-500 ms and shorten only for repeated UI work.

# GSAP Pattern Rules

When the route is GSAP:

- Register plugins explicitly when using a build tool or ScrollTrigger.
- Use `gsap.matchMedia()` or equivalent branching for responsive and reduced-motion behavior.
- Use `gsap.set()` or CSS initial states before first paint for elements that start hidden or offset.
- Use `fromTo()` only when the start and end states are part of the contract.
- Use `immediateRender: false` when a later `from()` or `fromTo()` targets the same property as an earlier tween.
- Prefer transform aliases, opacity/autoAlpha, and stroke dash values. Avoid layout-heavy animation unless the contract requires layout change.
- Store timelines/triggers when later control, cleanup, or validation introspection is needed.

# Trigger Choice

Choose the trigger from the watched visual subject, not from the page section by habit:

| Subject situation | Trigger model | Rule |
|---|---|---|
| Subject is meaningfully visible on initial arrival | entry-play | Play once on page/component entry; do not pretend it is scroll-linked. |
| Subject appears later but scroll progress is not the story | view-entry | Play once when the subject enters the active viewport. |
| Subject is initially visible on some breakpoints and below the fold on others | entry-or-view | Resolve per viewport: entry-play when initial visibility passes the entry threshold, otherwise view-entry. |
| Drawing represents a route, sequence, timeline, or process where scroll progress carries meaning | scroll | Map scroll progress to drawing progress inside the display-window. |
| Static export, reduced motion, or animation would add no meaning | static | Render complete and keep the visual still. |

# Scroll-Linked SVG Contract

For SVG line or border drawing linked to scroll, the contract should be focus-complete, display-window bounded, and owned by the watched visual subject:

```yaml
motion_contract:
  id: svg-route-draw
  type: scroll-linked-svg-draw
  implementation_route: GSAP ScrollTrigger
  visual_subject_selector: "#case-study-blueprint"
  display_window: subject top 80% to focus auto
  mapping: visualSubjectFocusProgress -> strokeRevealProgress
  trigger_range: subject top 80% to subject bottom 100%
  focus_complete: auto -> stroke_reveal >= 0.95
  exit_complete_guard: subject bottom 60% -> stroke_reveal >= 0.95
  acceptance_samples:
    - progress: 0
      stroke_reveal: 0
    - progress: 0.25
      stroke_reveal: 0.25
    - progress: 0.5
      stroke_reveal: 0.5
    - progress: 0.75
      stroke_reveal: 0.75
    - progress: 1
      stroke_reveal: 1
  tolerance: 0.12
  reverse_behavior: reversible
  reduced_motion: fully_drawn_static
  no_flash: true
```

Default the ScrollTrigger trigger to the visual subject, not a taller surrounding section. Use a larger trigger only when the line spans that larger section, a sticky/pinned story keeps the subject in view, or the contract states why the subject range is different. The larger-trigger case still needs display-window and focus-complete samples against the watched subject.

When start and completion belong to different objects, use ScrollTrigger's `endTrigger` pattern and record it as `data-ud-motion-end-trigger`. A common section pattern is: start at the media panel's `top 80%`, end at the same panel's `bottom 100%`, so the drawing is done when the panel is first fully framed.

If a visual subject is already meaningfully visible on initial arrival, do not pretend it is scroll-linked. Use entry-play SVG drawing or render it complete, then record the trigger model as `entry-play` or `static`. If the same subject is below the fold on a smaller viewport, use responsive trigger logic such as `entry-or-view`: entry-play on viewports where the subject is initially visible, and view-entry or scroll on viewports where it is not.

Prefer real path lengths from `getTotalLength()` and map `strokeDashoffset` from length to zero. Use `pathLength="1"` only when browser validation proves progress remains linear. Mark animated paths with `data-ud-motion="svg-route-draw"` or another stable id so validation can find them. Add `data-ud-motion-subject` when the watched subject is not the path's nearest SVG.

# Reveal Contract

For section reveals, prevent reveal flash:

- The static no-JS state must be readable, or the pre-JS hidden state must be deliberately declared and paired with a no-flash initialization pattern.
- Do not combine default-visible CSS with a delayed `from()`/`fromTo()` hidden state unless first-paint flash is acceptable and recorded.
- Use one source of truth for reveal state. Avoid CSS animations plus GSAP reveal tweens on the same property.
- Use one-way reveal for reading sections unless reversible reveal has a clear purpose.

# Validation

Static screenshots are not motion validation.

For any motion contract that includes scroll-linked animation, SVG drawing, no-flash promises, or reduced-motion fallback, run `scripts/validate_motion_contract.mjs` when a browser is available. The validator samples rendered states, not just DOM presence.

Minimum evidence:

- A JSON report listing every checked motion id.
- Scroll samples at the contract's required progress points.
- Display-window samples showing the scroll-linked range finishes near the subject's focus moment, not materially before or after it.
- Focus-complete samples showing the watched subject reaches its completed state at its first full-frame or center-focus moment.
- Exit-complete guard samples when the contract declares a late guard.
- Observed output progress and tolerance results.
- Reduced-motion result.
- No-flash or duplicate-reveal result when requested.
- Screenshots or traces when the validator supports them.

# Done Check

The concept is applied when:

1. The motion contract is recorded in the design contract.
2. The implementation route is named and fits the requested behavior.
3. SVG or scroll-linked targets have stable validation markers.
4. Reduced-motion and initial states are intentionally handled.
5. Browser-sampled validation has passed or is explicitly reported as not run with a reason.
