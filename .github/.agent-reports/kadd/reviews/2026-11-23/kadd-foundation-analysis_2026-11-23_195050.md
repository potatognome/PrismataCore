# KADD Foundation Analysis: Layers 1-2

**Status:** READ-ONLY, PROPOSAL-BASED  
**Primary repository:** PrismataCore  
**Analysis timestamp:** 2026-11-23 19:50:50 -05:00  
**Filename:** `kadd-foundation-analysis_2026-11-23_195050.md`

## Executive Summary

The PrismataCore Layers 1-2 foundation is mature, internally coherent, and deliberately separated across Core, SDK, and Corp concerns. The vision, concept model, doctrines, systems, subsystems, decisions, and relationship definitions form a complete and traceable architectural foundation. The collection shows strong CMF discipline: all ten reviewed definition and architecture KADs are active, versioned, complete in the required envelope, and connected through imports.

Three findings reduce the foundation score:

1. The relationship KAD's YAML structure does not consistently represent its intended top-level relationship groups. `registry-relationships`, `ecosystem-relationships`, and `tenant-relationships` are nested more deeply under `capability-relationships`, while `Schema-to-PSO` and `Schema-to-ExampleObject` are nested under `Schema-to-Artifact` rather than at the `schema-relationships` level.
2. `CapabilityUDI` is classified as an SDK subsystem foundation asset, while the concept model and ecosystem requirements assign it to capability identity and it is also a Core architectural identity concern. This creates an ownership ambiguity without an explicitly documented SDK implementation/Core definition split.
3. The workspace did not contain `Prism/canonical/kadd` or another separate `"former combined Prismata"` canonical collection. Only `PrismataCore/canonical/kadd` was accessible. Consequently, no separate minor-update delta can be established for this review.

**Foundation health:** 8.3/10  
**Layer 1 overall:** 8.9/10  
**Layer 2 overall:** 8.3/10

## Assessment Summary

Shared dimensions use the requested 0-10 scale.

| Dimension | Score | Evidence-based rationale |
|---|---:|---|
| Completeness | 8.1/10 | All required Layer 1 and Layer 2 documents are present and substantial. A relationship ownership correction and explicit SDK implementation/Core definition split are the most material remaining gaps. |
| Clarity | 8.7/10 | Purposes, exclusions, ownership boundaries, and conflict-resolution fields are explicit. The relationship YAML indentation and `CapabilityUDI` ownership reduce precision in one subsystem area. |
| Consistency | 7.9/10 | Terminology and review metadata are consistent across the files. The relationship hierarchy and subsystem placement of `CapabilityUDI` are the notable inconsistencies. |
| Coherence | 8.9/10 | Vision, concepts, principles, doctrines, systems, subsystems, decisions, and planning evidence align into a stable knowledge-first architecture. |
| Maturity | 8.8/10 | The documents are active, versioned, dated, cross-linked, validated, and governed by quarterly or more frequent review rules. |

### Specialist dimensions

| Specialist dimension | Score | Evidence-based rationale |
|---|---:|---|
| Vision Clarity | 9.2/10 | Purpose, mission, pillars, goals, success criteria, outcomes, and non-goals are explicit and mutually aligned. |
| Concept Maturity | 8.7/10 | The concept groups cover identity, structure, capability, governance, knowledge, interaction, and ecosystem concerns; foundational relationships are stated. |
| Architectural Coherence | 8.8/10 | ADR-006 and the Systems, Subsystems, and Relationships documents consistently describe three mandatory layers and non-overlapping concerns. |
| Relationship Completeness | 6.8/10 | Core relationship categories exist, but the YAML hierarchy misplaces several top-level relationship groups and omits an explicit SDK-to-Corp relationship. |
| Definition Quality | 8.8/10 | Definitions use clear purposes and boundaries, with glossary authority and authoritative imports. |

### Foundation composite

The foundation composite is 8.3/10 (83/100) using the mean of the five shared dimensions and specialist Foundation Health value:

