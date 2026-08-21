# Default Commit Rules

Read only the sections needed when repository rules and explicit user instructions leave a decision open.

## Message Shape

- Use `type(scope): subject` or `type: subject`; this format is mandatory.
- Omit scope when it would be guessed, unstable, or cross-cutting.
- Use English unless the user clearly requests another language.
- Keep the subject specific, imperative, and without a trailing period.
- Keep the subject within 50 characters when practical.
- Add a body only when the why, impact, migration, trade-off, or caveat matters; wrap it at about 72 characters.
- Do not include implementation trivia unless it is the system-relevant change.

## Type Selection

Choose the smallest accurate type:

- `feat`: new capability or user-visible behavior
- `fix`: bug, regression, or incorrect behavior
- `perf`: performance improvement without intended behavior change
- `refactor`: structural change without intended behavior change
- `docs`: documentation only
- `style`: formatting or lint only, with no logic change
- `test`: tests only
- `chore`: tooling, dependencies, configuration, maintenance, or generated housekeeping

If no intent dominates, recommend splitting the commit.

## Scope Selection

1. In a multi-module repository, prefer the affected app, package, or module.
2. In a single-module repository, use a stable feature area.
3. Omit scope for repository-wide or unrelated multi-area changes.
4. Do not invent a scope merely to satisfy the default shape.

## Edge Cases

- Breaking change: mark every confirmed break with `!` before `:` or a `BREAKING CHANGE:` footer. Prefer `!` for a visible subject signal; add the footer when migration impact needs explanation. `BREAKING-CHANGE:` is a valid synonym, but default to `BREAKING CHANGE:`.
- Binary-only diff: describe the asset or artifact changed.
- Generated files: focus on the visible source change; otherwise use `chore`.
- Pure move or rename: use `refactor` when structure changed, otherwise `chore`.
- Formatting mixed with logic: ignore formatting noise and classify the logic change.

## Examples

```text
feat(auth): add WeChat QR login
fix(api): handle null user response
refactor(db): migrate queries to async API
docs: update authentication guide
chore(deps): update axios security patch
test(auth): cover login regression
feat(api): remove legacy authentication

BREAKING CHANGE: clients must migrate to the session API
```

Avoid vague subjects, mixed intents, past tense, trailing periods, and claims not supported by the diff.
