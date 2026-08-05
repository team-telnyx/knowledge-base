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

*Part 5 of 7 — see also: [Part 1](stateful-actors--part-1.md), [Part 2](stateful-actors--part-2.md), [Part 3](stateful-actors--part-3.md), [Part 4](stateful-actors--part-4.md), [Part 6](stateful-actors--part-6.md), [Part 7](stateful-actors--part-7.md)*

A stateful actor is a single-threaded server that owns the state of one entity — one user, one cart, one call leg, one chat room. You write it as a TypeScript class; the platform runs one instance per name, routes every call for that name to that instance, runs your methods one at a time, and persists what you write. This page covers the runtime guarantees, the API surface (base class, context, storage, namespace, stub, alarms, errors, configuration), the execution model, lifecycle and placement, addressing, and project structure.

## Actor Context

`this.ctx` (an `ActorContext`) holds the instance's identity, per-key storage, single alarm, one-shot init, and the instance's live WebSocket connections.

```ts
interface ActorContext {
  readonly id: string;             // the name you chose with idFromName(name)
  readonly storage: ActorStorage;  // see Actor Storage
  blockConcurrencyWhile<T>(fn: () => Promise<T>): Promise<T>;
  setAlarm(when: number): Promise<void>;  // alias for ctx.storage.setAlarm(when)
  count(): number;                 // live WebSockets on this instance
  broadcast(data: string | ArrayBuffer | ArrayBufferView): number;  // returns sent count
}
```

### `ctx.id`

The customer-supplied `name` for this actor — opaque string. You chose it via `env.<BINDING>.idFromName(name)`. Common patterns: caller E.164, CRM user id, email, or a composite key.

### `ctx.blockConcurrencyWhile(fn)`

One-shot init primitive. Use it inside a subclass constructor to gate all other calls until init finishes. **30s budget** — a callback that exceeds it fails init (`BlockConcurrencyTimeoutError`), and the activation is torn down and retried on the next call.

```ts
class MyActor extends StatefulActor<Env> {
  constructor(ctx: ActorContext, env: Env) {
    super(ctx, env);
    ctx.blockConcurrencyWhile(async () => {
      // preload state, set up initial alarm, etc.
      // every other method call to this instance waits until this resolves
    });
  }
}
```

### `ctx.setAlarm(when)`

Top-level alias for `ctx.storage.setAlarm(when)`. `when` is **ms since epoch**. See [Alarms](alarms.md).

### `ctx.count()`

The number of WebSocket connections open on **this instance** right now. Synchronous — no `await`. Scoped to the instance: sockets on other names of the same actor class are never counted, and a socket never carries over between names. Callable from any handler — a socket message handler, an RPC method, or the alarm handler.

### `ctx.broadcast(data)`

Send one frame to every WebSocket open on **this instance**; returns the number of sockets the frame was sent to. A `string` is sent as a text frame; an `ArrayBuffer` or `ArrayBufferView` as a binary frame. Scoped to the instance, like `count()` — a broadcast never reaches another name's sockets. Like `ws.send()`, the write happens immediately; it is not held until the turn's storage writes commit. Callable from any handler. Calling it from `alarm()` is the server-initiated push pattern — the actor sends with no inbound frame prompting it:

```ts
async alarm(): Promise<void> {
  this.ctx.broadcast(JSON.stringify({ type: "tick", at: Date.now() }));
}
```

## Actor Storage

`this.ctx.storage` (an `ActorStorage`) is the actor's per-key persistent storage. **A turn that returns successfully is persisted** — all writes made during the turn (put/delete/transaction/sql.exec/setAlarm) commit atomically at end-of-turn; a turn that throws commits nothing.

```ts
interface ActorStorage {
  get<T = unknown>(key: string): Promise<T | undefined>;
  put<T = unknown>(key: string, value: T): Promise<void>;
  delete(key: string): Promise<boolean>;            // true iff the key existed
  list<T = unknown>(options?: ListOptions): Promise<Map<string, T>>;
  deleteAll(): Promise<void>;                        // atomic clear of all keys; does NOT clear a pending alarm
  transaction<T>(fn: (txn: StorageTransaction) => Promise<T>): Promise<T>;

  readonly sql: SqlStorage;                          // per-actor embedded SQLite (synchronous)
  transactionSync<T>(fn: () => T): T;                // atomic SQL transaction (synchronous)

  // Alarm API (mirrors ctx.setAlarm)
  // Available in local development; prod support is pending.
  setAlarm(when: number): Promise<void>;
  getAlarm(): Promise<number | null>;
  deleteAlarm(): Promise<void>;
}
```

Key behaviors:

- **Lazy per `get`** — state is not preloaded on activation. Call `get` when you need it.
- **Read-your-writes** — reads always reflect prior writes from the same actor.
- **Per-actor method serialization** — calls to one actor instance are dispatched one at a time, giving you effective ACID at the actor level.
- **Values round-trip through a codec.** JSON natives plus `Date`, `Map`, `Set`, typed arrays, `ArrayBuffer`, `BigInt`, and `RegExp` come back as what you stored. Unstorable values — functions, class instances, circular structures, promises, streams — are rejected with a `CodecError` at the write.
- **Keys starting with `__telnyx_` are reserved** for the runtime's own bookkeeping — writes to them are rejected.

### `list(options)`

Lexicographic key order; `reverse: true` flips it. Returns a `Map<string, T>` to preserve ordering.

```ts
interface ListOptions {
  prefix?: string;        // filter to keys starting with this string
  start?: string;         // inclusive
  startAfter?: string;    // exclusive
  end?: string;           // exclusive
  reverse?: boolean;
  limit?: number;         // default 128, max 1000 — a larger limit is rejected
}
```

### `transaction(fn)`

Atomic batch. `fn` receives a `StorageTransaction` with the same `get`/`put`/`delete`/`list` surface.

```ts
await this.ctx.storage.transaction(async (txn) => {
  const v = (await txn.get<number>("count")) ?? 0;
  await txn.put("count", v + 1);
  await txn.put("updated_at", Date.now());
});
```

If `fn` throws, the buffered writes are discarded — **and the enclosing method call fails with `ActorOutputGateError`**, even if your code catches the rejection. Only the transaction's own writes are undone: writes you make after catching the rejection still commit, but the caller sees the error instead of your return value. A thrown transaction is not a control-flow tool for "try the write, continue on failure".

### `sql`

`ctx.storage.sql` is a private embedded SQLite database for this actor — a separate, synchronous store beside the key/value surface above.

### `transactionSync(fn)`

Atomic SQL transaction: runs `fn` synchronously, commits its `sql.exec` writes when it returns (passing the return value through), rolls all of them back if it throws. `fn` must not be `async` — an async callback throws `SqlAsyncTransactionError` and commits nothing. This is the only transaction API for SQL: `exec()` rejects raw `BEGIN` / `COMMIT` / `ROLLBACK` / `SAVEPOINT` with `SqlTransactionControlError`. Unlike a thrown `transaction(fn)`, a thrown `transactionSync` does **not** poison the turn: catch it and the method call completes normally.
