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

*Part 2 of 7 — see also: [Part 1](stateful-actors-index--part-1.md), [Part 3](stateful-actors-index--part-3.md), [Part 4](stateful-actors-index--part-4.md), [Part 5](stateful-actors-index--part-5.md), [Part 6](stateful-actors-index--part-6.md), [Part 7](stateful-actors-index--part-7.md)*

Stateful Actors on Telnyx Edge Compute give each named entity its own durable, single-threaded instance with private key/value and SQL storage, alarms, and WebSocket support. This page covers when to use them, the storage surfaces, local development, the Quick Start, shared actors across functions, and WebSocket patterns.

## SQL Storage

Every Stateful Actor has a private, durable embedded SQLite database reachable at `this.ctx.storage.sql`. It sits beside the key/value store under the same `this.ctx.storage`, but it is a separate engine: one SQLite database per actor instance, queried with real SQL.

Reach for it when a single entity's state is relational or needs queries the key/value store can't answer without a scan — aggregates, `GROUP BY`, secondary indexes, joins *within* the one actor. It is not a shared database: each instance sees only its own data, and there are no cross-actor queries or joins. When more than one function — or an operator at a terminal — has to query the same rows, use a standalone [SQL Database](sql-database.md) instead.

`ctx.storage.sql` requires `@telnyx/edge-runtime` **0.6.0 or later**; the `transactionSync()` type ships in **0.8.0**, so use the latest SDK.

### The Surface

```typescript
interface SqlStorage {
  exec<T = Record<string, SqlValue>>(query: string, ...bindings: SqlValue[]): SqlCursor<T>;
}

interface SqlCursor<T> extends Iterable<T> {
  toArray(): T[];
}

type SqlValue = null | number | string | ArrayBuffer;
```

`exec` is **synchronous** — it does not return a `Promise`. This is deliberate and unlike every other member of `ctx.storage`: the database is a local file in the actor's own process, so there is no network hop to await.

```typescript
import { StatefulActor } from "@telnyx/edge-runtime";

export class Inventory extends StatefulActor {
  async record(sku: string, cents: number) {
    this.ctx.storage.sql.exec(
      `CREATE TABLE IF NOT EXISTS orders(sku TEXT, cents INTEGER, ts INTEGER)`,
    );
    this.ctx.storage.sql.exec(
      `INSERT INTO orders(sku, cents, ts) VALUES (?, ?, ?)`,
      sku,
      cents,
      Date.now(),
    );
    // An aggregate the key/value store can't answer without scanning every key:
    return this.ctx.storage.sql
      .exec(
        `SELECT sku, SUM(cents) AS total FROM orders
         GROUP BY sku ORDER BY total DESC LIMIT 5`,
      )
      .toArray();
  }
}
```

There is no schema step in the manifest — any actor that calls `ctx.storage.sql` gets a database, created on first use. Create your tables with `CREATE TABLE IF NOT EXISTS` (a cheap no-op once they exist) at the top of the methods that need them.

### Binding Parameters

Use positional `?` placeholders and pass the values as trailing arguments. Always bind user input — never build SQL by string concatenation.

```typescript
const rows = this.ctx.storage.sql
  .exec(`SELECT * FROM orders WHERE sku = ? AND cents > ?`, sku, 1000)
  .toArray();
```

A bound value must be one of four types: `null`, `number`, `string`, or `ArrayBuffer` (for binary). Result columns come back as those same four types:

| SQLite type | JavaScript value you get back |
| --- | --- |
| `INTEGER` | `number` |
| `REAL` | `number` |
| `TEXT` | `string` |
| `BLOB` | `ArrayBuffer` |
| `NULL` | `null` |

### Reading Results: the Cursor

`exec` returns a `SqlCursor` — a **single-pass** iterator over the result rows. Drain it once, either by iterating or with `toArray()`:

```typescript
// Drain to an array (the common case):
const all = this.ctx.storage.sql.exec(`SELECT n FROM nums ORDER BY n`).toArray();

// Or stream row by row, without materializing the whole set:
for (const row of this.ctx.storage.sql.exec(`SELECT n FROM nums ORDER BY n`)) {
  handle(row.n);
}
```

Single-pass means the rows are consumed as you read them. After you iterate a cursor to the end, `toArray()` on that same cursor returns `[]`; calling `toArray()` a second time also returns `[]`. If you iterate partway and then call `toArray()`, you get the *rest* of the rows. Run `exec` again for a fresh pass.

