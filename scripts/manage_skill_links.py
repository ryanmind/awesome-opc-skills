#!/usr/bin/env python3
"""Reconcile configured agent skill directories with this repository."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ConfigError(ValueError):
    """Raised when distribution configuration is invalid."""


@dataclass(frozen=True)
class Target:
    name: str
    path: Path
    skills: tuple[str, ...]


@dataclass(frozen=True)
class Config:
    source: Path
    targets: tuple[Target, ...]


@dataclass(frozen=True)
class Operation:
    action: str
    target: str
    skill: str
    link: Path
    source: Path | None = None
    detail: str = ""

    def render(self) -> str:
        suffix = f" -> {self.source}" if self.source is not None else ""
        detail = f" ({self.detail})" if self.detail else ""
        return f"{self.action.upper():8} {self.target}:{self.skill} {self.link}{suffix}{detail}"


@dataclass(frozen=True)
class Plan:
    config: Config
    operations: tuple[Operation, ...]

    @property
    def conflicts(self) -> tuple[Operation, ...]:
        return tuple(op for op in self.operations if op.action == "conflict")

    @property
    def changes(self) -> tuple[Operation, ...]:
        return tuple(op for op in self.operations if op.action in {"create", "replace", "remove"})


def expand_path(value: str) -> Path:
    return Path(os.path.expanduser(value)).absolute()


def load_config(path: Path) -> Config:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"config file not found: {path}") from exc
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"invalid TOML in {path}: {exc}") from exc

    if data.get("version") != 1:
        raise ConfigError("config version must be 1")

    distribution = data.get("distribution")
    if not isinstance(distribution, dict):
        raise ConfigError("missing [distribution] table")
    source_raw = distribution.get("source")
    if not isinstance(source_raw, str) or not source_raw:
        raise ConfigError("distribution.source must be a non-empty path")

    source = expand_path(source_raw)
    if not source.is_absolute():
        raise ConfigError("distribution.source must resolve to an absolute path")
    skills_root = source / "skills"
    if not skills_root.is_dir():
        raise ConfigError(f"source skills directory not found: {skills_root}")

    raw_targets = data.get("targets")
    if not isinstance(raw_targets, dict) or not raw_targets:
        raise ConfigError("at least one [targets.<name>] table is required")

    targets: list[Target] = []
    for name in sorted(raw_targets):
        raw = raw_targets[name]
        if not isinstance(raw, dict):
            raise ConfigError(f"targets.{name} must be a table")
        path_raw = raw.get("path")
        skills_raw = raw.get("skills")
        if not isinstance(path_raw, str) or not path_raw:
            raise ConfigError(f"targets.{name}.path must be a non-empty path")
        if not isinstance(skills_raw, list) or not all(isinstance(item, str) for item in skills_raw):
            raise ConfigError(f"targets.{name}.skills must be a list of names")
        if len(skills_raw) != len(set(skills_raw)):
            raise ConfigError(f"targets.{name}.skills contains duplicates")

        target_path = expand_path(path_raw)
        try:
            target_path.relative_to(skills_root)
        except ValueError:
            pass
        else:
            raise ConfigError(f"target path cannot be inside source skills: {target_path}")

        for skill in skills_raw:
            skill_dir = skills_root / skill
            if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").is_file():
                raise ConfigError(f"unknown or invalid skill for {name}: {skill}")
        targets.append(Target(name=name, path=target_path, skills=tuple(skills_raw)))

    return Config(source=source, targets=tuple(targets))


def link_target(path: Path) -> Path | None:
    if not path.is_symlink():
        return None
    raw = os.readlink(path)
    target = Path(raw)
    if not target.is_absolute():
        target = path.parent / target
    return target.absolute()


def same_path(left: Path, right: Path) -> bool:
    return os.path.normpath(str(left)) == os.path.normpath(str(right))


def desired_links(config: Config) -> dict[str, tuple[str, str, Path, Path]]:
    desired: dict[str, tuple[str, str, Path, Path]] = {}
    for target in config.targets:
        for skill in target.skills:
            link = target.path / skill
            source = config.source / "skills" / skill
            key = str(link)
            if key in desired:
                raise ConfigError(f"duplicate destination across targets: {link}")
            desired[key] = (target.name, skill, link, source)
    return desired


def build_plan(config: Config, *, unlink_all: bool = False) -> Plan:
    desired = desired_links(config)
    operations: list[Operation] = []

    for _key, (target_name, skill, link, source) in desired.items():
        if unlink_all:
            if not os.path.lexists(link):
                continue
            actual = link_target(link)
            if actual is not None and same_path(actual, source):
                operations.append(Operation("remove", target_name, skill, link, source))
            else:
                operations.append(
                    Operation(
                        "conflict",
                        target_name,
                        skill,
                        link,
                        source,
                        "current entry does not point to configured source",
                    )
                )
            continue

        if not os.path.lexists(link):
            operations.append(Operation("create", target_name, skill, link, source))
            continue
        if not link.is_symlink():
            if link.is_dir():
                operations.append(Operation("replace", target_name, skill, link, source, "existing directory"))
            else:
                operations.append(Operation("conflict", target_name, skill, link, detail="real file exists"))
            continue

        actual = link_target(link)
        if actual is not None and same_path(actual, source):
            operations.append(Operation("keep", target_name, skill, link, source))
            continue

        operations.append(Operation("replace", target_name, skill, link, source, "existing symbolic link"))

    for target in config.targets:
        if not target.path.is_dir():
            continue
        source_to_names: dict[str, list[str]] = {}
        for entry in target.path.iterdir():
            actual = link_target(entry)
            if actual is None:
                continue
            try:
                relative = actual.relative_to(config.source / "skills")
            except ValueError:
                continue
            if len(relative.parts) != 1:
                continue
            source_to_names.setdefault(relative.name, []).append(entry.name)
        for skill, names in source_to_names.items():
            canonical = target.path / skill
            extras = sorted(name for name in names if name != skill)
            for extra in extras:
                operations.append(
                    Operation(
                        "conflict",
                        target.name,
                        skill,
                        target.path / extra,
                        canonical,
                        "duplicate alias resolves to the same source skill",
                    )
                )

    order = {"conflict": 0, "remove": 1, "replace": 2, "create": 3, "keep": 4}
    operations.sort(key=lambda op: (order[op.action], op.target, op.skill, str(op.link)))
    return Plan(config=config, operations=tuple(operations))


def print_plan(plan: Plan) -> None:
    if not plan.operations:
        print("No configured links.")
        return
    for operation in plan.operations:
        print(operation.render())
    counts: dict[str, int] = {}
    for operation in plan.operations:
        counts[operation.action] = counts.get(operation.action, 0) + 1
    summary = ", ".join(f"{name}={counts[name]}" for name in sorted(counts))
    print(f"Summary: {summary}")


def _require_source(operation: Operation) -> Path:
    if operation.source is None:
        raise ConfigError(f"{operation.action} operation requires a source: {operation.link}")
    return operation.source


def apply_plan(plan: Plan) -> None:
    if plan.conflicts:
        raise ConfigError("refusing to mutate while conflicts exist")

    completed: list[Operation] = []
    try:
        for operation in plan.operations:
            if operation.action == "remove":
                operation.link.unlink()
            elif operation.action == "replace":
                source = _require_source(operation)
                if operation.link.is_symlink():
                    operation.link.unlink()
                else:
                    shutil.rmtree(operation.link)
                operation.link.symlink_to(source, target_is_directory=True)
            elif operation.action == "create":
                source = _require_source(operation)
                operation.link.parent.mkdir(parents=True, exist_ok=True)
                operation.link.symlink_to(source, target_is_directory=True)
            else:
                continue
            completed.append(operation)
    except OSError as exc:
        summary = ", ".join(f"{op.action}:{op.link}" for op in completed) or "none"
        raise ConfigError(f"filesystem operation failed: {exc}; completed operations: {summary}") from exc


def verify(config: Config, *, unlink_all: bool = False) -> None:
    plan = build_plan(config, unlink_all=unlink_all)
    remaining = [op for op in plan.operations if op.action == "conflict" or (not unlink_all and op.action not in {"keep"})]
    if remaining:
        rendered = "\n".join(op.render() for op in remaining)
        raise ConfigError(f"verification failed:\n{rendered}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("status", "check", "sync", "unlink"))
    parser.add_argument("--config", type=Path, default=REPO_ROOT / "config" / "skill-links.toml")
    parser.add_argument("--dry-run", action="store_true", help="print mutations without applying them")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        config = load_config(args.config.absolute())
        unlink_all = args.command == "unlink"
        plan = build_plan(config, unlink_all=unlink_all)
        print_plan(plan)

        if args.command == "status":
            return 0
        if args.command == "check":
            return 1 if any(op.action != "keep" for op in plan.operations) else 0
        if plan.conflicts:
            return 2
        if args.dry_run:
            return 0

        apply_plan(plan)
        verify(config, unlink_all=unlink_all)
        print("Verified final configured-link state.")
        return 0
    except ConfigError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
