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

*Part 6 of 6 — see also: [Part 1](cloudfs--part-1.md), [Part 2](cloudfs--part-2.md), [Part 3](cloudfs--part-3.md), [Part 4](cloudfs--part-4.md), [Part 5](cloudfs--part-5.md)*

CloudFS is a POSIX filesystem you mount on any host or container, backed by Telnyx Cloud Storage. Built on the open-source JuiceFS Community Edition client, it splits a filesystem into a managed metadata database and an object storage data lane, with no JuiceFS server process running on the Telnyx side. The target use case is a shared, persistent filesystem for fleets of AI agents that need to read and write the same tree concurrently.

## Concurrent Access

CloudFS is a **shared** filesystem: the same filesystem can be mounted by many clients at once — a fleet of agents, a set of containers, several hosts — and they read and write it concurrently. Because the metadata index lives in one consistent store that every client reads and writes directly (rather than each client keeping its own copy and reconciling later), all mounts converge on the same directory tree.

### Mount the Same Filesystem on Many Clients

Every client mounts with the **same** `meta_url` (token included) and the **same** `TELNYX_API_KEY`. There is nothing per-client to set up — a mount holds no server-side state — so you can add or remove clients at any time. Run the [mount recipe](mounting-a-filesystem.md) on each host:

```
# on every client — same META_URL, same API key, any mountpoint
juicefs mount --no-usage-report --background --log /tmp/juicefs.log "$META_URL" /mnt/shared
```

Distribute the token to each client however you manage secrets. If you rotate the token, already-mounted clients keep working on their existing connection; only new mounts need the new `meta_url`.

### What One Client Sees of Another's Writes

CloudFS gives **close-to-open** consistency, the standard for shared filesystems: when a client writes a file and closes it, other clients see the new contents the next time they open it. Directory operations — create, rename, delete — commit to the metadata store immediately and become visible to other clients within about a second (the lifetime of a client's kernel metadata cache).

With client **A** and client **B** both mounted at `/mnt/shared`:

```
# on A — write a file and close it
echo "hello from A" > /mnt/shared/from-a.txt

# on B — read it back
cat /mnt/shared/from-a.txt        # -> hello from A
ls  /mnt/shared                   # -> from-a.txt (plus anything other clients wrote)
```

Concurrent writes to **different** files are independent: many clients can each write their own files at the same time with no coordination, and every client reads back exactly what another wrote, byte-for-byte.

### Coordinating Writers on the Same File

Two clients writing the **same** file (or the same byte range) at the same time is the one case that needs coordination — as on any shared filesystem, uncoordinated overlapping writes resolve last-writer-wins. Use file locks: CloudFS supports both **BSD locks** (`flock`) and **POSIX record locks** (`fcntl`), and JuiceFS coordinates them **across clients** through the shared metadata. A lock held on one host blocks a conflicting lock on another.

```
# on A — hold an exclusive lock while appending to a shared worklog
flock -x /mnt/shared/worklog.lock -c 'echo "$(date -u) A: built module X" >> /mnt/shared/worklog'

# on B — the same lock; B waits until A releases (here, up to 5s)
flock -x -w 5 /mnt/shared/worklog.lock -c 'echo "$(date -u) B: ran tests" >> /mnt/shared/worklog'
```

If B can't acquire the lock within its timeout, `flock` exits non-zero and B's command doesn't run — so a fleet can serialize access to a shared resource (a worklog, a build output directory, a leader-election file) without any external coordinator.

### Worked Example: Two Clients, One Filesystem

Two containers, each an independent client, mounting the same filesystem:

```
# build a JuiceFS-ready image once
docker build -t cfs-client - <<'EOF'
FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y curl ca-certificates fuse3 \
 && curl -sSL https://d.juicefs.com/install | sh -
EOF

# start two clients (each needs FUSE)
docker run -d --name client-a --privileged --device /dev/fuse cfs-client sleep infinity
docker run -d --name client-b --privileged --device /dev/fuse cfs-client sleep infinity

# mount the SAME filesystem in each (same META_URL + API key)
for c in client-a client-b; do
  docker exec -e META_URL="$META_URL" \
    -e AWS_ACCESS_KEY_ID="$TELNYX_API_KEY" -e AWS_SECRET_ACCESS_KEY="placeholder" "$c" \
    sh -c 'mkdir -p /mnt/shared && juicefs mount --no-usage-report --background --log /tmp/j.log "$META_URL" /mnt/shared'
done

# A writes, B reads it
docker exec client-a sh -c 'echo "written by A" > /mnt/shared/hello.txt'
docker exec client-b sh -c 'cat /mnt/shared/hello.txt'   # -> written by A
```

### Caveats

- **Same-file, uncoordinated concurrent writes** resolve last-writer-wins on overlapping regions. Use the locks above whenever more than one client may write the same file.
- **Metadata latency.** Every metadata operation — open, create, rename, lock — is a round-trip to `us-east-1`. Coordination-heavy or many-small-file workloads run faster the closer clients mount to us-east-1; bulk data throughput is unaffected.
- **One credential set per filesystem.** All clients share the same `meta_token` and API key; there is no per-client scoping *within* a filesystem.

## Further Reading

- [*Operating Systems: Three Easy Pieces*](https://pages.cs.wisc.edu/~remzi/OSTEP/) — [Files and Directories](https://pages.cs.wisc.edu/~remzi/OSTEP/file-intro.pdf), [File System Implementation](https://pages.cs.wisc.edu/~remzi/OSTEP/file-implementation.pdf), [Locality and the Fast File System](https://pages.cs.wisc.edu/~remzi/OSTEP/file-ffs.pdf), [Crash Consistency: FSCK and Journaling](https://pages.cs.wisc.edu/~remzi/OSTEP/file-journaling.pdf), [Data Integrity and Protection](https://pages.cs.wisc.edu/~remzi/OSTEP/file-integrity.pdf), and [Log-structured File Systems](https://pages.cs.wisc.edu/~remzi/OSTEP/file-lfs.pdf).
- [Sun's Network File System (NFS)](https://pages.cs.wisc.edu/~remzi/OSTEP/dist-nfs.pdf) and [The Andrew File System (AFS)](https://pages.cs.wisc.edu/~remzi/OSTEP/dist-afs.pdf), from OSTEP.
- [The Google File System](https://research.google/pubs/pub51) (Ghemawat, Gobioff, Leung), [Apache Hadoop / HDFS](https://hadoop.apache.org), and [MooseFS](https://moosefs.com).
- [JuiceFS](https://github.com/juicedata/juicefs) — the open-source filesystem CloudFS is built on: [architecture](https://juicefs.com/docs/community/architecture) and [how JuiceFS stores files](https://juicefs.com/docs/community/architecture#how-juicefs-store-files).
- [Cloud Storage authentication](https://developers.telnyx.com/docs/cloud-storage/authentication) — how the API key is used as the S3 access key.
- [Object Storage](https://developers.telnyx.com/docs/cloud-storage/overview) — the S3-compatible storage CloudFS is backed by.

## Next Steps

- [CloudFS Quick Start](cloudfs-quick-start.md) — create a filesystem and mount it end-to-end
- [How CloudFS Works](how-cloudfs-works.md) — the two-lane architecture and credentials
- [Mounting a Filesystem](mounting-a-filesystem.md) — the verified `juicefs mount` recipe
- [Serving Without FUSE](serving-without-fuse.md) — a WebDAV endpoint for hosts that can't mount
- [Concurrent Access](concurrent-access.md) — mount the same filesystem from many clients at once
- [CloudFS API Reference](cloudfs-api-reference.md) — the `/v2/storage/cloudfs` endpoints
