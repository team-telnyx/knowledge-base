---
title: Grandstream Devices with Telnyx
summary: How to configure Grandstream IP phones and adapters—including the GXP16XX,
  GXP21XX, HT802, and DP752—to connect with the Telnyx Mission Control Portal for
  SIP calling and faxing.
sources:
- url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
- url: https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup
- url: https://support.telnyx.com/en/articles/5808368-grandstream-dp752
- url: https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup
- url: https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx
updated_at: 2026-06-11T11:31:45Z
---

# Grandstream Devices with Telnyx

*Part 1 of 2 — see also: [Part 2](grandstream-devices-with-telnyx--part-2.md)*

How to configure Grandstream IP phones and adapters—including the GXP16XX, GXP21XX, HT802, and DP752—to connect with the Telnyx Mission Control Portal for SIP calling and faxing.

This guide covers the configuration of several Grandstream device families with Telnyx SIP trunks. The GXP series IP phones (GXP1620/25, GXP1630, GXP2135, GXP2170) share a nearly identical setup workflow. The HT802 analog telephone adapter is configured primarily for faxing. The DP752/DP750 DECT cordless system has its own profile-based configuration.

## Prerequisites

Before configuring any Grandstream device, complete the following:

- Ensure your [Telnyx Mission Control Portal](https://portal.telnyx.com) is set up properly — see the [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- Purchase and provision a Telnyx DID, and assign it to a SIP connection
- Create an [IP connection](https://portal.telnyx.com/#/app/connections) and an [outbound voice profile](https://portal.telnyx.com/#/app/outbound)
- Ensure your Grandstream device is running the [latest firmware](https://www.grandstream.com/support/firmware)
- **Recommended:** [Enable TLS](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication) to encrypt your traffic

For the **HT802**, an additional prerequisite is required in your Telnyx Portal: from **Connection Settings > Inbound**, set **Number Format (DNIS)** to *SIP Username*. Telnyx does not support phone numbers as connection usernames, and the HT802 expects inbound calls to be sent to the SIP username.

## GXP Series IP Phones

The configuration steps for the GXP1620, GXP1625, GXP1630, GXP2135, and GXP2170 are nearly identical. Follow the steps below for any of these models.

### Access the GXP Web UI

1. On the phone, navigate to **Menu > Status > Network Status > IPv4 Address** and note the IP address.
2. On a computer on the same network, open a browser and enter `http://` followed by the phone's IP address.
3. Log in with the default credentials — **Username:** `admin`, **Password:** `admin`. (Devices manufactured from January 2017 onward may have a unique random password printed on the unit's sticker.)

### Configure GXP Account and SIP Settings

1. Click **Accounts** in the top menu, then expand the account (e.g., Account 1) and select **General Settings**.
2. Enter the following:
   - **Account Name:** A descriptive name of your choice
   - **SIP Server:** `sip.telnyx.com`
   - **SIP User ID:** Your Telnyx SIP account username
   - **Authenticate ID** (or **Authentication ID**): Your Telnyx SIP account username
   - **Authenticate Password:** Your Telnyx SIP account password
   - **Name (Caller ID):** Use capital letters, no special characters (spaces allowed), 15 characters maximum recommended
   - **Voice Mail Access Number:** `*97`
3. Navigate to **Accounts > Account X > SIP Settings > Basic Settings** and set:
   - **SIP Registration:** `Yes`
   - **Register Expiration:** `5` (minutes)
   - **Enable OPTIONS Keep Alive:** `Yes`
   - **Local SIP Port:** `5060` (unencrypted) or `5061` (TLS)
   - **SIP Transport:** `UDP` or `TCP` (unencrypted) or `TLS/TCP` (encrypted)
4. Click **Save and Apply**.

### Configure GXP Network Settings

Under **Accounts > Account X > Network Settings**:

- **DNS Mode:** `A Record`
- **NAT Traversal:** `Keep-Alive`

### Disable Problematic Custom SIP Headers

Navigate to **Accounts > Account X > SIP > Custom SIP Header** and set the following to **No** (or disable them):

- **Use X-Grandstream-PBX Header**
- **Use P-Access-Network-Info Header**
- **Use P-Emergency-Info Header**

For the GXP21XX, additionally set:

- **Use Privacy Header:** `Yes`
- **Use P-Preferred-Identity Header:** `Yes`

### Select GXP Codec Preferences

Under **Accounts > Account X > Audio Settings**, choose a preferred vocoder. Supported Telnyx codecs include:

- PCMU (G.711u / ulaw)
- PCMA (G.711a / alaw)
- G.722
- G.729A/B

For the GXP21XX, **G729A/B** or **G722** is recommended as the preferred vocoder.

## HT802 Analog Telephone Adapter

The Grandstream HT802 is a 2-port analog telephone adapter (ATA) suitable for residential and office VoIP, with particular emphasis on fax support.

### Access the HT802 Web UI

1. Connect the HT802 to your router via Ethernet, and connect an analog phone to the configured FXS port. Power on the device and wait 60 seconds.
2. Pick up the phone and dial `***`, then dial `02` to hear the device's IP address. Write it down.
3. Open a browser and enter the IP address (remove any leading zeros — e.g., `192.168.001.010` becomes `192.168.1.10`). The interface has a timeout, so do this promptly.
4. Log in with the default **Password:** `admin`.

### Configure the HT802 FXS Port

Click **FXS PORT1** in the top menu and set the following:

- **Primary SIP Server:** `sip.telnyx.com`
- **Failover SIP Server:** (leave blank)
- **Outbound Proxy:** Leave blank (use `sip.telnyx.com` only if on firmware 1.0.15.4 or lower)
- **NAT Traversal:** `Keep-Alive`
- **SIP User ID:** Your Telnyx SIP ID
- **Authenticate ID:** Your Telnyx SIP ID
- **Authenticate Password:** Your Telnyx SIP account password
- **Name:** Outbound Caller ID — capital letters, no special characters, 15 characters max
- **DNS Mode:** `A Record`
- **SIP Registration:** `Yes`
- **Unregister on Reboot:** `No`
- **Outgoing Call Without Registration:** `Yes`
- **Register Expiration:** `5`
- **Allow Incoming SIP Messages from SIP Proxy Only:** `Yes`
- **Preferred DTMF Method:** `In-audio, RFC2833`
- **Use P-Access-Network-Info Header:** `No`
- **Use P-Emergency-Info Header:** `No`
- **Enable Call Features:** `No`
- **Dial Plan:** `{[x*]+}`
- **Preferred Vocoder:** PCMU, PCMA, G722
- **Fax Mode:** `T38`
- **Re-INVITE After Fax Tone Detected:** `Disabled`

If large faxes have a low success rate, also set:

- **Jitter Buffer Type:** `Fixed`
- **Jitter Buffer Length:** `High`
- **Disable Line Echo Canceller (LEC):** `Yes`
- **Disable Network Echo Suppressor:** `Yes`

### Prevent Direct IP Calls on the HT802

To allow calls only from Telnyx (blocking direct IP calls), enable both of these on the FXS PORT1 page:

- **Check SIP User ID for Incoming INVITE:** `Yes`
- **Allow Incoming SIP Messages from SIP Proxy Only:** `Yes`

### Complete HT802 Telnyx Portal Setup

In the [Telnyx Portal](https://portal.telnyx.com), ensure you have created:

- A [Number](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers)
- A [Connection](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection)
- An [Outbound Profile](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles)
