---
type: Governance Concept
title: Request Integrity
description: Prevent requirement drift in long design runs by preserving a compact request anchor and checking it before critique, verification, and delivery.
tags: [request-anchor, requirement-drift, validation, brief, traceability]
---

# Purpose

Use this concept when a design task is long, content-heavy, multi-file, multi-phase, or likely to exceed the agent's short-term attention. It keeps the original user need visible through critique, verification, and final delivery.

# Principle

Do not turn every user request into a temporary OKF bundle. OKF is for reusable design knowledge. A user's task-specific request is runtime state and should be captured in a compact `Request Anchor`.

The `Request Anchor` is the source of truth for what this run is supposed to accomplish. It is not a full PRD. It is a guardrail against drifting from "what the user asked for" into "what the design process tends to produce."

# Request Anchor Fields

Record these fields as soon as the brief is safe enough to proceed:

- Original user request: quote or concise faithful paraphrase of the initiating request.
- Latest user override: the newest instruction that changes scope, style, output, priority, or constraints.
- Deliverable: the concrete thing to create or change.
- Primary audience: who must understand or use the artifact.
- Core job to be done: the main user outcome, not the internal method.
- Success criteria: what must be true for the user to accept the result.
- Non-goals: what this run should not spend effort on.
- Must preserve: source facts, brand constraints, data, wording, assets, or behavior that must not be lost.
- Validation must check against: a short list of user-need checks to run before delivery.

# When To Persist

Persist the anchor in `DESIGN.md` when the design contract is created or updated.

Use a compact inline note or run trace when:

- The task is a one-off graphic or small polish pass.
- Writing project files is inappropriate.
- The user explicitly asks only for an audit or explanation.

In monitored eval mode, include the Request Anchor in the run trace.

# Update Rules

- If the user changes the task, update `Latest user override` and any affected fields.
- If the agent infers a missing detail, record it as an assumption, not as original user intent.
- If two user instructions conflict, the latest instruction wins and the conflict is noted.
- If the deliverable changes, update the anchor before continuing.
- If a request is ambiguous but not blocking, proceed with a conservative assumption and record it.

# Critique And Verification

Before critique, ask:

- Does the artifact still solve the core job to be done?
- Does the first screen or first view answer the user's actual request?
- Did the process add attractive but irrelevant material?
- Did any critical source content get lost, softened, or reordered against the user's need?
- Are non-goals respected?

Before final delivery, explicitly compare the artifact against `Validation must check against`.

# Drift Signals

Watch for:

- The design becomes a generic landing page, dashboard, or brand system when the user asked for a specific visualization or explanation.
- The artifact optimizes for style while losing the requested content.
- The agent spends more words explaining the process than delivering the requested artifact.
- The final verification checks generic quality gates but not the user-specific success criteria.
- The contract contains many design decisions but no quote or faithful paraphrase of the request.

# Done Check

Request integrity is done when the run has a Request Anchor, the artifact was critiqued against it, verification includes user-specific success criteria, and the final response names any unresolved mismatch.
