---
title: Telnyx API Binding
summary: The Telnyx API binding exposes a ready-to-use, authenticated Telnyx client
  on `env` inside an Edge Compute function, so handlers can call the Telnyx REST API
  without managing API keys. This page covers the binding model, the client shape,
  error handling, and end-to-end examples for sending messages, receiving inbound
  SMS, and handling inbound voice calls.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/api-reference
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/handling-calls
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/index
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/receiving-messages
updated_at: 2026-08-05T13:43:00Z
---

# Telnyx API Binding

*Part 2 of 2 — see also: [Part 1](telnyx-api-binding--part-1.md)*

The Telnyx API binding exposes a ready-to-use, authenticated Telnyx client on `env` inside an Edge Compute function, so handlers can call the Telnyx REST API without managing API keys. This page covers the binding model, the client shape, error handling, and end-to-end examples for sending messages, receiving inbound SMS, and handling inbound voice calls.

## Receiving messages

Inbound SMS is webhook-driven: Telnyx POSTs a `message.received` event to your messaging profile's webhook, and your Edge Compute function is that webhook. Replying to another Telnyx number is **on-net** — no 10DLC campaign required.

### Write the handler

```ts
// index.ts
import * as http from "node:http";
import { env } from "@telnyx/edge-runtime";

const port = Number(process.env.PORT ?? 8080);
const received: any[] = []; // in-memory; use KV or SQL DB for durable storage

function body(req: http.IncomingMessage): Promise<string> {
  return new Promise((r) => {
    let b = "";
    req.on("data", (c) => (b += c));
    req.on("end", () => r(b));
  });
}

http.createServer(async (req, res) => {
  // GET: see what's been received
  if (req.method === "GET") {
    res.writeHead(200, { "content-type": "application/json" });
    res.end(JSON.stringify({ received }, null, 2));
    return;
  }

  // POST: Telnyx inbound webhook — parse it through the binding
  const evt = env.MY_TELNYX.webhooks.unsafeUnwrap<{ data: any }>(await body(req)).data;
  if (evt?.event_type === "message.received") {
    const p = evt.payload;
    const from = p.from.phone_number;
    const to = p.to[0].phone_number;
    received.unshift({ from, to, text: p.text, at: evt.occurred_at });

    // Auto-reply on-net (no 10DLC when the recipient is a Telnyx number)
    await env.MY_TELNYX.messages.send({ from: to, to: from, text: `You said: ${p.text}` });
  }
  res.writeHead(200);
  res.end();
}).listen(port);
```

Declare the binding in `func.toml` (see the [Quick Start](quick-start.md)):

```toml
[telnyx]
binding = "MY_TELNYX"
```

### Ship

```
telnyx-edge ship
```

### Point a messaging profile at it

Set a messaging profile's inbound webhook to your function URL, then assign your number to that profile:

```
# webhook -> your function
curl -X POST https://api.telnyx.com/v2/messaging_profiles \
  -H "Authorization: Bearer $TELNYX_API_KEY" -H "Content-Type: application/json" \
  -d '{"name":"inbound-demo","webhook_url":"https://YOUR-FUNC.telnyxcompute.com","whitelisted_destinations":["US"]}'

# assign your number to the profile (use the profile id from the response)
curl -X PATCH https://api.telnyx.com/v2/phone_numbers/YOUR-NUMBER-ID/messaging \
  -H "Authorization: Bearer $TELNYX_API_KEY" -H "Content-Type: application/json" \
  -d '{"messaging_profile_id":"YOUR-PROFILE-ID"}'
```

### Test on-net

Send from another Telnyx number on your account to your function's number:

```
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Authorization: Bearer $TELNYX_API_KEY" -H "Content-Type: application/json" \
  -d '{"from":"+1ANOTHER_TELNYX_NUMBER","to":"+1YOUR_FUNC_NUMBER","text":"hello"}'
```

You get back **"You said: hello"** on-net, and `GET https://YOUR-FUNC.telnyxcompute.com` shows what arrived. The inbound event the function parses looks like:

```json
{
  "data": {
    "event_type": "message.received",
    "occurred_at": "2026-06-19T16:06:17.464+00:00",
    "payload": {
      "from": { "phone_number": "+1..." },
      "to": [ { "phone_number": "+1..." } ],
      "text": "hello"
    }
  }
}
```

**Only on-net replies skip 10DLC.** Receiving is always free. Replying to a Telnyx number is on-net (no campaign). Replying to an off-net number — e.g. a personal mobile — is application-to-person traffic and requires 10DLC registration.

