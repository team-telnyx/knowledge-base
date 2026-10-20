import contextlib
import io
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.incremental_support_docs_wiki import main


class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.cwd = os.getcwd()
        os.chdir(self.temp.name)
        Path('support-docs').mkdir()

    def tearDown(self):
        os.chdir(self.cwd)
        self.temp.cleanup()

    def source(self, name='en--articles--123-example.md', slug='123-example', timestamp=''):
        path = Path('support-docs') / name
        path.write_text(f'---\nsource_url: https://support.telnyx.com/en/articles/{slug}\n{timestamp}---\n# Example\n\nThis article provides enough information for a useful summary.\n')
        return path

    def run_generator(self, *paths, extra=()):
        args = ['generator', *extra]
        for path in paths:
            args.extend(['--changed-file', str(path)])
        with patch('sys.argv', args), contextlib.redirect_stdout(io.StringIO()):
            return main()

    def snapshot(self):
        return {str(p): p.read_bytes() for p in Path('wiki').rglob('*.md')}

    def test_repeatable_missing_or_invalid_timestamp_and_drift_exit(self):
        for timestamp in ('', 'updated_at: invalid\n'):
            path = self.source(timestamp=timestamp)
            # First run detects entirely new/untracked output.
            first = self.run_generator(path, extra=('--fail-on-drift',))
            if not timestamp:
                self.assertEqual(first, 2)
            before = self.snapshot()
            self.assertEqual(self.run_generator(path, extra=('--fail-on-drift',)), 0)
            self.assertEqual(before, self.snapshot())
            self.assertIn(b'updated_at: 1970-01-01T00:00:00Z', next(iter(before.values())))

    def test_delete_uses_source_path_and_preserves_synthesis(self):
        path = self.source()
        self.run_generator(path)
        synthesis = Path('wiki/support-docs/articles/synthesized.md')
        synthesis.write_text('# Preserve me\n')
        path.unlink()
        self.assertEqual(self.run_generator(path, extra=('--fail-on-drift',)), 2)
        self.assertFalse(Path('wiki/support-docs/articles/123-example.md').exists())
        self.assertNotIn('123-example.md', Path('wiki/index.md').read_text())
        self.assertTrue(synthesis.exists())

    def test_rename_and_url_slug_changes_remove_old_projection(self):
        old = self.source()
        self.run_generator(old)
        new = Path('support-docs/aaa-renamed.md')
        old.rename(new)
        self.run_generator(old, new)
        self.assertIn('support-docs/aaa-renamed.md', Path('wiki/support-docs/articles/123-example.md').read_text())
        self.source(name='aaa-renamed.md', slug='123-new-slug')
        self.run_generator(new)
        self.assertFalse(Path('wiki/support-docs/articles/123-example.md').exists())
        self.assertTrue(Path('wiki/support-docs/articles/123-new-slug.md').exists())
        self.assertNotIn('123-example.md', Path('wiki/index.md').read_text())

    def test_reconcile_backfills_sources_and_removes_owned_deletions(self):
        old = self.source()
        self.run_generator(old)
        self.source(name='never-projected.md', slug='456-never-projected')
        old.unlink()
        self.run_generator(extra=('--reconcile',))
        self.assertFalse(Path('wiki/support-docs/articles/123-example.md').exists())
        self.assertTrue(Path('wiki/support-docs/articles/456-never-projected.md').exists())

    def test_article_becomes_non_article(self):
        path = self.source()
        self.run_generator(path)
        path.write_text('# Collection\n')
        self.run_generator(path)
        self.assertFalse(Path('wiki/support-docs/articles/123-example.md').exists())

    def test_refuses_to_overwrite_synthesis(self):
        path = self.source()
        target = Path('wiki/support-docs/articles/123-example.md')
        target.parent.mkdir(parents=True)
        target.write_text('# Handwritten page\n')
        with self.assertRaisesRegex(ValueError, 'unowned page'):
            self.run_generator(path)
        self.assertEqual(target.read_text(), '# Handwritten page\n')
