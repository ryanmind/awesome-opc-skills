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

管理器只创建和校验配置中的链接；取消选择的旧链接保持不动；用软链接替换配置目标位置的旧目录或旧软链接；拒绝重复配置；不会覆盖未受管的真实文件。

## LLM Wiki 目录配置

`llm-wiki` Skill 通过 `<wiki-root>/llm-wiki.json` 发现正式页面和原始资料。没有该文件时，使用内置的 `domains/`、`entities/`、`workshop/` 和 `raw/` 目录结构。

Skill 内置的 [examples.llm-wiki.json](skills/llm-wiki/assets/examples.llm-wiki.json) 只用于展示格式；复制到 Wiki 根目录后按实际结构修改：

```json
{
  "formal": [
    "notes/**/*.md",
    "README.md"
  ],
  "raw": ["sources/**/*"],
  "ignored_parts": [".git", ".obsidian", ".claude"]
}
```

搜索、页面读取、lint、source map 生成和验证共用同一份目录配置。`SCHEMA.md`、`AGENTS.md`、`index.md` 和 `log.md` 仍固定在 wiki 根目录。配置位于其他位置时，使用 `--config <path>` 或 `LLM_WIKI_CONFIG`。

## 验证

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
PYTHONPYCACHEPREFIX="${TMPDIR:-/tmp}/agent-skills-pycache" python3 -m compileall -q scripts tests skills
```

## Skills

- [design-convergence-review](skills/design-convergence-review/SKILL.md)
- [first-principles](skills/first-principles/SKILL.md)
- [git-commit](skills/git-commit/SKILL.md)
- [llm-wiki](skills/llm-wiki/SKILL.md)

项目真实文档维护在 `~/llm-wiki/workshop/agent-skills/raw/`，仓库通过 `docs` 软链接访问。

## License

MIT
