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

*Part 4 of 6 — see also: [Part 1](cloudfs--part-1.md), [Part 2](cloudfs--part-2.md), [Part 3](cloudfs--part-3.md), [Part 5](cloudfs--part-5.md), [Part 6](cloudfs--part-6.md)*

CloudFS is a POSIX filesystem you mount on any host or container, backed by Telnyx Cloud Storage. Built on the open-source JuiceFS Community Edition client, it splits a filesystem into a managed metadata database and an object storage data lane, with no JuiceFS server process running on the Telnyx side. The target use case is a shared, persistent filesystem for fleets of AI agents that need to read and write the same tree concurrently.

## Quick Start

Get up and running with CloudFS: create a filesystem over the API, then mount it with the JuiceFS client inside a Linux container and use it like any local directory — write files, read them back, run `git`. The whole path below is verified end-to-end against production.

CloudFS is built on [JuiceFS Community Edition](https://github.com/juicedata/juicefs). There is no server process to run: the JuiceFS client on your host talks directly to a per-filesystem metadata database and to Telnyx Cloud Storage. That means you hold two credentials — the `meta_token` (returned on create) and your `TELNYX_API_KEY` — and the client does the rest.

### 1. Create a Filesystem

`POST /v2/storage/cloudfs`. The `Idempotency-Key` header is **required** (a request without it is rejected with `400`), and so is `region` — there is no default. Allowed regions are `us-central-1`, `us-east-1`, and `us-west-1`.

```
curl -X POST https://api.telnyx.com/v2/storage/cloudfs \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{"name": "agent-fs", "region": "us-east-1"}'
```

Replaying the same `Idempotency-Key` returns the same filesystem instead of creating a second one. A `201` response looks like this:

```
{
  "data": {
    "record_type": "cloudfs",
    "id": "0195e0a2-3f4b-4c8d-9a1e-7b62d4c90f13",
    "name": "agent-fs",
    "status": "ready",
    "meta_url": "postgres://fs_9f3c8e2a4b7d01c6:cloudfs_tok_...@us-east-1.telnyxcloudfs.com:5432/fs_9f3c8e2a4b7d01c6?sslmode=require",
    "meta_token": "cloudfs_tok_...",
    "s3_endpoint": "https://us-east-1.telnyxcloudstorage.com",
    "s3_bucket": "cloudfs-fs-9f3c8e2a4b7d01c6",
    "region": "us-east-1",
    "created_at": "2026-07-14T21:42:01.384912Z",
    "updated_at": "2026-07-14T21:42:03.192847Z"
  }
}
```

**This is the only time you see the token.** `meta_url` (with the token inline as the password) and the standalone `meta_token` are returned **only** on create and on rotate. `GET /v2/storage/cloudfs/{id}` returns `meta_url` **without** the token and no `meta_token` at all — it cannot be read back. Store the token securely now; if you lose it, rotate to get a new one.

You'll use two values from this response to mount:

- `meta_url` — the full connection string, token included. This is the metadata endpoint; the host is always `us-east-1.telnyxcloudfs.com` regardless of the filesystem's region.
- `id` — the filesystem UUID, for later API calls (detail, rename, rotate).

The response's `s3_bucket` (`cloudfs-fs-<hex>`) is in **your** Telnyx Cloud Storage account, but it holds CloudFS's internal blocks — not your files. Never modify or delete its objects directly; that corrupts the filesystem. Read and write only through the mount below.

### 2. Mount It with JuiceFS

CloudFS **pre-formats** the volume during provisioning — the bucket already contains the JuiceFS volume metadata.

Do **not** run `juicefs format`. The filesystem is already formatted; running `format` against it fails with `cannot update volume name`. Go straight to `juicefs mount`. (The one exception: if the filesystem's status is `needs_format`, it *does* need a one-time `juicefs format` before mounting — see [Mounting a Filesystem](mounting-a-filesystem.md).)

Mount inside a Linux container with FUSE — a portable path that runs the same anywhere and needs no FUSE install on the host. (You can also mount natively on any Linux or macOS host that has FUSE/macFUSE installed.) The data lane authenticates to Telnyx Cloud Storage over S3: your `TELNYX_API_KEY` is the **access key**, and the secret key can be **any non-empty placeholder** (Telnyx Storage ignores the SigV4 signature, but JuiceFS's AWS SDK rejects an empty secret).

```
# Start a Linux container with FUSE access, passing your API key through.
docker run --rm -it --privileged --device /dev/fuse \
  -e TELNYX_API_KEY \
  ubuntu:24.04 bash
```

```
# --- inside the container ---

# Install the JuiceFS Community Edition client
apt-get update && apt-get install -y curl fuse
curl -sSL https://d.juicefs.com/install | sh -

# Point JuiceFS at your S3 credentials:
export AWS_ACCESS_KEY_ID="$TELNYX_API_KEY"     # S3 access key = your Telnyx API key
export AWS_SECRET_ACCESS_KEY="cloudfs-unused"  # any NON-EMPTY value; the signature is ignored

# Mount with the meta_url from step 1 (token inline). --background --log keeps
# the mount off your terminal; --no-usage-report opts out of JuiceFS telemetry.
mkdir -p /mnt/agentfs
juicefs mount --no-usage-report --background --log /tmp/juicefs.log \
  "postgres://fs_9f3c8e2a4b7d01c6:cloudfs_tok_...@us-east-1.telnyxcloudfs.com:5432/fs_9f3c8e2a4b7d01c6?sslmode=require" \
  /mnt/agentfs
```

Check `/tmp/juicefs.log` for progress. Once mounted, `df -h /mnt/agentfs` shows the volume.

### 3. Smoke-Test Over POSIX

The mount is a normal directory. Write a file, read it back, and initialize a git repo — all standard POSIX, no CloudFS-specific calls.

```
cd /mnt/agentfs

# Write and read back
echo "hello cloudfs" > hello.txt
cat hello.txt                 # -> hello cloudfs

# git works against the mounted filesystem
git init -q
git -c user.email=agent@example.com -c user.name=agent add hello.txt
git -c user.email=agent@example.com -c user.name=agent commit -q -m "first commit"
git log --oneline             # -> the commit you just made
```

Data written here lands in Telnyx Cloud Storage as 4 MiB block objects under `chunks/…` in the filesystem's bucket, and persists across unmount and remount — remount with the same `meta_url` and your files are still there.
