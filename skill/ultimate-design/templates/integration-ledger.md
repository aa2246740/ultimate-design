# Integration Ledger

- **run:**
- **integrator:**
- **mode:** portable-specialist (serial | parallel)

## Ownership map

| Active OKF | Owner work order | Reviewers | Status |
|---|---|---|---|
| `design-okf/...` | | | owned |

## Conflict matrix

| Conflict | Parties | Resolution | Owner |
|---|---|---|---|
| | | accept / rewrite / waive | |

## Co-constraint pass

| Constraint pair | Check | Result | Notes |
|---|---|---|---|
| | | pass / rewrite / waive | |

## Integration gates

- [ ] Every Active OKF has an owner work order
- [ ] Every Active binding is complete
- [ ] Conflict matrix resolved (no silent concat)
- [ ] Cross-domain accepts/waives recorded when required
- [ ] Joint co-constraint pass done
- [ ] `validate_okf_usage` (and handoff structural check if used) pass

## Final write authority

- Artifact writer: Integrator
- DESIGN.md writer: Integrator
- Specialist final writes: forbidden
