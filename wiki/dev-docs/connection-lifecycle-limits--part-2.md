---
title: Connection Lifecycle & Limits
summary: WebSocket support for Stateful Actors is in beta. Every connection ends —
  by redeploy, duration budget, or handler failure — so clients must reconnect to
  the same actor name to recover durable state from `ctx.storage`. This page covers
  the handshake contract, close codes, reconnect patterns, and the limits that govern
  frame size, queue depth, handler budget, and connection duration.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/websockets/lifecycle
updated_at: 2026-08-05T13:42:28Z
---

# Connection Lifecycle & Limits

*Part 2 of 2 — see also: [Part 1](connection-lifecycle-limits--part-1.md)*

WebSocket support for Stateful Actors is in beta. Every connection ends — by redeploy, duration budget, or handler failure — so clients must reconnect to the same actor name to recover durable state from `ctx.storage`. This page covers the handshake contract, close codes, reconnect patterns, and the limits that govern frame size, queue depth, handler budget, and connection duration.

## Limits

| Limit | Value | On violation |
| --- | --- | --- |
| Inbound frame size | 1 MiB | Close `1009` |
| Event queue while a handler runs | 256 events / 1 MiB | Close `1013` |
| Per-message method budget | 30 seconds | Close `1011` |
| Connection duration | ~5 minutes today (expected to increase) | Close `1006`, no close frame |
| Socket scope | One actor id — `ctx.count()` and `ctx.broadcast()` reach only this id's sockets; sockets never carry over between ids | — |
| Actor names used with sockets | Printable ASCII, no leading/trailing whitespace, today | Connection fails to establish |
| Header values your function forwards | Printable ASCII today | Connection fails to establish |
| Outbound frame size | No platform cap — unsent bytes wait in the actor's memory until the client's connection drains them | — |

The queue limit is a consequence of single-threaded dispatch: an inbound frame is handled like a method call — one at a time per instance, serialized with RPCs and alarms. While one handler runs, further frames queue; a slow handler with fast senders overflows the queue and the socket closes `1013`. Keep per-message work well under the 30-second budget — the queue bound is sized for handlers that finish in milliseconds, not tens of seconds.

The same serialization sets the practical ceiling on how many sockets one instance should carry. The table has no socket-count row because the working bound is not a count — it is aggregate frame rate. An instance handles one frame at a time from all of its sockets combined: at one millisecond of handler work per frame, the whole instance drains at most on the order of a thousand inbound frames per second, and a `ctx.broadcast()` inside a handler writes one frame to every connected socket, so fan-out work grows with the audience. The 256-event queue absorbs a burst of at most a couple hundred frames, not thousands of senders talking at once. When one name's combined rate approaches what its handlers can drain, partition the workload across names — a room per `idFromName`, a shard per topic or region — so each instance coordinates only the sockets whose combined traffic it can serialize. An actor is a unit of coordination, not a unit of capacity.

The outbound direction is the mirror image, and it is not policed. `ws.send()` never blocks the handler, and the platform never drops or coalesces frames on a live connection — anything the client hasn't drained yet waits in the actor's memory, and `ws.bufferedAmount` (standard Node `ws`) reports how much is queued on a socket. Against a responsive client that number stays near zero; against a stalled one — a backgrounded tab, a dead radio link — every `ctx.broadcast()` tick adds another payload to the stalled socket's queue. Bound what one slow consumer can cost: keep broadcast payloads small, and when updates outpace a client, send the latest state rather than queueing every delta — durable state in `ctx.storage` means a client that fell behind can re-sync from a snapshot instead of replaying a backlog. A socket whose `bufferedAmount` only grows is gone in every way that matters; close it, and the reconnect-and-re-sync logic every client here needs anyway will pick it back up.

## What Holds the Actor in Memory

While a connection is open its actor stays resident — the actor is not deactivated between frames — and under today's duration budget a connection never lives long enough for the idle eviction described in [Lifecycle & placement](lifecycle-placement.md) to be a factor. The cost model follows: a million idle actors are cheap; a million actors each holding an open socket are a million resident activations.

Teardown is orderly on the actor side. `close` and `error` listeners run under the same single-threaded dispatch as any other event, and a `ctx.storage` write inside a `close` handler commits — the instance stays resident until those final handlers finish, not merely until the raw socket drops. Recording "last seen" in a close handler is safe. After the last socket's close handler finishes, the actor is an ordinary idle actor again: evictable, and revivable by the next `idFromName` call — or by an [alarm](alarms.md) it set while the connection was up.

## Next Steps

- [WebSockets](websockets.md) — the front-door pattern, the `webSocket()` handler, and how messages dispatch
- [Lifecycle & placement](lifecycle-placement.md) — eviction and restart for actors generally
- [Alarms](alarms.md) — deferred work that outlives any connection
