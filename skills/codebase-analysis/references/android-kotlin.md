# Android / Kotlin 源码剖析提示

Android/Kotlin 项目要先看应用如何启动、页面和导航如何组织、状态与数据如何跨生命周期流动，再看协程与后台任务边界。

## 先看哪里

- `settings.gradle`、`build.gradle(.kts)`、`gradle/libs.versions.toml`
- `AndroidManifest.xml`：Application、Activity、Service、Provider、权限、intent-filter
- `Application`、启动 Activity、Navigation graph、Deep Link
- UI：XML View / Jetpack Compose / 混合架构
- 状态管理：ViewModel、StateFlow、LiveData、MVI/MVVM
- 数据层：Repository、Room、DataStore、Retrofit、OkHttp
- 异步与后台：Coroutine、WorkManager、Service、Push、Sync

## 重点关注

### 1. 启动与装配
- 应用进程启动后首先初始化哪些全局对象
- 首屏、登录态、AB 配置、远程配置在哪一步决策
- 多 module / 动态 feature 如何接入

### 2. 页面与导航
- Activity / Fragment / Compose Nav 的职责边界
- 路由和 Deep Link 由谁统一编排
- 页面状态由 ViewModel 持有还是散在 UI 层

### 3. 状态与数据
- UI State、Domain State、Cache State 是否分层
- Flow / suspend / callback 的边界是否清晰
- 网络、缓存、本地数据库如何协同

### 4. 后台任务与稳定性
- 同步、重试、离线任务在哪里做
- 崩溃、ANR、卡顿、重复请求优先查哪里

## 你要回答的问题

- 从进程启动到首个业务页面的真实链路是什么
- 一个核心业务动作如何穿过 UI、ViewModel、UseCase、Repository、API/DB
- 状态错乱、返回丢数据、Deep Link 异常、后台同步失败优先看哪层
- 新功能更适合放在 UI、ViewModel、Domain 还是 Data 层

## 常见风险

- Activity / Fragment / Compose 多套 UI 架构并存
- ViewModel 变成大总管
- Repository 同时承担编排、缓存、业务规则
- 协程作用域和生命周期绑定不清
- 多 module 看似解耦，实际通过 util 和 singleton 强耦合
