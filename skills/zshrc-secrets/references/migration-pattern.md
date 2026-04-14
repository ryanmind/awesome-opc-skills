# Migration Pattern

## Goals

- Remove plaintext sensitive values from shell startup files.
- Keep the original environment variable names.
- Keep shell behavior unchanged.
- Keep all terminal and documentation output redacted.

## Preferred naming

Convert the env var name to lowercase snake case for the secret filename.

| Env var | Secret file |
| --- | --- |
| `OPENAI_API_KEY` | `~/.secrets/openai_api_key` |
| `ANTHROPIC_API_KEY` | `~/.secrets/anthropic_api_key` |
| `FEISHU_APP_SECRET` | `~/.secrets/feishu_app_secret` |
| `FEISHU_APP_ID` | `~/.secrets/feishu_app_id` |

## Preferred rewrite

From:

```bash
export OPENAI_API_KEY="<MASKED_LITERAL>"
```

To:

```bash
export OPENAI_API_KEY="$(cat ~/.secrets/openai_api_key)"
```

## Keep redacted during audits

Safe to show:

- variable name
- line number
- whether it is `literal`, `reference`, `command`, or `secrets-file`
- target path like `~/.secrets/openai_api_key`

Never show:

- literal values
- `cat ~/.secrets/...` output
- screenshots or pasted diffs containing real values

## Permission baseline

```bash
mkdir -p ~/.secrets
chmod 700 ~/.secrets
find ~/.secrets -type f -exec chmod 600 {} +
```

## Edge cases

### Existing file-based loads

If the shell file already uses `$(cat ~/.secrets/...)`, treat it as migrated. Do not churn it unless the user asks for cleanup.

### Generic names that look sensitive but are not

Be conservative with broad matches. Do not auto-migrate obvious non-secret settings such as:

- `KEYCHAIN_PATH`
- `AUTHORS`
- `MONKEY_TYPE`

### Multi-line helper functions

When a helper function passes env vars through `env -u` or similar, document the variable names only. Those lines may mention secret-bearing vars but do not themselves contain the secret value.

### ID-like values

Some IDs are public and some are not. If the user explicitly says to migrate `id` values too, include `APP_ID`, `CLIENT_ID`, `ORG_ID`, `BOT_ID`, and similar identifiers in the audit/migration set.
