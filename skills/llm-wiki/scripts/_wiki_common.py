from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(os.environ.get("LLM_WIKI_ROOT", "~/llm-wiki")).expanduser()
IGNORED_PARTS = {".git", ".obsidian", ".claude"}


class UnsupportedContentError(ValueError):
    pass


def resolve_root(root: str | None) -> Path:
    candidate = Path(root).expanduser() if root else DEFAULT_ROOT
    return candidate.resolve()


def ensure_inside(root: Path, path: Path) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path escapes wiki root: {path}") from exc
    return resolved


def read_text(path: Path) -> str:
    data = path.read_bytes()
    if b"\x00" in data:
        raise UnsupportedContentError(f"unsupported non-text content: {path}")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise UnsupportedContentError(f"unsupported non-UTF-8 content: {path}") from exc


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return parse_yaml_subset(lines[1:index]), "\n".join(lines[index + 1 :])
    return {}, text


def parse_yaml_subset(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            index += 1
            continue
        key, raw_value = stripped.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if raw_value:
            data[key] = parse_value(raw_value)
            index += 1
            continue

        items: list[str] = []
        lookahead = index + 1
        while lookahead < len(lines):
            item = lines[lookahead]
            if item and not item.startswith((" ", "\t")):
                break
            item = item.strip()
            if item.startswith("- "):
                items.append(item[2:].strip().strip('"').strip("'"))
            lookahead += 1
        data[key] = items
        index = lookahead
    return data


def parse_value(value: str) -> Any:
    if value in {"true", "false"}:
        return value == "true"
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip('"').strip("'") for item in split_inline_list(inner)]
    return value.strip('"').strip("'")


def split_inline_list(value: str) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    quote: str | None = None
    for char in value:
        if char in {"'", '"'}:
            quote = None if quote == char else char if quote is None else quote
        if char == "," and quote is None:
            items.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    if current:
        items.append("".join(current).strip())
    return items


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def page_slug(root: Path, path: Path) -> str:
    relative = rel(root, path)
    return relative[:-3] if relative.endswith(".md") else relative


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not any(part in IGNORED_PARTS for part in path.parts)
    )


def formal_pages(root: Path) -> list[Path]:
    pages: list[Path] = []
    for base in ("domains", "entities"):
        base_path = root / base
        if base_path.exists():
            pages.extend(base_path.rglob("*.md"))
    workshop = root / "workshop"
    if workshop.exists():
        pages.extend(path / "README.md" for path in workshop.iterdir() if (path / "README.md").is_file())
    for name in ("index.md", "SCHEMA.md", "AGENTS.md", "_meta/topic-map.md"):
        path = root / name
        if path.is_file():
            pages.append(path)
    return sorted(set(ensure_inside(root, path) for path in pages if path.is_file()))


def raw_pages(root: Path) -> list[Path]:
    pages: list[Path] = []
    raw = root / "raw"
    if raw.exists():
        pages.extend(raw.rglob("*"))
    workshop = root / "workshop"
    if workshop.exists():
        for raw_dir in workshop.glob("*/raw"):
            pages.extend(raw_dir.rglob("*"))
    return sorted(
        ensure_inside(root, path)
        for path in pages
        if path.is_file() and not any(part in IGNORED_PARTS for part in path.parts)
    )


def iter_scope(root: Path, scope: str) -> list[Path]:
    if scope == "formal":
        return formal_pages(root)
    if scope == "raw":
        return raw_pages(root)
    if scope == "all":
        return sorted(set(formal_pages(root) + raw_pages(root)))
    raise ValueError(f"unknown scope: {scope}")


def wikilinks(text: str) -> list[str]:
    targets: list[str] = []
    for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            targets.append(target)
    return targets


def compact_page(root: Path, path: Path, text: str | None = None) -> dict[str, Any]:
    text = read_text(path) if text is None else text
    frontmatter, body = parse_frontmatter(text)
    title = frontmatter.get("title") or first_heading(body) or path.stem
    return {
        "path": rel(root, path),
        "slug": page_slug(root, path),
        "title": title,
        "type": frontmatter.get("type"),
        "tags": frontmatter.get("tags", []),
        "sources": frontmatter.get("sources", []),
        "confidence": frontmatter.get("confidence"),
        "contested": frontmatter.get("contested", False),
        "contradictions": frontmatter.get("contradictions", []),
    }


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def snippet(text: str, query: str, *, width: int = 220) -> str:
    collapsed = re.sub(r"\s+", " ", text).strip()
    if not collapsed:
        return ""
    if not query:
        return collapsed[:width]
    location = collapsed.lower().find(query.lower())
    if location < 0:
        for token in tokens(query):
            location = collapsed.lower().find(token)
            if location >= 0:
                break
    if location < 0:
        return collapsed[:width]
    start = max(0, location - width // 3)
    end = min(len(collapsed), start + width)
    prefix = "..." if start else ""
    suffix = "..." if end < len(collapsed) else ""
    return f"{prefix}{collapsed[start:end]}{suffix}"


def tokens(value: str) -> list[str]:
    return [token for token in re.split(r"[^\w\u4e00-\u9fff]+", value.lower()) if token]


def dump_json(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))
