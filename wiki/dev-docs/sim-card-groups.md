---
title: SIM Card Groups
summary: SIM Card Groups let you apply ongoing policy to a collection of SIMs. Every
  SIM belongs to a group and inherits its settings, so you manage policy at the group
  level rather than updating SIMs individually.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/sim-card-groups/index
updated_at: 2026-08-05T13:47:11Z
---

# SIM Card Groups

SIM Card Groups let you apply ongoing policy to a collection of SIMs. Every SIM belongs to a group and inherits its settings, so you manage policy at the group level rather than updating SIMs individually.

## Overview

Every SIM belongs to a group and inherits its settings. Set policy on the group instead of updating SIMs individually.

Groups are ongoing policy: a SIM inherits its group's settings as long as it is a member. This is distinct from bulk operations, which are one-time actions on an explicit list of SIMs.

## Default Group

Every account has a default group. SIMs that are not explicitly assigned to another group land in the default group. Deleting a group moves its member SIMs back to the default group. Moving SIMs between groups after they are active can briefly interrupt connectivity.

## Group Settings

Group settings are configurable via [`PATCH /sim_card_groups/{id}`](/api-reference/sim-card-groups/update-a-sim-card-group).

| Setting | Description |
| --- | --- |
| `name` | Display name for the group. |
| `data_limit` | Data cap (`amount` + `unit`). SIMs exceeding this enter `data_limit_exceeded` until the limit is raised or the billing cycle resets. |

## Group Actions

Group actions are asynchronous. Each action returns an action ID, and progress can be tracked via [`GET /sim_card_group_actions`](/api-reference/sim-card-group-actions/list-sim-card-group-actions).

Available actions:

- [Assign Private Wireless Gateway](/api-reference/sim-card-groups/request-private-wireless-gateway-assignment-for-sim-card-group)
- [Remove Private Wireless Gateway](/api-reference/sim-card-groups/request-private-wireless-gateway-removal-from-sim-card-group)
- [Assign Wireless Blocklist](/api-reference/sim-card-groups/request-wireless-blocklist-assignment-for-sim-card-group)
- [Remove Wireless Blocklist](/api-reference/sim-card-groups/request-wireless-blocklist-removal-from-sim-card-group)
