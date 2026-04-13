#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

STACK_HINTS = {
    "ios": [
        "入口：AppDelegate / SceneDelegate / @main / Info.plist / 路由入口",
        "关键层次：UI、导航、状态、网络、持久化、组件化、配置",
        "关注 SwiftUI / UIKit 混用、Coordinator、依赖注入、异步边界",
    ],
    "flutter": [
        "入口：lib/main.dart、runApp、Router、DI、状态管理初始化",
        "关键层次：Widget 树、状态容器、Repository、Platform Channel、Isolate",
        "关注页面路由、异步状态、平台桥接、构建 flavor",
    ],
    "ai": [
        "入口：请求如何进入 prompt / tool / retrieval / memory / model 调用",
        "关键层次：编排层、模型适配层、工具层、检索层、评测与观测层",
        "关注上下文拼装、提示词模板、容错回退、缓存、成本与安全边界",
    ],
    "react": [
        "入口：main.tsx / index.tsx、Router、页面装配、数据预取",
        "关键层次：页面、组件、hooks、状态管理、API client、构建产物",
        "关注客户端/服务端边界、状态来源、数据请求与副作用",
    ],
    "harmonyos": [
        "入口：EntryAbility / UIAbility / app.json5 / module.json5 / 路由",
        "关键层次：Ability、页面、状态装饰器、服务、分布式能力、配置",
        "关注 Stage 模型、ArkTS 状态同步、Ability 生命周期",
    ],
    "python": [
        "入口：CLI / main.py / app factory / server bootstrap / worker bootstrap",
        "关键层次：接口层、服务层、领域层、数据层、任务层、配置层",
        "关注同步/异步边界、框架生命周期、依赖注入、任务编排",
    ],
    "typescript": [
        "入口：tsconfig、构建入口、运行时入口、导出边界、monorepo package 边界",
        "关键层次：类型模型、运行时实现、接口契约、构建工具、共享库",
        "关注类型与运行时不一致、路径别名、包依赖和代码生成",
    ],
    "android-kotlin": [
        "入口：Application、启动 Activity、AndroidManifest、Navigation graph",
        "关键层次：UI、ViewModel、Domain、Repository、API/DB、后台任务",
        "关注 Compose/Fragment 边界、协程作用域、状态容器、Deep Link",
    ],
    "java-spring": [
        "入口：@SpringBootApplication、application.yml、Filter/Security/Controller",
        "关键层次：Controller、Service、Domain、Repository、MQ/Task、集成层",
        "关注 Bean 装配、事务边界、配置 profile、外部系统调用链",
    ],
    "node-nestjs": [
        "入口：main.ts/bootstrap、AppModule、全局 middleware/guard/interceptor",
        "关键层次：Module、Controller、Service、Repository、Queue/Event、Adapter",
        "关注异步错误传播、模块依赖、DTO/Entity 边界、任务编排",
    ],
    "vue-nextjs": [
        "入口：Vue 的 main/router/store 或 Next.js 的 app/pages、layout、middleware",
        "关键层次：页面、组件、composable/hook、store、API/BFF、SSR/RSC 边界",
        "关注页面装配、取数时机、客户端/服务端边界、缓存与副作用",
    ],
    "go-rust": [
        "入口：Go 的 cmd/main.go 或 Rust 的 main.rs/lib.rs/workspace",
        "关键层次：handler、service、domain、storage、client、worker",
        "关注并发模型、错误传播、I/O 路径、模块边界与资源生命周期",
    ],
}

STACK_ALIASES = {
    "objc": "ios",
    "swift": "ios",
    "ios-swift": "ios",
    "ios-objc": "ios",
    "reactjs": "react",
    "ts": "typescript",
    "android": "android-kotlin",
    "kotlin": "android-kotlin",
    "android-kotlin": "android-kotlin",
    "java": "java-spring",
    "spring": "java-spring",
    "springboot": "java-spring",
    "spring-boot": "java-spring",
    "java-spring": "java-spring",
    "node": "node-nestjs",
    "nodejs": "node-nestjs",
    "node-js": "node-nestjs",
    "nestjs": "node-nestjs",
    "nest": "node-nestjs",
    "node-nestjs": "node-nestjs",
    "vue": "vue-nextjs",
    "next": "vue-nextjs",
    "nextjs": "vue-nextjs",
    "next-js": "vue-nextjs",
    "vue-nextjs": "vue-nextjs",
    "go": "go-rust",
    "rust": "go-rust",
    "go-rust": "go-rust",
}

