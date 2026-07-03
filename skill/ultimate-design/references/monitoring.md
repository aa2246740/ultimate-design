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

The checker should pass before claiming the published flowchart matches the skill. It verifies the ordered phases, optional monitoring boundary, critique/repair loop, typed OKF concept files, and research coverage anchors.

Static proof is appropriate when the user asks, "Can you prove the flowchart is what the skill actually says?"

## Runtime Evidence

Use a run trace only for evals, regression tests, development debugging, or when the user explicitly asks to monitor a real design run.

When the run creates a screenshotable visual artifact, runtime evidence should include the rendered screenshot folder, contact sheet, visual-validation report, or a clear reason visual verification was not run.

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
