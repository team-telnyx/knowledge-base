import os
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import unittest

from scripts.detect_changed_support_docs import changed_support_docs


class GitChangesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.cwd = os.getcwd()
        os.chdir(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.com')

    def tearDown(self):
        os.chdir(self.cwd)
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git', *args], text=True).strip()

    def write(self, name, text='article'):
        path = Path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        return self.git('rev-parse', 'HEAD')

    def test_root_nested_initial_rename_modify_delete(self):
        self.write('support-docs/root.md')
        self.write('support-docs/nested/space name.md')
        first = self.commit()
        self.assertEqual(changed_support_docs('0' * 40, first), ['support-docs/nested/space name.md', 'support-docs/root.md'])
        self.git('mv', 'support-docs/root.md', 'support-docs/renamed.md')
        self.write('support-docs/nested/space name.md', 'changed')
        second = self.commit()
        self.assertEqual(changed_support_docs(first, second), ['support-docs/nested/space name.md', 'support-docs/renamed.md', 'support-docs/root.md'])
        Path('support-docs/renamed.md').unlink()
        third = self.commit()
        self.assertEqual(changed_support_docs(second, third), ['support-docs/renamed.md'])

    def test_merge_base_excludes_unrelated_base_changes(self):
        self.write('README', 'base')
        first = self.commit()
        self.git('checkout', '-qb', 'feature')
        self.write('support-docs/feature.md')
        head = self.commit()
        self.git('checkout', '-qb', 'base', first)
        self.write('support-docs/unrelated.md')
        base = self.commit()
        self.assertEqual(changed_support_docs(base, head, merge_base=True), ['support-docs/feature.md'])

    def test_shared_generation_stages_new_files_even_without_source_diff(self):
        self.write('support-docs/en--articles--123-new.md', '---\nsource_url: https://support.telnyx.com/en/articles/123-new\n---\n# New\n\nThis is a new article that must be detected as generated drift.\n')
        for name in ('regenerate_support_docs_manifest.py', 'incremental_support_docs_wiki.py', 'detect_changed_support_docs.py', 'prepare_support_doc_artifacts.sh'):
            Path('scripts').mkdir(exist_ok=True)
            shutil.copy(Path(self.cwd) / 'scripts' / name, Path('scripts') / name)
        self.write('support-docs/_manifest.json', '{}')
        subprocess.run([sys.executable, 'scripts/regenerate_support_docs_manifest.py'], check=True, capture_output=True)
        sha = self.commit()
        env = dict(os.environ, BASE_REF=sha, HEAD_REF=sha, PATH=str(Path(sys.executable).parent) + os.pathsep + os.environ['PATH'])
        subprocess.run(['bash', 'scripts/prepare_support_doc_artifacts.sh'], check=True, capture_output=True, env=env)
        self.assertIn('wiki/support-docs/articles/123-new.md', self.git('diff', '--cached', '--name-only'))
        self.assertEqual(self.git('diff', '--name-only'), '')
