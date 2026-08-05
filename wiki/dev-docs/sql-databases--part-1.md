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

*Part 1 of 6 — see also: [Part 2](sql-databases--part-2.md), [Part 3](sql-databases--part-3.md), [Part 4](sql-databases--part-4.md), [Part 5](sql-databases--part-5.md), [Part 6](sql-databases--part-6.md)*

SQL Databases are standalone SQLite databases on Telnyx Edge Compute that live outside any function and are reached through a single primary. They can be queried from inside a TypeScript function via the `env` binding, or from anywhere via the REST API and the `telnyx-edge storage sqldb` CLI, with the same data visible through both paths.

## Overview

A SQL database is a SQLite database that lives on its own, outside any function. Create it once, bind it by id, and query it as `env.DB` from as many functions as need it — or from the CLI and REST API without deploying anything at all. There is no server to size and nothing to deploy per database. Every path reaches the same data through one primary, so writes serialize and there is no replica lag to reason about.

The engine is stock SQLite (3.51.3 in production today), so the dialect and built-in functions are SQLite's, not a subset invented for the edge. Foreign keys are on and enforced, which is worth knowing if you are arriving from a SQLite build that leaves them off: a `REFERENCES` violation fails the statement.

## Two Ways to Reach a Database

The same database is reachable two ways. Pick based on where the code runs.

|  | `env` binding | REST API and CLI |
| --- | --- | --- |
| **Where** | Inside an edge function — TypeScript only | Anywhere — any language, any host, no function required |
| **Auth** | Injected by the runtime; no API key in your code | Your `TELNYX_API_KEY` as a bearer token |
| **Shape** | `env.DB.prepare(sql).bind(...).all()` | `POST https://api.telnyx.com/v2/storage/sqldbs/{id}/actions/query`, `telnyx-edge storage sqldb execute` |
| **Use it for** | Reads and writes on the request path | Creating databases, applying schema and migrations, backfills, one-off inspection — SQL you wrote yourself, since this path has no parameter binding |

A row written by a function is visible to the next CLI query, and a table created from the CLI is visible to the next request. That is what lets schema exist before any code does: create the database, apply [Migrations](migrations.md), then ship a function that binds it.

## How SQL Databases Work

### A Standalone Resource

Create a database with the [CLI](cli.md) or the REST API and it comes back immediately with status `pending`; it reaches `provision_ok` a few seconds later — typically 2 to 11, since provisioning is picked up by a poll loop rather than done inline. A query issued while it is still `pending` returns HTTP 409 `Database is not ready`. In a script, poll `get` until the status is `provision_ok` rather than sleeping a fixed interval.

The **UUID is the only durable handle**. A `telnyx.toml` binding takes an id, never a name:

```
[storage.sqldb.DB]
id = "0198c2c5-8f1e-7a3d-9b21-6e4a0d5f1c88"
```

The name is a label, unique within the organization, matching `^[a-z0-9-]+$`. It exists so humans can find a database in a list; the CLI resolves a name to an id locally as a convenience, while REST calls and manifests take the id. There is no rename, and deleting a database frees its name for a new, empty database with a different id.

Nothing is deployed per database, and nothing about a database is derived from a function. Shipping, rolling back, or deleting a function does not touch the data.

### One Primary, Serialized Writes

Today every read and every write for a given database funnels through a single primary, so a caller never contends with a second writer: not another region, not a replica, not a second connection opened by a different caller. That is the current topology rather than a promise about future ones; what you can design against is that statements against one database are serialized, and that every access path sees the same data.

Two consequences, both worth designing around:

- **Writes are serialized.** Concurrent writers queue behind one another instead of contending for the database. Lost-update anomalies are still possible at the *application* level — two callers that each read, compute, and write can still clobber each other — which is what `batch()` exists for.
- **Statements run one at a time.** The database is single-threaded. A slow statement occupies it and other callers wait behind it. That is the cost of the property above.

Keep statements bounded. A simple `SELECT 1` round-trips in about 10 ms warm and a 5,000-row read in about 160 ms, so the cost that matters is the one a slow statement imposes on everything queued behind it. Long analytical scans belong in a warehouse, not here — see [Limits](limits.md). Indexes matter for the same reason they matter in any SQLite deployment, and more so because the cost is paid by every other caller:

```
CREATE INDEX IF NOT EXISTS links_by_slug ON links(slug);
```

### Sharing Across Functions

A database is not owned by the function that first wrote to it. Any number of functions can declare a binding to the same id, and each one sees the same tables and the same rows. The **binding name is a local alias**, declared per function. One function can call the database `DB` and another can call the same id `SHARED`; both statements land in the same place.

```
# links-api/telnyx.toml
[storage.sqldb.DB]
id = "0198c2c5-8f1e-7a3d-9b21-6e4a0d5f1c88"
```

```
# analytics-worker/telnyx.toml
[storage.sqldb.SHARED]
id = "0198c2c5-8f1e-7a3d-9b21-6e4a0d5f1c88"
```

Because the alias is local, nothing in the schema records which function created a table. Coordination between functions is ordinary database work: agree on a schema, own it in migrations, and use `batch()` where a sequence has to be atomic.

The id is validated when a function ships. An id that does not exist, belongs to another organization, or is not yet `provision_ok` fails the deploy rather than producing a function with a dead binding — though the failure currently surfaces as a generic `API error (HTTP 500)` that never names the binding, so if a ship starts failing right after a `[storage.sqldb]` edit, re-check the id and the database's status before believing the retry-later advice. The check reads the database record rather than opening a connection, so it is not a promise that the first query will succeed — only that the id resolves to a database this organization owns.

### Isolation

Isolation runs along two lines, both enforced by the platform rather than by convention.

- **Database to database.** Two bindings in the same function are two separate databases. `env.DB` cannot see `env.DB2`'s tables and `env.DB2` cannot see `env.DB`'s — each direction fails with `no such table`. There is no cross-database query: each statement addresses exactly one id, and one database cannot be joined to another.
- **Organization to organization.** A database belongs to the organization that created it. An id from another organization returns `404` — the same response as an id that never existed, so existence cannot be probed. A function can only ever reach its own organization's databases.

### Consistency and Durability

Because there is one primary and no replicas, consistency is the simple kind:

- **A write that resolves has committed.** When `all()`, `run()`, `batch()`, or `exec()` resolves without throwing, the transaction has committed on the primary and every later reader sees it.
- **Reads reflect prior writes.** Both access paths reach the same primary, so there is no replica lag to design around and no eventual-consistency window between the function path and the REST path.
- **Data outlives functions.** Rows written before a deploy are there after it — across redeploys of the functions that bind the database, across CLI and REST sessions, and across the creation of other databases in the same organization.

Deletion is asynchronous: for a few seconds the record reports `status: deleting` — queries return `409` and the name is still held — and then the id turns `404` and the name frees. Re-creating the same name after that produces a new, empty database under a new id, so poll `get` until the `404` before re-creating. Keep the schema in version-controlled [Migrations](migrations.md).
