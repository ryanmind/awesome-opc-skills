---
name: governance-layer-review
description: Use when checking a governance layer system for unclear boundaries, mixed responsibilities, duplicate rules, naming mismatch, or gradual drift over time.
---

# Governance Layer Review

## Overview
Keep a governance layer system clear, stable, and easy to maintain over time.

`governance-layer-review` reviews **governance-oriented layer systems**. It is designed by default for layer models such as identity, rules, preferences, methods, templates, and assets, and helps identify:
- unclear ownership
- mixed responsibilities across layers
- duplicated definitions
- gradual drift over time
- names that no longer match responsibilities

This skill is not tied to any specific product, platform, repository, or fixed layer naming scheme. If you apply it to another system, define that system's layer mapping and role responsibilities before starting the review.

---

## When to use
Use this skill when:
- key files in a governance layer system were just changed
- a layer was added, split, merged, or renamed
- role definitions, responsibility boundaries, or ownership rules were adjusted
- you want a periodic review to confirm the system has not drifted back into cross-layer mixing
- you want to share a layer design externally and first verify that the framing is stable and the boundaries are clear
- the user explicitly asks whether the system has cross-layer leakage, duplication, or needs cleanup or renaming

---

## Out of scope
By default, do not use this skill for:
- technical architecture layering such as controller / service / repository
- runtime system architecture layers
- business-module boundaries or domain-model boundaries
- org structure, permission models, or reporting-line reviews

Use this skill only when the object being reviewed is itself a governance, standards, or responsibility-allocation system.

---

## What good output looks like
A strong review should:
- map each file or directory to a layer
- separate declared responsibility from actual responsibility
- explain the verdict with concrete evidence
- flag duplication, drift, and naming mismatch
- recommend the smallest set of changes that would restore clean boundaries

---

## Workflow
### Step 1: establish the layer map
Clarify:
- which layers exist
- what each layer is responsible for
- which files or directories belong to which layer
- which files are authoritative and which are only derived explanations
- whether the system is currently in a migration or transition state

Do not assume the existing names are correct. Judge by responsibility first, not by file name.

### Step 2: review each layer against the standard
During the review, prioritize:
- `references/standard.md`: the **single source of truth for evaluation criteria**, including the layer standard, boundary tests, evaluation rules, and output expectations
- `references/failure-modes.md`: common failure patterns and warning signals
- `references/example.md`: minimal examples for calibration and judgment consistency

### Step 3: produce a structured conclusion
Use:
- `templates/review-report.md`

`templates/review-report.md` provides only the output structure. It does not introduce new evaluation criteria.

For a formal review, include at least:
- the current layer map
- the verdict
- key findings
- evaluation basis and supporting evidence
- unresolved items or migration-period exceptions
- recommended adjustments
- a minimum-change plan

---

## End-to-end flow
1. Define the layer map
2. Mark authoritative files, derived files, and migration status
3. Identify each layer's responsibility
4. Check for cross-layer leakage against the standard
5. Identify duplicated definitions, drift, and misleading naming
6. Recommend only the minimum necessary adjustments
7. If changes were made, run one more review pass

---

## Companion files
- `references/standard.md`: layer standard, evaluation rules, and output conventions
- `references/failure-modes.md`: common failure modes and how to spot them
- `references/example.md`: minimal examples and calibration guidance
- `templates/review-report.md`: governance boundary review report template

---

## Completion criteria
The review is complete when you can answer the following questions from real files with stable, structured reasoning:
- Who defines role or identity?
- Who defines rules or standards?
- Who records long-term preferences or corrections?
- Who defines task methods?
- Who provides reusable templates, checklists, or references?
- Are the layers free of obvious cross-layer leakage, duplication, and drift?
