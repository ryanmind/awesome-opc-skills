---
name: codebase-analysis
description: Use when the user needs to deeply understand a codebase, module, or system implementation: first build a high-level system map, then drill into the most important execution paths and implementation details, and produce a handoff-quality explanation that can be understood without constantly rereading the source. Suitable for iOS (ObjC/Swift), Flutter, AI applications, React, HarmonyOS, Python, TypeScript, Android/Kotlin, Java/Spring, Node.js/NestJS, Vue/Next.js, Go/Rust, as well as legacy-system analysis, architecture reviews, critical-path breakdowns, technical due diligence, and onboarding handoffs.
---

# Codebase Analysis

Upgrade "reading source code" into a transferable, drillable, reusable understanding of how a system actually works.
The goal is not to restate files. The goal is to **build the system picture first, then drill into the key implementation details**, so you can answer:

- How the system starts and gets assembled
- How data flows, how interactions enter, and how rendering or final output happens
- How the most important modules are implemented and why they are designed that way
- Where to debug, where to change code for new requirements, and what refactors will affect

## When to use

Prefer this skill when:

- The user asks for source analysis, code walkthroughs, architecture breakdowns, or system deconstruction
- You need to explain a repository clearly to a new teammate, owner, or reviewer
- You need to understand the implementation path without constantly rereading the repo
- You need to locate core paths, critical state, dependencies, and risks
- You need context for debugging, extension, refactoring, or migration
- You need to produce technical due diligence notes, module docs, handoff docs, or a system map

This skill is not the best first choice when:

- The user only wants a tiny bug fixed
- The user only wants API usage, syntax help, or wording polish
- The user mainly needs the latest external information rather than understanding local code

## Success criteria

After the analysis, the reader should be able to answer:

1. Where the system entry point is and what the startup order looks like
2. Which key modules a request or user action moves through
3. What each core module owns, where its boundaries are, and how it collaborates
4. Where state, data, config, and dependencies come from and where they go
5. How user interactions enter the system and how rendering or final output occurs
6. How critical modules are implemented and why the main abstractions exist
7. Which layer is most likely responsible when something breaks and how to investigate it
8. Where a new feature should be added and why
9. Which parts are most fragile or most valuable to refactor first

If the result only tells the reader what folders exist, but not why the system behaves the way it does, where the implementation pressure points are, or what a change will affect, the analysis is not deep enough.

## Default output contract

By default, produce a handoff-friendly, drillable codebase analysis document in roughly this order:

1. **One-sentence conclusion**: what this system fundamentally is and how it works
2. **System landscape**: major modules, runtime boundaries, external dependencies
3. **Entry points and startup path**: where execution begins and how key objects are first created
4. **Core runtime paths**: explain the 1-3 most important call/state flow paths
5. **Module responsibility breakdown**: what each important directory, class, service, page, or state container owns
6. **Data / state / config flow**: inputs, outputs, cache, persistence, remote dependencies
7. **Key implementation details**: how critical classes, functions, state transitions, branches, and failure paths work
8. **Design choices and tradeoffs**: why layering, encapsulation, or orchestration looks the way it does
9. **Debugging map**: where to look first when something breaks, and common symptoms/log points
10. **Extension and refactor guidance**: where new work should go, what to refactor first, and what risks exist
11. **Evidence and open questions**: separate facts, inferences, and still-unverified points

Unless the user explicitly asks for a file-by-file walkthrough, do not narrate the repo in directory order.
If the user's goal is to truly understand the system, do not stop at architecture diagrams; continue into key implementation details, state transitions, and failure branches.

## Workflow

### 1. Define the scope first

Gather or infer:

- Analysis target: the whole repository, a subsystem, or a business flow
- Goal: handoff, debugging, extension, refactoring, due diligence, or knowledge capture
- Audience: developer, tech lead, architect, collaborator, or AI agent
- Stack: iOS, Flutter, AI, React, HarmonyOS, Python, TypeScript, Android, Kotlin, Java, Spring, Node.js, NestJS, Vue, Next.js, Go, Rust, or mixed

If the user did not provide all of this, infer it from the repo and state your assumptions clearly.

### 2. Build the skeleton first, then decide where to drill down

Start with:

- Directory structure
- Dependency and build files
- App entry points / service entry points / top-level execution paths
- Routing, state management, DI, config, networking, and persistence layers
- Top-level orchestrators, coordinators, controllers, services, stores, agents, or pipelines

Answer "what layers make up this system" before answering "how one layer works internally."
Do not get trapped in local detail too early, but also do not stay at a vague high level. The right sequence is: **build the skeleton first, then drill into the key joints.**

### 3. Follow the most important runtime paths

After you understand the shape of the system, trace the most important paths, for example:

