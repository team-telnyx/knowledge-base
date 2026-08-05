---
title: Stateful Actors
summary: A stateful actor is a single-threaded server that owns the state of one entity
  — one user, one cart, one call leg, one chat room. You write it as a TypeScript
  class; the platform runs one instance per name, routes every call for that name
  to that instance, runs your methods one at a time, and persists what you write.
  This page covers the runtime guarantees, the API surface (base class, context, storage,
  namespace, stub, alarms, errors, configuration), the execution model, lifecycle
  and placement, addressing, and project structure.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/alarms
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/base
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/configuration
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/context
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/errors
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/namespace
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/storage
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/stub
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/addressing
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/how-it-works/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/lifecycle
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/project-structure/index
updated_at: 2026-08-05T13:42:53Z
---

# Stateful Actors

*Part 3 of 7 — see also: [Part 1](stateful-actors--part-1.md), [Part 2](stateful-actors--part-2.md), [Part 4](stateful-actors--part-4.md), [Part 5](stateful-actors--part-5.md), [Part 6](stateful-actors--part-6.md), [Part 7](stateful-actors--part-7.md)*

A stateful actor is a single-threaded server that owns the state of one entity — one user, one cart, one call leg, one chat room. You write it as a TypeScript class; the platform runs one instance per name, routes every call for that name to that instance, runs your methods one at a time, and persists what you write. This page covers the runtime guarantees, the API surface (base class, context, storage, namespace, stub, alarms, errors, configuration), the execution model, lifecycle and placement, addressing, and project structure.

## Execution Model

The runtime makes four guarantees. Each is the managed form of a mechanism you'd otherwise build by hand — the C server and mapping table in [How It Works](how-it-works.md) show where each one comes from. Stated precisely:

**1. Exactly one instance per name.** `idFromName("acct_123")` routes every call for that name to one owner — the shard map and router you'd otherwise build by hand, done for you. No two hosts run account `acct_123` at once, so the instance is the source of truth for that account.

**2. One call at a time — no concurrency inside an instance.** This is the per-account `pthread_mutex`, except you don't write it and can't forget it. One thread per instance runs each method to completion before the next starts. `await` yields the thread, but the next call still won't start until your method returns. The C `debit` is correct *because* it holds the lock across the change; the actor `debit` is correct because two debits on one account never run at the same time.

**3. Writes are durable before the caller sees a result.** This is `write()` + `fsync()` before you reply. When your method returns, the runtime holds the response until every write you issued has been flushed — the caller can't observe a result built on an unflushed write. (If a write rejects after the method returns, the call fails with `ActorOutputGateError` instead of returning success.)

**4. Only persisted state survives; memory is a cache.** This is "the on-disk snapshot + log is the truth; the in-memory map is a cache." An instance can be evicted or restarted between any two calls — a deploy, idle eviction, host failure — and instance fields (`this.x`) vanish while `ctx.storage` does not. The runtime does the snapshotting and recovery; you just read from `storage`. Treat memory exactly like a process that can be `SIGKILL`ed at any instant: only what you flushed to `storage` is real.

## Lifecycle and Placement

A stateful actor instance is activated on demand, kept in memory while it's busy, evicted when idle, and can be restarted or relocated at any time. You don't manage any of this — but you design around it, because **only what you write to `storage` survives.**

### Where it runs

An instance is placed on **first touch** — the first method call to a name brings it up. After that you address it by name, never by location; the platform routes every call to wherever the instance currently lives. (`idFromName` accepts a `locationHint` option, reserved for regional placement — see [Actor Namespace](actor-namespace.md).)

### Activation and eviction

- **Activated on demand.** Naming an instance is cheap; the first method call to a name brings the instance up and routes the call to it.
- **Kept warm while busy, evicted when idle.** Between calls, an idle instance may be removed from memory to free resources, then re-activated on the next call.
- **Restarted on deploy or host failure.** A new code version or a host issue tears the instance down and re-creates it.

### What survives a restart

