# Agent Skills

自研 Agent Skill 的统一仓库。通过软链接分发到 Codex、Claude、Hermes 和 Zcode。

[English](README.md)

## 是什么

`skills/` 是唯一源码。每个 Skill 都以 `SKILL.md` 为入口，并可按需包含参考资料、脚本和资源。

## 为什么

维护一次，即可让所有已配置的 Agent 使用同一版本。链接管理器让分发结果可预期，并保护它不管理的文件。

## 怎么做

1. 在 `skills/` 中新增或更新 Skill。
2. 在 `config/skill-links.toml` 中选择目标 Agent 和要分发的 Skill。
3. 先预览变更：

   ```bash
   python3 scripts/manage_skill_links.py sync --dry-run
   ```

4. 确认后同步：

   ```bash
   python3 scripts/manage_skill_links.py sync
   ```

用 `status` 查看当前链接，用 `check` 校验配置。`sync` 只处理配置中的目标位置，遇到未受管理的文件会拒绝覆盖。

## Skills

| Skill | 用途 |
| --- | --- |
| [design-convergence-review](skills/design-convergence-review/SKILL.md) | 检查设计是否可以进入开发，并指出未收敛的阻塞问题。 |
| [first-principles](skills/first-principles/SKILL.md) | 从证据、约束和可验证假设出发，重新推导决策或诊断。 |
| [git-commit](skills/git-commit/SKILL.md) | 生成符合仓库规则的 Conventional Commit 信息，或提交已暂存的变更。 |
| [hermes-context-review](skills/hermes-context-review/SKILL.md) | 审查 Hermes 上下文中的冲突、过期、不安全或冗余指令。 |
| [llm-wiki](skills/llm-wiki/SKILL.md) | 在显式调用时搜索、验证和维护本地 Markdown Wiki。 |

## 验证

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

## 许可证

MIT
