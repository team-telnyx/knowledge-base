---
title: Telecom Event Processor
summary: Process voice, SMS, and messaging events in real-time.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
    content_hash: fcee9a40bc3e97c74c4faf1d204d8a7e1e2370de30f4547df621450e1d4ab7da
updated_at: 2026-04-10T00:00:00Z
---

# Telecom Event Processor

Process voice, SMS, and messaging events in real-time.

Process voice calls, SMS messages, and fax events in real-time with low latency.

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                    Telnyx Network                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │  Voice   │  │   SMS    │  │   Fax    │  │  Number  │     │
│  │  Calls   │  │ Messages │  │  Events  │  │  Lookup  │     │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘     │
└───────┼─────────────┼─────────────┼─────────────┼────────────┘
        │             │             │             │
        └─────────────┴──────┬──────┴─────────────┘
                             ▼
              ┌──────────────────────────────┐
              │    Edge Compute Function     │
              │  ┌─────────┐  ┌───────────┐  │
              │  │ Webhook │→ │ Business  │  │
              │  │ Handler │  │   Logic   │  │
              │  └─────────┘  └───────────┘  │
              └──────────────────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │   CRM    │  │ Analytics│  │ Alerts   │
        │  System  │  │ Platform │  │ Service  │
        └──────────┘  └──────────┘  └──────────┘
```

## Implementation

```javascript theme={null}
// Unified telecom event handler
export async function handler(request) {
    const webhook = await request.json();
    const eventType = webhook.data.event_type;

    // Route by event type
    switch (eventType) {
        case "call.initiated":
        case "call.answered":
        case "call.hangup":
            return handleVoiceEvent(webhook);

        case "message.received":
        case "message.sent":
            return handleSMSEvent(webhook);

        case "fax.received":
            return handleFaxEvent(webhook);

        case "fax.sent":
            return handleFaxEvent(webhook);

        default:
            console.log(`Unhandled event: ${eventType}`);
            return new Response("OK");
    }
}

async function handleVoiceEvent(webhook) {
    const event = webhook.data;
    const callId = event.payload.call_control_id;

    // Log to analytics
    await fetch(process.env.ANALYTICS_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            type: "voice",
            event: event.event_type,
            call_id: callId,
            from: event.payload.from,
            to: event.payload.to,
            timestamp: event.occurred_at
        })
    });

    // Business logic
    if (event.event_type === "call.initiated") {
        // Check CRM for caller info
        const caller = await lookupCaller(event.payload.from);

        if (caller.vip) {
            // Route VIP to priority queue
            return generateTeXML(`

                    Welcome back, ${caller.name}. Connecting you now.
                    <Queue name="vip"/>

            `);
        }
    }

    return new Response("OK");
}

async function handleSMSEvent(webhook) {
    const event = webhook.data;

    if (event.event_type === "message.received") {
        const text = event.payload.text.toLowerCase();
        const from = event.payload.from.phone_number;

        // Keyword detection (TCPA-compliant opt-out keywords)
        if (text.includes("stop") || text.includes("unsubscribe") || 
            text.includes("cancel") || text.includes("quit")) {
            await updateOptOut(from, true);
            await sendSMS(from, "You have been unsubscribed. Reply START to resubscribe.");
        } else if (text.includes("help")) {
            await sendSMS(from, "Reply STOP to unsubscribe, START to resubscribe.");
        } else if (text.includes("start")) {
            await updateOptOut(from, false);
            await sendSMS(from, "You have been resubscribed.");
        }
    }

    return new Response("OK");
}

async function handleFaxEvent(webhook) {
    const event = webhook.data;

    // Log fax event
    await fetch(process.env.ANALYTICS_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            type: "fax",
            event: event.event_type,
            fax_id: event.payload.fax_id,
            from: event.payload.from,
            to: event.payload.to,
            pages: event.payload.page_count,
            timestamp: event.occurred_at
        })
    });

    // Download and store fax if received
    if (event.event_type === "fax.received" && event.payload.media_url) {
        await storeFax(event.payload.fax_id, event.payload.media_url);
    }

    return new Response("OK");
}
```

## Use Cases

* **Contact center** — Route calls based on caller history
* **SMS marketing** — Process opt-ins/outs in real-time
* **Two-factor auth** — Generate and verify SMS codes


## Related Pages

- [Telecom glossary](../runbooks/telecom-glossary.md)
