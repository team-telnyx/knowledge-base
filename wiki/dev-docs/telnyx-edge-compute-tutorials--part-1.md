---
title: Telnyx Edge Compute Tutorials
summary: Learn Telnyx Edge by building real applications. This guide curates four
  end‑to‑end demos (REST API, SMS webhook, voice call router, image resizer), plus
  patterns you’ll reuse across projects and links to quickstarts and references.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/demos/index
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
- url: https://developers.telnyx.com/docs/edge-compute/examples/index
updated_at: 2026-05-20T08:25:26Z
---

# Telnyx Edge Compute Tutorials

*Part 1 of 2 — see also: [Part 2](telnyx-edge-compute-tutorials--part-2.md)*

Learn Telnyx Edge by building real applications. This guide curates four end‑to‑end demos (REST API, SMS webhook, voice call router, image resizer), plus patterns you’ll reuse across projects and links to quickstarts and references.

## Before you begin

- Requirements:
  - Telnyx account with Edge Compute enabled
  - telnyx-edge CLI installed
- Helpful pages: [Edge Compute Quickstart](edge-compute-quickstart.md), [Edge Compute Examples](edge-compute-examples.md), [Edge Compute CLI Reference](edge-compute-cli-reference.md)

## Build a REST API (15 min · Beginner)
Create a JSON API with routing, validation, and error handling.

1) Create a function

```
telnyx-edge new-func -l=python -n=my-api
cd my-api
```

2) Implement CRUD in src/main.py

```python
import json
from urllib.parse import urlparse

items = {}
next_id = 1

class Function:
    async def handler(self, request):
        path = urlparse(request.url).path
        method = request.method
        if path == "/items" and method == "GET":
            return self.json_response(list(items.values()))
        elif path == "/items" and method == "POST":
            return await self.create_item(request)
        elif path.startswith("/items/") and method == "GET":
            return self.get_item(path.split("/")[-1])
        elif path.startswith("/items/") and method == "DELETE":
            return self.delete_item(path.split("/")[-1])
        return self.json_response({"error": "Not found"}, 404)

    async def create_item(self, request):
        global next_id
        try:
            body = json.loads(await request.text())
        except json.JSONDecodeError:
            return self.json_response({"error": "Invalid JSON"}, 400)
        if "name" not in body:
            return self.json_response({"error": "name is required"}, 400)
        item = {"id": str(next_id), "name": body["name"]}
        items[str(next_id)] = item
        next_id += 1
        return self.json_response(item, 201)

    def get_item(self, item_id):
        return self.json_response(items[item_id]) if item_id in items else self.json_response({"error": "Not found"}, 404)

    def delete_item(self, item_id):
        if item_id in items:
            del items[item_id]
            return self.json_response({"deleted": True})
        return self.json_response({"error": "Not found"}, 404)

    def json_response(self, data, status=200):
        return {"status": status, "headers": {"Content-Type": "application/json"}, "body": json.dumps(data)}
```

3) Test locally

```
telnyx-edge dev
# Create
curl -X POST http://localhost:8787/items -H "Content-Type: application/json" -d '{"name":"Test Item"}'
# List / Get / Delete
curl http://localhost:8787/items
curl http://localhost:8787/items/1
curl -X DELETE http://localhost:8787/items/1
```

4) Deploy

```
telnyx-edge ship
```
Live URL: https://my-api-{orgId}.telnyxcompute.com

Tips you’ll reuse: [Edge Compute Examples](edge-compute-examples.md) has patterns for parsing query parameters, handling HTTP methods, and reading request bodies.

## SMS Webhook Handler (20 min · Beginner)
Process incoming SMS webhooks and auto‑reply with keyword logic.

Prerequisites:
- Telnyx phone number configured for SMS

1) Create a function

```
telnyx-edge new-func -l=javascript -n=sms-handler
cd sms-handler
```

2) Implement src/index.js

```javascript
export async function handler(request) {
  if (request.method !== "POST") {
    return new Response("Method not allowed", { status: 405 });
  }
  const webhook = await request.json();
  const event = webhook.data;
  if (event.event_type === "message.received") {
    const from = event.payload.from.phone_number;
    const text = event.payload.text.toLowerCase().trim();
    let reply;
    if (text === "help") reply = "Commands: HOURS, LOCATION, STATUS";
    else if (text === "hours") reply = "We're open Mon-Fri 9am-5pm EST";
    else if (text === "location") reply = "123 Main St, New York, NY 10001";
    else if (text === "status") reply = "All systems operational ✓";
    else reply = "Thanks for your message! Reply HELP for options.";
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
      Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      from: process.env.TELNYX_PHONE_NUMBER,
      to,
      text
    })
  });
  if (!response.ok) console.error("Failed to send SMS:", await response.text());
}
```

3) Configure secrets

```
telnyx-edge secrets add TELNYX_API_KEY "your-api-key-from-portal"
telnyx-edge secrets add TELNYX_PHONE_NUMBER "+15551234567"
```
Get your API key from the Telnyx Portal: https://portal.telnyx.com (API Keys). Use your Telnyx number in E.164 format.

4) Deploy and set webhook

```
telnyx-edge ship
```
In the Portal: Messaging → Phone Numbers → select your number → set webhook URL to https://sms-handler-{orgId}.telnyxcompute.com

5) Test: text HELP to your number and verify the reply.

## Voice Call Router (25 min · Intermediate)
Route incoming calls by time of day (and optionally by caller location) using TeXML.

1) Create a function and add dependency

```
telnyx-edge new-func -l=python -n=call-router
cd call-router
echo "pytz>=2024.1" > requirements.txt
```

2) Implement time‑based routing in src/main.py

```python
from datetime import datetime
import pytz

class Function:
    async def handler(self, request):
        webhook = await request.json()
        caller = webhook.get("from", "")  # available for custom logic
        destination = self.get_destination(caller)
        texml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Please hold while we connect your call.</Say>
  <Dial timeout="30">
    <Number>{destination}</Number>
  </Dial>
  <Say>We're sorry, no one is available. Please try again later.</Say>
  <Hangup/>
</Response>"""
        return {"status": 200, "headers": {"Content-Type": "application/xml"}, "body": texml}

    def get_destination(self, caller):
        est = pytz.timezone("America/New_York")
        hour = datetime.now(est).hour
        return "+15551234567" if 9 <= hour < 17 else "+15559876543"
        # Example geographic routing:
        # if caller.startswith("+44"): return "+44..."  # UK support
        # return "+1..."  # US support
```

3) Deploy and connect your number

```
telnyx-edge ship
```
In the Portal, configure your number to use this function’s URL as the TeXML webhook.
