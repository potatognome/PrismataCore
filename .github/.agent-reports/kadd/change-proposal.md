# KADD Change Proposals

## Proposal 1

KAD:
5-01-research.yaml

Finding:
The post-implementation research document is empty, leaving a major gap in the project’s ability to preserve lessons, findings, and research continuity.

Recommendation:
Add a structured research KAD that records relevant findings, unknowns, and discovery outcomes across the Prismata ecosystem.

Rationale:
The broader KADD system explicitly frames knowledge preservation as a core objective. An empty research KAD weakens continuity and reduces future reuse of project understanding.

Benefits:
- Preserves research context
- Improves operational memory
- Supports future planning decisions

Risks:
- If left empty, knowledge will remain unrecorded and hard to recover later.

Suggested Change:
Populate the file with structured sections for research objectives, findings, open questions, evidence, and implications.

Suggested Content:
- purpose
- research-themes
- findings
- open-questions
- decision-impact
- related-artifacts

Impact Assessment:
Low effort, high strategic value, and significant long-term knowledge benefit.

---

## Proposal 2

KAD:
5-02-lessons.learned.yaml

Finding:
The lessons learned file is empty despite the discipline emphasizing preserved experience and historical knowledge.

Recommendation:
Create the document with structured lessons, root causes, and corrective actions derived from current project experience.

Rationale:
Lessons learned are a key mechanism for preserving knowledge beyond implementation specifics.

Benefits:
- Improves reuse of project insights
- Reduces repeated mistakes
- Strengthens governance continuity

Risks:
- Repeated defects and weak knowledge retention if not captured.

Suggested Change:
Add sections for repeating patterns, lessons, owner, context, and recommended follow-up.

Suggested Content:
- lesson-id
- context
- issue
- lesson
- action
- owner
- status

Impact Assessment:
Low effort, high value, and direct improvement to project maturity.

---

## Proposal 3

KAD:
5-03-retrospectives.yaml

Finding:
The retrospective document is empty, leaving no formal record of project reflection or governance closure.

Recommendation:
Define a retrospective structure aligned to the project’s architecture and planning cycles.

Rationale:
Retrospectives are necessary for continuous knowledge preservation and disciplined architectural improvement.

Benefits:
- Encourages reflection and improvement
- Creates governance continuity
- Documents what should be kept, changed, or retired

Risks:
- Lack of explicit retrospective structure weakens future learning and accountability.

Suggested Change:
Add sections for what went well, what changed, what failed, and what should be improved next.

Suggested Content:
- retrospective-id
- timeframe
- scope
- positives
- failures
- learnings
- follow-up-actions

Impact Assessment:
Moderate effort but high strategic value for organizational learning.

---

## Proposal 4

KAD:
9-02-appendixes.yaml

Finding:
The appendices file is empty despite the reference layer being a part of the KADD structure.

Recommendation:
Populate appendices with support material, glossary mapping, canonical examples, and project-specific reference patterns.

Rationale:
Appendices provide stable context for ecosystem participants and reduce ambiguity in interpretation.

Benefits:
- Better project traceability
- Improved onboarding
- Better support for future agents and maintainers

Risks:
- Missing operational references makes interpretation harder.

Suggested Change:
Create a baseline appendices KAD with system context, examples, and supporting material.

Suggested Content:
- appendix-id
- purpose
- content
- related-kads
- usage-guidance

Impact Assessment:
Low effort but useful for knowledge durability and usability.

---

## Proposal 5

KAD:
9-03-references.yaml

Finding:
The reference file is empty, leaving the resource layer without an authoritative support list.

Recommendation:
Add a curated reference list for canonical standards, documents, and external dependencies.

Rationale:
Reference integrity is critical to long-term maintainability and ecosystem traceability.

Benefits:
- Better discovery of supporting material
- Stronger cross-document trust
- Better project continuity and onboarding

Risks:
- Future contributors may not know which references are authoritative.

Suggested Change:
Build a reference catalog with titles, types, owners, and relevance to the Prismata ecosystem.

Suggested Content:
- reference-id
- title
- type
- owner
- url-or-location
- relevance

Impact Assessment:
Low-to-moderate effort and important for governance hygiene.

