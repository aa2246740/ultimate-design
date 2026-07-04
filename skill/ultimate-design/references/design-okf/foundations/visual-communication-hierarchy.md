---
type: Design Foundation
title: Visual Communication And Information Hierarchy
description: Coordinates intent, information priority, message hierarchy, visual hierarchy, attention, reading path, understanding, action, and ethical boundaries.
tags: [visual-communication, hierarchy, attention, reading-path, action, ethics]
---

# Purpose

Use this concept before designing or critiquing any artifact whose success depends on users seeing, understanding, remembering, or acting on information: pages, screens, decks, posters, reports, dashboards, social graphics, and data stories.

This concept is the coordination layer. Use `message-model.md` for content hierarchy details, `visual-hierarchy.md` for emphasis levers, and `gestalt-composition.md` for grouping and composition mechanics.

# Core Chain

Good design organizes attention so users can understand and act:

```text
Design intent
-> information priority
-> message hierarchy
-> visual hierarchy
-> attention
-> reading path
-> Gestalt grouping
-> understanding
-> action
```

Do not start with style. First decide what the artifact must communicate, what users should notice first, how they should read through it, and what they should do next.

# Communication Layers

Design communicates more than literal copy. Check six layers:

- Information: what is this, what facts matter, what data is shown.
- Function: what can users do, what state or operation is available.
- Structure: what is primary, secondary, grouped, sequenced, or optional.
- Emotion: what mood, urgency, trust, caution, or energy the artifact conveys.
- Brand: who is speaking and what identity or posture is recognizable.
- Action: what the user should do next and what happens after.

# Information Priority

Information priority is the source of both message hierarchy and visual hierarchy. Rank information before layout.

Use these factors when evidence is available:

- User goal: what the user is trying to accomplish now.
- Business goal: what outcome the product, brand, or sender needs.
- Decision value: whether the information changes a choice.
- Risk or consequence: whether missing it causes error, loss, confusion, or mistrust.
- Urgency: whether it is time-sensitive.
- Frequency: whether it is needed often.
- Context necessity: whether this moment requires it.

Classify information:

- Critical: must be noticed immediately.
- Important: supports the main decision soon after.
- Useful: helps after orientation.
- Optional: auxiliary, low-frequency, or deferrable.

# Message To Visual Mapping

Write message hierarchy before choosing visual emphasis:

- L1 Primary message: the one thing users should remember.
- L2 Secondary message: what explains or qualifies L1.
- L3 Supporting information: details, features, specs, or body content.
- L4 Evidence and trust: proof, data, source, testimonial, certification, or risk reducer.
- L5 Action: the next step or decision.

Then map visual hierarchy to that message hierarchy:

- L1 usually receives the strongest focal treatment.
- L2 should be discoverable immediately after L1.
- L3 should not compete with L1/L2.
- L4 should appear close to the decision it supports.
- L5 should be visible, specific, and visually distinct from secondary actions.

Message hierarchy asks what should be important. Visual hierarchy asks how that importance becomes visible. Color is an amplifier, not the skeleton; establish hierarchy first with size, position, spacing, grouping, and type.

# Attention

Users do not inspect every element equally. First attention is shaped by both stimulus salience and user goals:

```text
first attention = salience x user goal x structure x reading culture x meaning
```

Use bottom-up cues deliberately: size, contrast, saturated color, motion, position, isolation, imagery, and faces can attract attention. Use top-down cues deliberately: task words, expected controls, prices, risk information, familiar labels, and search intent guide goal-driven scanning.

Do not encode absolute myths such as "image always beats text", "face always wins", or "warm color always converts". Verify against the task and context.

# Reading Path

Define the intended start, end, and intermediate nodes.

Common path models:

- F pattern: scan-heavy text, lists, search results, or weakly guided pages. Treat it as an observed fallback, not an ideal template.
- Z pattern: simple posters, heroes, or single-screen marketing flows.
- Layer-cake: sectioned pages where users scan headings before details.
- Spotted pattern: users hunt for keywords, numbers, links, prices, or names.
- Modular grid: dashboards, cards, catalogs, and comparison surfaces.
- Task flow: forms, onboarding, setup, checkout, approval, and operation flows.

Language direction and culture change the path. Recheck paths for Chinese vertical text, RTL, dense bilingual layouts, and mobile crops.

# Understanding And Action

Understanding happens in four steps:

1. Perception: users notice the elements.
2. Organization: users group them.
3. Decoding: users infer meaning.
4. Mapping: users know what they can do next.

Reduce cognitive load with grouping, progressive disclosure, plain language, consistent terms, and image-text alignment. Text and visuals should reinforce the same message; decorative or contradictory imagery weakens understanding.

Action usually needs five conditions:

- The action entry is visible.
- The user understands what will happen.
- The value is worth the effort.
- Cost, risk, or fear is reduced.
- Feedback or trust makes the result believable.

Write CTAs as action plus object or result. Keep risk, cost, consequence, and trust information close to the decision point.

# Ethics

Information hierarchy should clarify choices, not manipulate unclear choices.

Reject:

- Fake urgency or false scarcity.
- Misleading primary CTAs.
- Hidden costs, subscriptions, cancellations, or consequences.
- Shame-based refusal copy.
- Ads or sponsored content disguised as independent content.
- Visual treatment that hides risk while exaggerating benefit.

# Workflow

1. List all candidate information.
2. Rank it with information-priority factors.
3. Write L1-L5 message hierarchy.
4. Draft a low-fidelity or grayscale structure before decorative color.
5. Apply visual levers in order: size, position, spacing, grouping, type, contrast, color, imagery, motion.
6. Check the intended reading path from first focus to action.
7. Verify with the lightest useful method: squint test, grayscale test, 5-second test, task test, rendered screenshot review, analytics, or user research.

# Contract Fields

Record:

- Communication intent.
- Information priority: Critical, Important, Useful, Optional.
- L1-L5 message hierarchy.
- Intended first focus and reading path.
- Action path and risk reducers.
- Ethical risks or dark-pattern exclusions.
- Verification method and evidence.

# Done Check

This pass is done when another agent can answer four questions without reading the implementation:

1. What is the artifact trying to communicate?
2. What should users see first?
3. How should users understand the relationship between elements?
4. What should users know or do next?

If the strongest visual element is not the most important communication element, fix the hierarchy or record why the exception is intentional.

# Source Notes

Research basis includes NN/g visual hierarchy, F-pattern, proximity, and common-region guidance; CDC Clear Communication Index guidance on main message, visual cues, visual support, and CTA; Don Norman on signifiers; WCAG contrast requirements; Material Design tokens and type scale; FTC dark-pattern guidance; data.europa and Claus Wilke chart-title and annotation guidance. Treat specific patterns as context-sensitive, not universal laws.
