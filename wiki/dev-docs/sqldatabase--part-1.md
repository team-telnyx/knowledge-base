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

*Part 1 of 3 — see also: [Part 2](sqldatabase--part-2.md), [Part 3](sqldatabase--part-3.md)*

The `SqlDatabase` binding is the in-function handle to a SQL database in the Telnyx Edge Compute runtime. It exposes a synchronous `prepare()` builder and async terminal methods (`first`, `run`, `all`, `raw`, `batch`, `exec`) that route through a single primary per database, so writes from a function are immediately readable from the CLI and the REST query endpoint.

## Overview

`env.<BINDING>` (a `SqlDatabase`) is the in-function handle to a SQL database. The runtime routes the call for you, so function code holds no API key. Every database is served by one primary that serializes writes, and the binding, the [CLI](cli.md), and the REST query endpoint all funnel through that same primary — a row written from a function is immediately readable from the CLI, and the reverse.

```ts
interface SqlDatabase {
  prepare(query: string): SqlPreparedStatement;
  batch<T>(statements: SqlPreparedStatement[]): Promise<SqlQueryResult<T>[]>;
  exec(query: string): Promise<SqlExecResult>;
}

interface SqlPreparedStatement {
  bind(...values: unknown[]): SqlPreparedStatement;
  first<T>(column: string): Promise<T | null>;
  first<T>(): Promise<T | null>;
  run<T>(): Promise<SqlQueryResult<T>>;
  all<T>(): Promise<SqlQueryResult<T>>;
  raw<T>(options?: { columnNames?: boolean }): Promise<T[]>;
}

interface SqlQueryResult<T> {
  results: T[];
  success: boolean;
  meta: SqlQueryResultMeta;
}

interface SqlQueryResultMeta {
  duration: number;
  rows_read: number;
  rows_written: number;
  last_row_id: number;
  changes: number;
}

interface SqlExecResult {
  count: number;
  duration: number;
}
```

Every generic above has a default in the shipped types, so each method is usable without an explicit type argument — `all()` and `run()` hand back rows typed as plain records, and `raw()` hands back arrays of values.

Key behaviors:

- **`prepare` is synchronous; every terminal is async.** `prepare` builds a statement locally — nothing crosses the wire until `first`, `run`, `all`, `raw`, `batch`, or `exec` is awaited.
- **`bind` returns a new statement.** It never mutates the statement it was called on, so a prepared statement can be reused with different values.
- **`run()` is an alias for `all()`.** Both send the same request and return the same `SqlQueryResult`, rows included — `run()` on a `SELECT` returns rows. This matches Cloudflare D1.
- **`batch()` is atomic.** All statements commit together or none do.
- **`exec()` returns no rows** — only a statement count. Use it for schema scripts.
- **`success` is always `true` on a resolved promise.** Failures reject; they are never reported through the flag.
- **Errors throw plain `Error` objects.** There is no typed error class and no error-code taxonomy. See [#Errors](errors.md).
- **Transaction control statements are rejected.** SQL containing `BEGIN`, `COMMIT`, `ROLLBACK`, or `SAVEPOINT` fails when it runs — through a prepared statement or through `exec()` — with `SqlTransactionControlError` in the message. Transaction boundaries belong to the runtime; use `batch()` for all-or-nothing writes.

## Reading What a Write Touched

`meta` reports the statement's own accounting — `last_row_id`, `changes`, `rows_read`, `rows_written`, and `duration`. `RETURNING` is the more precise option, and worth preferring for anything you branch on. It names the rows the statement actually touched, so it survives concurrency: every caller of a database shares one connection, and `meta` describes the statement that most recently ran on it.

```ts
// The id of a new row
const row = await env.DB
  .prepare("INSERT INTO users(email) VALUES (?) RETURNING id")
  .bind("alice@example.com")
  .first<{ id: number }>();
const newId = row?.id;

// Exactly which rows an UPDATE touched, not just how many
const { results } = await env.DB
  .prepare("UPDATE users SET active = 0 WHERE last_seen < ? RETURNING id")
  .bind(cutoff)
  .run<{ id: number }>();
const changed = results.length;
```

SQLite accepts `RETURNING` on `INSERT`, `UPDATE`, and `DELETE`, and the rows it hands back are exactly the rows the statement touched. `SELECT changes()` reports the count instead, but it reads whichever statement most recently ran on the shared connection, so a concurrent write can land in between. When a bare count is all you need, issue it in the same `batch()` as the write so nothing can interleave:

```ts
const [, counted] = await env.DB.batch<{ n: number }>([
  env.DB.prepare("DELETE FROM sessions WHERE expires_at < ?").bind(Date.now()),
  env.DB.prepare("SELECT changes() AS n"),
]);
const deleted = counted.results[0].n;
```

## `prepare(query)`

Build a statement. Synchronous, and safe to call once and reuse.

```ts
const stmt = env.DB.prepare("SELECT id, email FROM users WHERE org = ?");
const acme = await stmt.bind("acme").all<{ id: number; email: string }>();
const globex = await stmt.bind("globex").all<{ id: number; email: string }>();
```

A query string may hold several `;`-separated statements. All of them execute in order, and the rows that come back are the final statement's — the same rule Cloudflare's Durable Object SQL storage follows. Bound parameters apply to that final statement only: place placeholders nowhere else, because the earlier statements run without bindings and a `?` in one of them fails.

## `bind(...values)`

Attach values to the placeholders in the query and get back a new statement. Always bind user input — never build SQL by string concatenation.

```ts
const stmt = env.DB
  .prepare("INSERT INTO events(name, at, payload) VALUES (?, ?, ?)")
  .bind("signup", Date.now(), null);
```

Placeholders are positional: anonymous `?` and ordered `?NNN` (1-indexed) both work, and values are consumed in argument order.
