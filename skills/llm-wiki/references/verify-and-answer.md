# Verify And Answer

Use this reference when wiki-backed claims need confidence handling, conflict handling, or current-source verification.

## Confidence Signals

Read frontmatter before relying on a page:

- `confidence: high`: use with high confidence unless current evidence conflicts.
- `confidence: medium`: use with moderate confidence and avoid overstating.
- `confidence: low`: treat as tentative and verify before presenting as fact.
- `contested: true`: inspect `contradictions:` and present competing positions.

## Verification Priority

Prefer the most verifiable current source:

1. Current project code or local source repository named by the wiki.
2. Official documentation, API references, release notes, or standards.
3. Raw source documents referenced by `sources:`.
4. Formal wiki synthesis.

When a wiki claim depends on a source that may change over time (API behavior, version-specific features, live documentation, current events), verify it against the current live source before answering.

## Conflict Policy

- Do not silently overwrite conflicting wiki content.
- If two wiki pages or source documents conflict, preserve both positions and mark the unresolved state in any proposed update.
- If verified current evidence contradicts the wiki, answer with the verified evidence and flag the wiki mismatch.
- Use `contested: true` and `contradictions: [...]` for unresolved wiki updates.

## Validation Labels

Use these labels when the answer depends on verification:

- `Verified`: checked against current code, official docs, or cited source.
- `Partially verified`: the core claim was checked but supporting details were not fully verified.
- `Unverified`: retrieved from wiki without independent checking.

Do not label a claim `Verified` merely because it appears in the wiki.
