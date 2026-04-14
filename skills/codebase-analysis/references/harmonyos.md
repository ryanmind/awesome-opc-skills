# HarmonyOS analysis prompts

For HarmonyOS projects, start with application entry, stage setup, page routing, state containers, and any bridge between ArkTS/UI logic and platform services.

## Start here

- `module.json5`, app/module configuration, permissions, abilities
- `EntryAbility`, `UIAbility`, stage setup, startup hooks
- Pages, routing, navigation stack, lifecycle hooks
- State containers, services, stores, shared utils
- Data access, network layer, persistence, distributed capabilities
- Device or platform integrations, events, background behavior

## Focus on

### 1. Startup and stage assembly
- How the app starts and which objects are created first
- Where permissions, configuration, auth state, and routing decisions happen
- How modules and abilities are wired together

### 2. Page flow and state
- How a user action moves across pages, stores, and services
- Whether state ownership is clear or duplicated
- How lifecycle changes affect data and rendering

### 3. Platform capabilities and distributed behavior
- Where device capabilities are accessed
- How events, cross-device behavior, or distributed data are coordinated
- How errors, retries, and fallbacks are handled

## Questions to answer

- What is the real path from app launch to the first business page?
- How do page logic, state containers, services, and platform APIs collaborate?
- Where should you look first for routing bugs, stale state, permission issues, or device capability failures?
- Should a new feature live in the page layer, store/service layer, or platform integration layer?

## Common risks

- Lifecycle and routing logic are scattered across pages and abilities
- State is duplicated between page-local and shared containers
- Platform integration is hidden in utility layers that obscure the real call path
- Distributed capabilities look abstractly clean but are hard to trace end to end
