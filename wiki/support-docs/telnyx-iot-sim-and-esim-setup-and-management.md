---
title: Telnyx IoT SIM and eSIM Setup and Management
summary: End‑to‑end guide to ordering, registering, activating, and managing Telnyx
  IoT SIMs and eSIMs, including APN settings, QR and manual eSIM activation, device
  and router notes, SIM security and lifecycle controls, engineering-only IMSI selection,
  and key FAQs on pricing, coverage, and operations.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card
- url: https://support.telnyx.com/en/articles/3269973-adding-the-telnyx-sim-apn-to-your-device
- url: https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs
- url: https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
- url: https://support.telnyx.com/en/articles/5812302-sim-card-location-and-device-details
- url: https://support.telnyx.com/en/articles/5812328-sim-card-actions
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/collections/1895859-telnyx-global-iot-sims
updated_at: 2026-05-20T15:26:30Z
---

# Telnyx IoT SIM and eSIM Setup and Management

End‑to‑end guide to ordering, registering, activating, and managing Telnyx IoT SIMs and eSIMs, including APN settings, QR and manual eSIM activation, device and router notes, SIM security and lifecycle controls, engineering-only IMSI selection, and key FAQs on pricing, coverage, and operations.

## Ordering and Registration
- Order physical SIMs from your Mission Control Portal wireless section; delivery typically takes a few days in the U.S. (longer internationally). For large orders (>50), contact sales; unbranded SIMs require a 5,000 MOQ.
- Ensure at least $2 USD account balance before registering SIMs.
- Register plastic SIMs in Portal: Wireless → Register SIM Cards → enter the 10‑digit registration code (multiple codes allowed, comma-separated). Optionally assign tags and a SIM Group, and set status (enabled/standby/disabled). Registration can also be performed via API (see developers docs).
- eSIMs are purchased in Portal (Wireless dashboard → Purchase eSIMs), where you choose quantity, group, status (Disabled/Enabled/Standby), and tags. You’ll receive a QR code for activation after purchase when status is Enabled.

## APN Configuration and Device Preparation
- Create/select an APN on your device with only these two fields:
  - Name: Telnyx
  - APN: data00.telnyx
- Leave all other APN fields unmodified (even if blank), save, and make the APN active.
- Typical OS paths:
  - Android: Settings → Connections (or Network & Internet) → Mobile Networks → Access Point Names → Add
  - iOS: Settings → Cellular/Mobile Data → APN
- Enable Data Roaming. Some devices require a reboot for settings to take effect.
- Important: Complete first‑time network registration over 4G/LTE (not 2G/3G) where required by local providers.

## eSIM Activation via QR Code
1. In Portal, purchase eSIMs and set status to Enabled.
2. Scan the displayed QR code with the eSIM‑capable device (e.g., phone camera → “Mobile plan” prompt) and follow on‑screen steps; activation can take a few minutes.
3. Verify APN is set to data00.telnyx after activation.

## Manual eSIM Activation (SM‑DP+ and Matching ID)
- Use manual activation when scanning a QR code isn’t feasible (e.g., IoT devices, modems, routers).
- Retrieve your eSIM activation code via API using the eSIM’s UUID (see developers API: Get SIM card activation code). If you can’t access the API, contact Telnyx Support to obtain the code.
- The activation code comprises:
  - SM‑DP+ address (identifies the SM‑DP+ server)
  - Matching ID (identifies your allocated eSIM profile on that server)
- Mobile OS manual entry:
  - iOS: Settings → Cellular/Mobile Data → Add eSIM → Enter Details Manually → enter SM‑DP+ and activation code
  - Android: Settings → Network & Internet → SIMs → Add eSIM → enter SM‑DP+ and activation code
- Modems/routers:
  - AT‑command modems (e.g., Quectel): enter SM‑DP+ and activation code via the modem interface/AT commands.
  - GUI‑based routers (e.g., Peplink): use the cellular settings page to enter SM‑DP+ and activation code.
- Note: Exact steps vary by manufacturer; consult your device’s documentation.

