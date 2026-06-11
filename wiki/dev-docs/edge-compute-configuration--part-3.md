---
title: Edge Compute Configuration
summary: Covers all aspects of configuring Telnyx Edge Compute functions, including
  the func.toml file, environment variables, secrets management, routing, cron triggers,
  deployment versions, and best practices for performance, reliability, security,
  and observability.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices
  content_hash: ebd5b8ce19ade9b4d6259f150c48431da686a351a12568dbe87a0eb9782e6f2f
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
  content_hash: 2b5e37aab24cf188062e87c580f9098a7cbfe0dadad94edb5c38ba971c359d80
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
  content_hash: b4a08fa2a80a87df06159ed54c39b13b4fbba633d8ef62213988b1590fe903d6
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
  content_hash: a27db27bb4f6e787f0896af40111e1ac2a1bdee41700ced14ddeb938ecc7a33c
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
  content_hash: b87a71c2265cf4d900a92c74332ba1fd79fe8630a015bafa76793f4d6dd6d214
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
  content_hash: 2044c95976564f15c55848354720503297f83f88f442135ca948035bcd7c319d
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
  content_hash: a3661d4f38cd0f1db37a998d0f66a2f97b3143e9710c5fafc18b0fcc7808d56d
updated_at: 2026-06-11T10:26:17Z
---

# Edge Compute Configuration

*Part 3 of 3 — see also: [Part 1](edge-compute-configuration--part-1.md), [Part 2](edge-compute-configuration--part-2.md)*

Covers all aspects of configuring Telnyx Edge Compute functions, including the func.toml file, environment variables, secrets management, routing, cron triggers, deployment versions, and best practices for performance, reliability, security, and observability.

## Versions and Deployments

Version history and rollback commands are planned for a future release. Version management will let you track deployments, roll back to previous versions, and implement gradual rollout strategies.

### Current Deployment Model

Today, `telnyx-edge ship` deploys your function as an atomic update. Each deployment fully replaces the previous version.

### Current Rollback Strategy

Until rollback commands are available, use Git:

```bash
# Revert to previous commit
git revert HEAD
telnyx-edge ship
```

Or checkout a specific version:

```bash
git log --oneline
git checkout abc123 .
telnyx-edge ship
```

## Configuration Best Practices

### Set Appropriate Timeouts

Configure timeouts based on your function's needs in `func.toml`:

```toml
[edge_compute]
timeout_seconds = 30  # Default: 30, Max: 300
```

### Use Descriptive Function Names

Function names become part of your URL. Choose wisely:

```bash
# ✅ Good
telnyx-edge new-func --name=user-api
telnyx-edge new-func --name=webhook-handler

# ❌ Bad
telnyx-edge new-func --name=func1
telnyx-edge new-func --name=test
```

## Performance Best Practices

### Reuse Connections

Initialize clients once at module level, not per request:

```javascript
// ✅ Good — client initialized once, reused across requests
const client = new HttpClient({ timeout: 5000 });

export async function handler(request) {
    const response = await client.get('https://api.example.com/data');
    return new Response(JSON.stringify(response));
}
```

```javascript
// ❌ Bad — new client created every request
export async function handler(request) {
    const client = new HttpClient({ timeout: 5000 });
    const response = await client.get('https://api.example.com/data');
    return new Response(JSON.stringify(response));
}
```

### Minimize Cold Starts

Cold starts happen when a new container spins up. Reduce their impact by:

1. **Lazy-loading dependencies** — Only import what you need, when you need it
2. **Keeping functions small** — Smaller code = faster load
3. **Using lightweight frameworks** — Hono over Express, FastAPI over Django

```javascript
// ✅ Good — lazy load heavy dependency
let heavyLib;
function getHeavyLib() {
    if (!heavyLib) {
        heavyLib = require('heavy-library');
    }
    return heavyLib;
}

export async function handler(request) {
    if (needsHeavyProcessing(request)) {
        const lib = getHeavyLib();
        // use lib
    }
}
```

### Cache Expensive Operations

Use KV for caching API responses and computed data:

