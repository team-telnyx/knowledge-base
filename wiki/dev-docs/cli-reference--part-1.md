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

*Part 1 of 2 — see also: [Part 2](cli-reference--part-2.md)*

Reference for the `telnyx-edge` command-line tool (v0.2.5) used to scaffold, deploy, and manage Telnyx Edge Compute functions and their bound resources. Covers installation, global flags, authentication, project scaffolding, deployment, revisions, rollback, secrets, bindings, type generation, storage, stateful actors, and function lifecycle commands.

## Overview

`telnyx-edge` is the command-line tool for Edge Compute: it scaffolds function projects, deploys them, and manages the resources they bind. This page covers every command in v0.2.5.

| Command | What it does |
| --- | --- |
| [auth](auth.md) | Log in via OAuth or API key; check or clear credentials |
| [new-func](new-func.md) | Scaffold a project and register the function server-side |
| [ship](ship.md) | Upload, build, and deploy a function |
| [list](list.md) | List your functions with status and invoke URL |
| [inspect](inspect.md) | One function's full details and actor bindings |
| [status](status.md) | CLI self-diagnostics: config, auth, connectivity |
| [revisions](revisions.md) | A function's deploy history |
| [rollback](rollback.md) | Retarget traffic to a previous revision |
| [secrets](secrets.md) | Manage organization-scoped secrets |
| [bindings](bindings.md) | Manage the org-level Telnyx API credential |
| [types](types.md) | Generate `telnyx-env.d.ts` from the project manifest |
| [storage](storage.md) | Manage KV namespaces and keys, and SQL databases |
| [actors](actors.md) | Manage account-scoped Stateful Actor types |
| [reset-func](reset-func.md) | Return a failed function to the `created` state |
| [delete-func](delete-func.md) | Delete a function permanently |

## Installation

The CLI ships as GitHub release binaries only — it is not on npm and there is no Homebrew formula. Assets are version-stamped; there is no un-versioned "latest" asset (`releases/latest/download/...` URLs return 404).

