---
title: Bulk Operations
summary: One-time batch operations on an explicit list of SIMs.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/bulk-sim-actions/index
    content_hash: 6739d3a588f79e47c54f9653ce08e7bb71364eafe56d99ba40749b46fca6352e
updated_at: 2026-04-10T00:00:00Z
---

# Bulk Operations

One-time batch operations on an explicit list of SIMs.

> **Warning:** **Bulk vs Group** — Bulk actions are one-time operations on an explicit list of SIM IDs. Nothing persists. For ongoing policy that applies to current and future SIMs, use [Groups](sim-card-groups.md).

## Bulk Actions

All actions are async — submit a list of SIM IDs, get back an action ID, poll for status.

| Action                                                                                        |
| :-------------------------------------------------------------------------------------------- |
| [Bulk Enable Voice](https://developers.telnyx.com/api-reference/sim-cards/request-bulk-enabling-voice-on-sim-cards)        |
| [Bulk Disable Voice](https://developers.telnyx.com/api-reference/sim-cards/request-bulk-disabling-voice-on-sim-cards)      |
| [Bulk Set Public IPs](https://developers.telnyx.com/api-reference/sim-cards/request-bulk-setting-sim-card-public-ips)      |
| [Validate Registration Codes](https://developers.telnyx.com/api-reference/sim-cards/validate-sim-cards-registration-codes) |

Track progress via [List Bulk SIM Card Actions](https://developers.telnyx.com/api-reference/sim-card-actions/list-bulk-sim-card-actions). Per-SIM results are included — some may succeed while others fail.

  For bulk registration, validate codes first with the validation endpoint. This dry-run catches typos and invalid codes before you commit to a large batch.
