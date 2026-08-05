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

*Part 6 of 7 — see also: [Part 1](stateful-actors--part-1.md), [Part 2](stateful-actors--part-2.md), [Part 3](stateful-actors--part-3.md), [Part 4](stateful-actors--part-4.md), [Part 5](stateful-actors--part-5.md), [Part 7](stateful-actors--part-7.md)*

A stateful actor is a single-threaded server that owns the state of one entity — one user, one cart, one call leg, one chat room. You write it as a TypeScript class; the platform runs one instance per name, routes every call for that name to that instance, runs your methods one at a time, and persists what you write. This page covers the runtime guarantees, the API surface (base class, context, storage, namespace, stub, alarms, errors, configuration), the execution model, lifecycle and placement, addressing, and project structure.

## Actor Namespace

`env.<BINDING>` is an `ActorNamespace` — the handle on `env` that your function calls into. It's declared in `telnyx.toml`:

```toml
[actors](actors.md)
binding = "ACCOUNT"    # env.ACCOUNT
type    = "Account"    # the class to instantiate per name
```

```ts
interface ActorNamespace {
  idFromName(name: string, options?: IdFromNameOptions): ActorStub;
  newUniqueId(options?: IdFromNameOptions): ActorStub;
}

interface IdFromNameOptions {
  locationHint?: LocationHint;     // "us-east" | "us-west" | "eu" | "apac" | (string & {})
}
```

### `idFromName(name, options?)`

Deterministic — the same `name` always lands on the same actor instance. This is the most common call: pick a stable identity (caller E.164, CRM id, room id) and let the platform route to the right state. `locationHint` is a placement **hint**, relevant on first touch only — an actor materializes once, so a hint on a later call can't move it. The platform may ignore the hint entirely (today it does — the option is accepted and reserved for regional placement). Abstract region codes (the taxonomy can evolve without breaking your code).

### `newUniqueId(options?)`

Random — a fresh, unguessable instance. Use when you want the runtime to mint the identity for you (e.g. a one-shot job actor). The id is generated client-side; keep it (via `stub.id`) if you'll need to reach the instance again.

`newUniqueId` currently fails at call time on the platform (a known runtime issue). Until it's fixed, mint an identity yourself and pass it to `idFromName`.

Both return an [Actor Stub](actor-stub.md). Method dispatch on the stub is provided by the runtime via a Proxy; in TypeScript, run `telnyx-edge types` to type `env.<BINDING>` against your class's public method shape, or hand-roll the narrowing — the [Actor Stub](actor-stub.md) page shows both.

## Actor Stub

An `ActorStub` is the client handle returned by `idFromName` / `newUniqueId`. Calling a method on it is an RPC to that one actor instance.

```ts
interface ActorStub {
  readonly id: string;                       // the name passed to idFromName
  fetch(req: Request): Promise<Response>;    // HTTP-style entry (see Base Class fetch)
  // + your subclass's public methods — typed via `telnyx-edge types` or by hand, below
}
```

`telnyx-edge types` generates the narrowing for every `[actors](actors.md)` binding in `telnyx.toml` — a `telnyx-env.d.ts` that types `env.<BINDING>` against your class's public method shape. To hand-roll it instead (also the path for a shared-actor reference, which ships no local class for codegen to read):

```ts
import { type ActorNamespace, type ActorStub, type IdFromNameOptions } from "@telnyx/edge-runtime";

type AccountStub = ActorStub & Pick<Account, "deposit" | "debit" | "balance">;

interface AccountNamespace extends ActorNamespace {
  idFromName(name: string, options?: IdFromNameOptions): AccountStub;
}

interface Env { ACCOUNT: AccountNamespace }
```

## Alarms

Every Stateful Actor has a **single per-instance alarm** — a one-shot timer you can set, replace, read, or clear from inside any method. When the alarm fires, the runtime calls the actor's `alarm(alarmInfo)` handler. Alarms are the way to do deferred work without an external scheduler.

