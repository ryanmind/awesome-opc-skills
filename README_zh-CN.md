# Agent Skills

自研 Agent Skills 的唯一源码基座，通过配置和软链接增量分发到 Codex、Claude 与 Hermes。

[English](README.md)

## 目录结构

```text
agent-skills/
├── skills/                  # Skill 运行包唯一源码
├── config/skill-links.toml  # 基座路径、目标目录和 Skill 选择
├── scripts/                 # 校验与软链接同步
├── tests/                   # 文件系统行为测试
└── docs -> ~/llm-wiki/workshop/agent-skills/raw
```

每个 Skill 使用统一契约：

```text
skills/<skill-name>/
├── SKILL.md
├── agents/openai.yaml
├── references/   # 可选，按需加载
├── scripts/      # 可选，确定性工具
└── assets/       # 可选，输出资源
```

## 管理软链接

修改 `config/skill-links.toml` 后执行：

```bash
python3 scripts/manage_skill_links.py status
python3 scripts/manage_skill_links.py check
python3 scripts/manage_skill_links.py sync --dry-run
python3 scripts/manage_skill_links.py sync
```

管理器只创建配置中的链接；基座路径变化后增量更新旧链接；清理取消选择的受管链接；用软链接替换配置目标位置的旧目录；拒绝重复配置；不会覆盖未受管的文件或软链接。

## 验证

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
PYTHONPYCACHEPREFIX=/tmp/agent-skills-pycache python3 -m compileall -q scripts tests skills
```

## Skills

- [ai-coding-workflow](skills/ai-coding-workflow/SKILL.md)
- [codebase-analysis](skills/codebase-analysis/SKILL.md)
- [design-convergence-review](skills/design-convergence-review/SKILL.md)
- [first-principles](skills/first-principles/SKILL.md)
- [git-commit](skills/git-commit/SKILL.md)
- [jaron-wiki](skills/jaron-wiki/SKILL.md)

项目真实文档维护在 `~/llm-wiki/workshop/agent-skills/raw/`，仓库通过 `docs` 软链接访问。

## License

MIT
