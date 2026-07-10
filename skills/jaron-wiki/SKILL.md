---
name: jaron-wiki
description: "Token-efficient search, retrieval, verification, and maintenance for the local Markdown wiki at ~/llm-wiki. Use for wiki-first answers, llm-wiki lookup, source checking, formal-page creation or update candidates, broken link/tag/index/log upkeep, and local replacement of llm-wiki-mcp retrieval workflows."
---

# Jaron Wiki

Use `~/llm-wiki` as the primary knowledge source when the user asks for knowledge that may already be captured there.

Recommended future package name: `local-wiki`. Keep `jaron-wiki` until callers, symlink config, docs catalogs, and prompts are migrated together.

## Core Rules

- Do not load the whole wiki into context.
- Prefer scripts for search, page lookup, metadata extraction, backlinks, and lint wrappers.
- Read detailed references only for the active intent.
- Treat wiki content as evidence, not absolute truth.
- Preserve `[[wikilinks]]`, tags, sources, confidence, and contradiction metadata unless a verified update requires a change.
- Never modify paths outside the resolved wiki root.
- Do not fabricate pages, sources, references, or validation status.

## Wiki Root

Resolve the root in this order:

1. A path explicitly provided by the user
2. `$LLM_WIKI_ROOT`
3. `~/llm-wiki`

Use `--root <path>` on scripts when the wiki root is not `~/llm-wiki`.

## Intent Routing

- Search or answer from existing wiki content: read [search-and-retrieve.md](references/search-and-retrieve.md).
- Verify claims, handle low confidence, or resolve conflicts: read [verify-and-answer.md](references/verify-and-answer.md).
- Create, update, rename, or delete formal pages, raw sources, `index.md`, `log.md`, `SCHEMA.md`, or `_meta/topic-map.md`: read [create-or-update.md](references/create-or-update.md).
- Run health checks, broken-link checks, source-map checks, or periodic cleanup: read [maintenance.md](references/maintenance.md).
- Replace or emulate an old `llm-wiki-mcp` operation locally: read [mcp-replacement.md](references/mcp-replacement.md).

Only read the references needed for the current intent.

## Script First

Use these helpers before opening large wiki files:

```bash
python3 skills/jaron-wiki/scripts/wiki_search.py --query "agent runtime" --limit 8 --json
python3 skills/jaron-wiki/scripts/wiki_page.py domains/agent/concepts/agent-runtime --max-chars 12000 --json
python3 skills/jaron-wiki/scripts/wiki_validate.py --json
```

The scripts return compact JSON by default when `--json` is passed. Use narrow `--limit`, `--scope`, and `--max-chars` values to keep context small.

## Safety Boundary

- Retrieval is read-only and may use scripts without reading `SCHEMA.md`, `AGENTS.md`, `index.md`, and `log.md` first.
- Any write or maintenance decision must load the specific reference above and then read the required wiki governance files named there.
- All wiki writes, including formal pages, raw sources, governance files, and generated metadata, should be candidate-first unless the user clearly asks to apply the change.
- `raw/` and `workshop/*/raw/` are evidence-preserving source areas. Existing raw source edits require explicit traceability, log handling, and the source-map closure defined in `create-or-update.md`.

## Output

For answers from wiki content, report the validation status when it matters:

- `Verified`: confirmed against current source, code, or official docs.
- `Partially verified`: some claims checked, others remain unchecked.
- `Unverified`: wiki content was used without external/current verification.

When no relevant wiki content is found, say so and distinguish any general knowledge from wiki-backed content.
