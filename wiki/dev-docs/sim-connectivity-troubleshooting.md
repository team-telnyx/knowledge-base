---
title: SIM Connectivity Troubleshooting
summary: A step-by-step guide for diagnosing and resolving SIM connectivity issues
  on the Telnyx IoT network, covering device configuration, connectivity log inspection,
  and common failure patterns.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/connectivity-troubleshooting/index
updated_at: 2026-08-05T13:46:40Z
---

# SIM Connectivity Troubleshooting

A step-by-step guide for diagnosing and resolving SIM connectivity issues on the Telnyx IoT network, covering device configuration, connectivity log inspection, and common failure patterns.

## Step 1: Check device configuration

1. Enable cellular data.
2. Set the network to 3G/LTE or 4G/LTE only. Note that the first registration requires at least 3G.
3. Enable roaming.
4. Set the APN with **Name:** `Telnyx` and **APN:** `data00.telnyx`. Leave all other fields blank.
5. Update firmware, then reboot the device.

APN configuration locations:
- **Android:** Settings → Mobile Networks → Access Point Names → Add
- **iOS:** Settings → Cellular → Mobile Data → APN

## Step 2: Check connectivity logs

Connectivity logs can be inspected in the [Mission Control Portal](https://portal.telnyx.com/#/app/wireless/sim-cards) by selecting a SIM ICCID and opening the Connectivity Logs tab, or retrieved programmatically via the API:

```
GET /sim_cards/{id}/wireless_connectivity_logs
```

The `type` column indicates whether each entry is a `Registration` or `Data` event. The MCC identifies the country and the MNC identifies the carrier.

## Step 3: Diagnose patterns

### No connectivity logs at all

If no connectivity logs are appearing, the connection is not reaching Telnyx. Possible causes include the device being on a network Telnyx cannot access, a misconfigured device, or a deactivated SIM.

**Fix:** Scan available networks and manually select one. Verify the device configuration from Step 1. Check the SIM status in the portal — the SIM may be disabled due to a data limit or billing issue.

### Multiple registration attempts, no data

If the SIM is registering repeatedly but never authenticating, the SIM is not authenticating successfully.

**Fix:** Enable data roaming. Verify the APN is set to `data00.telnyx`.

### Registration succeeds but no data sessions

If registration completes but no data sessions are created, data sessions are not being established.

**Fix:** Enable data roaming. Verify the APN is set to `data00.telnyx`.

If issues persist after following these steps, contact support via the Mission Control Portal.
