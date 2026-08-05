---
title: CLI Reference
summary: Reference for the `telnyx-edge` command-line tool (v0.2.5) used to scaffold,
  deploy, and manage Telnyx Edge Compute functions and their bound resources. Covers
  installation, global flags, authentication, project scaffolding, deployment, revisions,
  rollback, secrets, bindings, type generation, storage, stateful actors, and function
  lifecycle commands.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
updated_at: 2026-08-05T13:41:31Z
---

# CLI Reference

*Part 2 of 2 — see also: [Part 1](cli-reference--part-1.md)*

Reference for the `telnyx-edge` command-line tool (v0.2.5) used to scaffold, deploy, and manage Telnyx Edge Compute functions and their bound resources. Covers installation, global flags, authentication, project scaffolding, deployment, revisions, rollback, secrets, bindings, type generation, storage, stateful actors, and function lifecycle commands.

## secrets

Secrets are organization-scoped key-value pairs for sensitive data. The arguments are positional — there are no `--name`/`--value` flags:

```
telnyx-edge secrets add STRIPE_API_KEY "sk_live_abc123"
# → Secret 'STRIPE_API_KEY' added successfully

telnyx-edge secrets list      # keys only — values are never shown
telnyx-edge secrets delete OLD_API_KEY
```

`add` on an existing key overwrites it. Values are injected at deploy time, so `ship` each function that uses a changed secret.

Functions read secrets two ways, and both are always true: every secret is injected as a plain environment variable into **all** functions in your organization, and TypeScript functions can additionally declare a `[secrets](secrets.md)` binding and read through the typed `env.SECRETS.get()`. See [Secrets](secrets.md) for both surfaces.

## bindings

Manages the **org-level Telnyx credential** (one per organization) behind the [Telnyx API binding](telnyx-api-binding--part-1.md). The per-function flow needs none of these commands — declaring `[telnyx]` in `func.toml` wires the binding automatically on `ship`.

```
telnyx-edge bindings create     # provision the org credential (one per organization)
telnyx-edge bindings get        # binding metadata
telnyx-edge bindings validate   # check the credential works
telnyx-edge bindings update     # regenerate — use if you suspect compromise
telnyx-edge bindings delete     # remove; functions lose automatic Telnyx API access
```

## types

```
telnyx-edge types                  # writes telnyx-env.d.ts at the project root
telnyx-edge types -f ./my-func     # or point at another project directory
```

Generates TypeScript types for the `env` surface from your manifest (`func.toml` or `telnyx.toml`), folding every declared binding into one global `Env` interface:

| Declaration | Generated type |
| --- | --- |
| `[telnyx]` | `env.<BINDING>` is the Telnyx client class from the `telnyx` npm package — `env.<BINDING>.balance.retrieve()` type-checks |
| `[secrets](secrets.md)` | `env.SECRETS.get()` accepts the literal union of declared handles → `Promise<string>`; a typo'd handle fails to compile |
| `[storage.kv.<NAME>]` | `env.<NAME>` is `KvNamespace` from `@telnyx/edge-runtime` — new in v0.2.3 |
| `[storage.cloudstorage.<NAME>]` | `env.<NAME>` is `CloudStorageBucket` from `@telnyx/edge-runtime` — new in v0.2.4 |
| `[storage.sqldb.<NAME>]` | `env.<NAME>` is `SqlDatabase` from `@telnyx/edge-runtime` — requires the SDK at 0.9.0 or newer |
| `[actors](actors.md)` | `env.<BINDING>` exposes the bound actor class's public method signatures (umbrella `telnyx.toml` projects only) |

Declarations only — no JavaScript, no runtime glue, no source edits. Re-run after changing any binding declaration.

`types` generates a `.d.ts` consumed by `tsc` — it has no effect on `js`, `go`, `python`, or `quarkus` runtimes. Bindings on those runtimes are reached over REST instead; see [Bindings](bindings.md).

## storage

```
telnyx-edge storage kv create --name my-cache
telnyx-edge storage kv key put <namespace-id> user/123 "hello" --ttl 30s
telnyx-edge storage sqldb create --name links-db
telnyx-edge storage sqldb execute links-db --remote --command "SELECT 1"
```

Manages KV storage namespaces and keys: `storage kv` covers namespace create/list/get/delete, and `storage kv key` covers put/get/list/delete including server-side TTL and prefix listing. Full flags and examples live in the [KV CLI reference](kv-cli-reference.md).

`storage sqldb` manages SQL databases: create/list/get/delete, plus `execute` for running SQL against a database out-of-band and `migrations` for versioned schema files. It arrives in a later release than the v0.2.5 covered above — see the [SQL Databases CLI reference](sql-databases-cli-reference.md) for the version floor, full flags, and examples.

## actors

```
telnyx-edge actors list               # the account's registered actor types
telnyx-edge actors inspect Account    # one type, its attached functions, + live instance count
telnyx-edge actors instances Account  # list persisted instances (type/id pairs)
telnyx-edge actors delete Account     # delete an account-scoped type
```

Inspects and manages the [Stateful Actor](stateful-actor.md) types registered to your account (account-scoped, keyed by type). `inspect` reports the actor type's live instance count; `instances` lists the persisted instances (type/id pairs, e.g. `Counter/alice`). Output renders backend state — never inferred from local files.

## reset-func

```
telnyx-edge reset-func broken-func
```

Tears down a failed function's deployed resources and returns it to the `created` state — preserving its id, name, and config — so you can fix the code and `ship` again. Allowed only from a terminal failure state (`build_failed`, `deploy_failed`, `delete_failed`); a healthy function can't be reset (use `delete-func`), and an in-progress operation must finish first.

## delete-func

```
telnyx-edge delete-func my-old-func
```

Deletes a function by name. This cannot be undone — the function, its revisions, and its URL are gone.

## Related

- [Configuration](configuration--part-1.md) — every `func.toml` / `telnyx.toml` key the CLI reads
- [CI/CD](ci-cd.md) — install, authenticate, and ship from a pipeline
- [Versions & Rollback](versions-rollback.md) — how revisions and rollback behave
- [KV CLI](kv-cli.md) — the full `storage kv` surface
- [SQL Databases CLI](sql-databases-cli.md) — the full `storage sqldb` surface, including `execute` and `migrations`
- [Stateful Actors](stateful-actors--part-1.md) — the projects behind `--actor` and the `actors` command
