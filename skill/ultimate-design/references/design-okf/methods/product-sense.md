---
type: Method
title: Product Sense
description: Product-management judgment for design work: problem definition, user outcome, hypotheses, metrics, tradeoffs, MVP scope, and AI-product risk.
tags: [product, pm, problem-framing, metrics, mvp, validation]
---

# Purpose

Use this concept when the design is part of a product decision, not only a visual artifact. It helps the agent avoid making a polished page that solves the wrong problem.

Do not load it for pure posters, brand moodboards, small visual polish, or print collateral unless the product problem or audience is unclear.

# Product Sense Lens

Before choosing layout or visual style, translate the request into:

```text
When [specific situation],
[target user] wants to [make progress],
but [obstacle] prevents it,
causing [cost, risk, delay, or anxiety].
```

Then design from that statement, not from the surface feature request alone.

# Required Checks

- Problem before solution: decide whether the user asked for a problem, a solution, or an implementation detail.
- User and situation: make the primary audience and real usage context specific enough to guide density, language, and interaction.
- Job and outcome: name the progress the user is trying to make, plus the behavior or decision the artifact should enable.
- Alternatives: note the current workaround, competitor, manual process, or "do nothing" state when it affects positioning or UX.
- Value and tradeoff: record the user value, business value, and what the design deliberately does not optimize.
- Scope discipline: prefer the smallest useful v1, prototype, or page that can validate the riskiest assumption.
- Success signal: define a metric or observable user behavior. Use a North Star, driver, guardrail, adoption, completion, trust, retention, or qualitative signal as appropriate.
- Validation path: specify whether the work should be validated by interview, usability test, landing page, fake door, prototype, analytics, A/B test, or expert review.

# Product Type Cues

- B2B/internal tools: optimize workflow fit, permissions, handoff, auditability, efficiency, error recovery, and ROI.
- Consumer products: optimize activation, habit, emotion, trust, retention, and clear next action.
- Marketplaces/platforms: protect balance between sides, rules, incentives, and trust.
- AI products: design for uncertainty, latency, cost, hallucination risk, user correction, confidence, explainability, fallback, permissions, and human control.
- Developer products: optimize docs, API clarity, onboarding path, error messages, reliability, and examples.
- Content/community products: optimize supply quality, moderation, distribution, reputation, and healthy participation.

# AI Product UX

For AI-native interfaces, include these design requirements when relevant:

- Show inputs, sources, confidence, limits, or assumptions when trust matters.
- Provide correction, retry, edit, undo, fallback, and escalation paths.
- Make cost, latency, permissions, and safety boundaries visible where users could overtrust the system.
- Track AI-specific success and risk signals such as adoption, correction rate, hallucination rate, fallback rate, latency, cost per task, and safety events.

# Request Anchor Integration

For product-oriented tasks, fill or infer these ideas inside the Request Anchor and validation notes:

- Core job to be done: the user's progress, not merely the requested UI object.
- Success criteria: include at least one user outcome or success signal.
- Non-goals: name what v1 intentionally does not solve.
- Must preserve: source facts, constraints, data, compliance, trust boundaries, brand commitments, or existing workflow behavior.
- Validation must check against: whether the design solves the stated problem, supports the intended user behavior, and remains within the deliberate scope.

# Critique Prompts

Ask these during critique and repair:

- Is this solving the user's real problem, or only rendering the requested feature?
- Would the target user understand the value in the first screen or first state?
- Is the primary path the shortest path to the core job?
- Does the design expose enough trust, risk, cost, or status information for the product type?
- Are metrics and guardrails specific enough that a PM could tell whether v1 worked?
- Can the same learning be achieved with a smaller artifact or narrower scope?

# Done Check

The Product Sense pass is done when the artifact has a clear problem statement, target user, core job, scope boundary, success signal, and validation path, or when the agent explicitly records why those items are not relevant to the design task.
