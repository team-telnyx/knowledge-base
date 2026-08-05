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

*Part 1 of 2 — see also: [Part 2](telnyx-api-binding--part-2.md)*

The Telnyx API binding exposes a ready-to-use, authenticated Telnyx client on `env` inside an Edge Compute function, so handlers can call the Telnyx REST API without managing API keys. This page covers the binding model, the client shape, error handling, and end-to-end examples for sending messages, receiving inbound SMS, and handling inbound voice calls.

## Overview

The Telnyx API binding puts a ready-to-use, authenticated Telnyx client on `env`. Credentials are injected at the edge and never appear in your code, bundle, or logs — there is no `new Telnyx(...)` constructor and no API key to manage.

```ts
import { env } from "@telnyx/edge-runtime";

await env.MY_TELNYX.messages.send({
  from: "+13125550100",
  to: "+13125550101",
  text: "Hello from Edge Compute",
});
```

Key properties of the binding:

- **Free-formed name** — `MY_TELNYX` is whatever you set as `binding` in `func.toml`. It becomes the property on `env`.
- **Typed** — running `telnyx-edge types` types `env.MY_TELNYX` as the Telnyx client.
- **One per organization** — every function in the org shares the same binding.

The org-level credential behind the binding (`bindings create` / `validate` / `update`) is account-level and rarely touched — see the [CLI reference](cli-reference--part-1.md).

## Declaring the binding

Add a `[telnyx]` block to the generated `func.toml`:

```toml
# func.toml
[edge_compute]
func_id = "60c5ce48-…"   # created by new-func
func_name = "balance-check"

[telnyx]
binding = "MY_TELNYX"
```

After running `telnyx-edge types`, `env.MY_TELNYX` is typed as the Telnyx client.

## Client shape

`env.MY_TELNYX` is a Telnyx API client handle. Call it like any Telnyx API client, with auth already wired in. Calls take the shape `env.MY_TELNYX.<resource>.<method>(...)`, using resource and method names — not raw HTTP paths:

- `<resource>` — a camelCase property: `messages`, `calls`, `balance`, `availablePhoneNumbers`, …
- `<method>` — a method on the resource: `.send`, `.dial`, `.list`, `.retrieve`, …

The names don't always track the HTTP API (`messages.send` is `POST /messages`, but `messages.cancelScheduled` is `DELETE /messages/{id}`), so discover them rather than guessing from endpoints:

- **Autocomplete** — after `telnyx-edge types`, your editor completes `env.MY_TELNYX.` with every resource and method.
- **[Client method reference (`api.md`)](https://github.com/team-telnyx/telnyx-node/blob/master/api.md)** — lists every `<resource>.<method>(...)` and the endpoint it maps to.
- **[HTTP API reference](/api-reference)** — endpoint parameters and behavior.

```ts
await env.MY_TELNYX.messages.send({ from: "+13125550100", to: "+13125550100", text: "Hello" }); // POST /messages
await env.MY_TELNYX.calls.dial({ connection_id: "2985…", from: "+13125550100", to: "+13125550101" }); // POST /calls
await env.MY_TELNYX.availablePhoneNumbers.list({ filter: { country_code: "US" } });               // GET /available_phone_numbers
await env.MY_TELNYX.balance.retrieve();                                                            // GET /balance
```

Each method returns the API response; list and retrieve calls expose the payload on `.data`.

## Errors

Calls reject on API errors. Catch and inspect:

```ts
try {
  await env.MY_TELNYX.messages.send({ from: "+13125550100", to: "+13125550101", text: "Hello" });
} catch (err) {
  // err.status (e.g. 400), err.message, err.error (parsed body)
}
```

## Quick start: balance check

A complete function that returns your Telnyx account balance — declared, typed, shipped, and called.

1. **Create a function**

   ```
   telnyx-edge new-func --language ts --name balance-check
   cd balance-check
   ```

2. **Declare the binding** — add the `[telnyx]` block shown above to `func.toml`.

3. **Generate types**

   ```
   telnyx-edge types
   ```

4. **Write the handler**

   ```ts
   // index.ts
   import * as http from "node:http";
   import { env } from "@telnyx/edge-runtime";

   const port = Number(process.env.PORT ?? 8080);

   http.createServer(async (req, res) => {
     // Match /health and any /health/* probe path the platform requires
     // (the scaffold generates this guard — keep it).
     if (req.url === "/health" || req.url?.startsWith("/health/")) {
       return res.writeHead(200).end();
     }

     const { data } = await env.MY_TELNYX.balance.retrieve();
     res.writeHead(200, { "content-type": "application/json" });
     res.end(JSON.stringify(data));
   }).listen(port);
   ```

5. **Ship**

   ```
   telnyx-edge ship
   ```

6. **Call it** — `ship` prints your function URL. Hit it:

   ```
   curl https://balance-check-<id>.telnyxcompute.com
   ```

   ```json
   {
     "credit_limit": "1000.00",
     "frozen": "0.00",
     "currency": "USD",
     "available_credit": "1100.00",
     "pending": "0.00",
     "balance": "100.00",
     "record_type": "balance"
   }
   ```
