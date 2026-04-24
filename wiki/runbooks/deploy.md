---
title: Deploy
summary: Deploy your LiveKit agent to Telnyx infrastructure.
sources:
  - url: https://developers.telnyx.com/docs/livekit/deploy/index
    content_hash: b82151088a8c9b1221bd6ac66faa033d06373c4d93afa34f178f3d94a5b5a09a
updated_at: 2026-04-10T00:00:00Z
---

# Deploy

Deploy your LiveKit agent to Telnyx infrastructure.

Same commands as LiveKit Cloud. `lk agent deploy` uploads your code, builds a container image on Telnyx's build service, and deploys the worker.

> **Note:** **First time deploying?** Complete [Quickstart — Step 1](../tutorial/quick-start.md#step-1-configure-the-cli) to configure your CLI and register with the platform.

## 1. Create your agent

```bash theme={null}
lk agent create .
```

Registers the agent and writes the agent ID to `livekit.toml`. Skip this if you've already created the agent.

## 2. Deploy

```bash theme={null}
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

Subsequent deploys roll out a new version.

## 3. Check status

```bash theme={null}
lk agent list
```

## 4. Tail logs

```bash theme={null}
lk agent logs --id 
```

For build logs:

```bash theme={null}
lk agent logs --id  --log-type build
```

## 5. Update secrets

Add or update secrets on a running agent:

```bash theme={null}
lk agent update-secrets  --secrets "OPENAI_API_KEY=<your-key>"
```

## 6. Rollback

```bash theme={null}
lk agent rollback 
```

## What gets auto-injected

The platform injects these into your agent's environment at runtime — you don't need to set them manually:

* `LIVEKIT_URL`
* `LIVEKIT_API_KEY` — your Telnyx API key
* `LIVEKIT_API_SECRET`

## More

* [Secrets](secrets-2.md) — Managing API keys and sensitive config
* [Configuration](configuration-2.md) — Regions, multi-agent projects, env vars
* [Management](management-access.md) — What Telnyx manages vs. what you control
