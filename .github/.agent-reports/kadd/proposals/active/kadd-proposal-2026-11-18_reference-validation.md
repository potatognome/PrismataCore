# KADD Change Proposal: Reference and Glossary Validation

**Status:** Proposed
**Date Submitted:** 2026-11-18
**Submitted By:** KADD Reference Review
**Priority:** Medium
**Layer:** Layer 9
**Owner:** KADD Reference Steward

## Change Summary

Add a recurring validation pass connecting the canonical glossary, appendices, references, and terminology used across KAD files.

## Affected Documents

- `canonical/kadd/9-reference/9-01-glossary.yaml`
- `canonical/kadd/9-reference/9-02-appendices.yaml`
- `canonical/kadd/9-reference/9-03-references.yaml`
- All canonical KAD files containing ecosystem or governance terminology

## Finding

The reference layer is mature and stable, but repeated terminology and workflow changes increase the risk of drift across appendices and canonical documents.

## Rationale

The glossary is authoritative; appendices and references should reinforce rather than silently reinterpret its meanings.

## Suggested Change

1. Validate glossary terms used in each KAD.
2. Detect aliases, duplicate terms, and undefined ecosystem vocabulary.
3. Report appendix and reference provenance gaps.
4. Preserve first-class IDs and UDIs for glossary entries.

## Decision

Status: Approved with Modifications
