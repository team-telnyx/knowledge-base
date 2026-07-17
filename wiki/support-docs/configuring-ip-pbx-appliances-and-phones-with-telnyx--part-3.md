---
title: Configuring IP PBX Appliances and Phones with Telnyx
summary: This page provides step-by-step instructions for configuring several popular
  IP PBX appliances and IP phones to work with Telnyx as the SIP carrier, including
  the Grandstream UCM6202 (using both Registration and IP authentication), the broader
  Grandstream UCM6xxx series, the Synway UC-200, and the Cisco 68xx/88xx series IP
  phones. Each section covers logging into the device's web UI, creating a SIP trunk,
  configuring inbound and outbound routes, and setting an outbound caller ID where
  applicable.
sources:
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
- url: https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup
- url: https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks
- url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
updated_at: 2026-07-17T09:08:00Z
---

# Configuring IP PBX Appliances and Phones with Telnyx

*Part 3 of 3 — see also: [Part 1](configuring-ip-pbx-appliances-and-phones-with-telnyx--part-1.md), [Part 2](configuring-ip-pbx-appliances-and-phones-with-telnyx--part-2.md)*

This page provides step-by-step instructions for configuring several popular IP PBX appliances and IP phones to work with Telnyx as the SIP carrier, including the Grandstream UCM6202 (using both Registration and IP authentication), the broader Grandstream UCM6xxx series, the Synway UC-200, and the Cisco 68xx/88xx series IP phones. Each section covers logging into the device's web UI, creating a SIP trunk, configuring inbound and outbound routes, and setting an outbound caller ID where applicable.

## Cisco 68xx/88xx Setup

The Cisco 68xx and 88xx series are multiplatform IP phones designed for affordability, delivering reliable business-grade audio with Gigabit Ethernet integration. The setup and configuration for both series are identical.

### Pre-requisites

- Telnyx Mission Control Portal configured properly
- TLS encryption enabled (recommended)
- For TLS accounts: a TLS certificate may be required (obtainable from [crt.sh](https://crt.sh/?id=1199354))

### Get the Device IP and Log into the Web Portal

1. On the phone, press the **Menu** button and navigate to **Network Status > IPv4 Address**. Note the IP address.
2. On a computer on the same network, open a browser and enter `http://` followed by the phone's IP address.
3. Log into the portal. Out of the box, you can skip the login credentials by pressing **Skip**.

### Configure a SIP Extension

1. Click the **Voice** tab, then click the tab showing the extension to configure.
2. In **General and NAT Settings**:
   - **Line Enable:** Yes
   - **NAT Mapping Enable:** Yes
   - **NAT Keep Alive Enable:** Yes
3. In **SIP Settings**:
   - **SIP Transport:** UDP or TCP (or TLS if encrypting)
   - **SIP Port:** 5060 (or 5061 for TLS)
4. In **Proxy and Registration**:
   - **Proxy:** `sip.telnyx.com`
   - **Outbound Proxy:** `sip.telnyx.com`
   - **Register:** Yes
   - **Register Expires:** 300
5. In **Subscriber Information**:
   - **Display Name:** Your caller ID (capital letters, no special characters, max 15 characters)
   - **User ID:** Your Telnyx account ID
   - **Password:** Your Telnyx account password
   - **Auth ID:** Your Telnyx account ID
6. In **Audio Configuration**, set codecs in priority sequence. Telnyx supports `ulaw(g711u)`, `alaw(g711a)`, `g722`, and `g729`. If using TLS, set **Encryption Method** to **AES128**.

### Additional Security Settings (TLS Only)

If you have configured TLS call encryption:

1. On the **Voice** tab, click the **User** sub-tab.
2. In **Supplementary Services**, set **Secure Call Setting** to **Yes**.
3. If your device requires a TLS certificate (such as the 6821), obtain it from [crt.sh](https://crt.sh/?id=1199354). On the **Voice** tab, click the **Provisioning** sub-tab and paste the certificate link in the **Custom CA Rule** field.
4. Click **Submit All Changes**. Do not unplug the phone while it displays "Phone is updating configuration".

## Additional Resources

- [Getting started with Mission Control](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- [Does Telnyx encrypt communication?](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
- [Telnyx caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)
- [Grandstream UCM6200 series product page](https://www.grandstream.com/products/ip-pbxs/ucm-series-ip-pbxs/product/ucm6200-series)
- [Grandstream UCM6200 series datasheet](https://www.grandstream.com/hubfs/Product_Documentation/datasheet_ucm6200_series_english.pdf?hsLang=en)
- [Grandstream UCM62xx administrator's user manual](https://www.grandstream.com/hubfs/Product_Documentation/ucm62xx_usermanual.pdf)
- [Grandstream firmware updates](https://www.grandstream.com/support/firmware)
- [Synway user documentation](https://wiki.synway.net/index.php/User_Manual)
- [Synway UC-200 user manual](https://www.synway.net/Download/Manual/UserManual/IPPBX_User_ManualV1.8.0.pdf)
- [Cisco 68xx series support](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/series.html)
- [Cisco 88xx series support](https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/index.html?dtid=osscdc000283)
- [Asterisk dialplan patterns](https://www.voip-info.org/asterisk-dialplan-patterns/)
- [Telnyx signaling addresses](https://sip.telnyx.com/#signaling-addresses)
- [Telnyx audio codecs overview](https://telnyx.com/resources/codecs-affect-voip-sound-quality)
- [What is DTMF?](https://support.telnyx.com/en/articles/1130710-what-is-dtmf)
