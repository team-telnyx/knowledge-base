---
title: Stateful Actors - Index
summary: Stateful Actors on Telnyx Edge Compute give each named entity its own durable,
  single-threaded instance with private key/value and SQL storage, alarms, and WebSocket
  support. This page covers when to use them, the storage surfaces, local development,
  the Quick Start, shared actors across functions, and WebSocket patterns.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/storage/key-value/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/storage/sql
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/when-to-use
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/local-development
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/quick-start/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/shared-actors
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/websockets/index
updated_at: 2026-08-05T13:43:37Z
---

# Stateful Actors - Index

*Part 5 of 7 — see also: [Part 1](stateful-actors-index--part-1.md), [Part 2](stateful-actors-index--part-2.md), [Part 3](stateful-actors-index--part-3.md), [Part 4](stateful-actors-index--part-4.md), [Part 6](stateful-actors-index--part-6.md), [Part 7](stateful-actors-index--part-7.md)*

Stateful Actors on Telnyx Edge Compute give each named entity its own durable, single-threaded instance with private key/value and SQL storage, alarms, and WebSocket support. This page covers when to use them, the storage surfaces, local development, the Quick Start, shared actors across functions, and WebSocket patterns.

## Shared Actors

A **shared actor** is a single Stateful Actor type reachable from two or more Edge Compute functions on the same account. The function that ships the actor class **owns** the actor; other functions on the same account declare the same `type` under their own `binding` name and ship **no** class — their binding routes to the owner's actor and its state.

![Shared actor topology: an owner function ships the Account class under binding ACCOUNT; a reference function ships no class and declares the same type under binding READONLY; both bindings route to one durable Account actor on the same Telnyx account.](https://mintcdn.com/telnyx/Uty9JSANtZnOoIv9/img/stateful-actors-shared-actor-light.svg?fit=max&auto=format&n=Uty9JSANtZnOoIv9&q=85&s=45db0041c15be9329c6fbfbe84e0fd9b)

![Shared actor topology: an owner function ships the Account class under binding ACCOUNT; a reference function ships no class and declares the same type under binding READONLY; both bindings route to one durable Account actor on the same Telnyx account.](https://mintcdn.com/telnyx/Uty9JSANtZnOoIv9/img/stateful-actors-shared-actor-dark.svg?fit=max&auto=format&n=Uty9JSANtZnOoIv9&q=85&s=1eb51b67d0567051e22ab4d384504722)

### Why Share an Actor

- **Split read and write paths** into separate functions with their own auth, rate limits, and deploy cadence — without duplicating state.
- **Let a second function call into a domain the first one owns** (e.g., a reporting function reads an account actor that a payments function owns).
- **Keep one durable actor behind many entrypoints.** Both functions talk to the same per-name state; writes through one binding are visible to reads through the other.

Both functions must be on the **same account** — shared actors are bounded by account.

### The Pattern

The owner function is a normal Stateful Actor project — it ships the class. The reference function declares the same `type` under a different `binding` and ships **no** actor class — its binding routes to the owner's actor and state; no second instance is created.

There's no `new-func` flag for "reference-only," so the workflow is: scaffold with `--actor` (to mint a `func_id` and write `telnyx.toml`), then drop the actor class and rename the binding.

### Walkthrough: a Read-Only Account Reference

Prereq: an owner function for the type already shipped on your account (the `account` from the Quick Start, type `Account`).

**1. Mint a `func_id` and scaffold, then drop the class**

```
telnyx-edge new-func --actor --name=account-readonly   # registers the func, writes func_id
cd account-readonly
rm -f src/counter.ts                                    # the ref ships no actor class
```

**2. Point `telnyx.toml` at the owner's type under a new binding**

Edit the `[actors](actors.md)` block — keep `type` equal to the owner's type, change `binding`:

```toml
[actors](actors.md)
binding = "READONLY"    # this func's own handle
type    = "Account"     # SAME type the owner declares → shared actor
```

Leave `name`, `main`, `compatibility_date`, and the `[edge_compute]` `func_id` as scaffolded.

**3. Replace `src/index.ts` with a class-free handler that calls `env.READONLY`**

```typescript
import {
  type ActorNamespace,
  type ActorStub,
  type IdFromNameOptions,
} from "@telnyx/edge-runtime";

// Hand-rolled stub narrowing (mirrors the owner's read surface; no local class).
type AccountStub = ActorStub & {
  balance(): Promise<{ balance: number }>;
};
interface AccountNamespace extends ActorNamespace {
  idFromName(name: string, options?: IdFromNameOptions): AccountStub;
}
interface Env { READONLY: AccountNamespace }   // <- the binding from telnyx.toml

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    if (url.pathname === "/health/liveness") return new Response("ok");
    if (url.pathname === "/health/readiness") return new Response("ok");

    // Read-only view: balance for an account
    const m = url.pathname.match(/^\/accounts\/([^/]+)\/balance$/);
    if (m && req.method === "GET") {
      const result = await env.READONLY.idFromName(m[1]!).balance();
      return Response.json({ account: m[1], ...result, via: "READONLY->Account(shared)" });
    }
    return new Response("not found", { status: 404 });
  },
};
```

**Key point:** no `export class Account` in this file. The bundler roots at `main`, so with nothing importing the class, the reference bundle ships class-free (a few KB) — that's what makes it reference-only.

**4. Install deps and ship (same as the owner)**

```
npm install
telnyx-edge ship
```

**5. Prove they share one actor**

```
REF=https://account-readonly-<id>.telnyxcompute.com
OWN=https://account-<id>.telnyxcompute.com

# Write via the owner (ACCOUNT binding) — carol is a fresh account name
curl -sS -X POST $OWN/accounts/carol/deposit \
  -H 'content-type: application/json' -d '{"amount":100}'

# Read via the reference (READONLY binding) → same balance
curl -sS $REF/accounts/carol/balance
# → {"account":"carol","balance":100,"via":"READONLY->Account(shared)"}
```

Write through `ACCOUNT`, read through `READONLY`, same `balance` → one durable actor (Account), two functions. Both must be on the same account; the reference's `type` must exactly match the owner's.

### Rules of Thumb

- **Same account, same `type`.** Reference bindings whose `type` doesn't match an owner already on the account won't resolve.
- **Only one function owns the class.** The owner ships the actor class; every other function declares the same `type` and ships no class.
- **Renaming the binding is fine.** Each function picks its own `binding` name — that's the property on `env` for that function. The `type` is what glues them together.
- **Reference bundles are small.** With no class import, the bundler emits a class-free bundle. Keep it that way: don't import the actor class from your reference function.
