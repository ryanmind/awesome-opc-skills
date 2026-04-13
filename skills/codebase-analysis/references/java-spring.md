# Java / Spring 源码剖析提示

Java/Spring 系统的核心是：应用如何启动装配、请求和任务如何穿过 Bean 图、事务与数据边界在哪里。

## 先看哪里

- `pom.xml` / `build.gradle`：模块与依赖
- `@SpringBootApplication` 启动类、自动配置、profile
- `application.yml` / `application-*.yml`
- Controller / Filter / Interceptor / Advice / Security config
- Service / Domain / Repository / Mapper / Entity
- MQ、Scheduler、Batch、异步任务、缓存、事务
- OpenFeign / RestTemplate / WebClient / Dubbo / gRPC 等外部调用

## 重点关注

### 1. 启动与自动装配
- 应用启动时创建了哪些关键 Bean
- 条件装配、profile、配置绑定如何影响运行结果
- 多模块项目的边界是业务边界还是打包边界

### 2. 请求主链路
- 请求如何进入 Filter / Security / Interceptor / Controller
- 参数校验、DTO 转换、鉴权、事务、异常处理在哪一层做
- Service 是纯业务，还是掺杂流程编排与外部调用

### 3. 数据与事务
- Entity、DTO、VO、DO、Domain Model 是否混用
- 一个业务动作是否跨多个库/缓存/MQ
- 事务边界与幂等控制是否清晰

### 4. 任务与集成
- 定时任务、消息消费、批处理的入口在哪里
- 外部系统失败后的重试、补偿、降级如何做

## 你要回答的问题

- 应用从启动到接收第一条请求的主路径是什么
- 一个典型业务请求如何穿过控制层、服务层、数据层和外部系统
- 性能瓶颈、事务异常、数据不一致、配置漂移优先查哪里
- 新功能应放在 Controller、Service、Domain、Repository 还是集成层

## 常见风险

- Service 层过胖，Controller 过薄但没有真正领域边界
- 自动装配太多，真实依赖关系不透明
- 事务边界和消息边界错位
- 配置散落在 profile、Nacos、环境变量、代码常量中
- 多模块工程结构清晰，但运行时耦合依然严重
