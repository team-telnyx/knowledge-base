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

*Part 6 of 7 — see also: [Part 1](stateful-actors-index--part-1.md), [Part 2](stateful-actors-index--part-2.md), [Part 3](stateful-actors-index--part-3.md), [Part 4](stateful-actors-index--part-4.md), [Part 5](stateful-actors-index--part-5.md), [Part 7](stateful-actors-index--part-7.md)*

Stateful Actors on Telnyx Edge Compute give each named entity its own durable, single-threaded instance with private key/value and SQL storage, alarms, and WebSocket support. This page covers when to use them, the storage surfaces, local development, the Quick Start, shared actors across functions, and WebSocket patterns.

## WebSockets

WebSocket support for Stateful Actors is in **beta**. APIs and limits may change before general availability.

A client opens one WebSocket. Your function runs **once, at the handshake** — check the upgrade, authenticate, decide which actor owns this connection — and hands off. From then on the **actor owns the live socket**: each inbound frame is dispatched like a method call — one at a time per instance, serialized with RPCs and alarms — durable state is ordinary `ctx.storage`, and replies stream straight back with `ws.send()`.

That shape removes the plumbing a chat, agent, or live-session backend usually accretes. When the connection tier and the state tier are separate fleets, every message crosses a pub/sub bridge on the way in and needs a reverse channel to find whichever host holds the socket on the way out. Here the socket and the state live in the same single-threaded instance — a message handler is a plain method body that reads storage, writes storage, and sends.

Any actor class can terminate WebSockets — declaring the `webSocket()` method is the whole opt-in; there is no flag to enable, in `telnyx.toml` or anywhere else. Actor names used with sockets must be printable ASCII with no leading or trailing whitespace, and any header values your function forwards must be printable ASCII today.

### The Two Halves

|  | Runs | Responsible for |
| --- | --- | --- |
| **Function** | once per connection, at the handshake | reject non-upgrades (`426`), authenticate, rate-limit, resolve `idFromName`, stamp what it learned as headers |
| **Actor** | once per frame, and per close/error event | per-message logic, durable state, replies |

The boundary is strict: **per-message logic never lives in the function.** After the handshake the function is done — frames are delivered only to the actor. Everything the function learned rides the forwarded request as headers, so the socket reaches the actor already authenticated. The `req` the actor sees carries only those application headers; transport and handshake headers (`Upgrade`, `Sec-WebSocket-*`) are stripped.

The smallest complete pairing:

```typescript
// The function half — runs once, at the handshake.
export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    if (req.headers.get("Upgrade")?.toLowerCase() !== "websocket") {
      return new Response("expected websocket", { status: 426 });
    }
    const user = await authenticate(req);      // per-connection work — done once, here
    if (!user) return new Response(null, { status: 401 });

    const headers = new Headers(req.headers);
    headers.set("x-user", user.id);            // what you learned rides as headers
    return env.ROOM.idFromName(roomFor(req)).fetch(new Request(req, { headers }));
  },
};

// The actor half — owns the live socket from here on.
export class Room extends StatefulActor {
  async webSocket(ws: WebSocket, req: Request): Promise<void> {
    const user = req.headers.get("x-user");    // already authenticated
    ws.on("message", async (data) => {         // messages dispatch one at a time
      const n = ((await this.ctx.storage.get<number>("n")) ?? 0) + 1;
      await this.ctx.storage.put("n", n);
      ws.send(`${user} #${n}: ${data}`);       // streams straight back
    });
  }
}
```

The actor opts in by defining one optional method:

```typescript
async webSocket(ws: WebSocket, req: Request): Promise<void>
```

`ws` has Node `ws` socket semantics — `ws.on("message", (data, isBinary) => ...)`, `ws.send(data)`, `ws.close(code, reason)` — not a browser socket and not Cloudflare's `WebSocketPair`/`accept()`. Text and binary frames both work. An actor with no `webSocket()` method closes incoming sockets with code `1011`.

### A Chat Room, End to End

One module exports both halves. The `ChatRoom` actor holds the room's messages and its live sockets; the default export is the front door.

```toml
# telnyx.toml
name = "chat"
main = "src/index.ts"
compatibility_date = "2026-05-01"

[actors](actors.md)
binding = "ROOM"
type    = "ChatRoom"
```

```typescript
// src/index.ts
import { StatefulActor, type ActorNamespace } from "@telnyx/edge-runtime";
import type { WebSocket } from "ws";
// `ws` is a transitive dependency of @telnyx/edge-runtime. With npm it resolves
// automatically; with pnpm or other strict layouts, install @types/ws yourself.

