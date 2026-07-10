from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from scripts.manage_skill_links import ConfigError, apply_plan, build_plan, load_config, load_state, verify


class SkillLinkManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.target = self.root / "target"
        self.state = self.root / "state" / "links.json"
        self.config_path = self.root / "skill-links.toml"
        self.create_skill("alpha")
        self.create_skill("beta")
        self.write_config(["alpha"])

    def tearDown(self) -> None:
        self.temp.cleanup()

    def create_skill(self, name: str) -> None:
        skill = self.source / "skills" / name
        skill.mkdir(parents=True, exist_ok=True)
        (skill / "SKILL.md").write_text(f"---\nname: {name}\ndescription: test\n---\n", encoding="utf-8")

    def write_config(self, skills: list[str], *, source: Path | None = None) -> None:
        source = source or self.source
        quoted = ", ".join(json.dumps(skill) for skill in skills)
        self.config_path.write_text(
            "\n".join(
                [
                    "version = 1",
                    "",
                    "[distribution]",
                    f"source = {json.dumps(str(source))}",
                    f"state = {json.dumps(str(self.state))}",
                    "",
                    "[targets.test]",
                    f"path = {json.dumps(str(self.target))}",
                    f"skills = [{quoted}]",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    def sync(self) -> None:
        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state))
        apply_plan(plan)
        verify(config, load_state(config.state))

    def test_creates_links_and_second_sync_is_noop(self) -> None:
        self.sync()
        link = self.target / "alpha"
        self.assertTrue(link.is_symlink())
        self.assertEqual(Path(os.readlink(link)), self.source / "skills" / "alpha")

        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state))
        self.assertFalse(plan.changes)
        self.assertEqual([op.action for op in plan.operations], ["keep"])

    def test_rejects_duplicate_config_entries(self) -> None:
        self.write_config(["alpha", "alpha"])
        with self.assertRaisesRegex(ConfigError, "duplicates"):
            load_config(self.config_path)

    def test_replaces_existing_directory(self) -> None:
        (self.target / "alpha").mkdir(parents=True)
        (self.target / "alpha" / "old.txt").write_text("old", encoding="utf-8")
        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state))
        self.assertEqual([op.action for op in plan.changes], ["replace"])
        apply_plan(plan)
        self.assertTrue((self.target / "alpha").is_symlink())
        self.assertEqual(Path(os.readlink(self.target / "alpha")), self.source / "skills" / "alpha")

    def test_real_file_is_conflict(self) -> None:
        self.target.mkdir(parents=True)
        (self.target / "alpha").write_text("old", encoding="utf-8")
        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state))
        self.assertEqual(plan.conflicts[0].detail, "real file exists")

    def test_external_link_is_conflict(self) -> None:
        self.target.mkdir(parents=True)
        (self.target / "alpha").symlink_to(self.root / "external", target_is_directory=True)
        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state))
        self.assertEqual(plan.conflicts[0].detail, "unmanaged symbolic link exists")

    def test_removes_deselected_managed_link(self) -> None:
        self.sync()
        self.write_config([])
        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state))
        self.assertEqual([op.action for op in plan.changes], ["remove"])
        apply_plan(plan)
        self.assertFalse(os.path.lexists(self.target / "alpha"))

    def test_repairs_link_after_source_moves(self) -> None:
        self.sync()
        moved = self.root / "moved source"
        self.source.rename(moved)
        self.write_config(["alpha"], source=moved)

        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state))
        self.assertEqual([op.action for op in plan.changes], ["update"])
        apply_plan(plan)
        verify(config, load_state(config.state))
        self.assertEqual(Path(os.readlink(self.target / "alpha")), moved / "skills" / "alpha")

    def test_reports_duplicate_alias(self) -> None:
        self.sync()
        (self.target / "alias").symlink_to(self.source / "skills" / "alpha", target_is_directory=True)
        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state))
        self.assertTrue(any("duplicate alias" in op.detail for op in plan.conflicts))

    def test_unlink_only_removes_recorded_links(self) -> None:
        self.sync()
        external = self.target / "external"
        external.symlink_to(self.root / "elsewhere", target_is_directory=True)
        config = load_config(self.config_path)
        plan = build_plan(config, load_state(config.state), unlink_all=True)
        apply_plan(plan, unlink_all=True)
        self.assertFalse(os.path.lexists(self.target / "alpha"))
        self.assertTrue(external.is_symlink())


if __name__ == "__main__":
    unittest.main()