## Router and Modem Notes
- Use the Telnyx APN (data00.telnyx) and enable data roaming on cellular WAN profiles.
- For device‑specific examples, see:
  - Ubiquiti UniFi LTE Pro: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
  - InRouter300 Series: https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers
  - Teltonika 4G/LTE Routers: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers

## SIM Management: Actions, Location, and Device Details
- SIM Card Actions: Every lifecycle change (Enable, Disable, Standby, Data‑limit exceeded, Enable Standby) is tracked in Portal (SIM card → Actions) and via API for full auditability.
- Location: Portal and API show an estimated SIM location derived from the serving cell tower; stronger towers can increase the error radius. API returns latitude, longitude, accuracy, and unit.
- Device details: Portal/API expose device type, model, IMEI (plus brand/OS via API). You can restrict a SIM to specific devices by setting Authorized IMEIs.

## SIM Card Theft Prevention (Authorized IMEIs)
- Add up to 5 Authorized IMEIs per SIM to prevent unauthorized device use. If a non‑authorized IMEI appears, the SIM will auto‑disable (allow up to 5 minutes) and an email alert is sent.
- If no Authorized IMEIs are configured, all devices are treated as authorized (default behavior).

## Manual IMSI Selection (Engineering‑Only)
- Telnyx SIMs use Multi‑IMSI for global coverage and normally select IMSI automatically. Manual selection is for advanced troubleshooting only under Telnyx engineering direction.
- Android: Open the Telnyx/SIM Toolkit app → Roaming Services/Telnyx → IMSI Selection Menu → choose IMSI1/IMSI2 as instructed → wait a few minutes for reconnection → return to Automatic when done.
- iOS: Settings → Cellular/Mobile Data → SIM Applications (select the Telnyx SIM if multi‑SIM) → IMSI Selection Menu → choose IMSI as instructed → wait → revert to Automatic.
- Always switch back to Automatic unless explicitly told otherwise, or connectivity may be affected during movement.

## Product FAQs, Pricing, and Policies (Highlights)
- Service scope: Telnyx SIMs are data‑only. Two‑way SMS is available via AT commands.
- Coverage: Global roaming supported; see coverage/partners: https://telnyx.com/iot-global-coverage and https://support.telnyx.com/en/articles/3371977-international-roaming-partners
- Shipping: Small U.S. orders ship via USPS in a few days (longer for AK/HI and international). Contact sales for large orders and potential expedition.
- Costs (indicative):
  - SIMs from $1 each (plastic/MFF2); eSIMs from $0.70 OTA
  - Monthly Recurring Charge: $2 per active SIM; $0.20 per inactive SIM; no MRC for disabled SIMs
  - No fees for changing SIM state; pay‑as‑you‑go data available; data rounded to nearest MB; pricing from $0.0125/MB (see pricing page: https://support.telnyx.com/en/articles/3296669-iot-sim-card-pricing)
- Provisioning and usage control: SIMs are provisioned upon registration (standby or active). Set data limits at SIM or Group level and monitor near real‑time usage; see analytics/reporting: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics and data limits: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- Account transfer: You can delete a SIM from Account A and re‑register it to Account B using the registration code (contact support if you need the code).

## Troubleshooting and Logs
- Use SIM Connectivity Logs to investigate attach/registration/session states and events: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs and connectivity state definitions: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- Ensure APN is exactly data00.telnyx, Data Roaming is enabled, and first registration is attempted on LTE.
- For eSIM issues, confirm SM‑DP+ and Matching ID are entered correctly (manual) or rescan the QR code (QR flow).
- Need help? Contact support: https://telnyx.com/contact-us or support@telnyx.com

## Developer References
- Register SIMs via API: https://developers.telnyx.com/api-reference/sim-cards/register-sim-cards
- Get SIM card details (incl. current_device_location and device fields): https://developers.telnyx.com/api-reference/sim-cards/get-sim-card
- Retrieve eSIM activation code (SM‑DP+ and Matching ID): https://developers.telnyx.com/api-reference/sim-cards/get-sim-card-activation-code
- SIM lifecycle and actions API: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle
