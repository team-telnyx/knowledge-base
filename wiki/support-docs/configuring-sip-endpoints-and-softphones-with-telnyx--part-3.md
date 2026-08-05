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

*Part 3 of 3 — see also: [Part 1](configuring-sip-endpoints-and-softphones-with-telnyx--part-1.md), [Part 2](configuring-sip-endpoints-and-softphones-with-telnyx--part-2.md)*

Step-by-step instructions for registering a variety of SIP-compatible softphones, IP phones, and hardware endpoints (Linphone, Yealink, Zoiper variants, Algo 8xxx, NCH Express Talk, Zoiper Communicator) with the Telnyx Mission Control Portal, including credential setup, encryption (TLS/SRTP), caller ID configuration, and voicemail enablement.

## Algo 8xxx SIP Endpoints

[Algo](https://www.algotechnologies.co.za/about/) manufactures SIP endpoints, IP speakers, paging adapters, specialty handsets, strobe lights, clocks, push buttons, and doorphones/intercoms. This section covers the Algo 8xxx series.

Pre-requisites:
- A properly configured Telnyx Mission Control Portal.
- At least one Telnyx SIP account/sub-account with a valid caller ID (anonymous outgoing calls are not supported).
- SIP-TLS enabled if you want encrypted traffic.
- The [most current Algo device firmware](https://www.algosolutions.com/?s=firmware&v=7516fd43adaa).

### Associate SIP Credentials

1. Open the Algo device's web interface using its IP address.

   ![SIP Horn Control Panel.](_images/59078261cf5f6965.jpg)
2. Go to **Basic Settings > SIP** and enter:
   - **SIP Domain (Proxy Server):** `sip.telnyx.com`
   - **Base/Page Extension:** Account/sub-account username.
   - **Authentication ID:** Account/sub-account username.
   - **Authentication Password:** Account/sub-account password.
   - **Display Name:** Outbound caller ID.

   ![SIP Basic Settings tab.](_images/e216faec52fd9463.png)

> For additional extensions (ringing, paging, emergency alerting), use unique credentials for each. Any combination of page, ring, and emergency alert extensions is supported.

### Enable SIP-TLS/SRTP Encryption (Optional)

1. Go to **Advanced Settings > Advanced SIP** and set:
   - **SIP Transportation:** TLS.
   - **SDP SRTP Offer:** Standard (mandatory encryption). Set to Optional if you want calls to fall back to unencrypted when the other party does not support encryption.

   ![Advanced SIP Settings.](_images/f9babf5ba82342cc.jpg)

> **8301 Users:** A user certificate must be installed manually. Add a file named `sipclient.pem` (containing the device certificate and private key) to the `certs` folder under **Advanced Settings > File Manager**. Future releases will also support `.crt`, `.cer`, and `.der` extensions.

### Confirm Registration

1. Open the **Status > Device Status** tab.
2. Verify each extension's SIP registration shows as *Successful*.

   ![Device status screenshot.](_images/5404f8ba12e0f8cb.jpg)

### Enable G-722 Codec (Optional)

1. Go to **Basic Settings > Features**.
2. In **Inbound Page Settings**, enable **G-722 Support**.

   ![Test tone settings page.](_images/02e99a41cbbf3802.png)

> Algo supports G.711 u-law, G.711 A-law, and G.722 Wideband audio codecs.

### Algo Troubleshooting

**SIP Registration status = "Rejected by Server":**
- Verify SIP credentials (extension, authentication ID, password), including case. Disable browser auto-fill if the password field looks wrong.
- Confirm the SIP transportation setting on the Algo matches the Telnyx Mission Control Portal.
- Check the address/port for the SIP server. A *500 Internal Server error* in the system log (**System > System Log**) usually indicates an incorrect address/port.

**SIP Registration status = "No reply from server":**
- Verify the internet connection is up and stable.
- Confirm the **SIP Domain (Proxy Server)** is correct under **Basic Settings > SIP**.
- Check that no firewall is blocking incoming packets from the server.

## NCH Express Talk

[NCH Express Talk](https://www.nch.com.au/talk/) is a VoIP softphone for Windows and Mac that supports up to 6 lines, conferencing, call recording, caller ID display, voice commands, and integration with Microsoft Address Book. A free trial is available for non-commercial use only.

System requirements: Windows XP/Vista/7/8/8.1/10/11 or Mac OS X 10.5–10.14, plus a soundcard.

### Configure Express Talk

1. Run Express Talk.

   ![Express Talk softphone configurations tab.](_images/be6e6da81351e585.png)
2. Open **File > Options**.

   ![File menu](_images/dd89f759db560e96.png)
3. On the **Lines** tab, enter:
   - **Full "Friendly" display name:** Display name of your choice.
   - **Server (SIP Proxy or Virtual PBX):** `sip.telnyx.com`
   - **SIP Number (or Username):** Your Telnyx SIP account ID.
   - **Password:** Your Telnyx SIP account password.

   ![Lines tab](_images/2cf1b54f41af576a.png)

Additional Express Talk resources: [Windows download](https://www.nch.com.au/components/talksetup.exe), [Mac download](https://www.nch.com.au/components/talkmaci.zip), [SDK](https://www.nch.com.au/talk/sdk.html), [technical support](https://www.nch.com.au/talk/support.html), and [pricing](https://secure.nch.com.au/cgi-bin/register.exe?software=talk).

## Caller ID Configuration

Telnyx enforces a strict caller ID policy. The number used as caller ID must either be a number on your Telnyx account or a number previously verified with Telnyx. See the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) and [verified numbers](https://support.telnyx.com/en/articles/6988813-verified-numbers) articles for details.

If you receive a 403 error about an invalid caller ID, the softphone may not be passing the caller ID in the required headers. As a workaround, configure a caller ID override in the outbound section of your SIP connection settings.

When setting a caller ID name, follow these conventions:
- Use capital letters for better visibility on some devices.
- Do not use special characters (they will not be displayed).
- Some Canadian providers display no more than 15 characters; consider shortening the name.
- Spaces are allowed.

## Telnyx Voicemail

> Voicemail should only be enabled on numbers assigned to SIP Connections.

Telnyx voicemail forwards missed or rejected calls to a voicemail box. Messages can be retrieved by dialing `*98` from a voicemail-enabled number and authenticating with an access PIN. The calling device must have the voicemail-enabled number set as its Caller ID before dialing `*98`.

### Setting a Voicemail PIN

1. Go to **Numbers > My Numbers** in the [portal](https://portal.telnyx.com/).
2. Filter for the number to configure.
3. Click the pencil icon under the actions column.
4. Open the **voice** sub-tab.
5. Scroll to the **Voice Mail** section.
6. Toggle voicemail on and set a PIN.

### Voicemail Webhook Event

If a webhook URL is configured on your SIP Connection, Telnyx delivers a `calls.voicemail.completed` event:

```json
{
  "data": {
    "event_type": "calls.voicemail.completed",
    "id": "93958804-6787-4623-bb59-a4e4ce1c44de",
    "occurred_at": "2023-11-15T08:00:33.589698Z",
    "payload": {
      "call_session_id": "036c8492-838d-11ee-b3bb-02420a0d3a69",
      "connection_id": "1635420769989166414",
      "from": "+13121234567",
      "recording_url": "url of recording to download file",
      "to": "+13127654321"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/0a6718c8-e59a-4921-8119-c395d631a99b"
  }
}
```

### Current Limitations

- The voicemail box greeting message cannot be customized.
- Email notifications for deposited voicemails are not supported.

### Voicemail API

Programmatic voicemail management is available via the Telnyx developer documentation:
- [Get voicemail](https://developers.telnyx.com/api/voicemail/get-voicemail)
- [Create voicemail](https://developers.telnyx.com/api/voicemail/create-voicemail)
- [Update voicemail](https://developers.telnyx.com/api/voicemail/update-voicemail)

## Additional Resources

- [Getting Started with a Mission Control Account](getting-started-with-a-mission-control-account.md)
- [Linphone technical documentation](https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/)
- [Yealink Knowledge Base](https://support.yealink.com/en/portal/knowledge)
- [Zoiper 5 user guide](https://www.zoiper.com/pdf/User%20Guide%20Zoiper%205%20v.1.0.7.pdf)
- [Zoiper 3 user guide](https://www.zoiper.com/en/support/home/article/34/Installation_%26_configuration_manuals_Zoiper_3)
- [Algo user guides](https://www.algosolutions.com/resources/guides/)
- [Express Talk technical support](https://www.nch.com.au/talk/support.html)
