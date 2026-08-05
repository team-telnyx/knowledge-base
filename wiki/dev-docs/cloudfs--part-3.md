---
title: CloudFS
summary: CloudFS is a POSIX filesystem you mount on any host or container, backed
  by Telnyx Cloud Storage. Built on the open-source JuiceFS Community Edition client,
  it splits a filesystem into a managed metadata database and an object storage data
  lane, with no JuiceFS server process running on the Telnyx side. The target use
  case is a shared, persistent filesystem for fleets of AI agents that need to read
  and write the same tree concurrently.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/filesystems-from-first-principles/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/how-cloudfs-works
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concepts/network-filesystems
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/concurrent-access
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/mount/index
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/quickstart
updated_at: 2026-08-05T13:41:05Z
---

# CloudFS

*Part 3 of 6 — see also: [Part 1](cloudfs--part-1.md), [Part 2](cloudfs--part-2.md), [Part 4](cloudfs--part-4.md), [Part 5](cloudfs--part-5.md), [Part 6](cloudfs--part-6.md)*

CloudFS is a POSIX filesystem you mount on any host or container, backed by Telnyx Cloud Storage. Built on the open-source JuiceFS Community Edition client, it splits a filesystem into a managed metadata database and an object storage data lane, with no JuiceFS server process running on the Telnyx side. The target use case is a shared, persistent filesystem for fleets of AI agents that need to read and write the same tree concurrently.

## How CloudFS Works

