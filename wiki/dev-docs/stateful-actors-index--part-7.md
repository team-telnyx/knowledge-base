---
title: Stateful Actors - Index
summary: Stateful Actors on Telnyx Edge Compute give each named entity its own durable,
  single-threaded instance with private key/value and SQL storage, alarms, and WebSocket
  support. This page covers when to use them, the storage surfaces, local development,
  the Quick Start, shared actors across functions, and WebSocket patterns.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/storage/key-value/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/storage/sql
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/guides/when-to-use
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/local-development
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/quick-start/index
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/shared-actors
- url: https://developers.telnyx.com/docs/edge-compute/stateful-actors/websockets/index
updated_at: 2026-08-05T13:43:37Z
---

# Stateful Actors - Index

*Part 7 of 7 — see also: [Part 1](stateful-actors-index--part-1.md), [Part 2](stateful-actors-index--part-2.md), [Part 3](stateful-actors-index--part-3.md), [Part 4](stateful-actors-index--part-4.md), [Part 5](stateful-actors-index--part-5.md), [Part 6](stateful-actors-index--part-6.md)*

Stateful Actors on Telnyx Edge Compute give each named entity its own durable, single-threaded instance with private key/value and SQL storage, alarms, and WebSocket support. This page covers when to use them, the storage surfaces, local development, the Quick Start, shared actors across functions, and WebSocket patterns.

## Related

- [SQL](sql.md) — the `ctx.storage.sql` guide
- [Actor Storage reference](actor-storage-reference.md) — full method signatures and codec rules
- [Alarms](alarms.md) — scheduled self-wakeups
- [SQL Database](sql-database.md) — the shared, standalone SQLite database, for data more than one caller reads
- [Execution model](execution-model.md) — why `exec` needs no lock
- [How it works](how-it-works.md) — the execution model and its limits
- [Addressing](addressing.md) — choosing names that spread load
- [Shared actors](shared-actors.md) — one actor, many functions
- [Project structure](project-structure.md) — the two-export shape `telnyx-edge dev` runs
- [Deploy](deploy.md) — ship, revisions, and rollback
- [Connection Lifecycle](connection-lifecycle.md) — duration budget, close codes, reconnect strategy
- [Runtime API](runtime-api.md) — `StatefulActor`, `ctx`, `storage`, alarms
