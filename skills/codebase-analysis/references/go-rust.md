# Go / Rust analysis prompts

For Go or Rust systems, start from process entry points, concurrency primitives, module boundaries, and I/O behavior. These systems often look small from the outside but hide important control flow in workers, traits/interfaces, and runtime orchestration.

## Start here

- Entry points: `main.go`, `cmd/*`, `main.rs`, `bin/*`, workspace layout
- Build files: `go.mod`, `Cargo.toml`, workspaces, feature flags
- HTTP / RPC servers, CLI entry points, jobs, consumers, schedulers
- Package/module boundaries, traits/interfaces, adapters, domain services
- Concurrency: goroutines, channels, Tokio tasks, async runtimes, worker pools
- Persistence, queues, caches, external clients, config loading

## Focus on

### 1. Startup and dependency wiring
- How config is loaded and validated
- Which services are created at startup and in what order
- Where dependency injection or manual wiring happens

### 2. Request / job execution paths
- How requests, commands, or jobs move through handlers, services, and storage
- Where validation, retries, timeouts, and error translation happen
- How background workers are coordinated and shut down

### 3. Concurrency and ownership boundaries
- Which state is shared versus isolated
- How goroutines / async tasks communicate and fail
- Where backpressure, cancellation, and resource cleanup are enforced

### 4. Observability and reliability
- Where metrics, logging, tracing, and panic handling live
- Which errors are retried, surfaced, or intentionally swallowed
- Where data races, deadlocks, or resource leaks are most likely

## Questions to answer

- What is the real path from process start to the first meaningful unit of work?
- How does a core request or job move through transport, service, domain, and storage layers?
- Where should you look first for latency spikes, queue buildup, worker stalls, or inconsistent state?
- Should a new capability be implemented at the handler layer, service layer, module boundary, or shared runtime utility?

## Common risks

- Concurrency logic is implicit and hard to reconstruct
- Shared helpers become hidden global coupling points
- Interfaces / traits look clean but conceal tangled control flow
- Error handling is inconsistent across layers
- Runtime behavior differs sharply from the neat package layout
