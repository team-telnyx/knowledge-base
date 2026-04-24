---
title: SIM Connectivity Troubleshooting
summary: 'Troubleshooting SIM connectivity issues including APN configuration for Android and iOS.'
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/connectivity-troubleshooting/index
    content_hash: a38cd2860bc0d5cf08584b3eff0d0372b06771dc5266821362ecc47aefe33490
updated_at: 2026-04-10T00:00:00Z
---

# SIM Connectivity Troubleshooting

## Step 1: Check device configuration

1. Enable cellular data
2. Set network to 3G/LTE or 4G/LTE only (first registration requires at least 3G)
3. Enable roaming
4. Set APN: **Name:** `Telnyx` **APN:** `data00.telnyx` (leave all other fields blank)
5. Update firmware, then reboot

**Android:** Settings → Mobile Networks → Access Point Names → Add

**iOS:** Settings → Cellular → Mobile Data → APN

## Step 2: Check connectivity logs

View logs via [portal](https://portal.telnyx.com/#/app/wireless/sim-cards) (click SIM ICCID → Connectivity Logs) or API:

```
GET /sim_cards/{id}/wireless_connectivity_logs
```

The `type` column shows `Registration` or `Data`. MCC identifies the country, MNC identifies the carrier.

## Step 3: Diagnose patterns

### No connectivity logs at all

* Connection isn't reaching Telnyx. Device may be on a network Telnyx can't access, misconfigured, or SIM is deactivated.
* **Fix:** Scan networks and manually select one. Verify device config (Step 1). Check SIM status in portal — may be disabled due to data limit or billing.

### Multiple registration attempts, no data

* SIM isn't authenticating.
* **Fix:** Enable data roaming. Verify APN is `data00.telnyx`.

### Registration succeeds but no data sessions

* Data sessions not being created.
* **Fix:** Enable data roaming. Verify APN is `data00.telnyx`.

If issues persist, contact support via the Mission Control Portal.


## Related Pages

- [Troubleshooting](../reference/troubleshooting.md)
- [Troubleshooting](../reference/troubleshooting-2.md)
