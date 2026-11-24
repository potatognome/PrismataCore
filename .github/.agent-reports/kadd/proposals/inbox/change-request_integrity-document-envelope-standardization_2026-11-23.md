# KADD Change Request: Document Envelope Standardization

**Status:** Draft
**Date Submitted:** 2026-11-23
**Submitted By:** KADD Integrity & Cohesion Analysis Agent
**Priority:** High
**Impacted repository:** PrismataCore
**Ownership layer:** Core documentation discipline and cross-layer governance

## Change Summary

Define and validate a consistent canonical status, purpose, governance, ownership, validation, and lifecycle envelope across all KAD documents.

## Affected KAD Documents

- `1-00-documentation-discipline.yaml`
- All 24 remaining documents under `canonical/kadd/`
- `9-01-glossary.yaml` as the terminology authority

## Finding

The 25 canonical KAD files are mostly active and cross-linked, but envelope fields vary in depth and shape. Examples include:

- status, purpose, governance, owner, validation, review, and lifecycle fields occur in several locations but are not uniformly required or typed;
- `4-05-development.yaml` contains duplicate top-level `purpose` keys;
- record and requirement models do not consistently require stable `id`/`udi`, verification method, acceptance evidence, or implementation owner;
- status values differ between documents and nested records;
- governance ownership is predominantly a document-level architecture-team owner rather than a field for each normative record or roadmap item.

## Rationale

Standardization improves parser safety, automated review, graph construction, and Principal decisions. It reduces the need for agent-specific inference and makes purpose, authority, lifecycle, owner, and validation machine-checkable without moving implementation responsibility into Core.

## Suggested Change

Extend `1-00-documentation-discipline.yaml` with a canonical document-envelope profile and clarify that each profile is domain-appropriate rather than identical in every detail.

Minimum proposed envelope:

```yaml
document:
  udi: prismata.kad.<layer>.<name>
  version: x.y.z
  status: active
  purpose: >
    Normative or explicitly non-normative purpose.
governance:
  owner: <canonical-owner>
  repository: PrismataCore
  review-cadence: <cadence>
  supersedes: []
  superseded-by: null
validation:
  validation-method: <method>
  validation-status: validated
  required-fields: []
  forbidden-duplicates:
    - purpose
    - status
  validation-artifacts: []
```

Nested records should require:

- stable `id` or `udi`;
- explicit `status`;
- purpose or concise outcome where purpose is a normative property;
- owner or inherited-owner declaration;
- validation or verification reference appropriate to the record type;
- lifecycle fields where the record can be superseded or archived.

Suggested status taxonomy, subject to Principal approval:

- `draft`
- `active`
- `proposed`
- `approved`
- `implemented`
- `deprecated`
- `superseded`
- `archived`

## Impact Assessment

### Affected Areas
- [x] Layer 1
- [x] Layer 2
- [x] Layer 3
- [x] Layer 4
- [x] Layer 5
- [x] Layer 9

### Direct Dependencies
- `1-00-documentation-discipline.yaml`
- `1-06-doctrines.yaml`
- `3-01-requirements.yaml`
- `3-02-risks.yaml`
- `3-03-roadmap.yaml`
- `4-05-development.yaml`
- `5-01-research.yaml`
- `5-02-lessons-learned.yaml`
- `5-03-retrospectives.yaml`
- `9-01-glossary.yaml`
- `9-03-references.yaml`

### Risk Assessment

**Medium**

- Overly rigid fields could reject valid exploratory or non-normative records.
- Migration may expose many incomplete records that are useful as working context.
- Mitigation: classify fields as required, inherited, conditional, or optional by document profile; preserve draft-state exceptions until approval.

### Benefit Assessment

- Machine-checkable Core governance.
- More reliable status and validation reports.
- Reduced ambiguity and cognitive cost.
- Better cross-layer and cross-repository ownership mappings.

## Alternatives Considered

1. Rely on free-text purpose/governance/validation sections.
   - Rejected because automation and graph construction cannot enforce or compare them consistently.
2. Standardize every record identically.
   - Rejected because research, requirements, risks, roadmap items, interfaces, and lessons have materially different lifecycles.
3. Move envelope validation to SDK tooling only.
   - Rejected because Core owns the canonical validation rules and the canonical envelope.

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
