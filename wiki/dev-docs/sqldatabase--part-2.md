---
title: SqlDatabase
summary: The `SqlDatabase` binding is the in-function handle to a SQL database in
  the Telnyx Edge Compute runtime. It exposes a synchronous `prepare()` builder and
  async terminal methods (`first`, `run`, `all`, `raw`, `batch`, `exec`) that route
  through a single primary per database, so writes from a function are immediately
  readable from the CLI and the REST query endpoint.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/reference/sql-database
updated_at: 2026-08-05T13:42:03Z
---

# SqlDatabase

*Part 2 of 3 — see also: [Part 1](sqldatabase--part-1.md), [Part 3](sqldatabase--part-3.md)*

The `SqlDatabase` binding is the in-function handle to a SQL database in the Telnyx Edge Compute runtime. It exposes a synchronous `prepare()` builder and async terminal methods (`first`, `run`, `all`, `raw`, `batch`, `exec`) that route through a single primary per database, so writes from a function are immediately readable from the CLI and the REST query endpoint.

## Type Conversion

How values cross between JavaScript and SQLite, in both directions — what `bind()` accepts on the way in, and what the terminal methods hand back on the way out.

Four JavaScript types reach SQLite — `null`, `number`, `string`, and `ArrayBuffer` — plus `undefined`, which is accepted and stored as `NULL`. Every other value throws, and it throws when the statement runs rather than at the `bind()` call, because `bind()` performs no validation.

| JavaScript value | Bound as | Read back as |
| --- | --- | --- |
| `number` | `REAL` affinity — see below | `number` |
| `string` | `TEXT` | `string` |
| `null` | `NULL` | `null` |
| `undefined` | `NULL` (accepted; D1 rejects it) | `null` |
| `ArrayBuffer` | `BLOB` | `ArrayBuffer` over the binding; a JSON array of byte values over REST and the CLI |
| `boolean` | **throws** `Provided value cannot be bound to SQLite parameter N` | — |
| `Uint8Array` and other typed-array views | **throws** `Unknown named parameter` — pass the underlying `ArrayBuffer` | — |
| `bigint` | **throws** `Do not know how to serialize a BigInt` | — |
| plain object | **throws** `Unknown named parameter` | — |

Store a boolean as `0`/`1` and binary as an `ArrayBuffer`:

```ts
const bytes = new Uint8Array([9, 8, 7]);
await env.DB
  .prepare("INSERT INTO flags(active, blob) VALUES (?, ?)")
  .bind(isActive ? 1 : 0, bytes.buffer) // .buffer, not the view
  .run();
```

`.buffer` is the whole backing store, not the view. For a view that does not span its buffer, slice first: `bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength)`.