- Shared dimensions mean: **8.48/10**
- Specialist foundation health: **8.3/10**
- Composite evidence: approximately **83/100**

## Repository and Authority Classification

| Repository | Applicable ownership |
|---|---|
| PrismataCore | Canonical visions, concepts, doctrines, definitions, systems, subsystems, relationships, architectural decisions, schemas, laws, and validation standards |
| PrismataSDK | Runtime implementation of PSO, security, rendering, tooling, capability registries, composition, and authoring environments |
| PrismataCorp | Tenant workspaces/vaults, governance, policies, archive stewardship, preservation, and historical storage |

No finding in this review is assigned to a repository solely because a subsystem name appears outside PrismataCore. Ownership follows the normative Core KAD boundaries:

- Core owns definitions and standards.
- SDK owns runtime implementations and tooling.
- Corp owns tenant governance and preservation.

## Layer 1: Definitions Analysis

### File-by-file maturity

| Document | Version | Maturity | Assessment |
|---|---:|---:|---|
| `1-00-documentation-discipline.yaml` | 1.0.9 | 9.2/10 | Strong layer and CMF governance model. The required-document register is complete. It remains somewhat process-oriented, but that is its intended role. |
| `1-01-vision.yaml` | 1.0.7 | 9.3/10 | Exceptionally clear purpose, mission, pillars, goals, success criteria, and non-goals. |
| `1-02-project-profile.yaml` | 1.0.7 | 8.9/10 | Strong ecosystem role, responsibilities, boundary, and required-service classification. Some former ecosystem names remain illustrative rather than mandatory. |
| `1-03-concepts.yaml` | 1.0.7 | 8.8/10 | Broad, durable conceptual model with clear foundational relationships and domain groups. |
| `1-04-principles.yaml` | 1.0.7 | 8.7/10 | Clear distinction between principles, laws, and governance. Decision logic is explicit. |
| `1-05-foundational-narratives.yaml` | 1.0.7 | 8.6/10 | Human-centered operational and historical scenarios align with preservation, abstraction, and architecture themes. It is explicitly non-authoritative. |
| `1-06-doctrines.yaml` | 1.0.2 | 8.7/10 | Mature beliefs and relationships; deliberately challengeable and subordinate to evidence. |

### Vision clarity

The vision is highly precise and strategically bounded. It defines why Prismata exists, its desired end state, foundational pillars, ultimate beneficiary, and non-goals. The scope remains broad enough for a multi-repository ecosystem while excluding implementation and project ownership details. Cross-repository scope is acknowledged in `relations.scope`, and repository-specific responsibility is separated later in the architecture.

### Concept analysis

The concept inventory is complete for the current foundation. Identity, structure, capability, governance, knowledge, interaction, and ecosystem concepts are distinct and supported by a compact conceptual model. `UDI`, `CMF`, `PSO`, `Schema`, `Law`, `Capability`, `Manifest`, `Registry`, `Knowledge Index`, and `VaultGuard` are mature concepts.

Potential concept-vocabulary issue:

- `Capability UDI` is named in concepts and requirements.
- It appears in the SDK subsystem decomposition as `CapabilityUDI`.
- The canonical glossary only defines the informal aliases `cUDI` and `mUDI`, not `Capability UDI` or `Manifest UDI` as stable canonical terms.

This is more a terminology/relationship issue than a missing concept.

### Narrative coherence

The narratives consistently illustrate knowledge loss, architectural drift, repeated implementation, governance, abstraction, and long-term preservation. The document clearly distinguishes illustrative narratives from requirements or approved work. `NARRATIVE-003` and `NARRATIVE-004` provide strong operational and historical context for the vision and doctrines.

### Definition completeness

The six definition documents required for Layer 1 are present and internally cross-linked. Coverage is strong across purpose, profile, concepts, principles, narratives, and doctrines. The main improvement is explicit repository ownership for Core, SDK, and Corp terms, which is now established in the architecture but could be reiterated in the project profile or glossary for discoverability.

