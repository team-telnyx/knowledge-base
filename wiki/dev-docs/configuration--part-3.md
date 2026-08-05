---
title: Configuration
summary: Every Telnyx Edge Compute project is configured by a single TOML manifest
  at its root — `func.toml` for classic single-function projects or `telnyx.toml`
  for umbrella TypeScript projects. The manifest declares the function's identity,
  environment variables, secret bindings, storage bindings, and (for umbrella projects)
  actors; configuration changes take effect on the next `telnyx-edge ship`.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
updated_at: 2026-08-05T13:40:37Z
---

# Configuration

*Part 3 of 4 — see also: [Part 1](configuration--part-1.md), [Part 2](configuration--part-2.md), [Part 4](configuration--part-4.md)*

Every Telnyx Edge Compute project is configured by a single TOML manifest at its root — `func.toml` for classic single-function projects or `telnyx.toml` for umbrella TypeScript projects. The manifest declares the function's identity, environment variables, secret bindings, storage bindings, and (for umbrella projects) actors; configuration changes take effect on the next `telnyx-edge ship`.

## Secrets

Secrets are key-value pairs for sensitive data — API keys, database passwords, signing keys. They are scoped to your organization, stored server-side, and never displayed by the CLI after you set them. Every function receives them; there are two ways to read one.

### Managing secrets

The `secrets` commands take positional arguments:

```bash
# Add a secret — or update it, same command
telnyx-edge secrets add STRIPE_API_KEY "sk_live_abc123"
# ✓ Secret 'STRIPE_API_KEY' added successfully

# List secret keys (values are never shown)
telnyx-edge secrets list
# SECRET ID                              SECRET NAME         CREATED AT            UPDATED AT
# ------------                           ----------------    -----------------     -----------------
# 1f4cafea-21ce-4e2b-9740-17d971c3d892   DATABASE_PASSWORD   Jun 12, 2026, 09:41   Jun 12, 2026, 09:41
# 21ef7449-edbb-4248-b869-3d1352563a64   STRIPE_API_KEY      May 28, 2026, 16:20   May 28, 2026, 16:20
# a209b1b3-062c-46f6-a2f2-3b0061751190   JWT_SECRET          May 28, 2026, 16:19   May 28, 2026, 16:19

# Delete a secret
telnyx-edge secrets delete OLD_API_KEY
# ✓ Secret 'OLD_API_KEY' deleted successfully
```

Secrets are injected into function containers at deploy time — after adding or updating one, `telnyx-edge ship` each function that uses it.

### Reading secrets

**As environment variables — every language**

Each secret is injected into **all** functions in your organization as an environment variable named after its key. No declaration needed:

**TypeScript / JavaScript**

```ts
const stripeKey = process.env.STRIPE_API_KEY;
if (!stripeKey) throw new Error("STRIPE_API_KEY not configured");
```

**Python**

```python
import os

stripe_key = os.environ["STRIPE_API_KEY"]
```

**Go**

```go
stripeKey := os.Getenv("STRIPE_API_KEY")
if stripeKey == "" {
    log.Fatal("STRIPE_API_KEY not configured")
}
```

**Quarkus (Java)**

```java
String stripeKey = System.getenv("STRIPE_API_KEY");
```

**Through the typed binding — TypeScript**

TypeScript projects can additionally declare a `[secrets](secrets.md)` binding in `func.toml` and read the secret through `env.SECRETS`:

```toml
# func.toml
[secrets](secrets.md)
binding = "STRIPE_KEY"       # the handle your code uses
name    = "STRIPE_API_KEY"   # the key stored with `secrets add`
```

```bash
telnyx-edge types   # regenerates telnyx-env.d.ts from the manifest
```

```ts
import { env } from "@telnyx/edge-runtime";

const stripeKey = await env.SECRETS.get("STRIPE_KEY"); // get returns Promise<string>
```

Both surfaces read the same store. The binding adds two things: `env.SECRETS.get` accepts only the literal union of declared handles — a typo'd handle fails to compile — and the in-code handle is decoupled from the stored key name, so you can swap `name` in the manifest without touching code. The binding SDK is TypeScript-only today; other runtimes use the injected environment variables.

Enforced when `[secrets](secrets.md)` is declared: a **binding** named `SECRETS` and **duplicate `[secrets](secrets.md)` handles** are hard errors — `ship` fails. An `[env_vars]` entry named `SECRETS` only **warns** (it shadows the `env.SECRETS` namespace), so rename it. See [Bindings](bindings.md) for how the `env` namespace works.

### Rotating a secret

`add` with an existing key overwrites its value:

```bash
telnyx-edge secrets add DATABASE_PASSWORD "new-password"
telnyx-edge ship                # redeploy each function that uses it
curl https://my-func-0198c2c5-8.telnyxcompute.com/health   # verify
```

### Scoping and local development

Secrets are organization-scoped. There is no per-environment scoping (dev/staging/prod) today — if you need separation, encode it in the key name (`DEV_DATABASE_PASSWORD`, `PROD_DATABASE_PASSWORD`) and pick one in code.

There is no local secrets emulation in the CLI. When running a function locally, export the same names as ordinary environment variables:

```bash
STRIPE_API_KEY="sk_test_..." node index.js
```

### Troubleshooting

| Symptom | Fix |
| --- | --- |
| Variable missing in the function | `telnyx-edge secrets list` to confirm the key exists, then `telnyx-edge ship` — values are injected at deploy time. |
| Stale value | `secrets add` again, then `ship`. |
| `env.SECRETS.get` doesn't type-check | Re-run `telnyx-edge types` after editing `[secrets](secrets.md)`; pass the `binding` handle, not the `name`. |
| CLI rejects the command | `telnyx-edge auth status`, then `telnyx-edge auth login` if needed. |

## Routes & Domains

Every function deployed with `telnyx-edge ship` gets a public HTTPS URL. Requests to that URL are the only trigger — there are no cron, queue, or event triggers today. If you need scheduled invocation, point an external scheduler (for example, a GitHub Actions cron job) at the URL.

### Public URL pattern

```
https://{func-name}-{func-id-prefix}.telnyxcompute.com
```

| Component | Description |
| --- | --- |
| `func-name` | The `func_name` from your `func.toml` |
| `func-id-prefix` | The first 10 characters of the function's `func_id` |

A function named `hello-world` with `func_id` `0198c2c5-8f1e-7a3d-9b21-6e4a0d5f1c88` is served at:

```
https://hello-world-0198c2c5-8.telnyxcompute.com
```

`telnyx-edge ship` prints the URL after a successful deploy:

```
📡 Your function is live at:
   https://hello-world-0198c2c5-8.telnyxcompute.com

💡 Test your function:
   curl https://hello-world-0198c2c5-8.telnyxcompute.com
```

`telnyx-edge list` shows the invoke URL for every function in your organization.

### Calling your function

All HTTP methods and paths under the function's URL are routed to your server — path handling is up to your code (see [HTTP handler](http-handler.md)):

```bash
# GET request
curl https://hello-world-0198c2c5-8.telnyxcompute.com

# POST request with JSON body
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "test"}' \
  https://hello-world-0198c2c5-8.telnyxcompute.com/anything
```

Requests time out after 30 seconds by default (60 seconds maximum) — see [Limits](limits.md).

### Custom domains

There is no custom domain support today — functions are reachable only at their `telnyxcompute.com` URL. To serve a function from your own domain, put a proxy you operate (CDN or reverse proxy) in front of it.

### Region placement

You can't pin a function to a region today; the platform chooses placement.
