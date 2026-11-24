# KADD Change Request: Requirement Traceability Evidence

**Status:** Draft  
**Date Submitted:** 2026-11-23  
**Submitted By:** KADD Execution Analysis Agent  
**Priority:** High  
**Impacted repository:** PrismataCore  
**Ownership layer:** Core planning standards

## Change Summary

Expand individual requirement records in `3-01-requirements.yaml` so each mandatory requirement can carry architecture, risk, roadmap, verification, acceptance, and evidence references.

## Affected KAD Document

- **Filename:** `3-01-requirements.yaml`
- **Layer:** 3 (Planning)
- **Current Version:** 1.0.6
- **Proposed Version:** Subject to Principal approval

## Finding

The declared `traceability.evidence-model` requires requirement ID, source architecture decision, linked risk, and dependent roadmap item, but every requirement record currently contains only `id`, `udi`, `type`, and `statement`. Verification method and acceptance evidence are also not modeled.

## Rationale

This gap prevents a requirement from being traced consistently from mandatory statement to ADR, risk, roadmap item, implementation evidence, and validation result. It can allow roadmap and implementation work to appear complete without a machine-readable proof chain.

## Suggested Change

Add optional or required traceability fields to each requirement record, for example:

```yaml
- id: REQ-001
  udi: prismata.kadd.requirements.universal-asset-identity
  type: structural
  statement: >
    Every ecosystem asset SHALL possess a UDI.
  source-adrs:
    - prismata.kadd.adr.universal-identity-through-udi
  linked-risks:
    - prismata.kadd.risks.udi-namespace-fragmentation
  roadmap-items:
    - prismata.kadd.roadmap.core-schema-completion
  verification:
    method: validation-rule
    acceptance-evidence: >
      Addressable asset inventory validated against UDI rules.
  implementation-owner:
    - PrismataCore
```

Exact field names and cardinalities require architecture-team review.

## Impact Assessment

- **Affected areas:** Layers 2-4 and repository-specific traceability tooling.
- **PrismataCore:** owns canonical requirement evidence fields and references.
- **PrismataSDK:** must provide runtime/tooling evidence where applicable.
- **PrismataCorp:** must provide tenant/preservation evidence where applicable.
- **Risk:** incomplete backfills could create false traceability; mitigation is staged population and validation.
- **Benefit:** stronger auditability, coverage checks, and release readiness.

## Alternatives Considered

1. Keep traceability only in narrative text.
   - Rejected because it cannot support consistent automated or cross-repository checks.
2. Define a separate external traceability table.
   - Possible, but it would duplicate the KAD evidence model and separate canonical requirements from their traceability.

## Decision & Approval

- [ ] Approved
- [ ] Approved with modifications
- [ ] Deferred
- [ ] Rejected

**Principal:** Pending
