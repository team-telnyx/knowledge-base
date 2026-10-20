"""Prevent stale builds from mutating production; every main push queues a successor."""
import os
import subprocess


def require_current(selected, current, rollback=False):
    if not rollback and selected != current:
        raise RuntimeError(f"Selected release {selected} is superseded by main {current}; "
                           "the queued main deployment will reconcile production")


def main():
    selected = os.environ['RELEASE_SHA']
    current = subprocess.check_output(
        ['git', 'ls-remote', '--exit-code', 'origin', 'refs/heads/main'], text=True
    ).split()[0]
    require_current(selected, current)


if __name__ == '__main__':
    main()
