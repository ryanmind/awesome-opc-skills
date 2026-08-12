# Search And Retrieve

Use this reference for read-only lookup and wiki-backed answers.

## Workflow

1. Search with the script before opening files:

   ```bash
   python3 "$SKILL_DIR/scripts/wiki_search.py" --query "<query>" --scope formal --limit 8 --json
   ```

2. Prefer results in this order:
   - exact slug or title
   - `index.md` catalog match
   - tag or type match
   - wikilink inbound/outbound match
   - full-text match
3. Read only the smallest sufficient pages:

   ```bash
   python3 "$SKILL_DIR/scripts/wiki_page.py" "<slug-or-path>" --max-chars 12000 --json
   ```

4. Expand through backlinks or outbound links only when the current page is insufficient.
5. Stop searching once there is enough evidence to answer the user's question.

## Scope

- `--scope formal`: search formal wiki pages only. Use for most answers.
- `--scope raw`: search raw evidence only. Use when formal pages are missing or the user asks for source material.
- `--scope all`: search formal and raw areas. Use sparingly; ranking does not guarantee that formal results precede raw results.

By default, formal pages include `domains/**`, `entities/**`, `workshop/*/README.md`, `_meta/topic-map.md`, `index.md`, `SCHEMA.md`, and `AGENTS.md`. A custom `llm-wiki.json` replaces these defaults with its own `formal` globs.

Raw scope covers UTF-8 text files under `raw/**` and `workshop/*/raw/**`. Binary files such as PDF, XLSX, and XMind are excluded from search; direct reads return an unsupported-content error and require a file-specific tool.

Search JSON reports the number of excluded files in `skipped_unsupported`.

## Retrieval Discipline

- Do not open `log.md` for normal answers unless recency or maintenance history matters.
- Do not read `SCHEMA.md` for simple retrieval; scripts expose enough metadata for lookup.
- When formal evidence should take priority, search `--scope formal` first and fall back to `--scope raw`; do not depend on `--scope all` ordering.
- Keep result limits small, then rerun with a narrower query if needed.
- If script results are ambiguous, use titles, tags, type, confidence, and snippets to choose the next page.

## Answer Shape

Answer from the retrieved pages first. Preserve important terms and `[[wikilinks]]` when they carry relationship meaning. Mention source page slugs when useful for traceability.
