---
title: Configuring SIP Endpoints and Softphones with Telnyx
summary: Step-by-step instructions for registering a variety of SIP-compatible softphones,
  IP phones, and hardware endpoints (Linphone, Yealink, Zoiper variants, Algo 8xxx,
  NCH Express Talk, Zoiper Communicator) with the Telnyx Mission Control Portal, including
  credential setup, encryption (TLS/SRTP), caller ID configuration, and voicemail
  enablement.
sources:
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
- url: https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac
- url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
- url: https://support.telnyx.com/en/articles/5807457-nch-express-talk
- url: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail
- url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
updated_at: 2026-08-05T13:31:36Z
---

# Configuring SIP Endpoints and Softphones with Telnyx

*Part 1 of 3 — see also: [Part 2](configuring-sip-endpoints-and-softphones-with-telnyx--part-2.md), [Part 3](configuring-sip-endpoints-and-softphones-with-telnyx--part-3.md)*

Step-by-step instructions for registering a variety of SIP-compatible softphones, IP phones, and hardware endpoints (Linphone, Yealink, Zoiper variants, Algo 8xxx, NCH Express Talk, Zoiper Communicator) with the Telnyx Mission Control Portal, including credential setup, encryption (TLS/SRTP), caller ID configuration, and voicemail enablement.

## Overview

Telnyx supports a wide range of SIP-compatible softphones, IP phones, and hardware endpoints. This page consolidates setup instructions for the most common devices, including Linphone, Yealink T-series, Zoiper (Communicator, 3, and 5 Pro), Algo 8xxx, and NCH Express Talk. It also covers Telnyx voicemail configuration and shared prerequisites such as caller ID policy and encryption.

Before configuring any device, ensure your Telnyx Mission Control Portal is set up correctly. You will need a credentials-based connection, a DID assigned to that connection, and an outbound voice profile. See the [Getting Started with a Mission Control Account](getting-started-with-a-mission-control-account.md) guide for details.

## Shared Prerequisites

Most device setup guides require the following on the Telnyx side:

- A properly configured [Telnyx Mission Control Portal](https://portal.telnyx.com/) account.
- A purchased DID assigned to a SIP connection.
- A credentials-based connection that provides the SIP username and password used to register the device.
- An outbound voice profile.
- (Recommended) TLS/SRTP enabled to encrypt call traffic.

The SIP domain for all Telnyx registrations is `sip.telnyx.com`. For encrypted registrations, append port `5061` (e.g., `sip.telnyx.com:5061`) and select TLS as the transport.

## Linphone

[Linphone](https://www.linphone.org) is an open-source VoIP softphone SIP client that supports audio and video calls and instant messaging.

### Configuring Linphone

1. Run Linphone and follow the wizard.
2. Click **ACCOUNT ASSISTANT**.

   ![Linphone softphone account assistant wizard 2.](_images/8b335edacfc3dc96.png)
3. Click **USE A SIP ACCOUNT**.

   ![Linphone softphone account assistant wizard 2.](_images/019b946dee183f15.png)
4. Fill in the form:
   - **Username:** Your SIP connection auth username.
   - **Display Name:** Your caller ID. Most Linphone versions use the Display Name as the FROM field.
   - **SIP Domain:** `sip.telnyx.com`
   - **Password:** Your SIP connection auth password.
   - **Transport:** UDP or TCP.

   ![SIP Account credentials form.](_images/ce6604b2be2af738.png)
5. Click **USE**.

### Configuring Linphone with Encryption

1. In the **SIP Domain** field, append port 5061 (`sip.telnyx.com:5061`).
2. Set **Transport** to TLS.

   ![Linphone encryption configuration interface.](_images/199007f6c0bcd3ad.png)
3. Open the top-right menu and select **Preferences**.

   ![Linphone encryption configuration interface 2.](_images/5c88d2b750147f0e.png)
4. On the **Call and Chat** tab, enable SRTP.

   ![Linphone encryption configuration interface 3.](_images/a93183304bd48a07.png)

For Linphone documentation, see the [Linphone technical documentation](https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/) and [Linphone support](https://www.linphone.org/contact).

## Yealink T-Series IP Phones

[Yealink](https://www.yealink.com/en) provides SIP-compatible T-series hardphones for voice and video communication.

### Provisioning via the Phone Keypad

1. Press **Menu** on the handset.
2. Navigate to **Advanced** and enter the password (default: `admin`).
3. Navigate to **Accounts** and select an empty line.
4. Configure:
   - **Activation:** Enabled.
   - **Label:** Display name (e.g., *John Doe*).
   - **Register Name:** Your Telnyx account username.
   - **User name:** Your Telnyx account username.

### Provisioning via the Web Interface

1. Find the phone's IP address: press **Home/Menu**, then **Status**, and note the IPv4 address.
2. Enter the IP address in a browser. Default credentials are `admin` / `admin`.

   ![Telnyx web portal.](_images/a32aee771d9e50b6.png)
3. Click **Account**, then **Account 1**, and configure:
   - **Activation:** Enabled.
   - **Label:** Display name (e.g., *John Doe*).
   - **Register Name:** Username from your credentials-based Telnyx connection.
   - **User name:** Username from your credentials-based Telnyx connection.
   - **Password:** Password from your credentials-based connection.
   - **Display Name:** Outbound caller ID.

   ![Yealink web settings dashboard.](_images/d664bb1fdf756c3a.png)

Additional Yealink resources: [Knowledge Base](https://support.yealink.com/en/portal/knowledge), [equipment maintenance](https://ams.yealink.com/search/index), [license application](https://license.yealink.com/), and [support](https://support.yealink.com/en/portal/home).
