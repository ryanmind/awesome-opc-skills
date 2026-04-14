# Vue / Next.js analysis prompts

Use this reference for two frontend families: Vue systems and Next.js systems. The key focus is page assembly, server/client boundaries, state ownership, and data-fetch timing.

## For Vue projects, start here

- `package.json`, `vite.config.*`, `vue.config.js`
- `src/main.*`, router, pinia/vuex, layout, permissions
- Pages, composables, component libraries, API clients
- SSR / CSR, micro-frontends, i18n, analytics, auth/permissions

## For Next.js projects, start here

- `app/` or `pages/`
- layouts, route segments, server actions, API routes, middleware
- client component / server component boundaries
- data fetching, caching, revalidate, auth, edge/runtime config

## Focus on

### 1. Page assembly
- What layers sit between URL and rendered page
- Where route guards, layouts, permissions, and data prefetch happen
- Whether the page is a container or directly carries business orchestration

### 2. State and side effects
- Who owns local state, global state, and server state
- Whether composables/hooks are real reuse or hidden coupling
- Where requests, side effects, and cache invalidation are consistently handled

### 3. SSR / SSG / CSR / RSC boundaries
- Which logic runs on the server and which runs in the browser
- How hydration, streaming, caching, and revalidation influence behavior
- Whether API routes / BFF layers carry too much business logic

## Questions to answer

- How does a typical page assemble itself, fetch data, render, and update on interaction?
- Are responsibilities between pages, stores, composables/hooks, and API/BFF layers clear?
- Where should you look first for blank screens, duplicate requests, cache invalidation bugs, slow first paint, or inconsistent state?
- Is a new feature better implemented in the page container, store, composable/hook, or BFF / route handler?

## Common risks

- Page logic is moved into composables/hooks in a way that makes the call chain hard to explain
- Server and client state boundaries are muddled
- Router, store, and request layers each maintain their own implicit state
- Server/client component boundaries are unclear in Next.js
- Vue component split is extensive, but the real dependency graph is held together only by convention
