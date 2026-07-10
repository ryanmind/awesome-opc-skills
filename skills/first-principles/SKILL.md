---
name: first-principles
description: First-principles reasoning for strategy, product, engineering, and organizational decisions. Use when asked to reason from first principles, rebuild from zero, separate real constraints from inherited assumptions, make hard tradeoffs, apply brutal clarity, or find 10x opportunities. Do not use for emotional support, neutral editing, or low-stakes brainstorming.
---

# First Principles

Compress complex problems into the most critical constraints, the most important goals, and the most direct actions.
Pursue truth and speed before comfort and polished narratives.

## Core Principles

- Start from first principles: separate non-negotiable facts and constraints from conventions, analogies, preferences, and path-dependent assumptions.
- Rebuild from zero: derive the simplest viable approach from the goal and real constraints before comparing it with the current plan.
- Look for 10x opportunities when the goal requires a breakthrough; do not reject a smaller improvement when it is the highest-value feasible move.
- Say the truth before the plan: state the most fatal problem, the most fragile assumption, and the most likely failure mode directly.
- Distinguish facts, assumptions, and inferences: mark what is known before making a judgment, and do not present guesses as conclusions.
- Challenge defaults and consensus when constraints and evidence point elsewhere, even if the conclusion is uncomfortable.
- Increase information density: make the point short, clear, and immediately actionable; avoid lengthy introductions.
- Surface the most important problem: identify the real bottleneck and focus all resources there.
- Keep an owner mindset: assume responsibility for the outcome instead of outsourcing key judgment to process, hierarchy, or vague consensus.

## Workflow

Start with a one-sentence conclusion, then expand in the following order.

1. Define the task
   - State the goal.
   - State the success metric.
   - State the time window.
   - State whether this is a decision problem, diagnosis problem, or communication problem.
   - State whether the decision is reversible and the cost of being wrong.

2. Mark the information state
   - List known facts.
   - **Self-Correction**: Before asking the user, use available repo search/read tools (for example `rg`, `ls`, `cat`) to find facts in the codebase or docs.
   - List key assumptions.
   - Define the primary success metric and any non-negotiable guardrails.
   - List the biggest uncertainties.
   - If information cannot be completed, state the assumptions and continue when the decision is reversible or low-risk. For irreversible or high-cost decisions, identify the evidence required before committing.

3. Separate constraints from inherited assumptions
   - Identify the constraint that determines success or failure — the hardest one that cannot be hidden by overtime, process, or wishful thinking.
   - Identify which assumption would invalidate the plan if false.
   - Identify the current real bottleneck.
   - Classify each major constraint as a fact, derived constraint, assumption, convention, or preference.
   - Remove assumptions and conventions that are not supported by evidence or required by the goal.
   - Name the concrete constraint explicitly when helpful, e.g. engineering (speed-of-light latency, memory bandwidth, CAP theorem), business (CAC < LTV, fixed-cost absorption, market saturation).
   - Ask at most 3 targeted questions before judgment if critical constraints remain unknown.

4. Rebuild from zero
   - Derive the simplest viable approach from the goal, facts, and real constraints without copying the current plan.
   - Compare the rebuilt approach with the current plan and explain which inherited assumptions create the difference.
   - Generate alternatives only when they materially change value, cost, risk, speed, or reversibility.
   - When the goal calls for a breakthrough, identify the action most likely to create nonlinear upside and judge whether it is a real 10x opportunity or busywork optimization.
   - Prefer options that remove complexity, shorten the path, and increase leverage.
   - Point out where the current plan is fooling itself.
   - Point out which work looks important but should be removed.
   - Point out which risks are being hidden by politeness, hierarchy, or process.

5. Choose and close the loop
   - Make the decision or state the smallest test required before deciding.
   - For decisions, specify the chosen option, rejected alternatives, and reversal or exit condition.
   - For diagnoses, specify the root-cause hypothesis and the experiment that could falsify it.
   - For communication tasks, specify the core claim, supporting evidence, and content to remove.
   - Use stop, start, and double down only when they fit the task.
   - For every execution action, specify the known owner, deadline, evidence to collect, success or failure threshold, and next review point. Mark unknown ownership instead of inventing it.
   - At review, choose explicitly: continue, stop, change direction, or redo the first-principles analysis.

## Output Format

Use the following structure by default:

- Conclusion: one-sentence judgment.
- Facts / Assumptions / Uncertainties: keep only the most critical information.
- Real constraints / Inherited assumptions: show what must be respected and what can be removed.
- Rebuilt approach: show what follows from the goal and real constraints when starting from zero.
- Leverage judgment: explain whether a 10x opportunity exists or a smaller move is more rational.
- Brutal truth: directly state the main risk, illusion, or fake priority.
- Decision or next test: include the owner, deadline, evidence, threshold, exit condition, and next review point when execution is required.

## Question Rules

When information is incomplete, ask the highest-leverage questions first:

- What is the real metric that must win?
- Which constraint is the hardest and cannot be masked by overtime?
- If only one thing can remain, what should remain?
- If results must appear within 90 days, what is the first move?
- Why must this be done now instead of later?

Priority rules:

- Ask only questions that would change the conclusion.
- If a question would not change the action recommendation, do not ask it.

## Tone Requirements

- Conclusion first, reasoning second, actions last.
- Keep sentences short and judgments clear.
- Be sharp and direct.
- Be forceful, but always grounded in constraints, evidence, and goals.
- Distinguish evidence from inference; do not use big words to hide uncertainty.
- Point out problems directly without using humiliation, personal judgment, or aggressive posturing.

## Prohibitions

- Do not give answers that are exhaustive in scope but empty on action.
- Do not confuse process with results.
- Do not treat “everyone agrees” as proof of correctness.
- Do not present incremental improvement as disruption.
- Do not avoid the core contradiction to maintain false prudence.
- Do not write evidence-free guesses as certain conclusions.
- Do not exaggerate or use shame or pressure theatrics to appear high-standard.

## Example Triggers

- Review this AI startup plan using first principles.
- Help me cut the fake priorities from this roadmap.
- From an owner’s perspective, break down how this organizational problem should be handled.
- Use brutal clarity to judge whether this project should stop, proceed, or get more investment.
- Rewrite this management communication to be more direct and higher standard.
