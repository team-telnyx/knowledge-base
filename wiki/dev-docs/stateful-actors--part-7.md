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

*Part 7 of 7 — see also: [Part 1](stateful-actors--part-1.md), [Part 2](stateful-actors--part-2.md), [Part 3](stateful-actors--part-3.md), [Part 4](stateful-actors--part-4.md), [Part 5](stateful-actors--part-5.md), [Part 6](stateful-actors--part-6.md)*

A stateful actor is a single-threaded server that owns the state of one entity — one user, one cart, one call leg, one chat room. You write it as a TypeScript class; the platform runs one instance per name, routes every call for that name to that instance, runs your methods one at a time, and persists what you write. This page covers the runtime guarantees, the API surface (base class, context, storage, namespace, stub, alarms, errors, configuration), the execution model, lifecycle and placement, addressing, and project structure.

## Errors

| Error | Meaning |
| --- | --- |
| `BlockConcurrencyTimeoutError` | `ctx.blockConcurrencyWhile`'s callback exceeded the 30s budget |
| `ActorOutputGateError` | A storage write initiated during a method rejected after the method returned; surfaces in place of the successful return value, with the underlying failure appended to the error message. Also raised when a `transaction` callback throws |
| `ActorMethodTimeoutError` | An RPC method exceeded its wall-clock budget (30s by default). The invocation fails; the instance is not torn down |
| `ActorFetchTimeoutError` | The actor's `fetch(req)` handler exceeded its wall-clock budget (30s) |
| `CodecError` | A method argument, return value, or storage value could not be serialized (e.g. a function, a circular structure) |

On the **caller** side, a failed stub call rejects with an `Error` whose `name` identifies the cause — for example `ActorMethodError` (your method threw; message preserved), `ActorPrivateMethodError` (`_`-prefixed method), or `ActorUnknownMethodError`. Branch on `err.name` if you need to distinguish them.

## Related Resources

- [Bindings](bindings.md) — how bindings resolve on `env`
- [KV](kv--part-1.md) — globally distributed key-value storage
- [Execution Model](execution-model.md) — function lifecycle and concurrency
