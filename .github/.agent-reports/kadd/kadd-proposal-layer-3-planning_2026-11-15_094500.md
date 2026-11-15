# KADD Change Request Template

**Status:** Proposed  
**Date Submitted:** 2026-11-15  
**Submitted By:** KADD Review Agent  
**Priority:** High

---

## Change Summary

**One-sentence summary of the proposed change:** Strengthen the planning layer by making requirement-to-risk-to-roadmap traceability explicit and reviewable so the roadmap remains dependable and governance-friendly.

---

## Affected KAD Document(s)

### Document 1
- **Filename:** `3-planning/3-01-requirements.yaml`
- **Layer:** 3 (Planning)
- **Current Version:** 1.0.0+
- **Proposed Version:** 1.1.0

### Document 2
- **Filename:** `3-planning/3-02-risks.yaml`
- **Layer:** 3 (Planning)
- **Current Version:** 1.0.0+
- **Proposed Version:** 1.1.0

### Document 3
- **Filename:** `3-planning/3-03-roadmap.yaml`
- **Layer:** 3 (Planning)
- **Current Version:** 1.0.0+
- **Proposed Version:** 1.1.0

---

## Change Type

- [ ] Addition (new content)
- [x] Modification (existing content change)
- [ ] Deletion (removal of content)
- [ ] Refactoring (restructuring without semantic change)
- [x] Clarification (improved language/documentation)

---

## Finding

The planning layer is well-structured and aligned with project intent, but it is not yet explicit enough about how requirements lead to risk management and roadmap sequencing. A strong plan should make its decision traceability auditable, because this is where governance and execution confidence are established.

---

## Rationale

Roadmaps are only as strong as their visible dependency logic. A project can appear aligned on paper while still lacking a transparent path from requirement to risk mitigation to execution priority. Explicit traceability lowers review cost and improves governance confidence.

---

## Suggested Change

### Detailed Change Description
- Add explicit dependency fields or linkage sections for each requirement, risk, and roadmap milestone.
- Record when a roadmap item is derived from a requirement or architectural decision.
- Document ownership and closure conditions for high-risk issues.
- Make review and approval criteria explicit within each roadmapping record.

### Proposed Content
```yaml
relations:
  traceability:
    requirements:
      - prismata.kad.planning.requirements
    risks:
      - prismata.kad.planning.risks
    roadmap:
      - prismata.kad.planning.roadmap
```

---

## Impact Assessment

### Affected Areas
- [ ] Layer 1 (Definitions)
- [x] Layer 2 (Architecture)
- [x] Layer 3 (Planning)
- [ ] Layer 4 (Implementation)
- [ ] Layer 5 (Knowledge)
- [ ] Layer 9 (Reference)

### Direct Dependencies
- `2-04-decisions.yaml`
- `3-01-requirements.yaml`
- `3-02-risks.yaml`
- `3-03-roadmap.yaml`
- `4-01-interfaces.yaml`

### Risk Assessment
**Medium**

- Risk is modest but meaningful if dependency mapping is not handled carefully.
- The main challenge is preserving the planning logic while making it more explicit.

### Benefit Assessment
- Better governance confidence
- Easier review and execution planning
- Reduced ambiguity about priorities and dependencies

---

## Alternatives Considered

### Alternative 1
- Keep dependency logic implicit and rely on human interpretation.
- Pros: Minimal work
- Cons: Weakens operational traceability and review readiness

### Alternative 2
- Rewrite the full planning layer around a new taxonomy.
- Pros: Stronger structure
- Cons: High churn and unnecessary complexity

---

## Decision & Approval

### Decision
- [x] Approved with modifications
- [ ] Deferred
- [ ] Rejected

### Approved By
- **Principal:** Pending review

---

## Implementation

### Implementation Date
- **Target:** 2026-11-17
- **Actual:** Pending

### Implementation Notes
This change should be implemented only after validating that it preserves the planning layer’s current intent while improving explicit traceability.

---

## Validation

### Pre-Implementation Validation
- [x] Change request complete and clear
- [x] Impact assessment thorough
- [x] Alternatives considered
- [x] All dependencies identified

### Post-Implementation Validation
- [ ] Change successfully implemented
- [ ] CMF compliance verified
- [ ] Related documents updated
- [ ] No unintended side effects
- [ ] Documentation complete
