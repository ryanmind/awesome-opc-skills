# Repository Architecture

## Goal

Keep agent runtime instructions minimal while preserving useful human-facing documentation and enforcing one repository-wide package contract.

## Layers

```text
awesome-opc-skills/
├── skills/                 # runtime packages consumed by agents
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/     # optional, read on demand
│       ├── scripts/        # optional, executable helpers
│       └── assets/         # optional, output resources
├── docs/
│   ├── architecture.md     # repository contract and ownership
│   └── skills/             # optional human-facing guides
├── scripts/
│   └── validate_skills.py  # structural and metadata enforcement
├── .github/workflows/      # continuous validation
├── README.md               # English catalog
├── README_zh-CN.md         # Chinese catalog
├── CONTRIBUTING.md         # contribution workflow
└── CHANGELOG.md            # release-facing change record
```

## Ownership

| Layer | Audience | Responsibility | Source of truth |
| --- | --- | --- | --- |
| `skills/*/SKILL.md` | Agent | Trigger and execution instructions | Yes |
| `skills/*/agents/openai.yaml` | Product UI | Display metadata and default invocation | Yes for UI metadata |
| `skills/*/references/` | Agent | Detailed knowledge loaded only when needed | Yes for referenced detail |
| `skills/*/scripts/` | Agent/runtime | Deterministic repeated operations | Yes for script behavior |
| `skills/*/assets/` | Generated output | Templates and files copied or transformed | Yes for asset content |
| `docs/skills/` | Human | Installation, motivation, examples | No execution rules |
| Root README files | Human | Catalog and discovery | No execution rules |

## Boundary Rules

1. A runtime package contains only files needed to execute the skill.
2. `SKILL.md` is the only top-level instruction document in a package.
3. Human documentation never overrides or duplicates execution rules.
4. Markdown that an agent must read belongs in `references/`; Markdown copied into output belongs in `assets/`.
5. Every skill has `agents/openai.yaml` in this repository, even though upstream treats it as recommended, so catalog behavior stays consistent.
6. Generated files and operating-system metadata are never repository content.
7. Validation converts these rules from convention into an enforced contract.

## Change Flow

```text
Search existing skill
  -> define trigger and responsibility
  -> initialize package
  -> write SKILL.md
  -> add only necessary resources
  -> update catalog/changelog
  -> validate locally
  -> CI validates again
```

## Non-Goals

- Maintaining separate translated `SKILL.md` files
- Requiring a README inside every runtime package
- Supporting arbitrary top-level package folders
- Keeping duplicated instructions for different agent products
- Treating repository marketing copy as execution policy
