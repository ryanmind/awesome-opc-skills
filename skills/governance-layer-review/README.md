# Governance Layer Review

A reusable skill for reviewing governance-oriented layer systems.

It helps you check whether a layered governance setup stays clear over time:

- Are responsibilities assigned to the right layer?
- Are rules, preferences, methods, templates, and assets kept separate?
- Is the system drifting, duplicating itself, or becoming harder to maintain?
- Do layer names still match what the files actually do?

## What this is for

Use this skill when you need to review a governance-style layered system rather than a runtime software architecture.

Typical use cases:

- reviewing a layer model after a refactor or rename
- checking whether identity, rules, preferences, methods, and templates are mixed together
- finding duplicate ownership across files
- spotting naming mismatch and long-term drift
- preparing a governance design for public sharing or long-term maintenance

## What this is not for

This skill is not primarily for:

- controller / service / repository layering
- runtime system decomposition
- domain-driven design boundaries
- org-chart or permission-model audits

## What the skill reviews

By default, the skill works well with these layers:

- **Identity** — who the actor is
- **Rules** — what standards and constraints apply
- **Preferences** — what a user or team consistently cares about
- **Methods** — how a class of tasks should be executed
- **Templates** — reusable structures and checklists
- **Assets** — reusable examples, references, and materials

You can also adapt it to other governance-oriented layer models.

## What good output looks like

A useful review should:

- map each file or directory to a layer
- distinguish declared responsibility from actual responsibility
- identify cross-layer mixing and duplicated ownership
- explain the judgment with concrete evidence
- recommend the smallest set of changes needed to restore clean boundaries

## Repository structure

```text
.
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── agents/openai.yaml
├── references/
│   ├── standard.md
│   ├── failure-modes.md
│   └── example.md
└── templates/
    └── review-report.md
```

## Included files

- `SKILL.md` — the skill definition and execution workflow
- `agents/openai.yaml` — display metadata for skill UIs
- `references/standard.md` — evaluation standard and review rules
- `references/failure-modes.md` — common failure patterns
- `references/example.md` — minimal examples for calibration
- `templates/review-report.md` — structured report template

## Example prompt

```text
Use governance-layer-review to inspect this governance-layer system for mixed responsibilities, duplicated rules, naming mismatch, and long-term drift.
```

## When to use this repository

This repository is a good fit if you want a focused, reusable review skill for governance layer design rather than a large general-purpose framework.
