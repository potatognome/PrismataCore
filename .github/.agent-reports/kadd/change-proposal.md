# KADD Change Proposals

## Status Overview

This proposal set reflects the current state of the full KADD collection after the latest glossary revisions, the completion of the appendices and references KADs, and the addition of lessons-learned content. Several gaps are now resolved or partially resolved; the remaining open items are the ones that still affect long-term completeness and governance quality.

## Proposal 1

KAD:
1-definitions/1-05-foundational-narratives.yaml

Finding:
The foundational narratives KAD remains empty even though the rest of the definition layer is materially complete.

Recommendation:
Populate the narratives KAD with 3–5 scenario-driven examples that illustrate human-centered value and ecosystem context without creating implementation commitments.

Rationale:
Narratives are part of the intended KADD value model and help communicate why the project matters to people and institutions.

Benefits:
- Better human context
- Improved onboarding and understanding
- Stronger scenario-driven planning foundation

Risks:
- Continued emptiness weakens the conceptual and educational value of the definitions layer.

Suggested Change:
Add scenario entries covering governance, adoption, operational change, and ecosystem value.

Suggested Content:
- narrative-id
- actors
- scenario
- challenge
- outcome
- lesson

Impact Assessment:
Low effort, high value.

Status: Open

---

## Proposal 2

KAD:
5-01-research.yaml

Finding:
The research KAD remains empty and still does not preserve the project’s structured findings and unresolved questions.

Recommendation:
Create a minimal but useful research KAD with findings, open questions, evidence, and implications.

Rationale:
A durable knowledge framework should preserve research context as a first-class artifact.

Benefits:
- Better continuity of discovery
- Improved review of open questions
- More durable project memory

Risks:
- Research outcomes will remain implicit and less reusable.

Suggested Change:
Populate with sections for purpose, findings, unknowns, evidence, and decisions influenced by the research.

Suggested Content:
- objective
- research-themes
- findings
- open-questions
- evidence
- implications

Impact Assessment:
Low effort, high strategic value.

Status: Open

---

## Proposal 3

KAD:
5-02-lessons.learned.yaml

Finding:
The lessons-learned KAD is now populated and should continue to be maintained as the project evolves.

Recommendation:
Expand the lesson records over time and treat the file as a living knowledge artifact rather than a one-time document.

Rationale:
The current records provide a strong foundation and demonstrate the value of preserving project learning over time.

Benefits:
- Better historical continuity
- Reduced recurrence of mistakes
- Improved governance learning

Risks:
- Without maintenance, the record will become stale or incomplete.

Suggested Change:
Continue adding lessons as new governance, technical, or architectural patterns emerge.

Suggested Content:
- lesson-id
- context
- observation
- lesson
- evidence
- recommendations

Impact Assessment:
Resolved in principle; maintenance required.

Status: Open (maintenance)

---

## Proposal 4

KAD:
5-03-retrospectives.yaml

Finding:
The retrospective KAD remains empty.

Recommendation:
Add a retrospective structure aligned with architecture review, governance review, and project learning cycles.

Rationale:
Retrospectives close the loop on learning and provide formal closure for project change.

Benefits:
- Stronger reflection and accountability
- Better follow-through on improvement actions
- Improved project continuity

Risks:
- Without retrospectives, the project lacks a formal closure mechanism for learning and change.

Suggested Change:
Add sections for wins, failed assumptions, follow-up actions, and operational recommendations.

Suggested Content:
- retrospective-id
- timeframe
- positives
- negatives
- lessons
- follow-up-actions

Impact Assessment:
Moderate effort, high learning value.

Status: Open

---

## Proposal 5

KAD:
9-01-glossary.yaml

Finding:
The glossary has improved materially, but some entries remain incomplete, inconsistent, or malformed.

Recommendation:
Perform a final glossary normalization pass to correct typos, complete missing definitions, and eliminate placeholder values.

Rationale:
The glossary is now a strong reference layer, but it still needs quality cleanup before it is considered final canonical terminology.

Benefits:
- Better consistency across KADs
- Fewer interpretation ambiguities
- More reliable future indexing and validation

Risks:
- Incomplete glossary entries create ambiguity and weaken the value of the reference layer.

Suggested Change:
Correct terms such as “Canonial Metadata Framework,” replace “nul” placeholders, and complete incomplete definitions.

Suggested Content:
- entry-id
- term
- acronym
- definition
- owner
- validation-status

Impact Assessment:
Low-to-moderate effort, high quality benefit.

Status: Open

---

