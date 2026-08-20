# Hermes Conventions

Verified against the official Hermes Agent docs on 2026-08-20. Load this reference before judging path, ownership, or format questions.

Sources:

- Prompt assembly: https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly
- Persistent memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- Context files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files
- Context references: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references
- Personality & SOUL.md: https://hermes-agent.nousresearch.com/docs/user-guide/features/personality
- LLM-friendly docs index: https://hermes-agent.nousresearch.com/docs/llms.txt

## Home layout (HERMES_HOME, default ~/.hermes)

- `SOUL.md` — global persona and standing behavior. Loaded only from the Hermes home, never from project directories. Seeded with a default if missing; injected verbatim after security scan and truncation.
- `memories/MEMORY.md` — agent's personal notes; hard limit 2,200 chars (~800 tokens).
- `memories/USER.md` — user profile; hard limit 1,375 chars (~500 tokens).
- `config.yaml` — model, providers, memory/skill write gates, platform hints, truncation caps.
- `skills/` — agent skills (SKILL.md packages; a skill may carry its own `references/`).
- `state.db` — FTS5 session storage backing `session_search`.
- `pending/` — staged memory and skill writes awaiting approval.

Neither a home-level `references/` directory nor a home-level `AGENTS.md` is part of the documented layout, and Hermes does not auto-load `AGENTS.md` from the home — project `AGENTS.md` is discovered from the working directory (git-root chain) only. "Context references" in Hermes means the CLI `@file:` / `@folder:` / `@url:` inline-injection feature, not a directory of markdown files.

### Personal home layout (observed on this machine)

A home may extend the documented layout with personal conventions, usually described in its own `README.md`:

- Home-level `AGENTS.md` — cross-project default execution rules. Not auto-loaded by Hermes; effective only where the rules are copied into a project context file. Review it as a target when present, but flag any rule that assumes global effect.
- Home-level `references/*.md` — on-demand methods and templates, read per task type.
- The home may itself be a git repository tracking only the managed files (`SOUL.md`, `AGENTS.md`, `skills/`, `bin/`), with runtime state (logs, sessions, caches, databases) gitignored. The staged-change review path (`git diff --cached`) applies there.

## Memory format

- Entries are separated by a `§` (U+00A7) delimiter on its own line; entries may be multiline.
- Both stores are injected as a frozen snapshot at session start. Mid-session writes persist to disk immediately but do not mutate the running prompt until the next session.
- A write that would exceed the char limit errors out — memory never auto-compacts; the agent must consolidate in the same turn.
- Exact duplicates are rejected. Content is security-scanned (injection/exfiltration patterns) before acceptance.
- Externally edited files that break the `§` format are detected as drift; the memory tool refuses to overwrite and saves a backup.

## Project context files

- Priority, first match wins: `.hermes.md` / `HERMES.md` (walks to git root) → `AGENTS.override.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules` / `.cursor/rules/*.mdc` (CWD only).
- `AGENTS.md` merges a chain from git root down to the working directory (deeper files take precedence). Outside a git repo only the working directory is checked — a file planted in `$HOME` or `/tmp` cannot leak into sessions.
- All context files are security-scanned (prompt injection) and head/tail-truncated at 70% head / 20% tail when over the cap (`context_file_max_chars` if set, otherwise dynamic with a 20,000-char floor).
- `SOUL.md` is loaded independently as the identity slot, always from the Hermes home.

## config.yaml keys worth cross-checking

- `memory.memory_enabled`, `memory.memory_char_limit` (default 2200), `memory.user_char_limit` (default 1375), `memory.write_approval`
- `skills.write_approval`
- `context_file_max_chars`
- `platform_hints`
