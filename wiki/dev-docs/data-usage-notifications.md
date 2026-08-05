---
title: Data Usage Notifications
summary: Configure data limits and per-SIM usage notifications for IoT SIM cards,
  and monitor consumption across groups and individual SIMs via the Telnyx API.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/data-usage-notifications
updated_at: 2026-08-05T13:46:43Z
---

# Data Usage Notifications

Configure data limits and per-SIM usage notifications for IoT SIM cards, and monitor consumption across groups and individual SIMs via the Telnyx API.

## Data Limits

Limits can be set at two levels:

| Level | Set Via | Scope |
| --- | --- | --- |
| **Group** | `PATCH /sim_card_groups/{id}` | All SIMs in the group share the limit. SIMs exceeding it enter `data_limit_exceeded`. Resets monthly. |
| **SIM** | `PATCH /sim_cards/{id}` | Per-SIM `data_limit` override. |

## Per-SIM Usage Notifications

Set a threshold on individual SIMs to get notified before they hit their limit.

| Action | Endpoint |
| --- | --- |
| List Notifications | `GET /sim_card_data_usage_notifications` |
| Create Notification | `POST /sim_card_data_usage_notifications` |
| Get Notification | `GET /sim_card_data_usage_notifications/{id}` |
| Update Notification | `PATCH /sim_card_data_usage_notifications/{id}` |
| Delete Notification | `DELETE /sim_card_data_usage_notifications/{id}` |

## Monitoring Consumption

- **Per group** — `GET /sim_card_groups/{id}` returns `consumed_data`.
- **Per SIM** — visible in the SIM card detail response.
- **Portal** — Settings page shows real-time consumption per group.
