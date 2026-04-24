---
title: Versions & Deployments
summary: Manage function versions, rollbacks, and deployment strategies.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
    content_hash: 3121630acc5f4ba258cda0229648d1e60ec7ce56b0a73fb647066c0a1a64bae3
updated_at: 2026-04-10T00:00:00Z
---

# Versions & Deployments

Manage function versions, rollbacks, and deployment strategies.

  **Coming Soon** — Version history and rollback commands are planned for a future release.

Version management will let you track deployments, roll back to previous versions, and implement gradual rollout strategies.

## Current Deployment Model

Today, `telnyx-edge ship` deploys your function as an atomic update. Each deployment fully replaces the previous version.

## Current Rollback Strategy

Until rollback commands are available, use Git:

```bash theme={null}
