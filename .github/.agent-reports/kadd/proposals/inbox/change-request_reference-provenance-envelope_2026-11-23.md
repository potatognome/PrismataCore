# KADD Change Request: Reference Provenance Envelope

**Status:** Draft
**Date Submitted:** 2026-11-23
**Submitted By:** KADD Knowledge Analysis Agent
**Priority:** Medium
**Impacted repository:** PrismataCore
**Ownership layer:** Core reference and bibliography standards

## Change Summary

Add a consistent provenance and citation envelope for internal, external, methodology, standard, historical, and conceptual reference entries.

## Affected KAD Documents

### Document 1
- **Filename:** `9-03-references.yaml`
- **Layer:** 9 (Reference)
- **Current Version:** 1.0.7
- **Proposed Version:** Subject to Principal approval

### Document 2
- **Filename:** `9-02-appendices.yaml`
- **Layer:** 9 (Reference)
- **Current Version:** 1.0.6
- **Proposed Version:** Subject to Principal approval

### Document 3
- **Filename:** `9-01-glossary.yaml`
- **Layer:** 9 (Reference)
- **Current Version:** 1.1.8
- **Proposed Version:** Subject to Principal approval

## Change Type

- [x] Addition
- [x] Modification
- [x] Clarification
- [ ] Deletion
- [ ] Refactoring

## Finding

`9-03-references.yaml` covers 22 entries across internal, methodology, standards, historical, conceptual, and future-consumer categories, but many entries lack durable source locators, publication dates, editions, access/review dates, and canonical/derived/historical classification. Appendix claims also rely mainly on descriptive prose rather than structured source links.

## Rationale

A consistent provenance envelope enables citation verification, graph navigation, review of source drift, and clear distinction between canonical authority and historical influence.

## Suggested Change

Add optional or category-appropriate fields to every reference entry:

```yaml
source-type: internal-canonical | external-standard | methodology | historical | conceptual
locator: # URL, file path, UDI, ISBN/DOI where available
publication-date: null
version: null
accessed-date: null
canonical-status: supporting | authority | historical | influence
related-kads: []
provenance-confidence: high | medium | low
```

Preserve `relevance` and `owner`, and require a `locator` or explicit reason for sources that cannot be located. Add appendix source links where a lineage or observation depends on an external or internal source.

Add validation rules that:

- internal references resolve to a canonical KAD UDI or approved artifact;
- external references include a stable locator or an explicit unavailable-locator rationale;
- references do not confer normative authority;
- source-category and glossary-alignment reports are emitted on drift.

## Impact Assessment

### Affected Areas
- [ ] Layer 1
- [ ] Layer 2
- [ ] Layer 3
- [ ] Layer 4
- [ ] Layer 5
- [x] Layer 9

### Direct Dependencies
- `9-03-references.yaml`
- `9-02-appendices.yaml`
- `9-01-glossary.yaml`
- All scoped KAD imports

### Risk Assessment

**Medium**

- Historical or inspirational sources may not have stable locators.
- Mitigation: allow explicit provenance-unavailable status and owner-confirmed historical context.
- Rollback: keep provenance fields optional until each source is verified.

### Benefit Assessment

- Better provenance quality.
- Stronger knowledge graph edges.
- Easier source refresh and review.
- Clearer authority boundaries.

## Alternatives Considered

### Alternative 1: Use free-text provenance only
- Pros: Least restrictive.
- Cons: Not machine-checkable.
- Why not selected: Reference rules already require recurring validation.

### Alternative 2: Restrict the catalog to internal canonical sources
- Pros: Strongest authority.
- Cons: Removes valuable methodology and historical context.
- Why not selected: It would contradict the intended influence and lineage scope.

## Decision & Approval

- [ ] Approved
- [ ] Approved with modifications
- [ ] Deferred
- [ ] Rejected

**Principal:** Pending
