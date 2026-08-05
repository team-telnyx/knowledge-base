---
title: SQL Databases
summary: SQL Databases are standalone SQLite databases on Telnyx Edge Compute that
  live outside any function and are reached through a single primary. They can be
  queried from inside a TypeScript function via the `env` binding, or from anywhere
  via the REST API and the `telnyx-edge storage sqldb` CLI, with the same data visible
  through both paths.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/sqldb
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/cli
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/concepts/how-sqldb-works/index
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/limits
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/migrations
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/sqldb/reference/index
updated_at: 2026-08-05T13:42:39Z
---

# SQL Databases

*Part 6 of 6 — see also: [Part 1](sql-databases--part-1.md), [Part 2](sql-databases--part-2.md), [Part 3](sql-databases--part-3.md), [Part 4](sql-databases--part-4.md), [Part 5](sql-databases--part-5.md)*

SQL Databases are standalone SQLite databases on Telnyx Edge Compute that live outside any function and are reached through a single primary. They can be queried from inside a TypeScript function via the `env` binding, or from anywhere via the REST API and the `telnyx-edge storage sqldb` CLI, with the same data visible through both paths.

## Runtime API

The types in this reference are exported from `@telnyx/edge-runtime` (TypeScript) and describe version **≥ 0.9.0** — the first release that exports `SqlDatabase` and wires the `env` binding. They describe the **`env` binding**, the in-function surface. Running SQL from outside a function — schema changes, ad-hoc queries, migrations — goes over a separate REST path, covered in the [CLI](cli.md) reference.

The SQL Databases Runtime API is a single binding type plus the statement and result types its methods return. A database declared as `[storage.sqldb.<NAME>]` in `telnyx.toml` resolves on `env.<NAME>` as a `SqlDatabase`.

| Surface | Where it lives | What it's for |
| --- | --- | --- |
| `SqlDatabase` | `env.<BINDING>` | The binding handle — `prepare`, `batch`, `exec`. |
| `SqlPreparedStatement` | returned by `prepare()` | `bind()`, then one terminal: `first`, `run`, `all`, `raw`. |
| `SqlQueryResult<T>` | resolved by `run()`, `all()`, and each entry of `batch()` | `{ results, success, meta }` — the rows plus their envelope. |
| `SqlQueryResultMeta` | `SqlQueryResult.meta` | `duration`, `rows_read`, `rows_written`, `last_row_id`, `changes` — the statement's own accounting. |
| `SqlExecResult` | resolved by `exec()` | `{ count, duration }` — how many statements ran. Returns no rows. |

### Getting the Binding

```
import { env } from "@telnyx/edge-runtime";

// env.DB is a SqlDatabase, from [storage.sqldb.DB] in telnyx.toml
const { results } = await env.DB
  .prepare("SELECT id, email FROM users WHERE id = ?")
  .bind(1)
  .all<{ id: number; email: string }>();
```

Read the binding off the **imported** `env` — not the `env` argument of `fetch(request, env)`. The object handed to `fetch` carries actor bindings only: `env.DB` on it is `undefined`, and the call fails at runtime with `Cannot read properties of undefined (reading 'prepare')` even though it type-checks cleanly. The generated types deliberately declare the binding in both places, so the compiler will not catch this.

Declaring the binding is covered in the [Quick Start](quick-start.md). The binding resolves at runtime from `telnyx.toml`; run `telnyx-edge types` after editing the manifest to regenerate `telnyx-env.d.ts`, which types `env.<NAME>` as a `SqlDatabase`. That command checks the `@telnyx/edge-runtime` version declared in `package.json` and fails with `@telnyx/edge-runtime <version> does not export SqlDatabase (requires >= 0.9.0)` when the floor is not met.

## Limits

| Limit | Value | Behavior past it |
| --- | --- | --- |
| Database size | 1 GiB | Writes fail the way SQLite fails on a full disk |
| One bound value | 2 MiB | `SqlParameterTooLargeError`, before the statement runs |
| Bound parameters per statement | 32,766 | SQLite's variable limit |
| SQL script, REST and CLI | ~4 MiB | `422` — the transport rejects the request with `stream too large`; past 8 MiB, `413` — `SQL body exceeds the maximum size` |
| Rows returned by one statement | ~4 MiB | The query fails with a `ResourceExhausted … larger than max` error — on the REST path and the `env` binding alike |
| Expression tree depth | 1,000 | `Expression tree is too large` |
| Database name | `^[a-z0-9-]+$`, up to 255 characters | Character-set violations return `422`; past 255 characters the create fails with `500`; a duplicate name returns `409` |

The ~4 MiB script ceiling covers the whole SQL script sent over the REST query path — which is also what `telnyx-edge storage sqldb execute --file` and `migrations apply` use. The service advertises an 8 MiB gate and returns the `413` past it, but the transport underneath rejects anything over roughly 4 MiB (4,194,304 bytes, less a few hundred bytes of envelope) with a `422` whose detail ends in `stream too large` — so ~4 MiB is the number to plan against, and a large seed file needs splitting across several calls.

Result sets are capped at the same ~4 MiB, per statement. A query whose rows exceed it fails with a `ResourceExhausted … trying to send message larger than max` error, through REST and through the `env` binding alike. Only shipping the rows is capped — computing over the same data server-side (`length()`, aggregates) is fine — so page through large reads instead of selecting them whole.

The 2 MiB cap applies only to values passed through `.bind()`. A value produced inside SQL is never bound and never checked, which is why `randomblob(100000000)` stores without complaint. Keep anything approaching either figure — images, archives, model weights — in object storage and bind the key instead.

Database size and bound-value size come from the SQLite storage engine that SQL Databases share with [Per-Actor SQLite](per-actor-sqlite.md), so the same numbers apply on both surfaces.

### Query Performance

A database is served by one primary, and statements run one at a time. A long statement delays everything else queued against that database, so the useful discipline is keeping individual statements short.

| Query | Typical |
| --- | --- |
| Simple statement, warm | ~10 ms round trip |
| 5,000-row read | ~160 ms |

Add indexes on the columns you filter and order by, page through large result sets instead of selecting them whole, and maintain a summary table on write rather than aggregating across millions of rows on read. Long analytical scans belong in a warehouse, not here.

## Related Resources

- [Quick Start](quick-start.md) — Create a database, apply a schema, bind it, query it
- [How SQL Databases Work](how-sql-databases-work.md) — The single primary, sharing, and what durability means today
- [Migrations](migrations.md) — Versioned schema changes with `storage sqldb migrations`
- [Runtime API](runtime-api.md) — The `env` binding surface (`SqlDatabase`)
- [CLI](cli.md) — Create, inspect, and query databases from the terminal
- [Limits](limits.md) — Size and duration ceilings, and known gaps
- [Bindings](bindings.md) — How the `env` binding surface works
- [Stateful Actor SQL](stateful-actor-sql.md) — The private, per-instance SQLite database
- [KV](kv--part-1.md) — Key-value storage for read-heavy lookups
- [CLI Reference](cli-reference--part-1.md) — The full `telnyx-edge` command surface
