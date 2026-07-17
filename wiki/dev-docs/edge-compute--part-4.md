---
title: Edge Compute
summary: 'Telnyx Edge Compute is a platform of compute primitives for building and
  deploying applications to the Telnyx edge. The core primitive is a function: an
  ordinary HTTP server packaged as a container, deployed to Telnyx''s global edge
  network, and served at its own public URL. The platform adds bindings (pre-authenticated
  handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable
  per-entity state via Stateful Actors, globally distributed key-value storage via
  KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage.
  Functions are real Linux containers running your language''s own runtime — Node.js,
  Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is
  declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the
  `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and
  rollback automatically.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/filesystems-from-first-principles/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/how-cloudfs-works
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/network-filesystems
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concurrent-access
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/mount/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/quickstart
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
- url: https://developers.telnyx.com/docs/edge-compute/deploy/index
- url: https://developers.telnyx.com/docs/edge-compute/development/index
- url: https://developers.telnyx.com/docs/edge-compute/guides/ai-assistant-backend
- url: https://developers.telnyx.com/docs/edge-compute/kv/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
- url: https://developers.telnyx.com/docs/edge-compute/kv/concepts/how-kv-works/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/api-response-caching
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/feature-flags
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/session-storage/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/kv-namespace
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
- url: https://developers.telnyx.com/docs/edge-compute/network/index
- url: https://developers.telnyx.com/docs/edge-compute/observability/index
- url: https://developers.telnyx.com/docs/edge-compute/overview/index
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview/index
- url: https://developers.telnyx.com/docs/edge-compute/platform/limits
- url: https://developers.telnyx.com/docs/edge-compute/platform/pricing
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/runtime/http-handler
- url: https://developers.telnyx.com/docs/edge-compute/runtime/index
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
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/when-to-use
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/local-development
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/quick-start/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/shared-actors
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/api-reference
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/handling-calls
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/index
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/receiving-messages
updated_at: 2026-07-17T09:13:17Z
---

# Edge Compute

*Part 4 of 7 — see also: [Part 1](edge-compute--part-1.md), [Part 2](edge-compute--part-2.md), [Part 3](edge-compute--part-3.md), [Part 5](edge-compute--part-5.md), [Part 6](edge-compute--part-6.md), [Part 7](edge-compute--part-7.md)*

Telnyx Edge Compute is a platform of compute primitives for building and deploying applications to the Telnyx edge. The core primitive is a function: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. The platform adds bindings (pre-authenticated handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable per-entity state via Stateful Actors, globally distributed key-value storage via KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage. Functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and rollback automatically.

## Stateful Actors

A stateful actor is a single-threaded server that owns the state of one entity — one user, one cart, one call leg, one chat room. You write it as a TypeScript class; the platform runs one instance per name, routes every call for that name to that instance, runs your methods one at a time, and persists what you write. You never bind a socket, take a lock, or shard it.

```
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

That `debit` is a read-modify-write with no lock and no transaction. In a normal request handler that's a race; here it isn't — and that property is the whole product.

### Runtime Guarantees

- **One instance per name** — `idFromName("acct_123")` routes every call to a single owner; no two hosts run it at once.
- **One call at a time** — single-threaded dispatch. No locks, no races inside an instance.
- **Durable before reply** — a method's result isn't returned until the writes it made are persisted.
- **Memory is a cache** — only what you write to `storage` survives eviction or restart.

### Project Structure

A Stateful Actor project ships from one module that exports two things, wired together by a binding declared in `telnyx.toml`: the actor class and a `fetch` handler that calls the actor through a binding on `env`.

```
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
    const acct = new URL(req.url).pathname.slice(1);
    const { amount } = (await req.json()) as { amount: number };
    const result = await env.ACCOUNT.idFromName(acct).debit(amount);
    return Response.json(result);
  },
};
```

The `[actors](actors.md)` block in `telnyx.toml` declares the binding:

```
name = "account-svc"
main = "src/index.ts"
compatibility_date = "2026-05-01"

[actors](actors.md)
binding = "ACCOUNT"
type    = "Account"
```

### Addressing

`env.<BINDING>` is your handle to an actor class. You name an instance, get a stub, and call methods on it:

```
env.ACCOUNT.idFromName("acct_123")  // deterministic — same name, same instance
env.ACCOUNT.newUniqueId()           // random — mints a fresh, unguessable identity
```

`idFromName(name)` is deterministic: the same name always lands on the same instance, from anywhere. Pick a stable identity for the entity and let the platform route to its state. `newUniqueId()` mints a fresh, unguessable instance; it currently fails at call time on the platform (a known runtime issue) — until it's fixed, mint an identity yourself and pass it to `idFromName`.

### Storage

`this.ctx.storage` (an `ActorStorage`) is the actor's per-key persistent storage. Writes that return successfully are persisted.

```
interface ActorStorage {
  get<T = unknown>(key: string): Promise<T | undefined>;
  put<T = unknown>(key: string, value: T): Promise<void>;
  delete(key: string): Promise<boolean>;
  list<T = unknown>(options?: ListOptions): Promise<Map<string, T>>;
  deleteAll(): Promise<void>;
  transaction<T>(fn: (txn: StorageTransaction) => Promise<T>): Promise<T>;
  setAlarm(when: number): Promise<void>;
  getAlarm(): Promise<number | null>;
  deleteAlarm(): Promise<void>;
}
```

Calls to one actor instance are dispatched one at a time, giving you effective ACID at the actor level. Values round-trip through a codec — JSON natives plus `Date`, `Map`, `Set`, typed arrays, `ArrayBuffer`, `BigInt`, and `RegExp` come back as what you stored. Keys starting with `__telnyx_` are reserved.

### Alarms

Every Stateful Actor has a single per-instance alarm — a one-shot timer you can set, replace, read, or clear from inside any method. When the alarm fires, the runtime calls the actor's `alarm(alarmInfo)` handler.

```
await this.ctx.storage.setAlarm(Date.now() + 5 * 60_000);
```

Delivery is at-least-once. A failed run is redelivered 3 times, about a second apart. If the handler throws (or exceeds its time budget), the platform re-fires it with `retryCount` incremented — 4 attempts total, then the alarm is deleted. Make writes idempotent — re-check state in `storage` before applying effects.

### Shared Actors

A shared actor is a single Stateful Actor type reachable from two or more Edge Compute functions on the same account. The function that ships the actor class owns the actor; other functions declare the same `type` under their own `binding` name and ship no class — their binding routes to the owner's actor and its state.

Both functions must be on the same account — shared actors are bounded by account. The reference's `type` must exactly match the owner's.

### When to Use

Use a stateful actor when an entity has state that must be mutated coherently across many requests — a cart, a chat room, a call leg's media state, a per-user rate limiter, a job coordinator.

Don't reach for one for stateless work (routing, transforms, independent fan-out), a global counter or singleton (one name is one single-threaded bottleneck), large blobs or bulk scans, or cross-entity transactions or ad-hoc queries. A single instance processes calls serially, so its ceiling is roughly `1 / (method wall-time)` calls per second. Sharding by a well-chosen name is how you scale.
