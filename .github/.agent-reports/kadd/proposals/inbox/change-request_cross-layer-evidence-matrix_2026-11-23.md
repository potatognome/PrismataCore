# KADD Change Request: Cross-Layer Evidence Matrix

**Status:** Draft
**Date Submitted:** 2026-11-23
**Submitted By:** KADD Integrity & Cohesion Analysis Agent
**Priority:** High
**Impacted repositories:** PrismataCore (primary), PrismataSDK (evidence provider), PrismataCorp (evidence provider)
**Ownership layer:** Core cross-layer traceability; repository-specific evidence execution

## Change Summary

Define a canonical, generated cross-layer evidence matrix connecting vision and concepts to ADRs, requirements, risks, roadmap items, implementation contracts, validation artifacts, repository owners, and post-implementation records.

## Finding

Cross-layer alignment exists in imports and narrative statements, but it is not complete enough for automated integrity verification:

- requirement records lack source ADR, linked risk, roadmap item, verification method, acceptance evidence, and implementation owner;
- roadmap items lack phases, repository assignments, accountable owners, and exit gates;
- implementation contracts do not consistently reference governing requirements or validation artifacts;
- risk records lack ownership, indicators, triggers, and residual-risk treatment;
- Layer 5 records are sparse and do not consistently provide stable identity or cross-review links;
- no canonical matrix identifies unsupported requirements or implementation without architectural justification.

## Rationale

A generated or validated evidence matrix would make architectural cohesion review repeatable and expose unsupported requirements, orphaned ADRs, unowned roadmap work, missing evidence, and implementation without canonical authority.

## Suggested Change

Create a canonical matrix model or generated validation report with, at minimum, these edge types:

```yaml
evidence-edge:
  source-udi: prismata.kadd.requirements.<name>
  source-adrs: []
  linked-risks: []
  roadmap-items: []
  implementation-kads: []
  repository-owner: PrismataCore | PrismataSDK | PrismataCorp
  verification-method: validation-rule | test | review | inspection
  acceptance-evidence: []
  status: proposed | active | implemented | verified | deprecated
  last-reviewed: YYYY-MM-DD
```

Define coverage reports for:

- requirement-to-ADR missing;
- requirement-to-risk missing;
- requirement-to-roadmap missing;
- roadmap-item-to-requirement missing;
- implementation-KAD-to-governance missing;
- repository-owner missing;
- evidence-artifact missing;
- orphan ADR;
- orphan risk;
- unresolved or circular roadmap dependency.

The matrix should be a generated view or approved KAD-governed record, not a competing implementation authority.

## Impact Assessment

### Affected Areas
- [x] Layer 1
- [x] Layer 2
- [x] Layer 3
- [x] Layer 4
- [x] Layer 5
- [x] Layer 9

### Direct Dependencies
- `1-03-concepts.yaml`
- `2-04-decisions.yaml`
- `3-01-requirements.yaml`
- `3-02-risks.yaml`
- `3-03-roadmap.yaml`
- `4-01-interfaces.yaml`
- `4-02-data-model.yaml`
- `4-03-storage.yaml`
- `4-04-configuration.yaml`
- `4-05-development.yaml`
- `5-01-research.yaml`
- `5-02-lessons-learned.yaml`
- `5-03-retrospectives.yaml`
- `9-03-references.yaml`

### Risk Assessment

**Medium**

- Backfilling every edge could create false confidence or approval theater.
- Repository-specific evidence may be unavailable before implementation starts.
- Mitigation: distinguish planned traceability from verified evidence and require explicit unresolved state.
- Rollback: retain the matrix as advisory until coverage reaches approved thresholds.

### Benefit Assessment

- Repeatable cross-layer integrity checks.
- Clear ownership and repository impact.
- Better release and validation governance.
- Fewer unsupported requirements and orphaned implementations.

## Alternatives Considered

1. Keep traceability in specialist reports.
   - Rejected because reports are snapshots and cannot provide continuous validation.
2. Implement repository-local matrices separately.
   - Rejected because competing graphs would weaken Core authority.
3. Add only a requirement/roadmap table.
   - Rejected because it would omit ADR, risk, implementation, evidence, and post-implementation layers.

## Decision & Approval

- [ ] Approved
- [ ] Approved with modifications
- [ ] Deferred
- [ ] Rejected

**Principal:** Pending

## Validation

- [ ] Change request complete and clear
- [ ] Impact assessment thorough
- [ ] Alternatives considered
- [ ] All dependencies identified
