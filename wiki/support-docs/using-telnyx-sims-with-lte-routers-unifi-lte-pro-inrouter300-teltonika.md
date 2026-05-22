---
title: Using Telnyx SIMs with LTE Routers (UniFi LTE Pro, InRouter300, Teltonika)
summary: A consolidated setup and operations guide for using Telnyx IoT SIMs across
  popular LTE routers from Ubiquiti, InHand InRouter300, and Teltonika—covering APN
  configuration, verification, troubleshooting, monitoring, coverage, and pricing
  essentials.
sources:
- url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
  content_hash: 80ae14fa87e193de71eefc36d42498ab4fbdc7fa42707e6fab2fe8e566b760aa
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
  content_hash: 2633418286f8bf05c620e3db4dd0e3a092a7f50b170c21b60cd604ce8c627d14
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
  content_hash: df6aa05f81cac2ebcc9609fb2cd5de07b6283e7de1d6b7b750314ec2884b33f9
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
  content_hash: 104e2765e043c96022b6893a0e1ae0e0a796ce2395df3b4bb79de353a4b613fd
- url: https://support.telnyx.com/en/articles/3270106-international-iot-sim-coverage
  content_hash: d5728028063f1e58d322010a5154a6b5a81cccc32d0e31a33efa844d245c1a85
- url: https://support.telnyx.com/en/articles/3371977-international-roaming-partners
  content_hash: 0a20d7b82336a97c0251f9295f2eb32ee421e75be07c302774bba14381baf185
- url: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing
  content_hash: 8f335cfae2e8e73f7d926179e3baf432d7865f7091141cc4131a717ddeb3f13e
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
  content_hash: fe8ac3fdb3b7feef214e77f30024e0c99b2a028939fc00d88338207644155bdb
- url: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics
  content_hash: 87353ad196a844c5937e776dd27b499ed00036843b49c2582bdf1a48da4575bf
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
  content_hash: 4ef9732651ee85a65af0acfea4abb65ef58e8f6b565b0513c0504a092517a0f5
- url: https://support.telnyx.com/en/articles/7966416-telnyx-iot-sim-data-usage-zone-mapping
  content_hash: a73ece498fa9586c87cf3b947a236d5a6c8c3b9d0a5f539d7d00cf272601ad7b
updated_at: 2026-05-20T15:27:54Z
---

# Using Telnyx SIMs with LTE Routers (UniFi LTE Pro, InRouter300, Teltonika)

A consolidated setup and operations guide for using Telnyx IoT SIMs across popular LTE routers from Ubiquiti, InHand InRouter300, and Teltonika—covering APN configuration, verification, troubleshooting, monitoring, coverage, and pricing essentials.

## Overview and Required APN

- Telnyx APN: data00.telnyx
- Authentication: None (leave username/password blank)
- Enable data roaming on the device
- First attach on a new SIM/network can take up to 30 minutes
- Keep SIMs enabled and within data limits to avoid auto-disable events (see [SIM Data Limits & Notifications](sim-data-limits-notifications.md))
- For general SIM prep, see [How to set up a Telnyx SIM Card](how-to-set-up-a-telnyx-sim-card.md) and [SIM Setup and Configuration](sim-setup-and-configuration.md)

## Ubiquiti UniFi LTE Pro Setup

- Insert the Telnyx Nano SIM into the UniFi LTE Pro
- Power via PoE (802.3af) Ubiquiti switch
- Log in at https://unifi.ui.com and adopt the LTE Pro in your console
- Go to Settings > Internet > LTE Backup > Settings and set:
  - APN: data00.telnyx
  - Authentication Type: None
- Apply settings, then in Overview confirm Status: Ready and Connected: Yes
- If the device restarts or is re-provisioned and enters SIM-Activation mode, enable modem autoconnect via CLI: qmicli -p -d /dev/cdc-wdm0 --wds-set-autoconnect-settings=enabled
- Note: First-time network attachment may take up to 30 minutes
- Full walkthrough: [Using Telnyx SIM with Ubiquiti UniFi LTE Pro](using-telnyx-sim-with-ubiquiti-unifi-lte-pro.md)

## InRouter300 Series Setup

Prerequisites: IR300 (e.g., IR302), active Telnyx SIM, Ethernet-connected computer, power adapter

- Connect to the router at http://192.168.2.1
  - Default credentials: Username adm, Password 123456 (unless changed)
- Navigate Network > Cellular > SIM Profiles
  - Select the SIM slot in use and set APN: data00.telnyx (leave user/pass blank)
  - Apply
- Optional dual-SIM redundancy: enable Dual SIM Mode, configure carrier APN for SIM 2, and set Failover Mode
- Verify at Status > Network Connection for IP address, signal, and registration
- Optional features:
  - Static IP (if provisioned by Telnyx): Network > WAN Settings > Static IP
  - VPN (IPSec/OpenVPN/PPTP): VPN > Settings
  - Firewall: Security > Firewall
  - Backup/restore: System > Config Management (export/import .dat)
- Troubleshooting: confirm SIM active, APN correct, reboot, and test SIM in another device
- Full walkthrough: [Using Telnyx SIM with InRouter300 Series Cellular Routers](using-telnyx-sim-with-inrouter300-series-cellular-routers.md)

## Teltonika LTE Routers Setup

- Connect to the router at http://192.168.2.1
  - Default login: Username admin, Password on the device label (change when prompted)
