---
name: hermes-context-review
description: Review durable Hermes Agent context for conflicting rules, stale references, memory-format violations, unsafe instructions, and wasted context. Use when the user asks to review, audit, simplify, or validate SOUL.md, AGENTS.md, memories, references, or config.yaml for a Hermes agent.
---

# Hermes Context Review

Review Hermes's durable operating context. Focus on behavior, authority, and maintainability rather than prose polish. Base path, ownership, and limit checks on the verified Hermes conventions in [references/hermes-conventions.md](references/hermes-conventions.md); read that file before judging ownership or format questions.

## Resolve The Target

- Use the explicit Hermes home when supplied; otherwise use `$HERMES_HOME` or `~/.hermes`.
- Home-directory targets: `SOUL.md`, `AGENTS.md`, `memories/USER.md`, `memories/MEMORY.md`, `references/*.md`, and the relevant parts of `config.yaml`, each when present. Do not expose secrets.
- Project context targets: `AGENTS.md` and the other project context files (`AGENTS.override.md`, `.hermes.md`/`HERMES.md`, `CLAUDE.md`, `.cursorrules`) when the user supplies a project directory or asks for a project-context review.
- Confirm the resolved target contains at least one review target. Otherwise stop and report that no reviewable Hermes context was found; do not issue a verdict.
- For a staged-change or pre-commit review, use `git diff --cached --name-status` to identify added, modified, deleted, and renamed paths. Read added and modified files with `git show :<path>`, deleted files with `git show HEAD:<path>`, and both sides of a rename with their respective `HEAD:` and `:` revisions. The index, not unstaged files, is the source of truth.

## Review Procedure

1. Read each target completely and resolve its local paths, section references, skill names, and configuration claims.
2. Check ownership against Hermes semantics: global persona and standing behavior belong in `SOUL.md` (Hermes loads it only from the home), per-project instructions belong in the project `AGENTS.md`, compact user preferences and environment facts belong in memory, and on-demand methods and templates belong in `references/`. A home-level `AGENTS.md` is a personal cross-project default that Hermes does not auto-load from the home; flag rules there that assume global effect. Flag rules filed in the wrong layer.
3. Check for duplicate, conflicting, stale, unverifiable, overly broad, or unsafe instructions. Prefer one authoritative rule over parallel copies. Cross-check `config.yaml` claims against the files it governs.
4. Treat the memory format as a contract: one `§` delimiter line per entry boundary. Flag broken delimiters, stores at or over their character limits, and entries that duplicate SOUL.md or project context content.
5. Check context efficiency without deleting meaningful constraints: flag low-frequency detail that belongs in `references/`, an on-demand skill reference, or `session_search` instead of always-on context, and repeated wording that has no distinct behavioral effect. Oversized `SOUL.md`/`AGENTS.md` content is silently head/tail-truncated, so flag sections at risk of dropping out.

## Boundaries

- Work read-only. Do not edit files, stage, commit, change configuration, create schedules, or create cron jobs.
- Base findings on files and commands actually read. Mark external facts and unavailable targets as unverified.
- Do not report cosmetic wording preferences as findings.

## Report

Start with the overall conclusion. List evidence-backed findings by severity:

- **P0**: broken authority, security risk, invalid reference, or memory-format violation that can change Hermes behavior.
- **P1**: conflicting, stale, duplicated, or misplaced instruction with meaningful maintenance or context cost.
- **P2**: bounded clarity or compression improvement that does not alter behavior.

For every finding include the file and precise location, evidence, impact, and smallest correction. Report in the language of the user's request. State "Checked, no findings" for checked dimensions without findings (or the equivalent in the report language). Unless the review stopped because no target exists, end with exactly one line: `VERDICT: PASS`, `VERDICT: WARN`, or `VERDICT: BLOCK`. Use `BLOCK` only for P0 findings.
