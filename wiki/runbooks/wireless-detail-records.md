---
title: Wireless Detail Records
summary: Export per-session data usage records for billing, auditing, and troubleshooting.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records/index
    content_hash: 8c076529f1f1b33e5007195c2e831d0382f7d56e82d0470473c7db0ab1bdf8da
updated_at: 2026-04-10T00:00:00Z
---

# Wireless Detail Records

Export per-session data usage records for billing, auditing, and troubleshooting.

Wireless Detail Records (WDRs) provide granular, per-session usage data for your SIM fleet. Each record captures a single data session — when it started, how long it lasted, bytes transferred, and which network was used.

## Generating Reports

WDR reports are async. Request one, poll for completion, download when ready.

1. **Create** — `POST /wireless/detail/records/reports` with a time range:
   ```json theme={null}
   {
     "start_time": "2026-04-01T00:00:00Z",
     "end_time": "2026-04-07T00:00:00Z"
   }
   ```

2. **Poll** — `GET /wireless/detail/records/reports/{id}` until `status` is `complete`.

3. **Download** — The `report_url` field contains a pre-signed URL to the report file.

## What's in a Report

Each record includes:

| Field                                         | Description                |
| :-------------------------------------------- | :------------------------- |
| `sim_card_id`                                 | Which SIM                  |
| `start_time` / `stop_time`                    | Session duration           |
| `radio_access_technology`                     | LTE, 3G, etc.              |
| `mobile_country_code` + `mobile_network_code` | Which carrier              |
| `apn`                                         | Access Point Name used     |
| `ipv4` / `ipv6`                               | IP assigned during session |
| `cell_id`                                     | Cell tower                 |

## Connectivity Logs

For real-time session visibility (not batch reports), use connectivity logs:

`GET /sim_cards/{id}/wireless_connectivity_logs`

Returns recent sessions for a specific SIM, including IMSI, IMEI, radio technology, and connection state. Useful for debugging why a device can't connect or which network it attached to.

## Use Cases

* **Billing reconciliation** — match data usage against your invoices
* **Anomaly detection** — spot SIMs consuming unexpected data volumes
* **Coverage analysis** — see which carriers your devices attach to by region
* **Troubleshooting** — correlate connectivity issues with specific cells or networks


## Related Pages

- [Message Detail Records](../runbooks/message-detail-records.md)
- [WebRTC Voice SDKs Call Detail Records](../runbooks/webrtc-voice-sdks-call-detail-records.md)
