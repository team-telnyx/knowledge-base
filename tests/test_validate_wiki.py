import tempfile
import unittest
from pathlib import Path
from scripts.validate_wiki import validate

HEADER = '---\ntitle: Example\n---\n\n# Example\n\n'


class WikiValidationTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        (self.root / 'index.md').write_text(HEADER + '- [Example](page.md) — Summary\n')
        (self.root / 'page.md').write_text(HEADER)

    def test_existing_contract_is_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_index_target(self):
        (self.root / 'page.md').unlink()
        self.assertIn('missing or out-of-corpus', '\n'.join(validate(self.root)))

    def test_unclosed_frontmatter_and_missing_heading(self):
        (self.root / 'page.md').write_text('---\ntitle: Example\nbody\n')
        self.assertEqual(len(validate(self.root)), 2)

    def test_external_index_links_allowed(self):
        (self.root / 'index.md').write_text(HEADER + '- [Example](https://example.com) — Summary\n')
        self.assertEqual(validate(self.root), [])

    def test_empty_corpus_and_missing_root_index_fail(self):
        (self.root / 'index.md').unlink()
        self.assertIn('missing flattened index', '\n'.join(validate(self.root)))
        (self.root / 'page.md').unlink()
        self.assertIn('no Markdown', '\n'.join(validate(self.root)))
