# TypeScript analysis prompts

Use this reference mainly for non-React TypeScript emphasis, or to supplement React analysis with type-system, build-system, module-boundary, and monorepo concerns.

## Start here

- `tsconfig.json` / `tsconfig.*.json`
- Build config: Vite, Webpack, tsup, Rollup, esbuild, Turborepo, Nx
- Package boundaries: `package.json`, workspaces, `exports`, `types`
- Entry files, shared types, generated code, API clients, SDKs, shared packages
- Whether runtime config and type declarations actually match

## Focus on

### 1. Type boundaries
- Where core type definitions live
- Whether DTOs, domain models, view models, and API schemas are mixed together
- Whether types only document intent or actually drive runtime constraints

### 2. Module boundaries
- Responsibilities and dependency direction across monorepo packages
- Whether barrel files hide the real dependency graph
- Whether path aliases affect readability and build behavior

### 3. Build and runtime
- Whether dev, test, and prod entry points are aligned
- Whether ESM/CJS, browser/node, SSR/client boundaries are clear
- Where code generation, schema generation, and type generation sit in the workflow

## Questions to answer

- Do the runtime spine and the type-definition spine of the project actually line up?
- Which modules are stable contracts and which are just temporary stitching?
- Where should you look first for build failures, type drift, or runtime/type mismatches?
- Should a new capability live in the app layer, shared package, domain model, or contract/type layer?

## Common risks

- The type system looks clean, but runtime constraints are missing
- Shared packages become catch-all utility dumps
- Path aliases and barrel files hide the real boundaries
- Generated code and handwritten code have unclear responsibilities
- Dependency direction in the monorepo drifts out of control
