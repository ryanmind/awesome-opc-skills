---
name: git-commit
description: Draft repository-aware Conventional Commit messages or create atomic Git commits from staged or selected working-tree changes.
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
- **Commit mode**: create one or more atomic commits from the selected working-tree changes and verify them. Atomicity is mandatory for every scope choice, including A, B, and automatic all-change selection.

## Decision Priority

Apply rules in this order:

1. The mandatory message contract above
2. Compatible enforceable repository rules
3. Compatible explicit user instructions
4. Default type, scope, subject, and body rules

Do not use repository history to choose the message format.

## Workflow

1. Determine message mode or commit mode.
2. Run `git status --short` to identify staged, unstaged, untracked, and conflicting paths. Interpret its two porcelain columns literally: `X` is the index/staged state and `Y` is the working-tree/unstaged state; the `?` in `??` means untracked, not staged. Do not infer staging boundaries from the number of edited files, an app's edit card, or `git diff --stat` alone. For example, ` M file` is unstaged-only, `M  file` is staged-only, `MM file` has both, and `?? file` is untracked-only.
3. In commit mode, determine the commit scope before inspecting or changing the index:
   - Ask exactly one A/B question only when at least one path has an actual staged/index status (`X` is neither a space nor `?`) and at least one path has an actual unstaged/worktree status (`Y` is neither a space nor `?`) or is untracked (`??`). A second edited file alone is not evidence of both scopes:
     - **A. Only commit staged changes** — leave all unstaged and untracked changes untouched.
     - **B. Commit all changes** — include staged, unstaged, and untracked changes, grouping them into atomic commits.
   - If no path has an actual staged/index status and tracked or untracked changes exist, select all of them automatically and keep the commits atomic. Do not stop merely because the index is empty or ask A/B for multiple unstaged files.
   - If at least one path has an actual staged/index status and no path has an actual unstaged/worktree status or is untracked, select the staged changes.
   - In message mode, do not ask this scope question or change Git state; use the existing staged-first, unstaged-fallback evidence rules below.
4. Use low-output discovery for repository rules:
   - Find dedicated rule sources with `git ls-files`: commitlint config, hooks, `lefthook`, `.gitmessage`, and explicit commit or release configuration.
   - Search broad tracked candidates such as `package.json`, `.github/**`, contribution guides, `AGENTS.md`, and development guides for commit-related keywords before treating them as candidates.
   - Check `.git/hooks/commit-msg` separately when it exists.
5. Read [repository-rules.md](references/repository-rules.md) only when a dedicated source exists or a broad candidate contains a commit-related match.
6. Inspect the selected scope. Start with `git diff --cached --stat` and `git diff --cached`, then inspect the relevant working-tree diff and untracked paths when the selected scope includes them.
7. If the staged diff is empty:
   - In message mode, inspect `git diff --stat` and `git diff` for unstaged tracked changes.
   - Also identify untracked paths from `git status --short`. For relevant, safe-to-read text files, inspect their names and contents; summarize directories or binary files without attempting to read them.
   - Clearly state when the message is based on unstaged and/or untracked changes. Stop only when neither exists.
   - In commit mode, this branch applies only when the selected scope is staged-only. If the selected scope includes unstaged or untracked changes, continue with those changes instead of stopping.
8. If staged changes exist in message mode, use only the staged diff as message evidence; leave unstaged and untracked changes out of the message. If the staged diff is empty, use relevant unstaged and untracked changes as described above.
9. Stop when no relevant changes exist.
10. Check for conflict markers, sensitive data, generated noise, binary-only changes, unrelated intents, and breaking behavior. If any selected change is clearly unsuitable for committing, pause and ask how to handle it before changing the index or committing. Identify the path and reason, but never expose secret values. Do not silently omit, force through, or reclassify the change. Suspected secrets may only be excluded, remediated and re-inspected, or left uncommitted.
11. Partition the selected changes by primary intent before writing messages. Each atomic group must be independently understandable and must not mix unrelated fixes, features, documentation, tests, or housekeeping. A single logical change may span multiple files; do not split such a change merely by file.
12. Derive one message per atomic group from that group's diff. Do not invent changes or scopes.
13. Apply the mandatory message contract, then compatible repository rules and explicit user instructions.
14. Read [default-rules.md](references/default-rules.md) for type, scope, subject, or body decisions left open.
15. If the selected changes cannot be partitioned into coherent atomic groups, ask how to handle the conflicting groups instead of producing a mixed fallback message. If a group boundary is clear, create separate atomic commits; ask only when the correct treatment is materially uncertain.
16. In message mode, return the best message directly (or one message per clearly separable group when the evidence contains multiple intents).
17. In commit mode, read [commit-execution.md](references/commit-execution.md), stage only the selected changes as needed, create the atomic commits non-interactively, and verify every result.

## Question Policy

Default to one-shot execution or output. In commit mode, the staged-plus-unstaged boundary question above is mandatory. Also ask before committing when a selected change is clearly unsuitable or its atomic-group treatment is materially uncertain. Otherwise ask only when the answer would materially change the type, required scope, or breaking-change status.

## Safety Boundary

- Never stage changes outside the selected scope. In commit mode, selecting **B** or automatically selecting all changes when the index is empty authorizes staging those in-scope changes, including untracked files, as needed to create atomic commits.
- Atomicity is mandatory even when the selected scope contains one file or was already staged: do not combine unrelated intents into one commit.
- When splitting into multiple commits, leave each not-yet-committed in-scope group in the working tree or index and preserve all out-of-scope changes exactly.
- Never include unrelated user changes to make a commit look complete.
- Never expose secret values while reporting a sensitive-data finding.
- For unresolved conflicts or other clearly unsuitable changes, pause and ask whether to exclude the change, handle it separately, or stop. For suspected secrets, ask only whether to exclude them, remediate and re-inspect them, or stop; never commit suspected secret content, even in a separate commit. Do not proceed until the user decides; do not reveal secret values.
- Do not add trailers such as `Co-Authored-By`, `Signed-off-by`, or AI attribution unless explicitly required by the user or repository.
- Do not create or switch branches, push, amend, rebase, bypass hooks, or change signing behavior unless the user explicitly requests that separate operation.

## Output

- Message mode: return one best subject per atomic group; when there are multiple groups, return one clearly labeled message per group. Add a body only when the why, impact, migration, or caveat matters.
- Commit mode: report every created commit's short hash and subject after verification, then report the final status and preserved changes.
- If blocked: state the exact blocker, ask how it should be handled, and do not commit until the decision is clear.
- If a split is needed: identify the atomic groups and their messages before committing them.
