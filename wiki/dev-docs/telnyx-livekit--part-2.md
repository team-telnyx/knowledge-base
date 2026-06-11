---
title: Telnyx LiveKit
summary: Telnyx LiveKit is a managed platform for building, deploying, and scaling
  voice AI agents on Telnyx infrastructure. It combines the LiveKit agent framework
  with built-in SIP trunking, colocated GPU inference for STT/TTS/LLM, and automatic
  autoscaling — collapsing the voice AI stack into a single platform with one bill.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
  content_hash: 562050b8d5fdf2d99199f841e1961cc03fc56ccb86847d7eba54813caac25818
- url: https://developers.telnyx.com/docs/livekit/build/index
  content_hash: 92796d9b98ce443a5da4f326451546f47053454df2a8cc0dd915b250b5b99e23
- url: https://developers.telnyx.com/docs/livekit/compatibility
  content_hash: bd35a5a936b53a502201d69456d718670eebf75d3618174239d207f3b36afff1
- url: https://developers.telnyx.com/docs/livekit/connect
  content_hash: d24764bd1616fbeda8910d52efa872444cff475e7856aa10651bf6a5a6bd0e16
- url: https://developers.telnyx.com/docs/livekit/deploy/configuration
  content_hash: 797c9f219444fa8b824f4e90623062a708003dafc04f6b05a076777b7140b3ad
- url: https://developers.telnyx.com/docs/livekit/deploy/index
  content_hash: 72ff72efab2f35776214a62ba465220ae36d5ff7291406a42860b32e94e480cf
- url: https://developers.telnyx.com/docs/livekit/deploy/management
  content_hash: 4eb1b7a2b5817de9fcd692e7fc3bcf0304ef75ea36615e220515b9de9b0a548b
- url: https://developers.telnyx.com/docs/livekit/deploy/secrets
  content_hash: 2597f80347b016f50c8255672c0124f7d1247d79cc6f28c2d7748a831c1dda93
- url: https://developers.telnyx.com/docs/livekit/index
  content_hash: b7e94750be216371a58fbe786c152745786650511a3e1015876958da4f78795f
- url: https://developers.telnyx.com/docs/livekit/limits
  content_hash: c2c8b617e59a313d5d92d1069a3a157439ff9799db77da96d220376db2e576bd
- url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
  content_hash: 5a955282223665b430dc7d6dff8e8fc84e1a3cf8ed86b2a2da44e5a5d2218058
- url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
  content_hash: d9ed98fdfc4c4af8e83e472c11fb446e88d6bd636a8c5500d5516c10eb22b0ed
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