## Layer 2: Architecture Analysis

### File-by-file maturity

| Document | Version | Maturity | Assessment |
|---|---:|---:|---|
| `2-01-systems.yaml` | 1.0.7 | 9.2/10 | Clear three-layer architecture, responsibilities, exclusions, and mandatory boundaries. |
| `2-02-subsystems.yaml` | 1.0.7 | 8.3/10 | Detailed decomposition and classification model. `CapabilityUDI` placement is the primary ownership ambiguity. |
| `2-03-relationships.yaml` | 1.0.7 | 6.8/10 | Strong relationship principles and cardinality model, but structural indentation and hierarchy require correction. |
| `2-04-decisions.yaml` | 1.0.7 | 9.1/10 | Fourteen traceable decisions with explicit questions, positions, and rationales. |

### System architecture

The three mandatory systems are clearly responsible for:

- **PrismataCore:** definitions, standards, schemas, laws, manifests, identity, validation definitions, and tests.
- **PrismataSDK:** runtime execution, security implementations, rendering, tooling, composition, and authoring environments.
- **PrismataCorp:** governance, stewardship, tenant isolation, archives, and preservation.

The boundaries are explicit and complementary. There is no evidence of Core taking on runtime rendering or Corp taking on schema ownership.

### Subsystem organization

The subsystem classification model distinguishes foundation assets, validators, registries, runtime components, tooling components, and governance components. The decomposition is coherent, with one ownership exception:

- `CapabilityUDI` is a foundation asset for capability identity.
- It is placed under the PrismataSDK subsystem block.
- Core concept and requirement KADs establish Capability UDI as a foundational ecosystem identity model.

The correct model is likely a Core-defined identity/registry contract with SDK implementation and runtime consumption, but this split must be made explicit rather than inferred.

### Relationship integrity

The relationship principles and cardinality notation are clear. However, evidence at `2-03-relationships.yaml` lines 118-210 shows structural issues:

- `Schema-to-PSO` and `Schema-to-ExampleObject` are YAML children of `Schema-to-Artifact`, so they do not register as peer entries in `schema-relationships`.
- `registry-relationships`, `ecosystem-relationships`, and `tenant-relationships` are indented six to eight spaces under `capability-relationships`, making them capability children in YAML rather than peer top-level relationship groups.
- No explicit SDK-to-Corp relationship is stated, although the boundaries imply SDK services operate with Corp workspaces, vaults, and tenant isolation.
- Tenant-to-Archive is stated, while Archive-to-Vault/Provenance relationships are not.

No circular dependency or orphaned relationship was identified in the intended semantic model.

### Decision quality

Architectural decisions are specific and traceable. Every reviewed ADR contains an identifier, UDI, question, position, and rationale. The decisions cover identity, CMF, PSO, metadata, composition, layer separation, minimal executable core, validation, tenant isolation, interface rendering, knowledge preservation, structure/behavior separation, security, and registries.

Potential governance improvement: the relationship of each ADR to the requirement and risk sets is mostly established through downstream KAD imports and roadmap dependency lists, but there is no explicit ADR-to-requirement cross-reference table inside `2-04-decisions.yaml`. This may be better handled by planning-layer traceability rather than changing the decision document.

## Cross-Layer Coherence

### Vision to systems

The systems implement the vision's foundational pillars:

- UDI and CMF/PSO correspond to identity and structure.
- Core validation and SDK registries implement validation and discoverability.
- Corp preservation and archives implement memory and historical knowledge.
- The three-layer split minimizes coupling and preserves accessibility.

### Concepts to systems

Concept-to-system mapping is coherent:

- Identity and schemas: PrismataCore.
- Runtime, rendering, security, tooling: PrismataSDK.
- Governance, tenant isolation, archives: PrismataCorp.

The one ambiguity is `CapabilityUDI` placement, as discussed above.

### Architecture decision traceability

