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

*Part 3 of 6 — see also: [Part 1](sql-databases--part-1.md), [Part 2](sql-databases--part-2.md), [Part 4](sql-databases--part-4.md), [Part 5](sql-databases--part-5.md), [Part 6](sql-databases--part-6.md)*

SQL Databases are standalone SQLite databases on Telnyx Edge Compute that live outside any function and are reached through a single primary. They can be queried from inside a TypeScript function via the `env` binding, or from anywhere via the REST API and the `telnyx-edge storage sqldb` CLI, with the same data visible through both paths.

## Quick Start

### Prerequisites

- The `telnyx-edge` [CLI Reference](cli-reference--part-1.md), authenticated (`telnyx-edge auth api-key set <YOUR_API_KEY>`), on a release that includes `storage sqldb`.
- A Telnyx API key, if calling the REST API directly.
- An Edge Compute function project with a `telnyx.toml` (or `func.toml`) manifest, and Node.js for `npm`.

### Create a Database

A database is an isolated SQLite database with its own schema. Create one with the CLI or the API.

```
telnyx-edge storage sqldb create --name my-app-db
```

```
curl -X POST https://api.telnyx.com/v2/storage/sqldbs \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "my-app-db"}'
```

The response carries the database `id` — a UUID, and the only durable handle. Names are not resolution keys:

```
{
  "data": {
    "record_type": "storage_sqldb",
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "my-app-db",
    "status": "pending",
    "created_at": "2026-07-29T14:52:03Z",
    "updated_at": "2026-07-29T14:52:03Z"
  }
}
```

A name may contain lowercase letters, numbers, and hyphens, and must be unique within the organization — a duplicate returns `409`, and the API rejects an empty or upper-case name with `422` (the CLI stops an empty name before any request is made). Hyphen placement is not constrained — a leading hyphen is accepted — but avoid one: that name then reads as a flag when passed to CLI commands, so you are left addressing the database by id. Keep names short: past 255 characters the create fails with a `500` instead of a validation error.

A new database starts at `status: "pending"`. SQL sent to it from outside a function — `execute`, `migrations`, or the REST query endpoint — returns `409` (`"Database is not ready (status: pending)"`) until provisioning finishes, typically in 2 to 11 seconds. If scripting, poll until the status is `provision_ok` rather than sleeping a fixed interval:

```
telnyx-edge storage sqldb get 550e8400-e29b-41d4-a716-446655440000
```

### Create the Schema

Create your tables from the terminal, before any code exists. `execute` takes exactly one of `--command` or `--file`, and `--remote` is required — there is no local emulation.

```
telnyx-edge storage sqldb execute 550e8400-e29b-41d4-a716-446655440000 --remote \
  --command "CREATE TABLE links (
    id INTEGER PRIMARY KEY,
    slug TEXT NOT NULL UNIQUE,
    target TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
  )"
# ✓ Statement executed — no rows returned
```

Longer schemas belong in a file. The file is submitted as one multi-statement script — the engine splits it, the CLI does not:

```
telnyx-edge storage sqldb execute 550e8400-e29b-41d4-a716-446655440000 --remote --file schema.sql
```

Add `--json` to get the raw result object instead of the rendered table. For scripting note one wrinkle: the current CLI writes the JSON to **stderr**, so capture it with `2>&1 >/dev/null` rather than piping stdout.

`execute` is for one-off statements and inspection. For schema changes intended to be kept and replayed on another database, use [Migrations](migrations.md) — numbered `.sql` files with a tracking table inside the database itself.

### Bind the Database to a Function

Declare the database in the function's manifest. The only part this step adds is the `[storage.sqldb.DB]` block:

```
name = "links-api"
main = "src/index.ts"
compatibility_date = "2026-05-14"

[storage.sqldb.DB]
id = "550e8400-e29b-41d4-a716-446655440000"  # Database ID from step 1

[edge_compute]
func_id = "<written by new-func — do not edit>"
func_name = "links-api"
```

The block key — `DB` here — is a name of your choosing, and it is what the code sees on `env`: this manifest produces `env.DB`. It must be a valid identifier (letters, digits, underscores; no leading digit, no `__`) and unique across every binding in the manifest. `id` must be the database UUID. Binding by name, or creating a database from the manifest, is rejected before deploy. Declare as many `[storage.sqldb.<NAME>]` blocks as needed; two bindings that carry different ids are two different databases, and neither can see the other's tables.

### Generate Types

```
npm install @telnyx/edge-runtime   # 0.9.0 or newer — the first release exporting SqlDatabase
telnyx-edge types                  # writes telnyx-env.d.ts
# env.DB → SqlDatabase
```

`telnyx-edge types` reads the manifest — plus the `@telnyx/edge-runtime` version declared in `package.json` — and nothing else: it runs offline and needs no authentication. Re-run it after adding, renaming, or removing a binding. Types are for the compiler only. The binding itself resolves at runtime from the manifest, so a stale `telnyx-env.d.ts` does not change what the deployed function sees — in either direction.

