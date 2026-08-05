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

*Part 4 of 6 — see also: [Part 1](sql-databases--part-1.md), [Part 2](sql-databases--part-2.md), [Part 3](sql-databases--part-3.md), [Part 5](sql-databases--part-5.md), [Part 6](sql-databases--part-6.md)*

SQL Databases are standalone SQLite databases on Telnyx Edge Compute that live outside any function and are reached through a single primary. They can be queried from inside a TypeScript function via the `env` binding, or from anywhere via the REST API and the `telnyx-edge storage sqldb` CLI, with the same data visible through both paths.

## CLI

Manage SQL databases using the `telnyx-edge` CLI. Every command in this family reaches a database through the same primary as the `env` binding, so the CLI is not a second writer — SQL run from a terminal and SQL run from a deployed function are serialized together.

The `storage sqldb` family requires **CLI v0.3.0 or newer** — the first release to carry any SQL surface. On v0.2.5 and earlier `telnyx-edge storage sqldb` fails as an unknown command. Check with `telnyx-edge --version`.

### Database Management

```
# List databases
telnyx-edge storage sqldb list

# Create a database (name: lowercase letters, numbers, hyphens)
telnyx-edge storage sqldb create --name links-db

# Get one database by id
telnyx-edge storage sqldb get <database-id>

# Delete a database by id — no confirmation prompt
telnyx-edge storage sqldb delete <database-id>
```

`create` returns immediately with `status: pending`; provisioning finishes in the background, typically in 2 to 11 seconds. Poll `get` until the status is `provision_ok`.

`list` paginates, newest first. `delete` takes effect immediately and asks nothing first — there is no confirmation prompt and no `--yes` flag. The record disappears shortly afterwards: `get` and any query against that id return `404`. Delete removes the database record and makes the data unreachable through every path; it is not a guaranteed erase of the stored bytes, so it does not satisfy a data-destruction requirement on its own. It also does not touch functions that still declare the id in a `[storage.sqldb.<NAME>]` block: those functions stay deployed and their queries start failing. Remove the block and redeploy them.

#### `list` Flags

| Flag | Description |
| --- | --- |
| `--page` | Page number, 1-based (default `1`) |
| `--page-size` | Items per page, `1`–`250` (default `20`) |

`get` and `delete` take the database **id** only. `execute` and the `migrations` subcommands accept either the id or the database name.

### Running SQL

`execute` runs SQL against a database without deploying anything — to create a schema, load seed data, or inspect what a function wrote.

```
# One statement, inline
telnyx-edge storage sqldb execute links-db --remote \
  --command "CREATE TABLE links (id INTEGER PRIMARY KEY, slug TEXT UNIQUE, url TEXT NOT NULL)"

# A whole file — submitted as one multi-statement script
telnyx-edge storage sqldb execute links-db --remote --file ./schema.sql

# Read rows back
telnyx-edge storage sqldb execute links-db --remote \
  --command "SELECT id, slug, url FROM links ORDER BY id"
```

A statement that returns no rows prints a confirmation; a read prints a table and a row count. Columns are ordered alphabetically rather than by their order in the `SELECT` list, and a SQL `NULL` renders as `NULL`. To learn a new row's id, or to count the rows a write touched, add `RETURNING` to the statement and count the rows it prints. `SELECT changes()` in a separate call reads a counter on a connection shared with every other caller of the database, so another write can land in between.

`--json` prints the raw result object instead of a table — on **stderr** in the current CLI, so scripts should capture it with `2>&1 >/dev/null` rather than piping stdout. `results` holds the rows and is the only field the service returns — a statement that produces no rows prints `{}`.

`BLOB` columns cross this boundary as a JSON array of byte values — a three-byte blob comes back as `[9, 8, 7]`, not base64 and not an object. Decode it as bytes on the client. Writing binary this way means a SQL hex literal (`X'090807'`), since this path has no parameter binding; from a function, bind an `ArrayBuffer` instead.

#### `execute` Flags

| Flag | Description |
| --- | --- |
| `--command`, `-c` | SQL to run inline. Mutually exclusive with `--file`; exactly one of the two is required |
| `--file`, `-f` | Path to a `.sql` file, submitted verbatim as a single multi-statement script |
| `--remote` | **Required.** Runs against the remote database — local execution is not supported |
| `--json` | Print the raw result object instead of a table |

`--remote` is mandatory. Omitting it fails with `--remote is required` before any network call: there is no local SQLite emulation to run against, and no `--local` flag.

The SQL text is submitted verbatim — the CLI never splits statements itself. A script may hold several `;`-separated statements; all of them run in order, and the rows returned are the **last** statement's rows. The whole script must fit under the ~4 MiB script ceiling (see [Limits](limits.md)). A database that has not finished provisioning rejects `execute` with `409` — `Database is not ready (status: pending)`. Wait for `provision_ok`.

### Addressing a Database

`execute`, `migrations list`, and `migrations apply` take a `<database>` argument that resolves either way:

- An exact **id** match always wins.
- A **name** resolves when exactly one database in the organization carries it.
- A name shared by several databases errors with `Multiple SQL databases are named "..."` — pass the id instead.
- No match errors with `No SQL database found matching "..."`.

Names are unique within an organization, so an ambiguous match should not occur in practice — the CLI guards against it anyway. `get` and `delete` do not resolve names; they take the id.
