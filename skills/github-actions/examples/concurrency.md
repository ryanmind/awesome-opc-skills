# Concurrency Examples

`concurrency` controls the concurrent execution behavior of a group of workflows or jobs. It prevents multiple workflow runs from modifying shared state simultaneously.

## 1. Auto-cancel Old Builds (Cancel in Progress)

This is the most common pattern used in Pull Requests (PRs). When a developer continuously pushes new code to the same PR, it cancels previous builds that are still queued or running, saving runner resources.

```yaml
concurrency:
  # Group by workflow name plus PR number or branch name
  group: ${{ github.workflow }}-${{ github.ref }}
  # Cancel in-progress runs for the same group
  cancel-in-progress: true
```

## 2. Serial Deployment (Queueing)

When deploying to a Production or Staging environment, you must never execute two deployment tasks simultaneously, as this leads to resource race conditions or state conflicts. In this case, **do not** enable `cancel-in-progress`.

```yaml
concurrency:
  # Fix the group to the environment name to ensure only one deployment process exists per environment
  group: production-deploy
  # Do not use cancel-in-progress; this ensures subsequent triggers will queue (Pending)
  cancel-in-progress: false
```