---

## Proposal 6

KAD:
3-planning/3-03-roadmap.yaml

Finding:
Several roadmap items cite requirements or risks that are not present in the current requirement baseline, creating traceability drift.

Recommendation:
Audit the roadmap dependencies and remove or replace undefined references with a validated requirement set.

Rationale:
Roadmap items should map to explicit and authoritative planning artifacts to remain trustworthy and reviewable.

Benefits:
- Better traceability
- More reliable project planning
- Easier validation and risk management

Risks:
- Unchecked dependency drift may cause misaligned planning and false execution assumptions.

Suggested Change:
Add a dependency validation checklist and only permit requirements/risks referenced by actual KADs.

Suggested Content:
- validated-dependencies
- missing-references
- review-status
- mapping-source

Impact Assessment:
Moderate effort with a strong return in governance quality.

---

## Proposal 7

KAD:
4-implementation/4-05-development.yaml

Finding:
The development KAD explicitly states that it is a draft and requires architecture review, suggesting incomplete implementation governance.

Recommendation:
Either complete the architecture review and stabilize the document or clearly label it as a pilot framework until the review is finished.

Rationale:
A draft document with explicit review requirements should not be treated as final implementation policy without an explicit approval gate.

Benefits:
- Reduces false confidence
- Preserves review discipline
- Improves architectural accountability

Risks:
- Teams may infer policy from an unapproved draft and create inconsistent implementations.

Suggested Change:
Add a formal approval gate, maturity tag, and canonical ownership marker.

Suggested Content:
- maturity
- architecture-review-status
- owner
- approved-by
- next-review-date

Impact Assessment:
Moderate effort, high governance value.

---

## Proposal 8

KAD:
4-implementation/4-02-data-model.yaml

Finding:
The data model file uses some inconsistent ID and naming patterns compared to the other KAD files.

Recommendation:
Normalize the KAD IDs and naming conventions to match the rest of the KADD pattern and official layer naming.

Rationale:
Consistent naming supports indexing, automation, and cross-document validation.

Benefits:
- Better machine readability
- More stable registry behavior
- Better future validation tooling

Risks:
- Inconsistent IDs create ambiguity for automation and indexing tasks.

Suggested Change:
Standardize file IDs and metadata names to the KAD-PRISMATA-4-02-DATA-MODEL pattern used elsewhere when appropriate.

Suggested Content:
- id
- udi
- metadata.name
- source.path
- canonical filename

Impact Assessment:
Low effort with moderate value for consistency and tooling reliability.

---

## Proposal 9

KAD:
canonical/kadd/*

Finding:
Some source path entries are inconsistent, mixing relative paths with leading slash paths.

Recommendation:
Standardize all source.path values to a single repository-relative convention.

Rationale:
Path consistency is a small but important element of provenance, maintainability, and automation trust.

Benefits:
- Cleaner traceability
- Easier automation
- Better repository hygiene

Risks:
- Mixed path conventions create confusion for tooling and review.

Suggested Change:
Use a single canonical pattern such as canonical/kadd/<layer>/<file>.yaml.

Suggested Content:
- source.path
- canonical repository location
- repository-relative path

Impact Assessment:
Low effort and direct improvement to provenance quality.

---

## Proposal 10

KAD:
1-definitions/1-05-foundational-narratives.yaml

Finding:
The foundational narratives document exists but is empty, limiting the storytelling layer that should communicate ecosystem value and problem context.

Recommendation:
Populate the narratives file with a minimum viable set of human-centered scenario narratives tied to the Prismata vision.

Rationale:
Narratives provide context for human understanding and future requirements work, and they are explicitly intended to support exploration without committing to implementation.

Benefits:
- Improves understanding of value and context
- Supports future planning and opportunity exploration
- Better communicates non-technical outcomes

Risks:
- Empty narrative content reduces the project’s ability to demonstrate value and operational context.

Suggested Change:
Add 3-5 narrative scenarios covering operations, governance, and ecosystem adoption.

Suggested Content:
- narrative-id
- scenario
- actors
- challenge
- outcome
- learning

Impact Assessment:
Low effort and highly beneficial for communication and future design alignment.

---
