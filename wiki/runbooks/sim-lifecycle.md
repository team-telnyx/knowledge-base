---
title: SIM Lifecycle
summary: State machine, transitions, and what to know about managing SIM status.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle/index
    content_hash: 6e11a8a5c5a7a69a830fc7af2bd01b85b822dfe49ef10de2cf13b645778b005a
updated_at: 2026-04-10T00:00:00Z
---

# SIM Lifecycle

State machine, transitions, and what to know about managing SIM status.

Every SIM follows the same state machine regardless of type (physical or eSIM).

## Status

### User-Controlled

| Status     | On Network | Passes Traffic | Notes                                                |
| :--------- | :--------- | :------------- | :--------------------------------------------------- |
| `enabled`  | Yes        | Yes            | Active on the network.                               |
| `disabled` | No         | No             | Off the network. IP released. \$0.20/mo holding fee. |
| `standby`  | No         | No             | Off the network. IP preserved. \$0.20/mo.            |

  **`disabled` vs `standby`** — the only difference is IP preservation. If your application depends on a stable IP (e.g., firewall allowlists, IoT platforms that register by IP), use `standby`. Otherwise `disabled` is fine.

### Transitional

All transitions are asynchronous. While in progress, the SIM reports a transitional status.

| Status            | Target                      |
| :---------------- | :-------------------------- |
| `registering`     | → `enabled` (initial setup) |
| `enabling`        | → `enabled`                 |
| `disabling`       | → `disabled`                |
| `setting_standby` | → `standby`                 |

Track progress via [SIM Card Actions](https://developers.telnyx.com/api-reference/sim-card-actions/list-sim-card-actions).

> **Warning:** All state changes return `202` with a SIM Card Action — they are not instant. Poll the action status or list actions to confirm completion.

### System-Imposed

Set by Telnyx, not by API calls. The SIM cannot transition while in these states.

| Status                | Meaning                                                | How to Exit                                                                                                                                                                                                                                                                                  |
| :-------------------- | :----------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data_limit_exceeded` | SIM exceeded its group's data limit.                   | Raise the data limit via [`PATCH /sim_card_groups/{id}`](https://developers.telnyx.com/api-reference/sim-card-groups/update-a-sim-card-group) (group level) or [`PATCH /sim_cards/{id}`](https://developers.telnyx.com/api-reference/sim-cards/update-a-sim-card) (SIM level), or wait for billing cycle reset. Auto-transitions to `intended_status`. |
| `unauthorized_imei`   | SIM is in a device not on its `authorized_imeis` list. | Update `authorized_imeis` via [`PATCH /sim_cards/{id}`](https://developers.telnyx.com/api-reference/sim-cards/update-a-sim-card) to add the current IMEI or clear the list. Then re-enable with [`POST /sim_cards/{id}/actions/enable`](https://developers.telnyx.com/api-reference/sim-cards/request-a-sim-card-enable).                              |
| `blocked`             | Account-level service interruption (billing).          | Resolve account billing issue. Auto-syncs back to intended state.                                                                                                                                                                                                                            |
| `abolished`           | Account-level service interruption (billing).          | Resolve account billing issue. Auto-syncs back to intended state.                                                                                                                                                                                                                            |

## What Puts a SIM Into Each Status

> **Warning:** The SIM must have a `sim_card_group_id` before you can enable it or set it to standby.

| Target Status           | What Triggers It                                                                                                                                                                                        |
| :---------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `enabled`               | [Enable SIM](https://developers.telnyx.com/api-reference/sim-cards/request-a-sim-card-enable) — from `registered`, `disabled`, or `standby`                                                                                          |
| `disabled`              | [Disable SIM](https://developers.telnyx.com/api-reference/sim-cards/request-a-sim-card-disable) — from `enabled`                                                                                                                     |
| `standby`               | [Set Standby](https://developers.telnyx.com/api-reference/sim-cards/request-setting-a-sim-card-to-standby) — from `enabled`                                                                                                          |
| `data_limit_exceeded`   | System — SIM exceeded its group or SIM-level data limit. Adjust via [Update Group](https://developers.telnyx.com/api-reference/sim-card-groups/update-a-sim-card-group) or [Update SIM](https://developers.telnyx.com/api-reference/sim-cards/update-a-sim-card). |
| `unauthorized_imei`     | System — SIM inserted into a device not in its `authorized_imeis` list. Fix via [Update SIM](https://developers.telnyx.com/api-reference/sim-cards/update-a-sim-card).                                                               |
| `blocked` / `abolished` | System — account-level billing interruption. Resolve with Telnyx support.                                                                                                                               |

## Deletion

[`DELETE /sim_cards/{id}`](https://developers.telnyx.com/api-reference/sim-cards/deletes-a-sim-card) permanently deregisters the SIM. This is irreversible:

* **Physical SIMs** — the plastic is now waste. You'd need to order and register a new one.
* **eSIMs** — the profile is gone. You'd need to purchase a new eSIM.

Prefer disable or standby if there's any chance you'll need the SIM again.

> **Warning:** For eSIMs that can't be uninstalled from a device, pass `report_lost=true` — this is irreversible and the eSIM cannot be re-registered.


## Related Pages

- [Lifecycle](../runbooks/lifecycle.md)
- [Lifecycle](../runbooks/lifecycle-2.md)
