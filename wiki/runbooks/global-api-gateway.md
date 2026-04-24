---
title: Global API Gateway
summary: Route API traffic globally with caching, auth, and rate limiting.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
    content_hash: 39ee18682a537e61f85f6a087a203876e001b87c076aefeeaf552e6bc02fb5fe
updated_at: 2026-04-10T00:00:00Z
---

# Global API Gateway

Route API traffic globally with caching, auth, and rate limiting.

A globally distributed API gateway that provides authentication, rate limiting, and caching for backend services.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Client Requests                              │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    Telnyx Edge (Global PoPs)                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   Auth      │→ │Rate Limiter │→ │   Cache     │→ │   Router    │ │
│  │ Middleware  │  │             │  │   Layer     │  │             │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              ┌──────────┐  ┌──────────┐  ┌──────────┐
              │ Service  │  │ Service  │  │ Service  │
              │    A     │  │    B     │  │    C     │
              └──────────┘  └──────────┘  └──────────┘
```

## Components

| Component     | Product      | Purpose                     |
| ------------- | ------------ | --------------------------- |
| Edge Function | Edge Compute | Request processing, routing |
| Rate Limiting | Edge KV      | Distributed counters        |
| Caching       | Edge KV      | Response cache              |
| Auth          | Secrets      | JWT verification keys       |

## Implementation

```python theme={null}
import os
import jwt
import json
import hashlib
from datetime import datetime
from urllib.parse import urlparse, urlencode, parse_qs

class APIGateway:
    def __init__(self):
        self.jwt_secret = os.getenv("JWT_SECRET")
        self.rate_limit = 100  # requests per minute

    async def handler(self, request):
        # 1. Authentication
        auth_result = self.authenticate(request)
        if auth_result["error"]:
            return self.json_response(auth_result, 401)

        user_id = auth_result["user_id"]

        # 2. Rate limiting
        if await self.is_rate_limited(user_id):
            return self.json_response(
                {"error": "Rate limit exceeded"}, 
                429,
                {"Retry-After": "60"}
            )

        # 3. Cache check
        cache_key = self.cache_key(request)
        cached = await self.kv.get(cache_key)
        if cached:
            return self.json_response(json.loads(cached))

        # 4. Route to backend
        response = await self.route_request(request)

        # 5. Cache response
        if response["status"] == 200:
            await self.kv.put(cache_key, json.dumps(response), ttl=300)

        return response

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return {"error": "Missing token", "user_id": None}

        token = auth_header[7:]
        try:
            payload = jwt.decode(token, self.jwt_secret, algorithms=["HS256"])
            return {"error": None, "user_id": payload["sub"]}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token", "user_id": None}

    async def is_rate_limited(self, user_id):
        key = f"rate:{user_id}:{datetime.utcnow().strftime('%Y%m%d%H%M')}"
        count = int(await self.kv.get(key) or 0)

        if count >= self.rate_limit:
            return True

        await self.kv.put(key, str(count + 1), ttl=60)
        return False

    def cache_key(self, request):
        # Generate cache key from method + path + query string
        return f"cache:{request.method}:{request.path}:{hashlib.md5(request.url.encode()).hexdigest()}"

    async def route_request(self, request):
        parsed = urlparse(request.url)
        path = parsed.path
        query = parsed.query  # Preserve query string

        # Route based on path prefix
        if path.startswith("/api/users"):
            backend = "https://users-service.internal"
        elif path.startswith("/api/orders"):
            backend = "https://orders-service.internal"
        else:
            return self.json_response({"error": "Not found"}, 404)

        # Forward request with query string preserved
        upstream_url = f"{backend}{path}"
        if query:
            upstream_url = f"{upstream_url}?{query}"

        response = await fetch(upstream_url, {
            "method": request.method,
            "headers": request.headers,
            "body": await request.text() if request.method != "GET" else None
        })

        return {
            "status": response.status,
            "headers": dict(response.headers),
            "body": await response.text()
        }
```

## Use Cases

* **Microservices gateway** — Unified entry point for distributed services
* **Third-party API proxy** — Add auth and rate limiting to external APIs
* **Multi-region deployment** — Route to nearest backend region
