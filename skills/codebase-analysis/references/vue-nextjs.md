# Vue / Next.js 源码剖析提示

这个 reference 用于两类前端系统：Vue 系项目，以及 Next.js 系项目。重点是页面装配、服务端/客户端边界、状态来源与数据获取时机。

## Vue 项目先看哪里

- `package.json`、`vite.config.*`、`vue.config.js`
- `src/main.*`、router、pinia/vuex、布局与权限
- 页面、组合式函数（composables）、组件库、API client
- SSR / CSR、微前端、国际化、埋点、权限

## Next.js 项目先看哪里

- `app/` 或 `pages/` 目录
- layout、route segment、server action、API route、middleware
- client component / server component 划分
- 数据获取、缓存、revalidate、auth、edge/runtime 配置

## 重点关注

### 1. 页面装配
- 从 URL 到页面渲染经过哪些层
- 路由守卫、布局、权限、数据预取分别在哪一步
- 页面是容器还是直接承担业务编排

### 2. 状态与副作用
- 本地状态、全局状态、服务端状态由谁管理
- composable / hook 是抽象复用还是隐藏耦合
- 请求、副作用、缓存失效在哪里统一处理

### 3. SSR / SSG / CSR / RSC 边界
- 哪些逻辑运行在服务端，哪些运行在浏览器
- hydration、streaming、缓存、revalidate 如何影响行为
- API route / BFF 是否夹带太多业务逻辑

## 你要回答的问题

- 一个典型页面如何完成装配、取数、渲染和交互更新
- 页面、store、composable/hook、API/BFF 的职责是否清晰
- 白屏、重复请求、缓存失效、首屏慢、状态不一致优先查哪里
- 新需求更适合落在页面容器、store、composable/hook 还是 BFF / route handler

## 常见风险

- 页面逻辑塞进 composable/hook 后难以解释调用链
- 服务端和客户端状态边界混乱
- Router、Store、请求层各自维护一份隐式状态
- Next.js 中 server/client 组件边界不清
- Vue 组件拆分很多，但实际依赖关系靠约定维持
