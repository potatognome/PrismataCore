# KADD Change Request: Knowledge Vocabulary Alignment

**Status:** Draft
**Date Submitted:** 2026-11-23
**Submitted By:** KADD Knowledge Analysis Agent
**Priority:** High
**Impacted repository:** PrismataCore
**Ownership layer:** Core terminology and reference authority

## Change Summary

Resolve informal, alias, and undefined vocabulary used across Concepts, Subsystems, Requirements, Relationships, Roadmap, Configuration, and the Glossary.

## Affected KAD Documents

### Document 1
- **Filename:** `9-01-glossary.yaml`
- **Layer:** 9 (Reference)
- **Current Version:** 1.1.8
- **Proposed Version:** Subject to Principal approval

### Document 2
- **Filename:** `1-03-concepts.yaml`
- **Layer:** 1 (Definitions)
- **Current Version:** 1.0.7
- **Proposed Version:** Subject to Principal approval

### Document 3
- **Filename:** `3-01-requirements.yaml`
- **Layer:** 3 (Planning)
- **Current Version:** 1.0.6
- **Proposed Version:** Subject to Principal approval

### Document 4
- **Filename:** `2-02-subsystems.yaml`
- **Layer:** 2 (Architecture)
- **Current Version:** 1.0.7
- **Proposed Version:** Subject to Principal approval

## Change Type

- [x] Addition
- [x] Modification
- [x] Clarification
- [ ] Deletion
- [ ] Refactoring

## Finding

The glossary defines cUDI and mUDI as informal aliases, while canonical concepts and requirements use `Capability UDI` and `Manifest UDI`. Ecosystem terms `PCMS-2026`, `VILE`, and `VISE` appear in architecture, roadmap, and configuration KADs but have no glossary entries.

The Foundation report separately identified the `CapabilityUDI` subsystem placement and relationship-structure issues. These findings are terminology and ownership related and should be resolved consistently rather than through independent text changes.

## Rationale

Canonical terms improve discoverability and prevent Core/SDK/Corp implementations from adopting divergent names. Explicit alias status reduces false terminology duplication.

## Suggested Change

Add stable glossary entries or explicit aliases for:

- Capability UDI
- Manifest UDI
- PCMS-2026
- VILE
- VISE

For aliases, define canonical status explicitly:

```yaml
term: Capability UDI
acronym: null
aliases:
  - cUDI
canonical: true
```

Keep cUDI/mUDI entries if concise notation is useful, but explicitly mark them as aliases of canonical terms. Do not duplicate unrelated subsystem meanings.

Add validation that:

- every Prismata-specific term used outside the glossary is registered or explicitly marked;
- a glossary entry and aliases use one stable UDI;
- relationship or subsystem names are checked against glossary aliases;
- newly discovered undefined terms produce a provenance-gap report.

## Impact Assessment

### Affected Areas
- [x] Layer 1
- [x] Layer 2
- [x] Layer 3
- [x] Layer 4
- [ ] Layer 5
- [x] Layer 9

### Direct Dependencies
- `9-01-glossary.yaml`
- `1-03-concepts.yaml`
- `2-02-subsystems.yaml`
- `2-03-relationships.yaml`
- `3-01-requirements.yaml`
- `3-03-roadmap.yaml`
- `4-04-configuration.yaml`
- Existing capability-UDI ownership proposal

### Risk Assessment

**Medium**

- Renaming widely used labels could disrupt implementations or reports.
- Mitigation: preserve aliases and perform governance review before deprecating names.
- Rollback: retain both canonical and alias entries and defer removals.

### Benefit Assessment

- Clear terminology authority.
- Better search and graph readiness.
- Reduced duplicate definitions.
- Fewer Core/SDK/Corp interpretation conflicts.

## Alternatives Considered

### Alternative 1: Preserve all terms without canonical entries
- Pros: No immediate naming disruption.
- Cons: Undefined vocabulary persists.
- Why not selected: It conflicts with glossary authority rules.

### Alternative 2: Remove aliases
- Pros: Simplified vocabulary.
- Cons: Breaks concise established usages.
- Why not selected: Alias compatibility is necessary until implementation adoption is governed.

## Decision & Approval

- [ ] Approved
- [ ] Approved with modifications
- [ ] Deferred
- [ ] Rejected

**Principal:** Pending
