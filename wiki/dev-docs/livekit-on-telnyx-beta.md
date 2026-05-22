---
title: LiveKit on Telnyx (Beta)
summary: Run the same LiveKit you know on Telnyx’s global network with built‑in telephony
  and colocated AI (STT, TTS, LLM). Migrate by swapping URL and credentials, then
  build, deploy, and scale ultra‑low‑latency voice agents on one platform and one
  bill.
sources:
- url: https://developers.telnyx.com/docs/livekit/index
  content_hash: 88539f42175f2db98ef06414a856563b31035a4554b3ea3f0c9063d9ad79f0c8
- url: https://developers.telnyx.com/docs/livekit/architecture
  content_hash: 00e8b3ec6ccc6d81ee755dbe314771bf0f108af424121f5e3bd2277c81ae0f66
- url: https://developers.telnyx.com/docs/livekit/quickstart
  content_hash: d55cc000e2b4b332ab4ec4c20963b94f30ac0a96cdfafa8d238628a3c438ed50
- url: https://developers.telnyx.com/docs/livekit/build/index
  content_hash: 2fb855ef8c482e56f5633e903eae0766fb15d6f9caca24645bba46da69548751
- url: https://developers.telnyx.com/docs/livekit/compatibility
  content_hash: d75082d3fd4cab5b9b4f4ddb4123494729889559f0729f4369618d3d11b8b973
- url: https://developers.telnyx.com/docs/livekit/connect
  content_hash: 3fe29ca1f745f16a388682a72321790e6f09e1904e90c076592764842b733856
updated_at: 2026-05-20T08:50:16Z
---

# LiveKit on Telnyx (Beta)

Run the same LiveKit you know on Telnyx’s global network with built‑in telephony and colocated AI (STT, TTS, LLM). Migrate by swapping URL and credentials, then build, deploy, and scale ultra‑low‑latency voice agents on one platform and one bill.

## Key benefits
- Built-in telephony, no third‑party SIP fees — Telnyx is the carrier. Buy numbers, configure SIP, and connect agents in one portal.
- Ultra‑low‑latency AI — STT, TTS, and LLM run on Telnyx GPUs, colocated ~2 ms from your agents.
- Same LiveKit, zero migration risk — same SDKs, CLI, and agent framework; just swap three env vars.
- One platform, one bill — compute, models, telephony, and numbers consolidated with Telnyx.

## Compatibility at a glance
- What’s the same
  - The LiveKit agent framework and APIs work unchanged. See external references: agents, SIP/phone, API, cloud, and egress at docs.livekit.io (e.g., https://docs.livekit.io/agents, https://docs.livekit.io/sip).
- What’s different
  - STT/TTS/LLM: Telnyx‑hosted models available out of the box via the Telnyx plugin; or bring your own keys.
  - SIP trunking: on‑net with Telnyx (no external SIP fees). BYOT supported if you prefer your provider.
  - HD Voice: G.722 (16 kHz) enabled by default; Opus (48 kHz) available with SRTP. See [Telephony](telephony.md).
  - Phone numbers: Telnyx numbers in 140+ countries (vs. LiveKit Phone US‑only).
  - Deployment: same lk commands; point to a Telnyx region URL.
- Not supported today
  - Ingress (RTMP/WHIP), Sandbox environments.
- Coming soon (subject to change)
  - Egress/recording, observability (session timelines, transcripts, audio), agent tooling (Playground/Builder), security & compliance (E2EE, SSO, RBAC, HIPAA), enterprise SIP features (transfers), enhanced noise cancellation.

## Platform architecture
- Agents
  - Each deploy is an isolated worker under your account; rooms, SIP trunks, and dispatch rules are tenant‑scoped.
- Autoscaling
  - The platform scales workers up/down automatically based on active room load; unhealthy containers are replaced with rolling deploys.
- Inbound call flow
```
Caller → PSTN → Telnyx SIP → LiveKit SIP Bridge → Room → Agent Worker
```
  - Telnyx is both carrier and platform, so the SIP leg is on‑net (no third‑party hop).
- AI inference
```
Agent ── ~2 ms ──▶ Telnyx STT / TTS / LLM (colocated GPUs)
```
  - You can also route to external providers via BYOK.
- Regions
  - Each region runs the full stack: SFU, SIP, agent runtime, and AI inference. See [Regions](regions.md).

## Regions and endpoints
- Control plane URL pattern: https://<region>.livekit-telnyx.com
- SIP FQDN pattern: <region>.sip.livekit-telnyx.com
- Available regions today: nyc1 (New York), sfo3 (San Francisco), atl1 (Atlanta), syd1 (Sydney). See [Regions](regions.md) for updates.

## Connect your tooling
- Environment setup (one‑time per region)
```
export TELNYX_API_KEY=<your-telnyx-api-key>
export LIVEKIT_URL=https://<region>.livekit-telnyx.com
export LIVEKIT_API_KEY=$TELNYX_API_KEY
export LIVEKIT_API_SECRET=<your-secret>
```
- Provision your tenant in the region (one‑time)
```
curl -s -X POST "https://<region>.livekit-telnyx.com/provision" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-project",
    "api_key": "'$TELNYX_API_KEY'",
    "api_secret": "'$LIVEKIT_API_SECRET'"
  }'
```
- Verify: `lk --version` (>= 2.16.0) and `lk room list`.
- SDK example (Python)
```
from livekit.api import LiveKitAPI
api = LiveKitAPI(
    url="https://nyc1.livekit-telnyx.com",
    api_key="<your-telnyx-api-key>",
    api_secret="<your-livekit-api-secret>",
)
```
See [Connect to Telnyx](connect-to-telnyx.md).

## End-to-end quickstart
1) Prerequisites: Telnyx account and API key, your own LIVEKIT_API_SECRET, Python ≥ 3.10, LiveKit CLI ≥ 2.16.0. See [LiveKit on Telnyx quick start](livekit-on-telnyx-quick-start.md).

