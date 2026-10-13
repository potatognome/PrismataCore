# PrismataCore

PrismataCore is the canonical nucleus of the Prismata ecosystem.  
It defines the universal rules, schemas, identity model, and validation
framework that all other Prismata repositories depend on.

PrismataCore is **pure**, **deterministic**, and **tenant‑agnostic**.  
It contains no preview engine, no SDK tooling, and no tenant metadata.

---

## Core Responsibilities

### 1. Canonical Metadata Format (CMF)
PrismataCore defines the CMF envelope used to store every metadata object
in the ecosystem. CMF provides a stable, future‑proof capsule containing:

- identity (id, udi)
- versioning
- metadata
- content
- relations
- validation
- provenance

All Prismata metadata must conform to CMF.

### 2. Prismata Schematic Object (PSO)
PrismataCore defines the PSO runtime model, the canonical in‑memory
representation of CMF objects. PSO ensures deterministic loading,
validation, and runtime behavior across all repos.

### 3. Universal Deterministic Identity (UDI)
PrismataCore defines the UDI format and enforces identity rules across
the entire ecosystem. Every CMF and PSO object must include a valid UDI.

### 4. Canonical Schemas
PrismataCore provides the schema definitions required for rendering:

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
