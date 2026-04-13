# AI 应用源码剖析提示

AI 项目的重点不是“哪里调了模型”，而是“上下文如何组装、工具如何编排、结果如何验证与回退”。

## 先看哪里

- 模型/供应商配置：model、temperature、max tokens、fallback
- 系统提示词、模板、few-shot、prompt builder
- Agent / Workflow / Graph / Orchestrator
- Tools / function calling / external action adapters
- Retrieval / RAG / embedding / rerank / context assembly
- Memory / session / history trimming / cache
- Guardrails / policy / output validation / moderation
- Tracing / eval / feedback / cost logging

## 重点关注

### 1. 主链路
- 请求如何进入系统
- prompt 在哪里拼装
- 何时检索、何时调用工具、何时直接出答案
- 多步 agent 如何决定下一步动作

### 2. 上下文工程
- 指令、用户输入、历史消息、知识片段的拼接顺序
- 截断、压缩、去重和缓存策略
- 哪些信息是强约束，哪些是可选上下文

### 3. 工具与外部系统
- 工具 schema 在哪里定义
- 参数校验与错误处理在哪里做
- 工具返回结果如何再次进入模型上下文

### 4. 质量与风险
- 结果是否有结构化校验
- 是否有 fallback / retry / timeout / circuit breaker
- 是否记录 prompt、token、latency、失败原因

## 你要回答的问题

- 系统是单次问答、RAG、agent、多 agent 还是 workflow 编排
- 决策点在哪：模型、规则、工作流引擎还是人工阈值
- 一次典型请求的真实路径是什么
- 幻觉、上下文污染、工具失败、成本飙升、延迟抖动优先查哪里
- 新能力应该加在 prompt、tool、retrieval、router 还是 evaluator

## 常见风险

- Prompt、业务规则、工具编排耦在一起
- 检索与生成边界不清，问题难归因
- 缺少可观测性，只能靠猜
- 没有结构化输出校验
- fallback 存在但没有真正闭环验证
