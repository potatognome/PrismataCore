# KADD Proposal: Source Metadata Normalization

**Status:** Proposed
**Date Submitted:** 2026-11-16
**Submitted By:** Local KADD Maintenance Sweep
**Priority:** Medium
**Layer:** Reference and governance metadata
**Owner:** Prismata Architecture Team

## Change Summary

Normalize the `source` metadata field to the `last-updated` convention and confirm date accuracy for all KAD files after the 2026-11-16 update sweep.

## Affected KADs

- all canonical KADD YAML files under `canonical/kadd/`

## Finding

The metadata convention should remain stable and explicit across the entire KADD collection. Recent updates included source metadata refreshes and patch version increments.

## Rationale

Stable metadata improves traceability and reduces ambiguity when reviewing change history or deriving release status after updates.

## Suggested Change

- standardize the metadata key as `source.last-updated`
- keep the date value aligned with actual file refresh dates
- apply patch version increments for governance/documentation changes

## Impact

- cleaner change traceability
- easier review auditing
- higher consistency across all KADD files

## Decision

Status: Proposed
Recommended outcome: adopt as the standard maintenance procedure for future KADD updates.
