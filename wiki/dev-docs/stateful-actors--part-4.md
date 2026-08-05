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

*Part 4 of 7 — see also: [Part 1](stateful-actors--part-1.md), [Part 2](stateful-actors--part-2.md), [Part 3](stateful-actors--part-3.md), [Part 5](stateful-actors--part-5.md), [Part 6](stateful-actors--part-6.md), [Part 7](stateful-actors--part-7.md)*

A stateful actor is a single-threaded server that owns the state of one entity — one user, one cart, one call leg, one chat room. You write it as a TypeScript class; the platform runs one instance per name, routes every call for that name to that instance, runs your methods one at a time, and persists what you write. This page covers the runtime guarantees, the API surface (base class, context, storage, namespace, stub, alarms, errors, configuration), the execution model, lifecycle and placement, addressing, and project structure.

## Runtime API Overview

The types in this reference are exported from `@telnyx/edge-runtime` (TypeScript).

| Surface | Where it lives | What it's for |
| --- | --- | --- |
| `StatefulActor<E>` | `@telnyx/edge-runtime` | Base class you extend. Holds `this.ctx` and `this.env`. |
| `ActorContext` | `this.ctx` (runtime-injected) | Per-instance identity, storage, single alarm, one-shot init. |
| `ActorStorage` | `this.ctx.storage` | Per-key persistent storage. |
| `ActorNamespace` | `env.<BINDING>` | The handle from your function. Returns stubs you call methods on. |
| `ActorStub` | from `idFromName` / `newUniqueId` | Per-name handle; an RPC to one instance. |
| Alarms | `ctx.storage` + `alarm()` | Single per-actor alarm; at-least-once delivery. |
| Configuration | `telnyx.toml` `[actors](actors.md)` | Declaring the actor binding. |
| Errors | `@telnyx/edge-runtime` | `BlockConcurrencyTimeoutError`, `ActorOutputGateError`, timeout and codec errors. |

## Base Class

`StatefulActor` is the base class you extend. Subclass it, declare async methods, and they become RPC-callable from a stub. It holds `this.ctx` (see [Actor Context](actor-context.md)) and `this.env` (your bindings).

```ts
import { StatefulActor } from "@telnyx/edge-runtime";

export class Account extends StatefulActor {
  async debit(amount: number): Promise<{ ok: boolean; balance: number }> {
    const balance = (await this.ctx.storage.get<number>("balance")) ?? 0;
    if (balance < amount) return { ok: false, balance };
    await this.ctx.storage.put("balance", balance - amount);
    return { ok: true, balance: balance - amount };
  }
}
```

### Construction

You don't construct actors yourself — the runtime does. The base constructor wires `this.ctx` and `this.env`, so a subclass that doesn't need init logic can omit its constructor entirely.

```ts
class MyActor extends StatefulActor<Env> {
  // no constructor needed — this.ctx and this.env are wired by the base
}
```

If you do need one-shot init (preload state, set up an initial alarm), override the constructor and call `ctx.blockConcurrencyWhile` — see [Actor Context](actor-context.md).

### Dispatch rules

- **Public methods are RPC-callable** from a stub — declare them `async` (every stub call is a `Promise` on the caller's side regardless).
- Methods whose names start with `_` are internal helpers and are **not** RPC-exposed — the runtime rejects the call.
- The `_` prefix is the only opt-out. TypeScript's `private` keyword is erased at runtime and does **not** stop remote calls; name internal helpers with a leading `_`.
- `fetch(req)`, `alarm(info)`, `webSocket(ws, req)`, the constructor, and methods defined on `StatefulActor` itself (not your subclass) are special and not auto-RPC.
- **Methods have a wall-clock budget** (30s by default). A call that exceeds it fails with `ActorMethodTimeoutError` — see [Errors](errors.md).

### `alarm(alarmInfo)`

Optional alarm handler. Override to handle scheduled work. The base implementation is a no-op.

```ts
async alarm(info: AlarmInfo): Promise<void> {
  // at-least-once delivery — be idempotent
  // info.retryCount is 0 on first delivery; info.isRetry is true on retries
}
```

See [Alarms](alarms.md) for the delivery contract and retry policy.

### `fetch(req)`

Optional HTTP-style entry. The base default returns `404`. Override if you want callers to reach the actor over a raw `Request` instead of RPC methods:

```ts
async fetch(req: Request): Promise<Response> {
  return new Response("hello from " + this.ctx.id);
}
```

Callable from a binding as `env.BINDING.idFromName(name).fetch(req)`.

### `webSocket(ws, req)`

Optional WebSocket entry. Unlike `alarm()` and `fetch()`, there is **no default implementation** — declaring the method is the opt-in. An actor that doesn't declare `webSocket()` has no socket behavior at all, and an upgrade routed at it is closed with code `1011` (reason `actor has no webSocket handler`).

```ts
import { StatefulActor } from "@telnyx/edge-runtime";
import type { WebSocket } from "ws";

export class Room extends StatefulActor {
  async webSocket(ws: WebSocket, req: Request): Promise<void> {
    const user = req.headers.get("x-user") ?? "anonymous";

    ws.on("message", async (data, isBinary) => {
      if (isBinary) return;
      // messages dispatch one at a time — this read-modify-write never races
      const seq = ((await this.ctx.storage.get<number>("seq")) ?? 0) + 1;
      await this.ctx.storage.put("seq", seq);
      ws.send(JSON.stringify({ echo: String(data), seq, user }));
    });
  }
}
```

- **Called once per accepted connection**, with the live socket and the handshake `Request`. `req` is the request your function's front door forwarded: the URL plus application headers, with transport and handshake headers stripped. Client-sent app headers pass through too, so trust only headers your front door explicitly set or overwrote — the front door must overwrite or strip anything auth-bearing (like `x-user` above) before forwarding.
- **`ws` is a Node `ws` socket** (`import type { WebSocket } from "ws"`): `ws.on("message", (data, isBinary) => ...)`, `ws.send(data)`, `ws.close(code, reason)`. There is no `WebSocketPair`/`accept()` shape.
- **Register your listeners before `webSocket()` returns.** Frames that arrive before `webSocket()` returns — including any the client sent immediately after the handshake — are buffered and replayed in order once it returns; nothing drops.
- **Socket events share the instance's single-threaded dispatch.** `message`, `close`, and `error` handlers run one at a time, serialized with RPC methods and alarms, each under the method wall-clock budget (30s by default). A message handler that throws or exceeds the budget closes the socket with code `1011`.

Connections reach the actor through your function's `fetch` front door: check the `Upgrade` header, authenticate, then forward with `env.BINDING.idFromName(name).fetch(...)`.
