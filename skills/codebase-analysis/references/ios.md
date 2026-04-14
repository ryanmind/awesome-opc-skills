# iOS analysis prompts

For iOS projects, first identify app entry, navigation/container structure, state ownership, data flow, and any host-to-subsystem boundaries. Then drill into concurrency, rendering, and platform integration.

## Start here

- `AppDelegate`, `SceneDelegate`, `@main`, app lifecycle setup
- Root coordinators, routers, tab bars, navigation controllers, container controllers
- UI stack: UIKit, SwiftUI, or hybrid
- State ownership: view model, store, presenter, coordinator, reactive streams
- Networking, persistence, cache, analytics, feature flags
- Background tasks, push, deep links, notifications, system integrations

## Focus on

### 1. Startup and assembly
- Which objects are created first and how dependencies are injected
- Where login state, first-screen routing, feature flags, and environment config are decided
- How modules or feature boundaries are wired together

### 2. Screen flow and state
- How a user action travels from screen event to state change and output
- Whether UIKit / SwiftUI boundaries are clear
- Whether coordinators, presenters, or view models own the right responsibilities

### 3. Async behavior and platform integration
- How async tasks, callbacks, Combine/Rx, or actors are used
- Where background work, notifications, and deep links enter the system
- How failures, retries, and cancellations are handled

## Questions to answer

- What is the real path from app launch to the first meaningful user screen?
- How does a core business flow move through screen layer, presentation/state layer, domain logic, and data layer?
- Where should you look first for navigation bugs, stale UI, duplicate requests, or lifecycle issues?
- Should a new capability live in UI, coordination, state/presentation, domain, or data integration?

## Common risks

- Coordinators/presenters/view models are nominally separated but practically entangled
- UIKit and SwiftUI coexist without clean ownership boundaries
- Shared managers become hidden global state
- Async logic is spread across delegates, callbacks, and reactive streams without a clear spine
