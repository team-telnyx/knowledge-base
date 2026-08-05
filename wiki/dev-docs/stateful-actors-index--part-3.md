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

*Part 3 of 7 — see also: [Part 1](stateful-actors-index--part-1.md), [Part 2](stateful-actors-index--part-2.md), [Part 4](stateful-actors-index--part-4.md), [Part 5](stateful-actors-index--part-5.md), [Part 6](stateful-actors-index--part-6.md), [Part 7](stateful-actors-index--part-7.md)*

Stateful Actors on Telnyx Edge Compute give each named entity its own durable, single-threaded instance with private key/value and SQL storage, alarms, and WebSocket support. This page covers when to use them, the storage surfaces, local development, the Quick Start, shared actors across functions, and WebSocket patterns.

## Quick Start

Ship an `Account` actor end-to-end: scaffold, write the class, deploy, and curl it. Each account name is its own actor instance — `alice` and `bob` are isolated, each with their own balance, all persisted.

### What You'll Build

A function with routes that all share a single durable `Account` actor type — but each account name is its own isolated instance:

```
POST /accounts/:id/deposit   { "amount": 100 }  → { account, balance }
POST /accounts/:id/debit     { "amount": 30 }   → { account, ok, balance }
GET  /accounts/:id/balance                       → { account, balance }
GET  /health/{liveness,readiness}                → "ok"
```

A `debit` never overdraws, and a committed debit is never lost.

### Prerequisites

