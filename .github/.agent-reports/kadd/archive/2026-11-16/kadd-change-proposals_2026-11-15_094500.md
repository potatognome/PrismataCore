# KADD Change Proposal Set

Date: 2026-11-15 09:45:00 -05:00
Scope: Recommended proposal-based changes for every KADD layer

## Overview

This proposal set contains the recommended change requests generated from the latest review of the canonical KADD collection. All proposals remain proposal-based and do not modify the authoritative source KADs directly. The review process now includes an operational proposal/review/archive workflow to keep change records current, reviewable, and easily archival-safe.

## Layer Summary

| Layer | Primary Proposal | Status |
| --- | --- | --- |
| 1 — Definitions | Populate foundational narratives and improve narrative coverage | Proposed |
| 2 — Architecture | Normalize terminology and strengthen traceability to implementation | Proposed |
| 3 — Planning | Add explicit dependency links and execution traceability | Proposed |
| 4 — Implementation | Establish formal review gates for development maturity and naming consistency | Proposed |
| 5 — Post-Implementation | Populate research and retrospectives and assign governance ownership | Proposed |
| 9 — Reference | Complete glossary cleanup and eliminate placeholder values | Proposed |

---

## Proposal 1: Definitions Layer

- File: `kadd-proposal-layer-1-definitions_2026-11-15_094500.md`
- Affected KAD: `1-definitions/1-05-foundational-narratives.yaml`
- Finding: The foundational narratives KAD is incomplete despite the rest of Layer 1 being materially mature.
- Recommended change: Add scenario-based narratives that communicate human value, operational context, and ecosystem outcomes without prescribing implementation.
- Status: Proposed

## Proposal 2: Architecture Layer

- File: `kadd-proposal-layer-2-architecture_2026-11-15_094500.md`
- Affected KADs: `2-architecture/2-01-systems.yaml`, `2-02-subsystems.yaml`, `2-03-relationships.yaml`, `2-04-decisions.yaml`
- Finding: Architecture is strong, but terminology and traceability consistency should be tightened.
- Recommended change: Normalize terminology against the glossary and add explicit links from architectural decisions to implementation and planning concerns.
- Status: Proposed

## Proposal 3: Planning Layer

- File: `kadd-proposal-layer-3-planning_2026-11-15_094500.md`
- Affected KADs: `3-planning/3-01-requirements.yaml`, `3-02-risks.yaml`, `3-03-roadmap.yaml`
- Finding: Requirement-to-risk-to-roadmap mapping is not explicit enough to support high-confidence governance.
- Recommended change: Add explicit dependency and ownership metadata and validate that each roadmap item is directly traceable to a requirement or architectural decision.
- Status: Proposed

## Proposal 4: Implementation Layer

- File: `kadd-proposal-layer-4-implementation_2026-11-15_094500.md`
- Affected KADs: `4-implementation/4-01-interfaces.yaml`, `4-02-data-model.yaml`, `4-03-storage.yaml`, `4-04-configuration.yaml`, `4-05-development.yaml`
- Finding: Implementation documentation is credible, but 4-05-development remains provisional and naming governance is inconsistent.
- Recommended change: Establish a formal review gate for draft-vs-canonical maturity and align naming across implementation artifacts.
- Status: Proposed

## Proposal 5: Post-Implementation Layer

- File: `kadd-proposal-layer-5-post-implementation_2026-11-15_094500.md`
- Affected KADs: `5-post-implementation/5-01-research.yaml`, `5-post-implementation/5-02-lessons-learned.yaml`, `5-post-implementation/5-03-retrospectives.yaml`
- Finding: The layer is partially populated but still lacks completion in the research and retrospective tracks.
- Recommended change: Populate the research and retrospectives records, assign ownership, and add a recurring review cadence.
- Status: Proposed

## Proposal 6: Reference Layer

- File: `kadd-proposal-layer-9-reference_2026-11-15_094500.md`
- Affected KADs: `9-reference/9-01-glossary.yaml`, `9-reference/9-02-appendices.yaml`, `9-reference/9-03-references.yaml`
- Finding: The reference layer is useful but still includes incomplete or malformed glossary content and requires a final terminology cleanup.
- Recommended change: Normalize terminology, replace placeholder values, and complete glossary quality review before treating the layer as fully canonical.
- Status: Proposed

---

## Decision Guidance

These recommendations are intentionally framed as proposals rather than direct changes to the source KADs. They are intended to support principal review, approval, and implementation in the formal KADD governance process.
