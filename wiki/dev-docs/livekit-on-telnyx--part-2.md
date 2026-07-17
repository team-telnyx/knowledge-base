---
title: LiveKit on Telnyx
summary: Telnyx LiveKit is a managed platform for deploying voice AI agents at scale,
  combining LiveKit's agent framework with built-in telephony, colocated AI inference
  on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers
  architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM),
  telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.
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
- url: https://developers.telnyx.com/docs/livekit/models/index
- url: https://developers.telnyx.com/docs/livekit/models/llm
- url: https://developers.telnyx.com/docs/livekit/models/stt
- url: https://developers.telnyx.com/docs/livekit/models/tts
- url: https://developers.telnyx.com/docs/livekit/observability/index
- url: https://developers.telnyx.com/docs/livekit/pricing
- url: https://developers.telnyx.com/docs/livekit/quickstart
- url: https://developers.telnyx.com/docs/livekit/regions
- url: https://developers.telnyx.com/docs/livekit/telephony
updated_at: 2026-07-17T09:14:35Z
---

# LiveKit on Telnyx

*Part 2 of 6 — see also: [Part 1](livekit-on-telnyx--part-1.md), [Part 3](livekit-on-telnyx--part-3.md), [Part 4](livekit-on-telnyx--part-4.md), [Part 5](livekit-on-telnyx--part-5.md), [Part 6](livekit-on-telnyx--part-6.md)*

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale, combining LiveKit's agent framework with built-in telephony, colocated AI inference on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM), telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.

## Quickstart

Go from zero to a working voice agent you can call from your phone. By the end, you'll have a LiveKit agent deployed on Telnyx infrastructure, connected to a real phone number.

### Prerequisites

