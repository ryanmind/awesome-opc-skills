# Node.js / NestJS 源码剖析提示

Node.js / NestJS 项目要重点看启动装配、模块依赖、异步链路、中间件/拦截器，以及 I/O 与任务编排如何贯穿整个系统。

## 先看哪里

- `package.json`、workspace、构建与运行脚本
- `main.ts/js`、bootstrap、env/config 加载
- NestJS：`AppModule`、feature modules、providers、guards、interceptors、pipes
- Express / Koa / Fastify 中间件链
- Controller / Resolver / Service / Repository / Client
- 队列、定时任务、事件总线、WebSocket、stream
- ORM / query builder / schema / migration

## 重点关注

### 1. 启动与模块装配
- 应用启动时注册了哪些全局中间件、拦截器、异常处理器
- 配置、logger、tracing、数据库连接、缓存在哪一步建立
- 模块依赖方向是否清晰

### 2. 请求与异步链路
- 一个请求如何穿过 middleware、guard、pipe、controller、service
- 异步错误是如何传播和统一处理的
- 重试、超时、并发控制由谁负责

### 3. 数据与集成
- DTO、schema、domain object、ORM entity 的边界
- 外部 API、MQ、缓存、数据库如何组合
- BFF 是否承担了不该承担的业务规则

### 4. 任务与实时能力
- cron、queue、event consumer、socket gateway 的入口和职责
- 请求链路和任务链路之间如何共享上下文

## 你要回答的问题

- 系统如何 bootstrap，模块之间怎么连起来
- 一个典型接口 / job / event 是如何流经各层的
- 内存上涨、事件循环阻塞、接口超时、消息重复消费优先查哪里
- 新能力应加在 module、service、adapter、queue worker 还是中间件层

## 常见风险

- service 层既写业务又写集成编排
- module 切得很多，但 provider 实际彼此强依赖
- 异步错误链路不统一，日志难串起来
- DTO、ORM entity、返回对象混用
- queue / event / HTTP 三套入口并存但边界不清
