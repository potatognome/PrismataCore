# KADD Change Request: Layer 5 Record Identity and Integrity

**Status:** Draft
**Date Submitted:** 2026-11-23
**Submitted By:** KADD Knowledge Analysis Agent
**Priority:** High
**Impacted repository:** PrismataCore
**Ownership layer:** Core knowledge and post-implementation standards

## Change Summary

Standardize stable identifiers and required evidence fields across research, lessons, and retrospective records, and complete LLR-003.

## Affected KAD Documents

### Document 1
- **Filename:** `5-01-research.yaml`
- **Layer:** 5 (Post-Implementation)
- **Current Version:** 1.0.4
- **Proposed Version:** Subject to Principal approval

### Document 2
- **Filename:** `5-02-lessons-learned.yaml`
- **Layer:** 5 (Post-Implementation)
- **Current Version:** 1.0.7
- **Proposed Version:** Subject to Principal approval

### Document 3
- **Filename:** `5-03-retrospectives.yaml`
- **Layer:** 5 (Post-Implementation)
- **Current Version:** 1.0.4
- **Proposed Version:** Subject to Principal approval

## Change Type

- [x] Addition
- [x] Modification
- [x] Clarification
- [ ] Deletion
- [ ] Refactoring

## Finding

The three Layer 5 documents define mature lifecycles and required-element models, but research and retrospective record models do not require stable `id`/`udi` values. LLR-003 omits implications, recommendations, and related fields required by `lesson-record-standards.required-elements`. No actual research or retrospective record instances are populated.

Evidence:

- `5-01-research.yaml` defines `research-record-model.required-elements` but no actual research records.
- `5-02-lessons-learned.yaml` defines LLR-003 without required implication/recommendation/related elements.
- `5-03-retrospectives.yaml` defines an action-based record model but no actual records.

## Rationale

Stable record identities are necessary for citations, graph relationships, lifecycle tracking, supersession, and proposal traceability. Required-element validation prevents incomplete lessons or retrospective records from becoming accepted knowledge.

Repository classification:

- **PrismataCore:** canonical record envelope and validation rules.
- **PrismataSDK:** may implement capture/index/discovery tooling.
- **PrismataCorp:** may preserve and govern tenant-owned historical copies.

## Suggested Change

Add `id` and `udi` to the required-elements of `5-01-research.yaml` and `5-03-retrospectives.yaml`. Add validation rules that reject records missing required fields. Complete LLR-003 with its implications, recommendations, and related KAD references.

Example record-envelope additions:

```yaml
required-elements:
  - id
  - udi
  - title
  # existing evidence and outcome fields remain
```

For LLR-003, add:

```yaml
implications:
  - Knowledge should remain independent of implementation technology.
  - KAD and glossary stewardship should continue after code replacement.

recommendations:
  - Preserve architecture and historical evidence.
  - Prioritize knowledge continuity during implementation migration.

related:
  - 1-01-vision.yaml
  - 2-01-systems.yaml
  - 9-01-glossary.yaml
```

Optionally add one actual research record for the 2026-11-23 KADD review cycle and one retrospective record for the agent-sequencing and repository-boundary findings, with an explicit trace to the relevant report and proposals.

## Impact Assessment

### Affected Areas
- [ ] Layer 1
- [ ] Layer 2
- [ ] Layer 3
- [ ] Layer 4
- [x] Layer 5
- [x] Layer 9

### Direct Dependencies
- `5-01-research.yaml`
- `5-02-lessons-learned.yaml`
- `5-03-retrospectives.yaml`
- `9-01-glossary.yaml`
- `9-03-references.yaml`
- Existing specialist reports and KADD proposals

### Risk Assessment

**Medium**

- Overly strict validation could block exploratory records.
- Mitigation: require identity and core evidence fields while retaining lifecycle states for draft/incomplete work.
- Rollback: preserve draft-state exceptions until stable record schemas are approved.

### Benefit Assessment

- Improved graph identifiers.
- Better cross-review traceability.
- Consistent required elements.
- More complete and reusable post-implementation knowledge.

## Alternatives Considered

### Alternative 1: Leave Layer 5 as policy-only
- Pros: Minimal change.
- Cons: Weak operational capture and poor graph readiness.
- Why not selected: It does not use the record framework for real knowledge.

### Alternative 2: Create no identifiers and add separate indexes
- Pros: Faster initial implementation.
- Cons: Duplicate identity models and brittle joins.
- Why not selected: Stable UDI fields are already the ecosystem convention.

## Decision & Approval

- [ ] Approved
- [ ] Approved with modifications
- [ ] Deferred
- [ ] Rejected

**Principal:** Pending
