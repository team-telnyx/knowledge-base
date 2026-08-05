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

*Part 1 of 7 — see also: [Part 2](stateful-actors--part-2.md), [Part 3](stateful-actors--part-3.md), [Part 4](stateful-actors--part-4.md), [Part 5](stateful-actors--part-5.md), [Part 6](stateful-actors--part-6.md), [Part 7](stateful-actors--part-7.md)*

A stateful actor is a single-threaded server that owns the state of one entity — one user, one cart, one call leg, one chat room. You write it as a TypeScript class; the platform runs one instance per name, routes every call for that name to that instance, runs your methods one at a time, and persists what you write. This page covers the runtime guarantees, the API surface (base class, context, storage, namespace, stub, alarms, errors, configuration), the execution model, lifecycle and placement, addressing, and project structure.

## Overview

A **stateful actor** is a single-threaded server that owns the state of one entity — one user, one cart, one call leg, one chat room. You write it as a TypeScript class; the platform runs **one instance per name**, routes every call for that name to that instance, runs your methods **one at a time**, and **persists** what you write. You never bind a socket, take a lock, or shard it.

```ts
import { StatefulActor } from "@telnyx/edge-runtime";

export class Account extends StatefulActor {
  async debit(amount: number): Promise<{ ok: boolean; balance: number }> {
    const balance = (await this.ctx.storage.get<number>("balance")) ?? 0;
    if (balance < amount) return { ok: false, balance };   // check-then-act, no lock
    await this.ctx.storage.put("balance", balance - amount);
    return { ok: true, balance: balance - amount };
  }
}
```

That `debit` is a read-modify-write with no lock and no transaction. In a normal request handler that's a race; here it isn't — and that property is the whole product. See [How It Works](how-it-works.md) for the derivation from first principles, starting from a plain C server.

Two words used precisely throughout these docs: the **actor** is the class you ship (`Account`); an **instance** is its per-name materialization (`idFromName("acct_123")` reaches the `acct_123` instance of `Account`).

## Runtime Guarantees

The runtime makes four guarantees. Each is the managed form of a mechanism you'd otherwise build by hand.

- **One instance per name** — `idFromName("acct_123")` routes every call to a single owner; no two hosts run it at once.
- **One call at a time** — single-threaded dispatch. No locks, no races inside an instance.
- **Durable before reply** — a method's result isn't returned until the writes it made are persisted.
- **Memory is a cache** — only what you write to `storage` survives eviction or restart.

[Execution Model](execution-model.md) states each precisely; [How It Works](how-it-works.md) derives them from a plain C server.
