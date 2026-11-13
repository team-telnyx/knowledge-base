import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "gate", Path(__file__).resolve().parents[1] / "scripts/check_automerge_review.py"
)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class ReviewGateTests(unittest.TestCase):
    def setUp(self):
        self.pr = {
            "state": "open",
            "draft": False,
            "labels": [],
            "head": {"repo": {"full_name": "org/repo"}, "sha": "current"},
            "user": {"login": "bot", "type": "Bot"},
        }
        self.approval = {
            "id": 1,
            "user": {"login": "Owner"},
            "state": "APPROVED",
            "commit_id": "current",
        }

    def check(self, reviews=(), permission="none", owners=None):
        return gate.eligible(
            self.pr,
            reviews,
            {"owner"} if owners is None else owners,
            permission,
            "org/repo",
            "current",
            "no-auto-merge",
        )

    def test_bot_needs_owner_approval_even_with_write_access(self):
        self.assertFalse(self.check(permission="write"))
        self.assertTrue(self.check([self.approval]))

    def test_internal_human_preserves_automatic_route(self):
        self.pr["user"]["type"] = "User"
        self.assertTrue(self.check(permission="write"))
        self.assertFalse(self.check(permission="read"))
        self.assertTrue(self.check([self.approval], permission="read"))

    def test_non_owner_self_and_old_commit_approvals_rejected(self):
        for update in (
            {"user": {"login": "someone"}},
            {"commit_id": "old"},
            {"user": {"login": "bot"}},
        ):
            with self.subTest(update=update):
                self.assertFalse(
                    self.check([self.approval | update], owners={"owner", "bot"})
                )

    def test_comments_preserve_approval_but_dismissal_and_changes_replace_it(self):
        for state, expected in (
            ("COMMENTED", True),
            ("DISMISSED", False),
            ("CHANGES_REQUESTED", False),
        ):
            with self.subTest(state=state):
                later = self.approval | {"id": 2, "state": state}
                self.assertEqual(self.check([later, self.approval]), expected)

    def test_other_reviewers_changes_block_both_routes(self):
        request = self.approval | {
            "id": 2,
            "user": {"login": "reviewer"},
            "state": "CHANGES_REQUESTED",
        }
        self.assertFalse(self.check([self.approval, request]))
        self.pr["user"]["type"] = "User"
        self.assertFalse(self.check([request], permission="admin"))

    def test_later_approval_clears_request_for_changes(self):
        request = self.approval | {"state": "CHANGES_REQUESTED"}
        self.assertTrue(self.check([request, self.approval | {"id": 2}]))

    def test_forks_closed_drafts_holds_and_changed_heads_block_all_routes(self):
        original = copy.deepcopy(self.pr)
        for update in (
            {"state": "closed"},
            {"draft": True},
            {"labels": [{"name": "no-auto-merge"}]},
            {"head": {"repo": {"full_name": "outsider/repo"}, "sha": "current"}},
            {"head": {"repo": None, "sha": "current"}},
            {"head": {"repo": {"full_name": "org/repo"}, "sha": "new"}},
        ):
            with self.subTest(update=update):
                self.pr = original | update
                self.assertFalse(self.check([self.approval]))
                self.pr["user"] = {"login": "human", "type": "User"}
                self.assertFalse(self.check(permission="admin"))

    def test_codeowners_supports_only_single_global_user_rule(self):
        self.assertEqual(
            gate.global_owners("# owners\n* @Owner @Other # comment\n"),
            {"owner", "other"},
        )
        for content in (
            "",
            "*",
            "* @org/team",
            "* user@example.com",
            "docs/ @owner",
            "* @owner\nprivate/ @other",
            "* @owner\n* @other",
        ):
            with self.subTest(content=content):
                self.assertEqual(gate.global_owners(content), set())


if __name__ == "__main__":
    unittest.main()
