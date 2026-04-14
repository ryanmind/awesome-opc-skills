# Zshrc Secrets

Audit and migrate sensitive shell environment variables from `~/.zshrc` or similar shell startup files into per-file entries under `~/.secrets`, while keeping output redacted and preserving env var names.

## Overview

This skill is for safely hardening local shell configuration without exposing credentials in terminal output, docs, or screenshots.

It helps with:

- auditing `~/.zshrc`, `~/.zprofile`, `~/.bashrc`, and similar files
- identifying likely secret-bearing env vars
- rewriting config to load values from `~/.secrets/...`
- checking permissions without printing secret contents
- documenting the migration in a redacted way

## Security model

The skill is intentionally conservative:

- it never prints real secret values
- it never dumps `~/.secrets/*` contents
- it reports only variable names, line numbers, load mode, and target file paths
- it avoids broad false-positive matches for generic names like `KEYCHAIN_PATH` or `AUTHORS`

## Sensitive names detected by default

The audit script looks for names such as:

- `*TOKEN*`
- `*SECRET*`
- `*PASSWORD*` / `*PASS*`
- `*COOKIE*`
- `*WEBHOOK*`
- `*DSN*`
- `*_API_KEY`
- `*_ACCESS_KEY`
- `*_SECRET_KEY`
- `*_PRIVATE_KEY`
- `*_AUTH_TOKEN`, `*_AUTH_KEY`, `*_AUTH_SECRET`
- `*_SESSION_TOKEN`, `*_SESSION_KEY`, `*_SESSION_SECRET`, `*_SESSION_COOKIE`

ID-like values such as `APP_ID` or `CLIENT_ID` are included only when requested via `--include-id` or when the migration explicitly covers ID hardening.

## Files

```text
skills/zshrc-secrets/
├── SKILL.md
├── README.md
├── agents/openai.yaml
├── references/migration-pattern.md
└── scripts/audit_zshrc_secrets.py
```

## Quick start

### Run a redacted audit

```bash
python3 skills/zshrc-secrets/scripts/audit_zshrc_secrets.py ~/.zshrc
```

Include `*_ID`-style values too:

```bash
python3 skills/zshrc-secrets/scripts/audit_zshrc_secrets.py ~/.zshrc --include-id
```

Example output:

```text
line    name                mode          target
12      OPENAI_API_KEY      literal       ~/.secrets/openai_api_key
19      ANTHROPIC_API_KEY   command       ~/.secrets/anthropic_api_key
27      APP_SESSION_TOKEN   literal       ~/.secrets/app_session_token
```

## Migration pattern

Before:

```bash
export OPENAI_API_KEY="<MASKED_LITERAL>"
```

After:

```bash
export OPENAI_API_KEY="$(cat ~/.secrets/openai_api_key)"
```

## Permission baseline

```bash
mkdir -p ~/.secrets
chmod 700 ~/.secrets
find ~/.secrets -type f -exec chmod 600 {} +
```

## False positives intentionally avoided

These should stay inline unless the user explicitly wants them externalized:

- `KEYCHAIN_PATH`
- `AUTHORS`
- `MONKEY_TYPE`
- normal URLs, paths, and non-secret config values

## Usage in a Codex / Claude-style agent

Examples:

```text
Use zshrc-secrets to audit my ~/.zshrc and show only redacted output.
Use zshrc-secrets to migrate API keys from ~/.zprofile into ~/.secrets.
Use zshrc-secrets to check whether my secret files have safe permissions.
```

## Notes

- Preserve existing variable names unless the user asks to rename them.
- If a line already loads from `~/.secrets/...`, treat it as migrated.
- Prefer minimal, behavior-preserving edits over large rewrites.
