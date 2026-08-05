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

*Part 1 of 7 — see also: [Part 2](stateful-actors-index--part-2.md), [Part 3](stateful-actors-index--part-3.md), [Part 4](stateful-actors-index--part-4.md), [Part 5](stateful-actors-index--part-5.md), [Part 6](stateful-actors-index--part-6.md), [Part 7](stateful-actors-index--part-7.md)*

Stateful Actors on Telnyx Edge Compute give each named entity its own durable, single-threaded instance with private key/value and SQL storage, alarms, and WebSocket support. This page covers when to use them, the storage surfaces, local development, the Quick Start, shared actors across functions, and WebSocket patterns.

## Overview

A Stateful Actor is a long-lived, named instance that holds private, durable state and processes calls one at a time. One instance per name gives you serialized, durable, private state for that entity without locks or a shared database — useful for a cart, a chat room, a call leg's media state, a per-user rate limiter, or a job coordinator.

The actor runtime exposes two storage surfaces under `this.ctx.storage`:

- **Key/value** at `this.ctx.storage` — simple keyed state, prefix listing, atomic multi-key updates. The default.
- **SQL** at `this.ctx.storage.sql` — a private embedded SQLite database for relational shape, aggregates, `GROUP BY`, secondary indexes, and joins *within one actor*.

Both are private, strongly consistent, and transactional. Only the actor instance reads and writes its data, its methods run one at a time (serialized turns), and a write that returns successfully is durable — it survives the actor being evicted, relocated, or its pod replaced. Reads always reflect prior writes.

## When to Use a Stateful Actor

Reach for a stateful actor when an entity has state that must be mutated coherently across many requests.

**Do not reach for one when:**

- The work is stateless (routing, transforms, independent fan-out) — use a plain function. An actor only adds a routing hop and a serialization point you don't need.
- You need a global counter or singleton — one name is one single-threaded instance is one throughput ceiling. Shard across many names so load spreads.
- You need to store large blobs or run bulk scans — the keyspace holds one entity's working set, not a warehouse. Use object storage or a database.
- You need cross-entity transactions or ad-hoc queries — each instance is its own consistency domain. There is no transaction across two actors and no `JOIN` across them. Use a database for that.

A single instance processes calls serially, so its ceiling is roughly `1 / (method wall-time)` calls per second. Sharding by a well-chosen name is how you scale.

## Key/Value Storage

Every Stateful Actor has private, durable key/value storage at `this.ctx.storage`. It is the default place to keep an entity's state. Drop to [SQL](sql.md) only when a lookup by key isn't enough and you'd otherwise scan.

### Reading and Writing

`get` and `put` are the whole surface for simple state. Both are async — they may cross the network — so `await` them:

```typescript
import { StatefulActor } from "@telnyx/edge-runtime";

export class Cart extends StatefulActor {
  async add(item: string) {
    const items = (await this.ctx.storage.get<string[]>("items")) ?? [];
    items.push(item);
    await this.ctx.storage.put("items", items);
    return items.length;
  }

  async clear() {
    await this.ctx.storage.delete("items");   // returns true iff the key existed
  }
}
```

State is lazy per `get` — nothing is preloaded when the actor activates; you read a key when you need it. Values round-trip through a codec, so JSON natives plus `Date`, `Map`, `Set`, typed arrays, `ArrayBuffer`, `BigInt`, and `RegExp` come back as what you stored. Functions, class instances, promises, and circular structures are rejected at the write. Keys are strings. Those starting with `__telnyx_` are reserved for the runtime — writes to them are rejected.

### Listing Keys

`list` returns a `Map` in lexicographic key order, which makes prefixes a natural grouping:

```typescript
// Every message in a room, in order:
const messages = await this.ctx.storage.list<Message>({ prefix: "msg:" });

// The 20 most recent, newest first:
const recent = await this.ctx.storage.list<Message>({
  prefix: "msg:",
  reverse: true,
  limit: 20,
});
```

`limit` defaults to 128 and maxes at 1000. Use `start` / `startAfter` / `end` to page through a large keyspace.

### Atomic Updates

`transaction` batches multiple keys into one atomic unit — all of the writes land, or none do:

```typescript
await this.ctx.storage.transaction(async (txn) => {
  const balance = (await txn.get<number>("balance")) ?? 0;
  await txn.put("balance", balance - amount);
  await txn.put("updated_at", Date.now());
});
```

If the callback throws, its buffered writes are discarded. A thrown transaction also fails the enclosing method call — it is not a "try the write, continue on failure" tool.

### Clearing an Actor

`deleteAll()` atomically removes every key for this actor. It does **not** clear a pending alarm — delete that separately if you want the actor fully reset.
