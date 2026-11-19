# KADD Change Proposal: Proposal Lifecycle Enforcement

**Status:** Actioned
**Actioned Date:** 2026-11-19
**Date Submitted:** 2026-11-18
**Submitted By:** KADD Governance Review
**Priority:** High
**Layer:** Cross-layer governance
**Owner:** Prismata Architecture Team

## Change Summary

Enforce proposal lifecycle transitions and archive boundaries consistently across human and agent workflows.

## Lifecycle

1. Inbox
2. Active
3. Approved or Changes Requested
4. Implemented
5. Archived
6. Historical snapshot, only for superseded or completed dated cycles

## Finding

The lifecycle is documented, and all pre-2026-11-17 artifacts are historical, but no automated or periodic enforcement currently verifies status transitions.

## Rationale

A proposal should not be moved directly to historical storage without a recorded decision and implementation status.

## Suggested Change

- Keep new proposals in `proposals/inbox/`.
- Move only reviewed proposals to `proposals/active/`.
- Require status and decision rationale before archival.
- Use date-stamped archive and historical records.
- Preserve superseded reports in date-stamped historical folders.

## Decision

Status: Approved
