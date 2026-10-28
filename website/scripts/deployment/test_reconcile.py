import unittest
from reconcile import require_current


class ReconcileTests(unittest.TestCase):
    def test_current_release_is_allowed(self):
        require_current('new', 'new')

    def test_superseded_release_is_blocked(self):
        with self.assertRaisesRegex(RuntimeError, 'queued main deployment'):
            require_current('old', 'new')

    def test_explicit_rollback_is_exempt(self):
        require_current('old', 'new', rollback=True)