| Platform | Asset |
| --- | --- |
| Linux amd64 | `telnyx-edge-v0.2.5-linux-amd64.tar.gz` |
| Linux arm64 | `telnyx-edge-v0.2.5-linux-arm64.tar.gz` |
| macOS arm64 (Apple silicon) | `telnyx-edge-v0.2.5-macos-arm64.tar.gz` |
| macOS amd64 (Intel) | `telnyx-edge-v0.2.5-macos-amd64.tar.gz` |
| Windows | `.zip` archives on the same [release page](https://github.com/team-telnyx/edge-compute/releases) |

Each tarball extracts into a versioned directory containing the `telnyx-edge` binary:

```
VERSION=v0.2.5

curl -fsSL "https://github.com/team-telnyx/edge-compute/releases/download/${VERSION}/telnyx-edge-${VERSION}-linux-amd64.tar.gz" | tar xz
sudo mv "telnyx-edge-${VERSION}-linux-amd64/telnyx-edge" /usr/local/bin/

telnyx-edge --version   # prints the installed version
```

For macOS, substitute `macos-arm64` (Apple silicon) or `macos-amd64` (Intel) in both lines. To update, download the new version's asset and replace the binary the same way.

## Global flags and configuration

| Flag | Effect |
| --- | --- |
| `-h`, `--help` | Help for any command: `telnyx-edge <command> --help` |
| `-v`, `--verbose` | Verbose logging — the first thing to try on an obscure failure |
| `--version` | Print the CLI version (root command only) |

Credentials persist in `~/.telnyx-edge/config.toml`. Two environment variables affect the binary itself: `TELNYX_CONFIG_PATH` relocates the config file, and `TELNYX_NO_UPDATE_CHECK` disables the release update check.

## auth

```
telnyx-edge auth login                       # OAuth 2.0 in the browser
telnyx-edge auth api-key set "KEY..."        # persist a Telnyx API key instead
telnyx-edge auth status                      # who am I, and does the token work
telnyx-edge auth logout                      # clear stored tokens
```

`login` opens a browser for OAuth; `api-key set` writes the key to `~/.telnyx-edge/config.toml`. Both end in the same place — subsequent commands read the stored credential.

The CLI does not read a `TELNYX_API_KEY` environment variable. In CI, run `telnyx-edge auth api-key set "$TELNYX_API_KEY"` as a pipeline step — see [CI/CD](ci-cd.md).

## new-func

```
telnyx-edge new-func -l ts -n my-func
cd my-func
```

| Flag | Description |
| --- | --- |
| `-l`, `--language` | Runtime — exactly one of `go`, `js`, `ts`, `python`, `quarkus`. **Required** unless `--from-dir` is given; the value is exact (`javascript` is rejected). |
| `-n`, `--name` | Function name. Becomes the directory name and part of the URL. |
| `--actor` | Scaffold a Stateful Actor (`telnyx.toml`) project — TypeScript only. See the [Stateful Actors quick start](stateful-actors-quick-start.md). |
| `--from-dir` | Copy files from an existing directory instead of a language scaffold. |

`new-func` does two things: it creates a project directory (the command fails if one with that name already exists), and it **registers the function server-side** — so it requires authentication, and the generated `func.toml` already contains the function's UUID `func_id`. Rapid successive calls can hit HTTP 429 rate limits.

What each scaffold contains:

| Language | Files |
| --- | --- |
| `ts` | `func.toml`, `index.ts`, `package.json`, `tsconfig.json` |
| `js` | `func.toml`, `index.js`, `package.json` |
| `go` | `func.toml`, `handler.go`, `go.mod` |
| `python` | `func.toml`, `function/func.py`, `pyproject.toml` |
| `quarkus` | `func.toml`, `pom.xml`, `mvnw`, `.mvn/`, `src/main/java/functions/` |

The entrypoint contract differs per language — see [HTTP handler](http-handler.md).

## ship

```
telnyx-edge ship                       # deploy the function in the current directory
telnyx-edge ship --from-dir ../other   # or any relative, absolute, or ~/ path
```

| Flag | Description |
| --- | --- |
| `-f`, `--from-dir` | Path to the function directory (default: current directory) |
| `-t`, `--timeout` | Deployment monitoring timeout as a Go duration (`2m`, `300s`; default `5m0s`) |

`ship` uploads, builds, pushes, and deploys the function named by the directory's `func.toml`. There is no environment flag — staging and production are [separate functions](separate-functions.md). Umbrella projects (`telnyx.toml`) are bundled client-side before upload: the module graph rooted at `main` is compiled into a single file with esbuild (TypeScript/JavaScript only), and the manifest is included so the platform can deploy any `[actors](actors.md)` it declares.

On success, `ship` prints the live URL — stable across deploys:

```
📡 Your function is live at:
   https://my-func-0198c2c5-8.telnyxcompute.com
```

The scheme is `{func-name}-{func-id-prefix}.telnyxcompute.com` — see [Routes & Domains](routes-domains.md). Each successful ship also produces an immutable revision ([revisions](revisions.md), [rollback](rollback.md)).

## list

```
telnyx-edge list
telnyx-edge list --page 2 --page-size 50
```

Lists your functions — id, name, status, creation time, and invoke URL. Paginated: `--page` (default 1) and `--page-size` (default 25).

## inspect

```
telnyx-edge inspect my-func   # accepts a name or an id (first column of 'list')
```

Shows one function's status, invoke URL, and timestamps, plus the actor types it binds — each binding's type, status, and owner/reference role.

## status

```
telnyx-edge status
```

Self-diagnostics: config file existence, authentication status, and connectivity to `https://api.telnyx.com`. Run it first when any other command misbehaves.

## revisions

```
telnyx-edge revisions list my-func
```

Lists the most recent revisions for a function, newest first, with each revision's id, ship time, author, and deploy status; the revision currently serving traffic is marked. Every successful `ship` produces an immutable revision — see [Versions & Rollback](versions-rollback.md).

## rollback

```
telnyx-edge rollback my-func a1b2c3d
# → Rollback of 'my-func' to revision a1b2c3d accepted; traffic is switching across clusters.
```

Instantly retargets traffic to an existing, immutable revision across all clusters — no rebuild, no re-upload. Only revisions that reached `deploy_ok` can be rolled back to; get ids from `revisions list`. Your source tree is untouched — the next `ship` deploys whatever is on disk, as a new revision.