2) Configure the CLI and provision: export env vars and POST /provision (see Connect your tooling).

3) Set up telephony
- Buy a number via API or portal; assign it to a SIP connection.
- Create an FQDN SIP connection pointing to your region:
  - nyc1 → nyc1.sip.livekit-telnyx.com
  - sfo3 → sfo3.sip.livekit-telnyx.com
  - atl1 → atl1.sip.livekit-telnyx.com
  - syd1 → syd1.sip.livekit-telnyx.com
- Register with the platform
  - Create an inbound SIP trunk for your DID and restrict sources to Telnyx SIP IPs:
    - allowed_addresses: 192.76.120.0/22
  - Add a dispatch rule that routes calls from the trunk to your agent.
See [Telephony](telephony.md).

4) Clone an example agent
```
git clone https://github.com/team-telnyx/telnyx-livekit-agent-examples.git
cd telnyx-livekit-agent-examples/restaurant
```

5) Deploy your agent
```
lk agent create .
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
lk agent status
```

6) Call your agent
- Dial your purchased number and interact with the bot.

## Build agents with the Telnyx plugin
- Install
```
pip install "telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin"
```
- Minimal example
```
import asyncio
from livekit.agents import Agent, AgentSession, JobContext, RoomInputOptions
from livekit.plugins import openai, silero, telnyx

class MyAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful voice assistant.")
    async def on_enter(self):
        self.session.generate_reply(instructions="Greet the caller and ask how you can help.")

async def entrypoint(ctx: JobContext):
    session = AgentSession(
        stt=telnyx.STT(
            transcription_engine="Deepgram",
            base_url="wss://api.telnyx.com/v2/speech-to-text/transcription",
        ),
        llm=openai.LLM.with_telnyx(model="moonshotai/Kimi-K2.6"),
        tts=telnyx.TTS(voice="Telnyx.NaturalHD.astra", sample_rate=24000),
        vad=silero.VAD.load(),
    )
    await ctx.connect()
    await session.start(agent=MyAgent(), room=ctx.room, room_input_options=RoomInputOptions())
    done = asyncio.Event()
    @ctx.room.on("disconnected")
    def _on_disc(*_):
        done.set()
    await done.wait()
```
- requirements.txt
```
livekit-agents
livekit-plugins-openai
livekit-plugins-silero
telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin
```
- Deploy
```
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
lk agent logs --id <AGENT_ID>
```
- Swap models anytime: see [Models](models.md), [STT](stt.md), [TTS](tts.md), and [LLM](llm.md).
See [Build](build.md).

## Troubleshooting tips
- Call doesn’t connect: confirm your SIP connection targets the correct regional FQDN and the DID is assigned.
- Agent doesn’t pick up: `lk agent status` and `lk agent logs` for health/logs.
- Audio quality: choose the closest region and enable HD Voice per [Telephony](telephony.md).

## Next steps and references
- Architecture and scaling: [LiveKit on Telnyx architecture](livekit-on-telnyx-architecture.md)
- Build and deploy: [Build](build.md), [Deploy](deploy.md)
- Telephony: [Telephony](telephony.md)
- Models and plugins: [Models](models.md), [STT](stt.md), [TTS](tts.md), [LLM](llm.md)
- Regions, limits, and pricing: [Regions](regions.md), [Limits](limits.md), [Pricing](pricing.md)
- Migration and compatibility: [Compatibility](compatibility.md), [Connect to Telnyx](connect-to-telnyx.md)
