---
name: codebase-analysis
description: 当用户需要剖析一个代码库、模块或系统实现，输出一份即使脱离源码也能理解的系统说明，并为后续接手维护、排障、扩展与重构建立上下文时使用。适用于 iOS（ObjC/Swift）、Flutter、AI 应用、React、HarmonyOS、Python、TypeScript、Android/Kotlin、Java/Spring、Node.js/NestJS、Vue/Next.js、Go/Rust 等项目，也适用于遗留系统梳理、架构复盘、核心链路拆解和新人交接。
---

# Codebase Analysis

把“看源码”升级成“建立可交接的系统认知”。
目标不是复述文件，而是回答：**系统怎么跑起来、关键模块如何协作、问题应该去哪里查、需求应该在哪里改、重构会牵动什么。**

## 什么时候用

在下面场景优先使用本 skill：

- 用户要“源码剖析 / 代码走读 / 架构拆解 / 系统解构”
- 需要把一个仓库讲清楚给新同学、接手人或评审人
- 需要在不持续翻源码的前提下理解实现路径
- 需要定位核心链路、关键状态、依赖关系和风险点
- 需要为排障、扩展、重构、迁移建立上下文
- 需要输出技术尽调、模块说明、接手文档、系统全景图

不适合优先使用本 skill 的场景：

- 用户只是要修一个很小的点状 bug
- 用户只要 API 用法、语法解释或代码润色
- 用户主要需要“最新资料”而不是“读懂本地代码”

## 成功标准

完成后，读者即使不再打开源码，也应该能回答：

1. 系统的入口在哪里，启动顺序是什么
2. 用户或请求经过哪些关键模块
3. 每个核心模块的职责、边界和协作方式是什么
4. 状态、数据、配置、依赖分别从哪里来，到哪里去
5. 常见问题最可能卡在哪一层，如何排查
6. 新功能应该加在哪里，为什么
7. 如果要重构，哪些点最脆弱、最值得先动

## 默认输出合同

默认产出一份“可接手”的源码剖析文档，建议按这个顺序：

1. **一句话结论**：这个系统本质上是怎么工作的
2. **系统全景**：主要模块、运行边界、外部依赖
3. **入口与启动链路**：程序从哪里启动，第一批关键对象如何建立
4. **核心运行时链路**：按 1～3 条最重要链路讲清楚调用/状态流转
5. **模块职责拆解**：每个核心目录、类、服务、页面、状态容器负责什么
6. **数据 / 状态 / 配置流**：输入、输出、缓存、持久化、远端依赖
7. **关键抽象与设计取舍**：为什么这样分层、封装或编排
8. **排障地图**：出现问题优先看哪里，常见断点/日志/症状是什么
9. **扩展与重构建议**：新增需求放哪里，重构先动哪里，风险是什么
10. **证据与未决问题**：事实、推断、仍待验证的点分开写

除非用户明确要“逐文件讲解”，否则不要按文件顺序流水账式复述源码。

## 工作流

### 1. 先定范围

先收敛以下信息；如果用户没给全，就基于仓库自行推断并明确假设：

- 分析对象：整个仓库 / 某个子系统 / 某条业务链路
- 目标：接手、排障、扩展、重构、技术尽调、知识沉淀
- 读者：开发、TL、架构师、跨端协作方、AI 代理
- 技术栈：iOS / Flutter / AI / React / HarmonyOS / Python / TypeScript / Android / Kotlin / Java / Spring / Node.js / NestJS / Vue / Next.js / Go / Rust / 混合

### 2. 先建立“骨架认知”，不要一上来读细节

优先看：

- 目录结构
- 依赖清单与构建文件
- 应用入口 / 服务入口 / 主流程入口
- 路由、状态管理、DI、配置、网络层、数据层
- 顶层 orchestrator、coordinator、controller、service、store、agent、pipeline

先回答“系统由哪几层组成”，再回答“某一层内部如何实现”。

### 3. 以“运行链路”代替“文件列表”

优先选最关键的 1～3 条链路来拆：

