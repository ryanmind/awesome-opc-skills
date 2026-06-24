# Governance Layer Review

一个用于检查**治理型分层体系**的可复用 skill。

它帮助你判断一套治理分层在长期演进后是否仍然清晰：

- 职责是否还放在正确的层里？
- 规则、偏好、方法、模板、资产是否被混写？
- 体系是否正在漂移、重复定义，或者越来越难维护？
- 层名是否还和文件实际承担的职责一致？

## 适用场景

这个 skill 适合检查**治理型分层设计**，而不是运行时软件架构。

典型场景包括：

- 重构、拆分、合并、重命名之后做一次分层复查
- 检查 identity / rules / preferences / methods / templates 是否混层
- 识别多个文件之间的重复归属与重复定义
- 发现命名失真和长期漂移
- 在对外分享某套治理设计前，先确认边界是否稳定、表达是否清楚

## 不适合的场景

这个 skill 默认**不主要用于**：

- controller / service / repository 这类技术分层
- 运行时系统架构拆分
- 领域建模或业务模块边界评审
- 组织架构、权限模型、汇报关系审计

## 默认检查的层

默认最适合以下几类层：

- **Identity** — 谁在执行
- **Rules** — 有哪些标准和约束
- **Preferences** — 用户或团队长期在意什么
- **Methods** — 这类任务应该怎么做
- **Templates** — 可复用结构、模板、checklist
- **Assets** — 可复用样例、参考资料、沉淀材料

也可以按你的实际治理体系扩展到其他层。

## 一个好的输出应该长什么样

一次有价值的 review 至少应该：

- 给每个文件或目录建立层映射
- 区分“声明职责”和“实际职责”
- 找出串层、混写、重复归属
- 用明确证据解释判断
- 给出恢复清晰边界所需的最小改动建议

## 仓库结构

```text
.
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── agents/openai.yaml
├── references/
│   ├── standard.md
│   ├── failure-modes.md
│   └── example.md
└── templates/
    └── review-report.md
```

## 主要文件说明

- `SKILL.md` — skill 定义与执行流程
- `agents/openai.yaml` — skill 展示元数据
- `references/standard.md` — 判定标准与 review 规则
- `references/failure-modes.md` — 常见失败模式
- `references/example.md` — 最小示例与尺度校准
- `templates/review-report.md` — 结构化报告模板

## 使用示例

```text
Use governance-layer-review to inspect this governance-layer system for mixed responsibilities, duplicated rules, naming mismatch, and long-term drift.
```

## 这个仓库适合谁

如果你想要的是一个**聚焦、可复用**的治理分层 review skill，而不是一个大而全的框架，这个仓库就很适合单独开源。
