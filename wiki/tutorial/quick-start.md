---
title: Quick Start
summary: Deploy a LiveKit voice agent on Telnyx and call it from your phone.
sources:
  - url: https://developers.telnyx.com/docs/livekit/quickstart
    content_hash: def7047c57590573b2df0b236cd0f57a79ffea7beba0071c4164fa2f43f8b12c
updated_at: 2026-04-10T00:00:00Z
---

# Quick Start

Deploy a LiveKit voice agent on Telnyx and call it from your phone.

Go from zero to a working voice agent you can call from your phone. By the end, you'll have a LiveKit agent deployed on Telnyx infrastructure, connected to a real phone number.

## Prerequisites

Before you start, make sure you have:

* A [Telnyx account](https://portal.telnyx.com)
* A Telnyx API key (generate one in the [portal](https://portal.telnyx.com))
* A secret key you create and keep safe — this is your `LIVEKIT_API_SECRET`
* Python ≥ 3.10
* [LiveKit CLI](https://docs.livekit.io/home/cli/) (`lk`) version 2.16.0 or later

Verify your CLI version:

```bash theme={null}
lk --version
```

## Step 1: Configure the CLI

Set your environment variables to point at a Telnyx LiveKit region:

```bash theme={null}
export TELNYX_API_KEY=<your-telnyx-api-key>
export LIVEKIT_URL=https://<region>.livekit-telnyx.com
export LIVEKIT_API_KEY=$TELNYX_API_KEY
export LIVEKIT_API_SECRET=<your-secret>
```

> **Note:** `LIVEKIT_API_KEY` is your Telnyx API key — the same one you use everywhere else on the platform. Set `TELNYX_API_KEY` once and reference it throughout.

Register your credentials with the platform:

```bash theme={null}
curl -s -X POST "https://<region>.livekit-telnyx.com/provision" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-project",
    "api_key": "'$TELNYX_API_KEY'",
    "api_secret": "'$LIVEKIT_API_SECRET'"
  }'
```

> **Note:** This creates your tenant record on the platform. You only need to do this once per region.

### Available regions

| Region        | Name (slug) | URL                       |
| ------------- | ----------- | ------------------------- |
| New York      | `nyc1`      | `nyc1.livekit-telnyx.com` |
| San Francisco | `sfo3`      | `sfo3.livekit-telnyx.com` |
| Atlanta       | `atl1`      | `atl1.livekit-telnyx.com` |
| Sydney        | `syd1`      | `syd1.livekit-telnyx.com` |

Choose the region closest to your users for the lowest latency.

## Step 2: Set up telephony

To receive phone calls, you need a phone number (DID) pointed at the Telnyx LiveKit SIP servers. No third-party SIP fees — Telnyx is the carrier.

### Buy a phone number

### With our APIs

    Search for an available number in your area code and order it:

    **1. Browse available numbers** (replace `512` with your area code):

    ```bash theme={null}
    curl -sg "https://api.telnyx.com/v2/available_phone_numbers?filter[country_code]=US&filter[national_destination_code]=512" \
      -H "Authorization: Bearer $TELNYX_API_KEY" | \
      jq -r '["NUMBER","LOCATION","MONTHLY"], (.data[] | [.phone_number, (.region_information | map(.region_name) | join(", ")), .cost_information.monthly_cost]) | @tsv' | \
      column -t | less
    ```

    > **Note:** Note the number you want before exiting — you'll need it below.

    **2. Order the number you want:**

    ```bash theme={null}
    curl -s -X POST "https://api.telnyx.com/v2/number_orders" \
      -H "Authorization: Bearer $TELNYX_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"phone_numbers": [{"phone_number": "+1XXXXXXXXXX"}]}' | \
      jq '{id: .data.id, status: .data.status, phone_number: .data.phone_numbers[0].phone_number}'
    ```

    **3. Confirm the order completed:**

    ```bash theme={null}
    curl -s "https://api.telnyx.com/v2/number_orders/ORDER_ID" \
      -H "Authorization: Bearer $TELNYX_API_KEY" | \
      jq '{id: .data.id, status: .data.status, phone_number: .data.phone_numbers[0].phone_number}'
    ```

    Wait for `"success"` before moving on.

    > **Note:** If your order didn't complete successfully, [chat with us](https://telnyx.com/contact-us) — we're happy to help.

### With the portal

    1. Log in to the [Telnyx portal](https://portal.telnyx.com)
    2. Go to [**Real Time Communcations** → **Numbers** → **Buy Numbers**](https://portal.telnyx.com/#/numbers/buy-numbers)
    3. Purchase a number by checking out

### Create a SIP connection

A SIP connection tells Telnyx how to route inbound calls. You'll point it at one of our regional LiveKit SIP servers so calls land on the right infrastructure.

| Region        | Name (slug) | SIP FQDN                      |
| ------------- | ----------- | ----------------------------- |
| New York      | `nyc1`      | `nyc1.sip.livekit-telnyx.com` |
| San Francisco | `sfo3`      | `sfo3.sip.livekit-telnyx.com` |
| Atlanta       | `atl1`      | `atl1.sip.livekit-telnyx.com` |
| Sydney        | `syd1`      | `syd1.sip.livekit-telnyx.com` |

### With our APIs

    **1. Create the FQDN connection** (replace `{slug}` with your region slug):

    ```bash theme={null}
    curl -s -X POST "https://api.telnyx.com/v2/fqdn_connections" \
      -H "Authorization: Bearer $TELNYX_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"connection_name": "{slug}-livekit-sip-connection"}' | \
      jq '{id: .data.id, name: .data.connection_name}'
    ```

    **2. Attach the regional SIP FQDN** (replace `CONNECTION_ID` and `{slug}` with your region slug):

    ```bash theme={null}
    curl -s -X POST "https://api.telnyx.com/v2/fqdns" \
      -H "Authorization: Bearer $TELNYX_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"connection_id": "CONNECTION_ID", "fqdn": "{slug}.sip.livekit-telnyx.com", "dns_record_type": "a", "port": 5060}' | \
      jq '{fqdn: .data.fqdn, connection_id: .data.connection_id}'
    ```

    **3. Assign your phone number to the connection** (replace `CONNECTION_ID` and phone number):

    ```bash theme={null}
    curl -s -X PATCH "https://api.telnyx.com/v2/phone_numbers/+1XXXXXXXXXX" \
      -H "Authorization: Bearer $TELNYX_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"connection_id": "CONNECTION_ID"}' | \
      jq '{phone_number: .data.phone_number, connection_id: .data.connection_id}'
    ```

### With the portal

    1. In the portal, go to [**Real Time Communcations** → **Voice** → **SIP Connections** → **Create**](https://portal.telnyx.com/#/voice/connections)
    2. Set the connection type to **FQDN**
    3. Point it at your region's SIP endpoint from the table above
    4. Assign your phone number to this SIP connection

### Register the number with the platform

Set up an [inbound trunk](https://docs.livekit.io/telephony/accepting-calls/inbound-trunk/) for your number and a [dispatch rule](https://docs.livekit.io/telephony/accepting-calls/dispatch-rule/) to route calls to your agent.

**1. Create an inbound SIP trunk:**

```bash theme={null}
echo '{
  "trunk": {
    "name": "telnyx-inbound",
    "numbers": ["+1XXXXXXXXXX"],
    "allowed_addresses": ["192.76.120.0/22"]
  }
}' | lk sip inbound create -
```

Note the trunk `sid` in the response — you'll need it in the next step.

> **Note:** `allowed_addresses` restricts which source IPs can send SIP traffic to this trunk. `192.76.120.0/22` is Telnyx's SIP network — since Telnyx is your carrier, all inbound calls will originate from this range.

**2. Create a dispatch rule:**

```bash theme={null}
echo '{
  "dispatchRule": {
    "name": "route-to-agent",
    "trunkIds": [""],
    "rule": { "dispatchRuleIndividual": {} },
    "roomConfig": { "agents": [{ "agentName": "agent" }] }
  }
}' | lk sip dispatch create -
```

## Step 3: Clone an example agent

Clone the example agents repo and navigate to the restaurant agent:

```bash theme={null}
git clone https://github.com/team-telnyx/telnyx-livekit-agent-examples.git
cd telnyx-livekit-agent-examples/restaurant
```

This is a fully working voice agent — an Italian restaurant ordering assistant built with [`livekit-plugins-telnyx`](https://github.com/team-telnyx/telnyx-livekit-plugin) for STT, TTS, and LLM.

## Step 4: Deploy

Register the agent with the platform, then deploy it to your Telnyx LiveKit region:

```bash theme={null}
lk agent create .
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

The CLI uploads your agent code, builds a container image, and deploys it. You'll see build logs streaming in real-time.

Check that your agent is running:

```bash theme={null}
lk agent status
```

> **Note:** `lk agent status` reads the agent ID from your `livekit.toml` file — you don't need to specify it manually. If you skip `lk agent create`, there's no ID in the file and the command will fail.

## Step 5: Call your agent

Pick up your phone and dial the number you purchased. You should hear:

> "Thanks for calling Bella's Kitchen!"

Try ordering some pasta. The agent handles the full conversation — browsing the menu, answering questions, and taking your order.

### Troubleshooting

* **Call doesn't connect** — Verify your SIP connection is pointed at the correct regional FQDN and your DID is assigned to it.
* **Agent doesn't pick up** — Run `lk agent status` to confirm the agent is running. Check logs with `lk agent logs`.
* **Audio quality issues** — Make sure you're using the region closest to you.

## Next steps

You've deployed your first agent. Here's where to go from here:

* [Build](../runbooks/build.md) — Write your own agent from scratch
* [Deploy](../runbooks/deploy.md) — Regions, scaling, secrets, and production deployment
* [Models](../runbooks/overview.md) — STT, TTS, and LLM options available on Telnyx
* [Telephony](../runbooks/telephony.md) — Inbound/outbound calls, dispatch rules, multiple numbers
* [Compatibility](../runbooks/compatibility.md) — What's the same and different from LiveKit Cloud


## Related Pages

- [Quick Start](../runbooks/quick-start.md)
- [Edge Compute Quick Start](../tutorial/edge-compute-quick-start.md)
- [Start](../runbooks/start.md)
