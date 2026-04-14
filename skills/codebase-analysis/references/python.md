# Python analysis prompts

Use this reference for Python systems to understand process entry points, service boundaries, module layering, runtime configuration, and how requests, jobs, or scripts actually move through the codebase.

## Start here

- Entry points: `main.py`, `app.py`, `manage.py`, `cli.py`, package `__main__`
- Framework wiring: FastAPI, Flask, Django, Celery, Typer, Click, asyncio
- Config, env loading, settings objects, dependency injection patterns
- Routers/views, services, domain modules, repositories, tasks, workers
- Persistence, caches, queues, external clients, model/runtime integrations
- Logging, metrics, tracing, retries, timeout handling

## Focus on

### 1. Startup and runtime assembly
- How config is loaded and validated
- Which app objects, clients, and services are created first
- How web, task, and CLI entry points share or split dependencies

### 2. Request / task / script paths
- How a typical request or job flows through routers, services, and persistence
- Where validation, retries, error translation, and side effects happen
- How background work differs from request-response flow

### 3. Module and state boundaries
- Whether modules are cleanly layered or rely on ad hoc imports
- Which state is global, cached, request-local, or persisted
- Whether shared helpers hide important business logic

### 4. Reliability and operability
- Where logs, traces, and metrics are emitted
- Where timeout, retry, and fallback behavior is implemented
- Where race conditions, stale cache, or hidden I/O are most likely

## Questions to answer

- What is the real path from process start to the first useful request, command, or job?
- How does a core business flow move through API/CLI/task entry points, service logic, and storage/integration layers?
- Where should you look first for config drift, import coupling, duplicate side effects, or async issues?
- Should a new capability live in the entry layer, service layer, domain module, task worker, or integration adapter?

## Common risks

- Utility modules become a dumping ground for real business logic
- Framework structure looks clean but actual control flow is hidden in decorators or imports
- Shared mutable state leaks across requests or tasks
- Retry and timeout behavior differs across scripts, web handlers, and workers
