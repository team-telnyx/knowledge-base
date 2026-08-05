---
title: Serving Without FUSE
summary: Explains how to expose a CloudFS filesystem as a WebDAV endpoint using the
  JuiceFS client when FUSE mounting is not available, including setup, macOS Finder
  integration, operational limits, and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/cloudfs/serve
updated_at: 2026-08-05T13:39:59Z
---

# Serving Without FUSE

Explains how to expose a CloudFS filesystem as a WebDAV endpoint using the JuiceFS client when FUSE mounting is not available, including setup, macOS Finder integration, operational limits, and troubleshooting.

## Overview

A WebDAV-served filesystem is not full POSIX. Everyday file operations work, but the POSIX surface a [FUSE mount](mounting-a-filesystem.md) provides does not survive the HTTP hop.

**Good for:** reading and writing files, shuttling them between machines, browsing in Finder, everyday `ls` / `cd` / `cp` / `mv` / `mkdir`, and any app that speaks WebDAV directly.

**No good for:** git working trees (`git init` fails), executing binaries in place (`noexec`), coordinating writers with file locks (`flock` is local-only), or anything that needs faithful permissions and ownership. For those, [mount with FUSE](mounting-a-filesystem.md).

[Mounting a Filesystem](mounting-a-filesystem.md) goes through FUSE, and not every host has FUSE to give: a managed Mac whose MDM policy blocks [macFUSE](https://macfuse.github.io/), a container you can't run with `--device /dev/fuse`, a host where you aren't root. The same JuiceFS client can **serve** the filesystem instead: `juicefs webdav` is an ordinary user-space process listening on a TCP port — it holds the same two backend connections a mount holds and exposes the filesystem as a [WebDAV](https://juicefs.com/docs/community/deployment/webdav) endpoint over HTTP, with no kernel support at all.

Serving is not mounting — no path on the host becomes the filesystem; clients speak HTTP to a port. On macOS you can then mount that endpoint in Finder with the OS's built-in WebDAV client and get a Finder-visible volume anyway. A serve process is a full JuiceFS client, so it coexists with every other client of the filesystem — FUSE mounts elsewhere, [many clients at once](concurrent-access.md) — with the same close-to-open consistency between clients as between mounts. Verified end-to-end with JuiceFS CE 1.4.0 against a live filesystem.

## Prerequisites

- **The JuiceFS Community Edition client.** Install it per the [JuiceFS docs](https://juicefs.com/docs/community/getting-started/installation).
- **An existing CloudFS filesystem** ([create one](quickstart.md)), and the same environment a mount takes — the tokenized `META_URL` plus the `AWS_*` pair. Set them per [Set the Environment](/docs/edge-compute/cloudfs/mount#set-the-environment) on the mount page.

## Start the WebDAV Server

```
juicefs webdav --no-usage-report --background --log /tmp/juicefs-webdav.log \
  "$META_URL" 127.0.0.1:9007
```

On success the launcher prints `OK, service is ready on "127.0.0.1:9007"` and returns. The filesystem is now an HTTP endpoint — round-trip a file to confirm:

```
echo "hello over webdav" | curl -s -T - http://127.0.0.1:9007/hello.txt   # -> Created
curl -s http://127.0.0.1:9007/hello.txt                                   # -> hello over webdav
```

By default the endpoint is **unauthenticated**, which is why these examples bind to `127.0.0.1` — only processes on the same host can reach it. To serve beyond localhost, set `WEBDAV_USER` and `WEBDAV_PASSWORD` in the server's environment before starting it; the server then returns `401` unless the request carries matching Basic credentials (`curl -u agent:...`). Basic auth over plain `http://` sends the password — and your files — readable on the wire, so pair it with TLS (`juicefs webdav` serves HTTPS with `--cert-file` / `--key-file`) or keep the port reachable only over a private network or SSH tunnel.

`--background` daemonizes the server, which is convenient interactively. Under a supervisor (launchd, systemd, a container entrypoint), drop `--background` and run it in the foreground — the supervisor then owns restarts, and startup errors land in its logs instead of a detached daemon's.

## Mount the WebDAV Endpoint in Finder (macOS)

macOS ships its own WebDAV filesystem — it's what **Go → Connect to Server** uses. It is part of the OS, so an MDM policy that blocks third-party system extensions (the reason macFUSE won't install) doesn't apply to it. Point it at the local server and you get a real mounted volume — a mount of the *endpoint*, one hop in front of CloudFS:

```
mkdir -p ~/CloudFS
mount_webdav -v CloudFS http://127.0.0.1:9007/ ~/CloudFS
```

The Finder-only equivalent is **Cmd+K → `http://127.0.0.1:9007`**. If Finder prompts for credentials against an anonymous server, connect as **Registered User** with any username and an empty password — the **Guest** option is rejected. Unmount with `umount ~/CloudFS`.

## What Works Through the Mount — and What Doesn't

Everyday file operations behave like a local directory: `ls`, `cd`, `mkdir`, `cp`, `mv`, `cat`, editing files, working in Finder — all verified against a live filesystem. But it is WebDAV underneath, not POSIX, and the difference shows at the edges:

- **No executing in place.** The volume is mounted `nodev,noexec,nosuid` — you can read and write binaries, but running one from the mount fails with `permission denied`. Copy it out first.
- **Listings lag a few seconds.** Apple's WebDAV client caches directory listings, so a file another client just wrote may take a moment (or a Finder refresh) to appear.
- **Git working trees don't work.** `git init` inside the mount fails writing `.git/config` (`Invalid argument`). Keep repositories on a [FUSE mount](mounting-a-filesystem.md), which handles them fine.
- **File locks coordinate nothing.** `flock` calls succeed, but the lock is local to your machine — the [cross-client lock coordination](/docs/edge-compute/cloudfs/concurrent-access#coordinating-writers-on-the-same-file) that FUSE mounts get through the shared metadata does not ride over WebDAV. Don't rely on locks taken through this mount.
- **Permissions are cosmetic.** Every entry appears owned by your local user with `-rwx------` modes, whatever a POSIX client would see.

When you need POSIX behavior — locks, executability, repositories — use a [FUSE mount](mounting-a-filesystem.md). For reading, writing, and shuttling files between machines, the WebDAV path is enough.

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| The `--background` launcher exits with `The service is not ready in 10 seconds, please check the log or restart in foreground` | The launcher waits only 10s for the serve port; a slow first metadata connection (the client warns `The latency to database is too high`) can exceed that — the child process often becomes ready moments later | Check the port before assuming failure (`nc -z 127.0.0.1 9007`), or run in the foreground |
| `open log file ...: no such file or directory` at startup | The `--log` file's directory (or `~/.juicefs`, the default log location) doesn't exist. The server still starts — but logs nowhere | `mkdir -p` the log directory first |
| Every request returns `401 Unauthorized` | The server was started with `WEBDAV_USER` / `WEBDAV_PASSWORD` set | Send Basic credentials (`curl -u`, or the username/password prompt in Finder) |
| A file written by another client isn't in a listing yet | Apple's WebDAV client caches directory listings for a few seconds | Wait a moment or refresh; opening the file by name fetches it fresh |

## Next Steps

- [Mounting a Filesystem](mounting-a-filesystem.md) — the FUSE recipe, and the environment setup this page reuses
- [Concurrent Access](concurrent-access.md) — many clients on one filesystem, and what consistency they get
- [How CloudFS Works](how-cloudfs-works.md) — the metadata and data lanes every client connects to
