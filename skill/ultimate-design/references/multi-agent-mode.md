# Portable Specialist Mode

Optional execution protocol for Ultimate Design. The skill layer defines roles, work orders, single-writer integration, and serial degradation. Parallel spawn is a harness adapter, not a skill requirement.

Default remains single-agent. Load this file only when execution mode is **portable-specialist**.

## Protocol vs scheduling

| Decision | Owner | Meaning |
|----------|-------|---------|
| Choose **Specialist Protocol** | Integrator (semantic) | Concern clusters need deep specialist work and joint adjudication |
| Choose **parallel vs serial** | Harness adapter | Whether workers run concurrently or as sequential role-passes |

Never conflate these. Absence of spawn capability means **serial same-protocol role-passes**, not that the protocol disappears.

## Triggers (semantic, not count-based)

Select Portable Specialist mode when **at least one** holds:

- Two or more independently deep-diveable decision clusters that still need joint adjudication
- Public, high-risk, multi-domain, or multi-medium work where silent under-binding is costly
- Parallel deep analysis is worth the merge cost **and** the host can keep a single Integrator

Do **not** trigger on:

- Tiny fixes, single-decision polish, or strict existing-system UI
- Active OKF count alone (any N)
- Habit of always multi-agenting
- One agent per OKF file

## Roles

### Integrator (always present)

Owns:

- Request Anchor, audience, deliverable boundary, and primary direction
- Active OKF list, ownership map, and binding capsules (Decision | Artifact target | Verification)
- Work-order routing, conflict matrix, accept/reject/rewrite of specialist packets
- Final artifact and final `DESIGN.md` writes
- Integration pass, co-constraint pass, and verification ledger

The Integrator is never a dumb forwarder. It must hold enough binding summaries and conflict context to adjudicate.

### Concern specialists (0–N)

Own deep analysis inside assigned clusters. Output **specialist-result packets** only:

- Proposed decisions and bindings
- Failure modes and verification obligations
- Risks, cross-read requirements, and optional patch proposals

Specialists **do not** write final HTML/`DESIGN.md` unless the Integrator later applies a controlled merge of an isolated patch.

### Verifier (MVP)

MVP Verifier is the Integrator's explicit second pass (same agent or later turn). A separate process is optional, never required.

## Concern-cluster routing

Unit of work = **decision concern clusters**, not OKF files.

Routing template buckets (hints only, not fixed taxonomy):

| Bucket | Example OKF |
|--------|-------------|
| Narrative & Structure | message-model, information-architecture, ux-writing, request-integrity |
| Visual Direction | taste-engine, visual hierarchy, composition, color, type personality, brand |
| Interaction & Inclusion | state-language, responsive, a11y, semantic binding, motion |
| Medium & Production | graphic-print, media production, data-viz, i18n/legal, production verification |

### Routing algorithm

1. List Active OKF concepts after preflight.
2. Tag each with a primary decision type / cluster.
3. Group into independent decision clusters; mark required cross-reads for mutual veto.
4. Prefer about **2–4 work orders** as orchestration-cost guidance only—never an Active OKF cap or trigger.
5. Emit `work-orders/<id>.md` with ownership, Active set, cross-reads, and deliverable fields.
6. Assign every Active OKF to exactly one accountable owner work order; others may be required reviewers.

Rules:

- One OKF may be read by multiple specialists
- One decision has one accountable owner
- Do not force exclusive partitions that sever real co-constraints

## Blackboard layout

When specialist mode is on, keep a file blackboard (paths relative to the project or run root):

```text
DESIGN.md
okf-read-manifest.json          # required: path, sha256, owner coverage for every declared read
work-orders/<id>.md
specialist-results/<id>.md
integration-ledger.md           # required Specialist Protocol artifact
verification-ledger.md          # required Specialist Protocol artifact
artifact/
```

`okf-read-manifest.json` is a **required** blackboard file whenever Specialist Protocol mode is on. Normal structural validation checks nonempty `{path, sha256, owner}` coverage for every declared read pair `(OKF, work-order id)`. `--require-hashes` additionally verifies exact hashes of canonical skill-root files.

Templates live under `templates/` in this skill package:

- `templates/work-order.md`
- `templates/specialist-result.md`
- `templates/integration-ledger.md`
- `templates/verification-ledger.md`

## Work order fields (normative)

Each work order must structurally carry:

| Field | Required | Notes |
|-------|----------|-------|
| `id` | yes | Stable work-order id |
| `owner` | yes | Accountable specialist role/name |
| `status` | yes | open \| in_progress \| done \| blocked |
| `execution` | yes | serial \| parallel (scheduling only) |
| `cluster` | recommended | Routing hint, not fixed taxonomy |
| Request Anchor reference / digest | yes | Link or short digest of the frozen Request Anchor |
| Input artifact / version / hash | yes | Artifact path(s), version label, content hash when known |
| Applicable design-contract constraints | yes | Contract rules that bind this cluster |
| Active OKF ownership (accountable) | yes | Primary owned `design-okf/...` paths; **exactly one** accountable owner work order per Active OKF |
| Primary / read OKF references | yes | Owned + cross-read list; cross-reads are not ownership |
| Manifest / hash linkage | yes | Required `okf-read-manifest.json` entries (canonical `references/design-okf/...md` path, sha256, owner=work-order id) for every owned and cross-read OKF |
| Explicit forbidden / out-of-scope | yes | Non-goals and forbidden writes |
| Expected result / return schema | yes | What the specialist-result packet must return |
| Artifact targets | yes | Concrete artifact targets in scope |
| Verification obligations | yes | Checks the specialist or Integrator must evidence |
| Integrator merge notes | recommended | Conflict priorities, waive policy |

