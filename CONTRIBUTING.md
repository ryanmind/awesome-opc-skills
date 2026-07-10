# Contributing to Awesome OPC Skills

This repository follows the current Codex skill package model. Keep runtime packages small, deterministic, and free of duplicated user documentation.

## Repository Contract

Each skill lives at `skills/<skill-name>/`.

```text
skills/<skill-name>/
├── SKILL.md              # required: the only execution-instruction source
├── agents/
│   └── openai.yaml       # required by this repository: UI metadata
├── references/           # optional: material the agent reads on demand
├── scripts/              # optional: deterministic executable helpers
└── assets/               # optional: templates or files copied into outputs
```

Allowed top-level entries inside a skill package are exactly:

- `SKILL.md`
- `agents/`
- `references/`
- `scripts/`
- `assets/`

Do not add `README.md`, `README.zh-CN.md`, `SKILL.zh-CN.md`, `templates/`, `examples/`, `config/`, changelogs, installation guides, or quick-reference files inside a runtime skill package.

## File Responsibilities

### `SKILL.md`

- Use YAML frontmatter containing only `name` and `description`.
- Match `name` to the skill directory exactly.
- Use lowercase letters, digits, and hyphens only.
- Put all trigger conditions in `description` because it controls skill activation.
- Keep the body focused on instructions another agent needs to execute the task.
- Prefer imperative instructions and progressive disclosure.
- Keep detailed domain knowledge in `references/` instead of duplicating it.

### `agents/openai.yaml`

Provide:

```yaml
interface:
  display_name: "Human-facing name"
  short_description: "A 25-64 character UI description"
  default_prompt: "Use $skill-name to perform a concrete task."
```

Quote every string. The default prompt must explicitly mention `$skill-name`.

### `references/`

Store content the agent may need to read while executing:

- domain rules
- API or schema notes
- calibration examples
- detailed checklists
- reusable response structures

Link every reference directly from `SKILL.md`. Avoid nested reference chains.

### `scripts/`

Store deterministic helpers that prevent repeatedly rewriting the same code. Scripts must:

- avoid hardcoded credentials
- use redacted output for sensitive data
- provide a useful `--help` when they expose a CLI
- be executed during validation when practical

### `assets/`

Store files intended for output rather than agent context, such as document templates, starter files, or media. If the agent must read a Markdown file to make a decision, that file belongs in `references/`, not `assets/`.

## Human Documentation

User-facing guides belong outside runtime packages:

```text
docs/skills/<skill-name>.md
docs/skills/<skill-name>.zh-CN.md
```

Human guides are optional. They may explain installation, examples, or motivation, but must not define execution rules that differ from `SKILL.md`.

The root `README.md` and `README_zh-CN.md` are the skill catalog. Link runtime definitions directly to `skills/<skill-name>/SKILL.md` and optional guides to `docs/skills/`.

## Add a Skill

1. Initialize the package with the official skill creator:

   ```bash
   python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/init_skill.py" \
     <skill-name> \
     --path skills \
     --interface 'display_name=...' \
     --interface 'short_description=...' \
     --interface 'default_prompt=Use $<skill-name> to ...'
   ```

2. Replace every scaffold placeholder in `SKILL.md`.
3. Create only the resource directories the skill actually needs.
4. Add an optional human guide under `docs/skills/`, not inside the skill.
5. Add the skill to both root catalog files.
6. Add an entry under `CHANGELOG.md` → `Unreleased`.
7. Run validation.

## Validate

```bash
python3 scripts/validate_skills.py
```

When the official validator is available locally, also run:

```bash
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" \
  skills/<skill-name>
```

## Quality Bar

- The skill has a narrow, reusable responsibility.
- Trigger conditions are specific enough to avoid accidental activation.
- Instructions do not duplicate general model knowledge without a reason.
- Inputs, evidence boundaries, output contract, and stop conditions are explicit.
- No secret, proprietary configuration, generated artifact, or machine-local path is committed unless the path is the skill's intentional domain contract.
- Scripts and examples are tested in proportion to risk.
- Repository validation passes without warnings or ignored failures.

## Git

Use Conventional Commits unless repository tooling establishes a stricter rule:

```text
feat(skill-name): add capability
fix(skill-name): correct behavior
docs: update skill catalog
chore: maintain repository tooling
```

Do not add `Co-Authored-By`, `Signed-off-by`, or AI-contribution trailers.
