# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Configurable, incremental symbolic-link distribution for Codex, Claude, and Hermes
- Filesystem tests for path relocation, deduplication, conflicts, pruning, and idempotence
- Design convergence review skill for single documents and multi-document design folders
- Repository architecture contract, skill package validator, and GitHub Actions validation workflow
- AI-powered coding workflow skill with Claude Code, Cursor, and Copilot integration
- AI-first development philosophy and modern tech stack recommendations
- Success metrics comparing traditional vs AI-augmented development
- Comprehensive AI tools comparison and productivity benchmarks

### Changed
- Repositioned the repository as `agent-skills`, a self-maintained skill source and distribution base
- Moved human-facing project documentation to the llm-wiki workshop and exposed it through `docs`
- Standardized every skill package on `SKILL.md`, `agents/openai.yaml`, and optional `references/`, `scripts/`, or `assets/`
- Moved human-facing skill guides from runtime packages to `docs/skills/`
- Moved templates and agent-readable examples into their correct resource directories
- Repositioned from "one person company" to "AI-augmented solo developer"
- Updated philosophy to emphasize 10x productivity with AI
- Enhanced value proposition with AI-first approach

### Removed
- Removed low-value, overly generic, or obsolete skills: `a-share-value-investing`, `thinking-toolkit`, `github-actions`, `governance-layer-review`, `indie-hacker-methodology`, and `zshrc-secrets`

### Planned
- AI design system skill (Midjourney + Figma AI)
- AI content engine for marketing automation
- AI customer support automation
- Rapid prototyping skill
- Launch checklist skill
- Pricing strategy skill
- Build in public tools

## [1.0.0] - 2026-03-05

### Added
- Initial repository structure
- Indie Hacker methodology skill (独立开发者方法论)
- Core documentation (Philosophy, Best Practices)
- Contributing guidelines
- MIT License
- README with project overview

### Documentation
- OPC philosophy deep dive
- Best practices for solo developers
- Skill development guidelines

[Unreleased]: https://github.com/ryanmind/awesome-opc-skills/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ryanmind/awesome-opc-skills/releases/tag/v1.0.0
