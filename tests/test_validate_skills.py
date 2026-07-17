from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import validate_skills


class ValidateSkillsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills" / "alpha"
        (self.skill / "agents").mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_package(self, frontmatter: str, interface: str) -> None:
        (self.skill / "SKILL.md").write_text(
            f"---\n{frontmatter}\n---\n\n# Alpha\n",
            encoding="utf-8",
        )
        (self.skill / "agents" / "openai.yaml").write_text(
            f"interface:\n{interface}\n",
            encoding="utf-8",
        )

    def validate(self) -> list[str]:
        with patch.object(validate_skills, "ROOT", self.root):
            return validate_skills.validate_skill(self.skill)

    def test_accepts_supported_optional_fields(self) -> None:
        self.write_package(
            "\n".join(
                [
                    "name: alpha",
                    "description: test skill",
                    "license: MIT",
                    "allowed-tools:",
                    "  - Read",
                    "metadata:",
                    "  owner: local",
                ]
            ),
            "\n".join(
                [
                    '  display_name: "Alpha"',
                    '  short_description: "A sufficiently long test description"',
                    '  default_prompt: "Use $alpha for this test."',
                    '  icon_small: "./assets/icon.png"',
                    '  brand_color: "#336699"',
                ]
            ),
        )
        self.assertEqual(self.validate(), [])

    def test_rejects_unknown_fields(self) -> None:
        self.write_package(
            "\n".join(
                [
                    "name: alpha",
                    "description: test skill",
                    "unknown-field: value",
                ]
            ),
            "\n".join(
                [
                    '  display_name: "Alpha"',
                    '  short_description: "A sufficiently long test description"',
                    '  default_prompt: "Use $alpha for this test."',
                    '  unknown_field: "value"',
                ]
            ),
        )
        errors = self.validate()
        self.assertTrue(any("unsupported frontmatter fields ['unknown-field']" in error for error in errors))
        self.assertTrue(any("unsupported interface fields ['unknown_field']" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
