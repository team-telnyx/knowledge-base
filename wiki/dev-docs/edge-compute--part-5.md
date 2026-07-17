---
title: Edge Compute
summary: 'Telnyx Edge Compute is a platform of compute primitives for building and
  deploying applications to the Telnyx edge. The core primitive is a function: an
  ordinary HTTP server packaged as a container, deployed to Telnyx''s global edge
  network, and served at its own public URL. The platform adds bindings (pre-authenticated
  handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable
  per-entity state via Stateful Actors, globally distributed key-value storage via
  KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage.
  Functions are real Linux containers running your language''s own runtime — Node.js,
  Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is
  declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the
  `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and
  rollback automatically.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/filesystems-from-first-principles/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/how-cloudfs-works
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/network-filesystems
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concurrent-access
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/mount/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/quickstart
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
- url: https://developers.telnyx.com/docs/edge-compute/deploy/index
- url: https://developers.telnyx.com/docs/edge-compute/development/index
- url: https://developers.telnyx.com/docs/edge-compute/guides/ai-assistant-backend
- url: https://developers.telnyx.com/docs/edge-compute/kv/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/kv/cli
- url: https://developers.telnyx.com/docs/edge-compute/kv/concepts/how-kv-works/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/api-response-caching
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/feature-flags
- url: https://developers.telnyx.com/docs/edge-compute/kv/examples/session-storage/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/pricing/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/index
- url: https://developers.telnyx.com/docs/edge-compute/kv/reference/kv-namespace
- url: https://developers.telnyx.com/docs/edge-compute/kv/ttl-and-metadata
- url: https://developers.telnyx.com/docs/edge-compute/network/index
- url: https://developers.telnyx.com/docs/edge-compute/observability/index
- url: https://developers.telnyx.com/docs/edge-compute/overview/index
- url: https://developers.telnyx.com/docs/edge-compute/platform-overview/index
- url: https://developers.telnyx.com/docs/edge-compute/platform/limits
- url: https://developers.telnyx.com/docs/edge-compute/platform/pricing
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
- url: https://developers.telnyx.com/docs/edge-compute/reference/cli
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/runtime/http-handler
- url: https://developers.telnyx.com/docs/edge-compute/runtime/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/alarms
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/base
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/configuration
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/context
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/errors
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/namespace
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/storage
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/api-reference/stub
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/addressing
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/how-it-works/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/concepts/lifecycle
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/project-structure/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/when-to-use
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/local-development
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/quick-start/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/shared-actors
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/api-reference
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/handling-calls
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/index
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/quick-start
- url: https://developers.telnyx.com/docs/edge-compute/telnyx-api/receiving-messages
updated_at: 2026-07-17T09:13:17Z
---

# Edge Compute

*Part 5 of 7 — see also: [Part 1](edge-compute--part-1.md), [Part 2](edge-compute--part-2.md), [Part 3](edge-compute--part-3.md), [Part 4](edge-compute--part-4.md), [Part 6](edge-compute--part-6.md), [Part 7](edge-compute--part-7.md)*

Telnyx Edge Compute is a platform of compute primitives for building and deploying applications to the Telnyx edge. The core primitive is a function: an ordinary HTTP server packaged as a container, deployed to Telnyx's global edge network, and served at its own public URL. The platform adds bindings (pre-authenticated handles to the Telnyx API, secrets, KV, object storage, and Stateful Actors), durable per-entity state via Stateful Actors, globally distributed key-value storage via KV, a mountable POSIX filesystem via CloudFS, and S3-compatible object storage. Functions are real Linux containers running your language's own runtime — Node.js, Go, Python, or Java (Quarkus) — with HTTP as the only trigger. Configuration is declarative through `func.toml` or `telnyx.toml` manifests, deployment is via the `telnyx-edge` CLI, and the platform handles scaling, cold starts, revisions, and rollback automatically.

## CloudFS

CloudFS is a POSIX filesystem you mount on any host or container. Once mounted, it behaves like a local directory — `read`, `write`, `mkdir`, `rename`, `git init` — but every byte is stored durably in Telnyx Cloud Storage, and the same filesystem can be mounted by many clients at once.

You mount it with the open-source JuiceFS Community Edition client (Apache-2.0), which you run yourself — Telnyx does not host or bundle it. JuiceFS has no server process: the client does all the filesystem work and talks directly to a metadata database and to object storage, so no JuiceFS component runs on the Telnyx side. Telnyx provides and authenticates the two managed backends — the metadata database and object storage — and hands you a ready-to-mount filesystem.

The target use case is a shared, persistent filesystem for AI agents: provision one CloudFS, mount it once, and every file, repo, and checkpoint an agent produces is there — and still there on the next mount, from anywhere.

### Architecture

CloudFS is built on JuiceFS, which takes the metadata/data split that GFS, HDFS, and MooseFS proved at cluster scale and replaces each half with a managed cloud primitive:

- The **metadata index** becomes a transactional database. The database provides strong consistency for the small, hot, correctness-critical half: an entry is committed or it is not, and every client reads the same tree.
- The **data blocks** become object storage (Telnyx Cloud Storage). JuiceFS splits every file into a chunk → slice → block hierarchy and writes the blocks as ordinary objects.
- There is no CloudFS server in the data path. JuiceFS is a "rich client": all the filesystem logic runs in the process that mounts the volume.

A CloudFS mount talks to two backends over two independent lanes:

|  | Metadata lane | Data lane |
| --- | --- | --- |
| What it stores | Directory tree, filenames, inodes, chunk/slice index | File contents, split into 4 MiB block objects |
| Backend | Per-filesystem metadata database | Per-filesystem bucket on Telnyx Cloud Storage |
| Endpoint | `us-east-1.telnyxcloudfs.com:5432` (TLS) | `https://<region>.telnyxcloudstorage.com` |
| Location | Always us-east-1 | The data region you chose at create time |
| Credential | `meta_token` | Your `TELNYX_API_KEY` as the S3 access-key |

Metadata is centralized in us-east-1 for every filesystem, no matter which data region you pick. A client mounting from another region pays a network round-trip on every metadata operation, so metadata-heavy work is slower the farther you mount from us-east-1. Data throughput is unaffected.

### Mounting

A CloudFS filesystem is mounted with the JuiceFS Community Edition client. The client talks to two backends directly: the metadata database (over a managed endpoint) and Telnyx Cloud Storage (over S3).

```
export TELNYX_API_KEY="KEY..."
export META_URL="postgres://fs_<hex>:cloudfs_tok_...@us-east-1.telnyxcloudfs.com:5432/fs_<hex>?sslmode=require"
export AWS_ACCESS_KEY_ID="$TELNYX_API_KEY"
export AWS_SECRET_ACCESS_KEY="placeholder"

mkdir -p /mnt/agentfs
juicefs mount --no-usage-report --background --log /tmp/juicefs.log "$META_URL" /mnt/agentfs
```

The S3 access key is your API key. The secret key's signature is ignored by Telnyx Storage — but it must be non-empty. CloudFS volumes are formatted without embedded object-storage credentials, so JuiceFS picks them up from `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` at mount time.

Do not run `juicefs format` against a filesystem whose status is `ready` — provisioning already formats the volume. The one exception is a filesystem in `needs_format`.

### Concurrent Access

CloudFS is a shared filesystem: the same filesystem can be mounted by many clients at once. Every client mounts with the same `meta_url` (token included) and the same `TELNYX_API_KEY`. There is nothing per-client to set up.

CloudFS gives close-to-open consistency: when a client writes a file and closes it, other clients see the new contents the next time they open it. Directory operations commit to the metadata store immediately and become visible to other clients within about a second.

Two clients writing the same file (or the same byte range) at the same time is the one case that needs coordination — uncoordinated overlapping writes resolve last-writer-wins. Use file locks: CloudFS supports both BSD locks (`flock`) and POSIX record locks (`fcntl`), and JuiceFS coordinates them across clients through the shared metadata.

### Important Warning

Do not touch the `cloudfs-fs-*` bucket directly. A CloudFS filesystem's data lives in a bucket named `cloudfs-fs-<hex>` inside your own Telnyx Cloud Storage account. Its objects are opaque JuiceFS blocks, not your files. Deleting, renaming, or editing objects in that bucket out of band corrupts the filesystem — a missing block is unrecoverable and there is no repair path. Manage a CloudFS filesystem only through the CloudFS API and a JuiceFS mount.

CloudFS is in beta. The API surface and behavior may still change as it moves toward general availability.

## Telnyx API Binding

The Telnyx API binding puts a ready-to-use, authenticated Telnyx client on `env`. You never handle an API key — the binding injects credentials at the edge and keeps them out of your code, bundle, and logs.

```
import { env } from "@telnyx/edge-runtime";

await env.MY_TELNYX.messages.send({
  from: "+13125550100",
  to: "+13125550101",
  text: "Hello from Edge Compute",
});
```

`MY_TELNYX` is whatever you set as `binding` in `func.toml`. It becomes the property on `env`. `telnyx-edge types` types `env.MY_TELNYX` as the Telnyx client. One binding per organization — every function in the org shares it.

Calls take the shape `env.MY_TELNYX.<resource>.<method>(...)`, using resource and method names — not raw HTTP paths. Each method returns the API response; list and retrieve calls expose the payload on `.data`. Calls reject on API errors — catch and inspect `err.status`, `err.message`, and `err.error`.
