---
title: Local Development
summary: 'An Edge Compute function is an ordinary program in a container, so local
  development is unremarkable: run the program, curl it, iterate, then ship. This
  page covers running and testing each scaffolded language locally, framework servers,
  bindings and secrets, and deploying with `telnyx-edge ship`.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/development/index
updated_at: 2026-08-05T13:40:41Z
---

# Local Development

*Part 2 of 2 — see also: [Part 1](local-development--part-1.md)*

An Edge Compute function is an ordinary program in a container, so local development is unremarkable: run the program, curl it, iterate, then ship. This page covers running and testing each scaffolded language locally, framework servers, bindings and secrets, and deploying with `telnyx-edge ship`.

## Deploy

When it works locally, ship it:

```
telnyx-edge ship
# → 📡 Your function is live at:
#      https://<func-name>-<org>.telnyxcompute.com
```

Each successful ship creates an immutable revision; `telnyx-edge revisions list <function>` shows them and `telnyx-edge rollback <function> <revision-id>` retargets traffic to an earlier one. See [Deploy](deploy.md).

## Next Steps

- [Deploy](deploy.md) — ship, revisions, and rollback
- [HTTP handler](http-handler.md) — the exact entrypoint contract per language
- [Bindings](bindings.md) — the `env` surface a deployed function gets
- [CLI reference](cli-reference--part-1.md) — every `telnyx-edge` command
