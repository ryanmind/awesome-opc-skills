# Commit Execution

Read this file only in commit mode.

## Preconditions

1. Confirm that staged changes exist.
2. Record the intended staged path set with `git diff --cached --name-only` before committing.
3. Confirm that the recorded paths match the user's requested scope.
4. Stop on unresolved conflicts, suspected secrets, or unrelated staged intents that should be split.
5. Preserve all unstaged and untracked user changes.
6. Run relevant pre-commit verification when the repository or user requires it. If verification cannot run, report that before committing when the risk is material.

## Commit

- Use a non-interactive `git commit` command.
- Pass a single-line message with `git commit -m <subject>`.
- For a body, pass the subject and body as separate `-m` arguments.
- Do not amend, bypass hooks, disable signing, or use `--no-verify` unless the user explicitly requests it.
- If hooks modify files or reject the commit, inspect the new status and report the exact result. Do not retry blindly.

## Verification

After success:

1. Read the new commit subject and summary with `git show --stat --oneline --decorate --no-renames HEAD` or an equivalent read-only command.
2. Read the committed path set with `git diff-tree --no-commit-id --name-only -r HEAD`.
3. Confirm that the subject matches the generated message and the committed paths match the recorded staged set.
4. Report the short commit hash and subject.

If `git commit` fails, do not claim success. Report the failure and the minimum next action.
