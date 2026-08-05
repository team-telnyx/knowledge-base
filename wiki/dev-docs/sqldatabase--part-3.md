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

*Part 3 of 3 — see also: [Part 1](sqldatabase--part-1.md), [Part 2](sqldatabase--part-2.md)*

The `SqlDatabase` binding is the in-function handle to a SQL database in the Telnyx Edge Compute runtime. It exposes a synchronous `prepare()` builder and async terminal methods (`first`, `run`, `all`, `raw`, `batch`, `exec`) that route through a single primary per database, so writes from a function are immediately readable from the CLI and the REST query endpoint.

## Errors

Every failure — syntax error, missing table, constraint violation, bad bind — rejects with a plain `Error`. There is no typed error class, no `cause` chain, and no error-code taxonomy equivalent to D1's `D1_ERROR` / `D1_TYPE_ERROR` / `D1_COLUMN_NOTFOUND`.

`error.message` is a long transport string with the SQLite message embedded near the end:

```
actor invocation <org>__telnyx_sqldb/<database-id>.sql returned 500: error invoke actor
method: rpc error: code = Internal desc = ... (500) {"error":"method_failed",
"message":"Error: UNIQUE constraint failed: users.email","name":"Error"}
```

Match on the SQLite text as a substring. Do not parse the envelope — its shape is not part of the contract, and the surrounding transport detail changes.

```ts
try {
  await env.DB
    .prepare("INSERT INTO users(email) VALUES (?)")
    .bind(email)
    .run();
} catch (err) {
  const message = err instanceof Error ? err.message : String(err);
  if (message.includes("UNIQUE constraint failed")) {
    return new Response("email already registered", { status: 409 });
  }
  throw err;
}
```

Long-running statements fail differently: no SQLite message comes back at all. Statements running for tens of seconds complete, but past the caller's own budget — a function invocation tops out around 60 seconds — the call was observed to hang rather than fail with anything identifying the statement. The database stays healthy afterwards. See [Limits](limits.md).

## Related

- [Overview](overview.md) — the SQL Databases Runtime API surface at a glance
- [Quick Start](quick-start.md) — declare the binding and type it
- [How SQL Databases Work](how-sql-databases-work.md) — one primary per database, and where the data lives
- [Migrations](migrations.md) — versioned schema changes from the CLI
- [Limits](limits.md) — statement size, parameter, and duration ceilings
- [Stateful Actor SQL](stateful-actor-sql.md) — the per-actor embedded SQLite at `ctx.storage.sql`, private to one instance and synchronous
