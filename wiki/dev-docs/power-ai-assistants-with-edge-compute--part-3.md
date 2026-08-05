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

*Part 3 of 3 — see also: [Part 1](power-ai-assistants-with-edge-compute--part-1.md), [Part 2](power-ai-assistants-with-edge-compute--part-2.md)*

Walks through building a single Go Edge Compute function that serves as both the dynamic-variables webhook and a webhook tool backend for a Telnyx AI Assistant, including Ed25519 signature verification, body-shape dispatch, secret management, deployment, and end-to-end testing.

## Tips and gotchas

### Choosing body-shape vs path-based dispatch

Since Edge Compute routes all paths to your handler, you can use path-based routing (e.g. `r.URL.Path == "/tool/lookup-order"`) or body-shape dispatch as shown in this guide. Both work. If you configure separate URLs for the DV webhook and the tool on the assistant, path-based routing is natural. If you point both at the same URL, body-shape dispatch is the way to go.

For a path-based routing example, see the [RESTful API example](https://github.com/team-telnyx/edge-compute-cli/tree/main/docs/examples/python/restful-api) in the Edge Compute CLI repo.

### Consider a higher webhook timeout

The default dynamic variables webhook timeout is 1,500 ms. Edge Compute functions may occasionally need a bit more time on a cold start, so consider setting `dynamic_variables_webhook_timeout_ms` to 8,000 ms to give the function room. The maximum is 10,000 ms.

### Always verify signatures

Without signature verification, anyone who knows your function URL can inject fake dynamic variables or tool responses. The `telnyx-signature-ed25519` and `telnyx-timestamp` headers are present on every request from Telnyx.

### Ship takes a few minutes

A normal ship takes 2–3 minutes. The CLI's build monitor has a 5-minute timeout, but the build continues server-side regardless. If the CLI reports a timeout, check `telnyx-edge list` for the actual status before retrying — the function may have deployed successfully.

### Secrets require re-shipping

Adding or changing a secret (`telnyx-edge secrets add`) does not affect an already-deployed function. Run `telnyx-edge ship` again to pick up the new secret.

### The `dynamic_variables` wrapper is mandatory

Returning a flat JSON object like `{"customer_name": "James"}` will be silently ignored. Variables must be nested under `dynamic_variables`:

```json
{
  "dynamic_variables": {
    "customer_name": "James"
  }
}
```

## Next steps

- [Dynamic Variables](dynamic-variables.md) — full reference for the DV webhook payload and resolution precedence.
- [Webhook signing](https://developers.telnyx.com/docs/development/api-fundamentals/webhooks/receiving-webhooks#webhook-signing) — how Telnyx signs webhooks and how to verify signatures.
- [Edge Compute](edge-compute.md) quickstart — getting started with your first function.
- [Secrets](secrets.md) — encrypted, org-scoped environment variables.
- [Bindings](bindings.md) — pre-authenticated Telnyx API client for your function.
