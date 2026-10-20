import tempfile
import unittest
from pathlib import Path
from scripts.monthly_llmwiki_refresh import (
    install_workspace, rebuild_root_index, remove_workspace_indexes,
    strip_content_hashlines,
)


class MonthlyRefreshTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def test_strip_only_volatile_hashes_and_preserve_prose(self):
        page = self.root / 'page.md'
        page.write_text('---\ncontent_hash: ' + 'a' * 64 + '\n---\n# Page\ncontent_hash: explanation\n')
        stats = strip_content_hashlines(self.root)
        self.assertEqual(stats['content_hash_lines_removed'], 1)
        self.assertEqual(page.read_text(), '---\n---\n# Page\ncontent_hash: explanation\n')
        self.assertEqual(strip_content_hashlines(self.root)['files_changed'], 0)

    def test_install_replaces_one_workspace_and_preserves_the_other(self):
        compiled = self.root / 'compiled'
        wiki = self.root / 'wiki'
        for directory in (compiled / 'support-docs', wiki / 'support-docs', wiki / 'dev-docs'):
            directory.mkdir(parents=True)
        (compiled / 'support-docs/new.md').write_text('new')
        (wiki / 'support-docs/old.md').write_text('old')
        (wiki / 'dev-docs/keep.md').write_text('keep')
        install_workspace('support-docs', compiled, wiki)
        self.assertFalse((wiki / 'support-docs/old.md').exists())
        self.assertEqual((wiki / 'support-docs/new.md').read_text(), 'new')
        self.assertEqual((wiki / 'dev-docs/keep.md').read_text(), 'keep')
        with self.assertRaises(FileNotFoundError):
            install_workspace('support-docs', self.root / 'missing', wiki)
        self.assertTrue((wiki / 'support-docs/new.md').exists())

    def test_flatten_both_workspaces_then_remove_only_workspace_indexes(self):
        for workspace, title in [('support-docs', 'Zulu'), ('dev-docs', 'Alpha')]:
            directory = self.root / workspace
            directory.mkdir()
            (directory / 'index.md').write_text(f'- [{title}](page.md) — Summary\n')
            (directory / 'page.md').write_text('page')
        stats = rebuild_root_index(self.root)
        self.assertEqual(stats['entry_count'], 2)
        text = (self.root / 'index.md').read_text()
        self.assertLess(text.index('[Alpha]'), text.index('[Zulu]'))
        self.assertIn('(dev-docs/page.md)', text)
        self.assertIn('(support-docs/page.md)', text)
        self.assertEqual(remove_workspace_indexes(self.root)['removed_count'], 2)
        self.assertTrue((self.root / 'index.md').exists())
        self.assertTrue((self.root / 'support-docs/page.md').exists())

    def test_monthly_replacement_restores_projections_without_followup_drift(self):
        import contextlib
        import io
        from unittest.mock import patch
        from scripts.incremental_support_docs_wiki import main as project_articles

        source = self.root / 'support-docs'
        source.mkdir()
        (source / 'one.md').write_text(
            '---\nsource_url: https://support.telnyx.com/en/articles/1-one\n'
            'updated_at: 2026-01-01T00:00:00Z\n---\n# One\n\nSource article text.\n'
        )
        wiki = self.root / 'wiki'
        compiled = self.root / 'compiled'
        workspace = compiled / 'support-docs'
        workspace.mkdir(parents=True)
        (workspace / 'index.md').write_text('- [Synthesis](synthesized.md) — Summary\n')
        (workspace / 'synthesized.md').write_text('---\ntitle: Synthesis\n---\n# Synthesis\n')
        old = wiki / 'support-docs/articles/stale.md'
        old.parent.mkdir(parents=True)
        old.write_text('old monthly workspace')

        install_workspace('support-docs', compiled, wiki)
        rebuild_root_index(wiki)
        remove_workspace_indexes(wiki)
        self.assertFalse(old.exists())
        args = ['incremental_support_docs_wiki.py', '--source-root', str(source),
                '--wiki-root', str(wiki), '--reconcile']
        with patch('sys.argv', args), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(project_articles(), 0)
        self.assertTrue((wiki / 'support-docs/articles/1-one.md').exists())
        self.assertTrue((wiki / 'support-docs/synthesized.md').exists())
        index = (wiki / 'index.md').read_text()
        self.assertIn('(support-docs/synthesized.md)', index)
        self.assertIn('(support-docs/articles/1-one.md)', index)
        with patch('sys.argv', args + ['--fail-on-drift']), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(project_articles(), 0)
        self.assertEqual((wiki / 'index.md').read_text(), index)
