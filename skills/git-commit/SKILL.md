---
name: git-commit
description: Conventional Commits helper for Git commit messages.
---

# Git Commit

## Workflow

1. **Check constraints**: Scan for `.commitlintrc.js`, `commitlint.config.js`, `husky` configs, or `package.json` for linting rules. These override all following heuristics.
2. **Check staged changes**: Execute `git diff --cached` first.
3. **Fallback to unstaged**: If no staged changes, execute `git diff` and inform user.
4. **No changes**: If both empty, inform user and stop.
5. **Learn repo patterns**: Execute `git log --oneline -20 --format="%s"` to understand existing commit style.
6. **Analyze changes**: Review diff to determine change intent and affected components.
7. **Infer type**: Match change intent to type (feat/fix/perf/refactor/docs/style/test/chore).
8. **Detect edge cases**: Flag if diff contains only binary files, breaking change indicators, or cross-cutting changes — adjust plan accordingly.
9. **Safety gate + plan**: Block on sensitive data/conflict markers; show type/scope/subject for confirmation before generating.
10. **Generate message**: Output final message after user confirms the plan.

## Message Rules

- Allowed `type`: `feat`, `fix`, `perf`, `refactor`, `docs`, `style`, `test`, `chore`.
- Primary format: `type(scope): subject` (Conventional Commits).
- Compatible format: `[Module]type: subject` only when repository convention explicitly requires it.
- **Language**: Use English unless the user or repo convention clearly specifies otherwise.
- Keep subject short, specific, and action-oriented.
- Avoid trailing period in subject.
- **Forbidden content**: No sign-off lines (e.g., Co-Authored-By) in commit messages.

## Type Selection Heuristics

- `feat`: new user-visible behavior or capability.
- `fix`: bug fix or regression fix.
- `perf`: performance improvement without behavior change.
- `refactor`: internal restructuring without behavior change.
- `docs`: documentation-only changes.
- `style`: formatting/lint-only changes, no logic change.
- `test`: test-only additions or updates.
- `chore`: tooling, dependency, config, or maintenance work.

## Scope/Module Selection

**Priority order:**
1. **Multi-module repos**: Use top-level directory (e.g., `api`, `web`, `mobile`, `admin`).
2. **Single-module repos**: Use feature area (e.g., `auth`, `payment`, `order`, `ui`).
3. **Cross-cutting changes**: Omit scope if multiple unrelated areas are affected.
4. **When uncertain**: Omit scope rather than guessing.

**Module format `[Module]type:`**: Only use when repo history consistently shows this pattern.

## Output Patterns

- **Default**: Provide 1 best message (subject only for simple changes).
- **If user asks for options**: Provide 3 alternatives with different type/scope emphasis.
- **If user asks for commit body**: Return subject + blank line + bullet points (use `-` prefix).
- **Footer lines**: Add when relevant (e.g., `Refs: #123`, `BREAKING CHANGE: ...`).
- **Insufficient context**: Ask for missing information instead of guessing.

## When to Add Commit Body

**Add body when:**
- Multiple related changes in one commit
- Need to explain "why" not just "what"
- Technical trade-offs or design decisions
- Breaking changes or migration steps
- Complex refactoring with multiple steps

**Skip body when:**
- Simple single-line fix or addition
- Self-explanatory changes (e.g., `docs: fix typo`)
- Small scope with obvious intent

**Example with body:**
```
refactor(api): migrate from REST to GraphQL

- Reduce over-fetching by 60%
- Enable client-side caching with Apollo
- Maintain backward compatibility via REST adapter
- Migration guide: docs/graphql-migration.md
```

```
fix(order): fix amount calculation when discount applied

- Handle edge case when multiple discounts stack
- Add validation for negative amounts
- Update test cases for discount scenarios
```

## Examples

**Good:**
```
feat(auth): add WeChat QR login
fix(api): handle null response in user query
refactor(db): migrate from callbacks to async/await
docs: update API documentation
chore(deps): upgrade axios to fix security vulnerability
test(auth): add unit tests for login flow
```

**Bad:**
```
Update code                          # Too vague
feat: add login and fix bugs         # Mixed types
Fix bug.                             # Has trailing period
feat(auth): implemented login        # Wrong tense
```

## Senior-Level Writing

**Principle: State facts, not intentions.** Commit messages are historical record, not announcements.

**Voice:** Use imperative mood ("add feature" not "added feature", "fix bug" not "fixed bug"). Avoid first-person and future tense.

**Rationale:** Body explains the consequence of the change, not the change itself. "Without this, the pool exhausts under load" — not "This commit adds connection pooling."

**Specificity:** Name the actual problem or mechanism. "Fix race condition in pool allocation" over "Improve resource handling."
