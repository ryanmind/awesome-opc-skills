# TypeScript 源码剖析提示

TypeScript 参考主要用于非 React 侧重点，或者补充 React 之外的类型系统、构建系统、模块边界与 monorepo 结构分析。

## 先看哪里

- `tsconfig.json` / `tsconfig.*.json`
- 构建配置：Vite / Webpack / tsup / Rollup / esbuild / Turborepo / Nx
- 包边界：`package.json`、workspace、`exports`、`types`
- 入口文件、公共类型、生成代码、API client、SDK、shared package
- 运行时配置与类型声明是否一致

## 重点关注

### 1. 类型边界
- 核心类型定义在哪里
- DTO、Domain Model、View Model、API Schema 是否混用
- 类型是否只是提示，还是实际驱动了运行时约束

### 2. 模块边界
- monorepo 中各 package 的职责与依赖方向
- barrel file 是否掩盖了真实依赖
- path alias 是否影响可读性和构建行为

### 3. 构建与运行时
- 开发态、测试态、生产态入口是否一致
- ESM/CJS、browser/node、SSR/client 边界是否清晰
- 代码生成、schema 生成、类型生成在流程中的位置

## 你要回答的问题

- 项目的运行时主链路和类型定义主链路是否一致
- 哪些模块是“稳定契约”，哪些模块只是临时拼接
- 构建失败、类型漂移、运行时与类型不一致优先查哪里
- 新能力应放在应用层、共享包、领域模型还是类型契约层

## 常见风险

- 类型系统看起来整齐，但运行时约束缺位
- shared 包变成万能包
- path alias 和 barrel file 隐藏真实边界
- 生成代码与手写代码职责不清
- monorepo 依赖方向失控
