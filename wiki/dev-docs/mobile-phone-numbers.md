---
title: Mobile Phone Numbers
summary: When voice is enabled on a Telnyx SIM, the device is assigned a real +E.164
  Mobile Phone Number that handles inbound and outbound calls natively. This page
  covers enabling voice per-SIM, managing the assigned number, and configuring the
  associated Mobile Voice Connection.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/mobile-phone-numbers/index
updated_at: 2026-08-05T13:46:57Z
---

# Mobile Phone Numbers

When voice is enabled on a Telnyx SIM, the device is assigned a real +E.164 Mobile Phone Number that handles inbound and outbound calls natively. This page covers enabling voice per-SIM, managing the assigned number, and configuring the associated Mobile Voice Connection.

## Overview

When you enable voice on a SIM, Telnyx assigns a Mobile Phone Number — a real +E.164 number. Inbound calls ring the device natively, and outbound calls show your number as the caller ID.

## Enabling Voice

Voice is enabled per-SIM via action endpoints rather than by patching a field directly.

| Action | Endpoint |
| --- | --- |
| Enable Voice | `POST /sim_cards/{id}/actions/enable_voice` |
| Disable Voice | `POST /sim_cards/{id}/actions/disable_voice` |
| Bulk Enable Voice | `POST /sim_cards/actions/bulk_enable_voice` |
| Bulk Disable Voice | `POST /sim_cards/actions/bulk_disable_voice` |

The `enable_voice` action accepts an optional `connection_id` parameter to associate the SIM with a [Mobile Voice Connection](mobile-voice-connection.md).

## Mobile Phone Number

Once voice is enabled, the assigned number can be managed through the Mobile Phone Numbers API.

| Action | Endpoint |
| --- | --- |
| List Numbers | `GET /mobile_phone_numbers` |
| Get Number | `GET /mobile_phone_numbers/{id}` |
| Update Number | `PATCH /mobile_phone_numbers/{id}` |

### Configurable Settings

| Setting | Description |
| --- | --- |
| `call_forwarding` | Forward calls on no-answer, busy, or unconditional |
| `call_recording` | Record inbound, outbound, or both |
| `caller_id_name_enabled` | Enable CNAM lookup on outbound calls |
| `cnam_listing` | Register business name for inbound CNAM display |
| `noise_suppression` | AI noise reduction on calls |
| `inbound_call_screening` | Filter inbound calls before connecting |
| `connection_id` | Associate with a [Mobile Voice Connection](mobile-voice-connection.md) |
| `customer_reference` | Your own reference string |
| `tags` | Arbitrary tags for filtering |
| `inbound` / `outbound` | Routing configuration per direction |

## Mobile Voice Connection

The Mobile Voice Connection is the voice application attached to a number. It controls webhooks, API version, and routing behavior.

| Action | Endpoint |
| --- | --- |
| List Connections | `GET /mobile_voice_connections` |
| Create Connection | `POST /mobile_voice_connections` |
| Get Connection | `GET /mobile_voice_connections/{id}` |
| Update Connection | `PATCH /mobile_voice_connections/{id}` |
| Delete Connection | `DELETE /mobile_voice_connections/{id}` |

### Connection Settings

| Setting | Description |
| --- | --- |
| `webhook_event_url` | Where call events are sent |
| `webhook_event_failover_url` | Backup URL if the primary fails |
| `webhook_timeout_secs` | How long to wait for a webhook response |
| `outbound` / `inbound` | Routing configuration per direction |
| `active` | Whether the connection is active |
