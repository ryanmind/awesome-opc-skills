from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SEARCH = ROOT / "skills" / "llm-wiki" / "scripts" / "wiki_search.py"
PAGE = ROOT / "skills" / "llm-wiki" / "scripts" / "wiki_page.py"
SKILL_DIR = ROOT / "skills" / "llm-wiki"


class LlmWikiScriptTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.write_page(
            "domains/agent/concepts/agent-runtime.md",
            """---
title: Agent Runtime
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [ai, agent]
sources: [raw/runtime.md]
confidence: high
---

# Agent Runtime

Runtime content links to [[domains/agent/concepts/tool-calling]].
""",
        )
        self.write_page(
            "domains/agent/concepts/tool-calling.md",
            """---
title: Tool Calling
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [ai, agent]
sources: [raw/tools.md]
confidence: medium
---

# Tool Calling

Backlink target.
""",
        )
        self.write_page("raw/runtime.md", "# Raw runtime\n\nsource facts")
        self.write_page("index.md", "# Wiki Index\n\n- [[domains/agent/concepts/agent-runtime]]")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_page(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_bytes(self, relative: str, content: bytes) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def run_json(self, script: Path, *args: str) -> dict[str, Any]:
        completed = subprocess.run(
            [sys.executable, str(script), "--root", str(self.root), *args, "--json"],
            text=True,
            capture_output=True,
            check=True,
        )
        return json.loads(completed.stdout)

    def test_search_returns_compact_metadata(self) -> None:
        payload = self.run_json(SEARCH, "--query", "runtime", "--limit", "1")
        self.assertEqual(payload["count"], 1)
        result = payload["results"][0]
        self.assertEqual(result["slug"], "domains/agent/concepts/agent-runtime")
        self.assertEqual(result["confidence"], "high")
        self.assertIn("Runtime", result["snippet"])

    def test_page_reads_slug_and_backlinks(self) -> None:
        payload = self.run_json(
            PAGE,
            "domains/agent/concepts/tool-calling",
            "--max-chars",
            "10",
            "--with-backlinks",
        )
        self.assertEqual(payload["title"], "Tool Calling")
        self.assertEqual(payload["returned_chars"], 10)
        self.assertTrue(payload["truncated"])
        self.assertEqual(payload["backlinks"][0]["slug"], "domains/agent/concepts/agent-runtime")

    def test_raw_scope_reads_raw_source(self) -> None:
        payload = self.run_json(PAGE, "raw/runtime.md", "--scope", "raw", "--max-chars", "200")
        self.assertEqual(payload["path"], "raw/runtime.md")
        self.assertIn("source facts", payload["content"])

    def test_search_skips_binary_raw_sources(self) -> None:
        self.write_bytes("raw/source.pdf", b"%PDF-1.7\x00binary")
        payload = self.run_json(SEARCH, "--query", "runtime", "--scope", "raw")
        self.assertEqual(payload["skipped_unsupported"], 1)
        self.assertEqual(payload["results"][0]["path"], "raw/runtime.md")

    def test_page_rejects_binary_raw_source(self) -> None:
        self.write_bytes("raw/source.pdf", b"%PDF-1.7\x00binary")
        completed = subprocess.run(
            [
                sys.executable,
                str(PAGE),
                "--root",
                str(self.root),
                "raw/source.pdf",
                "--scope",
                "raw",
                "--json",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 2)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["error"], "unsupported content")
        self.assertEqual(payload["path"], "raw/source.pdf")

    def test_installed_script_does_not_create_bytecode_in_skill(self) -> None:
        installed_scripts = self.root / "installed-skill" / "scripts"
        shutil.copytree(
            SKILL_DIR / "scripts",
            installed_scripts,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        self.run_json(installed_scripts / "wiki_search.py", "--query", "runtime", "--limit", "1")
        generated = [
            path
            for path in installed_scripts.rglob("*")
            if path.name == "__pycache__" or path.suffix == ".pyc"
        ]
        self.assertEqual(generated, [])

    def test_documented_script_paths_are_skill_relative(self) -> None:
        docs = [
            SKILL_DIR / "SKILL.md",
            SKILL_DIR / "references" / "search-and-retrieve.md",
            SKILL_DIR / "references" / "maintenance.md",
        ]
        for path in docs:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("skills/llm-wiki/scripts", text)
            self.assertIn("$SKILL_DIR/scripts", text)


if __name__ == "__main__":
    unittest.main()
