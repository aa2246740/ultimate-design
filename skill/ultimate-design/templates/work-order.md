# Work Order: <id>

- **id:**
- **owner:**
- **status:** open | in_progress | done | blocked
- **execution:** serial | parallel
- **cluster:** Narrative | Visual | Interaction | Production | <custom>

## Request Anchor

- **request_anchor_ref:** path or section id (for example `DESIGN.md#request-anchor`)
- **request_anchor_digest:** short digest of deliverable, audience, core job, success criteria

## Input artifact

- **artifact_path:**
- **artifact_version:**
- **artifact_hash:** sha256:… | unknown

## Applicable design-contract constraints

-

## Active OKF ownership (accountable)

Primary owned concepts only. Exactly one work order is accountable per Active OKF.

- `design-okf/...`

## Primary / read OKF references

- Owned: `design-okf/...`
- Cross-read / reviewer (not ownership): `design-okf/...` — reason:

## Manifest / hash linkage

- **manifest_path:** okf-read-manifest.json
- Required blackboard file. Every owned and cross-read OKF must appear as a canonical `references/design-okf/...md` entry with `path`, `sha256`, and `owner` exactly equal to this work-order id. Absolute paths and path traversal are forbidden.

## Explicit forbidden / out-of-scope

- Forbidden writes: final HTML, final DESIGN.md, other clusters' owned decisions
- Out of scope:

## Expected result / return schema

Return a `specialist-results/<id>.md` packet with: findings, proposed changes, cluster dependencies, local verification evidence, unresolved questions, conflicts/risks, and one complete `Reference | Decision | Artifact target | Verification` row per owned Active OKF.

## Artifact targets

-

## Verification obligations

-

## Integrator merge notes

-
