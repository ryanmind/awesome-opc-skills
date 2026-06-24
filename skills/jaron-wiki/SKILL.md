---
name: jaron-wiki
description: Search, verify, and maintain knowledge in ~/llm-wiki. Use when the user needs wiki-first retrieval, source checking, broken-link fixes, tag/index upkeep, or wiki maintenance without loading the entire knowledge base.
---

# Jaron Wiki
Use `~/llm-wiki` as the primary knowledge source for knowledge-related tasks.

## When to Use
- User asks a question that may be covered in the wiki
- User asks to search, retrieve, or verify wiki content
- User asks to create, update, or maintain wiki pages
- Fixing broken links, tags, index entries, or log entries
- Cross-referencing wiki claims against external sources

## When NOT to Use
- Pure coding, debugging, or system operations unrelated to wiki content
- The task is entirely covered by another active skill
- User explicitly asks to skip the wiki
- The question is purely conversational or trivial (no knowledge retrieval needed)
- Wiki content is known to be absent and the task doesn't involve creating it

## Setup
Before any wiki operation:
1. Read `~/llm-wiki/SCHEMA.md` — page format, frontmatter, tag taxonomy, page types, thresholds, update policy
2. Read `~/llm-wiki/index.md` — full page catalog and section structure
3. Read `~/llm-wiki/log.md` — recent changes
4. Follow all rules in `~/llm-wiki/SCHEMA.md` and `~/llm-wiki/AGENTS.md`

## Search
Search in the following order:
1. **Exact page title** — direct file lookup by slug (e.g. `ios-sdk-overview.md`)
2. **`~/llm-wiki/index.md` section lookup** — scan the section that matches the topic domain
3. **Tags** — grep frontmatter `tags:` for the relevant tag from `~/llm-wiki/SCHEMA.md` taxonomy
4. **Wikilinks** — grep `[[target-page]]` across `~/llm-wiki/` to find pages that reference a concept; also check the current page's outbound links for related pages
5. **Full-text search** — fallback when structured search yields nothing

Prefer the smallest relevant scope first. Stop as soon as sufficient pages are found — do not exhaust all layers.

## Retrieve
Read only the pages required for the current task.
Priority:
1. Exact-match pages
2. Entity pages (`type: entity`)
3. Concept pages (`type: concept`)
4. Query / Comparison / Summary pages
5. `~/llm-wiki/index.md` (as fallback navigation)

Stop expanding context once sufficient information is found. Never load the entire wiki into context.

## Verify
The wiki is not absolute truth.

### Check frontmatter signals
- `confidence: low` → treat as tentative, cross-check with external sources
- `confidence: medium` → use with moderate confidence
- `confidence: high` → use with high confidence
- `contested: true` + `contradictions:` → conflicting records exist, present all positions

### Resolve conflicts
If wiki content conflicts with:
- Current code
- Official documentation
- Official APIs
- Verifiable facts
- Current release information

Prefer the verifiable source. When two wiki pages or source docs conflict, do NOT overwrite — record both positions with `contested: true` and `contradictions: [other-page-slug]` per `~/llm-wiki/SCHEMA.md` update policy.

### Validation status (include in answer when relevant)
- **Verified** — confirmed against current external source
- **Partially verified** — some claims checked, others unverified
- **Unverified** — not yet cross-checked

## Answer
Prefer verified wiki content.
Preserve:
- Original terminology
- Valid `[[wikilinks]]`
- Important concept relationships

Qualify answers with validation status and confidence level when relevant.

If no relevant wiki content exists:
- State that no matching content was found
- Use general knowledge only as a supplement
- Do not fabricate pages, entities, or references

## Maintain
Update wiki content only when supported by verifiable evidence.
Examples:
- Incorrect content
- Missing content
- Broken links
- Broken references
- Incorrect tags
- Missing `~/llm-wiki/index.md` or `~/llm-wiki/log.md` entries
- Conflicts with verified sources

### Update rules (from `~/llm-wiki/SCHEMA.md`)
- Always bump `updated` date when editing a page
- Preserve `[[wikilinks]]`, tags, and references
- New tags must be added to the tag taxonomy in `~/llm-wiki/SCHEMA.md` first
- Record conflicts with `contested: true` and `contradictions:` — never silently overwrite
- Respect page thresholds: create new pages when a concept appears in 2+ source docs or is a top-level area; split when a page exceeds ~200 lines
- `~/llm-wiki/raw/` is immutable — reference source docs in place, never modify them

### Update infrastructure
After any page change:
- Update `~/llm-wiki/index.md` if a page was added, removed, or renamed
- Append to `~/llm-wiki/log.md` with reason, source, impact, and evidence

## Prohibited
Do not:
- Load the entire wiki into context
- Fabricate pages, entities, or references
- Remove valid `[[wikilinks]]`
- Overwrite content without verification
- Modify `~/llm-wiki/raw/` directory
- Create pages for passing mentions or isolated details
- Overwrite conflicting positions — use `contested: true` instead
