# Flutter 源码剖析提示

Flutter 项目要先看应用如何装配，再看状态如何传播，最后看平台能力和异步任务如何接进来。

## 先看哪里

- `pubspec.yaml`：依赖、assets、fonts、flavors 线索
- `lib/main.dart`：`runApp`、初始化顺序、环境切换
- Router 配置：`GoRouter` / `Navigator` / 自定义路由
- 状态管理：Bloc / Cubit / Provider / Riverpod / GetX / MobX
- DI / service locator：如 `get_it`
- Repository / API client / local storage
- `MethodChannel` / `EventChannel` / FFI
- 后台任务、Isolate、推送、埋点

## 重点关注

### 1. 启动与装配
- 初始化顺序：env、logger、storage、service、router、analytics
- 根 Widget 如何把依赖和状态注入树中
- 多 flavor / 多环境如何切换

### 2. 页面与状态
- 页面是薄壳还是承载业务逻辑
- Widget、ViewModel、Bloc、UseCase 的分层是否清晰
- 状态变化由谁触发、由谁订阅、由谁渲染

### 3. 数据流
- API -> Repository -> State -> UI 的链路是否稳定
- 缓存、分页、重试、离线数据在哪里处理
- 异常如何冒泡回 UI

### 4. 平台交互
- 哪些能力来自原生层
- 方法通道的协议定义与调用时机
- Flutter 与原生之间谁拥有最终状态

## 你要回答的问题

- 应用从 `main.dart` 到首屏的完整链路是什么
- 一个典型业务动作如何穿过 Widget、状态层、Repository 与 API
- 页面卡顿、状态错乱、返回后丢数据、通道调用失败通常查哪里
- 新功能应加在 Widget、状态层还是 Repository/Service

## 常见风险

- 页面层直接拼装太多业务状态
- 多种状态管理方案并存
- service locator 滥用导致依赖不可见
- 原生通道协议分散，问题难追
- 异步状态 race condition 导致 UI 闪烁或覆盖
