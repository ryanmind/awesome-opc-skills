# Report Format

Read this file when writing the review report, not while evaluating the design. It contains no
judgment rules — only presentation.

## Score Bands

The score is computed in `SKILL.md`. It represents implementation readiness, not general
architecture quality.

| Score | Typical state |
| --- | --- |
| 100 | Converged; ready for implementation |
| 80-99 | A few warnings or evidence gaps to resolve |
| 50-79 | A blocking finding, or several warnings and gaps |
| 0-49 | Multiple blocking findings; do not begin implementation |

## Report Skeleton

Write the report in the language the user used to request the review, keeping the English enum
values for Dimension, Severity, and Verdict. Start with the verdict, then use this structure:

```markdown
## Review Basis

- Target documents: ...
- Scope: provided / not provided
- Requirements: provided / not provided
- External evidence: ...
- For multiple files or folder reviews only: included files; excluded or uncertain files and reasons; confirmed entry, reference, and authority relationships

## Findings

### [file path / section or precise location]

- Dimension: Closure / Completeness / Redundancy / Scope Drift / Consistency / Evolvability
- Severity: Blocking / Warning / Cannot assess, gating / Cannot assess, non-gating
- Evidence: quote or accurately summarize the target and reference evidence
- Problem: one sentence explaining the implementation, verification, or shared-understanding impact
- Minimum action: the smallest change or evidence required for convergence

## Convergence Score

- Score: XX / 100
- Deductions: N blocking, N warning, N gating evidence gaps

## Admission Decision

One sentence: enter implementation, revise and review again, or supply evidence and review again.
```

## Ordering

Order findings by blocking, warning, then cannot assess. When no findings exist, state that no
convergence-affecting issue was found. Do not manufacture findings to cover every dimension.

## Finding Quality Bar

- Acceptable: "`design.md` §4.2 caps retries at 3; the §6 sequence diagram loops without a retry
  limit" — cites both locations and states the contradiction.
- Not acceptable: "error handling could be more robust" — no location, no evidence, and an
  architecture preference rather than a convergence gap.
