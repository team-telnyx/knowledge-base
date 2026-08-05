---
title: Deploy LiveKit Agents on Telnyx
summary: Walks through deploying, configuring, and managing LiveKit agents on Telnyx,
  including the deploy workflow, environment variables, secrets handling, log access,
  and the split between platform-managed and user-controlled capabilities.
sources:
- url: https://developers.telnyx.com/docs/livekit/deploy/configuration
- url: https://developers.telnyx.com/docs/livekit/deploy/index
- url: https://developers.telnyx.com/docs/livekit/deploy/management
- url: https://developers.telnyx.com/docs/livekit/deploy/secrets
updated_at: 2026-08-05T13:47:41Z
---

# Deploy LiveKit Agents on Telnyx

Walks through deploying, configuring, and managing LiveKit agents on Telnyx, including the deploy workflow, environment variables, secrets handling, log access, and the split between platform-managed and user-controlled capabilities.

## Overview

Telnyx runs a managed LiveKit platform for hosting voice and realtime AI agents. Deployment uses the `lk` CLI, which uploads your code, builds a container image on Telnyx's build service, and deploys the worker. The same commands work as on LiveKit Cloud. If this is your first deploy, complete the CLI configuration step in the [Quickstart](quickstart.md) before continuing.

## Deploy workflow

The standard deploy flow has six steps:

1. **Create the agent** — `lk agent create .` registers the agent and writes the agent ID to `livekit.toml`. Skip this if the agent is already registered.
2. **Deploy** — `lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY`. Subsequent deploys roll out a new version.
3. **Check status** — `lk agent list`.
4. **Tail logs** — `lk agent logs --id <AGENT_ID>`. For build logs, add `--log-type build`.
5. **Update secrets** — `lk agent update-secrets <AGENT_ID> --secrets "OPENAI_API_KEY=<your-key>"`.
6. **Rollback** — `lk agent rollback <AGENT_ID>`.

## Configuration

### Regions

Deploy to the region closest to your users. See [Regions](regions.md) for all available endpoints.

### Environment variables and `livekit.toml`

Set `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` as environment variables. You also need a `livekit.toml` in your project directory that defines the subdomain and agent ID:

```toml
[project]
subdomain = "nyc1"

[agent]
id = "<agent-id>"
```

`lk agent create` writes the agent ID to `livekit.toml`. Do not edit the `[agent]` section manually. If you clone an example repo, remove the `[agent]` section before running `lk agent create` so a fresh ID is generated.

For multi-agent projects, use the `--config` flag to point at different TOML files:

```
lk agent deploy . --config agent-a.toml
lk agent deploy . --config agent-b.toml
```

### Multiple environments

Use separate API keys for dev, staging, and production environments. Each key operates independently.

## Secrets

### Setting secrets on deploy

Pass secrets when you deploy:

```
lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
```

To set additional secrets after deploy:

```
lk agent update-secrets <agent-id> --secrets "OPENAI_API_KEY=<your-key>"
```

### Updating secrets

Update secrets on a running agent at any time:

```
lk agent update-secrets <agent-id> --secrets "KEY=value"
```

### Auto-injected variables

The platform automatically injects these into your agent's environment at runtime — you do not need to set them manually:

- `LIVEKIT_URL`
- `LIVEKIT_API_KEY` — your Telnyx API key, used for both platform auth and model access
- `LIVEKIT_API_SECRET`

`LIVEKIT_API_KEY` is your Telnyx API key. Telnyx can revoke it if needed, giving you a single credential to manage.

### Local development

For local development, use a `.env.local` file:

```
TELNYX_API_KEY=your-key-here
LIVEKIT_URL=https://nyc1.livekit-telnyx.com
LIVEKIT_API_KEY=your-key
LIVEKIT_API_SECRET=your-secret
```

Secrets set via the CLI are encrypted at rest and injected at runtime. They cannot be retrieved after being set.

## Log access

Stream logs from your running agent:

```
lk agent logs <agent-id>
```

Log forwarding to third-party services (Datadog, Sentry, CloudWatch) is coming soon.

## Management and access

### Access model

All platform interaction is through the `lk` CLI and the [Telnyx Portal](https://portal.telnyx.com). There is no direct access to underlying infrastructure — no `kubectl`, no SSH.

### What Telnyx manages

- LiveKit SFU (media server)
- SIP service (built-in telephony)
- Agent container runtime and orchestration
- Autoscaling
- TLS/SSL termination and load balancing
- Health checks and rolling deploys

### What you control

| Capability | How |
| --- | --- |
| Agent code and Dockerfile | `lk agent deploy .` |
| Secrets | `lk agent deploy --secrets` / `lk agent update-secrets` |
| Rollback | `lk agent rollback` |
| Logs | `lk agent logs` |
| Phone numbers | Telnyx Portal |
| SIP connections | Telnyx Portal |
| Model selection | Telnyx plugin or BYOK |

### Current limitations

- No volume mounts or persistent storage
- No custom networking or network policies
- No privileged containers
- No custom domains
- No direct database access — use external services with secrets

See [Compatibility](compatibility.md) for the full list of supported and unsupported features.

## Related pages

- [Secrets](secrets.md) — Managing API keys and sensitive config
- [Configuration](configuration--part-1.md) — Regions, multi-agent projects, env vars
- [Management](management.md) — What Telnyx manages vs. what you control
