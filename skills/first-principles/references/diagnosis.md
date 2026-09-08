# Diagnosis Closure

Read this file only for diagnosis tasks.

## Close The Diagnosis

1. State the leading root-cause hypothesis, the proposed causal mechanism, and the evidence supporting it.
2. Name the nearest competing explanation and its mechanism.
3. Define a prediction unique to the leading mechanism, then an observation or experiment that distinguishes between them.
4. Specify the metric, success or failure threshold, owner when known, and review point.
5. State what each possible result would imply for the next action.

Do not call correlation a root cause. Prefer the cheapest test that can falsify the leading hypothesis.

## Calibration

- Acceptable: "Latency rose 40% in the same week traffic doubled — correlation, not yet a cause. Mechanism: connection pool saturation at 200 concurrent requests. Discriminating test: replay yesterday's peak against a pool raised to 500. If p95 returns to baseline, the pool was the cause; if not, the bottleneck is downstream." — states the mechanism and a test that can kill it.
- Not acceptable: "The database is probably overloaded; we should scale it." — asserts correlation as cause and commits to a fix before any test.

A diagnosis that no observation could falsify is a hypothesis with no mechanism attached. Return to step 3 of the core workflow.
