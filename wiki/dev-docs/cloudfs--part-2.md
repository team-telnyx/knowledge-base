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

*Part 2 of 6 — see also: [Part 1](cloudfs--part-1.md), [Part 3](cloudfs--part-3.md), [Part 4](cloudfs--part-4.md), [Part 5](cloudfs--part-5.md), [Part 6](cloudfs--part-6.md)*

CloudFS is a POSIX filesystem you mount on any host or container, backed by Telnyx Cloud Storage. Built on the open-source JuiceFS Community Edition client, it splits a filesystem into a managed metadata database and an object storage data lane, with no JuiceFS server process running on the Telnyx side. The target use case is a shared, persistent filesystem for fleets of AI agents that need to read and write the same tree concurrently.

## Concepts: Network Filesystems

A local filesystem is a metadata index over a pile of data blocks. To share one between machines you must move one or both of those halves across a network — and decades of distributed filesystems show that is where the difficulty lives.

### NFS: Stateless, and Brittle Over the WAN

[Sun's Network File System](https://pages.cs.wisc.edu/~remzi/OSTEP/dist-nfs.pdf) makes the filesystem a client/server protocol. Its central design goal is **simple, fast crash recovery**, achieved by making the server **stateless** — it keeps no per-client state, so every request carries everything needed to service it (a `READ` sends the explicit offset; the client, not the server, tracks position). Most operations are **idempotent**, so the failure handler collapses to a single rule: *set a timer, and if no reply arrives, retry.* Elegant — but it has costs that bite hard over a wide-area network:

- **Weak cache consistency.** Clients cache and buffer writes for performance, which introduces the update-visibility problem. NFS papers over it with flush-on-close and an **attribute cache with a timeout** (~3 seconds), so whether a client sees the latest version of a file "depends on whether the cache entry has timed out" — the source of NFS's notorious occasional stale reads.
- **The hang.** Because the client simply retries until the server answers, an unresponsive or partitioned server makes the client **block indefinitely**. A `read()` that never returns takes the calling process — and often a whole pipeline — down with it. A network partition is indistinguishable from a crash.
- **Small files are easy; large files are not.** Over a LAN with small files NFS is fine. Over a WAN, file seeks and mid-file updates on large files get ugly, and rapid writes suffer under lost packets.

With a default hard mount, if the NFS server crashes or the network partitions, any process that so much as `stat`s a path under the mount blocks in uninterruptible sleep — `ls` hangs, shrugs off Ctrl-C, and the console fills with `NFS server not responding, still trying`. The mount doesn't return an error; it waits, and takes the caller down with it. That is tolerable on a quiet LAN with a reliable server; for agents scattered across the internet — where partitions are routine and every mount is one flaky link from a hung process — it is the wrong default.

### AFS: Whole-File Caching, and Stateful Bookkeeping

The [Andrew File System](https://pages.cs.wisc.edu/~remzi/OSTEP/dist-afs.pdf) was built for **scale**. On `open()` it fetches the *whole file* to the client's local disk and serves subsequent reads and writes locally; on `close()` it ships the whole file back. To avoid clients constantly polling "has this changed?", AFS added **callbacks** — a promise from the server to notify a client when a cached file changes — giving **close-to-open** consistency. It scales better than NFS, but the design fights the shared-agent use case:

- **Callback state is awkward for clients that come and go.** A client that was offline may have missed an invalidation and must revalidate its whole cache on return; a rebooted server does not know which clients cache what and must have everyone re-validate. Ephemeral agents — containers that appear, work, and vanish — are exactly the clients this bookkeeping handles worst.
- **Whole-file caching punishes the workload we care about.** Fetching and rewriting an entire file just to append one line to a shared worklog, or to touch a small region of a large file, is precisely what AFS does poorly. AFS itself notes that its baseline consistency is not enough for concurrent updates to something like a shared code repository — you still need explicit **file-level locking**.

The through-line: NFS and AFS both begin with a filesystem that assumes **one server owns the disk**, and then bolt a network onto it. For a fleet of ephemeral agents working on a shared tree, over the public internet, on top of object storage rather than a local disk, that is the wrong starting shape.

### Separating Metadata From Data

By the early 2000s a different design had emerged — built for a fleet of cheap, failure-prone machines from the start, rather than making a single server's disk look remote.

[Google File System](https://research.google/pubs/pub51) (GFS, 2003) split the problem cleanly in two: a single **master** holds all the metadata — the namespace and the map from each file to its **chunks** — in memory, and a fleet of **chunkservers** holds the file data as large chunks (64 MB), replicated for durability. The move that matters: **the master is kept out of the data path.** A client asks the master *where* a file's chunks live, then streams the bytes **directly** to and from the chunkservers. Metadata (small, hot, consistency-critical) and data (large, bulk) are served by different systems on different paths — the same split seen inside the local filesystem, now drawn across a cluster.

[HDFS](https://hadoop.apache.org) is the open-source realization of that design: a **NameNode** holds the namespace and the file→block map — "user data never flows through the NameNode" — while **DataNodes** store the blocks (128 MB) and serve reads and writes directly to clients. [MooseFS](https://moosefs.com) applied the same master-plus-chunkservers split but exposed a full **POSIX filesystem you mount**, closing the gap back to the local-filesystem interface.

These systems fixed what NFS and AFS could not: they stopped pretending one server owns a disk, and instead let **an authoritative metadata service** coordinate **a scalable pool of data storage**. What they still asked of you was to run that metadata master and that fleet of data servers yourself — which is exactly the operational burden CloudFS removes.
