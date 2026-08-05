---
title: Wireless Detail Records
summary: Wireless Detail Records (WDRs) provide granular, per-session usage data for
  a SIM fleet, capturing details such as session timing, bytes transferred, and the
  network used. Reports are generated asynchronously and can be combined with real-time
  connectivity logs for troubleshooting and analysis.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records
updated_at: 2026-08-05T13:47:25Z
---

# Wireless Detail Records

Wireless Detail Records (WDRs) provide granular, per-session usage data for a SIM fleet, capturing details such as session timing, bytes transferred, and the network used. Reports are generated asynchronously and can be combined with real-time connectivity logs for troubleshooting and analysis.

## Generating Reports

WDR reports are generated asynchronously. The workflow is to request a report, poll for completion, and then download the result.

1. **Create** — `POST /wireless/detail/records/reports` with a time range:

   ```json
   {
     "start_time": "2026-04-01T00:00:00Z",
     "end_time": "2026-04-07T00:00:00Z"
   }
   ```
2. **Poll** — `GET /wireless/detail/records/reports/{id}` until `status` is `complete`.
3. **Download** — The `report_url` field contains a pre-signed URL to the report file.

## What's in a Report

Each record captures a single data session and includes the following fields:

| Field | Description |
| --- | --- |
| `sim_card_id` | Which SIM |
| `start_time` / `stop_time` | Session duration |
| `radio_access_technology` | LTE, 3G, etc. |
| `mobile_country_code` + `mobile_network_code` | Which carrier |
| `apn` | Access Point Name used |
| `ipv4` / `ipv6` | IP assigned during session |
| `cell_id` | Cell tower |

## Connectivity Logs

For real-time session visibility rather than batch reports, use connectivity logs:

`GET /sim_cards/{id}/wireless_connectivity_logs`

This endpoint returns recent sessions for a specific SIM, including IMSI, IMEI, radio technology, and connection state. It is useful for debugging why a device cannot connect or which network it attached to.

## Use Cases

- **Billing reconciliation** — match data usage against invoices.
- **Anomaly detection** — spot SIMs consuming unexpected data volumes.
- **Coverage analysis** — see which carriers devices attach to by region.
- **Troubleshooting** — correlate connectivity issues with specific cells or networks.
