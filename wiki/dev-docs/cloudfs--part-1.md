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

*Part 1 of 6 — see also: [Part 2](cloudfs--part-2.md), [Part 3](cloudfs--part-3.md), [Part 4](cloudfs--part-4.md), [Part 5](cloudfs--part-5.md), [Part 6](cloudfs--part-6.md)*

CloudFS is a POSIX filesystem you mount on any host or container, backed by Telnyx Cloud Storage. Built on the open-source JuiceFS Community Edition client, it splits a filesystem into a managed metadata database and an object storage data lane, with no JuiceFS server process running on the Telnyx side. The target use case is a shared, persistent filesystem for fleets of AI agents that need to read and write the same tree concurrently.

## Overview

CloudFS is a POSIX filesystem you mount on any host or container. Once mounted, it behaves like a local directory — `read`, `write`, `mkdir`, `rename`, `git init` — but every byte is stored durably in Telnyx Cloud Storage, and the same filesystem can be mounted by many clients at once, so a fleet of agents can read and write it concurrently.

You mount it with the open-source [JuiceFS Community Edition](https://github.com/juicedata/juicefs) client (Apache-2.0), which you run yourself — Telnyx does not host or bundle it. JuiceFS has **no server process**: the client does all the filesystem work and talks directly to a metadata database and to object storage, so **no JuiceFS component runs on the Telnyx side**. Telnyx provides and authenticates the two managed backends — the metadata database and object storage — and hands you a ready-to-mount filesystem.

The target use case is a **shared, persistent filesystem for AI agents**: provision one CloudFS, mount it once, and every file, repo, and checkpoint an agent produces is there — and still there on the next mount, from anywhere.

> **Do not touch the `cloudfs-fs-*` bucket directly.** A CloudFS filesystem's data lives in a bucket named `cloudfs-fs-<hex>` inside **your own Telnyx Cloud Storage account** — it appears alongside your other buckets and is reachable with your API key. Its objects are **opaque JuiceFS blocks** (`chunks/…` plus internal bookkeeping), not your files. Deleting, renaming, or editing objects in that bucket out of band **corrupts the filesystem** — a missing block is unrecoverable and there is no repair path. Manage a CloudFS filesystem only through the [CloudFS API Reference](cloudfs-api-reference.md) and a [JuiceFS mount](mounting-a-filesystem.md); treat its bucket as internal, hands-off storage.

CloudFS is in **beta**. The API surface and behavior may still change as it moves toward general availability.

## Concepts: Filesystems From First Principles

To understand how CloudFS is shaped, it helps to build the idea from the bottom up. A filesystem is [two abstractions](https://pages.cs.wisc.edu/~remzi/OSTEP/file-intro.pdf):

- A **file** is a linear array of bytes with a **low-level name** — a number, the **inode number**. The operating system does not care whether those bytes are a JPEG or C source; it stores them and hands them back intact.
- A **directory** is itself a file, but its contents are specific: a list of `(human-readable name → inode number)` pairs. Nest directories inside directories and you get the tree you navigate every day.

So underneath a familiar path like `/home/agent/work.log`, a filesystem is really two things: **an index** that maps names to inodes and inodes to the location of bytes, and **the bytes themselves**. Everything else — `open`/`read`/`write`/`close`, permissions, hard and symbolic links — is built on top of those two.

### How a Local Filesystem Is Built

On a single disk, those two things live in two different places. OSTEP's teaching filesystem, [vsfs](https://pages.cs.wisc.edu/~remzi/OSTEP/file-implementation.pdf), divides the disk into an **inode table** plus small **bitmaps** that track which inodes and blocks are free — this is the metadata index — and a much larger **data region** of fixed-size blocks that holds file contents. Each inode is a compact record of metadata (permissions, timestamps, size) plus a **multi-level index** of pointers to the file's data blocks. Reading a file means reading its inode to find the block pointers, then reading the blocks; writing a file may also flip an allocation bit and rewrite the inode.

The [Fast File System](https://pages.cs.wisc.edu/~remzi/OSTEP/file-ffs.pdf) added the lesson that *where* you place those blocks matters: the original Unix filesystem treated the disk like RAM and paid for it in seeks, so FFS made the filesystem **"disk-aware"** — keep an inode near its data, keep files of one directory together, respect the physical medium.

The durable takeaway is this: **a filesystem is a metadata index over a pile of data blocks — two kinds of state with two very different access patterns.** Metadata is small, hot, and demands consistency: an inode is either allocated or it is not. Data is large and wants throughput. Hold onto that split; it is the key to everything that follows.

### Staying Consistent Across Crashes

The metadata index has one more demand: it must survive a crash. A single logical operation — appending a block to a file, say — touches several structures (the allocation bitmap, the inode, the data block), but the disk writes them one at a time. Lose power in between and the index is left inconsistent: a block marked used by no file, or an inode pointing at garbage.

Early filesystems repaired this after the fact with **fsck**, scanning the whole disk on reboot — which stops scaling as disks grow. The durable fix, [**journaling** (write-ahead logging)](https://pages.cs.wisc.edu/~remzi/OSTEP/file-journaling.pdf), is borrowed straight from databases: write your intended changes to a **log** and commit them there first, then apply them to their real homes; after a crash, replay the committed log. Recovery then costs the size of the log, not the size of the disk. Keep this one in mind — it is the cleanest argument for *where* CloudFS keeps its metadata.

And the medium underneath can lie: a sector rots, or silently returns the wrong bytes. Filesystems and storage layers defend against it with [checksums and scrubbing](https://pages.cs.wisc.edu/~remzi/OSTEP/file-integrity.pdf); CloudFS leaves that to the object store, which does it for you.
