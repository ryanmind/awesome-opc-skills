---
name: git-commit
description: Draft repository-aware commit messages or create Git commits from staged changes. Use when the user asks for a commit message, says git commit or commit these changes, or asks to submit staged changes.
---

# Git Commit

Generate an accurate commit message from the actual diff. Create the commit when the user asks to commit; otherwise return the message only.

## Operation Modes

Choose the operation from the request:

- **Message mode**: draft a message without changing Git state.
- **Commit mode**: create a commit from already staged changes and verify it.

## Decision Priority

Apply rules in this order:

1. Enforceable repository rules
2. Explicit user instructions that do not violate enforceable rules
3. Clear, consistent repository history when it is useful and does not conflict above
4. Default rules

Treat history as advisory. Do not copy vague or inconsistent subjects.

## Workflow

1. Determine message mode or commit mode.
2. Run `git status --short` to identify staged, unstaged, untracked, and conflicting paths.
3. Use low-output discovery for repository rules:
   - Find dedicated rule sources with `git ls-files`: commitlint config, hooks, `lefthook`, `.gitmessage`, and explicit commit or release configuration.
   - Search broad tracked candidates such as `package.json`, `.github/**`, contribution guides, `AGENTS.md`, and development guides for commit-related keywords before treating them as candidates.
   - Check `.git/hooks/commit-msg` separately when it exists.
4. Read [repository-rules.md](references/repository-rules.md) only when a dedicated source exists or a broad candidate contains a commit-related match.
5. Inspect staged changes with `git diff --cached --stat` and `git diff --cached`.
6. If the staged diff is empty:
   - In message mode, inspect `git diff --stat` and `git diff`, clearly stating that the message is based on unstaged changes.
   - In commit mode, stop. Do not stage files unless the user explicitly asks.
7. Stop when no relevant changes exist.
8. Check for conflict markers, sensitive data, generated noise, binary-only changes, unrelated intents, and breaking behavior. Warn or stop when committing would be unsafe.
9. Derive the message from the diff's primary intent. Do not invent changes or scopes.
10. Apply confirmed repository rules and explicit user instructions.
11. Inspect recent history only when message style remains undecided and a small subject-only sample could resolve it.
12. Read [default-rules.md](references/default-rules.md) only for decisions that repository rules, the user, and useful history leave open.
13. If the change has no dominant intent, recommend splitting it before producing a fallback message.
14. In message mode, return the best message directly.
15. In commit mode, read [commit-execution.md](references/commit-execution.md), create the commit non-interactively, and verify the result.

## Question Policy

Default to one-shot execution or output. Ask only when the answer would materially change the type, required scope, breaking-change status, staging boundary, or whether unrelated changes should be split.

## Safety Boundary

- Never stage files implicitly.
- Never include unrelated user changes to make a commit look complete.
- Never expose secret values while reporting a sensitive-data finding.
- Stop on unresolved conflicts or suspected secrets.
- Do not add trailers such as `Co-Authored-By`, `Signed-off-by`, or AI attribution unless explicitly required by the user or repository.

## Output

- Message mode: return one best subject; add a body only when the why, impact, migration, or caveat matters.
- Commit mode: report the commit hash and subject after verification.
- If blocked: state the exact blocker and the minimum action needed.
- If a split is needed: identify the unrelated groups before suggesting any fallback message.
