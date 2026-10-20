import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('select_rollback', Path(__file__).with_name('select-rollback.py'))
rollback = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rollback)


class RollbackTests(unittest.TestCase):
    def download(self, args, **kwargs):
        root = Path(args[-1])
        page = root / 'dist/en/articles/1-one'
        page.parent.mkdir(parents=True)
        page.write_text('<h1>Archived release</h1>')
        (root / 'dist-edge').mkdir()
        (root / 'dist-edge/routes.json').write_text(json.dumps({'article:1': '/en/articles/1-one'}))
        (root / 'release-report').mkdir()
        (root / 'release-report/success.json').write_text(json.dumps(self.success))

    def setUp(self):
        self.metadata = {'head_branch': 'main', 'conclusion': 'success', 'path': '.github/workflows/deploy-website.yml', 'head_sha': 'a' * 40}
        self.success = {'mode': 'release-verified', 'source_sha': 'b' * 40}

    def test_uses_artifact_source_not_event_sha_and_only_downloads_data(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(rollback.subprocess, 'check_output', return_value=json.dumps(self.metadata)), patch.object(rollback.subprocess, 'run', side_effect=self.download) as run:
            self.assertEqual(rollback.select('123', Path(temp)), 'b' * 40)
            self.assertEqual(run.call_count, 1)
            self.assertEqual(run.call_args.args[0][:3], ['gh', 'run', 'download'])
            self.assertTrue((Path(temp) / 'dist/en/articles/1-one').is_file())

    def test_legacy_release_falls_back_to_event_sha(self):
        self.success.pop('source_sha')
        with tempfile.TemporaryDirectory() as temp, patch.object(rollback.subprocess, 'check_output', return_value=json.dumps(self.metadata)), patch.object(rollback.subprocess, 'run', side_effect=self.download):
            self.assertEqual(rollback.select('123', Path(temp)), 'a' * 40)

    def test_unverified_or_corrupt_download_does_not_replace_existing_content(self):
        for corrupt in [False, True]:
            with self.subTest(corrupt=corrupt), tempfile.TemporaryDirectory() as temp:
                target = Path(temp)
                (target / 'dist').mkdir()
                marker = target / 'dist/existing'
                marker.write_text('current')
                def download(args, **kwargs):
                    self.download(args, **kwargs)
                    root = Path(args[-1])
                    if corrupt:
                        (root / 'dist-edge/routes.json').write_text('{}')
                    else:
                        (root / 'release-report/success.json').write_text('{"mode":"bootstrap-ready-for-infra-activation"}')
                with patch.object(rollback.subprocess, 'check_output', return_value=json.dumps(self.metadata)), patch.object(rollback.subprocess, 'run', side_effect=download), self.assertRaises(ValueError):
                    rollback.select('123', target)
                self.assertEqual(marker.read_text(), 'current')

    def test_wrong_branch_or_failed_run_is_rejected_before_download(self):
        for field, value in [('head_branch', 'feature'), ('conclusion', 'failure')]:
            metadata = {**self.metadata, field: value}
            with patch.object(rollback.subprocess, 'check_output', return_value=json.dumps(metadata)), patch.object(rollback.subprocess, 'run') as run, self.assertRaises(ValueError):
                rollback.select('123')
            run.assert_not_called()
