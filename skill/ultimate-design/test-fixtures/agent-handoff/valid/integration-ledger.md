# Integration Ledger

- **run:** fixture-valid
- **integrator:** integrator
- **mode:** portable-specialist (serial)

## Ownership map

| Active OKF | Owner work order | Reviewers | Status |
|---|---|---|---|
| `design-okf/content/message-model.md` | wo-narrative | information-architecture (cross-read) | owned |

## Conflict matrix

| Conflict | Parties | Resolution | Owner |
|---|---|---|---|
| none | | accept | integrator |

## Co-constraint pass

| Constraint pair | Check | Result | Notes |
|---|---|---|---|
| message vs density | hero not overcrowded | pass | |

## Integration gates

- [x] Every Active OKF has an owner work order
- [x] Every Active binding is complete
- [x] Conflict matrix resolved (no silent concat)
- [x] Cross-domain accepts/waives recorded when required
- [x] Joint co-constraint pass done
- [x] `validate_okf_usage` (and handoff structural check if used) pass

## Final write authority

- Artifact writer: Integrator
- DESIGN.md writer: Integrator
- Specialist final writes: forbidden
