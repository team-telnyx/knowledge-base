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

*Part 2 of 6 — see also: [Part 1](sql-databases--part-1.md), [Part 3](sql-databases--part-3.md), [Part 4](sql-databases--part-4.md), [Part 5](sql-databases--part-5.md), [Part 6](sql-databases--part-6.md)*

SQL Databases are standalone SQLite databases on Telnyx Edge Compute that live outside any function and are reached through a single primary. They can be queried from inside a TypeScript function via the `env` binding, or from anywhere via the REST API and the `telnyx-edge storage sqldb` CLI, with the same data visible through both paths.

## SQL Databases vs Per-Actor SQL

Stateful Actors also have SQLite, at [Stateful Actor SQL](stateful-actor-sql.md). Both surfaces are SQLite, which is where the confusion starts. They solve different problems.

|  | SQL Database (`env.DB`) | Actor SQL (`ctx.storage.sql`) |
| --- | --- | --- |
| **Scope** | One database, shared by the functions that bind its id | One private database per actor instance |
| **Reached from** | Any bound function, the CLI, the REST API | Only from inside that one actor instance |
| **API shape** | Async — `await env.DB.prepare(sql).bind(...).all()` | Synchronous — `ctx.storage.sql.exec(sql, ...)` returns a cursor |
| **Use it for** | Application data more than one caller reads: catalogs, links, accounts, anything an operator also needs to query | State owned by a single entity — a room, a session, a device — where the actor itself is the lock |

A per-actor database cannot be queried from outside its actor and cannot join across instances; there is no CLI or REST path to it. A SQL database can be queried from anywhere, but no caller gets exclusive access to it — concurrent callers interleave, and correctness across statements comes from `batch()`, not from holding the database. Explicit `BEGIN` is rejected on both surfaces; the runtime owns transaction boundaries.

## Choosing Between SQL, KV, and Per-Actor SQLite

Three storage surfaces, three different scopes. They can be used together in one application.

|  | SQL Database | [KV](kv--part-1.md) | [Per-Actor SQLite](per-actor-sqlite.md) |
| --- | --- | --- | --- |
| **Data model** | Relational tables, full SQL | Key to opaque bytes | Relational tables, full SQL |
| **Scope** | One dataset shared by every function bound to its id | One namespace in a single global store | One private database per actor instance |
| **Reached from** | Any bound function, the CLI, the REST API | Any function, the CLI, the REST API | Only inside that one actor instance |
| **Call shape** | `await env.DB.prepare(...).all()` | `await env.KV.get(key)` | `ctx.storage.sql.exec(...)` — synchronous |
| **Concurrency** | One primary; statements serialized | Last-write-wins per key | The actor instance is the lock |
| **Reach for it when** | Data is relational and more than one caller reads it | Lookups are by key and reads dominate | State belongs to one entity and nothing else reads it |

The distinction that catches people is the last column. Per-actor SQLite is the same engine but a *private* database per instance — it cannot be queried from the CLI, cannot be joined across instances, and has no REST path. A SQL database is the opposite: queryable from anywhere, but no caller ever holds it exclusively.
