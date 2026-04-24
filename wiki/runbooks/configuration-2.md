---
title: Configuration
summary: Configuration options for deploying agents on Telnyx.
sources:
  - url: https://developers.telnyx.com/docs/livekit/deploy/configuration
    content_hash: 3475ac0c21de23d11bf76b4d5f3a4f2ef0e64c38843498f63e19fa59ed98a9a9
updated_at: 2026-04-10T00:00:00Z
---

# Configuration

Configuration options for deploying agents on Telnyx.

## Regions

Deploy to the region closest to your users. See [Regions](regions.md) for all available endpoints.

## Environment variables and livekit.toml

Set `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` as environment variables. You also need a `livekit.toml` in your project directory that defines the subdomain and agent ID:

```toml theme={null}
[project]
subdomain = "nyc1"

[agent]
id = "<agent-id>"
```

> **Note:** `lk agent create` writes the agent ID to `livekit.toml`. Don't edit the `[agent]` section manually. If you clone an example repo, remove the `[agent]` section before running `lk agent create` so a fresh ID is generated.

For multi-agent projects, use the `--config` flag to point at different TOML files:

```bash theme={null}
lk agent deploy . --config agent-a.toml
lk agent deploy . --config agent-b.toml
```

## Multiple environments

Use separate API keys for dev, staging, and production environments. Each key operates independently.

## Log access

Stream logs from your running agent:

```bash theme={null}
lk agent logs <agent-id>
```

Log forwarding to third-party services (Datadog, Sentry, CloudWatch) is coming soon.


## Related Pages

- [Configuration](../runbooks/configuration.md)
- [Configuration](../runbooks/configuration-3.md)
- [AnchorSite Configuration](../runbooks/anchorsite-configuration.md)
