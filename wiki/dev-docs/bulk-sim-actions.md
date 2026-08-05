---
title: Bulk SIM Actions
summary: Bulk actions are one-time, asynchronous operations applied to an explicit
  list of SIM IDs. They differ from Groups, which provide ongoing policy for current
  and future SIMs. Submit a list of SIMs, receive an action ID, and poll for status
  to track per-SIM results.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/bulk-sim-actions/index
updated_at: 2026-08-05T13:46:35Z
---

# Bulk SIM Actions

Bulk actions are one-time, asynchronous operations applied to an explicit list of SIM IDs. They differ from Groups, which provide ongoing policy for current and future SIMs. Submit a list of SIMs, receive an action ID, and poll for status to track per-SIM results.

## Overview

Bulk actions are one-time operations on an explicit list of SIM IDs. Nothing persists after the action completes. For ongoing policy that applies to current and future SIMs, use [SIM Card Groups](sim-card-groups.md) instead.

All bulk actions are asynchronous: submit a list of SIM IDs, receive an action ID back, and poll for status to track progress.

## Available Actions

- [Bulk Enable Voice](https://developers.telnyx.com/api-reference/sim-cards/request-bulk-enabling-voice-on-sim-cards)
- [Bulk Disable Voice](https://developers.telnyx.com/api-reference/sim-cards/request-bulk-disabling-voice-on-sim-cards)
- [Bulk Set Public IPs](https://developers.telnyx.com/api-reference/sim-cards/request-bulk-setting-sim-card-public-ips)
- [Validate Registration Codes](https://developers.telnyx.com/api-reference/sim-cards/validate-sim-cards-registration-codes)

## Tracking Progress

Track the progress of bulk operations via the [List Bulk SIM Card Actions](https://developers.telnyx.com/api-reference/sim-card-actions/list-bulk-sim-card-actions) endpoint. Per-SIM results are included in the response, so some SIMs may succeed while others fail within the same batch.

## Registration Workflow

For bulk registration, validate codes first using the validation endpoint. This dry-run catches typos and invalid codes before committing to a large batch.
