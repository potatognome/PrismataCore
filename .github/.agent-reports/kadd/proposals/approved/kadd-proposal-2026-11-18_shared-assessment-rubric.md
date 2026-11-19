# KADD Change Proposal: Shared Assessment Rubric Gate

**Status:** Proposed
**Date Submitted:** 2026-11-18
**Submitted By:** KADD Orchestration Workflow
**Priority:** High
**Layer:** Cross-layer governance
**Owner:** KADD Agent Maintainers

## Change Summary

Make the five common rubric fields mandatory in every specialist and composite KADD report.

## Common Fields

- Completeness
- Clarity
- Consistency
- Coherence
- Maturity

## Affected Files

- `.github/agents/kadd-layer-1-2-foundation-agent.agent.md`
- `.github/agents/kadd-layer-3-4-execution-agent.agent.md`
- `.github/agents/kadd-layer-5-9-knowledge-agent.agent.md`
- `.github/agents/kadd-layer-4-integrity-cohesion-agent.agent.md`
- `.github/agents/kadd-layer-5-final-report-agent.agent.md`
- `.github/agents/ORCHESTRATION-GUIDE.agent.md`

## Finding

Specialist reports used historically inconsistent custom tables, while the final report did not consistently expose the shared 8-dimension summary.

## Rationale

A common rubric enables meaningful comparison across dates and layers without removing layer-specific metrics.

## Suggested Change

Require an `Assessment Summary` table with 0–10 scores and evidence-based rationales. Specialist reports may add layer-specific dimensions.

## Decision

Status: Approved
