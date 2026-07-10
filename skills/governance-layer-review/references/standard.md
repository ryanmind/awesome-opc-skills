# Governance Layer Review Standard

## 1. Review objective
The goal of this review is not to judge whether the content is well written. The goal is to determine:

1. whether responsibilities are clear
2. whether boundaries are stable
3. whether there is cross-layer leakage, overlap, or duplicated definition
4. whether names match actual responsibilities
5. whether the structure supports long-term evolution, sharing, and reuse

---

## 2. Default layer model (extensible)
Before reviewing, define the layer map for the current system. Do not assume the existing naming is correct. Judge by responsibility first, not by file name.

### 2.1 Identity layer
Answers: **Who am I / In what role do I operate**

Common content:
- identity positioning
- role perspective
- capability profile
- focus areas
- working style
- default judgment style

### 2.2 Rules layer
Answers: **How should I operate / What standards and constraints apply**

Common content:
- operating principles
- delivery standards
- prohibitions
- priorities
- derivation rules
- scope of application
- exception handling rules

### 2.3 Preferences layer
Answers: **What does this user or team care about especially**

Common content:
- user preferences
- team conventions
- long-term correction rules
- standing agreements
- style preferences
- output-format preferences

### 2.4 Methods layer
Answers: **How is this class of task executed in practice**

Common content:
- use cases
- inputs and outputs
- analysis steps
- recommended sequence
- common pitfalls
- execution guidance
- completion signals

### 2.5 Templates layer
Answers: **What reusable structure should this kind of work follow**

Common content:
- templates
- checklists
- structural skeletons
- sample fields
- reference formats

### 2.6 Assets layer (optional)
Answers: **What reusable material already exists**

Common content:
- references
- samples
- cases
- accumulated documents
- reusable fragments

> If the actual system uses fewer layers, trim the model. If it has additional layers such as strategy, domain, or platform, extend it as needed.

---

## 3. One-line boundary test
Use a one-line question to quickly validate each layer boundary:

- Identity layer: who am I
- Rules layer: how should I operate
- Preferences layer: what do you care about
- Methods layer: how is this kind of task done
- Templates layer: what reusable structure should this kind of work follow
- Assets layer: what reusable material already exists

If a layer consistently answers the wrong question, that usually signals cross-layer leakage or misleading naming.

---

## 4. Review process and evaluation rules

### 4.1 Establish the layer map
Clarify:
- which files or directories belong to which layer
- what responsibility each layer currently carries
- which files are authoritative and which are only derived explanations
- whether the system is in a migration or transition state
- whether the review should prioritize declared responsibility or actual carried responsibility
- whether one responsibility is declared by multiple layers at the same time
- whether any layer name no longer matches its actual responsibility

Default rule:
- Check **actual carried responsibility** first, then verify whether the **declared responsibility** matches it
- If the system is in migration or transition, record temporary mismatch between declared and actual responsibility under **Unresolved Items / Migration Exceptions** instead of treating it as an automatic failure

### 4.2 Check the identity layer
Healthy signals:
- primarily defines role, perspective, capabilities, and focus
- helps the reader understand who the actor in this system is

Risk signals:
- heavy use of “must”, “must not”, or “should”
- large sections on document formatting rules
- tool-usage rules, hard process constraints, or heavy derivation rules

Evaluation rule:
- If it mainly answers “who am I”, it is healthy
- If it mainly answers “what must I do”, it has leaked into the rules layer

### 4.3 Check the rules layer
Healthy signals:
- primarily defines operating principles, standards, boundaries, and exceptions
- helps the reader understand how tasks should be executed

Risk signals:
- large sections of role description
- long self-introduction of capabilities
- too many concrete task-method details
- user-specific preference prose mixed in

Evaluation rule:
- If it mainly answers “how should I operate”, it is healthy
- If it mainly answers “what kind of actor am I”, it has leaked into the identity layer
- If it mainly answers “how is this type of task broken down”, it has leaked into the methods layer

### 4.4 Check the preferences layer
Healthy signals:
- primarily records long-term preferences, long-term corrections, and stable conventions
- helps the reader understand what this user or team cares about especially

Risk signals:
- full rules prose
- large sections of methodology prose
- one-off task conclusions
- policy clauses that are effectively equivalent to rules
- architecture decisions mislabeled as personal preference

Extra checks:
- whether semantic duplication exists
- whether the same preference is duplicated across multiple languages
- whether temporary task outcomes were incorrectly stored as long-term memory

### 4.5 Check the methods layer
Healthy signals:
- primarily defines task inputs, steps, outputs, pitfalls, and completion criteria
- can directly guide execution for a class of tasks

Risk signals:
- primary identity definitions mixed in
- global governance policy prose mixed in
- user preference prose mixed in
- large constraint-heavy passages duplicated from the rules layer

Evaluation rule:
- If it mainly answers “how is this class of task done”, it is healthy
- If it mainly answers “what all tasks must obey”, it has leaked into the rules layer

### 4.6 Check the templates layer and assets layer
Healthy template-layer signals:
- provides stable structure, fields, checklists, and skeletons
- emphasizes reuse rather than method prose

Healthy asset-layer signals:
- provides samples, references, cases, and reusable material
- emphasizes accumulated artifacts rather than redefining responsibilities

Risk signals:
- the templates layer carries method prose
- the assets layer carries rules-layer or identity-layer responsibilities
- case files turn into policy files

### 4.7 Identify duplication and misleading naming
Check especially:
- whether the same responsibility is declared repeatedly across layers
- whether a layer name hides its true responsibility
- whether some content should be moved instead of continually appended
- whether the current naming is suitable for public sharing and long-term maintenance

---

## 5. Verdict levels
- **Pass**: responsibilities are clear, boundaries are stable, there is no obvious cross-layer leakage, and any overlap is minor and acceptable
- **Mostly pass**: boundaries are clear overall, but some mixed content or naming issues should still be improved
- **Fail**: responsibilities are materially confused, with obvious cross-layer leakage, duplicated definitions, or long-term drift risk

---

## 6. Output convention
A formal review should contain the following six sections:

### 6.1 Verdict
For each layer, provide:
- Pass / Mostly pass / Fail

### 6.2 Current layer map
State clearly:
- which file or directory belongs to which layer
- what responsibility each layer currently carries
- what the key evidence is

### 6.3 Findings
List by layer:
- what is already done well
- where cross-layer leakage still exists
- whether there is duplicated definition, drift, or misleading naming

### 6.4 Evaluation basis / key evidence
At minimum include:
- key file names
- representative lines, directories, or passages
- the direct signals that triggered the judgment

### 6.5 Unresolved items / migration exceptions
Clearly separate:
- judgments that are not yet fully confirmed
- overlaps temporarily accepted because of migration or transition

### 6.6 Recommendations
Recommend only necessary changes:
- what content should move
- which layer it should move to
- which layer names should change
- which items should be compressed into preference summaries
- which rule-style statements should be rewritten as method guidance
- which changes need immediate action and which can be monitored later

For a formal written review, prefer `assets/review-report.md`. The template provides structure only and does not replace this standard.
