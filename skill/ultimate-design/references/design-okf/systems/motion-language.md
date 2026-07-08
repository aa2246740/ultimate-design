---
type: Design System Concept
title: Motion Language And Choreography
description: Purpose-led motion system for feedback, continuity, hierarchy, navigation, storytelling, brand expression, accessibility, and performance.
tags: [motion, animation, interaction, choreography, reduced-motion, performance]
---

# Purpose

Use this concept when a visible artifact includes meaningful animation, microinteractions, page transitions, scroll storytelling, animated HTML decks, or a motion-depth taste dial above static.

Do not load this concept for ordinary static layouts, tiny hover polish, or strict existing-system UI unless motion is the source of the design problem.

When animation is a requested feature or final delivery claim, also read `motion-contract.md`. Motion language owns purpose and choreography; motion contract owns implementation routing and browser-sampled evidence.

Motion is time-based information design. It should explain change, causality, continuity, attention, navigation, or brand tone. If it only says "this is premium" or "this is designed", keep the surface still.

# First Principle

Static communication must work first. Motion spends attention budget; use it only when the extra time makes the artifact easier to understand, use, remember, or trust.

Before adding motion, name:

- What changes.
- Why the user needs to notice it.
- Where the motion starts and ends.
- Whether the user can ignore, interrupt, or reduce it.

# When To Use Motion

Use motion when it improves comprehension or operation:

- Feedback: press, hover, focus, drag, submit, save, error, success.
- State change: expanded/collapsed, selected/unselected, loading/loaded, empty/filled.
- Continuity: list-to-detail, thumbnail-to-full view, drawer/modal origin, item reorder, delete/undo.
- Hierarchy: guide attention to the next important thing without competing with the main task.
- Navigation: show where a route, step, panel, or slide came from and where it went.
- Loading/progress: communicate waiting, progress, or system liveness without faking certainty.
- Storytelling: reveal a process, timeline, product mechanism, spatial relationship, or brand world.
- Brand expression: micro-behavior that fits the brand posture and does not damage usability.

# When To Keep Motion Quiet

Prefer stillness or near-still feedback for:

- Long-form reading, documentation, legal copy, and dense reports.
- Dashboards, data tables, monitoring surfaces, and high-frequency operational tools.
- Forms, payment, checkout, confirmation, and other high-consequence flows.
- Danger, error, compliance, medical, finance, legal, and security moments.
- Multiple simultaneous loops, auto-playing decoration, heavy parallax, large rotation, large zoom, and scroll hijacking.
- Any case where content becomes hidden, delayed, or harder to compare because of animation.

Quiet motion is still design. A fast focus ring, pressed button, loading state, or continuity cue may be the right level.

# Motion Purpose

Assign every nontrivial animation exactly one primary purpose:

| Purpose | Good use | Bad use |
|---|---|---|
| Feedback | Confirms the system received input | Decorative bounce on every click |
| Continuity | Preserves object identity across states | Random fade that hides where content went |
| Hierarchy | Points to the next decision or changed region | Competes with the primary content |
| Navigation | Explains route, step, slide, or panel movement | Delays frequent navigation |
| Storytelling | Makes sequence, mechanism, or timeline legible | Turns reading into a forced show |
| Brand | Creates a recognizable behavior | Adds personality that conflicts with risk or task |

If the purpose cannot be named, remove or simplify the motion.

# Motion Budget

Choose one budget for the artifact and record it when motion matters:

| Budget | Use when | Behavior |
|---|---|---|
| Static | Print, read-alone deck/PDF, dense reading, compliance, dashboards | No required motion; still visual hierarchy carries meaning |
| Micro | Forms, product UI, dashboards, task tools | Feedback and state continuity only |
| Component | Interactive cards, tabs, drawers, modals, lists | Local transitions explain state and origin |
| Page | Marketing pages, portfolios, product stories, HTML decks | Section/route/slide choreography supports narrative |
| Brand/Experimental | Campaign, launch, art, entertainment, prototype | Stronger motion is allowed with controls, reduced mode, and performance budget |

Do not let one component's motion budget escalate the whole page.

# Choreography Layers

Think in layers, then move only the useful ones:

- System: global rules, reduced-motion behavior, duration/easing tokens.
- Component: button, input, card, modal, list, tab, drawer, tooltip, toast.
- Section: hero, proof, feature story, chart, timeline, testimonial, comparison.
- Page: route transition, scroll rhythm, slide sequence, reading pace.
- Brand: recurring behavioral motif that helps memory.

Most product work should stop at system and component. Most marketing work may use section and page. Brand/experimental motion must still serve the Request Anchor.

# Motion Hierarchy

Use motion to support priority, not to make every element equal.

- L1 Current task focus: button press, focused input, active selection, changed data. Immediate, small, reliable.
- L2 Core expression: hero, key visual, product mechanism, critical proof. Memorable but sparse.
- L3 Supporting content: cards, logos, secondary modules. Subtle reveal or no motion.
- L4 Reading and data: tables, long text, legal, dense reports. Mostly static.

If L2 or L3 motion distracts from L1 work, reduce it.

# Language Decisions

For meaningful motion, define these rules before implementation:

- Trigger: load, view, hover, focus, press, drag, scroll, route change, state change, or explicit play.
- Direction: follows spatial logic, reading flow, object origin, or product metaphor.
- Duration: fast enough for repeated use, slow enough to be understood.
- Easing: matches entry, exit, continuity, or brand posture.
- Distance: small by default; large movement only when spatial meaning matters.
- Repeat: one-time unless feedback, progress, or user-controlled playback requires repetition.
- Interruption: user input should not wait for decorative animation to finish.
- Reduced motion: provide a useful still or simplified version.

