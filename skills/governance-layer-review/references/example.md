# Minimal Examples for Governance Layer Reviews

## Example 1: rules leaking into the identity layer
### Scenario
A `SOUL.md` file defines a “senior architect assistant” while also containing many statements like “always lead with the conclusion” and “do not ask too many questions.”

### Verdict
- Identity layer: **Mostly pass**
- Rules layer: those rules should live in a rules file, not continue to sit inside the identity file

### Why
“Senior architect assistant” answers “who am I.” “Always lead with the conclusion” answers “how should I operate.” That content has leaked into the rules layer.

---

## Example 2: a methods file turns into a policy document
### Scenario
A `SKILL.md` is framed as workflow guidance, but its body repeatedly says things like “all tasks must follow,” “universally forbidden,” and “always required globally.”

### Verdict
- Methods layer: **Mostly pass or Fail**, depending on how much of the document is policy prose
- Rules layer: should absorb those global constraints

### Why
The methods layer is responsible for “how this kind of task is done,” not “what every task in the system must obey.”

---

## Example 3: small overlap that is still acceptable
### Scenario
A rules file says “see `~/.hermes/SOUL.md` for the identity definition” and adds only a one-line summary of the identity file's role.

### Verdict
- Identity layer: **Pass**
- Rules layer: **Pass**

### Why
This is a low-cost directional pointer, not repeated identity prose, so the overlap is acceptable.
