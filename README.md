# Agent Skills

One repository for the agent skills you maintain, shared with Codex, Claude, Hermes, and Zcode through symbolic links.

[简体中文](README_zh-CN.md)

## What

`skills/` is the source of truth. Each skill is a self-contained package with a `SKILL.md` entry point and optional references, scripts, and assets.

## Why

Maintain a skill once and make the same version available to every configured agent. The link manager keeps distribution predictable and protects files it does not manage.

## How

1. Add or update a skill in `skills/`.
2. Select the target agents and skills in `config/skill-links.toml`.
3. Review the proposed changes:

   ```bash
   python3 scripts/manage_skill_links.py sync --dry-run
   ```

4. Apply them:

   ```bash
   python3 scripts/manage_skill_links.py sync
   ```

Use `status` to see current links and `check` to validate the configuration. `sync` changes only configured destinations and refuses to overwrite unmanaged files.

## Skills

| Skill | What it does |
| --- | --- |
| [design-convergence-review](skills/design-convergence-review/SKILL.md) | Checks whether a design is ready for implementation and identifies unresolved blockers. |
| [first-principles](skills/first-principles/SKILL.md) | Rebuilds a decision or diagnosis from evidence, constraints, and testable assumptions. |
| [git-commit](skills/git-commit/SKILL.md) | Drafts repository-aware Conventional Commit messages or commits staged changes. |
| [hermes-context-review](skills/hermes-context-review/SKILL.md) | Audits Hermes context for conflicting, stale, unsafe, or wasteful instructions. |
| [llm-wiki](skills/llm-wiki/SKILL.md) | Searches, verifies, and maintains a local Markdown wiki when explicitly invoked. |

User guides are optional and live outside the runtime packages, in `docs/skills/`. That directory is
a symlink into the llm-wiki workshop, so it is not version-controlled here. Only
[design-convergence-review](docs/skills/design-convergence-review.md) ships a guide today.

## Verify

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

## License

MIT
