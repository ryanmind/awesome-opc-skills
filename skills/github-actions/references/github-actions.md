# GitHub Actions Reference

## Table of Contents

- Trigger routing
- Permissions and trust
- Orchestration
- State, Caching, and Idempotency
- Security guardrails
- Debugging and Diagnostics
- Validation checklist

## Trigger routing

- First confirm that the workflow file is on the default branch, especially for `schedule` events.
- `schedule` uses UTC, with a minimum interval of 5 minutes.
- When troubleshooting "not triggered" issues, check the `on:` event type first, then `branches`, `branches-ignore`, `paths`, `paths-ignore`, and `types`.
- `if:` conditions can appear on jobs and steps; many runs do not "fail" but are simply skipped by conditions.
- `workflow_dispatch`, `repository_dispatch`, and `workflow_call` have different inputs and trigger chains; do not mix their contexts.
- Events triggered by the repository's `GITHUB_TOKEN` generally will not trigger a new workflow run. Check this first for recursive chains or "no trigger after push" issues.

## Permissions and trust

- Default to minimal `permissions`; do not rely on vague default behaviors.
- Permissions like `contents: write`, `pull-requests: write`, `actions: write`, and `id-token: write` should be explicitly declared as needed.
- Fork PRs are untrusted by default. Do not assume secrets, write tokens, or deployment approvals are available.
- `pull_request` and `pull_request_target` have different trust boundaries. The latter is more dangerous; never expand permissions just to "make it run".
- When using environments, check if required reviewers, wait timers, or environment secrets are blocking the job.
- Reusable workflows do not automatically inherit what you might think they do; explicitly check inputs, secrets, permissions, and outputs.

## Orchestration

- First check if the `needs` chain is complete, then verify if job outputs are actually being written by upstream jobs.
- For `strategy.matrix`, troubleshoot `include`, `exclude`, `fail-fast`, conditional branches, and summary logic.
- `concurrency` is the primary mechanism for solving duplicate runs, releases, and notifications. Set a stable `group` for creation, release, and notification pipelines.
- Only enable `cancel-in-progress` when explicitly needed. Some deployment tasks are better queued sequentially and should not be canceled.
- When investigating reusable workflows, first align the input names, output names, and secret names between the caller and the callee.
- For composite action issues, prioritize checking input names, default shell, relative paths, and working directories.
- Explicitly verify runner differences: `ubuntu-latest`, `macos-latest`, and `windows-latest` may have different shells, paths, and toolchains.

## State, Caching, and Idempotency

- Caches have immutability: once generated for a specific key, they cannot be overwritten. Design a reasonable fallback strategy with `restore-keys`.
- Caches are only for acceleration. Do not treat old caches as the new source of truth. Pay attention to lockfile hashes when troubleshooting dependency or package manager cache invalidations.
- Artifacts are the output of a specific run. Do not treat old artifacts as inputs for the current run unless the pipeline is specifically designed that way.
- Checkpoints, cursors, deduplication keys, and last-release timestamps are frequent entry points for troubleshooting missed runs, reruns, and duplicate notifications.
- Release and notification pipelines must have idempotency keys. Relying merely on "this probably won't trigger twice" is unreliable.
- Uniformly verify time windows across UTC, local timezones, fetch window boundaries, daylight saving time (DST), and date rollovers.
- On failure reruns, confirm whether partial successes have already persisted side effects to avoid duplicate commits, releases, or pushes.

## Security guardrails

- Try to pin third-party actions to a commit SHA instead of a floating tag to prevent supply chain attacks.
- Do not write secrets, webhooks, tokens, or cloud credentials into the repository, build artifacts, or logs.
- For OIDC scenarios, check if `id-token: write`, the cloud provider's trust policy, and the audience configuration align correctly.
- Do not inflate a workflow to broad, high privileges just for a temporary fix.
- Use `pull_request_target`, self-hosted runners, and repository-level write tokens only when absolutely necessary.

## Debugging and Diagnostics

- **Enable Detailed Logs**: You can obtain low-level execution fingerprints by setting `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true` in Repository Variables or Secrets.
- **Local Reproduction**: Suggest or attempt using [nektos/act](https://github.com/nektos/act) for minimal local containerized reproduction to avoid frequent commits for debugging.
- **SSH Debugging**: You can inject a breakpoint using actions like `mxschmitt/action-tmate` or `tailscale/github-action` to drop into the runner environment to troubleshoot.

## Validation checklist

- First, static checks: YAML, expressions, inputs/outputs, `needs`, `if:`, and indentation.
- Next, minimal validation: Run only the modified script, minimal job, or minimal matrix branch.
- Then, pipeline validation: Cover empty inputs, partial successes, failure reruns, cache hits/misses, and deduplication of releases or notifications.
- For `schedule`, provide the exact time mapping between UTC and the business timezone. Do not just write "every morning".
- For permissions or secrets, explicitly state the dependency on repository settings, environment settings, and fork behavior.
