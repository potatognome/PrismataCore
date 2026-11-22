# PrismataCore Copilot Instruction Index

## Load Order

1. `../copilot-instructions.md`
2. `kadd-reference.md`
3. `compliance/udi-compliance-policy.md`
4. `compliance/cmf & pso envelope instructions.yaml`
5. `design/schema-driven-design-rules.yaml`
6. `cross-repository-boundaries.md`
7. `kadd-workflow.md`

## Instruction Modules

- `kadd-reference.md` - Normative architectural reference and repository placement.
- `cross-repository-boundaries.md` - Core, SDK, and Corp ownership rules.
- `compliance/udi-compliance-policy.md` - Artifact identity rules.
- `compliance/cmf & pso envelope instructions.yaml` - Canonical envelope rules.
- `design/schema-driven-design-rules.yaml` - Schema design constraints.
- `kadd-workflow.md` - Proposal, review, actioning, and archival lifecycle.

## Precedence

- Canonical KADD files in `canonical/kadd/` are architectural authority.
- Core repository Copilot instructions enforce repository execution policy.
- Supplementary modules constrain or specialize that policy.
- Operational reports under `.github/.agent-reports/kadd/` are records, not
  replacements for canonical KAD definitions.
