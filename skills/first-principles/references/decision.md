# Decision Closure

Read this file only for decision tasks.

## Close The Decision

1. State the chosen option and the decisive constraint or trade-off.
2. Name the strongest rejected alternative and why it loses under the stated goal.
3. State what to stop, start, or double down on only when those categories fit.
4. Define the smallest next action or validation step.
5. For execution, specify the known owner, deadline, evidence to collect, success or failure threshold, and review point. Mark unknown fields instead of inventing them.
6. Define the reversal or exit condition.
7. At review, choose explicitly: continue, stop, change direction, or redo the analysis.

For irreversible decisions, prefer a reversible test or staged commitment when it can answer the same uncertainty.

## Calibration

- Acceptable: "Adopt Postgres, not DynamoDB: the workload is ad-hoc joins across three tables, so query flexibility is the decisive constraint and write throughput is not binding. Test: load 1M rows and run the three reporting queries; abandon if p95 exceeds 2s." — names the binding constraint, the rejected alternative, and the exit condition.
- Not acceptable: "Both databases have trade-offs; choose based on your needs." — no goal, no constraint, no decision.

A conclusion that cannot name the constraint it turns on has not been rebuilt from first principles; it is a restatement. Return to step 3 of the core workflow.

