---
title: Number Reputation
summary: Monitor and manage the spam reputation of your outbound calling phone numbers with Telnyx Number Reputation.
sources:
  - url: https://developers.telnyx.com/docs/branded-calling/number-reputation/index
    content_hash: 9e431eabd40a13ea96ff70bec215c43fa2914dd5ea8768555e7d60a3cbcd6362
updated_at: 2026-04-10T00:00:00Z
---

# Number Reputation

Monitor and manage the spam reputation of your outbound calling phone numbers with Telnyx Number Reputation.

## Overview

**Number Reputation** gives you programmatic access to spam reputation data for your outbound calling phone numbers. Instead of guessing why calls get flagged as "Spam Likely," you get real-time scores and risk levels — letting you identify and fix flagged numbers before they impact your answer rates.

| Without Number Reputation   | With Number Reputation                     |
| :-------------------------- | :----------------------------------------- |
| Calls flagged "Spam Likely" | Spam risk level: `low` / `medium` / `high` |
| No visibility into *why*    | 4 granular scores (0–100)                  |
| Manual checking             | Automated monitoring on a schedule         |
| No historical tracking      | `last_refreshed_at` timestamps             |

Reputation data is powered by **Hiya** — AT\&T's primary spam analytics partner and the engine behind AT\&T ActiveArmor. When you register numbers, Hiya registers them across all three major analytics engines (Hiya, First Orion, TNS).

## How it works

1. **Register your business** as an [Enterprise](https://developers.telnyx.com/docs/branded-calling/enterprises/overview)
2. **Upload a signed LOA** (Letter of Authorization) via the Documents API
3. **Enable Number Reputation** — your details are sent to Hiya for automated vetting (takes minutes)
4. **Associate phone numbers** for monitoring (up to 100 per request, US local, E.164)
5. **Query reputation scores** — cached results are free, fresh (live) queries are billed
6. **Automatic monitoring** re-checks your numbers on a configurable schedule

No changes to your call control integration are required. Number Reputation is a standalone monitoring product.

## Constraints

| Constraint          | Limit                                       |
| :------------------ | :------------------------------------------ |
| Phone number format | E.164, US local numbers only                |
| Numbers per request | 100 (atomic — all-or-nothing)               |
| Score range         | 0–100 (`null` = insufficient data)          |
| Account access      | Verified and enterprise-level accounts only |


## Related Pages

- [Phone Number Reputation](../runbooks/phone-number-reputation.md)
- [Number Reputation Settings](../runbooks/number-reputation-settings.md)
- [Number Reservations](../runbooks/number-reservations.md)
- [Number Reputation Quickstart](../tutorial/number-reputation-quickstart.md)
- [Number Pool](../runbooks/number-pool.md)