export class ChatRoom extends StatefulActor {
  async webSocket(ws: WebSocket, req: Request): Promise<void> {
    // The front door authenticated this connection and stamped x-user; by the
    // time the socket reaches the actor, it is already authenticated.
    const user = req.headers.get("x-user") ?? "anonymous";

    ws.send(JSON.stringify({ type: "welcome", user, present: this.ctx.count() }));

    ws.on("message", async (data, isBinary) => {
      if (isBinary) return; // this room speaks text JSON

      // Parse defensively: an uncaught throw in a handler closes the
      // socket with code 1011.
      let text: string;
      try {
        ({ text } = JSON.parse(String(data)) as { text: string });
      } catch {
        ws.send(JSON.stringify({ type: "error", error: "frames must be JSON" }));
        return;
      }

      // Durable read-modify-write. Messages dispatch one at a time per
      // instance, so this never races another socket's frame — no lock, no
      // transaction.
      const seq = ((await this.ctx.storage.get<number>("seq")) ?? 0) + 1;
      await this.ctx.storage.put("seq", seq);
      await this.ctx.storage.put(`msg:${seq}`, { user, text, at: Date.now() });

      // Fan out to every live socket on THIS room, then ack the sender.
      const delivered = this.ctx.broadcast(
        JSON.stringify({ type: "message", seq, user, text }),
      );
      ws.send(JSON.stringify({ type: "sent", seq, delivered }));
    });

    // Close and error events go through the same single-threaded dispatch;
    // a storage write in a close handler still commits. The runtime removes the socket from
    // count()/broadcast() on its own — register these only for your own
    // bookkeeping.
    ws.on("close", async (code) => {
      await this.ctx.storage.put("lastLeave", { user, code, at: Date.now() });
    });
    // Keep an error listener so transport errors land in your logs instead of
    // vanishing; the runtime already tears the socket down on error.
    ws.on("error", (err) => console.error("ws error", err));
  }

  // Plain RPC on the same actor — same instance, same one-at-a-time dispatch.
  async messageCount(): Promise<number> {
    return (await this.ctx.storage.get<number>("seq")) ?? 0;
  }
}

interface Env {
  ROOM: ActorNamespace;
}

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    const match = url.pathname.match(/^\/rooms\/([^/]+)$/);
    if (!match) return new Response("not found", { status: 404 });

    if (req.headers.get("Upgrade")?.toLowerCase() !== "websocket") {
      return new Response("expected websocket", { status: 426 });
    }

    // Browser WebSocket clients cannot set request headers, so credentials
    // ride the URL. This code runs once per connection — the right place to
    // verify a signed token. The example only checks shape: forwarded header
    // values must be printable ASCII, and should be bounded.
    const user = url.searchParams.get("user");
    if (!user || !/^[\x20-\x7e]{1,128}$/.test(user)) {
      return new Response("missing or malformed ?user=", { status: 401 });
    }

    // Attach what the front door learned; overwrite anything client-supplied.
    const headers = new Headers(req.headers);
    headers.set("x-user", user);

    // Hand off: the actor named by the room owns the socket from here on.
    return env.ROOM.idFromName(match[1]!).fetch(new Request(req, { headers }));
  },
};
```

Connect with any WebSocket client:

```
websocat "wss://<your-function-host>/rooms/lobby?user=alice"
{"type":"welcome","user":"alice","present":1}
{"text":"hello"}
{"type":"message","seq":1,"user":"alice","text":"hello"}
{"type":"sent","seq":1,"delivered":1}
```

Every socket opened on `/rooms/lobby` lands on the same `ChatRoom` instance; `/rooms/standup` is a different instance with its own `seq`, its own messages, and its own sockets. `ctx.count()` and `ctx.broadcast()` see only this instance's sockets — a broadcast never crosses actor ids, and a socket never moves between them.

### Sending to Some Sockets, Not All

`ctx.broadcast()` is all-or-nothing: one frame to every socket on the instance. There is no built-in way to address a subset — no socket list to filter, no per-socket tags. "Everyone except the sender" and "just this user" are yours to build, and on a single-threaded instance the whole mechanism is one `Map`: filled in `webSocket()`, pruned in the close listener.

```typescript
export class Room extends StatefulActor {
  // Keyed by socket, not by user: one user may hold several sockets (two tabs).
  private peers = new Map<WebSocket, { user: string }>();

  async webSocket(ws: WebSocket, req: Request): Promise<void> {
    const user = req.headers.get("x-user") ?? "anonymous";
    this.peers.set(ws, { user });
    // Close events dispatch one at a time like everything else, so this
    // delete never races a message handler mid-iteration.
    ws.on("close", () => this.peers.delete(ws));

    ws.on("message", (data) => {
      // Everyone except the sender:
      for (const peer of this.peers.keys()) {
        if (peer !== ws) peer.send(`${user}: ${data}`);
      }
    });
  }

