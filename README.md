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

The manager creates only configured links, updates links after the configured source path changes, removes deselected managed links, rejects duplicates, and never overwrites unmanaged files, directories, or links.

## Validate

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
PYTHONPYCACHEPREFIX=/tmp/agent-skills-pycache python3 -m compileall -q scripts tests skills
```

## Skills

- [ai-coding-workflow](skills/ai-coding-workflow/SKILL.md)
- [codebase-analysis](skills/codebase-analysis/SKILL.md)
- [design-convergence-review](skills/design-convergence-review/SKILL.md)
- [first-principles](skills/first-principles/SKILL.md)
- [git-commit](skills/git-commit/SKILL.md)
- [jaron-wiki](skills/jaron-wiki/SKILL.md)

Human-facing project documentation is maintained in `~/llm-wiki/workshop/agent-skills/raw/` and exposed through the repository `docs` symbolic link.

## License

MIT