Templates: `templates/work-order.md`.

## Specialist result fields (normative)

Each specialist result must structurally carry:

| Field | Required | Notes |
|-------|----------|-------|
| `work_order_id` | yes | Must match a work order |
| `specialist` | yes | Author of the packet |
| `status` | yes | complete \| blocked \| waived |
| Source work-order linkage | yes | Same as `work_order_id`; never orphan packets |
| OKF / hash provenance | yes | Owned OKF paths and matching manifest sha256 when hashes are required |
| Findings | yes | What the deep dive discovered |
| Proposed changes | yes | Concrete design/implementation proposals |
| Dependencies on other clusters | yes | Cross-cluster waits or mutual vetoes |
| Local verification evidence | yes | What was checked locally (commands, screenshots, review notes) |
| Unresolved questions | yes | Open items for Integrator (may be "none") |
| Conflicts / risks | yes | Including mutual vetoes and failure modes |
| Binding proposals | yes | One complete row per owned Active OKF: `Reference \| Decision \| Artifact target \| Verification` |
| Explicit non-claims | recommended | What was not decided |
| Optional patch path | optional | Isolated patch only; never silent final write |

Binding rules:

- Reference must be a real `design-okf/...` path form (not free-form prose).
- Every Active OKF owned by the source work order must have a complete matching binding row.
- One complete row must not mask other unbound owned OKFs.
- Cross-read OKFs may appear as reviewer notes; they do not replace ownership bindings.

Templates: `templates/specialist-result.md`.

## Required blackboard ledgers

When Specialist Protocol mode is on, these are **required** blackboard artifacts (not optional continuity notes):

- `integration-ledger.md` — ownership map, conflict matrix, co-constraint pass, gate checklist, single-writer authority
- `verification-ledger.md` — binding verification, Request Anchor checks, rendered/production checks, validator results

`scripts/validate_agent_handoff.py` fails if either ledger is missing.

## Single-writer rule

Only the Integrator writes:

- Final deliverable artifact(s)
- Final `DESIGN.md`
- Final integration and verification ledger resolutions

Specialists write packets under `specialist-results/`. Concatenating packets without an integration pass is forbidden.

## Integration gates (before final write)

1. Every Active OKF has an owner work order.
2. Every Active binding has Decision, Artifact target, and Verification.
3. Conflict matrix is fully resolved (no silent concat).
4. If accessibility, responsive, motion, or production concepts are Active, Visual direction cannot go final without accept or explicit waive from those owners.
5. Joint co-constraint pass completed for overlapping constraints.
6. `scripts/validate_okf_usage.py` passes; when a handoff tree is present, `scripts/validate_agent_handoff.py` passes structural checks.
7. Rendered / production verification runs when applicable.

## Co-constraint pass

After specialist results land, the Integrator must re-check decisions that mutually constrain each other (examples: type personality vs WebFont payload; motion vs reduced-motion; hierarchy vs density; a11y vs visual flourish). Record accept, rewrite, or waive with owner in `integration-ledger.md`.

## Serial degradation

When the host cannot spawn concurrent workers:

1. Keep the same roles, work orders, blackboard, gates, and bans.
2. Execute work orders as sequential role-passes in one agent or one terminal.
3. Still separate specialist packets from Integrator final writes.
4. Still run integration and verification ledgers.

Serial is full protocol compliance, not a degraded doctrine.

## Ban list

1. One OKF = one agent
2. Always-on multi-agent
3. Multi-writer same HTML/`DESIGN.md`
4. Concat results without integration pass
5. Support references as fake Active
6. Active count auto-triggers parallel or specialist mode
7. Integrator as dumb forwarder
8. Harness-specific spawn API required in the core skill path
9. Fixed Active count caps (hard or soft-as-doctrine)
10. Treating 2–4 work orders as an Active OKF budget

## Active OKF admission (unchanged by multi-agent)

Portable Specialist mode does **not** invent a new Active budget. Admission remains count-free:

- Active while it adds a non-subsumed decision, failure mode, or verification obligation
- Complete binding required
- Progressive disclosure ≠ concurrent governance ceiling

## Non-normative harness notes

Adapters may accelerate scheduling; they must not rewrite protocol authority.

| Host class | Typical acceleration | Fallback |
|------------|----------------------|----------|
| Grok Build, Claude Code | `spawn_subagent` / Task tools for true parallel specialists | Serial role-passes |
| Codex, Pi, Gemini, other file-capable agents | Parallel if available; often serial | Same blackboard protocol |
| No subagent API | N/A | Serial complete protocol |

Do not put host-specific spawn APIs into the always-loaded `SKILL.md` path. Keep adapter recipes out of Active OKF governance.

## Done signal

Portable Specialist mode is complete when integration gates pass, the Integrator has written final artifact and contract, every Active binding is verified or explicitly waived with owner, and another agent can continue from the governed contract without replaying specialist chat.
