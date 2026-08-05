---
title: CI/CD for Edge Compute
summary: How to deploy Telnyx Edge Compute functions from CI pipelines using the `telnyx-edge`
  CLI, with working examples for GitHub Actions, GitLab CI, and CircleCI, plus patterns
  for staging/production, rollback, smoke testing, and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/deploy/index
updated_at: 2026-08-05T13:40:22Z
---

# CI/CD for Edge Compute

*Part 1 of 2 — see also: [Part 2](ci-cd-for-edge-compute--part-2.md)*

How to deploy Telnyx Edge Compute functions from CI pipelines using the `telnyx-edge` CLI, with working examples for GitHub Actions, GitLab CI, and CircleCI, plus patterns for staging/production, rollback, smoke testing, and troubleshooting.

## Overview

Every Edge Compute deployment from CI follows the same three steps: install a pinned `telnyx-edge` binary, authenticate with `auth api-key set`, and run `ship`. This page provides those steps as working pipelines for GitHub Actions, GitLab CI, and CircleCI, plus patterns for staging/production and rollback.

## The three steps every pipeline runs

```bash
TELNYX_EDGE_VERSION=v0.2.3

# 1. Install — release assets are version-stamped and extract into a versioned directory
curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${TELNYX_EDGE_VERSION}/telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64.tar.gz" | tar xz
sudo mv "telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/

# 2. Authenticate — the CLI does NOT read $TELNYX_API_KEY from the environment
telnyx-edge auth api-key set "$TELNYX_API_KEY"

# 3. Deploy the function in the current directory (or --from-dir <path>)
telnyx-edge ship
```

Three facts these steps depend on:

- **The CLI ships as GitHub release binaries only** — it is not on npm and there is no package manager formula. There is also no un-versioned "latest" asset: `releases/latest/download/...` URLs return 404. Pin a version in a `TELNYX_EDGE_VERSION` variable so bumping is a one-line change. For arm64 runners, use the `linux-arm64` asset.
- **`telnyx-edge` does not read a `TELNYX_API_KEY` environment variable on its own.** Store your API key as a CI secret and run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` as a pipeline step — it persists the key to `~/.telnyx-edge/config.toml` for the rest of the job.
- **`ship` has no environment flag.** It deploys the function identified by `func.toml` in the shipped directory, and its flags are `--from-dir` and `--timeout` only. Staging and production are separate functions.

On success, `ship` prints the function's live URL (`https://{func-name}-{func-id-prefix}.telnyxcompute.com` — see [Routes & Domains](routes-domains.md)). The URL is stable across deploys.

## GitHub Actions

A complete workflow that tests on every push and deploys on pushes to `main`. Only the install, authenticate, and ship steps are Telnyx-specific — the test job is ordinary `npm` and assumes a committed lockfile and a `test` script (the scaffold ships neither); substitute your project's own checks.

```yaml
# .github/workflows/deploy.yml
name: Deploy Edge Function

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  TELNYX_EDGE_VERSION: v0.2.3

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'
      - run: npm ci
      - run: npm test

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install telnyx-edge
        run: |
          curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${TELNYX_EDGE_VERSION}/telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64.tar.gz" | tar xz
          sudo mv "telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/

      - name: Authenticate
        env:
          TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY }}
        run: telnyx-edge auth api-key set "$TELNYX_API_KEY"

      - name: Deploy
        run: telnyx-edge ship
```

Add the secret under **Settings → Secrets and variables → Actions → New repository secret**, named `TELNYX_API_KEY`.

## GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - deploy

variables:
  TELNYX_EDGE_VERSION: v0.2.3

deploy:
  stage: deploy
  image: ubuntu:24.04
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  before_script:
    - apt-get update -qq && apt-get install -y -qq curl ca-certificates
    - curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${TELNYX_EDGE_VERSION}/telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64.tar.gz" | tar xz
    - mv "telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/
    - telnyx-edge auth api-key set "$TELNYX_API_KEY"
  script:
    - telnyx-edge ship
```

Define `TELNYX_API_KEY` as a **masked** variable under **Settings → CI/CD → Variables**. The `ubuntu:24.04` image runs as root, so no `sudo` is needed.

## CircleCI

```yaml
# .circleci/config.yml
version: 2.1

jobs:
  deploy:
    docker:
      - image: cimg/base:current
    environment:
      TELNYX_EDGE_VERSION: v0.2.3
    steps:
      - checkout
      - run:
          name: Install telnyx-edge
          command: |
            curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${TELNYX_EDGE_VERSION}/telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64.tar.gz" | tar xz
            sudo mv "telnyx-edge-${TELNYX_EDGE_VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/
      - run:
          name: Authenticate
          command: telnyx-edge auth api-key set "$TELNYX_API_KEY"
      - run:
          name: Deploy
          command: telnyx-edge ship

workflows:
  deploy:
    jobs:
      - deploy:
          filters:
            branches:
              only: main
```

Set `TELNYX_API_KEY` as a project environment variable (**Project Settings → Environment Variables**) or in a context.
