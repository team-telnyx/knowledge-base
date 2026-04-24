---
title: Secrets
summary: Manage API keys and sensitive configuration for your agents.
sources:
  - url: https://developers.telnyx.com/docs/livekit/deploy/secrets
    content_hash: cbfb35d81fb933016a984b18cba7166b10705d84f5f6c97c6c16cfccefc877ff
updated_at: 2026-04-10T00:00:00Z
---

# Secrets

Manage API keys and sensitive configuration for your agents.

## Setting secrets on deploy

Pass secrets when you deploy:

```bash theme={null}
lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
```

To set additional secrets after deploy:

```bash theme={null}
lk agent update-secrets <agent-id> --secrets "OPENAI_API_KEY=<your-key>"
```

## Updating secrets

Update secrets on a running agent:

```bash theme={null}
lk agent update-secrets <agent-id> --secrets "KEY=value"
```

## Auto-injected variables

The platform automatically injects these into your agent's environment at runtime:

* `LIVEKIT_URL`
* `LIVEKIT_API_KEY` (your Telnyx API key — used for both platform auth and model access)
* `LIVEKIT_API_SECRET`

You don't need to set these manually. Note: `LIVEKIT_API_KEY` is your Telnyx API key. Telnyx can revoke it if needed, giving you a single credential to manage.

## Local development

For local development, use a `.env.local` file:

```bash theme={null}
TELNYX_API_KEY=your-key-here
LIVEKIT_URL=https://nyc1.livekit-telnyx.com
LIVEKIT_API_KEY=your-key
LIVEKIT_API_SECRET=your-secret
```

Secrets set via the CLI are encrypted at rest and injected at runtime. They cannot be retrieved after being set.


## Related Pages

- [Secrets](../runbooks/secrets.md)
- [Secrets](../runbooks/secrets-3.md)
