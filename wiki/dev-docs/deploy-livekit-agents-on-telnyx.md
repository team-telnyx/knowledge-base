---
title: Deploy LiveKit agents on Telnyx
summary: How to create, deploy, configure, and manage LiveKit agents on Telnyx using
  the lk CLI—covering regions, secrets, logs, platform responsibilities, limits, and
  common migration paths from LiveKit Cloud or self‑hosted.
sources:
- url: https://developers.telnyx.com/docs/livekit/deploy/index
  content_hash: d32b343965bda8534e3386a8e5d6a0c13a23c71f466558747732b24453de8579
- url: https://developers.telnyx.com/docs/livekit/deploy/configuration
  content_hash: 1f051fd4cdf5361f98469eefc718c94d01753428425c3fa0c2e1406ca7c27236
- url: https://developers.telnyx.com/docs/livekit/deploy/management
  content_hash: 2cbaf8265e8c398e17c46f380592ae1e18910bd663be3d8ee63f08157ed80d45
- url: https://developers.telnyx.com/docs/livekit/deploy/secrets
  content_hash: 33b75861fcaa7a27f8e6503be3adfcb3169df67524a32f0453bc2b2c0f73259f
- url: https://developers.telnyx.com/docs/livekit/observability/index
  content_hash: 2074acf7a88a66db39206420511de8db3f8bfcb3776915f30c8aaab7fca61863
- url: https://developers.telnyx.com/docs/livekit/limits
  content_hash: 4480afb13accbba05dd3a230d18e9ead342461a889389d4b6ad108e59880da31
- url: https://developers.telnyx.com/docs/livekit/regions
  content_hash: a986d3a894a03f86e5aca917b8e749a46348a82971b0b7e74dc6e4125292eebb
- url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
  content_hash: 14f97dae3e18d696ed9201a8f825a132b423bfdd292944d302e3275088307de3
- url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
  content_hash: f0d0755561332a2ae9ba731b20463ca820245cec9de19f3c8ade84edf059c7f0
updated_at: 2026-05-20T08:53:45Z
---

# Deploy LiveKit agents on Telnyx

How to create, deploy, configure, and manage LiveKit agents on Telnyx using the lk CLI—covering regions, secrets, logs, platform responsibilities, limits, and common migration paths from LiveKit Cloud or self‑hosted.

## Before you start
- Install and configure the lk CLI; see [Quick Start](quick-start.md) (Step 1) to register with the platform.
- You’ll interact via the lk CLI and the Telnyx Portal (no kubectl or SSH access).
- Have a Telnyx account and API key ready.

## Create and deploy an agent
1) Create/register the agent (writes the agent ID to livekit.toml):

```
lk agent create .
```

2) Deploy (builds an image on Telnyx and rolls out the worker):

```
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

- Subsequent deploys create new versions automatically.

## Check status and view logs
- List agents and versions:

```
lk agent list
```

- Stream runtime logs:

```
lk agent logs --id <AGENT_ID>
```

- View build logs:

```
lk agent logs --id <AGENT_ID> --log-type build
```

## Secrets management
- Set secrets at deploy:

```
lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
```

- Add or update secrets later (hot-update on running agents):

```
lk agent update-secrets <AGENT_ID> --secrets "KEY=value,OTHER=value2"
```

- Auto-injected at runtime (no need to set manually on the platform):
  - LIVEKIT_URL
  - LIVEKIT_API_KEY (your Telnyx API key; used for platform auth and model access)
  - LIVEKIT_API_SECRET

- Local development example (.env.local):

```
TELNYX_API_KEY=your-key-here
LIVEKIT_URL=https://nyc1.livekit-telnyx.com
LIVEKIT_API_KEY=your-key
LIVEKIT_API_SECRET=your-secret
```

Notes: Secrets are encrypted at rest and only injected at runtime; they cannot be retrieved after being set. See also [Secrets](secrets.md).

## Configuration: regions, environments, and livekit.toml
- Choose the closest region for lowest latency; see [Regions](regions.md). Common endpoints:
  - New York: https://nyc1.livekit-telnyx.com
  - San Francisco: https://sfo3.livekit-telnyx.com
  - Atlanta: https://atl1.livekit-telnyx.com
  - Sydney: https://syd1.livekit-telnyx.com

- livekit.toml (created/updated by lk agent create — don’t hand-edit [agent]):

```
[project]
subdomain = "nyc1"

