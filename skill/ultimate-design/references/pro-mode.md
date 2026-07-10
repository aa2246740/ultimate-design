# Pro Mode

Use this branch only after the user invokes `--pro`, asks for explicit design consensus, or supplies a decision bundle that should be frozen before execution.

## Consensus

Confirm only high-impact choices: audience, deliverable, message hierarchy, content scope, brand posture, taste dials, color commitment, type personality, layout model, imagery/assets, interaction or export constraints, and acceptance criteria. Ask compact batches. Infer harmless details and record risky defaults.

Consensus is complete when unresolved choices can no longer change the audience, core message, primary task, production validity, or design direction.

## Decision Snapshot

Record:

- Agreed audience and core job.
- Deliverable and production constraints.
- Message and action hierarchy.
- Visual posture, taste dials, color, type, layout, imagery, and motion choices.
- Must-preserve constraints and explicit non-goals.
- Acceptance criteria and true blockers still open.

The snapshot freezes agreed choices. Re-open one only when new evidence makes execution unsafe, invalid, or pointed at the wrong outcome.

## Post-Consensus Gate

1. Record the Request Anchor and Decision Snapshot. In monitored eval mode, create `.ultimate-design/runs/<timestamp>-<slug>.md` immediately with every phase `pending`.
2. Load the selected branch, `content-model.md`, `design-contract.md`, `visual-verification.md`, `quality-gates.md`, and at most two directly relevant task-facing OKF concepts. Do not automatically load DESIGN.md governance concepts when the lean contract template and validator already settle the schema. In `DESIGN.md`, list task-facing concepts under `### Active OKF Concepts` and branch, workflow, governance, index, and verification reads under `### Support References`. Support references do not consume the active concept budget or require decision-binding rows unless they change a concrete artifact decision.
3. For a screenshotable deliverable, create the visible artifact skeleton with real content and responsive structure before expanding the full contract.
4. Create or update a compact `DESIGN.md`, then refine artifact and contract together.
5. Critique, repair, second-critique, verify, govern, and deliver.

In monitored eval mode, a run that creates only `DESIGN.md` fails. No applicable phase may remain `pending`. Use one visual verification path unless it fails. After Govern passes, write `.ultimate-design/runs/<timestamp>-<slug>.complete.json` with `status`, `trace`, `artifacts`, `verification`, `remaining_risks`, and `final_summary`, then deliver without expanding the scope.

## Done Criteria

Pro delivery is done when the artifact implements the frozen snapshot, every active OKF concept has a verified decision binding, critique/repair has no unresolved P0/P1, rendered evidence exists where practical, and the governed contract lets another agent continue without reopening settled choices.

When a restricted process cannot launch the pinned browser, use the cmux + Computer Use fallback when available so visible defects are still inspected. Record it separately from machine proof; Pro mode must not relabel a blocked Rendered UI Audit as passed.
