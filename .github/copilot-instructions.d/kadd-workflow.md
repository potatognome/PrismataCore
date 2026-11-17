# KADD Change Proposal and Archive Workflow

The KADD governance workflow is a repeatable review cycle for proposals, reviews, implementation, and archival decisions.

## Operating Model

- Canonical KAD files in `canonical/kadd/` are the normative reference set.
- `.github/.agent-reports/kadd/` is the operational governance workspace for proposals and review records.
- Every proposal or review artifact must preserve a clear status and archival destination.

## Required Lifecycle

1. Proposal creation in `.github/.agent-reports/kadd/proposals/inbox/` or `proposals/active/`.
2. Review documentation in `.github/.agent-reports/kadd/reviews/` or inline within the proposal.
3. Decision update indicating one of: Proposed, In Review, Changes Requested, Approved, Implemented, Archived, Rejected.
4. Archive of final accepted or superseded artifacts in `.github/.agent-reports/kadd/archive/` and retention in `.github/.agent-reports/kadd/historical/` when traceability matters.

## Documentation Rules

- Maintain current status in the document header.
- Record owner, review date, and decision rationale.
- Distinguish between a recommendation and the final decision.
- Preserve prior versions in historical archives when the document materially changes.

## KADD Review Practices

- Proposals should identify impacted KADs, dependencies, risk, and owner.
- Reviews should assess evidence, governance fit, and archive implications.
- Implementations should update the proposal record and status notes once completed.
- Archival should record what was adopted, superseded, or rejected and why.

## Templates

Use the templates in `.github/.agent-reports/kadd/templates/` for standard workflow entries:

- `proposal-template.md`
- `review-template.md`
- `archive-template.md`

## Governance Principle

The value of KADD is not only in creating documents; it is in preserving a disciplined chain of review, decision, implementation, and archival memory.
