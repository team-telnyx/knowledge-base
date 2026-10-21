#!/usr/bin/env bash
# Shared by the required PR check and post-merge/manual generation.
set -euo pipefail
changed_files=$(mktemp)
trap 'rm -f "$changed_files"' EXIT
args=(--base "${BASE_REF:-}" --head "${HEAD_REF:-HEAD}")
if [[ "${MERGE_BASE:-false}" == true ]]; then
  args+=(--merge-base)
fi
python scripts/detect_changed_support_docs.py "${args[@]}" > "$changed_files"
printf 'Changed support-doc markdown files: %s\n' "$(wc -l < "$changed_files" | tr -d ' ')"
cat "$changed_files"
python scripts/regenerate_support_docs_manifest.py
# Reconcile also catches previously missed source changes and generator changes.
python scripts/incremental_support_docs_wiki.py --reconcile --changed-files-file "$changed_files"
python - <<'PY'
from pathlib import Path
bad = []
for path in Path('wiki').rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        bad.append(f'{path}: missing frontmatter')
    if '\n# ' not in text:
        bad.append(f'{path}: missing H1')
if bad:
    raise SystemExit('\n'.join(bad))
PY
# Stage only generated artifacts, including new files. git diff alone misses them.
git add -- support-docs/_manifest.json wiki/index.md wiki/support-docs/articles