- Network > Interfaces
  - Edit mobile interface (e.g., mob1s1a1)
  - Uncheck Auto APN, set APN: data00.telnyx (leave user/pass blank)
  - Save & Apply
- Verify at Status > Network Information (Connected, IP assigned, signal OK)
- Recommended resilience: System > Auto Reboot
  - Enable watchdog, select Ping Reboot, targets like 8.8.8.8 and 1.1.1.1, set interval/retries; optionally schedule reboots
- Fleet operations: enroll devices in Teltonika RMS (System > RMS) for monitoring, bulk config, remote CLI, VPN, and alerts
- Keep firmware current (System > Firmware); configure firewall (Network > Firewall) and VPN as needed
- Backup: System > Backup
- Full walkthrough: [Using Telnyx SIM with Teltonika 4G/LTE Routers](using-telnyx-sim-with-teltonika-4g-lte-routers.md)

## Verify and Test Connectivity

- Confirm the router has an IP from the Telnyx network and good signal strength
- Validate reachability by opening a website or pinging external DNS (e.g., 8.8.8.8)
- For detailed SIM session visibility, use [SIM Reporting & Analytics](sim-reporting-analytics.md) and [SIM Connectivity Logs](sim-connectivity-logs.md)

## First-Time Attachment and Re-Provisioning Notes

- New SIMs and new geographies may require up to 30 minutes for the first network attach
- After successful attach, subsequent connections are faster as preferred operators are learned
- If UniFi LTE Pro reverts to SIM-Activation mode after a restart, re-enable modem autoconnect (see command above)

## Troubleshoot with Telnyx Connectivity Logs

Use [SIM Connectivity Logs](sim-connectivity-logs.md) in Portal or API to inspect two log types:
- Registration logs: show network authentication attempts
- Data logs: show data session creation/usage

Common patterns and fixes:
- No logs: signaling not reaching Telnyx core — contact support
- Many registrations but no data logs: usually roaming disabled or APN misconfigured (must be data00.telnyx)
- No data logs: enable roaming and re-check APN; reboot device
- Errors: device may be trying non-partner networks, SIM disabled, or roaming off. Run a manual network scan to select a supported operator, enable roaming, and verify SIM state and data limits in Mission Control
- MCC/MNC codes in logs identify country and operator; see public mappings if needed (https://en.wikipedia.org/wiki/Mobile_country_code)

## Understand Connectivity States (API)

When querying the Wireless Connectivity Logs API, sessions progress through states such as:
- Attached: SIM successfully registered and assigned IP
- Opened: data session begins (after attach)
- Closed: data session ended (e.g., loss of coverage, device turned off, Wi‑Fi switchover, intentional stop)
- Provisioned: SIM is newly provisioned and has not yet attached (also seen after certain SIM group changes)

A healthy cycle is typically: Attached → Opened → Closed. For details, see [Understanding Wireless Connectivity States (Telnyx API)](understanding-wireless-connectivity-states-telnyx-api.md).

## Monitor Usage and Get Alerts

- WDRs (Wireless Detail Records) are available in Portal reporting and via API; fields include timestamps, IP, MCC/MNC, IMSI, and uplink/downlink usage. See [SIM Reporting & Analytics](sim-reporting-analytics.md).
- Prevent bill shock with group-level or per-SIM data caps and alerts:
  - At 80% of the limit, the organization owner is emailed
  - At 100%, impacted SIMs are disabled to stop usage
  - Create notification profiles and channels (SMS, Voice, Email, Webhook) and assign them to a SIM’s Usage Notification Threshold
  - See setup steps in [SIM Data Limits & Notifications](sim-data-limits-notifications.md)

## Coverage, Roaming, and Pricing Basics

- Coverage: 180+ countries on 650+ networks (see [International IoT SIM Coverage](international-iot-sim-coverage.md) and [International Roaming Partners](international-roaming-partners.md))
- Pricing components (see [IoT SIM Card Pricing](iot-sim-card-pricing.md)):
  - One-time charge per SIM: $1
  - Monthly recurring per active SIM: $2 (reduced to $0.20 on standby/deactivated)
  - Data usage: tiered by country zone and total monthly account usage
- Zone mapping and live rates by country: [Telnyx IoT SIM Data Usage Zone Mapping](telnyx-iot-sim-data-usage-zone-mapping.md)
- The SIM’s country of use (MCC) determines the zone and rate applied

## Optional Network and Security Features

- Dual-SIM failover (InRouter300) for redundancy
- Static IP configuration if assigned by Telnyx
- VPN options: IPSec, OpenVPN, PPTP, WireGuard (model-dependent)
- Firewall rule hardening on the router
- Automated recovery via Teltonika Auto Reboot watchdog
- Fleet management with Teltonika RMS
- For broader edge networking, see [Intro to Telnyx Edge Router](intro-to-telnyx-edge-router.md)

## Back Up and Restore Device Configurations

- InRouter300: System > Config Management (Backup/Import .dat)
- Teltonika: System > Backup (export/restore)
- Keep labeled backups after each change for rapid rollback

## Common Issues and Fixes

- No Internet: confirm SIM active and enabled, APN = data00.telnyx, data roaming on, reboot, test SIM in another device
- Poor signal: relocate device, use external LTE antennas
- Config not saving: ensure Apply/Save steps, then reboot; factory reset if needed
- Unexpected disconnects: enable auto-reboot watchdog (Teltonika), consider dual-SIM failover (InRouter300), and review [SIM Connectivity Logs](sim-connectivity-logs.md) for root cause
