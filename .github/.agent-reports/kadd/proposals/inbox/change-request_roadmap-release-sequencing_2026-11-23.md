# KADD Change Request: Roadmap Release Sequencing

**Status:** Draft  
**Date Submitted:** 2026-11-23  
**Submitted By:** KADD Execution Analysis Agent  
**Priority:** High  
**Impacted repository:** PrismataCore  
**Ownership layer:** Core planning; cross-repository delivery mapping

## Change Summary

Add execution-ready sequencing metadata to `3-03-roadmap.yaml`, including phases, release gates, repository ownership, owners, target conditions, and requirement coverage.

## Affected KAD Document

- **Filename:** `3-03-roadmap.yaml`
- **Layer:** 3 (Planning)
- **Current Version:** 1.0.6
- **Proposed Version:** Subject to Principal approval

## Finding

All 20 roadmap items are `planned`. There are no phases, dates, milestones, exit gates, accountable owners, repository work-package assignments, or requirement-coverage matrix. Existing dependencies are directional and evidence-rich, but do not establish release readiness or implementation responsibility.

## Rationale

The roadmap currently defines a stable directional dependency graph but not an executable sequence. Without release gates and ownership, Core, SDK, and Corp work may overlap, begin out of dependency order, or use different completion criteria.

## Suggested Change

Add planning fields to roadmap items after Principal/architecture-team review, for example:

```yaml
phase: foundation
release-target: null
owner: prismata-architecture-team
repository: PrismataCore
entry-criteria:
  - approved KAD proposal
  - canonical dependencies available
exit-criteria:
  - evidence artifact exists
  - success metric is verified
  - proposal status is approved
coverage:
  requirements:
    - prismata.kadd.requirements...
```

Also add a roadmap coverage matrix or generated validation that identifies:

- requirements with no roadmap item;
- roadmap items with no requirement;
- circular roadmap dependencies;
- missing repository assignments; and
- missing exit criteria.

## Impact Assessment

- **Affected areas:** Layers 2-5, implementation planning, and cross-repository release governance.
- **PrismataCore:** canonical sequence and standards.
- **PrismataSDK:** runtime and tooling work packages.
- **PrismataCorp:** tenant, workspace, vault, and archive work packages.
- **Risk:** overcommitting uncertain work if dates are treated as binding.
- **Mitigation:** keep roadmap directional and mark milestones as target gates until approved.

## Alternatives Considered

1. Leave the roadmap as a dependency-only backlog.
   - Rejected because it does not support release sequencing or accountability.
2. Move delivery planning entirely out of KADD.
   - Rejected because architecture and requirement dependencies would lose canonical governance.

## Decision & Approval

- [ ] Approved
- [ ] Approved with modifications
- [ ] Deferred
- [ ] Rejected

**Principal:** Pending
