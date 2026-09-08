---
name: design-convergence-review
description: Use ONLY when the user explicitly invokes $design-convergence-review or /design-convergence-review, or explicitly says "收敛review" / "收敛评审" / "design convergence review". Reviews a design document, file set, or design folder for implementation readiness, reporting only convergence blockers, warnings, and evidence gaps. Do NOT trigger for general code review, /review, PR review, ordinary design feedback, or any review request that does not explicitly ask for a convergence review, even if the target is a design document, RFC, or ADR set.
---

# Design Convergence Review

Determine whether a design is sufficiently closed, complete, non-duplicative, scoped, and consistent to enter implementation. Review only for convergence. Do not optimize the architecture or replace undecided choices with your own design.

## Inputs

Accept one or more of:

- pasted design content
- a design document path
- multiple related document paths
- a folder containing a multi-document design set

Use these when available:

- scope, goals, and out-of-scope statements
- original requirements or acceptance criteria
- related designs, interface contracts, data models, code conventions, code, and tests
- exclusion patterns for folder review
- a declared design stage; when the user declares the design an early draft, report blocking findings and gating evidence gaps in full, and compress warnings into a short summary list. Each warning summary must retain its precise location, Dimension, Severity, and one-line Problem; warning summaries remain findings for ordering, scoring, and deductions.

Require at least one review target. Stop and report the missing input when no content, file, or folder is provided. Stop and report when the provided target contains no reviewable design content, such as only code, logs, or meeting notes.

## Evidence Boundaries

- Read complete target documents before judging them.
- Use only user-provided evidence or relevant files that can be located in the current workspace.
- Treat code and tests as evidence for design claims, not as general code-review targets.
- Do not fill project-specific gaps from model memory.
- Without scope evidence, flag only content that is clearly unrelated inside the design itself. Do not assert scope creep from preference.
- Without requirements, do not assert complete requirement coverage.
- Without external references, assess internal consistency but mark external consistency as not assessable.
- Separate facts, supported inferences, and missing evidence.

## Folder Review

When the target is a folder or multiple files, read [folder-review.md](references/folder-review.md) before reviewing details. Do not load it for pasted content or a single document.

## Workflow

1. Extract goals, scope, out-of-scope items, constraints, module responsibilities, main flows, failure flows, terminal states, and validation methods.
2. Build the minimum traceability chain:

   `requirement or goal -> design decision -> implementation responsibility -> verification method`

   When no requirements are provided, start the chain from the design's stated goals and do not assert requirement coverage.

3. Record which files define each part of the chain.
4. Evaluate the six convergence dimensions below.
5. Keep only evidence-backed findings and genuine evidence gaps.
6. Merge findings caused by the same root issue. Assign the highest-impact primary dimension and score the root issue once.
7. Assign severity before calculating the verdict and score.

## Review Dimensions

### Closure

Check whether:

- flows have an entry, meaningful states, exit conditions, and terminal states
- goals or requirements trace to design decisions
- module inputs, outputs, responsibilities, and collaboration boundaries close cleanly
- important constraints have executable verification methods
- any design element is unimplementable, unverifiable, or ownerless

### Completeness

Check whether:

- unresolved TODOs, TBDs, placeholders, or open questions block implementation
- initialization, normal behavior, primary failures, recovery, and termination are covered where relevant
- critical edge conditions, rollback, or recovery behavior are missing
- important decisions required by the current scope remain undecided
- upstream requirements have corresponding design and verification evidence when requirements are available
- a design folder contains orphan documents that carry important decisions
- every critical design can be located across a split document set

Do not require a fixed document template. Report missing material only when it affects implementation or verification within the declared scope.

### Redundancy

Check whether:

- terminology, interfaces, data models, or flows are independently defined in multiple places
- repeated definitions can drift and create conflicting implementations
- a single source of truth is missing
- multiple documents claim authority over the same subject
- repetition should become one definition plus references

