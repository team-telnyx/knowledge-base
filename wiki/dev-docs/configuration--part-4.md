---
title: Configuration
summary: Every Telnyx Edge Compute project is configured by a single TOML manifest
  at its root — `func.toml` for classic single-function projects or `telnyx.toml`
  for umbrella TypeScript projects. The manifest declares the function's identity,
  environment variables, secret bindings, storage bindings, and (for umbrella projects)
  actors; configuration changes take effect on the next `telnyx-edge ship`.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
updated_at: 2026-08-05T13:40:37Z
---

# Configuration

*Part 4 of 4 — see also: [Part 1](configuration--part-1.md), [Part 2](configuration--part-2.md), [Part 3](configuration--part-3.md)*

Every Telnyx Edge Compute project is configured by a single TOML manifest at its root — `func.toml` for classic single-function projects or `telnyx.toml` for umbrella TypeScript projects. The manifest declares the function's identity, environment variables, secret bindings, storage bindings, and (for umbrella projects) actors; configuration changes take effect on the next `telnyx-edge ship`.

## Versions & Rollback

Every successful `telnyx-edge ship` produces an immutable revision. `telnyx-edge revisions list` shows a function's deploy history; `telnyx-edge rollback` retargets traffic to a previous revision without rebuilding or re-uploading anything.

### Listing revisions

```bash
telnyx-edge revisions list my-func
```

Prints the most recent revisions, newest first: the revision ID, when it was shipped, who shipped it, and its deploy status. The revision currently serving traffic is marked with `*`.

Revision IDs are short identifiers like `a1b2c3d` — you pass one to `rollback`.

### Rolling back

```bash
telnyx-edge rollback my-func a1b2c3d
# → Rollback of 'my-func' to revision a1b2c3d accepted; traffic is switching across clusters.
#   Run 'telnyx-edge revisions list my-func' to confirm the active revision.
```

Traffic is instantly retargeted to the existing, immutable revision across all clusters — there is no rebuild and no re-upload. Two constraints:

- **The target must have reached `deploy_ok`.** A revision whose build or deploy failed never served traffic and can't be rolled back to; `revisions list` shows each revision's deploy status.
- **Rollback doesn't touch your source.** Your working tree and git history are unchanged. The next `ship` deploys whatever is on disk — as a new revision — regardless of which revision is currently active.

### Rolling forward

To move forward again, either `ship` — every successful ship creates a new revision and moves traffic to it — or `rollback` to any other revision that reached `deploy_ok`.

### Recovering a failed function

Rollback assumes the function has a healthy revision to return to. A function stuck in a terminal failure state (`build_failed`, `deploy_failed`, `delete_failed`) can instead be reset:

```bash
telnyx-edge reset-func broken-func
```

This tears down the function's deployed resources and returns it to the `created` state — preserving its ID, name, and config — so you can fix the code and `ship` again. A healthy function (`build_ok`/`deploy_ok`) can't be reset; use `delete-func` if you want it gone.

## Configured outside the manifest

The manifest references resources that exist outside it by name or ID — you create each one separately, and the block only points at it:

- **Secret values** — stored server-side with `telnyx-edge secrets`; `[secrets](secrets.md)` and the injected environment variables only reference the key. See [Secrets](secrets.md).
- **KV namespaces** — created with `telnyx-edge storage kv create`; `[storage.kv.<NAME>]` only references the namespace `id`. See the [KV quick start](kv-quick-start.md).
- **Cloud Storage buckets** — created in the [Mission Control portal](https://portal.telnyx.com/#/storage/buckets) or over the [S3-compatible API](/docs/cloud-storage/quick-start); `[storage.cloudstorage.<NAME>]` only references an existing bucket by `bucket_name`. See [Cloud Storage binding](cloud-storage-binding.md).
- **SQL databases** — created with `telnyx-edge storage sqldb create`; `[storage.sqldb.<NAME>]` only references the database `id`. See the [SQL Databases quick start](sql-databases-quick-start.md).

## Ship-time validation

Binding handles and `[env_vars]` names share one `env` namespace. `ship` (and `types`) enforce two hard rules and warn on a third:

- **Duplicate `[secrets](secrets.md)` handles are rejected** — `ship` fails, because `env.SECRETS.get("<handle>")` would be ambiguous.
- **A binding (or actor) named `SECRETS` is rejected** when a `[secrets](secrets.md)` block is declared — it conflicts with the `env.SECRETS` namespace.
- **A name collision between `[env_vars]` and a binding — including an `[env_vars]` entry named `SECRETS` — only warns.** Both land on `env`, so one shadows the other and `ship` proceeds; rename one.

## Related

- [Bindings](bindings.md) — every binding at a glance: declaration and `env` surface for Telnyx API, Secrets, KV, Object storage, SQL databases, and Actors
- [Environment Variables](environment-variables.md) — everything that lands in the container's environment
- [Secrets](secrets.md) — both access surfaces for `[secrets](secrets.md)`
- [Telnyx API binding](telnyx-api-binding--part-1.md) — the `[telnyx]` block and the `env.<binding>` client
- [KV quick start](kv-quick-start.md) — the `[storage.kv.<NAME>]` block and `KvNamespace`
- [Cloud Storage binding](cloud-storage-binding.md) — the `[storage.cloudstorage.<NAME>]` block and `CloudStorageBucket`
- [SQL Databases](sql-databases--part-1.md) — the `[storage.sqldb.<NAME>]` block and `SqlDatabase`
- [Stateful Actors configuration](stateful-actors-configuration.md) — the `[actors](actors.md)` block in full
- [CLI reference](cli-reference--part-1.md) — `new-func` writes the manifest; `ship` and `types` read it
