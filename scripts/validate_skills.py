#!/usr/bin/env python3
"""Validate the repository's Codex skill package contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
ALLOWED_ENTRIES = {"SKILL.md", "agents", "references", "scripts", "assets"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
QUOTED_FIELD_RE = re.compile(r'^\s{2}([a-z_]+):\s+"(.*)"\s*$')
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, ["missing opening YAML frontmatter delimiter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, ["missing closing YAML frontmatter delimiter"]

    fields: dict[str, str] = {}
    current: str | None = None
    for line in lines[1:end]:
        match = FIELD_RE.match(line)
        if match:
            current = match.group(1)
            raw_value = (match.group(2) or "").strip()
            if raw_value and raw_value not in {"|", "|-", ">", ">-"}:
                if not (
                    (raw_value.startswith('"') and raw_value.endswith('"'))
                    or (raw_value.startswith("'") and raw_value.endswith("'"))
                ) and ": " in raw_value:
                    errors.append(
                        f"plain scalar contains an unquoted colon: {raw_value!r}"
                    )
                fields[current] = raw_value.strip('"\'')
            else:
                fields[current] = ""
            continue
        if current and (line.startswith("  ") or not line.strip()):
            value = line.strip()
            if value and value not in {"|", "|-", ">", ">-"}:
                fields[current] = f"{fields[current]} {value}".strip()
            continue
        errors.append(f"unsupported frontmatter line: {line!r}")

    body = "\n".join(lines[end + 1 :])
    if "[TODO" in text or re.search(r"\bTODO:\s*(?:Complete|Replace|Add content)", text):
        errors.append("contains scaffold TODO content")
    if not body.strip():
        errors.append("SKILL.md body is empty")
    return fields, errors


def parse_openai_yaml(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "interface:":
        errors.append("must start with 'interface:'")
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if not line.strip():
            continue
        match = QUOTED_FIELD_RE.match(line)
        if not match:
            errors.append(f"unsupported or unquoted field: {line!r}")
            continue
        fields[match.group(1)] = match.group(2)
    return fields, errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    relative = skill_dir.relative_to(ROOT)
    name = skill_dir.name

    if not NAME_RE.fullmatch(name):
        errors.append(f"{relative}: invalid directory name")

    entries = {path.name for path in skill_dir.iterdir()}
    for entry in sorted(entries - ALLOWED_ENTRIES):
        errors.append(f"{relative}: unsupported top-level entry {entry!r}")

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{relative}: missing SKILL.md")
    else:
        fields, frontmatter_errors = parse_frontmatter(skill_file)
        errors.extend(f"{skill_file.relative_to(ROOT)}: {error}" for error in frontmatter_errors)
        if set(fields) != {"name", "description"}:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: frontmatter fields must be exactly name and description"
            )
        if fields.get("name") != name:
            errors.append(f"{skill_file.relative_to(ROOT)}: name must match directory {name!r}")
        if not fields.get("description", "").strip():
            errors.append(f"{skill_file.relative_to(ROOT)}: description is empty")

    openai_file = skill_dir / "agents" / "openai.yaml"
    if not openai_file.is_file():
        errors.append(f"{relative}: missing agents/openai.yaml")
    else:
        fields, yaml_errors = parse_openai_yaml(openai_file)
        errors.extend(f"{openai_file.relative_to(ROOT)}: {error}" for error in yaml_errors)
        required = {"display_name", "short_description", "default_prompt"}
        if set(fields) != required:
            errors.append(
                f"{openai_file.relative_to(ROOT)}: interface fields must be exactly {sorted(required)}"
            )
        short_description = fields.get("short_description", "")
        if short_description and not 25 <= len(short_description) <= 64:
            errors.append(
                f"{openai_file.relative_to(ROOT)}: short_description must be 25-64 characters"
            )
        if f"${name}" not in fields.get("default_prompt", ""):
            errors.append(
                f"{openai_file.relative_to(ROOT)}: default_prompt must mention ${name}"
            )

    for path in skill_dir.rglob("*"):
        if path.name == ".DS_Store" or path.name == "__pycache__" or path.suffix == ".pyc":
            errors.append(f"{path.relative_to(ROOT)}: generated file is not allowed")

    return errors


def validate_catalog(skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    for catalog_name in ("README.md", "README_zh-CN.md"):
        catalog_path = ROOT / catalog_name
        if not catalog_path.is_file():
            errors.append(f"missing catalog file: {catalog_name}")
            continue
        text = catalog_path.read_text(encoding="utf-8")
        for skill_name in sorted(skill_names):
            expected = f"skills/{skill_name}/SKILL.md"
            if expected not in text:
                errors.append(f"{catalog_name}: missing catalog entry for {skill_name}")
    return errors


def validate_markdown_links() -> list[str]:
    errors: list[str] = []
    external_docs = (ROOT / "docs").is_symlink()
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if external_docs and path.parent == ROOT and Path(target).parts[:1] == ("docs",):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: broken local link {match.group(1)!r}"
                )
    return errors


def main() -> int:
    errors: list[str] = []
    if not SKILLS_DIR.is_dir():
        print("ERROR: skills directory not found", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        errors.append("skills directory contains no skill packages")

    names: set[str] = set()
    for skill_dir in skill_dirs:
        if skill_dir.name in names:
            errors.append(f"duplicate skill directory: {skill_dir.name}")
        names.add(skill_dir.name)
        errors.extend(validate_skill(skill_dir))

    errors.extend(validate_catalog(names))
    errors.extend(validate_markdown_links())

    if errors:
        print(f"Skill validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skill package(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