Ignore harmless summaries and deliberate repetition that cannot create divergence. Report duplication that has not yet diverged here; report definitions that already contradict each other under Consistency.

### Scope Drift

Check whether:

- each design element traces to a stated goal, requirement, or scope item
- platform introductions, framework tutorials, or background material displace actual decisions
- implementation tutorials, future plans, or extension discussions are presented as current design
- declared out-of-scope or unrelated work has entered the design

Require scope, requirement, or stated-goal evidence before confirming scope drift.

### Consistency

Check whether:

- terminology, names, interfaces, states, models, and constraints agree internally
- prose, diagrams, examples, and appendices describe the same facts
- documents agree on versions, definitions, ownership, and status
- cross-document links resolve to current targets and follow declared authority
- the design agrees with provided requirements, contracts, related designs, code conventions, code, and tests
- conflicting definitions lack a clear priority or source of truth

Distinguish internal inconsistency from disagreement with external evidence.

### Evolvability

Check whether:

- variability declared in requirements or scope (multiple providers, pluggable strategies, anticipated variants, versioned interfaces) has a decided extension mechanism
- declared extension points define their contract: interface, registration or dispatch, and constraints, rather than remaining placeholders
- adding a variant that is already declared in scope would, by the design's own statements, require modifying decisions the design marks as closed or stable
- stability commitments (public interfaces, published contracts, frozen schemas) state what is closed to modification, and the rest of the design honors them

Require declared variability, a stated extension point, or an explicit stability commitment before reporting an evolvability finding. Do not speculate about hypothetical future requirements; unrequested flexibility is out of scope, and recommending new abstractions remains prohibited by the review boundary.

## Severity

- **Blocking / 阻塞**: prevents a core flow from being implemented or verified, leaves critical ownership unresolved, omits a key requirement, creates a material contradiction, or confirms scope creep with evidence.
- **Warning / 警告**: does not immediately block implementation but creates important ambiguity, local incompleteness, source-of-truth divergence, or meaningful implementation risk.
- **Cannot assess, gating / 无法判断（阻断判定）**: missing evidence is necessary to decide whether the design can be implemented or verified within the declared scope. State the minimum evidence needed.
- **Cannot assess, non-gating / 无法判断（不阻断判定）**: missing evidence limits an optional or external comparison but does not prevent an implementation-readiness decision. State the limitation without deducting points.

Classify an evidence gap as gating only when its answer could change the admission decision. Missing optional context or evidence outside the requested review boundary is non-gating.

Do not report prose polish, formatting, coding style, personal preference, or optional optimization.

## Review Boundary

Do not:

- propose a new architecture or alternative technology
- discuss future optimization
- expand requirements or invent product decisions
- request refactoring based on preference
- perform general code review
- edit the reviewed documents

Recommend only the smallest action needed for convergence, such as clarifying an existing choice, adding a missing constraint, identifying one authoritative definition, replacing duplication with a reference, or supplying missing evidence.

## Verdict

Choose exactly one in this priority order:

- **Revision required / 需修订**: at least one blocking finding or warning exists, regardless of evidence gaps.
- **Insufficient evidence / 证据不足**: no blocking finding or warning exists, but at least one gating evidence gap prevents an implementation-readiness decision.
- **Converged / 收敛**: no blocking findings, warnings, or gating evidence gaps exist.

Non-gating evidence gaps do not change the verdict. The verdict is authoritative; the score only expresses distance to convergence and never overrides the verdict.

## Score

Start from 100 and score merged root causes:

- subtract 25 for each blocking finding
- subtract 6 for each warning
- subtract 10 for each gating evidence gap
- do not deduct for non-gating evidence gaps
- score a shared root cause once at its highest severity
- use a minimum score of 0

The score represents implementation readiness, not general architecture quality.

## Output

Write the report in the language the user used to request the review, keeping the English enum values for Dimension, Severity, and Verdict. Start with the verdict. Load [report-format.md](references/report-format.md) for the score band table, the report skeleton, finding ordering, and the finding quality bar.
