# React analysis prompts

In React projects, first understand **how pages are assembled, where state comes from, when data is fetched, who triggers side effects, and where the client/server boundary actually sits**.

## Start here

- `package.json`: framework, build tool, state library, router library
- `src/main.*`, `src/index.*`, `app/`, `pages/`
- Router: React Router, Next.js App Router, or custom routing
- State management: Redux, Zustand, MobX, Context, Recoil, Jotai
- Data layer: React Query, SWR, API client, BFF
- Page containers, hooks, component libraries, form layer
- Config: env vars, feature flags, permissions, analytics

## Focus on

### 1. App assembly
- How the root entry mounts the app
- Which global capabilities are implied by provider order
- How routing, auth, layout, theme, and i18n are plugged in

### 2. Primary page paths
- The path from URL to rendered page
- Where initial page data is fetched
- How user interaction mutates local state and remote state

### 3. State boundaries
- Whether server state and client state are clearly separated
- Whether hooks are reusable logic or hidden coupling
- Whether deep components are over-aware of global state

### 4. SSR / CSR / RSC boundaries
- Which logic runs on the server versus the client
- How hydration, caching, and prefetch affect behavior

## Questions to answer

- After a user enters a page, how do key data and key state actually flow?
- Are responsibilities between pages, hooks, stores, and API clients clear?
- Where should you look first for blank screens, duplicate requests, inconsistent state, or render thrash?
- Is a new requirement better added in the page container, hook, store, or service layer?

## Common risks

- Hooks take on too much orchestration logic
- Deep components directly read and write global state
- Server state and client state are mixed together
- Multiple state systems overlap without clear ownership
- The page works, but the real dependency relationships are hard to explain