# Timing Heuristics

Use these as starting points, not laws:

| Motion | Typical range |
|---|---:|
| Press/tap feedback | 80-150 ms |
| Hover/focus | 120-200 ms |
| Small state change | 150-250 ms |
| Modal/drawer/sheet | 250-400 ms |
| Section reveal | 250-500 ms |
| Page/route/slide transition | 300-600 ms |
| Hero storytelling | 600-1200 ms, only when skippable or non-blocking |

Repeated work needs shorter durations. Brand or story moments can be longer only when they do not block reading or action.

# Easing Grammar

- Ease-out: entry, reveal, object arriving at rest.
- Ease-in: exit, dismissal, object leaving attention.
- Ease-in-out: large movement, route transitions, spatial continuity.
- Linear: progress indicators, looping rotation, time-based media.
- Spring: playful microinteractions, drag release, consumer/social personality. Use sparingly and avoid for finance, medical, legal, enterprise risk, and dense tools.

Use a small set of named motion tokens. Do not invent one-off curves for every section.

# Scene Presets

| Scene | Suitable motion |
|---|---|
| Product UI/dashboard | Micro feedback, state continuity, loading/error/success, list updates. No decorative loops. |
| Marketing/portfolio site | Hero or section reveal, product mechanism, scroll-supported story. Static reading must still work. |
| B2B/enterprise | Precise, short, restrained motion that signals reliability and system state. |
| Editorial/culture | Rhythm, reveal, image/text pacing, but do not slow reading. |
| Consumer/social | Livelier feedback and characterful transitions, controlled density. |
| Finance/medical/legal/security | Minimal, literal feedback; avoid playful motion, suspense, and surprise. |
| HTML deck | Use motion only for live or interactive delivery. Read-alone/PDF/export versions default static. |
| Art/experimental | Bold motion is acceptable only with controls, reduced motion, and performance checks. |

# Scroll Motion

Use scroll motion for product stories, timelines, spatial explanations, data stories, and campaign pacing.

Rules:

- Do not hijack scroll or trap the user in ornamental sequences.
- Reveal information, relationship, or sequence; do not animate just to prove craft.
- Keep vertical reading usable without animation.
- Prefer one-time reveal or progress-bound movement over repeated scroll-trigger loops.
- Treat large parallax, rotation, scale, and pinned sections as high-risk. Use them only when they make the story clearer.

# Microinteractions

Common minimum states:

- Button: default, hover, focus, press, loading, success, error, disabled.
- Input: default, focus, filled, error, helper, disabled.
- Navigation: current, hover, focus, transition or active indicator.
- Card/list: hover/focus affordance, selection, reorder, delete/undo continuity.
- Async action: loading, partial, success, failure, retry.

Motion should make the state legible; copy still explains consequence and recovery.

# Accessibility And Safety

- Honor `prefers-reduced-motion`; reduce, fade, or remove nonessential movement.
- Do not carry critical meaning only through animation.
- Avoid flashes above three times per second.
- Auto-moving, blinking, scrolling, or updating content that lasts more than five seconds needs a way to pause, stop, hide, or control it unless it is essential.
- Avoid vestibular triggers: large zoom, rotation, depth, forced parallax, and camera-like movement.
- Provide keyboard and screen-reader paths that do not depend on hover or timed animation.

# Performance Rules

- Prefer transform and opacity.
- Avoid animating layout, large filters, shadows, background-position, or properties that cause repeated reflow/paint.
- Avoid many simultaneous animations on low-powered devices.
- Reserve media dimensions to avoid layout shift.
- Pause offscreen or hidden loops.
- Do not stack video, particles, parallax, blur, and scroll effects without a measured performance reason.

# Contract Fields

When motion matters, record a compact Motion Strategy:

- Motion purpose:
- Motion budget:
- Primary motion focus:
- Do-not-move zones:
- Trigger model:
- Duration and easing rules:
- Direction and causality rules:
- Scroll behavior:
- Reduced-motion fallback:
- Performance risks:

# Critique Checklist

Before delivery, ask:

1. Does the static artifact communicate the message and task?
2. Does every nontrivial motion have a named purpose?
3. Is the motion budget appropriate for the surface and audience?
4. Are reading, comparison, data, form, and high-risk areas quiet enough?
5. Does direction explain origin, destination, hierarchy, or causality?
6. Are timing and easing consistent rather than random?
7. Does scroll remain user-controlled?
8. Is reduced motion useful rather than broken?
9. Is performance protected by transform/opacity and limited concurrency?
10. Would removing the motion damage meaning, usability, memory, or trust? If not, remove it.

# Done Check

This concept is applied when another agent can answer:

1. Which motion purpose and budget were chosen?
2. Which regions move and which regions intentionally stay still?
3. Which duration, easing, direction, scroll, and trigger rules govern implementation?
4. How reduced motion, safety, and performance are handled?
5. Where the Motion Strategy is recorded for future agents?

# Source Notes

This concept distills the provided motion-design research into runtime OKF and cross-checks it against current official accessibility and web-performance references: WCAG 2.2.2 Pause, Stop, Hide; WCAG 2.3.1 Three Flashes or Below Threshold; WCAG 2.3.3 Animation from Interactions; MDN `prefers-reduced-motion`; and web.dev animation performance guidance. It is an operating model, not a template.