| What | How |
| --- | --- |
| Set or replace the alarm | `await this.ctx.storage.setAlarm(when)` — `when` is ms since epoch |
| Read the scheduled time | `await this.ctx.storage.getAlarm()` → `number \| null` |
| Clear the alarm | `await this.ctx.storage.deleteAlarm()` |
| Top-level alias | `await this.ctx.setAlarm(when)` (mirrors `storage.setAlarm`) |
| Handle the fire | override `async alarm(info: AlarmInfo)` on your subclass |

There is one alarm per actor instance, not per method or per key. Setting it again replaces the previous time.

### Set and handle

```ts
import { StatefulActor, type AlarmInfo } from "@telnyx/edge-runtime";

export class Session extends StatefulActor {
  // Called when a session is touched — push the timeout out by 5 minutes.
  async touch() {
    await this.ctx.storage.put("last_seen", Date.now());
    await this.ctx.storage.setAlarm(Date.now() + 5 * 60_000);
  }

  // Fires once when the alarm goes off.
  async alarm(info: AlarmInfo): Promise<void> {
    const lastSeen = (await this.ctx.storage.get<number>("last_seen")) ?? 0;
    if (Date.now() - lastSeen > 5 * 60_000) {
      // session actually idle — clean up
      await this.ctx.storage.deleteAll();
    }
  }
}
```

The handler is just another method call on the actor — it inherits the same single-threaded dispatch guarantee as any other method. You don't need a lock around the state the alarm touches.

### Delivery contract

`AlarmInfo`:

```ts
interface AlarmInfo {
  retryCount: number;   // 0 on first delivery; increments on each retry
  isRetry: boolean;     // true when retryCount > 0
}
```

- **At-least-once delivery.** Plan for the handler to run more than once for the same scheduled time. Make writes idempotent — re-check state in `storage` before applying effects (as the `Session` example above does), or record a done-marker keyed by the scheduled time.
- **A failed run is redelivered 3 times, about a second apart.** If the handler throws (or exceeds its time budget), the platform re-fires it with `retryCount` incremented — 4 attempts total, then the alarm is **deleted** (`getAlarm()` returns `null`). There is no signal when that happens.
- **A failing handler loses its alarm — don't use `throw` as your retry mechanism.** Three retries a second apart won't outlast a real outage. If the deferred work must happen, make the handler tolerate its own errors: catch, record, and re-arm with `setAlarm` at a backoff you choose.
- **Use `info.isRetry` to branch.** On retry, log it, treat the work as best-effort, or skip already-completed steps.

```ts
async alarm(info: AlarmInfo): Promise<void> {
  if (info.isRetry) {
    // redelivery after a failed run — be extra careful about double-applies
  }
  // re-check state in storage before applying effects, then do the work
}
```

### Patterns

**TTL / expiry.** Set the alarm when you create the row; on fire, check the row is still expired and delete it. If the row was touched since, reset the alarm instead.

**Retry backoff.** If your method kicks off a flaky external call, set an alarm to retry later; on fire, attempt again and either succeed or set a new alarm with a longer backoff.

**Session timeout.** See `Session.touch` above — every interaction pushes the alarm out by the idle window; the alarm only fires if no one touches the session in time.

**Coalesced drain.** Because there's only one alarm per instance, you can use it as a "flush trigger": set it on the first write, and when it fires, drain the queue and clear it. Subsequent writes during the window just append to the queue.

### Limits

- **One alarm per actor instance.** If you need multiple timers, keep a queue in `storage` and use the single alarm to drive a scheduler loop.
- **`when` is ms since epoch.** Don't pass seconds. Firing precision is about one second — don't schedule sub-second work with it.
- **No recurring flag.** If you want periodic work, set the next alarm at the end of your `alarm` handler.
- **The handler has a time budget.** `alarm()` runs under its own wall-clock cap — larger than the 30-second method budget, on the order of minutes, but still bounded. A run that exceeds it counts as a failure and is redelivered.
- **`deleteAll()` does not clear the alarm.** Keys and the alarm are separate; a pending alarm still fires after `deleteAll()`, and a handler that re-arms itself will keep running against empty state. To decommission an actor: `deleteAlarm()` first, then `deleteAll()`.