CloudFS is built on [JuiceFS](https://github.com/juicedata/juicefs), which — in its authors' words — was *"inspired by Google File System, HDFS and MooseFS."* JuiceFS takes the metadata/data split those systems proved at cluster scale and replaces each half with a managed cloud primitive, so you operate neither a metadata master nor a fleet of data servers:

- The **metadata index** — the master's job in GFS, the NameNode's in HDFS — becomes a **transactional database**. The database provides strong consistency for the small, hot, correctness-critical half: an entry is committed or it is not, and every client reads the same tree. This is the direct answer to NFS's stale-attribute cache and AFS's callback bookkeeping — put the index in one consistent place that all clients share, rather than caching copies and trying to keep them in sync. It also inherits the database's transactions: the crash-consistency machinery a local filesystem hand-builds as journaling — write-ahead log, commit, replay — is simply what the database already does, so a metadata change is one atomic transaction with no partial-update window and no `fsck`-style recovery scan.
- The **data blocks** — the chunkservers' job — become **object storage** (Telnyx Cloud Storage). JuiceFS splits every file into a **chunk → slice → block** hierarchy and writes the blocks as ordinary objects; object storage supplies the durability and throughput for the large half. The blocks are opaque — you cannot reassemble a file from the bucket alone, because the index that orders them lives in the metadata database. Object storage also rewards writing new immutable objects over rewriting in place, so JuiceFS follows a [log-structured](https://pages.cs.wisc.edu/~remzi/OSTEP/file-lfs.pdf) discipline: each write becomes a new **slice**, never an overwrite, and a background **compaction** later merges overlapping slices and reclaims the garbage — exactly the cleaner a log-structured filesystem runs.
- There is **no CloudFS server in the data path.** JuiceFS is a **"rich client"**: like AFS's client and MooseFS's FUSE mount, all the filesystem logic — the directory tree, inode allocation, splitting files into blocks, caching — runs in the process that mounts the volume. But instead of caching whole files and chasing callbacks, it reads and writes the shared metadata database directly, so consistency comes from the database rather than from a promise a server has to remember. When you `juicefs mount`, the client opens one connection to the metadata database and one to object storage, and serves POSIX calls from those two.

CloudFS is Telnyx's managed packaging of [JuiceFS Community Edition](https://github.com/juicedata/juicefs) (Apache-2.0): Telnyx runs and authenticates both the metadata database and the object storage and hands you a formatted, ready-to-mount filesystem. Because JuiceFS Community Edition is a client library with **no server process**, there is no JuiceFS component running on the Telnyx side at all. The server side is a generic managed metadata database and object storage; **every line of filesystem logic runs in the open-source JuiceFS client you mount** — which you can read, pin a version of, and run yourself. CloudFS is that community client plus managed backends and a control-plane API, not a proprietary server tier.

### The Two Lanes

Concretely, a CloudFS mount talks to two backends over two independent lanes, each with its own credential. There is no CloudFS server in the request path — your client connects to both directly.

![CloudFS two-lane architecture: the JuiceFS client on your host talks to a managed metadata lane and a Telnyx Cloud Storage data lane; no JuiceFS component runs server-side.](https://mintcdn.com/telnyx/xmslwVKx1bR_ia8Y/img/cloudfs-two-lanes-light.svg?fit=max&auto=format&n=xmslwVKx1bR_ia8Y&q=85&s=9c4efd1cc23db9dfca2788c8df61dcbb)

![CloudFS two-lane architecture: the JuiceFS client on your host talks to a managed metadata lane and a Telnyx Cloud Storage data lane; no JuiceFS component runs server-side.](https://mintcdn.com/telnyx/xmslwVKx1bR_ia8Y/img/cloudfs-two-lanes-dark.svg?fit=max&auto=format&n=xmslwVKx1bR_ia8Y&q=85&s=bcd721e36c6bee7278374f1f042211c7)

|  | Metadata lane | Data lane |
| --- | --- | --- |
| **What it stores** | Directory tree, filenames, inodes, chunk/slice index | File contents, split into 4 MiB block objects |
| **Backend** | Per-filesystem metadata database, behind a managed endpoint | Per-filesystem bucket on **Telnyx Cloud Storage** |
| **Endpoint** | `us-east-1.telnyxcloudfs.com:5432` (TLS, `sslmode=require`) | `https://<region>.telnyxcloudstorage.com` |
| **Location** | Always **us-east-1**, regardless of the filesystem's data region | The **data region** you chose at create time |
| **Credential** | `meta_token` (the metadata connection password) | Your `TELNYX_API_KEY` as the S3 access-key |

### The Metadata Lane

The client reaches metadata over the connection string CloudFS gives you as `meta_url`:

```
postgres://fs_<hex>:cloudfs_tok_...@us-east-1.telnyxcloudfs.com:5432/fs_<hex>?sslmode=require
```

A few things are load-bearing here:

- **You connect to a managed metadata endpoint, not to the database directly.** The public host `us-east-1.telnyxcloudfs.com:5432` is a pooled front end to a **per-filesystem metadata database** (`fs_<hex>`). The database server itself is not directly reachable.
- **TLS is required.** The connection uses `sslmode=require`; there is no plaintext metadata path.
- **The `meta_token` is the password.** In the `meta_url` above, the `cloudfs_tok_...` embedded before the `@` is the `meta_token` used as the connection password. It is a managed, rotatable credential — not the underlying database's own credential, which you never handle.

Metadata is **centralized in us-east-1 for every filesystem**, no matter which data region you pick. A `us-central-1` or `us-west-1` filesystem still has its metadata host set to `us-east-1.telnyxcloudfs.com`. Always use the host embedded in `meta_url`.

Because metadata lives only in us-east-1, a client mounting from another region pays a network round-trip on every metadata operation, so metadata-heavy work (listing large trees, many small files) is slower the farther you mount from us-east-1. Data throughput is unaffected — that lane goes to your region's storage endpoint.

### The Data Lane

File contents go to a **per-filesystem bucket** named `cloudfs-fs-<hex>` on Telnyx Cloud Storage, reached through the S3 endpoint for the filesystem's region (`s3_endpoint`, e.g. `https://us-east-1.telnyxcloudstorage.com`). JuiceFS splits every file into **4 MiB block objects** and writes them under `chunks/…` in that bucket; a 10 MiB file plus a small git repo, for example, lands as dozens of block objects. The blocks are opaque to S3 — reconstructing a file requires the chunk/slice index from the metadata lane.

That bucket lives in **your own Telnyx Cloud Storage account** — it shows up in your bucket list and is reachable with your `TELNYX_API_KEY`, exactly like any other bucket you own. But its contents are CloudFS's internal state, not your files: the `chunks/…` objects are opaque 4 MiB JuiceFS blocks, and a small `juicefs_uuid` object holds the volume format. **Do not delete, rename, move, or edit objects in a `cloudfs-fs-*` bucket by hand.** An out-of-band change corrupts the filesystem — a missing or altered block cannot be reconstructed, and there is no `fsck` to repair it. Read and write your files through the mount, and leave the bucket to JuiceFS.

Authentication to the data lane reuses your account credentials, following the Telnyx Cloud Storage model:

- The **S3 access-key is your `TELNYX_API_KEY`**.
- The **S3 secret-key is ignored** — Telnyx Storage does not verify the SigV4 signature (see [Cloud Storage authentication](https://developers.telnyx.com/docs/cloud-storage/authentication)). You must still supply *some* non-empty secret, because JuiceFS's AWS SDK rejects empty static credentials.

CloudFS **pre-formats** the bucket at create time: provisioning writes a `juicefs_uuid` object and formats the volume (JuiceFS volume name `cloudfs-fs-<hex>`). Do **not** run `juicefs format` against a `ready` filesystem — it is already formatted, and re-formatting fails with `cannot update volume name`. Just mount. The one exception is a filesystem whose status is `needs_format`, which was provisioned without the final format step: format it once as described in [Mounting a Filesystem](mounting-a-filesystem.md), then mount.

### Two Credentials, One API Key

Putting the lanes together, a mounting client holds exactly what it needs and nothing more:

| Credential | Reaches | Where you get it |
| --- | --- | --- |
| `TELNYX_API_KEY` | The data lane (S3 access-key) | You already have it |
| `meta_url` + `meta_token` | The metadata lane | Returned by **create** and **rotate** only |

The point of splitting the credentials this way is that **the client never holds a raw database credential**. It talks to the metadata endpoint with a managed `meta_token` that Telnyx can rotate independently of the underlying metadata database, and it never connects to the database server directly. Your API key, meanwhile, only ever reaches object storage. Compromising a mount host exposes a rotatable metadata token and your (already-scoped) API key — not standing database credentials.

Create and rotate are the **only** responses that return the `meta_token` (and the token-bearing `meta_url`). `GET` detail returns `meta_url` **without** the token, and list returns neither. Store the token when you create the filesystem — there is no way to read it back.

### Regions

You choose a **data region** at create time: `us-central-1`, `us-east-1`, or `us-west-1`. That region is required — there is no default — and it determines the S3 endpoint (`s3_endpoint`) and where the file blocks physically live. It is the only region choice you make.

**Metadata is always in us-east-1.** Picking `us-west-1` for data does not move the metadata database; that filesystem's metadata host is still `us-east-1.telnyxcloudfs.com`. Mount as close to us-east-1 as your data region allows if metadata latency matters to your workload.

### The Metadata Token Lifecycle

The `meta_token` is the one credential in the system designed to be rolled. Rotation is a control-plane action: `POST /v2/storage/cloudfs/{id}/actions/rotate-meta-token` (Idempotency-Key required) issues a **new** `meta_token` and returns a new token-bearing `meta_url`. Rotation touches **only the token** — the metadata database and the S3 bucket are unchanged, so no data moves and no files are re-encrypted or re-keyed.

The cutover is connection-scoped, which makes rotation safe to run against a live filesystem:

- The **old token stops authenticating on the next metadata connection** — any *new* `juicefs mount` (or reconnect) must use the new `meta_url`.
- An **already-mounted client is unaffected** on its existing connection. It keeps working with the connection it opened before rotation; you only need the new token the next time it reconnects.

So the operational rule is: rotate, then update wherever the old `meta_url` is stored (secrets, deploy config) before your mounts next reconnect.

### Filesystem Status

Each filesystem carries a `status`:

| `status` | Meaning |
| --- | --- |
| `provisioning` | Create is in progress. Create is synchronous (up to a 300s timeout) and normally returns `ready` directly, so this state is mostly visible when listing during a create. |
| `ready` | Fully provisioned and mountable. |
| `needs_format` | The bucket and metadata database were provisioned, but the volume was never formatted. Mounting fails with `database is not formatted`; run `juicefs format` once first — see [Mounting a Filesystem](mounting-a-filesystem.md). |
| `deleting` | Delete is in progress. |
| `failed` | The last lifecycle action failed; the detail response carries an `error` string explaining why. |
| `deleted` | Returned only by the delete response. A deleted filesystem no longer appears in list results and returns `404` on retrieval. |

The steady states are `ready`, `needs_format`, and `failed`; `provisioning` and `deleting` are transitional. There is no soft-delete or trash lifecycle — `deleted` is terminal and permanent.
