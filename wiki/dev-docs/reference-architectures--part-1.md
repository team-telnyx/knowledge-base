---
title: Reference Architectures
summary: Reference architectures show how to combine Telnyx Edge Compute products
  to solve common problems, with diagrams, component breakdowns, and sample implementations.
  This guide summarizes four blueprints—Global API Gateway, Telecom Event Processor,
  Real-Time Media Pipeline, and IoT Data Ingestion—and notes upcoming framework support
  for deploying popular web frameworks with minimal changes.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/index
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
updated_at: 2026-05-20T08:18:53Z
---

# Reference Architectures

*Part 1 of 2 — see also: [Part 2](reference-architectures--part-2.md)*

Reference architectures show how to combine Telnyx Edge Compute products to solve common problems, with diagrams, component breakdowns, and sample implementations. This guide summarizes four blueprints—Global API Gateway, Telecom Event Processor, Real-Time Media Pipeline, and IoT Data Ingestion—and notes upcoming framework support for deploying popular web frameworks with minimal changes.

## What These Blueprints Provide
- Opinionated patterns for building on the edge: global routing, event handling, media processing, and IoT ingestion.
- Each pattern includes an architecture sketch, core components, and a starter implementation you can adapt.
- Use with [Quick Start](quick-start.md), then harden using [Best Practices](best-practices.md), [Testing](testing.md), and [CI/CD](ci-cd.md). See environment details in [Runtime](runtime.md) and limits in [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md).

## Global API Gateway
A globally distributed gateway that authenticates, rate-limits, caches, and routes requests to upstream services.

### Architecture
```
Client Requests
       │
       ▼
Telnyx Edge (Global PoPs): Auth → Rate Limiter → Cache → Router
       │
   ┌───┼───────────────┬───────────────┐
   ▼   ▼               ▼               
 Service A        Service B        Service C
```

### Components
- Edge Function (Edge Compute) — request processing and routing
- Rate limiting (Edge KV) — distributed counters per identity/time window
- Caching (Edge KV) — response caching with TTL
- Auth (Secrets) — JWT verification keys and configuration

### Sample implementation (Python-like pseudocode)
```python
import os, jwt, json, hashlib
from datetime import datetime

class APIGateway:
    def __init__(self):
        self.jwt_secret = os.getenv("JWT_SECRET")
        self.rate_limit = 100  # requests per minute
        self.kv = kv  # assume bound Edge KV instance

    async def handler(self, request):
        # 1) Auth
        auth = self.authenticate(request)
        if auth["error"]:
            return self.json({"error": auth["error"]}, 401)
        user_id = auth["user_id"]

        # 2) Rate limit
        if await self.is_rate_limited(user_id):
            return self.json({"error": "Rate limit exceeded"}, 429, {"Retry-After": "60"})

        # 3) Cache
        key = self.cache_key(request)
        cached = await self.kv.get(key)
        if cached:
            return self.json(json.loads(cached))

        # 4) Route
        resp = await self.route(request)

        # 5) Cache success
        if resp.get("status") == 200:
            await self.kv.put(key, json.dumps(resp), ttl=300)
        return resp

    def authenticate(self, request):
        h = request.headers.get("Authorization", "")
        if not h.startswith("Bearer "):
            return {"error": "Missing token", "user_id": None}
        try:
            payload = jwt.decode(h[7:], self.jwt_secret, algorithms=["HS256"])
            return {"error": None, "user_id": payload["sub"]}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token", "user_id": None}

    async def is_rate_limited(self, user_id):
        bucket = datetime.utcnow().strftime('%Y%m%d%H%M')
        key = f"rate:{user_id}:{bucket}"
        count = int(await self.kv.get(key) or 0)
        if count >= self.rate_limit:
            return True
        await self.kv.put(key, str(count + 1), ttl=60)
        return False

    def cache_key(self, request):
        raw = f"{request.method}:{request.url}"
        return "cache:" + hashlib.md5(raw.encode()).hexdigest()

    async def route(self, request):
        path = request.path
        backend = (
            "https://users-service.internal" if path.startswith("/api/users") else
            "https://orders-service.internal" if path.startswith("/api/orders") else None
        )
        if not backend:
            return {"status": 404, "body": json.dumps({"error": "Not found"})}
        upstream_url = backend + path + ("?" + request.query if request.query else "")
        upstream = await fetch(upstream_url, {
            "method": request.method,
            "headers": request.headers,
            "body": await request.text() if request.method != "GET" else None
        })
        return {"status": upstream.status, "headers": dict(upstream.headers), "body": await upstream.text()}

    def json(self, body, status=200, headers=None):
        h = {"Content-Type": "application/json", **(headers or {})}
        return {"status": status, "headers": h, "body": json.dumps(body)}
```

### When to use
- Microservices gateway and unified entry point
- Adding auth, rate limiting, and caching to third‑party APIs
- Multi‑region backends with geo‑routing at the edge

## Telecom Event Processor
Process voice, SMS, and fax events in real time with low latency, invoking business logic and downstream systems.

### Architecture
```
Telnyx Network: Voice | SMS | Fax | Number Lookup
                     │
                     ▼
         Edge Compute Function: Webhook Handler → Business Logic
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
        CRM               Analytics/Alerts
```

### Sample implementation (JavaScript)
```js
// Unified telecom event handler
export async function handler(request) {
  const webhook = await request.json();
  const type = webhook.data.event_type;
  switch (type) {
    case "call.initiated":
    case "call.answered":
    case "call.hangup":
      return handleVoiceEvent(webhook);
    case "message.received":
    case "message.sent":
      return handleSMSEvent(webhook);
    case "fax.received":
    case "fax.sent":
      return handleFaxEvent(webhook);
    default:
      console.log(`Unhandled event: ${type}`);
      return new Response("OK");
  }
}

async function handleVoiceEvent(webhook) {
  const e = webhook.data;
  const callId = e.payload.call_control_id;
  await fetch(process.env.ANALYTICS_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      type: "voice",
      event: e.event_type,
      call_id: callId,
      from: e.payload.from,
      to: e.payload.to,
      timestamp: e.occurred_at
    })
  });
  if (e.event_type === "call.initiated") {
    const caller = await lookupCaller(e.payload.from);
    if (caller.vip) {
      return generateTeXML(`
        <Response>
          <Say>Welcome back, ${caller.name}. Connecting you now.</Say>
          <Dial><Queue name="vip"/></Dial>
        </Response>
      `);
    }
  }
  return new Response("OK");
}

async function handleSMSEvent(webhook) {
  const e = webhook.data;
  if (e.event_type === "message.received") {
    const text = e.payload.text.toLowerCase();
    const from = e.payload.from.phone_number;
    if (/(stop|unsubscribe|cancel|quit)/.test(text)) {
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
  const e = webhook.data;
  await fetch(process.env.ANALYTICS_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      type: "fax",
      event: e.event_type,
      fax_id: e.payload.fax_id,
      from: e.payload.from,
      to: e.payload.to,
      pages: e.payload.page_count,
      timestamp: e.occurred_at
    })
  });
  if (e.event_type === "fax.received" && e.payload.media_url) {
    await storeFax(e.payload.fax_id, e.payload.media_url);
  }
  return new Response("OK");
}
```

### When to use
- Contact centers routing calls based on CRM history
- SMS marketing flows handling opt‑ins/outs in real time
- 2FA workflows generating and verifying SMS codes
