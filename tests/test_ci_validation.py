import unittest
from scripts.ci_validation import JOBS, check_results, classify


class CIValidationTests(unittest.TestCase):
    def test_path_coverage(self):
        cases = {
            'README.md': (False, False, False),
            'website/scripts/deployment/release.py': (True, False, False),
            'support-docs/article.md': (True, True, True),
            'support-docs/nested/article.md': (True, True, True),
            'wiki/index.md': (False, True, True),
            'wiki/support-docs/articles/article.md': (False, True, True),
            'wiki/support-docs/synthesized.md': (False, False, True),
            'scripts/monthly_llmwiki_refresh.py': (False, False, True),
            'tests/test_monthly_llmwiki_refresh.py': (False, False, True),
            'scripts/prepare_support_doc_artifacts.sh': (False, True, True),
            'scripts/detect_changed_support_docs.py': (False, True, True),
            'scripts/ci_validation.py': (False, False, True),
            '.github/utils/setup-runner/action.yaml': (True, True, True),
            '.github/workflows/deploy-website.yml': (True, True, True),
        }
        for path, expected in cases.items():
            with self.subTest(path=path):
                self.assertEqual(tuple(classify([path]).values()), expected)

    def needs(self, expected):
        return {
            'changes': {'result': 'success', 'outputs': {j: expected for j in JOBS}},
            **{j: {'result': 'success' if expected == 'true' else 'skipped'} for j in JOBS},
        }

    def test_applicable_success_and_unrelated_skips(self):
        for expected in ('true', 'false'):
            self.assertEqual(check_results(self.needs(expected)), [])

    def test_required_failure_cancellation_or_skip_fails(self):
        for result in ('failure', 'cancelled', 'skipped', None):
            needs = self.needs('true')
            needs['website']['result'] = result
            self.assertTrue(check_results(needs))

    def test_failed_or_missing_classification_fails_closed(self):
        needs = self.needs('false')
        needs['changes']['result'] = 'failure'
        self.assertTrue(check_results(needs))
        self.assertTrue(check_results({}))
        needs = self.needs('false')
        del needs['changes']['outputs']['corpus']
        self.assertTrue(check_results(needs))


class ChangedPathsIntegrationTests(unittest.TestCase):
    def test_stacked_branch_uses_merge_base_and_classifies_both_rename_paths(self):
        import os
        import subprocess
        import sys
        import tempfile
        from pathlib import Path
        script = Path(__file__).resolve().parents[1] / 'scripts/ci_validation.py'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.check_output(['git', '-C', directory, *args], stderr=subprocess.DEVNULL).decode().strip()
            git('init', '-b', 'main')
            git('config', 'user.email', 'test@example.com')
            git('config', 'user.name', 'Test')
            (root / 'support-docs').mkdir()
            (root / 'support-docs/article.md').write_text('article')
            git('add', '.')
            git('commit', '-m', 'base')
            git('checkout', '-b', 'feature')
            git('mv', 'support-docs/article.md', 'article.md')
            git('commit', '-m', 'move out of support')
            head = git('rev-parse', 'HEAD')
            git('checkout', 'main')
            (root / 'wiki').mkdir()
            (root / 'wiki/unrelated.md').write_text('base-only change')
            git('add', '.')
            git('commit', '-m', 'advance base')
            base = git('rev-parse', 'HEAD')
            output = root / 'outputs'
            subprocess.run([sys.executable, str(script), 'classify', '--base', base, '--head', head],
                           cwd=root, env={**os.environ, 'GITHUB_OUTPUT': str(output)},
                           check=True, capture_output=True)
            self.assertEqual(output.read_text(), 'website=true\nsupport=true\ncorpus=true\n')
            git('checkout', 'feature')
            git('mv', 'article.md', 'README.md')
            git('commit', '-m', 'rename unrelated file')
            output.write_text('')
            subprocess.run([sys.executable, str(script), 'classify', '--base', head, '--head', 'HEAD'],
                           cwd=root, env={**os.environ, 'GITHUB_OUTPUT': str(output)},
                           check=True, capture_output=True)
            self.assertEqual(output.read_text(), 'website=false\nsupport=false\ncorpus=false\n')
