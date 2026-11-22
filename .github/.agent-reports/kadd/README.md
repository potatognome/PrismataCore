# KADD Review and Archive Workflow

This directory manages the operational lifecycle for KADD proposals, reviews, and archival decisions.

## Directory Structure

- `proposals/inbox/` — newly identified or newly received proposals ready for review.
- `proposals/active/` — proposals under review or awaiting implementation.
- `proposals/approved/` — accepted proposals that have been approved for implementation.
- `proposals/rejected/` — proposals declined or superseded by a later decision.
- `reviews/` — review records, change notes, and recommendation memos.
- `archive/` — current operational archive for approved and superseded artifacts.
- `historical/` — long-lived legacy snapshots retained for traceability.
- `templates/` — reusable review and archival templates. KADD change proposals use the single authoritative repository template at `.github/kad-change-proposal.template.md`.

## Lifecycle

1. Proposal enters `proposals/inbox/`.
2. A reviewer records findings in a file under `reviews/` or in the proposal itself.
3. The proposal is moved to `proposals/active/` when under review.
4. The file is updated with either:
   - `Status: Approved`
   - `Status: Changes Requested`
   - `Status: Rejected`
5. When implementation is complete, the proposal is archived to `archive/` and the final accepted version is retained in `historical/` as needed.

## Status Values

- Proposed
- In Review
- Changes Requested
- Approved
- Implemented
- Archived
- Rejected

## Review Standards

- Proposals must identify scope, impact, dependencies, and owner.
- Reviews must distinguish between recommendation and decision.
- Final decisions should capture rationale and follow-up actions.
- Historical snapshots remain preserved for traceability and governance memory.

## Practical Rule

The canonical KADs under `canonical/kadd/` remain the normative reference set. The files in this directory are operational governance artifacts that track review, change, and archival activities around those documents.