## Proposal 6

KAD:
3-planning/3-03-roadmap.yaml

Finding:
Roadmap dependency traceability still needs review against the current requirement and risk baseline.

Recommendation:
Audit dependency mappings and remove or replace references that are not clearly supported by the canonical planning set.

Rationale:
Stable planning depends on a clear and trustworthy requirement-to-roadmap chain.

Benefits:
- Better planning quality
- Stronger governance confidence
- Reduced drift risk

Risks:
- Misaligned dependencies can produce false confidence in roadmap execution.

Suggested Change:
Create a validation checklist for roadmap dependencies and ensure each item resolves to a supported requirement or risk record.

Suggested Content:
- dependency-check
- source-kad
- verified-status
- missing-reference
- reviewer

Impact Assessment:
Moderate effort, strong governance value.

Status: Open

---

## Proposal 7

KAD:
4-implementation/4-05-development.yaml

Finding:
The development KAD remains explicitly draft-level and architecture-review-pending.

Recommendation:
Finalize a review gate or designate the document as a provisional working policy until it receives architecture approval.

Rationale:
Draft-level policy should not be treated as final governance without explicit approval.

Benefits:
- Better clarity of maturity
- Reduced false confidence
- More structured review governance

Risks:
- Readers may misinterpret the document as approved policy when it is not.

Suggested Change:
Add explicit review status, owner, and next review date metadata.

Suggested Content:
- maturity
- review-status
- owner
- approved-by
- next-review-date

Impact Assessment:
Moderate effort, important governance benefit.

Status: Open

---

## Proposal 8

KAD:
4-implementation/4-02-data-model.yaml

Finding:
Some naming and ID conventions remain inconsistent with the broader KADD pattern.

Recommendation:
Normalize file IDs, metadata names, and pattern consistency across the implementation layer.

Rationale:
Consistency improves automation, cross-document traceability, and long-term maintenance quality.

Benefits:
- Better indexing
- More stable automation support
- Cleaner metadata hygiene

Risks:
- Ongoing inconsistencies weaken the quality of the knowledge model.

Suggested Change:
Standardize naming to the project’s dominant KAD pattern and update path metadata where required.

Suggested Content:
- id
- udi
- metadata.name
- source.path

Impact Assessment:
Low effort, moderate value.

Status: Open

---

## Proposal 9

KAD:
canonical/kadd/*

Finding:
Source paths and metadata remain somewhat inconsistent across the KADD files.

Recommendation:
Standardize source.path formatting and path conventions across the KAD collection.

Rationale:
A consistent provenance model improves trust, maintenance, and automation reliability.

Benefits:
- Cleaner traceability
- Better project hygiene
- Easier future automation

Risks:
- Inconsistent metadata reduces confidence in document provenance.

Suggested Change:
Adopt a single canonical repository-relative path convention for all KADs.

Suggested Content:
- source.path
- canonical-location
- repo-relative-path

Impact Assessment:
Low effort, strong governance improvement.

Status: Open

---

## Proposal 10

KAD:
9-02-appendices.yaml

Finding:
The appendixes file is now populated and provides strong support, but it should be continued as a maintained reference and onboarding asset.

Recommendation:
Treat appendices as an active project support layer and expand it as additional ecosystem context emerges.

Rationale:
The appendices document is valuable because it reduces onboarding friction and gives the project a durable interpretive layer.

Benefits:
- Better onboarding
- Better project communication
- More durable interpretive context

Risks:
- A static appendix will soon become stale if not reviewed and expanded.

Suggested Change:
Add new appendices for emerging concepts, workflows, or future ecosystem references as they appear.

Suggested Content:
- appendix-id
- title
- purpose
- content
- related-kad

Impact Assessment:
Low effort, high practical value.

Status: Open (maintenance)

---

## Proposal 11

KAD:
9-03-references.yaml

Finding:
The references KAD is now populated and useful, but it should continue to evolve as project lineage and external influence become clearer.

Recommendation:
Continue to curate and maintain the reference catalog as the project’s knowledge lineage expands.

Rationale:
This file is now a proper provenance and influences record, which is important for long-term understanding.

Benefits:
- Better provenance
- Better historical understanding
- Better support for future architecture decisions

Risks:
- If not maintained, the reference catalog will fall behind the project’s actual lineage.

Suggested Change:
Add future references as new standards, methods, or influences emerge.

Suggested Content:
- reference-id
- title
- type
- owner
- relevance

Impact Assessment:
Low effort, high continuity value.

Status: Open (maintenance)

---
