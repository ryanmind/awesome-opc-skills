# Evidence Discovery

Read this file only when the request refers to a project, repository, document, or artifact that can be located in the workspace.

## Goal

Find the minimum evidence that could change the conclusion without loading the whole workspace.

## Workflow

1. Translate the decision into at most 3 evidence questions, such as current behavior, binding constraints, baseline metrics, or existing ownership.
2. Locate likely files with low-output searches such as `rg --files` and targeted `rg` patterns.
3. Read definitions, direct references, tests, configuration, and decision documents relevant to those questions.
4. Stop searching when additional evidence is unlikely to change the conclusion.
5. Separate observed facts from interpretations and missing evidence.

Do not perform broad repository analysis merely because tools are available. Do not search for evidence unrelated to the user's decision surface.

## Evidence Boundary

- Continue with explicit assumptions when missing evidence does not block a reversible or low-cost decision.
- Stop and state the minimum missing evidence when the conclusion would otherwise authorize an irreversible or high-cost action.
