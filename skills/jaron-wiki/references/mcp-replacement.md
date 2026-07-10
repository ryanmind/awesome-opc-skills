# MCP Replacement

Use this reference when replacing old `llm-wiki-mcp` workflows with local skill resources.

## Compatibility Boundary

These are workflow substitutes, not MCP API-compatible implementations. The scripts do not preserve the MCP request/response envelope, `next_action`, semantic or hybrid search modes, or guaranteed formal-first ordering for combined scopes. Use `--scope formal` first and fall back to raw search when formal evidence is insufficient.

## Local Tool Mapping

| MCP-style operation | Local workflow substitute |
| --- | --- |
| `search_wiki` | `scripts/wiki_search.py --scope formal --json` |
| `read_page` | `scripts/wiki_page.py <slug> --json` |
| `read_raw_source` | `scripts/wiki_page.py <raw-path> --scope raw --json` |
| `find_related_pages` | `wiki_search.py` plus `wiki_page.py --with-backlinks` |
| `find_referencing_pages` | `wiki_search.py --source <path> --json` |
| `run_lint` | `scripts/wiki_validate.py --json` |
| `create_formal_page_candidate` | Agent workflow in `create-or-update.md` |
| `update_index_candidate` | Agent workflow in `create-or-update.md` |
| `create_log_candidate` | Agent workflow in `create-or-update.md` |

## Token-Saving Strategy

- Put deterministic discovery in scripts.
- Return compact JSON with metadata and snippets instead of whole files.
- Read full pages only after search narrows candidates.
- Load governance references only for writes and maintenance.
- Keep `SCHEMA.md`, `AGENTS.md`, `index.md`, and `log.md` out of routine retrieval unless the active task needs them.

## Remaining Gaps

The skill does not provide MCP-compatible semantic or hybrid search, response envelopes, or action hints. It also lacks safe write APIs equivalent to atomic raw creation, locked log append, formal page candidate rendering, and source-map acceptance. Keep write operations candidate-first and use wiki-native scripts for source-map updates until local helpers implement the same safety boundaries.
