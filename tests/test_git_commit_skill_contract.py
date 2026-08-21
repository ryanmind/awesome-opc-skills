from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "git-commit" / "SKILL.md"
DEFAULTS = ROOT / "skills" / "git-commit" / "references" / "default-rules.md"
EXECUTION = ROOT / "skills" / "git-commit" / "references" / "commit-execution.md"


class GitCommitSkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.defaults = DEFAULTS.read_text(encoding="utf-8")
        cls.execution = EXECUTION.read_text(encoding="utf-8")

    def test_breaking_change_supports_subject_or_footer_marker(self) -> None:
        self.assertIn("`!` before `:` or a `BREAKING CHANGE:` footer", self.skill)
        self.assertIn("either form is valid, and both may be used", self.skill)
        self.assertIn("`BREAKING-CHANGE:` is a valid synonym", self.defaults)
        self.assertIn("BREAKING CHANGE: clients must migrate", self.defaults)

    def test_message_and_commit_modes_preserve_the_staging_boundary(self) -> None:
        self.assertIn("draft a message without changing Git state", self.skill)
        self.assertIn("create a commit from already staged changes", self.skill)
        self.assertIn("Do not stage files unless the user explicitly asks", self.skill)
        self.assertIn("use only the staged diff as message evidence", self.skill)
        self.assertIn("leave unstaged and untracked changes out", self.skill)

    def test_incompatible_repository_rules_and_split_intents_stop(self) -> None:
        self.assertIn(
            "incompatible message format, stop and report the conflict", self.skill
        )
        self.assertIn(
            "If the change has no dominant intent, recommend splitting", self.skill
        )
        self.assertIn("Never include unrelated user changes", self.skill)

    def test_sensitive_and_high_risk_git_operations_require_explicit_request(
        self,
    ) -> None:
        self.assertIn("Never expose secret values", self.skill)
        self.assertIn("Stop on unresolved conflicts or suspected secrets", self.skill)
        self.assertIn(
            "Do not create or switch branches, push, amend, rebase", self.skill
        )
        self.assertIn(
            "Do not amend, bypass hooks, disable signing, or use `--no-verify`",
            self.execution,
        )

    def test_commit_verification_checks_the_recorded_path_set(self) -> None:
        self.assertIn("Record the intended staged path set", self.execution)
        self.assertIn("Read the committed path set", self.execution)
        self.assertIn("committed paths match the recorded staged set", self.execution)


class GitCommitWorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        self.git("init")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "Test User")
        (self.repo / "README.md").write_text("base\n", encoding="utf-8")
        self.git("add", "README.md")
        self.git("commit", "-m", "chore: initialize repository")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def git(self, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=self.repo,
            check=check,
            text=True,
            capture_output=True,
        )

    def test_cached_diff_excludes_unstaged_and_untracked_changes(self) -> None:
        (self.repo / "staged.py").write_text("staged = True\n", encoding="utf-8")
        self.git("add", "staged.py")
        (self.repo / "README.md").write_text("unstaged\n", encoding="utf-8")
        (self.repo / "untracked.py").write_text("untracked = True\n", encoding="utf-8")

        self.assertEqual(
            self.git("diff", "--cached", "--name-only").stdout.splitlines(),
            ["staged.py"],
        )
        self.assertEqual(
            self.git("diff", "--name-only").stdout.splitlines(), ["README.md"]
        )
        self.assertIn("?? untracked.py", self.git("status", "--short").stdout)

    def test_empty_index_has_no_cached_diff(self) -> None:
        (self.repo / "README.md").write_text("changed\n", encoding="utf-8")

        self.assertEqual(self.git("diff", "--cached", "--name-only").stdout, "")
        self.assertEqual(
            self.git("diff", "--name-only").stdout.splitlines(), ["README.md"]
        )

    def test_rejected_hook_preserves_the_staged_path_set(self) -> None:
        (self.repo / "staged.py").write_text("staged = True\n", encoding="utf-8")
        self.git("add", "staged.py")
        before = self.git("diff", "--cached", "--name-only").stdout
        hook = self.repo / ".git" / "hooks" / "pre-commit"
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
        hook.chmod(0o755)

        result = self.git("commit", "-m", "feat: add staged module", check=False)

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.git("diff", "--cached", "--name-only").stdout, before)
        self.assertEqual(
            self.git("log", "-1", "--format=%s").stdout.strip(),
            "chore: initialize repository",
        )

    def test_successful_commit_matches_recorded_staged_paths(self) -> None:
        (self.repo / "staged.py").write_text("staged = True\n", encoding="utf-8")
        self.git("add", "staged.py")
        (self.repo / "untracked.py").write_text("untracked = True\n", encoding="utf-8")
        intended_paths = self.git("diff", "--cached", "--name-only").stdout.splitlines()

        self.git("commit", "-m", "feat: add staged module")

        committed_paths = self.git(
            "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"
        ).stdout.splitlines()
        self.assertEqual(committed_paths, intended_paths)
        self.assertIn("?? untracked.py", self.git("status", "--short").stdout)


if __name__ == "__main__":
    unittest.main()
