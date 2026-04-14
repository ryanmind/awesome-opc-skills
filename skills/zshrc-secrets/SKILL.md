---
name: zshrc-secrets
description: Standardize sensitive shell configuration by moving token, API key, auth token, secret, password, cookie, webhook, DSN, and optionally id-like values out of ~/.zshrc into ~/.secrets files while preserving environment variable names and behavior. Use when auditing or migrating zshrc/bashrc profile files, hardening shell env handling, updating docs after secret migration, or verifying ~/.secrets permissions without printing real values.
---

# Zshrc Secrets

Migrate sensitive values from shell rc files into per-file entries under `~/.secrets`. Never print secret values, paste them into docs, or echo secret file contents.

## Scope

Default to `~/.zshrc`. Reuse the same pattern for `~/.zprofile`, `~/.bashrc`, and similar shell startup files when requested.

Treat these names as sensitive by default:

- `*TOKEN*`
- `*SECRET*`
- `*PASSWORD*` or `*PASS*`
- `*COOKIE*`
- `*WEBHOOK*`
- `*DSN*`
- `*_API_KEY`
- `*_ACCESS_KEY`
- `*_SECRET_KEY`
- `*_PRIVATE_KEY`
- `*_AUTH_TOKEN`, `*_AUTH_KEY`, `*_AUTH_SECRET`
- `*_SESSION_TOKEN`, `*_SESSION_KEY`, `*_SESSION_SECRET`, `*_SESSION_COOKIE`

Be conservative with generic names like `KEY`, `AUTH`, `SESSION`, and filesystem paths. Do not migrate obvious non-secret settings like `KEYCHAIN_PATH`, `AUTHORS`, or other normal config names unless the user explicitly asks.

Treat `*_ID`, `APP_ID`, `CLIENT_ID`, `ORG_ID`, `BOT_ID`, and similar identifiers as sensitive when the user asks for `id` hardening too, or when the ID is paired with a secret-bearing integration.

## Workflow

1. **Audit redacted only**
   - Inspect the shell file.
   - Report only variable names, line numbers, load mode, and target secret path.
   - Replace any literal or command value with placeholders like `<MASKED>`.
   - Use `scripts/audit_zshrc_secrets.py <shell-file>` for a fast redacted inventory.

2. **Choose what to externalize**
   - Migrate all secret-bearing variables by default.
   - Include `*_ID` variables only when requested or clearly sensitive in context.
   - Preserve non-sensitive URLs, paths, and normal config inline unless the user asks otherwise.

3. **Map env vars to secret files**
   - Keep the environment variable name unchanged.
   - Store the value in `~/.secrets/<lower_snake_case_name>`.
   - Example mapping: `OPENAI_API_KEY` → `~/.secrets/openai_api_key`.

4. **Rewrite the shell config without changing behavior**
   - Preferred form:
     ```bash
     export VAR="$(cat ~/.secrets/var_name)"
     ```
   - Preserve surrounding comments and ordering when practical.
   - If a variable already reads from `~/.secrets/`, keep it unless the user asks for normalization.

5. **Harden permissions**
   - Ensure `~/.secrets` is `700`.
   - Ensure each secret file is `600`.
   - Never print file contents during validation.

6. **Validate safely**
   - Verify the variable names still exist in the shell file.
   - Verify the referenced secret files exist.
   - If useful, run `zsh -n ~/.zshrc`.
   - Report only names, paths, and status.

7. **Update docs redacted**
   - Record variable names, file paths, and migration status.
   - Do not write real values into docs, diffs, screenshots, or terminal output.

## Operating Rules

- Never echo or display a real secret value.
- Never paste secret file contents into markdown.
- Prefer redacted audits before making edits.
- Preserve variable names and runtime behavior unless the user explicitly asks to rename or refactor.
- When showing examples, use fake placeholders only.

## Resources

- `scripts/audit_zshrc_secrets.py`: redacted audit for shell files.
- `references/migration-pattern.md`: naming rules, edge cases, and redacted examples.
