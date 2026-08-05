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

*Part 1 of 2 — see also: [Part 2](connection-lifecycle-limits--part-2.md)*

WebSocket support for Stateful Actors is in beta. Every connection ends — by redeploy, duration budget, or handler failure — so clients must reconnect to the same actor name to recover durable state from `ctx.storage`. This page covers the handshake contract, close codes, reconnect patterns, and the limits that govern frame size, queue depth, handler budget, and connection duration.

## Overview

WebSocket support for Stateful Actors is in **beta**. APIs and limits may change before general availability.

One contract underlies everything on this page: **every connection ends**. A redeploy severs it, the duration budget expires it, a failing handler closes it. Build for that from the start — treat the socket as disposable transport and the actor as the durable thing. Reconnecting is the client's job; `idFromName` with the same name routes the new socket back to the same actor, and everything in `ctx.storage` is exactly where the last connection left it. A client that reconnects with backoff and re-syncs on open loses nothing but the socket.

## How a Connection Is Established

Your function's `fetch` runs **once**, at the handshake — check the `Upgrade` header, authenticate, pick the actor, forward. It never sees another byte of the connection; per-message logic lives in the actor's `webSocket()` handler. The full front-door pattern is on the [WebSockets](websockets.md) page.

What a client can rely on at and after the handshake:

- **The upgrade must be a `GET`.** A non-`GET` request with an `Upgrade` header is refused with HTTP `400` — no handshake starts.
- **The first client-offered subprotocol is echoed.** Offer `["chat.v2", "chat.v1"]` and the connection is accepted with `chat.v2`. The actor cannot select among the offers today; it observes the echoed value as `ws.protocol`. Put your preferred protocol first.
- **Compression is never negotiated.** A `permessage-deflate` offer is accepted without the extension; frames flow uncompressed.
- **Text and binary frames both work.** The handler's `message` listener receives `(data, isBinary)`; binary frames round-trip byte-identically.
- **Protocol-level pings are answered by the platform**, payload echoed. You don't write keepalive code on the actor side.

## How Connections End

| Code | Meaning | What the client should do |
| --- | --- | --- |
| `1000` | Normal close — either side asked for it (`ws.close(1000, ...)` on the actor, or the client). | Nothing. Don't reconnect. |
| `1005` | No close code received — a bare `ws.close()` or browser close with no code argument surfaces as `1005` at the peer. Treat as deliberate if you control both sides; otherwise indistinguishable from an abnormal drop. | Reconnect if the close was not expected; otherwise no action. |
| `1001` | Actor going away — a graceful drain before the actor restarts or moves. The close frame arrives with reason `actor going away`; a client that never completes the close handshake is dropped a few seconds later. | Reconnect promptly; the actor comes back under the same name. |
| `1006` | Abnormal — the connection was severed with no close frame: the duration budget expired, a function was redeployed, or infrastructure between your client and the actor restarted. An actor-side restart is not on this list — it closes gracefully with `1001`. | Reconnect with backoff. |
| `1009` | An inbound frame exceeded the 1 MiB cap. | Fix the client — chunk large payloads. Reconnecting without fixing it hits the same wall. |
| `1011` | A message handler threw or exceeded the 30-second method budget. Also sent when the actor class has no `webSocket()` handler at all (reason: `actor has no webSocket handler`). | Reconnect, but treat repeats as a server-side bug to fix, not a transient. |
| `1013` | Event queue overflow — frames arrived faster than handlers drained them (256 events / 1 MiB queued). The actor is overloaded. | Back off **longer** than for `1006` before reconnecting, and slow your send rate. High-frequency clients should [batch messages into fewer frames](https://developers.telnyx.com/docs/edge-compute/stateful-actors/websockets#messages-are-single-threaded-like-everything-else) — the queue counts events, not bytes. |
| `4000`–`4999` | Application-defined — the RFC 6455 private-use range. The platform doesn't use these codes; one of them means your own actor called `ws.close()`, and the code and reason arrive exactly as the actor sent them. | Whatever your protocol assigned it — kicked, room closed, session expired. It's a deliberate close: act on it, don't blind-retry it. |

**Today, a connection lives at most about five minutes.** The total-duration budget applies even to a socket actively exchanging frames; the cutoff surfaces as close code `1006` with no close frame. This is a current limit, not the contract — it will be raised in a later release. Until then, design clients to ride through a reconnect every few minutes as a matter of course.

There is no separate idle kill below that budget — a socket that goes quiet for 90 seconds and then sends a frame still gets that frame delivered and handled. The duration budget is what ends it.

That guarantee covers the platform's half of the path only. NATs, corporate proxies, and load balancers between your client and Telnyx run their own idle timers, and any of them can drop a quiet connection long before the duration budget would — often silently, leaving the client holding a socket that looks open but delivers nothing. No close event fires for a drop like that, so reconnect logic alone never notices it; only traffic does. If your clients sit quiet for long stretches, send a periodic heartbeat: non-browser clients can use a protocol-level ping, which the platform answers, and browser `WebSocket` clients — which cannot send pings — should use a small application-level frame the `webSocket()` handler replies to. A heartbeat frame is one more frame through the same single-threaded dispatch, so keep it small and infrequent, and give your client library's own idle or read timeouts the same review.

**Function deploys sever live sockets.** Shipping a new version of your function drops every connection it carries as `1006`. An actor-side restart, by contrast, drains gracefully: each socket receives a `1001` close frame before the actor goes down. Either way the connection ends — this is another reason reconnect logic is not optional: your own deploys exercise it.

## Reconnecting

A complete client. It reconnects on every close except the deliberate ones — `1000`, or an application-defined `4xxx` — backs off exponentially, backs off harder on `1013`, and re-syncs on open — the socket is new even though the actor and its storage are not.

```typescript
function connect(room: string, attempt = 0): void {
  const ws = new WebSocket(
    `wss://<your-function-host>/rooms/${room}?user=me`,
  );
  let openedAt = 0;

  ws.onopen = () => {
    openedAt = Date.now();
    // Re-request whatever context this client needs. Durable state picked
    // up where it left off — a counter in ctx.storage that read 2 before
    // the drop reads 3 after the next message, not 1.
    ws.send(JSON.stringify({ op: "sync" }));
  };

  ws.onmessage = (ev) => {
    // ... application protocol ...
  };

  ws.onclose = (ev) => {
    if (ev.code === 1000) return; // done on purpose
    if (ev.code >= 4000) return; // app-defined — deliberate; act on it, don't retry it
    // Reset the backoff only after a connection proved stable — an actor
    // that accepts the handshake and then dies must still back off.
    if (openedAt > 0 && Date.now() - openedAt > 30_000) attempt = 0;
    const base = ev.code === 1013 ? 2_000 : 250; // overloaded → back off harder
    const delay = Math.min(base * 2 ** attempt, 30_000) + Math.random() * 250;
    setTimeout(() => connect(room, attempt + 1), delay);
  };
}

connect("standup");
```

Reconnect to the **same name**. `idFromName("standup")` routes to the same actor every time, so the durable sequence counters, history, and alarms of the conversation are all still there. What does not survive is anything held only in the actor's instance fields or in the old socket itself — the same rule as the rest of the platform: only `ctx.storage` is real. See [Lifecycle & placement](lifecycle-placement.md).
