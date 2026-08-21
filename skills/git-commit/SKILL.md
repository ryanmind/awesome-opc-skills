---
name: git-commit
description: Draft repository-aware commit messages or create Git commits from staged changes. Use when the user asks for a commit message, says git commit or commit these changes, or asks to submit staged changes.
---

# Git Commit

Generate an accurate Conventional Commits message from the actual diff. Create the commit when the user asks to commit; otherwise return the message only.

## Message Contract

- Every generated subject MUST use `type(scope): subject` or `type: subject`.
- Mark every confirmed breaking change with `!` before `:` or a `BREAKING CHANGE:` footer; either form is valid, and both may be used.
- Require a type. Include a scope only when the diff or repository rules identify a stable scope; never invent one.
- Let enforceable repository rules refine allowed types, scopes, ticket identifiers, length, casing, and trailers.
- If an enforceable repository rule requires an incompatible message format, stop and report the conflict. Do not silently fall back to a non-Conventional subject.

## Operation Modes

Choose the operation from the request:

- **Message mode**: draft a message without changing Git state.
- **Commit mode**: create a commit from already staged changes and verify it.

## Decision Priority

Apply rules in this order:

1. The mandatory message contract above
2. Compatible enforceable repository rules
3. Compatible explicit user instructions
4. Default type, scope, subject, and body rules

Do not use repository history to choose the message format.

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
7. If staged changes exist, use only the staged diff as message evidence; leave unstaged and untracked changes out of the message and commit.
8. Stop when no relevant changes exist.
9. Check for conflict markers, sensitive data, generated noise, binary-only changes, unrelated intents, and breaking behavior. Warn or stop when committing would be unsafe.
10. Derive the message from the diff's primary intent. Do not invent changes or scopes.
11. Apply the mandatory message contract, then compatible repository rules and explicit user instructions.
12. Read [default-rules.md](references/default-rules.md) for type, scope, subject, or body decisions left open.
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
- Do not create or switch branches, push, amend, rebase, bypass hooks, or change signing behavior unless the user explicitly requests that separate operation.

## Output

- Message mode: return one best subject; add a body only when the why, impact, migration, or caveat matters.
- Commit mode: report the commit hash and subject after verification.
- If blocked: state the exact blocker and the minimum action needed.
- If a split is needed: identify the unrelated groups before suggesting any fallback message.
