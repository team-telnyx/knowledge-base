---
title: Telnyx Wireless and Messaging Reference
summary: A consolidated reference covering Telnyx eSIM setup (QR code and manual activation),
  manual IMSI selection, SIM connectivity logs and wireless connectivity states, SIM
  data limits and notifications, SIM theft prevention via IMEI authorization, MMS
  sending/receiving with FAQs, group messaging, bulk messaging via Google Sheets,
  number pooling, and the international voice spend limit.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
updated_at: 2026-07-17T08:59:32Z
---

# Telnyx Wireless and Messaging Reference

*Part 1 of 4 — see also: [Part 2](telnyx-wireless-and-messaging-reference--part-2.md), [Part 3](telnyx-wireless-and-messaging-reference--part-3.md), [Part 4](telnyx-wireless-and-messaging-reference--part-4.md)*

A consolidated reference covering Telnyx eSIM setup (QR code and manual activation), manual IMSI selection, SIM connectivity logs and wireless connectivity states, SIM data limits and notifications, SIM theft prevention via IMEI authorization, MMS sending/receiving with FAQs, group messaging, bulk messaging via Google Sheets, number pooling, and the international voice spend limit.

## Manual eSIM Activation

Manual eSIM activation is used when QR code scanning isn't feasible, particularly for devices that don't have cameras (IoT devices, modems, routers) or when the QR code cannot be displayed or printed.

