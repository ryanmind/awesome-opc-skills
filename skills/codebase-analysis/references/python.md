# Python 源码剖析提示

Python 项目差异很大，但剖析时通常先找入口、再找分层、再找配置与异步任务边界。

## 先看哪里

- `pyproject.toml` / `requirements.txt` / `setup.py`
- 入口：`main.py`、CLI、`__main__.py`、ASGI/WSGI 启动文件
- Web 框架：FastAPI / Flask / Django / Sanic / aiohttp
- 任务系统：Celery / RQ / APScheduler / 自定义 worker
- 配置：环境变量、settings、Pydantic、YAML、Hydra
- 服务层、领域层、仓储层、ORM、缓存、消息队列
- 测试目录：往往能暴露真实用法

## 重点关注

### 1. 入口与装配
- 应用如何启动，依赖如何注册
- 路由 / 命令 / worker 的入口分别是什么
- 配置和 secrets 在哪里注入

### 2. 分层与职责
- controller / router 之后进入 service 还是直接操作数据库
- domain model、schema、repository 是否有明确边界
- 公共 util 是否已经侵蚀核心领域

### 3. 同步 / 异步 / 后台任务
- 请求线程、async event loop、后台任务如何分工
- 耗时任务在哪里脱离主请求
- 重试、幂等、失败补偿如何处理

### 4. 数据与配置
- ORM model、DTO、Pydantic schema、序列化边界是否清晰
- 配置是静态加载还是运行期动态切换

## 你要回答的问题

- 一次典型请求 / 命令 / 任务如何穿过各层
- 哪些模块是业务核心，哪些只是适配层
- 线上异常、性能瓶颈、数据不一致优先查哪里
- 新需求应落在 router、service、domain、repository 还是 worker

## 常见风险

- 脚本式写法扩张成系统后缺乏边界
- util / helper 成为隐形耦合中心
- 同步异步混用导致上下文和错误传播复杂
- 配置散落，环境行为不稳定
- 测试覆盖存在，但无法解释真实系统结构
