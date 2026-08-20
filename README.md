# Agent Skills

Single source of truth for self-maintained agent skills, with configurable symbolic-link distribution to Codex, Claude, and Hermes.

[简体中文](README_zh-CN.md)

## Structure

```text
agent-skills/
├── skills/                  # Canonical runtime packages
├── config/skill-links.toml  # Source path, targets, and selected skills
├── scripts/                 # Validation and link reconciliation
├── tests/                   # Filesystem behavior tests
└── docs -> ~/llm-wiki/workshop/agent-skills/raw
```

Each runtime package follows this contract:

```text
skills/<skill-name>/
├── SKILL.md
├── agents/openai.yaml
├── references/   # optional, loaded on demand
├── scripts/      # optional, deterministic helpers
└── assets/       # optional, output resources
```

## Manage Links

Edit `config/skill-links.toml`, then run:

```bash
python3 scripts/manage_skill_links.py status
python3 scripts/manage_skill_links.py check
python3 scripts/manage_skill_links.py sync --dry-run
python3 scripts/manage_skill_links.py sync
```

The manager creates and verifies only the links listed in configuration, leaves deselected links untouched, replaces existing directories or symlinks at configured destinations, rejects duplicates, and never overwrites unmanaged files.

## LLM Wiki Layout

The `llm-wiki` skill reads `<wiki-root>/llm-wiki.json` to discover formal pages and raw sources. Without this file, it uses the built-in `domains/`, `entities/`, `workshop/`, and `raw/` layout.

The bundled [examples.llm-wiki.json](skills/llm-wiki/assets/examples.llm-wiki.json) demonstrates the schema; copy and adapt it at the wiki root:

```json
{
  "formal": [
    "notes/**/*.md",
    "README.md"
  ],
  "raw": ["sources/**/*"],
  "ignored_parts": [".git", ".obsidian", ".claude"]
}
```

Search, page lookup, lint, source-map generation, and validation use the same layout. `SCHEMA.md`, `AGENTS.md`, `index.md`, and `log.md` remain at the wiki root. Use `--config <path>` or `LLM_WIKI_CONFIG` when the configuration is stored elsewhere.

## Validate

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
PYTHONPYCACHEPREFIX="${TMPDIR:-/tmp}/agent-skills-pycache" python3 -m compileall -q scripts tests skills
```

## Skills

- [design-convergence-review](skills/design-convergence-review/SKILL.md)
- [first-principles](skills/first-principles/SKILL.md)
- [git-commit](skills/git-commit/SKILL.md)
- [hermes-context-review](skills/hermes-context-review/SKILL.md)
- [llm-wiki](skills/llm-wiki/SKILL.md)

Human-facing project documentation is maintained in `~/llm-wiki/workshop/agent-skills/raw/` and exposed through the repository `docs` symbolic link.

## License

MIT
