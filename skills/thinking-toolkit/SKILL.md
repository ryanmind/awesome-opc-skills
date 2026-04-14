---
name: thinking-toolkit
description: Use when the user needs to analyze a problem, make a decision, compare tradeoffs, find a root cause, clarify positioning, structure an argument, or identify leverage points in a system. Automatically choose the most suitable 1-3 mental models from first principles, inversion, SWOT, 5 Whys, Pareto, opportunity cost, and related references, then answer in a conclusion-first format: judgment first, then reasons, models used, and next actions.
---

# Thinking Toolkit

A general entry-point skill for mental models. Use it for decision-making, problem decomposition, root-cause analysis, positioning, structured communication, and system optimization.

## Default principles

- **Conclusion first**: answer "what should I conclude or do" before explaining theory
- **Automatic routing**: choose the best 1-3 models instead of piling up concepts
- **Action-oriented**: every analysis should end in concrete next steps
- **Do not force a model**: if a model does not help, do not use it just because it sounds smart
- **Model combinations are allowed**: different stages of a problem can use different models in sequence

## When to use

Prefer this skill when the user is:

- choosing between multiple options
- judging tradeoffs, opportunity cost, or whether to keep investing
- looking for the real cause rather than surface symptoms
- clarifying career direction, personal positioning, brand/IP positioning, or strategic focus
- turning a messy question into a clear, structured answer
- identifying leverage points, feedback loops, and long-term compounding effects in a system
- shaping a vague idea into a structured argument, answer, or content outline

Common triggers include:

- "Help me analyze this"
- "Should I choose A or B?"
- "Why do I keep getting stuck here?"
- "Is this direction worth doing?"
- "Help me clarify my positioning"
- "What is the real root cause?"
- "Help me build a thinking framework"
- "Use a few mental models to break this down"

## When not to use

This should not be your first choice when:

- the user mainly needs facts, external research, or the latest information
- the user only wants copy polishing, translation, or phrasing edits
- the user mainly wants emotional support rather than analysis and judgment
- another more specific skill is clearly a better match

## Default output order

By default, answer in this order:

1. **Conclusion**
2. **Why this judgment makes sense**
3. **Models used**
4. **Next actions**
5. **If useful: a template, checklist, or table**

Keep it concise unless the user explicitly asks for expansion.

## Routing guide

### 1. Decision and tradeoff problems

Prioritize:
- `opportunity-cost.md`
- `swot.md`
- `sunk-cost.md`
- `pareto.md`

Use for:
- choosing A vs B
- deciding whether to invest more time/resources
- deciding whether to continue the current direction

### 2. Root-cause diagnosis problems

Prioritize:
- `five-whys.md`
- `occams-razor.md`
- `inversion.md`

Use for:
- understanding why results are weak
- locating the real bottleneck
- deciding what errors to avoid first

### 3. Positioning and strategy problems

Prioritize:
- `first-principles.md`
- `swot.md`
- `pareto.md`

Use for:
- brand / IP positioning
- career direction
- strategic focus

### 4. System optimization and long-term advantage problems

Prioritize:
- `feedback-loops.md`
- `compounding.md`
- `pareto.md`

Use for:
- building positive feedback loops
- compounding advantage over time
- choosing which actions are most worth repeating long term

### 5. Content structure and argument-building problems

Prioritize:
- `first-principles.md`
- `inversion.md`
- `pareto.md`
- `assets/output-templates.md`

Use for:
- breaking down an argument
- judging which topic angle is worth pursuing
- designing a content outline

## Model selection rules

- Start from the real user problem, not just the model name the user mentions
- In most cases, use only **1-3 models**
- If the task includes both diagnosis and decision-making, prefer one model to find the cause and one to make the judgment
- If two models create tension, explain the conflict explicitly instead of force-merging them
- For simple problems, one strong model is better than five weak ones

## Reading guide

Load references on demand rather than all at once:

- If you want a model's use cases, misuse warnings, and output shape, open the relevant `references/*.md`
- If you want reusable answer structures, open `assets/output-templates.md`
- Unless you truly need a cross-model comparison, do not load every reference file at once

## General answer flow

By default:

1. Identify the real problem or decision point
2. Give a one-sentence conclusion
3. Explain the 2-3 most important reasons
4. State which models you used and why they fit
5. Give executable next steps
6. If the user wants reuse, add a template, checklist, or table

## Anti-patterns

Avoid:

- listing a pile of models without helping the user solve the problem
- explaining theory without turning it into action
- forcing a full framework every time and bloating the answer
- treating mental models as absolute truth instead of lenses
- ignoring concrete context because a model "sounds sophisticated"