After purchasing an eSIM, retrieve the activation code using the [Get SIM Card Activation Code API](https://developers.telnyx.com/api-reference/sim-cards/get-sim-card-activation-code). Pass the eSIM's UUID as the `id` parameter; the UUID is available in the SIM card view in the portal just above the QR code. If the activation code cannot be retrieved via the API, contact Telnyx support for assistance.

The activation code contains both the SM-DP+ address and matching ID. Manually entering these into a device (via AT commands or a GUI, depending on the device) connects it to the SM-DP+ server, which authenticates the device so it can download and activate the allocated eSIM. The manual setup method depends on the modem manufacturer, not the eSIM provider.

### Mobile phones

**iOS:**
1. Go to **Settings** > **Cellular** or **Mobile Data**.
2. Tap **Add eSIM** and select **Enter Details Manually**.
3. Input the SM-DP+ address and activation code.
4. Complete the setup by following the on-screen prompts.

**Android:**
1. Open **Settings** > **Network & Internet** > **SIMs**.
2. Choose **Add eSIM** or tap the **+** sign.
3. Manually enter the SM-DP+ address and activation code as prompted.
4. Follow the instructions to activate the eSIM.

### Modems and routers

Because modems lack screens and cameras, their eSIM activation process differs and may involve entering commands or using a graphical interface.

- **AT command modems (e.g. Quectel):** Log into the modem's interface and enter the required AT commands for eSIM activation, including the SM-DP+ address and activation code.
- **GUI-based routers (e.g. Peplink):** Open the router's GUI, go to the cellular settings, and manually enter the SM-DP+ address and activation code to initiate the connection.

Steps vary by modem and manufacturer, so consult the specific setup guide provided by the modem's manufacturer.

### Activation code concepts

- **Activation code:** A unique code comprising the SM-DP+ address and the matching ID. It contains everything needed to retrieve and activate the eSIM.
- **SM-DP+ address:** A unique code that identifies an SM-DP+ server, used to locate and connect to the server that manages eSIM profiles.
- **Matching ID:** A unique code that identifies a specific eSIM on an SM-DP+ server.

## eSIM Setup via QR Code

To purchase and activate a Telnyx eSIM via QR code:

1. **Visit the SIM card page:** Log into the account and visit the [wireless dashboard](https://portal.telnyx.com/#/wireless/dashboard).
2. **Purchase an eSIM:** Click **Purchase eSIMs** in the top right. In the pop-up window, select the number of eSIMs, choose a SIM Card Group, set the SIM Card Status (Disabled, Enabled, or Standby), and add SIM Card Tags for reporting segregation. The status must be set to Enabled to proceed with activation. For bulk eSIM pricing, contact [sales@telnyx.com](mailto:sales@telnyx.com).
3. **Activate with QR code:** After purchase, a new window displays the QR code. Scan it with the device's camera; the camera will highlight "mobile plan" beneath the QR code. Follow the on-screen instructions; activation may take a few minutes. Verify the APN is set correctly to `data00.telnyx`.

## Manual IMSI Selection

Manual IMSI selection is an engineering tool intended for advanced troubleshooting and should only be used when explicitly directed by the Telnyx engineering team.

Telnyx SIM cards use Multi IMSI technology to maximise global coverage and resilience. By default, the SIM automatically selects the most appropriate IMSI based on internal logic. A SIM Toolkit (STK) application is installed on the device when the Telnyx SIM is enabled, displaying a menu that allows manual IMSI selection.

### Android

1. Open the **SIM Toolkit** or **Telnyx** app (it may appear as "Telnyx UICC" or "SIM Toolkit").
2. Click on **Roaming Services** or **Telnyx**.
3. Tap **IMSI Selection Menu** and select the desired IMSI (e.g. IMSI1, IMSI2) as instructed by Telnyx support.
4. Wait a few minutes for the device to read the new IMSI and reconnect to the network.
5. Return to **Selection Mode** and switch back to **Automatic** for normal operation.

### iOS

1. Go to **Settings** → **Mobile Service** (or **Mobile Data** or **Cellular**) → **SIM Applications**. On multi-SIM devices, select the Telnyx SIM from the list of available SIMs first.
2. Tap **IMSI Selection Menu** and select the desired IMSI as instructed by Telnyx support.
3. Wait a few minutes for the device to read the new IMSI and reconnect to the network.
4. Return to **Selection Mode** and switch back to **Automatic** for normal operation.

Always switch back to Automatic once testing is complete (unless instructed otherwise). Failure to do so may result in loss of connectivity when the device moves geographically.

## SIM Connectivity Logs

Connectivity logs can be viewed via the Portal (by drilling down into a SIM card) and the API. There are two types of logs: `registration` and `data`. When SIMs attach to a network they first authenticate with the Telnyx mobile core, then create a data session to run traffic. The country code (MCC) represents the country in which the SIM is connecting, and the provider code (MNC) uniquely identifies the network. The mapping of these codes to operators is available on the [Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code) Wikipedia page.

### Troubleshooting patterns

- **No logs at all:** Signaling from the attach attempt has not reached the Telnyx core, indicating a likely downstream issue. Contact support.
- **Many registration attempts in succession without a data log:** The SIM is likely not authenticating with the Telnyx mobile core. The most common causes are that data roaming has not been enabled on the device or the APN is not correctly set to `data00.telnyx`.
- **No logs of type data:** The data session is not being created, typically due to roaming not being enabled or APN misconfiguration. Contact support if the issue persists.
- **Error logs:** Signaling is likely not reaching the mobile core. The SIM may be trying to connect to an unsupported operator, roaming may not be enabled, or the SIM may be disabled. Use a network scan to find a supported network, enable roaming and reboot, or check the Mission Control portal for a disabled state due to data limit or balance issues.

## Wireless Connectivity States

When using the [Telnyx Wireless Connectivity Logs API](https://developers.telnyx.com/api/wireless/get-wireless-connectivity-logs), different `state` values represent the status of wireless SIM sessions.

- **Opened:** A SIM initiates a new session to connect to a wireless network. Occurs immediately after an attached event when a device starts transmitting or receiving data.
- **Attached:** A SIM successfully connects to the local carrier network. Once attached, the SIM receives an IP address, enabling data sessions. Occurs when the SIM successfully registers with the cellular network.
- **Closed:** The data session has ended. Triggers include loss of network coverage, the device intentionally stopping the session (e.g. scheduled IoT sessions), the device switching off or entering airplane mode, or the device disconnecting from the cellular network upon connecting to Wi-Fi.
- **Provisioned:** A newly provisioned SIM remains in this state until it first attaches to a cellular network. May also appear if the SIM has been transferred from a regular SIM group to a private wireless gateway SIM group.

A standard successful connection cycle is **Attached → Opened → Closed**. The API does not explicitly identify devices that lose coverage, but a lack of "Attached" events indicates the device has not connected to the network.