- The `telnyx-edge` CLI, installed and authenticated — a release with Stateful Actor deploy support. **v0.2.2 and earlier cannot ship an actor project** (`new-func --actor` appears to work, but `ship` fails); upgrade from the [releases page](https://github.com/team-telnyx/edge-compute/releases).
- A Telnyx API key.
- Node.js (for `npm`).

### 1. Authenticate

```
telnyx-edge auth api-key set <YOUR_API_KEY>
telnyx-edge auth status
```

### 2. Scaffold the Actor Project

```
telnyx-edge new-func --actor --name=account
cd account
npm install
```

This writes an umbrella `telnyx.toml` (with a `[actors](actors.md)` block), a sample actor class, a `fetch` handler, and registers the function (writes a `func_id` into `telnyx.toml`). `npm install` pulls in `@telnyx/edge-runtime`.

### 3. Write the Account Actor

Replace the scaffolded actor class with `src/account.ts`. It holds one value — the balance — in `this.ctx.storage`:

```typescript
import { StatefulActor } from "@telnyx/edge-runtime";

export class Account extends StatefulActor {
  /** Add funds. Returns the new balance. */
  async deposit(amount: number): Promise<{ balance: number }> {
    const balance = (await this.ctx.storage.get<number>("balance")) ?? 0;
    const next = balance + amount;
    await this.ctx.storage.put("balance", next);
    return { balance: next };
  }

  /** Subtract funds if sufficient. Atomic — single-threaded dispatch means
   *  two debits on the same account can't both pass the check. */
  async debit(amount: number): Promise<{ ok: boolean; balance: number }> {
    const balance = (await this.ctx.storage.get<number>("balance")) ?? 0;
    if (balance < amount) return { ok: false, balance }; // insufficient funds
    const next = balance - amount;
    await this.ctx.storage.put("balance", next);
    return { ok: true, balance: next };
  }

  /** Read the current balance. */
  async balance(): Promise<{ balance: number }> {
    return { balance: (await this.ctx.storage.get<number>("balance")) ?? 0 };
  }
}
```

### 4. Write the Fetch Handler

Replace `src/index.ts` with a handler that routes HTTP to actor method calls. It re-exports the actor class (so it ships with the bundle) and calls it through the `ACCOUNT` binding on `env`:

```typescript
// Re-export the actor class from the entry point so it is bundled and shipped
// with the function. The exported class name must equal the [actors](actors.md) type.
export { Account } from "./account";
import type { Account } from "./account";

import {
  type ActorNamespace,
  type ActorStub,
  type IdFromNameOptions,
} from "@telnyx/edge-runtime";

type AccountStub = ActorStub & Pick<Account, "deposit" | "debit" | "balance">;
interface AccountNamespace extends ActorNamespace {
  idFromName(name: string, options?: IdFromNameOptions): AccountStub;
}
interface Env {
  ACCOUNT: AccountNamespace;
}

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);

    if (url.pathname === "/health/liveness") return new Response("ok");
    if (url.pathname === "/health/readiness") return new Response("ok");

    const m = url.pathname.match(/^\/accounts\/([^/]+)\/(deposit|debit|balance)$/);
    if (!m) return new Response("not found", { status: 404 });

    const id = m[1]!;
    const action = m[2]!;
    const stub = env.ACCOUNT.idFromName(id);

    if (action === "deposit" && req.method === "POST") {
      const body = (await req.json().catch(() => ({}))) as { amount?: number };
      if (typeof body.amount !== "number")
        return Response.json({ error: "amount (number) required" }, { status: 400 });
      const result = await stub.deposit(body.amount);
      return Response.json({ account: id, ...result });
    }

    if (action === "debit" && req.method === "POST") {
      const body = (await req.json().catch(() => ({}))) as { amount?: number };
      if (typeof body.amount !== "number")
        return Response.json({ error: "amount (number) required" }, { status: 400 });
      const result = await stub.debit(body.amount);
      return Response.json({ account: id, ...result });
    }

    if (action === "balance" && req.method === "GET") {
      const result = await stub.balance();
      return Response.json({ account: id, ...result });
    }

    return new Response("not found", { status: 404 });
  },
};
```

### 5. Update `telnyx.toml`

Point the `[actors](actors.md)` binding at your class. The scaffold generated a sample binding; change it to `ACCOUNT` → `Account`:

```toml
name = "account"
main = "src/index.ts"
compatibility_date = "2026-05-01"

[actors](actors.md)
binding = "ACCOUNT"   # the property on env — your handle
type    = "Account"   # the class to instantiate per account name

[edge_compute]
func_id = "..."       # created by new-func; leave as-is
func_name = "account"
```

### 6. Deploy

```
telnyx-edge ship
```

`ship` bundles the project, uploads it, and monitors the deploy — wait for `✅ Func 'account' is now deployed!` (in `telnyx-edge list`, the function's status becomes `deploy_ok`).

### 7. Hit the URL

`ship` prints a URL like `account-<id>.telnyxcompute.com`. The function may take a moment to come up — poll the health endpoint until it returns 200:

```
B=https://account-<id>.telnyxcompute.com

# wait for it to come up
curl -sS --retry 30 --retry-delay 5 --retry-connrefused "$B/health/liveness"
```

Now exercise it — two accounts, no overdraw, isolation, persistence:

```
# alice deposits 100, then debits 30
curl -sS -X POST $B/accounts/alice/deposit -H 'content-type: application/json' -d '{"amount":100}'
# → {"account":"alice","balance":100}
curl -sS -X POST $B/accounts/alice/debit   -H 'content-type: application/json' -d '{"amount":30}'
# → {"account":"alice","ok":true,"balance":70}

# an overdraw is rejected — balance unchanged
curl -sS -X POST $B/accounts/alice/debit   -H 'content-type: application/json' -d '{"amount":1000}'
# → {"account":"alice","ok":false,"balance":70}

# bob is a separate instance with its own balance
curl -sS -X POST $B/accounts/bob/deposit   -H 'content-type: application/json' -d '{"amount":5}'
# → {"account":"bob","balance":5}

# isolation + persistence: alice is still 70, bob is 5
curl -sS $B/accounts/alice/balance   # → {"account":"alice","balance":70}
curl -sS $B/accounts/bob/balance     # → {"account":"bob","balance":5}
```

You should see:

- `alice` ends at 70 (100 − 30; the 1000 debit was rejected)
- `bob` is independent at 5
- `alice` is unchanged by `bob`'s activity (isolation), and survives across requests (persistence)
