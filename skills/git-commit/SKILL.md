---
name: git-commit
description: Use when the user asks to git commit, commit changes, create a commit, write a commit message, or submit staged changes. Generate repository-aware commit messages from staged changes, following repository conventions before heuristics.
---
# Git Commit
Generate the best commit message from the repo's actual constraints and diff. Optimize for correctness first, then low-friction output.

## Decision Priority
Always decide in this order:
1. **Repo hard constraints** — commitlint, hooks, templates, release tooling, documented conventions
2. **Explicit user instructions**
3. **Actual diff** — staged first, unstaged only if nothing is staged
4. **Repo history** — only when recent commit subjects show a clear, consistent, high-signal local convention
5. **Heuristics** — use Conventional Commits best practices when stronger signals are absent
Never let heuristics override repository rules.
Repo hard constraints override everything else.
When no hard constraints exist, explicit user instructions override repo history and heuristics.
Treat repo history as advisory, not binding. Ignore it when it is inconsistent, vague, low-quality, or conflicts with better commit-writing practice.

## Workflow
1. **Find constraints**
   - Check `.commitlintrc*`, `commitlint.config.*`, `package.json`, `.husky/*`, `.git/hooks/*`, `lefthook.yml`, `.gitmessage`, `.github/*`, release tooling, and docs.
   - If the repo requires a non-standard format, follow it.
2. **Inspect staged changes first** with `git diff --cached`.
3. **Fallback to unstaged** with `git diff` only if staged diff is empty, and tell the user.
4. **Stop if no changes** when both diffs are empty.
5. **Learn local style** with `git log --oneline -20 --format="%s"` and adopt it only when recent history shows a clear, stable, high-signal pattern worth following.
6. **Classify the change** by primary intent and affected area.
7. **Run safety checks** for conflict markers, secrets, generated noise, binary-only diffs, and breaking changes.
8. **Generate directly by default**: return the best subject immediately; add a body only when the diff is complex or the why matters; ask only if ambiguity would materially change type, scope, or breaking-change status.

## Fallback Mode (Low Context)
Use fallback mode only when no stronger repository signal is available — for example, repo constraints are absent and recent history or usable git metadata is unavailable, inconsistent, or low-signal.
- Repo constraints always win over fallback heuristics when present
- Treat weak or low-quality history as no history
- Default to Conventional Commits best practices
- Infer type from keywords in the diff or description
- Omit scope unless clearly identifiable
- Keep the subject concise and imperative
- Do not ask questions unless ambiguity is critical

## Question Policy
Default to one-shot output.
Ask only when:
- The diff mixes unrelated intents and should likely be split
- The commit could reasonably be `feat` or `fix` and the choice matters
- The scope is materially ambiguous and the repo strongly prefers scopes
- The diff implies a breaking change but the migration impact is unclear
- Repo rules conflict or cannot be inferred confidently
If a question would not meaningfully change the message, do not ask it.

## Message Rules
- Prefer `type(scope): subject` when repo convention allows it.
- Omit `scope` when it would be a guess or the change is cross-cutting.
- Use English unless the user or repo clearly prefers another language.
- Keep the subject short, specific, imperative, and without a trailing period.
- Do not include implementation trivia unless it is the real system-relevant change.
- Do not imitate vague or low-quality repo history when better signals exist.
- Do not add footer or trailer lines unless the repo or user explicitly requires them.

## Formatting Constraints
- Keep subject within 50 characters when possible
- Use imperative mood
- Avoid trailing period
- Wrap body at ~72 characters if present

## Type Selection
Use the smallest accurate type:
- `feat` — new capability or user-visible behavior
- `fix` — bug, regression, or incorrect behavior fix
- `perf` — performance improvement without intended behavior change
- `refactor` — structural change without intended behavior change
- `docs` — documentation only
- `style` — formatting or lint only, no logic change
- `test` — tests only
- `chore` — tooling, dependencies, config, maintenance, or generated housekeeping
If the diff has multiple intents, choose the dominant reason the commit exists. If there is no dominant reason, say the commit should likely be split.

## Scope Selection
Choose scope conservatively:
1. Multi-module repo: top-level app/package/module
2. Single-module repo: feature area
3. Repo-wide or unrelated multi-area change: omit scope
4. Stable repo history uses no scope: do not invent one
Use formats like `[Module]type: subject` only when repo history or config clearly and consistently requires them.

## Body and Edge Cases
Add a body when the why matters: multiple tightly related changes, trade-offs, migrations, caveats, or breaking changes. Prefer short factual bullets.
Handle edge cases directly:
- **Breaking change**: call it out clearly in the subject or body; use a marker or trailer only when the repo or user explicitly requires it
- **Binary-only diff**: describe the asset/artifact changed
- **Generated files**: focus on the source change if visible; otherwise use `chore`
- **Pure moves/renames**: use `refactor` or `chore` based on behavior impact and repo convention
- **Formatting + logic mixed**: ignore formatting noise and classify the logic change
- **Sensitive data or conflict markers**: stop and warn instead of polishing a message

## Safety Rules
- Do not invent changes not present in the diff
- Do not assume repository conventions without evidence
- Prefer correctness over specificity when uncertain

## Output Patterns
- **Default**: return 1 best commit subject
- **If useful**: add 1 short sentence explaining type/scope choice
- **If asked for options**: provide 3 clearly different alternatives
- **If asked for a body**: return subject, blank line, then bullets
- **If the commit should be split**: say so before suggesting any fallback message

## Examples
**Good:**
```
feat(auth): add WeChat QR login
fix(api): handle null response in user query
refactor(db): migrate callbacks to async/await
docs: update API authentication guide
chore(deps): upgrade axios for security patch
test(auth): add login flow regression tests
```
**Bad:**
```
Update code
feat: add login and fix bugs
Fix bug.
feat(auth): implemented login
```

## Writing Standard
Commit messages are historical records, not status updates.
- State facts, not intentions
- Name the actual behavior, bug, or mechanism
- Keep bodies about why, impact, and caveats
- Do not add ceremony the repo did not ask for
