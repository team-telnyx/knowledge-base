---
title: Power AI Assistants with Edge Compute
summary: Walks through building a single Go Edge Compute function that serves as both
  the dynamic-variables webhook and a webhook tool backend for a Telnyx AI Assistant,
  including Ed25519 signature verification, body-shape dispatch, secret management,
  deployment, and end-to-end testing.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/guides/ai-assistant-backend
updated_at: 2026-08-05T13:40:59Z
---

# Power AI Assistants with Edge Compute

*Part 1 of 3 — see also: [Part 2](power-ai-assistants-with-edge-compute--part-2.md), [Part 3](power-ai-assistants-with-edge-compute--part-3.md)*

Walks through building a single Go Edge Compute function that serves as both the dynamic-variables webhook and a webhook tool backend for a Telnyx AI Assistant, including Ed25519 signature verification, body-shape dispatch, secret management, deployment, and end-to-end testing.

## Overview

Telnyx AI Assistants can call out to your own backend in several scenarios — resolving dynamic variables at the start of a conversation, executing webhook tool calls mid-conversation, and more. Whenever you need a backend for these callbacks, [Edge Compute](edge-compute.md) is a natural fit: no server to manage, secrets injected at runtime, and deployment via a single CLI command.

This guide walks through building a single Go function that handles both dynamic variables and webhook tool calls, using the demo app `telnyx-ai-edge` as the reference implementation.

## What you'll build

A support assistant for "Telnyx Logistics" that:

- Greets callers by name (dynamic variables resolved from the caller's phone number)
- Has a `lookup-order` tool the assistant can call to retrieve order status, carrier, and estimated delivery

Both the dynamic variable lookup and the tool call hit one Edge Compute function at a single URL.

## Prerequisites

- A Telnyx account with [Edge Compute](edge-compute.md) enabled.
- The `telnyx-edge` CLI installed and authenticated (see the [Edge Compute](edge-compute.md) quickstart).
- An existing [AI Assistant](https://portal.telnyx.com/#/ai/assistants) (or you can create one via API as shown below).
- Go 1.24+ installed locally (if following along with the Go sample).

## Key concepts

### Single function, two callbacks

Edge Compute routes all HTTP methods and paths under your function URL to your handler — path handling is up to your code (see [Routes & Domains](routes-domains.md)). The platform handles `/health/liveness` and `/health/readiness` probes automatically.

In this guide, both the dynamic variables webhook and the webhook tool call point to the same function URL, so the handler dispatches on the **request body shape** rather than the URL path:

- **Dynamic variables webhook** — Telnyx wraps the payload under `data.event_type`.
- **Webhook tool call** — the body is the flat arguments object from the tool's `body_parameters` schema (e.g. `{"order_id": "ORD-10042"}`).

You could also use separate paths (e.g. `/dynamic-variables` and `/tool/lookup-order`) if you prefer path-based routing — both approaches work. This guide uses body-shape dispatch to keep everything at a single URL.

### Webhook signature verification

Telnyx signs every dynamic-variables webhook and webhook tool call with an Ed25519 key. The signature is in the `telnyx-signature-ed25519` header, and the timestamp is in `telnyx-timestamp`. The signed message is `"{timestamp}|{raw_body}"`.

You must verify this signature to confirm the request is genuinely from Telnyx. Your org's public key is available at:

```
GET https://api.telnyx.com/v2/public_key
Authorization: Bearer <TELNYX_API_KEY>
```

The response contains `data.public` (not `data.public_key`) — the base64-encoded Ed25519 public key.

### Dynamic variables response format

The response **must** nest variables under a `dynamic_variables` key. A flat object (e.g. `{"customer_name": "James"}`) is silently ignored — variables will remain unresolved.

```json
{
  "dynamic_variables": {
    "customer_name": "James Smith",
    "account_tier": "premium"
  }
}
```

### Timeout

The default dynamic variables webhook timeout is 1,500 ms. Edge Compute functions may occasionally need more time on a cold start, so consider setting `dynamic_variables_webhook_timeout_ms` on the assistant to a higher value (up to 10,000 ms). A value of 8,000 ms is a reasonable choice for edge backends.

## Step 1: Scaffold the function

```
telnyx-edge new-func -l go -n telnyx-ai-edge
cd telnyx-ai-edge
```

This creates a `func.toml` with the registered function ID and a Go handler scaffold.

The Go module **must** be named `function` (package `function`, entrypoint `Handle(w, r)`). Other module names fail to build: "malformed module path: missing dot in first path element." Use `go 1.24` in `go.mod`.

## Step 2: Store the public key as a secret

Fetch your org's public key and store it as an encrypted secret. The public key endpoint requires authentication — use your Telnyx API key:

```
# Get the public key (requires authentication)
PUBLIC_KEY=$(curl -s -H "Authorization: Bearer $TELNYX_API_KEY" \
  https://api.telnyx.com/v2/public_key | jq -r '.data.public')

# Store it as a secret (encrypted, org-scoped, injected as env var at runtime)
telnyx-edge secrets add TELNYX_PUBLIC_KEY "$PUBLIC_KEY"
```

The function reads this secret from `os.Getenv("TELNYX_PUBLIC_KEY")` at startup. Secrets are never visible in `secrets list` — only the name is shown.
