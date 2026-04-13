# React 源码剖析提示

React 项目要先搞清楚“页面如何装配、状态从哪里来、数据何时拉、谁触发副作用、客户端与服务端边界在哪里”。

## 先看哪里

- `package.json`：框架、构建工具、状态库、路由库
- `src/main.*` / `src/index.*` / `app/` / `pages/`
- Router：React Router / Next.js App Router / 自定义路由
- 状态管理：Redux / Zustand / MobX / Context / Recoil / Jotai
- 数据层：React Query / SWR / API client / BFF
- 页面容器、hooks、组件库、表单层
- 配置：环境变量、feature flags、权限、埋点

## 重点关注

### 1. 应用装配
- 根入口如何挂载应用
- Provider 顺序代表了哪些全局能力
- 路由、权限、布局、主题、国际化如何接入

### 2. 页面主链路
- 从 URL 到页面渲染的路径
- 页面初始数据在哪里取
- 用户交互如何触发本地状态和远端状态变化

### 3. 状态边界
- 服务器状态和客户端状态是否分清
- hook 是复用逻辑，还是隐藏复杂耦合
- 组件是否过深地感知全局状态

### 4. SSR / CSR / RSC 边界
- 哪些逻辑在服务端执行，哪些在客户端执行
- hydration、缓存、prefetch 如何影响行为

## 你要回答的问题

- 用户进入一个页面后，关键数据和关键状态如何流动
- 页面、hooks、store、API client 的职责是否清晰
- 线上白屏、重复请求、状态不一致、渲染抖动优先看哪里
- 新需求更适合加在页面容器、hooks、store 还是服务层

## 常见风险

- hooks 承担了过多编排逻辑
- 组件树深处直接读写全局状态
- 服务器状态与客户端状态混用
- React Query / Redux / Context 多套状态混搭
- 页面可运行，但真实依赖关系很难解释
