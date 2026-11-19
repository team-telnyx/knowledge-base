"""Download data from a successful main-branch release; never execute archived code."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


def select(run, destination=Path('website')):
    repo = 'team-telnyx/knowledge-base'
    if not run.isdigit():
        raise ValueError('Rollback run ID must be numeric')
    metadata = json.loads(subprocess.check_output(['gh', 'api', f'repos/{repo}/actions/runs/{run}']))
    if metadata['head_branch'] != 'main' or metadata['conclusion'] != 'success' or metadata['path'] != '.github/workflows/deploy-website.yml':
        raise ValueError('Rollback requires a successful main deployment from this workflow')
    with tempfile.TemporaryDirectory() as directory:
        subprocess.run(['gh', 'run', 'download', run, '--repo', repo, '--name', f'support-site-release-{run}', '--dir', directory], check=True)
        downloaded = Path(directory)
        success = json.loads((downloaded / 'release-report/success.json').read_text())
        if success['mode'] != 'release-verified':
            raise ValueError('Cannot roll back to an unverified/bootstrap release')
        # Legacy releases built their event SHA; reconciled releases report the
        # actual source SHA, including releases which themselves were rollbacks.
        source_sha = success.get('source_sha', metadata['head_sha'])
        if not isinstance(source_sha, str) or not re.fullmatch('[0-9a-f]{40}', source_sha):
            raise ValueError('Invalid release source SHA')
        for name in ['dist', 'dist-edge']:
            source = downloaded / name
            if not source.is_dir() or source.is_symlink() or any(p.is_symlink() for p in source.rglob('*')):
                raise ValueError('Invalid release artifact')
        # These directories are consumed unconditionally by upload_content.
        # The current production build populates each (including images/downloads).
        for name in ['assets', '_images', 'downloads', 'content', 'en']:
            if not (downloaded / 'dist' / name).is_dir():
                raise ValueError('Incomplete release artifact: missing directory ' + name)
        for name in ['index.html', '404.html', 'content/search-index.json']:
            if not (downloaded / 'dist' / name).is_file():
                raise ValueError('Incomplete release artifact: missing file ' + name)
        # Validate generated data before replacing anything or acquiring AWS credentials.
        from release import validate_registry
        validate_registry(json.loads((downloaded / 'dist-edge/routes.json').read_text()), downloaded / 'dist')
        for name in ['dist', 'dist-edge']:
            target = destination / name
            shutil.rmtree(target, ignore_errors=True)
            shutil.copytree(downloaded / name, target)
        return source_sha


if __name__ == '__main__':
    source_sha = select(os.environ['ROLLBACK_RUN_ID'])
    with open(os.environ['GITHUB_ENV'], 'a') as env:
        env.write(f'ROLLBACK_SOURCE_SHA={source_sha}\n')
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
        summary.write(f'\nRollback artifact source revision: `{source_sha}`\n')
