---
title: SIM Card Groups
summary: Group-level configuration and policy for SIM cards.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/sim-card-groups/index
    content_hash: 879502e94ced60995c665656527b398127fbb94f060ba7fe245ae433d5d9c8b4
updated_at: 2026-04-10T00:00:00Z
---

# SIM Card Groups

Group-level configuration and policy for SIM cards.

> **Warning:** **Groups vs Bulk Operations** — Groups are ongoing policy; a SIM inherits its group's settings as long as it's a member. Bulk operations are one-time actions on an explicit list of SIMs.

Every SIM belongs to a group and inherits its settings. Set policy on the group instead of updating SIMs individually.

## Default Group

Every account has a default group. SIMs that aren't explicitly assigned land here. Deleting a group moves its SIMs back to default. Moving SIMs between groups after they're active can briefly interrupt connectivity.

## Group Settings

Configurable via [`PATCH /sim_card_groups/{id}`](https://developers.telnyx.com/api-reference/sim-card-groups/update-a-sim-card-group):

| Setting      | Description                                                                                                                          |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `name`       | Display name for the group.                                                                                                          |
| `data_limit` | Data cap (`amount` + `unit`). SIMs exceeding this enter `data_limit_exceeded` until the limit is raised or the billing cycle resets. |

## Group Actions

These are async — each returns an action ID. Track progress via [`GET /sim_card_group_actions`](https://developers.telnyx.com/api-reference/sim-card-group-actions/list-sim-card-group-actions).

| Action                                                                                                                           |
| :------------------------------------------------------------------------------------------------------------------------------- |
| [Assign Private Wireless Gateway](https://developers.telnyx.com/api-reference/sim-card-groups/request-private-wireless-gateway-assignment-for-sim-card-group) |
| [Remove Private Wireless Gateway](https://developers.telnyx.com/api-reference/sim-card-groups/request-private-wireless-gateway-removal-from-sim-card-group)   |
| [Assign Wireless Blocklist](https://developers.telnyx.com/api-reference/sim-card-groups/request-wireless-blocklist-assignment-for-sim-card-group)             |
| [Remove Wireless Blocklist](https://developers.telnyx.com/api-reference/sim-card-groups/request-wireless-blocklist-removal-from-sim-card-group)               |


## Related Pages

- [SIM Cards](../runbooks/sim-cards.md)
- [Insight Groups](../runbooks/insight-groups.md)