[agent]
id = "<agent-id>"
```

- Multi-agent projects: point to different TOML files with --config:

```
lk agent deploy . --config agent-a.toml
lk agent deploy . --config agent-b.toml
```

- Multiple environments: use separate Telnyx API keys for dev/staging/prod; keys are independent.

See also [Configuration](configuration.md).

## Rollbacks and releases
- Roll back to the previous version:

```
lk agent rollback <AGENT_ID>
```

- You can also “roll back” environment changes by restoring prior environment variables and redeploying.

## Management model and responsibilities
- Telnyx manages: LiveKit SFU, SIP service, agent container runtime/orchestration, autoscaling, TLS/SSL termination and load balancing, health checks, and rolling deploys.
- You control: agent code and Dockerfile (lk agent deploy .), secrets (lk agent deploy --secrets / lk agent update-secrets), rollbacks (lk agent rollback), logs (lk agent logs), phone numbers and SIP connections (Telnyx Portal), and model selection (Telnyx plugins or BYO keys). See [Management & Access](management-access.md) and [Models](models.md).
- Current limitations:
  - No volume mounts or persistent storage
  - No custom networking or privileged containers
  - No custom domains
  - No direct database access (use external services via secrets)
  - Log forwarding to third-party tools is coming soon

## Observability and logs
- Real-time stdout/stderr via:

```
lk agent logs --id <AGENT_ID>
```

- Traces, metrics, and session debugging are planned; see [Observability](observability.md).

## Limits and quotas
- Build limits: 10-minute build timeout; 1 GB build context size
- Agent/session concurrency and telephony concurrency: contact Telnyx for quotas and increases

See [Limits](limits.md) for details.

## Regions and SIP endpoints
- Platform endpoints:
  - New York: https://nyc1.livekit-telnyx.com
  - San Francisco: https://sfo3.livekit-telnyx.com
  - Atlanta: https://atl1.livekit-telnyx.com
  - Sydney: https://syd1.livekit-telnyx.com

- SIP endpoints for telephony:
  - New York: nyc1.sip.livekit-telnyx.com
  - San Francisco: sfo3.sip.livekit-telnyx.com
  - Atlanta: atl1.sip.livekit-telnyx.com
  - Sydney: syd1.sip.livekit-telnyx.com

See [Telephony](telephony.md) for voice setup.

## Migrate from LiveKit Cloud
- Zero code changes; swap credentials and redeploy.
- What changes:
  - LIVEKIT_URL → regional endpoint (e.g., https://nyc1.livekit-telnyx.com)
  - LIVEKIT_API_KEY → Telnyx API key
  - LIVEKIT_API_SECRET → your LiveKit API secret (unchanged value, new platform)

- Steps:
  1) Create a Telnyx account and generate a Telnyx API key
  2) One-time platform registration:

```
curl -s -X POST "https://<region>.livekit-telnyx.com/provision" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-project",
    "api_key": "'$TELNYX_API_KEY'",
    "api_secret": "'$LIVEKIT_API_SECRET'"
  }'
```

  3) Update environment variables
  4) Deploy:

```
lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
```

  5) Verify connectivity: `lk room list`
  6) Optional: install Telnyx plugins for on-prem STT, TTS, LLM (see [Build](build.md) and [Models](models.md))
  7) Optional: buy a Telnyx number for built-in telephony (see [Telephony](telephony.md))

- Rollback: point env vars back to LiveKit Cloud and redeploy.

## Migrate from self-hosted
- Keep your agents; offload infra. Telnyx replaces: LiveKit SFU, SIP/Otel SIP, TURN/STUN, container orchestration and autoscaling, TLS/load balancing, and monitoring infra.
- What stays the same: your agent code, SDK usage, room management, and dispatch rules.
- Steps:
  1) Create a Telnyx account and generate a Telnyx API key
  2) One-time platform registration (same curl as above)
  3) Point your agent to a regional endpoint (e.g., https://nyc1.livekit-telnyx.com)
  4) Move secrets to the platform:

```
lk agent deploy . --secrets TELNYX_API_KEY=<your-key>,OTHER_SECRET=<value>
```

  5) Re-create dispatch rules on Telnyx
  6) Update SIP config to Telnyx SIP endpoints (see above)
  7) Verify: `lk room list`
  8) Decommission your self-hosted infra

- Benefits: no infra management, built-in SIP with no third-party fees, managed autoscaling, and ultra-low-latency AI models colocated with your agents.

## See also
- [Compatibility](compatibility.md)
- [Architecture](architecture.md)
- [Pricing](pricing.md)
- [Build](build.md)
- [Connect](connect.md)
