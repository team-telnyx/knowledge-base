---
title: Telnyx LiveKit
summary: Telnyx LiveKit is a managed platform for building, deploying, and scaling
  voice AI agents on Telnyx infrastructure. It combines the LiveKit agent framework
  with built-in SIP trunking, colocated GPU inference for STT/TTS/LLM, and automatic
  autoscaling — collapsing the voice AI stack into a single platform with one bill.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
- url: https://developers.telnyx.com/docs/livekit/build/index
- url: https://developers.telnyx.com/docs/livekit/compatibility
- url: https://developers.telnyx.com/docs/livekit/connect
- url: https://developers.telnyx.com/docs/livekit/deploy/configuration
- url: https://developers.telnyx.com/docs/livekit/deploy/index
- url: https://developers.telnyx.com/docs/livekit/deploy/management
- url: https://developers.telnyx.com/docs/livekit/deploy/secrets
- url: https://developers.telnyx.com/docs/livekit/index
- url: https://developers.telnyx.com/docs/livekit/limits
- url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
- url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
updated_at: 2026-06-11T10:35:15Z
---

# Telnyx LiveKit

*Part 2 of 3 — see also: [Part 1](telnyx-livekit--part-1.md), [Part 3](telnyx-livekit--part-3.md)*

Telnyx LiveKit is a managed platform for building, deploying, and scaling voice AI agents on Telnyx infrastructure. It combines the LiveKit agent framework with built-in SIP trunking, colocated GPU inference for STT/TTS/LLM, and automatic autoscaling — collapsing the voice AI stack into a single platform with one bill.

## Building Agents

### Install the plugin

```
pip install "telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin"
```

This is the Telnyx-maintained plugin, which includes the latest features and fixes ahead of the upstream `livekit-plugins-telnyx` PyPI package. We host our own release to iterate faster than the upstream cadence allows. ([Plugin source on GitHub](https://github.com/team-telnyx/telnyx-livekit-plugin))

### Write your agent

Create `agent.py`:

```python
import asyncio
from livekit.agents import Agent, AgentSession, JobContext, RoomInputOptions
from livekit.plugins import openai, silero, telnyx

class MyAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful voice assistant.")

    async def on_enter(self):
        self.session.generate_reply(
            instructions="Greet the caller and ask how you can help."
        )

async def entrypoint(ctx: JobContext):
    session = AgentSession(
        stt=telnyx.STT(
            transcription_engine="Deepgram",
            base_url="wss://api.telnyx.com/v2/speech-to-text/transcription",
        ),
        llm=openai.LLM.with_telnyx(model="zai-org/GLM-5.1-FP8"),
        tts=telnyx.TTS(
            voice="Telnyx.NaturalHD.astra",
            sample_rate=24000,
        ),
        vad=silero.VAD.load(),
    )

    await ctx.connect()
    await session.start(
        agent=MyAgent(),
        room=ctx.room,
        room_input_options=RoomInputOptions(),
    )

    disconnect_event = asyncio.Event()

    @ctx.room.on("disconnected")
    def on_disconnect(*args):
        disconnect_event.set()

    await disconnect_event.wait()
```

The only Telnyx-specific parts are the `stt`, `tts`, and `llm` — everything else is standard LiveKit.

### Add a requirements file

Create `requirements.txt`:

```
livekit-agents
livekit-plugins-openai
livekit-plugins-silero
telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin
```

### Swap models

The example above uses Telnyx-hosted defaults. Swap any component independently:

- **STT** — Deepgram, Nova-3, Nova-2, Flux → [Telnyx LiveKit Models - STT](telnyx-livekit-models-stt.md)
- **TTS** — Telnyx Natural HD, MiniMax, Rime, ElevenLabs (BYOK), Azure → [Telnyx LiveKit Models - TTS](telnyx-livekit-models-tts.md)
- **LLM** — GPT-4o-mini, Kimi-K2.6, Claude (BYOK) → [Telnyx LiveKit Models - LLM](telnyx-livekit-models-llm.md)

## Deploying Agents

`lk agent deploy` uploads your code, builds a container image on Telnyx's build service, and deploys the worker. Subsequent deploys roll out a new version.

### Create and deploy

```bash
# Register the agent (writes the agent ID to livekit.toml)
lk agent create .

# Deploy with secrets
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

### Check status and logs

```bash
lk agent list
lk agent logs --id <AGENT_ID>
lk agent logs --id <AGENT_ID> --log-type build   # build logs
```

### Rollback

```bash
lk agent rollback <AGENT_ID>
```

### Auto-injected variables

The platform injects these into your agent's environment at runtime — you don't need to set them manually:

- `LIVEKIT_URL`
- `LIVEKIT_API_KEY` — your Telnyx API key (used for both platform auth and model access)
- `LIVEKIT_API_SECRET`

`LIVEKIT_API_KEY` is your Telnyx API key. Telnyx can revoke it if needed, giving you a single credential to manage.

### Deployment configuration

Set `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` as environment variables. You also need a `livekit.toml` in your project directory:

```toml
[project]
subdomain = "nyc1"

[agent]
id = "<agent-id>"
```

`lk agent create` writes the agent ID to `livekit.toml`. Don't edit the `[agent]` section manually. If you clone an example repo, remove the `[agent]` section before running `lk agent create` so a fresh ID is generated.

For multi-agent projects, use the `--config` flag to point at different TOML files:

```bash
lk agent deploy . --config agent-a.toml
lk agent deploy . --config agent-b.toml
```

Use separate API keys for dev, staging, and production environments. Each key operates independently.

### Secrets management

Pass secrets when you deploy:

```bash
lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
```

Add or update secrets on a running agent:

```bash
lk agent update-secrets <agent-id> --secrets "OPENAI_API_KEY=<your-key>"
```

Secrets set via the CLI are encrypted at rest and injected at runtime. They cannot be retrieved after being set.

For local development, use a `.env.local` file:

```
TELNYX_API_KEY=your-key-here
LIVEKIT_URL=https://nyc1.livekit-telnyx.com
LIVEKIT_API_KEY=your-key
LIVEKIT_API_SECRET=your-secret
```

## Management and Access

All platform interaction is through the `lk` CLI and the [Telnyx Portal](https://portal.telnyx.com). There is no direct access to underlying infrastructure (no kubectl, no SSH).

### What Telnyx manages

- LiveKit SFU (media server)
- SIP service (built-in telephony)
- Agent container runtime and orchestration
- Autoscaling
- TLS/SSL termination and load balancing
- Health checks and rolling deploys

### What you control

| Capability | How |
|---|---|
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
- Log forwarding to third-party services (Datadog, Sentry, CloudWatch) is coming soon
