# Java / Spring analysis prompts

For Java/Spring systems, first understand startup and bean wiring, then trace the main request or job paths, and finally inspect transaction, persistence, and async boundaries.

## Start here

- `pom.xml` / `build.gradle`, module boundaries, starters, dependency graph
- `@SpringBootApplication`, auto-configuration, profiles, property sources
- Controllers, filters, interceptors, schedulers, message consumers
- Services, domain layer, repositories, mappers, clients
- Transactions, events, caches, async jobs, MQ integration
- Config classes, security chain, feature toggles, observability

## Focus on

### 1. Startup and assembly
- Which beans are essential and how they are assembled
- Where config, profiles, security, and infra clients are initialized
- How modules are separated or accidentally coupled

### 2. Request and task execution
- How a typical request flows from controller to service to repository/client
- Where validation, transactions, retries, and exception translation happen
- How scheduled jobs or message consumers differ from HTTP flow

### 3. Data and transaction boundaries
- Where transactions begin and end
- How domain objects, DTOs, entities, and persistence models are separated or mixed
- How cache, DB, and remote calls are coordinated

### 4. Reliability and observability
- Where logs, metrics, traces, and alerts are hooked in
- Where timeouts, circuit breakers, and retries are configured
- Where state inconsistency or hidden side effects are most likely

## Questions to answer

- What is the real path from app startup to the first live business endpoint or job?
- How does a core business flow travel across controller, service, domain, repository, and external clients?
- Where should you look first for transaction bugs, stale cache, duplicate work, or security chain issues?
- Should a new capability live in controller, service, domain, integration, or infrastructure config?

## Common risks

- Service classes become orchestration-heavy god objects
- Entity / DTO / domain model boundaries are blurred
- Transactions span too much work and hide cross-system side effects
- Auto-configuration and annotations hide real control flow
