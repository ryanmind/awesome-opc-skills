# 更新日志

所有值得注意的变更都将记录在此文件中。

本文件格式基于 [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)，
项目遵循 [语义化版本控制](https://semver.org/spec/v2.0.0.html)。

## [未发布]

### 新增

- 可配置的增量符号链接分发，支持 Codex、Claude 和 Hermes
- 文件系统测试：路径重定位、去重、冲突、修剪与幂等性
- 设计一致性评审技能，支持单文档和多文档设计文件夹
- 第一性原理分析技能，覆盖决策、诊断和沟通任务
- Git 提交技能，支持提交消息生成与受控提交执行
- llm-wiki 技能，支持本地 Wiki 的检索、验证和维护
- 仓库架构契约、技能包验证器和 GitHub Actions 验证工作流

### 变更

- 将仓库重新定位为 `agent-skills`，作为自我维护的技能源和分发基础
- 将面向用户的项目文档移至 llm-wiki workshop，并通过 `docs` 暴露
- 将每个技能包统一为 `SKILL.md`、`agents/openai.yaml` 和可选的 `references/`、`scripts/`、`assets/`
- 将面向用户的技能指南从运行时包移至 `docs/skills/`
- 将模板和代理可读示例移至其正确的资源目录
- 定位从"个人公司"转变为"AI 增强的独立开发者"
- 更新理念以强调 AI 下的 10 倍生产力
- 通过 AI 优先方法增强价值主张

### 移除

- 移除了低价值、过于通用或已过时的技能：`a-share-value-investing`、`thinking-toolkit`、`github-actions`、`governance-layer-review`、`indie-hacker-methodology` 和 `zshrc-secrets`

## [1.0.0] - 2026-03-05

### 新增

- 初始仓库结构
- 独立开发者方法论技能
- 核心文档（理念、最佳实践）
- 贡献指南
- MIT 许可证
- 项目概述 README

### 文档

- OPC 理念深度解析
- 独立开发者的最佳实践
- 技能开发指南
