---
title: Secrets
summary: Securely store and access sensitive data in Edge Compute functions.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
    content_hash: 3f6e1b4da0c3c48c1a9fdaca576b03adff598ec293f236c51845ad3e3aa191d9
updated_at: 2026-04-10T00:00:00Z
---

# Secrets

Securely store and access sensitive data in Edge Compute functions.

Secrets are encrypted key-value pairs for storing sensitive configuration data like API keys, database passwords, and authentication tokens.

## Background

Secrets provide secure storage that is:

* **Encrypted at rest** — Stored with AES-256 encryption
* **Encrypted in transit** — All API calls use HTTPS/TLS
* **Injected at runtime** — Available as environment variables in your functions
* **Organization-scoped** — Shared across all functions in your organization
* **Never displayed** — Secret values are never shown in CLI output or logs

## Adding Secrets

Use the CLI to store sensitive data:

```bash theme={null}


## Related Pages

- [Secrets](../runbooks/secrets-2.md)
- [Secrets](../runbooks/secrets-3.md)
