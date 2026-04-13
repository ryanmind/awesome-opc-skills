# Go / Rust 源码剖析提示

Go 和 Rust 的共同重点是：进程入口、模块边界、并发/异步模型、I/O 路径、错误传播与资源所有权（尤其 Rust）。

## Go 项目先看哪里

- `go.mod`、`cmd/`、`main.go`
- `internal/`、`pkg/`、`api/`、`configs/`
- HTTP / gRPC / MQ / cron / worker 启动入口
- context、goroutine、channel、pool、middleware
- DB、cache、config、logger、tracing、feature flags

## Rust 项目先看哪里

- `Cargo.toml`、workspace、crate 边界
- `src/main.rs`、`lib.rs`、bin targets
- async runtime：tokio / async-std
- handler / service / repository / domain / adapter
- trait、error type、ownership、borrowing、Arc/Mutex/RwLock

## 重点关注

### 1. 入口与模块边界
- 进程如何启动，配置如何加载
- HTTP、gRPC、任务 worker 是否共用同一套核心服务
- 包 / crate 的边界是否真正体现架构边界

### 2. 并发与资源
- Go：goroutine、channel、context cancel、并发控制在哪里做
- Rust：async task、ownership、共享状态与锁粒度如何设计
- 超时、取消、重试、背压由谁负责

### 3. 数据与错误传播
- 一次请求如何穿过 handler、service、storage、external client
- 错误是被包装、转换还是吞掉
- 是否有统一 tracing、metrics、structured logs

## 你要回答的问题

- 进程启动后哪些组件最先建立，哪些组件是系统主干
- 一个核心请求 / 任务如何流经各模块与并发边界
- 死锁、阻塞、goroutine 泄漏、内存增长、超时传播异常优先查哪里
- 新功能应该放在 handler、service、domain、adapter 还是独立 worker

## 常见风险

- Go 项目按目录分层，但 context 和并发边界混乱
- goroutine 启得容易，回收与取消没闭环
- Rust 项目为了绕过所有权约束，过度共享状态
- crate / package 切分很多，但真正边界不稳定
- I/O 失败、超时、重试策略散落，系统行为不可预测