CORE_SECTIONS = [
    "一句话结论",
    "分析范围与目标",
    "系统全景",
    "入口与启动链路",
    "核心运行时链路",
    "模块职责拆解",
    "数据 / 状态 / 配置流",
    "关键抽象与设计取舍",
    "依赖与外部系统",
    "排障地图",
    "扩展落点",
    "重构建议与风险",
    "证据 / 推断 / 待验证问题",
]


def normalize_stack(raw_stack: str) -> tuple[str, str | None]:
    normalized = raw_stack.strip().lower()
    canonical = STACK_ALIASES.get(normalized, normalized)
    if canonical in STACK_HINTS:
        return canonical, None
    return normalized, f"[WARN] Unsupported stack '{raw_stack}'. No built-in hints available."


def render(system_name: str, stacks: list[str], focuses: list[str]) -> tuple[str, list[str]]:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    normalized_stacks: list[str] = []
    warnings: list[str] = []
    seen: set[str] = set()

    for raw_stack in stacks:
        canonical, warning = normalize_stack(raw_stack)
        if warning:
            warnings.append(warning)
        if canonical not in seen:
            normalized_stacks.append(canonical)
            seen.add(canonical)

    lines = [
        f"# {system_name} 源码剖析",
        "",
        f"- 生成时间：{now}",
        f"- 技术栈：{', '.join(normalized_stacks) if normalized_stacks else '待补充'}",
        f"- 分析焦点：{', '.join(focuses) if focuses else '系统全局'}",
        "",
        "> 目标：让读者即使不再打开源码，也能理解系统如何实现，并具备继续接手、排查、扩展和重构的能力。",
        "",
    ]

    if normalized_stacks:
        lines += ["## 技术栈阅读提示", ""]
        for stack in normalized_stacks:
            hints = STACK_HINTS.get(stack)
            if not hints:
                lines += [f"### {stack}", "- 未内置该技术栈提示，请手动补充该系统的入口、分层、状态与风险点。", ""]
                continue
            lines.append(f"### {stack}")
            lines += [f"- {hint}" for hint in hints]
            lines.append("")

    lines += ["## 建议先回答的关键问题", ""]
    questions = [
        "系统从哪里启动？第一个关键对象/模块是谁创建的？",
        "最重要的 1～3 条运行链路分别是什么？",
        "状态、配置、数据、依赖分别从哪里来？",
        "哪些模块是稳定边界，哪些模块耦合最重？",
        "线上出问题时，第一时间应该看哪里？",
        "如果要新增功能，优先落在哪一层？",
        "如果要重构，先拆哪一块最值？风险是什么？",
    ]
    lines += [f"- [ ] {q}" for q in questions]
    lines.append("")

    for section in CORE_SECTIONS:
        lines += [f"## {section}", "", "[待填写]", ""]

    if focuses:
        lines += ["## 分焦点深挖", ""]
        for focus in focuses:
            lines += [f"### {focus}", "", "- 入口：", "- 主链路：", "- 关键模块：", "- 状态变化：", "- 常见故障点：", "- 扩展建议：", ""]

    return "\n".join(lines).rstrip() + "\n", warnings


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a source code analysis markdown scaffold.")
    parser.add_argument("--system-name", required=True, help="System or repository name")
    parser.add_argument(
        "--stack",
        action="append",
        default=[],
        help=(
            "Stack name, repeatable. Supports aliases like ios/swift, react, typescript/ts, "
            "android/kotlin, java/spring, node/nestjs, vue/nextjs, go/rust."
        ),
    )
    parser.add_argument("--focus", action="append", default=[], help="Focus area, repeatable")
    parser.add_argument("--output", required=True, help="Output markdown file")
    args = parser.parse_args()

    content, warnings = render(args.system_name, args.stack, args.focus)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
    print(f"[OK] Wrote analysis scaffold to {output}")
    for warning in warnings:
        print(warning, file=sys.stderr)


if __name__ == "__main__":
    main()
