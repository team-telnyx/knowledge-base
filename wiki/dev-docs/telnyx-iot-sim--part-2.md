---
title: Telnyx IoT SIM
summary: Telnyx IoT SIMs provide global cellular connectivity for IoT devices with
  support for physical SIMs and eSIMs, fleet management through SIM Card Groups, private
  networking via Private Wireless Gateways, public static IPs, voice capabilities,
  and over-the-air updates. This page covers ordering, configuration, networking options,
  and device-specific setup guides.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/mikrotik-wap-lte
- url: https://developers.telnyx.com/docs/iot-sim/mobile-phone-numbers/index
- url: https://developers.telnyx.com/docs/iot-sim/nordic-semiconductor
- url: https://developers.telnyx.com/docs/iot-sim/ordering-sims/index
- url: https://developers.telnyx.com/docs/iot-sim/ota-updates
- url: https://developers.telnyx.com/docs/iot-sim/particle-boron-lte-kit
- url: https://developers.telnyx.com/docs/iot-sim/pepwave-max-br1-mini-lte
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to/index
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways
- url: https://developers.telnyx.com/docs/iot-sim/public-ips/index
- url: https://developers.telnyx.com/docs/iot-sim/sim-card-groups/index
updated_at: 2026-06-11T10:33:18Z
---

# Telnyx IoT SIM

*Part 2 of 3 — see also: [Part 1](telnyx-iot-sim--part-1.md), [Part 3](telnyx-iot-sim--part-3.md)*

Telnyx IoT SIMs provide global cellular connectivity for IoT devices with support for physical SIMs and eSIMs, fleet management through SIM Card Groups, private networking via Private Wireless Gateways, public static IPs, voice capabilities, and over-the-air updates. This page covers ordering, configuration, networking options, and device-specific setup guides.

## Mobile Phone Numbers and Voice

When you enable voice on a SIM, Telnyx assigns a Mobile Phone Number — a real +E.164 number. Inbound calls ring the device natively. Outbound calls show your number as caller ID. Voice is enabled per-SIM via action endpoints, not by patching a field.

### Voice Actions

| Action | Endpoint |
| --- | --- |
| Enable Voice | `POST /sim_cards/{id}/actions/enable_voice` |
| Disable Voice | `POST /sim_cards/{id}/actions/disable_voice` |
| Bulk Enable Voice | `POST /sim_cards/actions/bulk_enable_voice` |
| Bulk Disable Voice | `POST /sim_cards/actions/bulk_disable_voice` |

`enable_voice` accepts an optional `connection_id` to associate with a Mobile Voice Connection.

### Mobile Phone Number Management

| Action | Endpoint |
| --- | --- |
| List Numbers | `GET /mobile_phone_numbers` |
| Get Number | `GET /mobile_phone_numbers/{id}` |
| Update Number | `PATCH /mobile_phone_numbers/{id}` |

Configurable settings on a mobile phone number include:

| Setting | Description |
| --- | --- |
| `call_forwarding` | Forward calls on no-answer, busy, or unconditional |
| `call_recording` | Record inbound, outbound, or both |
| `caller_id_name_enabled` | Enable CNAM lookup on outbound calls |
| `cnam_listing` | Register business name for inbound CNAM display |
| `noise_suppression` | AI noise reduction on calls |
| `inbound_call_screening` | Filter inbound calls before connecting |
| `connection_id` | Associate with a Mobile Voice Connection |
| `customer_reference` | Your own reference string |
| `tags` | Arbitrary tags for filtering |
| `inbound` / `outbound` | Routing configuration per direction |

### Mobile Voice Connections

A Mobile Voice Connection is the voice application attached to a number — it controls webhooks, API version, and routing.

| Action | Endpoint |
| --- | --- |
| List Connections | `GET /mobile_voice_connections` |
| Create Connection | `POST /mobile_voice_connections` |
| Get Connection | `GET /mobile_voice_connections/{id}` |
| Update Connection | `PATCH /mobile_voice_connections/{id}` |
| Delete Connection | `DELETE /mobile_voice_connections/{id}` |

Connection settings include `webhook_event_url`, `webhook_event_failover_url`, `webhook_timeout_secs`, `outbound`/`inbound` routing, and `active` status.

## OTA Updates

OTA (Over-The-Air) updates let Telnyx push configuration changes to your SIMs remotely. No physical access is needed — updates are delivered to the SIM's on-card applet the next time the device connects.

OTA updates handle SIM-level configuration: IMSI profile switches, network preference changes, and applet settings. These are not firmware updates for the device itself — they modify the SIM card's internal state. The `type` field on each update indicates the operation source and what changed.

### Tracking OTA Updates

List updates with `GET /ota_updates` or check a specific update with `GET /ota_updates/{id}`. Each update includes:

| Field | Description |
| --- | --- |
| `sim_card_id` | Target SIM |
| `type` | Operation type — relates to the source of the request |
| `status` | Current state of the update |
| `settings` | JSON object with the specific changes applied |
| `created_at` | When the update was initiated |

### How OTA Updates Work

1. Telnyx queues the update for the target SIM.
2. The next time the device attaches to the network, the SIM's applet receives the update.
3. The update applies automatically. Status transitions from pending to complete (or failed).

There is no way to force immediate delivery — it depends on when the device next connects. For always-on devices this is near-instant; for devices that sleep or power cycle, it happens on next wake.

The most common OTA operation is IMSI profile switching. Telnyx SIMs carry multiple IMSIs, and the on-card applet auto-selects the best one per location. OTA updates can override this selection or push updated IMSI profiles when Telnyx adds new carrier partnerships.
