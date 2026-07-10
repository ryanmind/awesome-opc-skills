# Design Convergence Review

Review a single design document or a multi-document design folder for implementation readiness without redesigning the architecture.

## Features

- Reviews closure, completeness, redundancy, scope drift, and consistency
- Supports pasted content, single files, multiple files, and design folders
- Maps entry documents, references, authority, and single sources of truth
- Separates blocking issues, warnings, and missing evidence
- Uses a deterministic implementation-readiness score
- Treats code and tests as optional evidence, not general code-review targets
- Recommends only the minimum action needed to converge

## Usage

```text
Use $design-convergence-review to review docs/design/ and determine whether it is ready for implementation.
```

```text
Use $design-convergence-review to review architecture.md against requirements.md and the current interface definitions.
```

```text
Use $design-convergence-review to check these ADRs for conflicting authority, duplicated decisions, and missing verification paths.
```

## Review Outcomes

- `Converged`: ready to implement
- `Revision required`: confirmed convergence issues remain
- `Insufficient evidence`: missing context prevents an implementation-readiness decision

The score measures implementation readiness, not whether the architecture is elegant or optimal.

## Scope

This skill does not propose replacement architectures, perform general code review, edit the reviewed documents, or add optional improvements outside the declared scope.