`exec` is generic in the row type — `exec<Order>(...)` types the returned rows — but the type is a compile-time assertion only, not validated at runtime.

### Multiple Statements in One `exec`

A query string may contain several `;`-separated statements — useful for pasting a schema or a small migration. Every statement executes, in order; the bound parameters apply to the **last** statement, and the returned cursor is over the **last** statement's rows:

```typescript
const rows = this.ctx.storage.sql
  .exec(
    `CREATE TABLE IF NOT EXISTS t(x INTEGER);
     INSERT INTO t VALUES (1);
     SELECT x FROM t WHERE x >= ?;`,
    1,
  )
  .toArray(); // the final SELECT's rows; the CREATE and INSERT ran too
```

Statements run independently — if one fails, `exec` throws, but the statements before it have already been applied. Wrap the batch in a `transactionSync` callback when it must be all-or-nothing.

Multi-statement splitting is a best-effort TypeScript tokenizer, not exact SQLite parsing. It handles all realistic SQL, but unquoted keyword-identifiers (a column named `end`, `begin`, or `case` in a deep position) can confuse the splitter. **Quote reserved-word identifiers** (`"end"`) to avoid edge cases.

### Transactions

Wrap related writes so they commit together — or roll back together — with `transactionSync`. It runs your callback synchronously, commits when it returns, and rolls back every write if it throws:

```typescript
async transfer(from: string, to: string, cents: number) {
  this.ctx.storage.transactionSync(() => {
    this.ctx.storage.sql.exec(`UPDATE accounts SET cents = cents - ? WHERE id = ?`, cents, from);
    this.ctx.storage.sql.exec(`UPDATE accounts SET cents = cents + ? WHERE id = ?`, cents, to);
    // throw here — e.g. on an overdraft check — and neither UPDATE is applied
  });
}
```

The callback returns a value — `transactionSync` passes it through, so you can read back a result computed inside the transaction.

Two rules, both enforced by the runtime:

- **`transactionSync` is the only transaction API.** Raw transaction-control statements — `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT` — are rejected by `exec()` with `SqlTransactionControlError`, anywhere in a statement batch.
- **The callback must be synchronous.** Passing an `async` function throws `SqlAsyncTransactionError` and commits nothing — the transaction commits when the callback returns, so statements after an `await` would run outside it. Do async work before or after, not inside.

Because a single actor instance processes one method at a time, you never contend with another writer inside your own database — the actor *is* the lock.

### Bulk Writes

Each standalone `exec` write commits and flushes to disk on its own, which is slow in a loop. Wrap a batch in one `transactionSync` and it commits (and flushes) once:

```typescript
this.ctx.storage.transactionSync(() => {
  for (const row of rows) this.ctx.storage.sql.exec(`INSERT INTO t(v) VALUES (?)`, row);
});
```

The difference is large: thousands of individual auto-commit inserts take seconds; the same inserts inside one transaction take tens of milliseconds. Batch anything hot.

### Indexes

The database holds one entity's working set, but scans still cost time and — as it grows — memory. Add an index on any column you filter or order by frequently:

```typescript
this.ctx.storage.sql.exec(`CREATE INDEX IF NOT EXISTS orders_by_sku ON orders(sku)`);
```

### Limits

- **1 GB per actor database.** Enforced by the engine — writes past it fail.
- **2 MiB per bound value.** A bind larger than 2 MiB (2,097,152 bytes) is rejected with `SqlParameterTooLargeError` before the statement runs. There is no cap on output row size.
- **Up to 32,766 bound parameters** in a single statement (SQLite's variable limit).
- **Integers come back as JavaScript `number`.** SQLite stores 64-bit integers, but `exec` returns integer columns as JS numbers. A value beyond `Number.MAX_SAFE_INTEGER` (2^53 − 1, i.e. `9007199254740991`) can be written and compared in SQL, but **reading that column throws** `RangeError: Value is too large to be represented as a JavaScript number`. Store large ids, bitmasks, or nanosecond timestamps as `TEXT` (or `BLOB`), or keep integers within the safe range.
- **Foreign keys are ON** — a `REFERENCES` violation raises `FOREIGN KEY constraint failed`.
- Failed statements (syntax errors, constraint violations) throw from `exec`; the actor keeps running, so catch and handle them like any other error.
