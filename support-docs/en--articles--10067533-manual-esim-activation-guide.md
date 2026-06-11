---
source_url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
scraped: 2026-06-11
---

Manual eSIM activation guide | Telnyx Help Center

[Skip to main content](#main-content)

# Manual eSIM activation guide

How to activate your eSIM without a QR code.

Written by David

April 8, 2026

Table of contents

Manual eSIM activation is used when QR code scanning isn’t feasible, particularly for devices that don't have cameras like IoT devices, modems, or routers, or if you’re unable to display or print the QR code.

After you've purchased an eSIM, you need to retrieve the activation code to manually activate your eSIM:

**Retrieve your activation code using [this API call](https://developers.telnyx.com/api-reference/sim-cards/get-sim-card-activation-code):**

* Pass the UUID (Universally Unique Identifier) of the eSIM as the `id` parameter.
* The UUID is available in the SIM card view in the portal(just above the QR code).

If for some reason you are unable to retrieve your activation code via our API, please [contact our support team](https://telnyx.com/contact-us) who can provide your activation code.

The activation code contains both the SM-DP+ address and matching ID. Manually entering the SM-DP+ address and matching ID into your device (via AT commands or through a GUI, depending on the device) connects it to the SM-DP+ server. The server will authenticate your device so you can download and activate your allocated eSIM.

**Note: The manual setup method depends on the modem manufacturer and NOT the eSIM provider.**

# Manual eSIM setup on mobile phones

**For iOS devices**

1. Go to **Settings** > **Cellular** or **Mobile Data**.
2. Tap **Add eSIM** and select **Enter Details Manually**.
3. Input the SM-DP+ address and activation code.
4. Complete the setup by following the on-screen prompts.

**For Android devices**

1. Open **Settings** > **Network & Internet** > **SIMs**.
2. Choose **Add eSIM** or tap the **+** sign.
3. Manually enter the SM-DP+ address and activation code as prompted.
4. Follow the instructions to activate the eSIM.

# Manual eSIM setup on modems and routers

Because modems lack screens and cameras, their eSIM activation process is different and may involve entering commands or using a graphical interface.

**For modems using AT Commands (e.g. [Quectel modem](https://forums.quectel.com/t/esim-at-command-set/13313))**

Log into the modem’s interface and enter the required AT commands for eSIM activation, including the SM-DP+ address and activation code.

**For GUI-based Routers (e.g. [Peplink router](https://www.youtube.com/watch?v=igReb-oENS4))**

Open the router’s GUI, go to the cellular settings, and manually enter the SM-DP+ address and activation code to initiate the connection.

***These steps vary by modem and manufacturer, so it’s best to consult the specific setup guide provided by your modem’s manufacturer.***

# FAQs

## Why would I need to activate my eSIM manually?

Manual activation is useful when:

1. Devices don’t have a camera (e.g. IoT devices, routers).
2. You cannot display or print the QR code to scan with the device.

Manual activation is a great fallback if you need flexibility in device setup.

## What is an activation code?

An activation code is a unique code that in turn comprises two unique codes; the SM-DP+ address and the matching ID (*activation code* = *SM-DP+ address* + *matching ID*). When a customer purchases an eSIM, the eSIM provider gives an activation code to the customer. The activation code contains everything the customer needs to retrieve and activate the eSIM:

1. The SM-DP+ address to locate and connect to the SM-DP+ server
2. The matching ID to identify the specific eSIM on the server that has been allocated to the customer

## What is an SM-DP+ address?

The SM-DP+ address is a unique code that identifies an SM-DP+ server. The address is required to communicate with the server to set up an eSIM. The SM-DP+ address is part of the activation code.

## What is a matching ID?

The matching ID is a unique code that identifies an eSIM on an SM-DP+ server. The matching ID is part of the activation code.

## What is the role of the SM-DP+ address in eSIM activation?

During activation, the SM-DP+ address is used by the device to locate and connect to the SM-DP+ server that manages eSIM profiles. The device requests the necessary data from the server, and once verified, the server authorizes the eSIM profile download.

​

---

Related Articles

[Short Message Peer-to-Peer Set-up Guide](https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide)[Mediatrix C7/4100: Telnyx Setup](https://support.telnyx.com/en/articles/5733572-mediatrix-c7-4100-telnyx-setup)[Telnyx Messaging Error Codes](https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes)[How to setup a Telnyx eSIM via QR code](https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code)[Using Telnyx SIM with Teltonika 4G/LTE Routers](https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers)

Did this answer your question?

😞😐😃

Table of contents
