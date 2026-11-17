# KADD Change Request — Source Metadata Normalization

**Status:** Proposed  
**Date Submitted:** 2026-11-16  
**Submitted By:** Local KADD Maintenance Sweep  
**Priority:** Medium  
**Layer:** Reference and metadata governance  
**Owner:** Prismata Architecture Team

---

## Change Summary

Normalize metadata conventions across the KADD collection so the `source.last-updated` field remains the routine maintenance marker and all maintenance changes remain traceable.

## Affected Documents

- `canonical/kadd/**/*.yaml`

## Finding

The KADD update set introduced a consistent metadata maintenance model but still requires the operating discipline to preserve its date and version logic across future maintenance cycles.

## Rationale

Metadata hygiene is a low-risk but high-value governance action. It makes review and maintenance easier for both people and agents and reduces ambiguity when comparing older and newer KADD versions.

## Suggested Change

- keep `source.last-updated` as the canonical field for edit dates
- keep `version` as a patch increment indicator for maintenance updates
- apply both conventions consistently across the source collection

## Impact Assessment

### Affected Areas
- [x] Layer 1
- [x] Layer 2
- [x] Layer 3
- [x] Layer 4
- [x] Layer 5
- [x] Layer 9

### Risk Assessment
Low

### Benefit Assessment
- cleaner change history
- easier auditing
- better consistency across active KADs

## Decision

- [x] Approved for maintenance adoption
- [ ] Deferred
- [ ] Rejected

## Implementation Notes

Use the current pattern as the standard metadata maintenance rule for future KADD update cycles.