### Keyword auto-reply

The handler above echoes every message. To answer commands instead, replace the `messages.send` call with a keyword match:

```ts
const text = p.text.trim().toUpperCase();
if (text === "STOP") {
  // opt-out: send nothing
} else {
  const replies: Record<string, string> = {
    HELP: "Commands: HOURS, LOCATION. Reply STOP to opt out.",
    HOURS: "Open Mon-Fri 9am-5pm ET.",
    LOCATION: "600 Congress Ave, Austin, TX",
  };
  await env.MY_TELNYX.messages.send({
    from: to,
    to: from,
    text: replies[text] ?? "Thanks for your message. Reply HELP for options.",
  });
}
```

This handles the STOP message itself but doesn't remember it — store opted-out numbers in [KV](kv--part-1.md) and check before every send.

## Handling calls

Inbound voice is webhook-driven through Call Control: Telnyx POSTs call events to your Call Control application's webhook, and your Edge Compute function is that webhook. On `call.initiated` you answer the call; on `call.answered` you play audio.

### Write the handler

```ts
// index.ts
import * as http from "node:http";
import { env } from "@telnyx/edge-runtime";

const port = Number(process.env.PORT ?? 8080);
const AUDIO_URL = "https://YOUR-HOST/song.mp3"; // a reachable HTTPS mp3/wav you have rights to

function body(req: http.IncomingMessage): Promise<string> {
  return new Promise((r) => {
    let b = "";
    req.on("data", (c) => (b += c));
    req.on("end", () => r(b));
  });
}

http.createServer(async (req, res) => {
  if (req.method === "GET") { res.writeHead(200).end(); return; } // health

  // parse the inbound webhook through the binding
  const evt = env.MY_TELNYX.webhooks.unsafeUnwrap<{ data: any }>(await body(req)).data;
  const id = evt?.payload?.call_control_id;

  if (evt?.event_type === "call.initiated" && id) {
    await env.MY_TELNYX.calls.actions.answer(id, {});
  } else if (evt?.event_type === "call.answered" && id) {
    await env.MY_TELNYX.calls.actions.startPlayback(id, { audio_url: AUDIO_URL });
  }

  res.writeHead(200);
  res.end();
}).listen(port);
```

Declare the binding in `func.toml`:

```toml
[telnyx]
binding = "MY_TELNYX"
```

### Ship

```
telnyx-edge ship
```

### Point a Call Control app at it

```
# create a Call Control app whose webhook is your function
curl -X POST https://api.telnyx.com/v2/call_control_applications \
  -H "Authorization: Bearer $TELNYX_API_KEY" -H "Content-Type: application/json" \
  -d '{"application_name":"voice-demo","webhook_event_url":"https://YOUR-FUNC.telnyxcompute.com"}'

# route your number to that app (connection_id = the app id from the response)
curl -X PATCH https://api.telnyx.com/v2/phone_numbers/YOUR-NUMBER-ID \
  -H "Authorization: Bearer $TELNYX_API_KEY" -H "Content-Type: application/json" \
  -d '{"connection_id":"YOUR-CALL-CONTROL-APP-ID"}'
```

### Test

Call the number from any phone. The function answers and plays your audio.

`audio_url` must be a publicly reachable HTTPS `.mp3` or `.wav`. The flow is two events — `call.initiated` (answer) then `call.answered` (play) — so handle both. To loop, hang up, or chain more actions, respond to later events (`call.playback.ended`, `call.hangup`) the same way.

### Time-of-day routing

To route callers to a person instead of playing audio, replace both event branches with a single `transfer` on `call.initiated` — Telnyx dials the destination and bridges the caller when it answers, so there's nothing to do on `call.answered`:

```ts
const OFFICE = "+13125550100"; // business hours
const ON_CALL = "+13125550199"; // after hours

function businessHours(): boolean {
  const hour = Number(
    new Intl.DateTimeFormat("en-US", {
      timeZone: "America/New_York",
      hour: "numeric",
      hourCycle: "h23",
    }).format(new Date()),
  );
  return hour >= 9 && hour < 17;
}

if (evt?.event_type === "call.initiated" && id) {
  await env.MY_TELNYX.calls.actions.transfer(id, {
    to: businessHours() ? OFFICE : ON_CALL,
  });
}
```

If the transfer fails, you get a `call.hangup` webhook for the destination leg and the caller's leg stays active — transfer to an alternate number or answer and play a message.