```javascript
async function getUser(userId) {
    const cached = await kv.get(`user:${userId}`);
    if (cached) return JSON.parse(cached);

    const user = await fetchUserFromDB(userId);
    await kv.put(`user:${userId}`, JSON.stringify(user), { ttl: 300 });

    return user;
}
```

## Reliability Best Practices

### Handle Errors Gracefully

Always return proper error responses:

```javascript
export async function handler(request) {
    try {
        const data = await riskyOperation();
        return new Response(JSON.stringify(data), {
            headers: { "Content-Type": "application/json" }
        });
    } catch (error) {
        console.error("Operation failed:", error.message);

        return new Response(JSON.stringify({
            error: "Internal server error",
            requestId: request.headers.get("X-Request-ID")
        }), {
            status: 500,
            headers: { "Content-Type": "application/json" }
        });
    }
}
```

### Set Timeouts on External Calls

Don't let slow external services hang your function:

```javascript
const controller = new AbortController();
const timeout = setTimeout(() => controller.abort(), 5000);

try {
    const response = await fetch('https://api.example.com/data', {
        signal: controller.signal
    });
    clearTimeout(timeout);
    return response;
} catch (error) {
    if (error.name === 'AbortError') {
        return new Response('External service timeout', { status: 504 });
    }
    throw error;
}
```

### Implement Retries with Backoff

For critical operations, add retry logic with exponential backoff:

```javascript
async function fetchWithRetry(url, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
        try {
            const response = await fetch(url);
            if (response.ok) return response;

            if (response.status < 500) throw new Error(`HTTP ${response.status}`);
        } catch (error) {
            if (i === maxRetries - 1) throw error;

            await new Promise(r => setTimeout(r, Math.pow(2, i) * 100));
        }
    }
}
```

## Security Best Practices

### Validate Input

Never trust user input. Validate required fields, check formats, and sanitize data:

```javascript
export async function handler(request) {
    const body = await request.json();

    if (!body.email || typeof body.email !== 'string') {
        return new Response(JSON.stringify({ error: 'Invalid email' }), { status: 400 });
    }

    if (!isValidEmail(body.email)) {
        return new Response(JSON.stringify({ error: 'Invalid email format' }), { status: 400 });
    }

    const email = body.email.toLowerCase().trim();
    // ...
}
```

### Use HTTPS for External Calls

Always use HTTPS when calling external services. Never hardcode secrets; use the secrets API instead:

```bash
telnyx-edge secrets add API_KEY --value "sk-..."
```

Then access in code:

```javascript
const apiKey = process.env.API_KEY;
```

### Don't Log Sensitive Data

Be careful what you log:

```javascript
// ✅ Good — log request metadata
console.log(`Request: ${request.method} ${request.url}`);

// ❌ Bad — logging secrets
console.log(`API Key: ${process.env.API_KEY}`);

// ❌ Bad — logging full request body (may contain PII)
console.log(`Body: ${JSON.stringify(body)}`);
```

## Observability Best Practices

### Add Request IDs

Track requests through your system by reading or generating a request ID:

```javascript
export async function handler(request) {
    const requestId = request.headers.get('X-Request-ID') || crypto.randomUUID();

    console.log(`[${requestId}] Processing request`);

    return new Response(JSON.stringify({ data }), {
        headers: {
            "Content-Type": "application/json",
            "X-Request-ID": requestId
        }
    });
}
```

### Log at Appropriate Levels

Use log levels effectively:

```javascript
const logger = {
    debug: (msg) => process.env.LOG_LEVEL === 'debug' && console.log(`[DEBUG] ${msg}`),
    info: (msg) => console.log(`[INFO] ${msg}`),
    warn: (msg) => console.warn(`[WARN] ${msg}`),
    error: (msg) => console.error(`[ERROR] ${msg}`)
};

logger.debug(`Cache hit for key: ${key}`);      // Verbose debugging
logger.info(`User ${userId} created`);           // Normal operations
logger.warn(`Retry attempt ${i} for ${url}`);    // Concerning but handled
logger.error(`Database connection failed`);      // Errors requiring attention
```
