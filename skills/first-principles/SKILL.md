---
name: first-principles
description: First-principles reasoning for strategy, product, engineering, and organizational decisions. Use when asked to rebuild from zero, separate real constraints from inherited assumptions, make hard tradeoffs, apply brutal clarity, diagnose a root cause, or find leverage and 10x opportunities. Do not use for emotional support, neutral editing, or low-stakes brainstorming.
---

# First Principles

Reduce a complex problem to its goal, facts, real constraints, and falsifiable assumptions. Rebuild the simplest viable approach from those foundations, then close the loop with a decision or test.

## Task Modes

Classify the task before analysis:

- **Decision**: choose, stop, continue, or allocate resources.
- **Diagnosis**: identify and test the root cause.
- **Communication**: derive and express the core claim without changing the underlying decision.

## Core Workflow

1. **Define the decision surface**
   - State the goal, primary success metric, guardrails, and time window.
   - State the task mode, reversibility, and cost of being wrong.
2. **Establish the information state**
   - Separate facts, assumptions, inferences, and unknowns.
   - When the request refers to a project, repository, document, or artifact that can be located in the workspace, read [evidence-discovery.md](references/evidence-discovery.md) before asking questions.
   - Otherwise use the evidence supplied by the user and label unsupported assumptions and unknowns.
   - Ask at most 3 questions, and only when an answer could change the conclusion.
   - Continue with explicit assumptions for reversible or low-cost decisions. Require evidence before irreversible or high-cost commitments.
3. **Separate real constraints from inherited assumptions**
   - Identify non-negotiable physical, technical, economic, legal, resource, and time constraints.
   - Classify apparent constraints as fact, derived constraint, assumption, convention, analogy, or preference.
   - Treat unsupported assumptions and conventions as removable; do not ignore real-world constraints.
   - Identify the bottleneck and the assumption whose failure would invalidate the plan.
4. **Rebuild from zero**
   - Derive the simplest viable approach from the goal, facts, and real constraints without copying the current plan.
   - Compare it with the current plan and name the inherited assumptions that explain the difference.
   - Generate alternatives only when they materially change value, cost, risk, speed, or reversibility.
   - Look for nonlinear or 10x leverage when the goal requires a breakthrough; accept a smaller move when it is the highest-value feasible action.
   - In communication mode, rebuild the message structure without reopening the accepted decision. If the claim is unsupported or contradicted by evidence, reclassify the task as decision -> communication.
5. **Converge**
   - State the conclusion first and the strongest reason it could be wrong.
   - Load the primary task guide: [decision.md](references/decision.md), [diagnosis.md](references/diagnosis.md), or [communication.md](references/communication.md).
   - If the request explicitly spans two stages, load one additional guide only when needed. Use the order diagnosis -> decision -> communication; never load more than two guides.
   - End with a decision or the smallest test that can resolve the decisive uncertainty.

## Default Output

- Conclusion: one-sentence judgment.
- Facts / Assumptions / Unknowns: only decisive items.
- Real constraints / Inherited assumptions: what must remain and what can be removed.
- Rebuilt approach: what follows when starting from zero.
- Leverage judgment: whether a nonlinear opportunity exists or a smaller move is more rational.
- Main failure condition: the evidence or assumption most likely to overturn the conclusion.
- Decision or next test: use the selected task guide.

## Tone And Safety

- Be direct, concise, and evidence-grounded; do not use humiliation, pressure theatrics, or personal judgment.
- Do not present guesses as facts, consensus as proof, process as results, or incremental work as disruption.
- Do not invent owners, deadlines, metrics, or evidence.
- Do not let `10x`, brutal clarity, or starting from zero become excuses to ignore feasibility, safety, or irreversible downside.
- Remove optional sections that do not help the user decide or act.
