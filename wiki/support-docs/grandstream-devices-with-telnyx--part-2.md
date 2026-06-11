---
title: Grandstream Devices with Telnyx
summary: How to configure Grandstream IP phones and adapters—including the GXP16XX,
  GXP21XX, HT802, and DP752—to connect with the Telnyx Mission Control Portal for
  SIP calling and faxing.
sources:
- url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
  content_hash: a651066b20e770d097f2fa88a93cf6985a0b9c4b3295a91fc81a360298814d71
- url: https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup
  content_hash: d36408a50b43a803c90740a44fb56ccd93d2c1d9afd32e5992abde8b5ddd7a22
- url: https://support.telnyx.com/en/articles/5808368-grandstream-dp752
  content_hash: e813aeefa51a0d10472bcf6d9ebbc12afff274476e69058f07ae50985597d9ba
- url: https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup
  content_hash: cf43b29433ed3c67b95ef6c89238d2ec11716db66f6fb79a97a6366185959e41
- url: https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx
  content_hash: 4dab62a704117ec649e0377a0311a8d31690a8de9d164c9193f9bf0221f76659
updated_at: 2026-06-11T11:31:45Z
---

# Grandstream Devices with Telnyx

*Part 2 of 2 — see also: [Part 1](grandstream-devices-with-telnyx--part-1.md)*

How to configure Grandstream IP phones and adapters—including the GXP16XX, GXP21XX, HT802, and DP752—to connect with the Telnyx Mission Control Portal for SIP calling and faxing.

## DP752 DECT Cordless

The Grandstream DP752 base station pairs with up to 5 DP722 handsets and supports up to 10 SIP accounts with full HD audio. This guide also applies to the DP750 base station.

### Get the DP752 IP Address

1. On a DP72x or DP730 handset, press **Menu**.
2. Navigate to **Status > Base Status** and press **Select** to display the base station's IP address.

### Configure DP752 Profile and SIP Settings

1. Open a browser and enter `http://` followed by the base station's IP address. Log in with **Username:** `admin`, **Password:** `admin`.
2. From the left navigation, expand **Profiles > Profile 1 > General Settings** and set:
   - **Profile Active:** `Yes`
   - **Profile Name:** A descriptive name
   - **SIP Server:** `sip.telnyx.com`
   - **Failover SIP Server:** `sip.telnyx.com` (secondary SIP proxy for failover)
   - **Prefer Primary SIP Server:** `Yes`
   - **Outbound Proxy:** `sip.telnyx.com`
   - **Voice Mail Access Number:** `*97`
3. Click **Save**, then **Apply**.
4. Navigate to **SIP Settings > Basic Settings** and set:
   - **SIP Transport:** `UDP` (default) or `TLS` if encryption is enabled
   - **Local SIP Port:** `5060` (UDP) or `5061` (TLS)
5. Click **Save**, then **Apply**.

### Configure DP752 Codecs

Under **Profiles > Profile 1**:

- **Send DTMF:** Select *In-Audio* and *via RTP*
- **SRTP Mode:** If using TLS, select *Enabled and Forced*; otherwise leave as default

Click **Save**, then **Apply**.

### Configure DP752 SIP Accounts and Handsets

1. Navigate to **DECT > SIP Account Settings** and configure each account:
   - **SIP User ID:** Your Telnyx account ID
   - **Authenticate ID:** Your Telnyx account ID
   - **Password:** Your Telnyx account password
   - **Name:** Caller ID — capital letters, no special characters, 15 characters max
   - **Profile:** Select the profile created above
   - **HS Mode:** Choose a hunting group mode:
     - *Circular:* phones ring sequentially, rotating the starting phone
     - *Linear:* phones ring sequentially in a fixed order
     - *Parallel:* all phones ring concurrently; after one answers, others can make new calls
     - *Shared:* all phones ring concurrently and always share the same line
     - *Non-Hunting Group:* account assigned to a single specific handset
   - **Active:** `Yes`
2. Click **Save**, then **Apply**.
3. Navigate to **DECT > Handset Line Settings** and ensure the SIP account is selected in the Line 1 column for every handset.
4. Click **Save**, then **Apply**.

## Troubleshooting

### Outgoing Calls Fail with "No Response"

If incoming calls work but outgoing calls fail with a *No response* error:

1. Go to **Accounts > Account X > SIP > Custom SIP Header** and **disable**:
   - **Use X-Grandstream-PBX Header**
   - **Use P-Access-Network-Info Header**
   - **Use P-Emergency-Info Header**
2. Go to **Accounts > Account X > SIP > Audio Settings** and set the preferred vocoder to **G729A/B**, with the remaining codecs set to **PCMU**.

## Additional Resources

- [Grandstream firmware updates](https://www.grandstream.com/support/firmware)
- [GXP16XX administration guide](https://www.grandstream.com/hubfs/Product_Documentation/gxp16xx_administration_guide.pdf)
- [GXP21XX administration guide](https://www.grandstream.com/hubfs/Product_Documentation/gxp21xx_administration_guide.pdf)
- [HT802 user guide](https://www.grandstream.com/hubfs/Product_Documentation/ht80x_user_guide.pdf)
- [DP750/DP720 user guide](https://www.grandstream.com/hubfs/Product_Documentation/DP750_DP720_User_Guide.pdf)
- [DP750/DP720 administration guide](https://www.grandstream.com/hubfs/Product_Documentation/DP750_DP720_Administration_Guide.pdf)
- [Grandstream FAQ](https://blog.grandstream.com/faq)
- [Grandstream community forum](https://forums.grandstream.com/)
- [Grandstream Learning Center](https://www.grandstream.com/learning-center)
- [Grandstream Helpdesk](https://helpdesk.grandstream.com/)
- [Getting Started with a Mission Control Account](getting-started-with-a-mission-control-account.md)
