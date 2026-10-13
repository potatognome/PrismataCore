# PrismataCore — Canonical Schema Generation Instructions

## Purpose
Agents must generate the canonical PrismataCore schema set and core validators.
All schemas MUST conform to the Canonical Metadata Format (CMF) and runtime
Prismata Schematic Object (PSO) model.

## Mandatory Requirements
1. Every schema MUST include a valid UDI field.
2. Every schema MUST be wrapped in CMF format.
3. Every schema MUST produce a valid PSO when loaded.
4. Core validators MUST validate:
   - CMF envelope correctness
   - UDI correctness
   - canonical rule correctness
   - relations correctness
5. Agents MUST NOT generate tenant-specific schemas.
6. Agents MUST NOT generate preview or SDK tooling.

## Schema Generation Rules
Agents MUST generate the following canonical schemas required for rendering:

### 1. Chromaschemes
- Assume content imported from Chromaverse modules.
- Define canonical structure for chroma palettes, chroma roles, chroma metadata.
- UDI: prismata.core.schema.chromascheme

### 2. Colour Schemes
- Canonical colour palette structure.
- Base colours, semantic colours, gradients.
- UDI: prismata.core.schema.colour-scheme

### 3. Colour Roles
- Mapping of semantic roles → colours.
- UDI: prismata.core.schema.colour-role

### 4. Borders
- Border patterns (solid, dashed, inset, outset)
- Border roles (semantic border usage)
- UDI: prismata.core.schema.border-pattern
- UDI: prismata.core.schema.border-role

### 5. Panes
- Canonical pane object schema.
- Includes layout, padding, border, colour roles.
- UDI: prismata.core.schema.pane

### 6. UI Framework
- Canonical UI grammar and component definitions.
- UDI: prismata.core.schema.ui-framework

### 7. Menus
- Canonical menu schema.
- Includes header, menu-items, ordering, layout.
- UDI: prismata.core.schema.menu

### 8. Menu Items
- Canonical menu-item schema.
- MUST include:
  - UDI
  - capability (UDI-compliant)
  - type
  - order
  - selection method
  - action
- UDI: prismata.core.schema.menu-item

### 9. Headers
- Canonical header schema for menus and panes.
- UDI: prismata.core.schema.header

### 10. Core Schemas
- Manifest schema (for CMF manifests)
- Schema schema (meta-schema describing schemas)
- UDI:
  - prismata.core.schema.manifest
  - prismata.core.schema.schema

## Content Rules
Agents MUST use content based on existing Prismata object schemas.
Agents MUST NOT invent unrelated structures.
Agents MUST preserve deterministic naming, typing, and field structure.

## Output Format
All generated schemas MUST be valid CMF objects:

id: prismata.core.schema.<name>
udi: prismata.core.schema.<name>
kind: schema
version: 1.0.0
tenant: null
source: { ... }
metadata: { ... }
content: { ... }   # schema fields go here
relations: { ... }
validation: { ... }
notes: []

## Core Validators
Agents MUST generate:

- cmf_envelope_validator
- udi_validator
- canonical_schema_validator
- relations_validator
- pso_constructor_validator

Validators MUST operate ONLY on CMF and PSO envelopes.

## Forbidden
- No tenant schemas
- No SDK tooling
- No preview engine
- No UI rendering logic
