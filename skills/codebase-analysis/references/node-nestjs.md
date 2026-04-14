# Node.js / NestJS analysis prompts

For Node.js or NestJS systems, first map process startup, module wiring, request/job entry points, and async boundaries. Then drill into how controllers, services, queues, and external integrations collaborate.

## Start here

- `package.json`, workspace structure, build scripts, runtime scripts
- Nest modules, providers, controllers, guards, interceptors, pipes
- Express/Fastify middleware, route registration, API gateway layers
- Queues, cron jobs, workers, event handlers, message consumers
- Config, env loading, validation, feature flags, logging
- DB layer, cache, MQ, third-party clients, auth

## Focus on

### 1. Startup and dependency wiring
- How the app boots and loads configuration
- Which modules/providers are critical and how they depend on each other
- Where global middleware, pipes, guards, and interceptors are applied

### 2. Request and job paths
- How a typical request or job moves from entry to business logic to storage/integrations
- Where validation, authorization, retries, and error mapping happen
- How background jobs differ from HTTP request flow

### 3. State, async, and integration boundaries
- Which state is request-scoped, singleton, cached, or externalized
- Where promises, queues, schedulers, and event handlers overlap
- How external clients are wrapped and observed

### 4. Reliability and debugging
- Where structured logs, metrics, traces, and failure context are emitted
- Where duplicate execution, race conditions, or stuck jobs are most likely
- Where timeout and retry behavior is configured

## Questions to answer

- What is the real path from process startup to the first meaningful request or job?
- How does a core flow move through controller/handler, service, domain logic, repository/client, and queue/event layers?
- Where should you look first for auth bugs, validation issues, duplicate jobs, or inconsistent state?
- Should a new feature live in module wiring, controller, service, queue worker, or integration client?

## Common risks

- Providers and services become overly stateful singletons
- Nest modules look clean but hide circular or implicit coupling
- HTTP, queue, and cron logic share business code with weak boundaries
- Error handling and retries are inconsistent across async entry points
