---
title: SMS Webhook Handler
summary: Process incoming SMS messages and send automated replies.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
    content_hash: e4fb0601445bafdc27343811af9ba6c1f2100227005fa5578140105b5dc0571a
updated_at: 2026-04-10T00:00:00Z
---

# SMS Webhook Handler

Process incoming SMS messages and send automated replies.

Process incoming SMS messages and respond automatically based on keywords.

**What you'll learn:**

* Handling Telnyx webhooks
* Parsing SMS payloads
* Sending SMS responses via Telnyx API

## Prerequisites

* Telnyx account with a phone number
* Phone number configured for SMS

## Step 1: Create the Function

```bash theme={null}
telnyx-edge new-func -l=javascript -n=sms-handler
cd sms-handler
```

## Step 2: Implement the Handler

Replace `src/index.js`:

```javascript theme={null}
export async function handler(request) {
    // Verify this is a POST from Telnyx
    if (request.method !== "POST") {
        return new Response("Method not allowed", { status: 405 });
    }

    const webhook = await request.json();
    const event = webhook.data;

    // Handle incoming SMS
    if (event.event_type === "message.received") {
        const from = event.payload.from.phone_number;
        const text = event.payload.text.toLowerCase().trim();

        // Keyword-based responses
        let reply;
        if (text === "help") {
            reply = "Commands: HOURS, LOCATION, STATUS";
        } else if (text === "hours") {
            reply = "We're open Mon-Fri 9am-5pm EST";
        } else if (text === "location") {
            reply = "123 Main St, New York, NY 10001";
        } else if (text === "status") {
            reply = "All systems operational ✓";
        } else {
            reply = `Thanks for your message! Reply HELP for options.`;
        }

        // Send reply via Telnyx API
        await sendSMS(from, reply);
    }

    return new Response(JSON.stringify({ received: true }), {
        headers: { "Content-Type": "application/json" }
    });
}

async function sendSMS(to, text) {
    const response = await fetch("https://api.telnyx.com/v2/messages", {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${process.env.TELNYX_API_KEY}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            from: process.env.TELNYX_PHONE_NUMBER,
            to: to,
            text: text
        })
    });

    if (!response.ok) {
        console.error("Failed to send SMS:", await response.text());
    }
}
```

## Step 3: Configure Secrets

```bash theme={null}
telnyx-edge secrets add TELNYX_API_KEY "your-api-key-from-portal"
telnyx-edge secrets add TELNYX_PHONE_NUMBER "+15551234567"
```

> **Note:** Get your API key from the [Telnyx Portal](https://portal.telnyx.com) under **API Keys**. Use your Telnyx phone number in E.164 format.

## Step 4: Deploy and Configure Webhook

```bash theme={null}
telnyx-edge ship
```

In the Telnyx Portal:

1. Go to **Messaging → Phone Numbers**
2. Select your number
3. Set webhook URL to `https://sms-handler-{orgId}.telnyxcompute.com`

## Step 5: Test

Send an SMS with "HELP" to your Telnyx number. You should receive the help menu.