The vision and project profile establish intent, concepts establish meaning, systems and subsystems establish ownership, relationships establish dependencies and cardinalities, and ADRs establish architectural positions. The planning and implementation layers inherit these decisions. Roadmap dependencies reference ADR UDIs and requirement UDIs, demonstrating traceability beyond Layers 1-2.

## Findings

### Strengths

1. Strong explicit separation of Core, SDK, and Corp concerns.
2. Complete and active Layer 1 definition set.
3. Complete and active Layer 2 architecture set.
4. Clear conflict-resolution and ownership rules in each KAD.
5. ADR records include question, position, rationale, and stable UDI.
6. Foundation concepts are durable and implementation-independent.
7. Narratives, principles, and doctrines are consistently aligned around knowledge preservation and falsifiability.

### Gaps

1. The relationship KAD's YAML hierarchy incorrectly nests several relationship groups.
2. `CapabilityUDI` ownership is ambiguous between Core definition and SDK implementation.
3. `PCMS-2026`, `VILE`, and `VISE` need stable canonical glossary terms or explicit alias classifications.
4. SDK-to-Corp and Archive-to-Vault/Provenance relationships are not explicitly modeled.

### Inconsistencies

1. `2-02-subsystems.yaml` places a Core identity concept under the SDK subsystem block.
2. `2-03-relationships.yaml` uses incorrect indentation for nested relationship records.
3. `Glossary` defines `cUDI` and `mUDI` as informal aliases while concepts and requirements use full `Capability UDI`/`Manifest UDI` names.

### Risks

1. Automated relationship or graph tooling could traverse the wrong YAML hierarchy and omit registries, tenant relationships, or ecosystem relationships.
2. SDK/Core ownership ambiguity could lead to duplicated Capability UDI implementations or competing definitions.
3. Undefined or informally aliased subsystem terms may reduce cross-repository discoverability.

### Opportunities

1. Add machine-validation checks for relationship top-level keys and peer hierarchy.
2. Add an explicit Core definition/SDK implementation contract for capability identity and registries.
3. Publish a cross-repository ownership matrix derived from the Systems and Subsystems KADs.

## Recommendations

### Priority actions

1. Submit `CR-2026-11-23-01` to correct the YAML hierarchy in `2-03-relationships.yaml` and add missing top-level/peer relationships.
2. Submit `CR-2026-11-23-02` to clarify Core-owned Capability UDI definitions and SDK-owned implementations/registries.
3. Add canonical glossary entries or explicit aliases for `PCMS-2026`, `VILE`, `VISE`, `Capability UDI`, and `Manifest UDI`.
4. Establish a formal availability check for sibling canonical collections so future reviews can compare updates and report deltas.

### Proposal status

The proposals in `PrismataCore/.github/.agent-reports/kadd/proposals/inbox/` are draft-only. No canonical KAD, implementation, or action change request has been applied.

## Minor-Update Availability

The requested separate collection path `Prism/canonical/kadd` was not present in the workspace. A workspace-wide search for `**/canonical/kadd/**/*.yaml` found only `PrismataCore/canonical/kadd`. Therefore:

- The Core collection is the authoritative source for this review.
- No former combined-Prismata KAD is treated as authority.
- No delta or comparison against a current minor update can be certified.
- Findings involving SDK or Corp are classified by ownership as described above.

## Metadata

- **Methodology:** Reviewed repository boundaries, orchestration guide, documentation discipline, all 25 canonical KAD files for context, and the ten Layer 1-2 KAD files in full.
- **Document versions reviewed:** 1-00 1.0.9; 1-01 through 1-05 1.0.7; 1-06 1.0.2; 2-01 through 2-04 1.0.7.
- **Missing source path:** `Prism/canonical/kadd` (or any separate former combined-Prismata collection).
- **Canonical files modified:** None.
- **Implementation files modified:** None.
- **Report type:** Read-only analysis.
- **Next steps:** Principal review of proposals, Core relationship/KAD updates through approval, SDK/Corp implementation planning only after canonical proposals are approved.
