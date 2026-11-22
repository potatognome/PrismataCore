# Cross-Repository Architectural Boundaries

## PrismataCore

Owns canonical definitions, KADD, schemas, laws, manifests, UDIs, validators,
and reference assets. It should contain minimal executable code limited to
validation and verification responsibilities.

## PrismataSDK

Owns runtime implementations, composition, rendering, tooling, security services,
interaction frameworks, and SDK applications. SDK code consumes Core definitions
and must not create competing canonical schemas or laws.

## PrismataCorp

Owns governance, tenant administration, workspaces, vaults, policy, archives,
stewardship, and preservation. Corp code must not replace canonical definitions
or implement runtime rendering.

## Workspace Resolution

When repositories are sibling checkouts, reference the relative PrismataCore
`canonical/kadd/` directory. When cloned separately, resolve Core/KADD through
a documented dependency or the environment-specific PrismataCore checkout.
Do not duplicate KAD files across repositories.