  // One named user — every socket they have open. Call it from a message
  // handler that routes a direct-message frame, or expose it as an RPC.
  sendTo(user: string, data: string): number {
    let sent = 0;
    for (const [peer, meta] of this.peers) {
      if (meta.user === user) {
        peer.send(data);
        sent++;
      }
    }
    return sent;
  }
}
```

The map is a plain instance field, and here — unlike almost everywhere else on the platform — that is correct, with nothing written to `ctx.storage`. Sockets and instance memory share a lifetime: an open socket keeps the instance resident, and the events that replace an instance — a redeploy, an infrastructure restart — sever its sockets too. A fresh instance therefore starts with no sockets and an empty map, never one without the other; there is nothing to persist and nothing to rebuild. What should outlive the connection — who was here, what they said — goes in `ctx.storage` as usual.

### Messages Are Single-Threaded, Like Everything Else

An inbound frame is dispatched like a method call, under the execution model's "one call at a time" guarantee: while a message handler runs, frames from other sockets on the same instance, RPC calls, and the alarm all wait. That is exactly what makes the chat room's read-modify-write on `seq` safe with any number of concurrent senders.

The consequences:

- **The 30-second method budget applies to each message handler.** A handler that throws or exceeds it closes the socket with code `1011`.
- **`ws.send()` is immediate — and not held for durability.** A method's return value is held until your storage writes are durable; a sent frame is not. If a handler sends and then fails, the client keeps a frame describing state that never committed. If clients must act only on committed state, make frames re-derivable from storage on reconnect — the chat room's durable `seq` makes gaps and replays detectable.
- **Keep per-message work bounded.** Frames that arrive while a handler runs queue, up to 256 events or 1 MiB; overflow closes the socket with `1013` (back off before reconnecting), and a single inbound frame over 1 MiB closes it with `1009`. Don't stream minutes of work from one handler — chunk it across messages, or drive it from an alarm. `ws.send()` itself never blocks the handler.
- **High-frequency senders should coalesce.** Every frame costs a full dispatch — one turn of the instance's single thread, one queue slot — so a client emitting a stream of tiny messages (sensor readings, cursor positions, game state) spends the queue on frame count, not bytes: at 100 messages a second, a single handler that stalls for three seconds is enough to overflow the 256-event queue and close the socket with `1013`. Batch logical messages into one frame — an array, flushed on a short timer or a count threshold — and loop over the batch in the handler. Fifty readings in one frame cost one dispatch and one queue slot instead of fifty; just keep the batch under the 1 MiB frame cap.

An open socket also keeps the actor in memory for the duration of the connection.

### Connections End; State Doesn't

Every connection ends. Today a connection lives at most about five minutes from the handshake — even on a socket actively exchanging frames — and the cutoff surfaces as an abnormal close (code `1006`, no close frame). This cap will be raised in a future update. Function redeploys and infrastructure restarts sever sockets the same way; an actor-side restart instead closes each socket gracefully with code `1001`; a deliberate close from either side is code `1000`.

Reconnecting is the client's job: back off, reopen, rejoin the same name. `idFromName` routes the new socket back to the same actor, and everything in `ctx.storage` survived — the room's messages and `seq` are intact; only the socket is new. A reconnect is a new socket on the actor, never a resumption of the old one.

### Push Without an Inbound Frame

An actor runs only when something calls it — a frame, an RPC, or an alarm; time passing alone runs nothing. To push to connected clients without waiting for them to send anything, let the alarm make the call and fan out with `ctx.broadcast()`:

```typescript
export class Ticker extends StatefulActor {
  async webSocket(ws: WebSocket, req: Request): Promise<void> {
    // First socket arms the loop; later sockets just join the fan-out.
    if ((await this.ctx.storage.getAlarm()) === null) {
      await this.ctx.storage.setAlarm(Date.now() + 3_000);
    }
  }

  async alarm(): Promise<void> {
    this.ctx.broadcast(JSON.stringify({ type: "tick", at: Date.now() }));
    if (this.ctx.count() > 0) {
      await this.ctx.storage.setAlarm(Date.now() + 3_000); // re-arm while anyone listens
    }
  }
}
```

The alarm handler is an ordinary method call, so it can read storage, write storage, and send — a message handler on one socket can likewise broadcast to all of them, as the chat room does.

### Outbound Requests

Egress from an actor is ordinary Node: the global `fetch` and the global `WebSocket` client both work from inside any handler — call a model API and stream its output back over the socket, or dial an upstream WebSocket, exchange frames, and close it. The dispatch rules apply unchanged: outbound work inside a message handler holds the instance's only thread and runs under the 30-second budget, so ship interim results with `ws.send()` as they arrive, and chunk anything long across messages or drive it from an alarm.
