---
title: Telnyx eSIM activation and router setup (Ubiquiti, InRouter300, Teltonika)
summary: End-to-end guidance for activating a Telnyx eSIM without a QR code and configuring
  popular routers for cellular connectivity, with APN settings, first-attach tips,
  troubleshooting, and how to monitor sessions via the Telnyx Wireless Connectivity
  Logs API.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
- url: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
- url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
updated_at: 2026-05-14T11:26:21Z
---

# Telnyx eSIM activation and router setup (Ubiquiti, InRouter300, Teltonika)

End-to-end guidance for activating a Telnyx eSIM without a QR code and configuring popular routers for cellular connectivity, with APN settings, first-attach tips, troubleshooting, and how to monitor sessions via the Telnyx Wireless Connectivity Logs API.

## When to use manual eSIM activation
Manual activation is useful when the device can’t scan a QR code (e.g., IoT devices, modems, routers) or you can’t display/print one. It’s a flexible fallback that works across phones and headless hardware.

## Find and use your eSIM activation code
- Retrieve the activation code via the Telnyx API: Get SIM Activation Code (developers) — https://developers.telnyx.com/api-reference/sim-cards/get-sim-card-activation-code. Pass the eSIM’s UUID as the id parameter (visible in the SIM card view in the Telnyx Portal).
- If you can’t retrieve it via API, contact Telnyx Support — https://telnyx.com/contact-us.
- What the code contains:
  - SM-DP+ address: identifies the subscription manager server used to download the eSIM profile.
  - Matching ID: identifies the specific eSIM profile allocated to you on that server.
- Entering the SM-DP+ address and Matching ID (via device UI or AT commands) connects the device to the SM-DP+ server to authenticate, download, and activate your eSIM profile.
- Note: The manual setup flow depends on the modem/router manufacturer, not the eSIM provider.

## Manual eSIM entry on phones (iOS and Android)
- iOS: Settings > Cellular/Mobile Data > Add eSIM > Enter Details Manually > input SM-DP+ address and activation code; follow prompts.
- Android: Settings > Network & Internet > SIMs > Add eSIM (or +) > enter SM-DP+ address and activation code; follow prompts.

## Manual eSIM activation on modems and routers
- AT command–driven modems (e.g., Quectel): Use the vendor’s eSIM commands to supply the SM-DP+ address and Matching ID. Vendor reference: https://forums.quectel.com/t/esim-at-command-set/13313
- GUI-based routers (e.g., Peplink): Use the cellular settings page to enter the SM-DP+ address and activation code, then apply changes. Example video: https://www.youtube.com/watch?v=igReb-oENS4

## Telnyx APN settings (all devices)
- APN: data00.telnyx
- Authentication: None (leave Username/Password blank or set Authentication Type to NONE if required by UI)

## Ubiquiti UniFi LTE Pro: LTE backup with a Telnyx SIM
1. Insert the Telnyx Nano SIM into the UniFi LTE Pro.
2. Power via a PoE (802.3af) UniFi switch.
3. Log in at https://unifi.ui.com and adopt the device.
4. Go to Settings > Internet > LTE Backup > Settings.
5. Enter APN: data00.telnyx; Authentication Type: NONE; Apply.
6. Verify under Overview: Status = Ready and Connected = Yes.
Important notes:
- First-time attachment can take up to 30 minutes as the SIM discovers supported operators. Subsequent connections are faster.
- If a restart/re-provision puts the modem into SIM-Activation mode, enable modem autoconnect via UniFi CLI: qmicli -p -d /dev/cdc-wdm0 --wds-set-autoconnect-settings=enabled

## InRouter300 Series (InHand): APN and connectivity verification
Prerequisites: IR300-series router, active Telnyx SIM, Ethernet-connected computer.
1. Insert the Telnyx SIM and power the router.
2. Connect to http://192.168.2.1 and log in (Username: adm, Password: 123456 unless changed).
3. Network > Cellular > SIM Profiles: select the active SIM slot.
4. Set APN: data00.telnyx; leave Username/Password blank; Apply.
5. Optional: enable Dual SIM and failover if using a secondary SIM/carrier.
6. Verify: Status > Network Connection should show an IP address, registration, and healthy signal; test by reaching an external host.
Optional hardening:
- Static IP (if provisioned): Network > WAN Settings > Connection Type: Static IP; enter Telnyx-assigned details.
- VPN: VPN > Settings (IPsec/OpenVPN/PPTP) per your design.
- Firewall: Security > Firewall; apply least-privilege rules.
- Backup: System > Config Management > Backup to export a .dat file. Restore via Import on other units.
Troubleshooting highlights:
- No connectivity: confirm SIM active, APN correct, reboot, and check status; test the SIM in another device.
- Poor signal: reposition router or add LTE antennas.
- Settings not persisting: ensure you Apply/Save; factory reset if needed and reconfigure.

## Teltonika 4G/LTE routers: APN, auto-reboot, and RMS
Access and APN:
1. Connect to http://192.168.2.1 (Username: admin; Password on device label; change on first login if prompted).
2. Network > Interfaces; edit the mobile interface (e.g., mob1s1a1).
3. Uncheck Auto APN; set APN: data00.telnyx; leave Username/Password blank; Save & Apply.
Verify: Status > Network Information should show Connected, assigned IP, and adequate signal.
Resiliency via Auto-Reboot:
- System > Auto Reboot: enable watchdog; choose Ping Reboot with targets like 8.8.8.8 and 1.1.1.1; set interval (e.g., 60s) and retry count (e.g., 3). Optionally schedule periodic reboots.
Fleet management via Teltonika RMS:
- RMS (cloud) enables monitoring, bulk config, remote CLI, VPN setup, and alerts. Start at rms.teltonika-networks.com; register each device (System > RMS) and apply templates at scale.
Security & maintenance:
- Keep firmware current (System > Firmware), configure Network > Firewall, and use VPN options (OpenVPN, WireGuard, IPsec) as needed.
- Backup: System > Backup > Generate and store safely.
Troubleshooting:
- No Internet: verify SIM activity, APN accuracy, and signal; ensure watchdog is configured for recovery.
- Weak signal: relocate or fit external antennas.

## First-attach timing and network selection behavior
- Telnyx SIMs support multiple operators; initial attachment can take up to 30 minutes while the device discovers and selects networks. Once attached, learned operators are prioritized for faster future connections.

## Verifying and troubleshooting connectivity (general)
- Confirm APN is exactly data00.telnyx and authentication is disabled/blank.
- Check the device’s cellular status page for registration, IP assignment, and signal strength.
- Power-cycle the device after APN changes.
- For backups and repeatable deployments, export configs (feature names vary by vendor: Backup/Config Management/Export).
- For headless modems, ensure autoconnect is enabled so data sessions start automatically after reboot.

## Monitor sessions with the Wireless Connectivity Logs API
Use the Telnyx Wireless Connectivity Logs API to track session state — https://developers.telnyx.com/api/wireless/get-wireless-connectivity-logs
Key states you’ll see:
- Provisioned: Newly provisioned SIM (or moved to a private gateway group) awaiting its first network attach.
- Attached: SIM registered on a carrier network and assigned an IP; ready for data.
- Opened: A data session has begun (immediately after attach when traffic starts).
- Closed: The data session ended (e.g., coverage loss, device terminated session, device powered off/airplane mode, or device switched to Wi‑Fi).
Typical healthy cycle: Attached → Opened → Closed. A long absence of Attached events usually indicates the device isn’t connecting to any network.
