---
title: Management & Access
summary: What you control and what Telnyx manages on the LiveKit platform.
sources:
  - url: https://developers.telnyx.com/docs/livekit/deploy/management
    content_hash: 9c28e9d1fb90cad0c10acd8d59eb43ae5e3e17a0542bc2ac43e2e8f2a32f2fa2
updated_at: 2026-04-10T00:00:00Z
---

# Management & Access

What you control and what Telnyx manages on the LiveKit platform.

## Access model

All platform interaction is through the `lk` CLI and the [Telnyx Portal](https://portal.telnyx.com). There is no direct access to underlying infrastructure (no kubectl, no SSH).

## What Telnyx manages

* LiveKit SFU (media server)
* SIP service (built-in telephony)
* Agent container runtime and orchestration
* Autoscaling
* TLS/SSL termination and load balancing
* Health checks and rolling deploys

## What you control

| Capability                | How                                                     |
| ------------------------- | ------------------------------------------------------- |
| Agent code and Dockerfile | `lk agent deploy .`                                     |
| Secrets                   | `lk agent deploy --secrets` / `lk agent update-secrets` |
| Rollback                  | `lk agent rollback`                                     |
| Logs                      | `lk agent logs`                                         |
| Phone numbers             | Telnyx Portal                                           |
| SIP connections           | Telnyx Portal                                           |
| Model selection           | Telnyx plugin or BYOK                                   |

## Current limitations

* No volume mounts or persistent storage
* No custom networking or network policies
* No privileged containers
* No custom domains
* No direct database access — use external services with secrets

See [Compatibility](compatibility.md) for the full list of supported and unsupported features.
