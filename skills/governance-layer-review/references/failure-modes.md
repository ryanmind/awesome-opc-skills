# Common Failure Modes in Governance Layer Reviews

## 1. Rules leaking into the identity layer
### Pattern
- the identity layer contains many “must”, “must not”, or “should” statements
- large sections describe execution clauses, formatting requirements, or tool rules

### Risk
- the identity layer stops functioning as a role profile
- rules and persona become mixed, making maintenance harder over time

### Recommended fix
- move hard rules to the rules layer
- keep only role, perspective, capability profile, and focus areas in the identity layer

---

## 2. Identity leaking into the rules layer
### Pattern
- the rules layer spends large sections describing role identity
- it explains at length “what kind of person I am” or “what kind of architect I am”

### Risk
- the rules file loses focus
- rules and identity become duplicative

### Recommended fix
- move self-description of the role back to the identity layer
- keep only execution standards, boundaries, priorities, and exceptions in the rules layer

---

## 3. Policy prose taking over the preferences layer
### Pattern
- the preferences layer contains full policy design
- it carries long clauses that are effectively rules prose

### Risk
- long-term memory becomes too heavy
- deduplication becomes difficult and drift becomes more likely
- user preference and policy document get confused

### Recommended fix
- move policy prose back to the rules layer
- compress the preferences layer into summary-style long-term preferences or corrections

---

## 4. Policy prose taking over the methods layer
### Pattern
- the methods layer uses language like “all tasks must follow”
- method guidance is written like a policy document

### Risk
- the boundary between methods and rules becomes blurry
- the same constraints must be maintained in multiple places

### Recommended fix
- move mandatory constraints back to the rules layer
- rewrite the methods layer as steps, recommended practices, common pitfalls, and completion signals

---

## 5. Prose-heavy templates
### Pattern
- template files contain too much explanatory prose
- checklists grow into long method manuals

### Risk
- templates lose reuse value
- the templates layer starts carrying methods-layer responsibility

### Recommended fix
- keep only structure, fields, skeletons, and placeholder notes in the templates layer
- move explanatory prose back to the methods layer or the standard document

---

## 6. Policy prose appearing in the assets layer
### Pattern
- samples, cases, or references start redefining rules
- case files become new standard files

### Risk
- the assets layer conflicts with the rules or methods layer
- users can no longer tell which file is authoritative

### Recommended fix
- keep only samples, cases, and references in the assets layer
- keep rules and standards only in standard documents

---

## 7. Repeated ownership across layers
### Pattern
- the same responsibility appears in multiple layers
- different files keep re-explaining the same boundary

### Risk
- later updates drift out of sync
- readers cannot tell which statement is authoritative

### Recommended fix
- define a single primary layer for each type of information
- let other layers keep only short pointers instead of repeating full prose

---

## 8. Naming detached from responsibility
### Pattern
- a file name or layer name suggests one thing while carrying another
- the name stayed stable but the responsibility drifted

### Risk
- new maintainers misread the system
- incorrect content keeps accumulating over time

### Recommended fix
- first add a clear responsibility statement
- if the name is misleading in a lasting way, rename it directly

---

## 9. One-off conclusions fossilized as long-term rules
### Pattern
- a temporary judgment from one task gets written into long-term preferences or rules
- a local fix is mistaken for a general standard

### Risk
- long-term layers get polluted
- the system becomes heavier and messier over time

### Recommended fix
- distinguish long-term rules from task-specific conclusions
- keep one-off conclusions in task documents instead of writing them directly into long-term layers

---

## 10. Destroying readability in pursuit of perfect deduplication
### Pattern
- necessary context is removed just to eliminate all repetition
- layers contain only cross-references and lose self-explanatory value

### Risk
- the system becomes purer in form but worse in readability and maintainability
- new readers need much more effort to understand it

### Recommended fix
- remove harmful duplication first, not every possible repetition
- allow small harmless reminders, but avoid repeated full prose and repeated standards
