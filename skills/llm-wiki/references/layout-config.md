# Layout Configuration

Use this reference when a wiki has a custom directory structure or when explaining how to publish
the skill for other users.

## File and Precedence

The scripts look for `<wiki-root>/llm-wiki.json` after resolving the root. A path passed with
`--config` takes precedence; `LLM_WIKI_CONFIG` is the next fallback. A missing optional file uses
the built-in layout for backward compatibility (default formal: `domains/**/*.md`, `entities/**/*.md`,
`workshop/*/README.md`, `_meta/topic-map.md`, `index.md`, `SCHEMA.md`, `AGENTS.md`; default raw:
`raw/**/*`, `workshop/*/raw/**/*`). `.llm-wiki.json` is accepted as a legacy filename.

## Schema

```json
{
  "formal": ["notes/**/*.md", "README.md"],
  "raw": ["sources/**/*"],
  "ignored_parts": [".git", ".obsidian", ".claude"]
}
```

- `formal`: root-relative glob patterns for searchable formal pages.
- `raw`: root-relative glob patterns for evidence files.
- `ignored_parts`: directory or file names excluded from both scopes.

Each list is optional. When present, it replaces that scope's defaults. Patterns must be relative
and must not contain `..`; this keeps discovery inside the resolved wiki root. The patterns may
include any file extension, while binary files are still skipped by text search as before.

## Example

For a wiki organized as `knowledge/` and `sources/`, use:

```json
{
  "formal": ["knowledge/**/*.md"],
  "raw": ["sources/**/*"]
}
```

No script changes are needed for downstream users; copy the file to the wiki root or pass its path
with `--config`. Search, page lookup, lint, source-map generation, and the validation wrapper use
the same layout. Governance files (`SCHEMA.md`, `AGENTS.md`, `index.md`, and `log.md`) remain at
the wiki root. The package includes a generic schema example at
`$SKILL_DIR/assets/examples.llm-wiki.json`.
