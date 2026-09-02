from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.regenerate_support_docs_manifest import regenerate_manifest


class RegenerateSupportDocsManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.source_root = Path(self.temp_dir.name) / "support-docs"
        self.source_root.mkdir()
        (self.source_root / "z-last.md").write_text("# Last\n", encoding="utf-8")
        nested = self.source_root / "nested"
        nested.mkdir()
        (nested / "a-first.md").write_text("# First\n", encoding="utf-8")
        self.manifest_path = self.source_root / "_manifest.json"
        self.manifest_path.write_text(
            json.dumps(
                {
                    "scraped": "2026-07-08",
                    "pages_saved": 2,
                    "files": ["deleted.md", "z-last.md"],
                    "assets": ["_images/example.png", "_images/example.png"],
                },
                indent=2,
            ),
            encoding="utf-8",
        )

    def test_regenerates_sorted_file_inventory_and_preserves_snapshot_metadata(self):
        self.assertTrue(regenerate_manifest(self.source_root))

        manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["pages_saved"], 2)
        self.assertEqual(manifest["files"], ["nested/a-first.md", "z-last.md"])
        self.assertEqual(manifest["scraped"], "2026-07-08")
        self.assertEqual(
            manifest["assets"],
            ["_images/example.png", "_images/example.png"],
        )

    def test_check_reports_stale_manifest_without_rewriting(self):
        before = self.manifest_path.read_text(encoding="utf-8")

        self.assertTrue(regenerate_manifest(self.source_root, check=True))

        self.assertEqual(self.manifest_path.read_text(encoding="utf-8"), before)

    def test_reports_no_change_after_regeneration(self):
        regenerate_manifest(self.source_root)

        self.assertFalse(regenerate_manifest(self.source_root, check=True))


if __name__ == "__main__":
    unittest.main()