In-memory state — instance fields like `this.x` — is a **cache**. It vanishes on eviction, restart, or relocation. Your actor's `storage` is the **truth**: it is durable and reloaded when the instance next activates. Treat memory exactly like a process that can be `SIGKILL`ed at any instant — only what you flushed to `storage` is real. (This is guarantee 4 in [Execution Model](execution-model.md).) A common pattern is to load from `storage` once on activation and cache the result in memory; just never assume the cache is still there.

## Addressing

`env.<BINDING>` is your handle to an actor class. You name an instance, get a **stub**, and call methods on it.

### Two ways to name an instance

```ts
env.ACCOUNT.idFromName("acct_123") // deterministic — your shard key; same name, same instance
env.ACCOUNT.newUniqueId()          // random — mints a fresh, unguessable identity
```

- **`idFromName(name)`** is deterministic: the same `name` always lands on the same instance, from anywhere. This is the common case — pick a stable identity for the entity and let the platform route to its state.
- **`newUniqueId()`** mints a fresh, unguessable instance; you store the id (`stub.id`) yourself. It currently fails at call time on the platform (a known runtime issue — see [Actor Namespace](actor-namespace.md)); until it's fixed, mint an identity yourself and pass it to `idFromName`.

### Choosing a name

The name *is* your shard key — choose the entity's natural identity: a caller's E.164 number, a user or account id, a room id, or a composite key (`tenant:room`). Same name → same single-threaded instance → coherent state for that entity. Spreading load means choosing names that spread across entities; a single hot name is one single-threaded bottleneck.

### Calling the stub

Both calls return a **stub**. Calling a method on the stub is an RPC to that one instance: the call is queued there, your method runs, the value comes back.

## Project Structure

A Stateful Actor project ships from **one module that exports two things**, wired together by a binding declared in `telnyx.toml`.

### Two exports

One module exports the **actor class** and a **`fetch` handler** — an ordinary Edge Compute function that calls the actor through a binding on `env`. The deploy pipeline routes each export to the right runtime.

```ts
import { type ActorNamespace, type ActorStub } from "@telnyx/edge-runtime";
import { Account } from "./account";
export { Account };

type AccountStub = ActorStub & Pick<Account, "debit">;
interface AccountNamespace extends ActorNamespace {
  idFromName(name: string): AccountStub;
}
interface Env { ACCOUNT: AccountNamespace }

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const acct = new URL(req.url).pathname.slice(1);      // /acct_123
    const { amount } = (await req.json()) as { amount: number };
    const result = await env.ACCOUNT.idFromName(acct).debit(amount);
    return Response.json(result);
  },
};
```

### The binding

`env.ACCOUNT` is declared in `telnyx.toml` as an `[actors](actors.md)` entry — `binding` is the property on `env`, `type` is the class to instantiate per name:

```toml
name = "account-svc"
main = "src/index.ts"

[actors](actors.md)
binding = "ACCOUNT"   # the property on env — your handle
type    = "Account"   # the class to instantiate per name
```

## Configuration

A Stateful Actor project uses the umbrella `telnyx.toml` manifest (the same file your `[secrets](secrets.md)` and `[telnyx]` bindings live in). The actor declaration is a `[actors](actors.md)` array:

```toml
name = "account"                # function name
main = "src/index.ts"          # entry — exports the fetch handler (and the class, if this func owns the type)
compatibility_date = "2026-05-01"

[actors](actors.md)
binding = "ACCOUNT"           # the property on env — your handle
type    = "Account"           # the class to instantiate per name
```

| Field | Meaning |
| --- | --- |
| `name` | Function name (used by the platform to register the func) |
| `main` | Entry module — exports the `default { fetch }` handler, plus the actor class when this function owns the type (a reference binding ships no class) |
| `compatibility_date` | Runtime compatibility pin |
| `[actors](actors.md) binding` | The name you'll use as `env.<binding>` from your function |
| `[actors](actors.md) type` | The class name to instantiate per actor name |

Constraints, enforced at ship time: `binding` and `type` must be identifiers and must not contain `__`; `type` is capped at 32 characters; binding names must be unique across all bindings in the file, and `SECRETS` is reserved as a binding name when the file has a `[secrets](secrets.md)` block. Multiple `[actors](actors.md)` blocks are allowed — including two bindings pointing at the same `type`.
