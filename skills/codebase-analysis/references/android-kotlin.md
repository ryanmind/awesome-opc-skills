# Android / Kotlin analysis prompts

For Android/Kotlin systems, first understand how the app starts, how screens and navigation are organized, how state and data move across lifecycles, and where coroutine and background-job boundaries sit.

## Start here

- `settings.gradle`, `build.gradle(.kts)`, `gradle/libs.versions.toml`
- `AndroidManifest.xml`: Application, Activity, Service, Provider, permissions, intent-filters
- `Application`, launch Activity, Navigation graph, deep links
- UI: XML Views, Jetpack Compose, or mixed architecture
- State management: ViewModel, StateFlow, LiveData, MVI/MVVM
- Data layer: Repository, Room, DataStore, Retrofit, OkHttp
- Async and background work: coroutines, WorkManager, services, push, sync

## Focus on

### 1. Startup and assembly
- Which global objects are initialized first when the process starts
- Where first-screen routing, auth state, AB config, and remote config are decided
- How multi-module or dynamic-feature wiring works

### 2. Screens and navigation
- Responsibility boundaries between Activity / Fragment / Compose Nav
- Who owns route and deep-link orchestration
- Whether screen state lives in ViewModel or leaks into the UI layer

### 3. State and data
- Whether UI state, domain state, and cache state are separated
- Whether Flow / suspend / callback boundaries are clear
- How network, cache, and local database cooperate

### 4. Background work and reliability
- Where sync, retry, and offline work are handled
- Where to look first for crashes, ANRs, jank, or duplicate requests

## Questions to answer

- What is the real path from process startup to the first business screen?
- How does a core business action move through UI, ViewModel, UseCase, Repository, and API/DB?
- Which layer should you inspect first for corrupted state, missing return data, deep-link failures, or background sync issues?
- Should a new feature live in the UI, ViewModel, domain, or data layer?

## Common risks

- Multiple UI styles coexist without clear boundaries
- The ViewModel becomes a god object
- The Repository owns orchestration, caching, and business rules all at once
- Coroutine scopes and lifecycle ownership are unclear
- Modules look decoupled on paper but are tightly coupled through utils and singletons
