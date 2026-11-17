# PrismataCore

---

id: PRISMATACORE-README
udi: prismata.core.git.readme
version: 1.1.0
created: 2026-10-13
last updated: 2026-11-15

---

## Overview

PrismataCore is the canonical nucleus of the Prismata ecosystem.  
It defines the universal rules, schemas, identity model, and validation
framework that all other Prismata repositories depend on.

PrismataCore is **pure**, **deterministic**, and **tenant‑agnostic**.  
It contains no preview engine, no SDK tooling, and no tenant metadata.

---

## Core Responsibilities

### 1. Common Metadata Framework (CMF)
PrismataCore defines the CMF envelope used to store every metadata object
in the ecosystem. CMF provides a stable, future‑proof capsule, each containing
exactly 10 fields represented in the following order:

#### The 5 *Descriptor* Fields - udi, id, kind, version, tenant
Purpose: Find what you are looking for or identify what you have
- id
- udi
- kind
- version
- tenant

#### The 5 *Semantic* Fields
Purpose: Cover all Content, Scope, Governance, Status & Metadata
- source
- metadata
- relations
- notes
- content

All Prismata metadata must conform to CMF.

### 2. Prismata Schematic Object (PSO)
PrismataCore defines a *canonical object model (COM)*, called the **PSO** runtime model, the canonical in‑memory representation of CMF objects. PSO ensures deterministic loading, validation, and runtime behavior across all Prismata Compliant modules.

### 3. Universal Deterministic Identity / Universal Deterministic Identifier (UDI)
PrismataCore defines the UDI format and enforces identity rules across
the entire ecosystem. Every CMF and PSO object must include a valid UDI.

### 4. Canonical Schemas
PrismataCore provides the schema definitions required for rendering various Interface objects including:

- chromaschemes (imported from Chromaverse modules)
- colour schemes
- colour roles
- border patterns
- border roles
- panes
- ui framework
- menus
- menu items (with UDI‑compliant capability field)
- headers

These *interface objects* are rendered through tooling modules that are part of the **PrismataSDK** repository.

Core also includes meta‑schemas:

- manifest schema
- schema schema

### 5. Core Validators
PrismataCore includes the validator suite responsible for enforcing:

- CMF envelope correctness
- UDI correctness
- canonical schema correctness
- relations correctness
- PSO construction correctness

These validators ensure that all metadata objects are structurally and
semantically valid before being consumed by PrismataSDK or PrismataCorp.

---

## Architectural Role

PrismataCore is the **law layer** of the ecosystem:
PrismataCore → PrismataSDK → PrismataCorp

- Core defines the rules.
- SDK provides tools and rendering.
- Corp provides tenant content.

PrismataCore must never depend on SDK or tenant repositories.

---

## Contribution Rules

- All schemas must include a valid UDI.
- All metadata must conform to CMF.
- All runtime objects must conform to PSO.
- Core must remain deterministic and tenant‑agnostic.
- No preview logic or SDK tooling may be added to this repo.

---

## License

This repository defines the canonical Prismata metadata model and may be
used by any Prismata‑compatible tooling or tenant ecosystem.

---

## External References

- Metadata Frameworks -> https://www.ovaledge.com/blog/metadata-framework
- **Common Metadata Framework (CMF)** -> https://hewlettpackard.github.io/cmf/
- **Canonical Object Model (COM)** -> https://en.wikipedia.org/wiki/Canonical_model
- **Canonical Data Model (CDM)** -> https://www.bmc.com/resources/topics/canonical-data-model.html

---

## Change log

2026-10-13 - Version 1.0.0 - Initial commit of first draft
2026-11-15 - Version 1.1.0 - Add header with udi, last update and update section on Common metadata framework due to concerns over ambiguity of terminology.  Added External References.