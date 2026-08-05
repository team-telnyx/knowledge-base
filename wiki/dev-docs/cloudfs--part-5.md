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

*Part 5 of 6 — see also: [Part 1](cloudfs--part-1.md), [Part 2](cloudfs--part-2.md), [Part 3](cloudfs--part-3.md), [Part 4](cloudfs--part-4.md), [Part 6](cloudfs--part-6.md)*

CloudFS is a POSIX filesystem you mount on any host or container, backed by Telnyx Cloud Storage. Built on the open-source JuiceFS Community Edition client, it splits a filesystem into a managed metadata database and an object storage data lane, with no JuiceFS server process running on the Telnyx side. The target use case is a shared, persistent filesystem for fleets of AI agents that need to read and write the same tree concurrently.

## Mounting a Filesystem

A CloudFS filesystem is mounted with the [JuiceFS](https://juicefs.com) Community Edition client: give it the metadata URL and S3 credentials below, and it exposes a POSIX filesystem at a mountpoint through FUSE. This page is the end-to-end mount recipe for each environment, verified against a live filesystem. If your host can't do FUSE at all, see [Serving Without FUSE](serving-without-fuse.md) instead — no kernel support needed.

### Prerequisites

- **The JuiceFS Community Edition client.** Install it per the [JuiceFS docs](https://juicefs.com/docs/community/getting-started/installation). This page was verified end-to-end with JuiceFS CE 1.4.0.
- **An existing CloudFS filesystem** (create one via the [CloudFS Quick Start](cloudfs-quick-start.md)), and the `meta_url` and `meta_token` from its create response. The token is returned **only** at create (and on rotate) — if you didn't store it, you cannot reconstruct it and must rotate to get a new one.
- **FUSE.** A usable `/dev/fuse` on Linux, or [macFUSE](https://macfuse.github.io/) on macOS. ([Serving Without FUSE](serving-without-fuse.md) needs neither.)

### Credentials the Client Needs

The client holds three things. None of them is a raw database password — the metadata token *is* the password, embedded in the URL.

| Variable | Where it comes from | Used for |
| --- | --- | --- |
| `TELNYX_API_KEY` | Your Telnyx account | Doubles as the **S3 access key** for the data lane |
| `META_URL` | The `meta_url` field of the create/get response | The metadata connection (metadata endpoint) |
| `meta_token` | The `meta_token` field of the create/rotate response | The connection password, carried inline in `META_URL` |

The `meta_url` returned by **create** already has the token inline as the password:

```
postgres://fs_<hex>:cloudfs_tok_...@us-east-1.telnyxcloudfs.com:5432/fs_<hex>?sslmode=require
```

The `meta_url` returned by **`GET /v2/storage/cloudfs/{id}`** is the same string **without** the token:

```
postgres://fs_<hex>@us-east-1.telnyxcloudfs.com:5432/fs_<hex>?sslmode=require
```

If you're working from the tokenless URL, splice your stored `meta_token` in as the password (`postgres://fs_<hex>:<meta_token>@...`). The host is always the region metadata host `us-east-1.telnyxcloudfs.com` — metadata is centralized there regardless of the filesystem's data region.

### Set the Environment

```
export TELNYX_API_KEY="KEY..."   # your account API key
export META_URL="postgres://fs_<hex>:cloudfs_tok_...@us-east-1.telnyxcloudfs.com:5432/fs_<hex>?sslmode=require"

# S3 credentials for the data lane. The access key is your API key.
# The secret key's signature is ignored by Telnyx Storage — but it must be non-empty.
export AWS_ACCESS_KEY_ID="$TELNYX_API_KEY"
export AWS_SECRET_ACCESS_KEY="placeholder"
```

CloudFS volumes are formatted without embedded object-storage credentials, so JuiceFS picks them up from `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` at mount time. Set them explicitly. Telnyx Cloud Storage authenticates on the **access key alone** and ignores the SigV4 signature, so the secret can be any non-empty string. An empty secret fails: JuiceFS's AWS SDK rejects it with `static credentials are empty`.

Do **not** run `juicefs format` against a filesystem whose status is `ready`. Provisioning already formats the volume (the bucket ships with a `juicefs_uuid` object and a fixed volume name), and re-formatting fails with `cannot update volume name`. The one exception is a filesystem in `needs_format` — see below.

### Mount with FUSE

The first positional argument is the metadata URL; the second is the mountpoint. Mount in the background and write logs to a file so the mount doesn't block your terminal — on success the command returns immediately and the filesystem is live at the mountpoint.

**Linux** — needs a usable `/dev/fuse`, which stock kernels have.

```
mkdir -p /mnt/agentfs

juicefs mount --no-usage-report --background --log /tmp/juicefs.log "$META_URL" /mnt/agentfs
```

Watch `/tmp/juicefs.log` for the mount status and any warnings.

**Docker** — the most portable way to mount, with no FUSE install on the host and identical behavior everywhere. The container needs FUSE and the `juicefs` binary: run it privileged and pass the FUSE device through with `--device /dev/fuse`.

```
docker run --rm -it \
  --privileged \
  --device /dev/fuse \
  -e TELNYX_API_KEY="$TELNYX_API_KEY" \
  -e META_URL="postgres://fs_<hex>:cloudfs_tok_...@us-east-1.telnyxcloudfs.com:5432/fs_<hex>?sslmode=require" \
  ubuntu:24.04 bash
```

Inside the container, install the client and mount:

```
apt-get update && apt-get install -y curl fuse   # use fuse3 if fuse is unavailable
curl -sSL https://d.juicefs.com/install | sh -   # installs the JuiceFS CE client
juicefs version                                  # verified with 1.4.0

export AWS_ACCESS_KEY_ID="$TELNYX_API_KEY"
export AWS_SECRET_ACCESS_KEY="placeholder"

mkdir -p /mnt/agentfs
juicefs mount --no-usage-report --background --log /tmp/juicefs.log "$META_URL" /mnt/agentfs
```

`--privileged` and `--device /dev/fuse` are what let FUSE mount inside the container. Without them the mount fails to open `/dev/fuse`. If you bake the `juicefs` binary and `fuse` into your own image, you can skip the install step and go straight to `juicefs mount`.

**macOS (macFUSE)** — with [macFUSE](https://macfuse.github.io/) installed and its system extension approved, the recipe is the same — pick a mountpoint in your home directory:

```
mkdir -p ~/agentfs

juicefs mount --no-usage-report --background --log /tmp/juicefs.log "$META_URL" ~/agentfs
```

On a managed Mac, MDM policy often blocks macFUSE's system extension from loading at all. You don't need it: the [WebDAV serve path](serving-without-fuse.md) ends in a real Finder-mounted volume using only what ships with macOS.

The `--no-usage-report` flag opts out of JuiceFS's [anonymous usage reporting](https://github.com/juicedata/juicefs#usage-tracking). By default the JuiceFS client reports core metrics (such as its version) to the JuiceFS project on mount; it does not include user data. These docs pass `--no-usage-report` on every mount so CloudFS filesystems don't phone home by default — drop the flag if you'd like to share usage data with the upstream project.

### Formatting a `needs_format` Filesystem

If `GET /v2/storage/cloudfs/{id}` reports `"status": "needs_format"`, the bucket and metadata database exist but the volume was never formatted, and mounting fails with `database is not formatted, please run juicefs format ... first`. This is the one case where you run `juicefs format` — once, then mount as normal:

```
# Only for status: needs_format. The volume name is the s3_bucket value.
juicefs format --storage s3 \
  --bucket "<s3_endpoint>/<s3_bucket>" \
  "$META_URL" <s3_bucket>
```

`<s3_endpoint>` and `<s3_bucket>` come from the filesystem's detail response, and the JuiceFS volume name **must** be the `s3_bucket` value (`cloudfs-fs-<hex>`) — any other name is rejected. Keep `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` exported (`format` probes the bucket over S3) and leave `--access-key` / `--secret-key` unset: the stored volume config then carries no credentials, same as a factory-formatted filesystem. Note that `--no-usage-report` is a `mount` flag — `format` doesn't accept it.

### Verify the Mount

The checks below are written for Linux with the `/mnt/agentfs` mountpoint. On macOS, substitute yours (e.g. `~/agentfs`), check with `mount | grep agentfs` in place of `mountpoint`, and hash with `md5` in place of `md5sum`.

```
# Confirm the mountpoint is a real mount
mountpoint /mnt/agentfs

# CloudFS reports a very large logical capacity (~1.0 PB)
df -h /mnt/agentfs

# Round-trip a file
echo "hello cloudfs" > /mnt/agentfs/hello.txt
cat /mnt/agentfs/hello.txt

# Larger read/write test — write 10 MiB, read it back
dd if=/dev/urandom of=/mnt/agentfs/blob bs=1M count=10
md5sum /mnt/agentfs/blob
```

Anything you write is chunked into 4 MiB block objects in the filesystem's Cloud Storage bucket and persists across unmount/remount. A normal filesystem workflow works on top of it — for example `git init` and `git commit` inside the mountpoint behave as expected.

### Unmount

```
juicefs umount /mnt/agentfs   # your mountpoint — e.g. ~/agentfs on macOS
```

Unmounting only tears down the local FUSE mount; it does not touch the metadata database or the bucket. Remounting the same `META_URL` brings all files back.

### Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `static credentials are empty` at mount | `AWS_SECRET_ACCESS_KEY` is empty | Set it to any non-empty placeholder — the signature is ignored, but the value can't be blank |
| Mount succeeds, but writes hang for ~5 minutes and then fail (`flush … timeout`, `PutObject … exceeded maximum number of attempts` in the log), leaving 0-byte files | `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` missing or misnamed — mounting only talks to the metadata lane, so it comes up without S3 credentials; the data flush is what needs them | Export both variables, exact names, in the environment of the mount process (inside the container, not just on the host) and remount |
| `database is not formatted` at mount | The filesystem's status is `needs_format` | Format it once, then mount |
| `cannot update volume name` | You ran `juicefs format` against a `ready` (already-formatted) filesystem | Don't — `format` is only for `needs_format`. Otherwise, only `mount` |
