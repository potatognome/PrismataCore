# KADD Change Request: Relationship KAD Hierarchy

**Status:** Draft  
**Date Submitted:** 2026-11-23  
**Submitted By:** KADD Foundation Analysis Agent  
**Priority:** High  
**Impacted repository:** PrismataCore  
**Ownership layer:** Core canonical architecture

## Change Summary

Correct the YAML hierarchy and relationship coverage in `2-03-relationships.yaml` so relationship groups are peers and relationship entries are discoverable as intended.

## Affected KAD Documents

### Document 1
- **Filename:** `2-03-relationships.yaml`
- **Layer:** 2 (Architecture)
- **Current Version:** 1.0.7
- **Proposed Version:** 1.0.8, subject to Principal approval

## Change Type

- [x] Modification
- [x] Clarification
- [ ] Addition
- [ ] Deletion
- [ ] Refactoring

## Finding

`2-03-relationships.yaml` currently has:

1. `Schema-to-PSO` and `Schema-to-ExampleObject` nested under `Schema-to-Artifact` instead of as peers within `schema-relationships`.
2. `registry-relationships`, `ecosystem-relationships`, and `tenant-relationships` indented beneath `capability-relationships`, making them capability children in the YAML model.
3. No explicit relationship between PrismataSDK and PrismataCorp.
4. No explicit archive-to-vault, archive-to-provenance, or vault/tenant-governance relationship.

## Rationale

The intended model says relationship groups describe ownership, dependencies, and cardinality at the ecosystem architecture level. Incorrect indentation changes the machine-readable structure and may cause registry, ecosystem, and tenant relationships to be omitted or misclassified by validators, graph tools, or future agents.

## Suggested Change

### Current Content

The relevant hierarchy has the following shape:

```yaml
cardinalities:
  identity-relationships: ...
  schema-relationships:
    Schema-to-Artifact:
      ...
      Schema-to-PSO:
        ...
      Schema-to-ExampleObject:
        ...
  law-relationships: ...
  capability-relationships:
    ...
    registry-relationships:
      ...
    ecosystem-relationships:
      ...
    tenant-relationships:
      ...
```

### Proposed Structure

```yaml
cardinalities:
  identity-relationships: ...
  schema-relationships:
    Schema-to-Artifact: ...
    Schema-to-PSO: ...
    Schema-to-ExampleObject: ...
  law-relationships: ...
  capability-relationships: ...
  registry-relationships: ...
  ecosystem-relationships:
    PrismataCore-to-PrismataSDK: ...
    PrismataCore-to-PrismataCorp: ...
    PrismataSDK-to-PrismataCorp: ...
    EcosystemConsumer-to-PrismataLayer: ...
  tenant-relationships:
    Tenant-to-Workspace: ...
    Tenant-to-Vault: ...
    Tenant-to-SchemaOverride: ...
    Tenant-to-SchemaExtension: ...
    Tenant-to-Archive: ...
    Archive-to-Provenance: ...
    Vault-to-TenantGovernance: ...
```

The exact descriptions and cardinalities require Principal/architecture-team review. The change request does not prescribe implementation or storage details.

## Impact Assessment

### Affected Areas
- [x] Layer 1 (Definitions)
- [x] Layer 2 (Architecture)
- [x] Layer 3 (Planning)
- [ ] Layer 4 (Implementation)
- [ ] Layer 5 (Knowledge)
- [ ] Layer 9 (Reference)

### Direct Dependencies
- `2-01-systems.yaml`
- `2-02-subsystems.yaml`
- `3-01-requirements.yaml`
- `9-01-glossary.yaml`

### Risk Assessment

**Medium**

- YAML hierarchy could remain semantically unclear if only indentation is repaired.
- Adding relationships beyond evidence could over-constrain SDK/Corp implementation.
- Mitigation: retain architecture-level cardinalities and require governance review.
- Rollback: restore the prior hierarchy only if no approved replacement is available.

### Benefit Assessment

- Correct machine-readable relationship structure.
- Improved discoverability and graph traversal.
- Better validation and cross-layer traceability.
- Cleaner separation of relationship categories.

## Alternatives Considered

### Alternative 1: Leave hierarchy unchanged
- Pros: No immediate document churn.
- Cons: Automated parsing remains unreliable.
- Why not selected: The structural defect has direct analysis and tooling consequences.

### Alternative 2: Add nested relationships without changing existing shape
- Pros: Minimal diff.
- Cons: Preserves ambiguous ownership and capability nesting.
- Why not selected: It would not resolve the root hierarchy issue.

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
