---
name: github-actions
description: "Diagnose and fix GitHub Actions, CI/CD, cron, and repository automation issues. Use for workflows/jobs/steps that are un-triggered, skipped, failed, duplicated, or for issues involving filters, if-conditions, permissions, secrets, runners, caches, artifacts, matrices, workflow_call, concurrency, and release/notification idempotency."
---

# GitHub Actions Pipeline

## Objectives

- Verify the GitHub Actions orchestration first, then drill down into scripts and business code.
- Fix issues at the source of the failure, avoiding cross-layer patches.
- Keep modifications minimal, reproducible, and verifiable.

## Core Rules

- Do not directly modify generated paths like `reports/`, `output/`, or `build/`.
- Do not hardcode branches, paths, time windows, thresholds, or release targets in the code.
- Prefer passing critical inputs via workflow inputs, environment variables, configuration files, or job outputs.
- Always check for idempotency to avoid duplicate creations, syncs, releases, or notifications.
- Default to minimal `permissions`; explicitly declare write permissions only when necessary.
- Prefer pinning third-party actions to a commit SHA rather than floating tags.

## Mandatory Workflow

**When taking on any GitHub Actions troubleshooting task, you MUST strictly follow this sequence. It is absolutely forbidden to modify the underlying scripts first:**

1. **Review Orchestration**: First read `.github/workflows/` and the workflow call chain. Confirm `on:`, filters, `if:`, `needs`, `permissions`, and `concurrency`.
2. **Follow the Execution Path**: Only expand your reading along the execution chain to called scripts, configuration sources, cache/artifact/checkpoints, and release/notification scripts.
3. **Orchestration First**: Fix workflow orchestration and configuration issues first; **only after confirming the orchestration is completely correct** should you modify scripts or business code.
4. **Step-by-step Validation**: Verify from bottom up: `function -> script -> job -> workflow`. Start with minimal reproduction, then expand the scope.

## Reading Guidelines

- When encountering detailed GitHub Actions issues, read `references/github-actions.md`.
- Prioritize reading the sections directly related to the current failure; do not read the entire document unless necessary.
- Focus on: Trigger routing, `permissions`, `GITHUB_TOKEN`, fork PRs, `workflow_call`, `matrix`, `concurrency`, cache/artifacts, and scheduled task timezones.
- To reference standardized code structures, check the examples in the `examples/` directory (if applicable).

## Validation Requirements

- First, perform static checks: YAML structure, inputs/outputs names, `needs` chains, expressions, and indentation.
- Enable diagnostic logs: For complex issues, prompt the user to enable `ACTIONS_STEP_DEBUG=true` or perform local debugging (e.g., `nektos/act`).
- Next, perform minimal validation: Run only the modified script or the smallest job.
- Then, perform pipeline validation: Cover empty inputs, partial successes, failure reruns, cache hits/misses, and deduplication of releases or notifications.
- For scheduled tasks, explicitly verify the UTC timezone against the target business timezone.
- For releases or notifications, ensure that repeated triggers do not cause duplicate side effects.
