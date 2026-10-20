#!/usr/bin/env python3
"""Classify PR changes and enforce the aggregate CI result without API limits."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

JOBS = ('website', 'support', 'corpus')


def classify(paths: list[str]) -> dict[str, bool]:
    # Workflow/action changes can alter any job. Run the full suite for these.
    infrastructure = any(p.startswith(('.github/workflows/', '.github/utils/')) for p in paths)
    support = infrastructure or any(
        p.startswith(('support-docs/', 'wiki/support-docs/articles/')) or p in {
            'wiki/index.md',
            'scripts/incremental_support_docs_wiki.py',
            'scripts/detect_changed_support_docs.py',
            'scripts/prepare_support_doc_artifacts.sh',
            'scripts/regenerate_support_docs_manifest.py',
        } for p in paths
    )
    return {
        'website': infrastructure or any(p.startswith(('website/', 'support-docs/')) for p in paths),
        'support': support,
        'corpus': support or any(p.startswith(('wiki/', 'scripts/', 'tests/')) for p in paths),
    }


def check_results(needs: dict) -> list[str]:
    errors = []
    changes = needs.get('changes', {})
    if changes.get('result') != 'success':
        errors.append('Change classification did not succeed')
    for job in JOBS:
        expected = changes.get('outputs', {}).get(job)
        result = needs.get(job, {}).get('result')
        if expected not in ('true', 'false'):
            errors.append(f'{job}: missing/invalid change classification')
        elif result != ('success' if expected == 'true' else 'skipped'):
            errors.append(f'{job}: expected {expected=}, got {result}')
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['classify', 'gate'])
    parser.add_argument('--base')
    parser.add_argument('--head')
    args = parser.parse_args()
    if args.command == 'gate':
        errors = check_results(json.loads(os.environ['CI_NEEDS']))
        if errors:
            raise SystemExit('\n'.join(errors))
        print('All required validations passed; unrelated jobs were skipped.')
        return
    if not args.base or not args.head:
        parser.error('classify requires --base and --head')
    # Include both sides of renames, and use the PR merge base for stacked PRs.
    changed = subprocess.check_output([
        'git', 'diff', '--name-only', '--no-renames', '-z',
        f'{args.base}...{args.head}', '--',
    ]).decode().split('\0')
    output = ''.join(f'{key}={str(value).lower()}\n' for key, value in classify(changed).items())
    print(output, end='')
    with Path(os.environ['GITHUB_OUTPUT']).open('a') as handle:
        handle.write(output)


if __name__ == '__main__':
    main()
