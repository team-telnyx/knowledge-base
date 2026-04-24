---
title: Data Usage Notifications
summary: Set per-SIM usage thresholds and get notified when SIMs approach their limits.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/data-usage-notifications/index
    content_hash: fa8ae226791f5615579706dd9f75dde48930fb117e6e85bbeb76b7f22cbe3d2c
updated_at: 2026-04-10T00:00:00Z
---

# Data Usage Notifications

Set per-SIM usage thresholds and get notified when SIMs approach their limits.

## Data Limits

Limits can be set at two levels:

| Level     | Set Via                                                                                 | Scope                                                                                                 |
| :-------- | :-------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **Group** | [`PATCH /sim_card_groups/{id}`](https://developers.telnyx.com/api-reference/sim-card-groups/update-a-sim-card-group) | All SIMs in the group share the limit. SIMs exceeding it enter `data_limit_exceeded`. Resets monthly. |
| **SIM**   | [`PATCH /sim_cards/{id}`](https://developers.telnyx.com/api-reference/sim-cards/update-a-sim-card)                   | Per-SIM `data_limit` override.                                                                        |

## Per-SIM Usage Notifications

Set a threshold on individual SIMs to get notified before they hit their limit.

| Action                                                                                                     | Endpoint                                         |
| :--------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
| [List Notifications](https://developers.telnyx.com/api-reference/sim-cards/list-sim-card-data-usage-notifications)                      | `GET /sim_card_data_usage_notifications`         |
| [Create Notification](https://developers.telnyx.com/api-reference/sim-cards/create-a-new-sim-card-data-usage-notification)              | `POST /sim_card_data_usage_notifications`        |
| [Get Notification](https://developers.telnyx.com/api-reference/sim-cards/get-a-single-sim-card-data-usage-notification)                 | `GET /sim_card_data_usage_notifications/{id}`    |
| [Update Notification](https://developers.telnyx.com/api-reference/sim-cards/updates-information-for-a-sim-card-data-usage-notification) | `PATCH /sim_card_data_usage_notifications/{id}`  |
| [Delete Notification](https://developers.telnyx.com/api-reference/sim-cards/delete-sim-card-data-usage-notifications)                   | `DELETE /sim_card_data_usage_notifications/{id}` |

## Monitoring Consumption

* **Per group** — `GET /sim_card_groups/{id}` returns `consumed_data`.
* **Per SIM** — visible in the SIM card detail response.
* **Portal** — Settings page shows real-time consumption per group.


## Related Pages

- [iOS Push Notifications](../runbooks/ios-push-notifications.md)
- [Android Push Notifications](../runbooks/android-push-notifications.md)
- [Flutter Push Notifications](../runbooks/flutter-push-notifications.md)
- [React Native Push Notifications](../runbooks/react-native-push-notifications.md)
- [10DLC event notifications](../runbooks/10dlc-event-notifications.md)