- startup
- login / authentication
- request handling
- payment / checkout
- content generation
- sync / background jobs
- rendering / response output

For each path, make clear:

- what triggers it
- what receives it
- what makes decisions
- what persists data
- what mutates state
- what renders or returns the final result

If the user wants deep understanding, keep going into:

- what each critical function/class in the path actually does
- how key branches, error paths, and fallback logic work
- where state is created, passed, mutated, and invalidated
- which details determine real behavior versus thin wrappers

### 4. Extract stable knowledge, but drill into critical implementation details

You are producing reusable understanding, not temporary reading notes. Prioritize:

- module boundaries
- relationships between core objects
- state sources and lifecycles
- config and environment switching
- exception and error propagation paths
- extension points, replacement points, and coupling points
- architecture constraints implied by the coding style

At the same time, be willing to drill into implementation details for:

- critical execution order inside important modules
- key state transitions and lifecycles
- real implementations behind important interfaces/abstractions
- important conditional branches, failure branches, and fallback branches
- performance, concurrency, caching, retry, and idempotency behavior

The goal is not just "this module exists" but "this is how it works, why it works that way, and what changing it would affect."

### 5. Mark information status clearly

For each important judgment, label it when possible as:

- **Fact**: directly supported by files, symbols, config, or call relationships
- **Inference**: derived from multiple pieces of evidence
- **Needs verification**: cannot yet be fully confirmed without runtime checks, logs, tests, or business context

Do not present inferences as hard facts.

## Evidence rules

- Cite specific files, directories, classes, functions, config keys, or protocol names whenever possible
- Find the trunk from entries, dependencies, routing, state, networking, and persistence before drilling into detail
- If the repo is large, cover the highest-leverage directories and highest-frequency call paths first; do not spread effort evenly
- If multiple stacks are present, only load the references relevant to the current path
- If README and code disagree, trust the code and config, and explicitly call out the mismatch

## Stack routing

Read these references on demand:

- iOS (ObjC/Swift): `references/ios.md`
- Flutter: `references/flutter.md`
- AI applications: `references/ai.md`
- React: `references/react.md`
- HarmonyOS: `references/harmonyos.md`
- Python: `references/python.md`
- TypeScript: `references/typescript.md`
- Android / Kotlin: `references/android-kotlin.md`
- Java / Spring: `references/java-spring.md`
- Node.js / NestJS: `references/node-nestjs.md`
- Vue / Next.js: `references/vue-nextjs.md`
- Go / Rust: `references/go-rust.md`

Common combinations:

- React + TypeScript: read `react.md` first, then `typescript.md`
- Next.js: read `react.md` first, then `vue-nextjs.md` for SSR / App Router / boundary guidance
- Flutter + AI: read the Flutter runtime flow first, then use `ai.md` for model calls / retrieval / agent orchestration
- Python + AI: start with `python.md` for service boundaries, then `ai.md`
- Node.js / NestJS + AI: start with `node-nestjs.md`, then `ai.md`
- Java / Spring: use `java-spring.md` first to understand startup, bean wiring, request chains, and job flows
- Android / Kotlin: prioritize app entry points, navigation, state containers, data layer, and coroutine boundaries
- Go / Rust: start with process entry, concurrency model, module boundaries, I/O, and error propagation
- iOS / HarmonyOS / hybrid apps: map the host entry and container communication first, then drill into the platform-specific internals

## Scripts

If you need a quick skeleton for an analysis document, use:

- `scripts/scaffold_analysis_report.py`

It is useful for generating a structured Markdown outline before you fill it with source-backed evidence.

Example:

```bash
python3 scripts/scaffold_analysis_report.py   --system-name "Payment Center"   --stack react --stack typescript   --focus login-flow --focus payment-flow   --output payment-center-analysis.md
```

## Default answer style

- Start with the overall judgment, then expand into detail
- Explain how the system works before explaining why it was implemented that way
- Build the system skeleton first, then drill into key implementation details
- Organize around **paths + modules + state + risks** whenever possible
- Spend less time on generic concepts and more time on what this specific repo actually does
- If the user wants to really understand the system, cover key implementation details, failure paths, and design tradeoffs
- Optimize the final answer for: **understanding, handoff, debugging, extension, and refactoring**

## Anti-patterns

Avoid:

- mechanically introducing files in directory order
- describing local implementation without the main system path
- explaining only "what" but not "why this layering or split exists"
- stopping at a high-level architecture summary without drilling into key details
- describing only the happy path while ignoring failure paths, state changes, and critical branches
- mixing facts, inferences, and open questions together
- omitting debugging entry points, extension landing zones, and refactor risks
- trying to be "complete" in a way that loses the actual center of gravity of the system
