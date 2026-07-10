# Repository Rule Discovery

## Goal

Find explicit, enforceable commit-message rules without loading unrelated repository content.

Read this file only after the main workflow finds a dedicated rule source or a commit-related match inside a broad candidate file.

## Reading Rules

1. Read small, dedicated commit configuration files directly.
2. Search broad files such as `package.json`, `AGENTS.md`, `.github/**`, and contribution guides for `commit`, `commitlint`, `subject`, `scope`, `trailer`, or `Conventional Commits` before reading relevant sections.
3. Follow references from an authoritative file only when they point to commit-message rules.
4. Treat hooks and CI validation as enforceable. Treat written repository policy as authoritative unless it conflicts with executable validation.
5. When sources conflict, prefer executable validation, then the most specific repository policy. Report an unresolved material conflict.

Return only confirmed rules and unresolved conflicts to the main workflow. Do not load unrelated sections from candidate files.
