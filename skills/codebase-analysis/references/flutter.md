# Flutter analysis prompts

In Flutter projects, first understand how the app is assembled, then how state propagates, and finally how platform capabilities and async work are integrated.

## Start here

- `pubspec.yaml`: dependencies, assets, fonts, flavor clues
- `lib/main.dart`: `runApp`, init order, environment switching
- Router config: `GoRouter`, `Navigator`, or custom routing
- State management: Bloc, Cubit, Provider, Riverpod, GetX, MobX
- DI / service locator such as `get_it`
- Repository / API client / local storage
- `MethodChannel`, `EventChannel`, FFI
- Background jobs, isolates, push, analytics

## Focus on

### 1. Startup and assembly
- Initialization order for env, logger, storage, services, router, analytics
- How the root widget injects dependencies and state into the tree
- How flavors and environments are switched

### 2. Screens and state
- Whether pages are thin shells or contain business logic
- Whether Widget / ViewModel / Bloc / UseCase layering is clear
- Who triggers state changes, and who consumes them

### 3. Platform integration and async boundaries
- Where native platform capabilities enter Flutter runtime
- How channels are wrapped and surfaced to app code
- How async jobs, isolates, retries, and lifecycle transitions are managed

### 4. Data and persistence
- How API, cache, and local storage are coordinated
- Whether repository boundaries are clean or overloaded
- How offline behavior and error recovery are handled

## Questions to answer

- What is the real path from app launch to the first important screen?
- How does a core user action move through widget, state container, domain logic, and data layer?
- Where should you look first for rebuild storms, stale state, duplicate requests, or platform-channel errors?
- Should a new feature live in widget code, state management, domain logic, or platform integration?

## Common risks

- Widgets carry orchestration that should live elsewhere
- State containers are thin wrappers over tangled side effects
- Repositories mix transport, persistence, and business rules
- Multiple state-management styles coexist without clear boundaries
- Platform integration is hidden behind wrappers that are hard to trace
