---
title: CI/CD
summary: Deploy Edge Compute functions automatically with CI/CD pipelines.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/deploy/index
    content_hash: e3538f5745d22e78d8ce999b1d51915d1e69f3bb27cca2e397bb7863af6aae53
updated_at: 2026-04-10T00:00:00Z
---

# CI/CD

Deploy Edge Compute functions automatically with CI/CD pipelines.

Automate your Edge Compute deployments with continuous integration and delivery pipelines. This guide covers integration with popular CI/CD platforms.

## Overview

The deployment workflow:

1. **Push code** to your repository
2. **CI runs tests** and builds your function
3. **Deploy to Telnyx** using the CLI
4. **Verify deployment** with health checks

## Authentication

CI/CD pipelines need a Telnyx API key to deploy functions. Create a deployment key in the [Telnyx Portal](https://portal.telnyx.com) with Edge Compute permissions.

> **Warning:** Store your API key as a secret in your CI/CD platform. Never commit API keys to your repository.

## GitHub Actions

Deploy on every push to `main`:

```yaml theme={null}