**One bound value is capped at 2 MiB** (2,097,152 bytes). A larger `ArrayBuffer` or string is rejected with `SqlParameterTooLargeError` before the statement runs. This is a ceiling of the storage engine SQL Databases share with [Stateful Actor SQL](stateful-actor-sql.md), and it applies only to values sent through `.bind()` — a value produced inside SQL, such as `randomblob()`, is not bound and is not checked. Split larger payloads, or keep them in [object storage](https://developers.telnyx.com/docs/cloud-storage/bindings) and bind the key.

A bound number arrives with **`REAL` affinity** — `SELECT typeof(?)` on a bound `42` returns `real`. Inserted into a column declared `INTEGER`, it still lands as an integer (`typeof(col)` reads back `integer`); the affinity only shows in untyped or expression contexts. In a `STRICT` table the check is exact, so binding `3.5` into an `INTEGER` column correctly fails with `cannot store REAL value in INTEGER column`.

**Reading an integer larger than 2^53 − 1 throws** `RangeError: Value is too large to be represented as a JavaScript number`. SQLite stores 64-bit integers, but result columns come back as JavaScript numbers — a value past `Number.MAX_SAFE_INTEGER` (`9007199254740991`) can be written and compared in SQL, but the read fails loudly rather than losing precision. Store large ids, snowflake keys, and nanosecond timestamps as `TEXT`.

## `first()` and `first(column)`

Return the first row, or a single column of it. No `meta`.

```ts
// Whole row, or null when the query matched nothing
const user = await env.DB
  .prepare("SELECT id, email FROM users WHERE id = ?")
  .bind(1)
  .first<{ id: number; email: string }>();

// One column, as a bare value
const total = await env.DB.prepare("SELECT COUNT(*) AS n FROM users").first<number>("n");
```

`first()` resolves to `null` when there are no rows. `first(column)` returns the value at that key; if the column is not in the result set it also resolves to `null` rather than throwing — a divergence from D1, which raises `D1_COLUMN_NOTFOUND`.

## `run()` and `all()`

Run the statement and return the full envelope. The two methods are identical.

```ts
const { results, success } = await env.DB
  .prepare("SELECT id, email FROM users WHERE org = ?")
  .bind("acme")
  .all<{ id: number; email: string }>();

// results -> [{ id: 1, email: "alice@example.com" }, ...]
```

`results` holds the rows as objects keyed by column name. For an `INSERT`, `UPDATE`, or `DELETE` it is an empty array unless the statement carries a `RETURNING` clause. The generic is a compile-time assertion only — it is not validated against the columns the query actually returns.

## `raw(options?)`

Return rows as arrays of values instead of objects, for callers that already know the column order or that feed a columnar consumer. The rows are converted after they arrive, so this is a shape convenience, not a smaller response.

```ts
const rows = await env.DB.prepare("SELECT id, email FROM users").raw();
// [[1, "alice@example.com"], [2, "bob@example.com"]]

const withHeader = await env.DB.prepare("SELECT id, email FROM users").raw({ columnNames: true });
// [["id", "email"], [1, "alice@example.com"], [2, "bob@example.com"]]
```

`{ columnNames: true }` prepends one row of column names. An empty result set returns `[]` with no header row, so check the length before treating the first entry as headers. Rows are converted from the same objects `all()` returns, so two result columns with the same name collapse into one — alias them (`SELECT a.id AS a_id, b.id AS b_id`) when joining.

## `batch(statements)`

Run several prepared statements as one atomic unit. Results come back in the order the statements were passed.

```ts
const [debited] = await env.DB.batch<{ cents: number }>([
  env.DB
    .prepare("UPDATE accounts SET cents = cents - ? WHERE id = ? RETURNING cents")
    .bind(500, "a"),
  env.DB.prepare("UPDATE accounts SET cents = cents + ? WHERE id = ?").bind(500, "b"),
]);
const remaining = debited.results[0]?.cents;
```

The whole batch commits together: if any statement fails, every earlier statement in the same batch is rolled back and the promise rejects. A batch whose middle statement violates a `UNIQUE` constraint leaves the table exactly as it was.

Every statement must come from the same database's `prepare()`. Passing a statement built by a different binding throws `env.<DB>.batch() accepts only statements created by this database's prepare().`

`batch()` is the transaction primitive for parameterized, all-or-nothing writes: explicit `BEGIN` is rejected, so a transaction cannot be opened by hand.

## `exec(query)`

Run a raw SQL script. Takes no bound parameters and returns no rows.

```ts
const { count } = await env.DB.exec(`
  CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, email TEXT UNIQUE);
  CREATE INDEX IF NOT EXISTS users_by_email ON users(email);
`);
// count -> 2
```

`count` is the number of statements in the script. Passing bind arguments throws `env.<DB>.exec() takes no bound params — use prepare().bind() for parameterized statements.` Use `exec` for schema and one-shot maintenance work, and `prepare().bind()` for anything that takes user input.

A script is **atomic**: if any statement in it fails, every statement in that script rolls back. A script that creates a table, inserts a row, and then hits an error leaves no table behind. So `exec()` either applies a whole script or changes nothing.
