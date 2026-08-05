---
title: OTA Updates
summary: OTA (Over-The-Air) updates let Telnyx push configuration changes to your
  SIMs remotely. No physical access is needed — updates are delivered to the SIM's
  on-card applet the next time the device connects to the network.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/ota-updates
updated_at: 2026-08-05T13:47:01Z
---

# OTA Updates

OTA (Over-The-Air) updates let Telnyx push configuration changes to your SIMs remotely. No physical access is needed — updates are delivered to the SIM's on-card applet the next time the device connects to the network.

## What Gets Updated

OTA updates handle SIM-level configuration: IMSI profile switches, network preference changes, and applet settings. These are not firmware updates for the device itself — they modify the SIM card's internal state.

The `type` field on each update indicates the operation source and what changed.

## Tracking Updates

List updates for your fleet:

```
GET /ota_updates
```

Or check a specific update:

```
GET /ota_updates/{id}
```

Each update includes:

| Field | Description |
| --- | --- |
| `sim_card_id` | Target SIM |
| `type` | Operation type — relates to the source of the request |
| `status` | Current state of the update |
| `settings` | JSON object with the specific changes applied |
| `created_at` | When the update was initiated |

## How It Works

1. Telnyx queues the update for the target SIM.
2. The next time the device attaches to the network, the SIM's applet receives the update.
3. The update applies automatically. Status transitions from pending to complete (or failed).

There's no way to force immediate delivery — it depends on when the device next connects. For always-on devices this is near-instant. For devices that sleep or power cycle, it happens on next wake.

## Multi-IMSI Context

The most common OTA operation is IMSI profile switching. Telnyx SIMs carry multiple IMSIs, and the on-card applet auto-selects the best one per location. OTA updates can override this selection or push updated IMSI profiles when Telnyx adds new carrier partnerships.