- A [Telnyx account](https://portal.telnyx.com)
- A Telnyx API key (generate one in the [portal](https://portal.telnyx.com))
- A secret key you create and keep safe — this is your `LIVEKIT_API_SECRET`
- Python ≥ 3.10
- [LiveKit CLI](https://docs.livekit.io/home/cli/) (`lk`) version 2.16.0 or later

Verify your CLI version:

```
lk --version
```

### Step 1: Configure the CLI

Set your environment variables to point at a Telnyx LiveKit region:

```
export TELNYX_API_KEY=<your-telnyx-api-key>
export LIVEKIT_URL=https://<region>.livekit-telnyx.com
export LIVEKIT_API_KEY=$TELNYX_API_KEY
export LIVEKIT_API_SECRET=<your-secret>
```

`LIVEKIT_API_KEY` is your Telnyx API key — the same one you use everywhere else on the platform. Set `TELNYX_API_KEY` once and reference it throughout.

Register your credentials with the platform:

```
curl -s -X POST "https://<region>.livekit-telnyx.com/provision" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-project",
    "api_key": "'$TELNYX_API_KEY'",
    "api_secret": "'$LIVEKIT_API_SECRET'"
  }'
```

This creates your tenant record on the platform. You only need to do this once per region.

### Step 2: Set up telephony

To receive phone calls, you need a phone number (DID) pointed at the Telnyx LiveKit SIP servers. No third-party SIP fees — Telnyx is the carrier.

**Buy a phone number.** Search for an available number in your area code and order it. With the API, browse available numbers (replace `512` with your area code):

```
curl -sg "https://api.telnyx.com/v2/available_phone_numbers?filter[country_code]=US&filter[national_destination_code]=512" \
  -H "Authorization: Bearer $TELNYX_API_KEY" | \
  jq -r '["NUMBER","LOCATION","MONTHLY"], (.data[] | [.phone_number, (.region_information | map(.region_name) | join(", ")), .cost_information.monthly_cost]) | @tsv' | \
  column -t | less
```

Order the number you want:

```
curl -s -X POST "https://api.telnyx.com/v2/number_orders" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"phone_numbers": [{"phone_number": "+1XXXXXXXXXX"}]}' | \
  jq '{id: .data.id, status: .data.status, phone_number: .data.phone_numbers[0].phone_number}'
```

Confirm the order completed:

```
curl -s "https://api.telnyx.com/v2/number_orders/ORDER_ID" \
  -H "Authorization: Bearer $TELNYX_API_KEY" | \
  jq '{id: .data.id, status: .data.status, phone_number: .data.phone_numbers[0].phone_number}'
```

Wait for `"success"` before moving on. Alternatively, in the portal go to **Real Time Communications → Numbers → Buy Numbers** and purchase a number by checking out.

**Create a SIP connection.** A SIP connection tells Telnyx how to route inbound calls. Point it at one of the regional LiveKit SIP servers so calls land on the right infrastructure. With the API, create the FQDN connection (replace `{slug}` with your region slug):

```
curl -s -X POST "https://api.telnyx.com/v2/fqdn_connections" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"connection_name": "{slug}-livekit-sip-connection"}' | \
  jq '{id: .data.id, name: .data.connection_name}'
```

Attach the regional SIP FQDN (replace `CONNECTION_ID` and `{slug}` with your region slug):

```
curl -s -X POST "https://api.telnyx.com/v2/fqdns" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"connection_id": "CONNECTION_ID", "fqdn": "{slug}.sip.livekit-telnyx.com", "dns_record_type": "a", "port": 5060}' | \
  jq '{fqdn: .data.fqdn, connection_id: .data.connection_id}'
```

Assign your phone number to the connection (replace `CONNECTION_ID` and phone number):

```
curl -s -X PATCH "https://api.telnyx.com/v2/phone_numbers/+1XXXXXXXXXX" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"connection_id": "CONNECTION_ID"}' | \
  jq '{phone_number: .data.phone_number, connection_id: .data.connection_id}'
```

Alternatively, in the portal go to **Real Time Communications → Voice → SIP Connections → Create**, set the connection type to **FQDN**, point it at your region's SIP endpoint, and assign your phone number to this SIP connection.

**Register the number with the platform.** Set up an [inbound trunk](https://docs.livekit.io/telephony/accepting-calls/inbound-trunk/) for your number and a [dispatch rule](https://docs.livekit.io/telephony/accepting-calls/dispatch-rule/) to route calls to your agent.

Create an inbound SIP trunk:

```
echo '{
  "trunk": {
    "name": "telnyx-inbound",
    "numbers": ["+1XXXXXXXXXX"],
    "allowed_addresses": ["192.76.120.0/22"]
  }
}' | lk sip inbound create -
```

Note the trunk `sid` in the response — you'll need it in the next step. `allowed_addresses` restricts which source IPs can send SIP traffic to this trunk. `192.76.120.0/22` is Telnyx's SIP network — since Telnyx is your carrier, all inbound calls will originate from this range.

Create a dispatch rule:

```
echo '{
  "dispatchRule": {
    "name": "route-to-agent",
    "trunkIds": ["<TRUNK_ID>"],
    "rule": { "dispatchRuleIndividual": {} },
    "roomConfig": { "agents": [{ "agentName": "agent" }] }
  }
}' | lk sip dispatch create -
```

### Step 3: Clone an example agent

Clone the example agents repo and navigate to the restaurant agent:

```
git clone https://github.com/team-telnyx/telnyx-livekit-agent-examples.git
cd telnyx-livekit-agent-examples/restaurant
```

This is a fully working voice agent — an Italian restaurant ordering assistant built with [`livekit-plugins-telnyx`](https://github.com/team-telnyx/telnyx-livekit-plugin) for STT, TTS, and LLM.

### Step 4: Deploy

Register the agent with the platform, then deploy it to your Telnyx LiveKit region:

```
lk agent create .
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

The CLI uploads your agent code, builds a container image, and deploys it. You'll see build logs streaming in real-time. Check that your agent is running:

```
lk agent status
```

`lk agent status` reads the agent ID from your `livekit.toml` file — you don't need to specify it manually. If you skip `lk agent create`, there's no ID in the file and the command will fail.

### Step 5: Call your agent

Pick up your phone and dial the number you purchased. You should hear:

> "Thanks for calling Bella's Kitchen!"

Try ordering some pasta. The agent handles the full conversation — browsing the menu, answering questions, and taking your order.

Troubleshooting:

- **Call doesn't connect** — Verify your SIP connection is pointed at the correct regional FQDN and your DID is assigned to it.
- **Agent doesn't pick up** — Run `lk agent status` to confirm the agent is running. Check logs with `lk agent logs`.
- **Audio quality issues** — Make sure you're using the region closest to you.

## Connect

Connecting to the Telnyx LiveKit platform is a URL and credential swap. No code changes. Make sure your `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` are exported in your shell. Verify the connection:

```
lk room list
```

Server SDKs (Python, Go, Node.js) just need the URL and credentials:

```
from livekit.api import LiveKitAPI

api = LiveKitAPI(
    url="https://nyc1.livekit-telnyx.com",
    api_key="<your-telnyx-api-key>",
    api_secret="<your-livekit-api-secret>",
)
```

If you're migrating from LiveKit Cloud or self-hosted, change the three environment variables and everything else stays the same.
