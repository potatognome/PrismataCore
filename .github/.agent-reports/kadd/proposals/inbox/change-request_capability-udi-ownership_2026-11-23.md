# KADD Change Request: Capability UDI Ownership

**Status:** Draft  
**Date Submitted:** 2026-11-23  
**Submitted By:** KADD Foundation Analysis Agent  
**Priority:** High  
**Impacted repositories:** PrismataCore (primary), PrismataSDK (implementation), PrismataCorp (none by default)  
**Ownership layer:** Cross-repository Core/SDK contract

## Change Summary

Define Capability UDI as a Core identity and definition concern and explicitly state the SDK implementation, registry, and runtime responsibilities that consume it.

## Affected KAD Documents

### Document 1
- **Filename:** `1-03-concepts.yaml`
- **Layer:** 1 (Definitions)
- **Current Version:** 1.0.7
- **Proposed Version:** Subject to Principal approval

### Document 2
- **Filename:** `2-02-subsystems.yaml`
- **Layer:** 2 (Architecture)
- **Current Version:** 1.0.7
- **Proposed Version:** Subject to Principal approval

### Document 3
- **Filename:** `9-01-glossary.yaml`
- **Layer:** 9 (Reference)
- **Current Version:** 1.1.8
- **Proposed Version:** Subject to Principal approval

## Change Type

- [x] Modification
- [x] Clarification
- [ ] Addition
- [ ] Deletion
- [ ] Refactoring

## Finding

`1-03-concepts.yaml` defines `Capability UDI` as a foundational ecosystem concept. `3-01-requirements.yaml` requires every capability to possess one. However, `2-02-subsystems.yaml` places `CapabilityUDI` under the PrismataSDK subsystem block while the Core subsystem block owns UDI and schemas.

The glossary also treats `cUDI` and `mUDI` as informal aliases, while canonical concepts and requirements use `Capability UDI` and `Manifest UDI` names. The relationship is therefore unclear for Core definition ownership, SDK implementation, and cross-repository discoverability.

## Rationale

This clarification prevents duplicate or divergent capability identity implementations. It preserves Core authority over canonical identities and allows SDK to own the operational registry and runtime behavior.

Repository classification:

- **PrismataCore:** canonical term, identity definition, schema/law/relationship constraints.
- **PrismataSDK:** registry implementation, capability discovery, runtime resolution, manifest consumption.
- **PrismataCorp:** no direct ownership unless a tenant governance process explicitly adopts a policy about capability identity; archives may preserve historical records.

## Suggested Change

### Core concept clarification

Add or clarify:

```yaml
Capability UDI:
  owner: PrismataCore
  purpose: >
    Provide the canonical identity definition for a capability independent
    of a manifest or runtime implementation.
```

### Subsystem clarification

Move or explicitly split `CapabilityUDI` in the subsystem model:

```yaml
PrismataCore:
  components:
    CapabilityUDI:
      classification: Foundation Asset
      purpose: >
        Canonical identity model for capabilities.

PrismataSDK:
  components:
    CapabilityRegistry:
      classification: Registry
      purpose: >
        Runtime discovery, lookup, resolution, and composition support
        for capabilities identified by Capability UDIs.
```

### Glossary clarification

Add stable glossary entries for `Capability UDI` and `Manifest UDI`, or explicitly classify `cUDI` and `mUDI` as aliases and state canonical terms.

## Impact Assessment

### Affected Areas
- [x] Layer 1 (Definitions)
- [x] Layer 2 (Architecture)
- [x] Layer 3 (Planning)
- [x] Layer 4 (Implementation)
- [ ] Layer 5 (Knowledge)
- [x] Layer 9 (Reference)

### Direct Dependencies
- `1-03-concepts.yaml`
- `2-01-systems.yaml`
- `2-02-subsystems.yaml`
- `2-03-relationships.yaml`
- `3-01-requirements.yaml`
- `9-01-glossary.yaml`

### Risk Assessment

**Medium**

- Moving ownership in a nameplate-only way could affect SDK and Core repositories.
- Preserving no explicit implementation contract could leave the relationship ambiguous.
- Mitigation: approve a Core definition/SDK implementation split, then track repository implementation through separate change processes.
- Rollback: retain existing subsystem entry with an explicit ownership annotation if the split is deferred.

### Benefit Assessment

- Clear Core and SDK responsibilities.
- Reduced duplication risk.
- Better capability discovery and traceability.
- Stronger glossary alignment.

## Alternatives Considered

### Alternative 1: Keep CapabilityUDI in SDK
- Pros: Preserves existing subsystem wording.
- Cons: Reproduces ambiguity with Core concepts and requirements.
- Why not selected: Ownership remains inconsistent.

### Alternative 2: Move all capability behavior into Core
- Pros: Centralizes identity and behavior.
- Cons: Violates minimal executable Core and mandatory SDK runtime/tooling boundaries.
- Why not selected: It would reverse the established three-layer architecture.

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
