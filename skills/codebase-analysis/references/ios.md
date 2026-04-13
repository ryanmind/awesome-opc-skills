# iOS（ObjC / Swift）源码剖析提示

在分析 iOS 项目时，优先回答“应用如何启动、首屏如何落地、状态如何传递、导航如何切换、网络与本地数据如何协作”。

## 先看哪里

- `*.xcodeproj/project.pbxproj`：模块、targets、build settings、资源组织
- `Package.swift` / `Podfile` / `Podfile.lock`：依赖来源
- `Info.plist`：启动配置、URL Scheme、权限、环境变量
- `AppDelegate` / `SceneDelegate` / `@main` / `main.swift`
- Root Router / Coordinator / TabBar / Navigation 容器
- 网络层、Repository、数据库（Core Data / Realm / SQLite）
- 配置与环境切换（Debug / Release / Feature Flag）

## 重点关注

### 1. 启动链路
- 应用启动后第一个关键对象是谁
- 首屏路由如何决定
- 登录态、实验开关、远程配置在哪一步注入

### 2. 页面与导航
- UIKit 还是 SwiftUI，是否混用
- Push / Present / Deep Link / Tab 切换的入口
- 是否有 Coordinator / Router / Builder 模式

### 3. 状态与数据
- ViewController / ViewModel / Store / Presenter 谁持有状态
- 异步更新通过 callback、Combine、RxSwift、async/await 还是通知
- 本地缓存、持久化、网络数据如何合流

### 4. 边界与耦合
- 页面是否直接调网络层
- 业务逻辑是否被 VC 吞掉
- 是否存在超大 Manager / Singleton

## 你要回答的问题

- 首屏、登录、详情、支付等主链路分别如何走
- 页面、状态、数据层之间的依赖方向是否清晰
- 哪些对象生命周期最长，哪些对象最容易泄漏或失效
- 崩溃、白屏、状态错乱通常会卡在哪一层

## 常见风险

- 视图层承担过多业务逻辑
- 全局单例过多，导致状态来源不清
- 多套导航与状态机制并存
- 异步回调层层嵌套，错误传播困难
- SwiftUI / UIKit 混用但边界不清