- 用户启动应用后的首屏链路
- 一次核心请求 / 操作 / 任务执行链路
- 一条高价值业务链路（如登录、支付、问答、同步、渲染）

沿着链路写清楚：

- 谁触发
- 谁接收
- 谁做决策
- 谁持久化
- 谁更新状态
- 谁渲染或返回结果

### 4. 抽取“稳定知识”

你要输出的是可复用认知，不是临时阅读痕迹。优先沉淀：

- 模块边界
- 核心对象关系
- 状态来源与生命周期
- 配置与环境切换方式
- 异常传播路径
- 扩展点、替换点、耦合点
- 代码风格背后的架构约束

### 5. 明确标注信息状态

对每个关键判断尽量标记：

- **事实**：可直接由文件、符号、配置、调用关系证明
- **推断**：由多处证据综合判断得到
- **待验证**：当前代码里还不能完全坐实，需要运行、日志、测试或业务确认

不要把推断写成事实。

## 证据规则

- 尽量引用具体文件、目录、类名、函数名、配置项或协议名
- 先从入口、依赖、路由、状态、网络、持久化找主干，再下钻细节
- 如果仓库很大，优先覆盖“高杠杆目录”和“高频调用链”，不要平均用力
- 若存在多技术栈，只加载当前链路相关的 reference，不要全读
- 如果发现 README 与代码不一致，以代码和配置为准，并明确指出偏差

## 技术栈路由

按需读取以下 reference：

- iOS（ObjC/Swift）：`references/ios.md`
- Flutter：`references/flutter.md`
- AI 应用：`references/ai.md`
- React：`references/react.md`
- HarmonyOS：`references/harmonyos.md`
- Python：`references/python.md`
- TypeScript：`references/typescript.md`
- Android / Kotlin：`references/android-kotlin.md`
- Java / Spring：`references/java-spring.md`
- Node.js / NestJS：`references/node-nestjs.md`
- Vue / Next.js：`references/vue-nextjs.md`
- Go / Rust：`references/go-rust.md`

常见组合建议：

- React + TypeScript：先读 `react.md`，再补 `typescript.md`
- Next.js：先读 `react.md`，再补 `vue-nextjs.md` 中的 SSR / App Router / 边界提示
- Flutter + AI：先看 Flutter 主流程，再用 `ai.md` 拆模型调用 / 检索 / agent 编排
- Python + AI：先看 `python.md` 的服务边界，再读 `ai.md`
- Node.js / NestJS + AI：先读 `node-nestjs.md`，再看 `ai.md`
- Java / Spring：优先用 `java-spring.md` 梳理启动装配、Bean 边界、请求链与任务链
- Android / Kotlin：优先看宿主入口、页面导航、状态容器、数据层与协程边界
- Go / Rust：优先先看进程入口、并发模型、模块边界、I/O 与错误传播
- iOS / HarmonyOS 与跨端混合：先梳理宿主入口、容器通信，再看对应端内实现

## 脚本

如需快速起草剖析文档骨架，使用：

- `scripts/scaffold_analysis_report.py`

它适合先生成一个结构化 Markdown 骨架，再把源码证据填进去。

示例：

```bash
python3 scripts/scaffold_analysis_report.py   --system-name "Payment Center"   --stack react --stack typescript   --focus 登录链路 --focus 支付链路   --output payment-center-analysis.md
```

## 默认回答风格

- 先给整体判断，再展开细节
- 先讲系统如何工作，再讲为什么这样实现
- 尽量按“链路 + 模块 + 状态 + 风险”组织
- 少讲泛泛概念，多讲当前仓库里的真实实现
- 最终回答要服务于：**接手、排障、扩展、重构**

## 反模式

避免以下问题：

- 机械地按目录顺序介绍文件
- 只讲局部实现，不讲系统主链路
- 只讲“做了什么”，不讲“为什么这样分层”
- 不区分事实、推断、待验证
- 没有给出排障入口、扩展落点和重构风险
- 为了“全面”而失去重点，导致读者仍然无法接手系统