### Write the Function

Bindings live on the `env` **imported** from `@telnyx/edge-runtime` — **not** on the second argument to `fetch(req, env)`. Reading `env.DB` off that argument type-checks cleanly and is `undefined` at runtime.

```
import { env } from "@telnyx/edge-runtime";

type Link = { id: number; slug: string; target: string };

export default {
  async fetch(req: Request): Promise<Response> {
    if (req.method === "POST") {
      const { slug, target } = (await req.json()) as { slug: string; target: string };

      // RETURNING hands back the generated id
      const inserted = await env.DB.prepare(
        `INSERT INTO links (slug, target) VALUES (?, ?) RETURNING id`,
      )
        .bind(slug, target)
        .run<{ id: number }>();

      return Response.json({ id: inserted.results[0]!.id }, { status: 201 });
    }

    const slug = new URL(req.url).searchParams.get("slug");

    const { results } = slug
      ? await env.DB.prepare(`SELECT id, slug, target FROM links WHERE slug = ?`)
          .bind(slug)
          .all<Link>()
      : await env.DB.prepare(
          `SELECT id, slug, target FROM links ORDER BY id DESC LIMIT 20`,
        ).all<Link>();

    return Response.json({ links: results });
  },
};
```

`prepare()` is synchronous and returns a statement. `.bind()` returns a *new* statement with the values attached — it never mutates the one it was called on. The terminal calls are async, and each resolves to a different shape: `run()` and `all()` give `{ results, success, meta }`, `first()` gives a single row or `null` (`first("col")` gives that column's value), and `raw()` gives an array of value-arrays. `run()` and `all()` are the same call: both return rows, including the rows a `RETURNING` clause produces.

Bind every value that comes from a request with `?` placeholders rather than building SQL by concatenation. Ordered `?NNN` placeholders work too. A failing statement — a syntax error, a `UNIQUE` violation, a missing table — rejects with a plain `Error`. There is no typed error class or error-code taxonomy: the SQLite message is nested inside a longer transport string on `error.message`.

### Ship and Call It

```
telnyx-edge ship
```

`ship` bundles the project, uploads it, and prints the function host — `{func-name}-{func-id-prefix}.telnyxcompute.com`, without a scheme; add `https://` when calling it.

```
B=https://links-api-<func-id-prefix>.telnyxcompute.com

curl -sS -X POST $B -H 'content-type: application/json' \
  -d '{"slug":"docs","target":"https://developers.telnyx.com"}'
# → {"id":1}

curl -sS $B
# → {"links":[{"id":1,"slug":"docs","target":"https://developers.telnyx.com"}]}

curl -sS "$B?slug=docs"
# → {"links":[{"id":1,"slug":"docs","target":"https://developers.telnyx.com"}]}
```

### Query It Without Deploying

The rows the function wrote are readable from the terminal against the same database:

```
telnyx-edge storage sqldb execute 550e8400-e29b-41d4-a716-446655440000 --remote \
  --command "SELECT id, slug, target FROM links ORDER BY id DESC LIMIT 5"
```

The CLI renders the rows as a table followed by a row count. This is the same database the function holds on `env.DB`, reached through the same primary — the CLI is not a second writer, and no schema or data is duplicated. Use it to inspect state, apply a fix-up statement, or seed a table without redeploying.

### Query It From Any Language

The CLI is a wrapper over one HTTP endpoint. Anything that can make a request can reach the same database — a Go or Python function, a backfill script, a CI job:

```
curl -sS -X POST \
  https://api.telnyx.com/v2/storage/sqldbs/550e8400-e29b-41d4-a716-446655440000/actions/query \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sql": "SELECT id, slug FROM links ORDER BY id DESC LIMIT 5"}'
```

```
{ "data": { "results": [ { "id": 2, "slug": "home" }, { "id": 1, "slug": "docs" } ] } }
```

The body takes exactly one key, `sql`. Any other key — including `params` — is rejected with `400 Invalid request body`. The response carries `results` and nothing else: no `meta`, no row counts, no duration. A script may hold several `;`-separated statements, and the rows returned are the last statement's.

**This endpoint has no parameter binding.** There is no way to send values separately from the statement, so any value that varies has to be written into the SQL text itself. Never interpolate a string that came from a request, a user, or any other untrusted source into a statement sent this way — that is a SQL injection, and the endpoint gives you nothing to defend with. Use this path for schema, migrations, backfills, and inspection, where the SQL is written by you and fixed in advance. For request-path queries whose values come from callers, use a TypeScript function and the `env` binding, where `prepare().bind()` keeps the statement and the data separate.

Binary columns come back as JSON arrays of byte values (`[9, 8, 7]`), not base64. Errors arrive in the standard Telnyx envelope: a SQL failure is a `422` whose detail embeds the SQLite message inside the same longer transport string, a database that has not finished provisioning is a `409`, and an unknown or other-organization id is a `404`.
