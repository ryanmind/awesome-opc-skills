# AI application analysis prompts

In AI systems, the key question is not merely "where the model is called" but **how context is assembled, how tools are orchestrated, and how outputs are validated, retried, or rolled back**.

## Start here

- Model / provider config: model, temperature, max tokens, fallback
- System prompts, templates, few-shot examples, prompt builders
- Agent / workflow / graph / orchestrator layers
- Tools / function calling / external action adapters
- Retrieval / RAG / embeddings / reranking / context assembly
- Memory / sessions / history trimming / caching
- Guardrails / policy / output validation / moderation
- Tracing / evals / feedback / cost logging

## Focus on

### 1. The primary runtime path
- How a request enters the system
- Where the prompt is assembled
- When retrieval happens, when tools are called, and when the model answers directly
- How a multi-step agent chooses the next action

### 2. Context engineering
- The ordering of instructions, user input, history, and knowledge snippets
- Truncation, compression, deduplication, and caching strategy
- Which inputs are hard constraints versus optional context

### 3. Tools and external systems
- Where tool schemas are defined
- Where argument validation and error handling happen
- How tool results get fed back into model context

### 4. Quality and risk controls
- Whether outputs are structurally validated
- Whether fallback / retry / timeout / circuit breakers exist
- Whether prompt, token, latency, and failure reasons are logged

## Questions to answer

- Is the system single-turn Q&A, RAG, an agent, multi-agent, or workflow orchestration?
- Where are the actual decision points: the model, rules, workflow engine, or human thresholds?
- What is the real execution path of a typical request?
- Where should you look first for hallucination, context pollution, tool failure, cost spikes, or latency jitter?
- Should a new capability be added at the prompt, tool, retrieval, router, or evaluator layer?

## Common risks

- Prompt logic, business rules, and tool orchestration are tightly coupled
- Retrieval and generation boundaries are unclear, making failures hard to attribute
- Observability is weak, so teams can only guess
- Structured output validation is missing
- Fallbacks exist on paper but are not actually closed-loop validated
