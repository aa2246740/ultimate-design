# Monitoring And Evidence

Use this reference only in development/testing mode: when the user asks whether the workflow really ran, wants proof, asks for evals, or needs repeatable monitoring. Do not enable this during ordinary design work unless the user explicitly asks for monitoring or proof.

## Principle

There are two kinds of evidence:

- **Static flow proof:** a deterministic check that `SKILL.md`, branch references, and OKF files contain the expected workflow structure.
- **Runtime evidence:** a trace from one concrete test run showing which phases executed and what evidence each phase used.

Neither kind proves that the design is excellent. Visual quality still depends on rendered output, accessibility checks, tests, stakeholder review, and user feedback.

## Static Flow Proof

Run the bundled checker from the skill root or pass the skill path explicitly:

```bash
python3 scripts/flow_check.py
python3 /path/to/ultimate-design/scripts/flow_check.py /path/to/ultimate-design
```

The checker should pass before claiming the published flowchart matches the skill. It verifies the ordered phases, optional monitoring boundary, research-ingestion boundary, critique/repair loop, typed OKF concept files, and research coverage anchors.

Static proof is appropriate when the user asks, "Can you prove the flowchart is what the skill actually says?"

## Runtime Evidence

Use a run trace only for evals, regression tests, development debugging, or when the user explicitly asks to monitor a real design run.

When the run creates a screenshotable visual artifact, runtime evidence should include the rendered screenshot folder, contact sheet, visual-validation report, or a clear reason visual verification was not run.

For Pro mode end-to-end evals, consensus confirmation and artifact delivery are separate evidence points:

- The confirmation turn passes only when it asks compact decision questions and does not create artifacts.
- The post-consensus delivery turn passes only when it creates a visible artifact, a design contract or compact contract update, critique/repair evidence, rendered verification evidence, and a run trace.
- A post-consensus delivery turn that creates only `DESIGN.md`, or only plans the artifact, is a failed delivery turn even if the contract is high quality.
- For screenshotable deliverables, the visible artifact skeleton should be created before a full `DESIGN.md` draft. If `DESIGN.md` is the first substantial output and no artifact follows promptly, the run has stalled in contract drafting.
- The trace should be created early, before long rationale or optional OKF expansion, so timeout failures still show which phase stalled.
- Update the trace as phases complete. A table that still says `pending` for applicable phases is not runtime proof, even if all phase names appear.
- After rendered visual verification passes, do not run duplicate visual validators unless diagnosing a failure; spend the remaining budget on repair, contract validation, trace governance, and final delivery.

## Run Trace Location

Prefer this path when working in a project:

```text
.ultimate-design/runs/<timestamp>-<slug>.md
```

If writing files is inappropriate, include a compact trace table in the final response.

## Required Trace Table

Each phase records status and evidence:

| Phase | Status | Evidence | Open Risk |
|---|---|---|---|
| Orient | pending/pass/blocked/not-run | files, screenshots, assets, or notes read | |
| Brief | pending/pass/blocked/not-run | inferred brief, question asked, and Request Anchor created | |
| Request Anchor | pending/pass/blocked/not-run | original request, latest override, deliverable, core job, success criteria, non-goals, must-preserve, validation checks | |
| Contract | pending/pass/blocked/not-run | DESIGN.md created/updated or reason skipped | |
| OKF | pending/pass/blocked/not-run | concepts loaded from design-okf | |
| Branch | pending/pass/blocked/not-run | branch reference loaded | |
| Direction | pending/pass/blocked/not-run | chosen strategy | |
| Artifact | pending/pass/blocked/not-run | files/assets/specs created | |
| Critique 1 | pending/pass/blocked/not-run | findings and severity | |
| Repair | pending/pass/blocked/not-run | fixes applied or blocked | |
| Critique 2 | pending/pass/blocked/not-run | no P0/P1 or remaining risk | |
| Verify | pending/pass/blocked/not-run | browser/a11y/responsive/print/tests | |
| Govern | pending/pass/blocked/not-run | contract/review log updated | |
| Deliver | pending/pass/blocked/not-run | final summary | |

## Status Meanings

- `pass`: phase completed with evidence.
- `blocked`: phase could not proceed without external input.
- `not-run`: phase did not apply or the environment lacked tools; explain why.
- `pending`: phase is not done yet and final delivery should not happen.

## Minimum Delivery Rule

In monitored eval mode, do not claim the full workflow ran unless every applicable phase is `pass`, `blocked`, or `not-run` with evidence. No applicable phase should remain `pending` at final response.

For screenshotable artifact evals, `Artifact`, `Critique 1`, `Repair`, `Critique 2`, `Verify`, `Govern`, and `Deliver` are applicable unless the task explicitly excludes implementation. `Verify` is not satisfied by running a validator help command; it requires checking the created artifact or recording why artifact verification could not run.

`Run trace exists and covers all monitored phases` means each applicable phase has a non-`pending` status and evidence. Presence of the phase label alone is insufficient.

## Completion Seal

For automated development tests, create a machine-readable seal after Govern and before the final chat response:

```text
.ultimate-design/runs/<timestamp>-<slug>.complete.json
```

Minimum schema:

```json
{
  "status": "pass",
  "trace": ".ultimate-design/runs/<timestamp>-<slug>.md",
  "artifacts": ["index.html", "DESIGN.md"],
  "verification": {
    "visual_report": ".ultimate-design/runs/<timestamp>-visual/visual-report.json",
    "contract_validator": "pass",
    "negative_letter_spacing": "pass"
  },
  "remaining_risks": [],
  "final_summary": "Short user-facing delivery summary."
}
```

The seal is valid only when the trace has no applicable `pending` phases and the artifact evidence already exists. A development watchdog may stop the process after a valid seal appears; the final chat response is then redundant for proving the workflow.

Do not claim professional quality in any mode if:

- The task is long/content-heavy/drift-prone and no Request Anchor was recorded.
- The final artifact was not checked against the Request Anchor.
- Critique 1 found P0/P1 issues and no repair or second critique happened.
- Visual verification was possible but skipped.
- The contract was required but not created or updated.
- Open assumptions materially affect the design direction and were not recorded.

## Eval Evidence

For actual skill validation, use realistic tasks and compare outputs:

- With-skill output versus baseline output.
- Human review of visual output.
- Checks for DESIGN.md quality, phase trace completeness, critique/repair evidence, responsive/a11y notes, and final artifact quality.

Static checks prove only structure and coverage. They do not prove the design outcome.
