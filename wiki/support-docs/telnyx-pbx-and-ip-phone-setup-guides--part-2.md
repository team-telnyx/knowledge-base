---
title: Telnyx PBX and IP Phone Setup Guides
summary: This page consolidates Telnyx setup instructions for several PBX platforms
  and IP phones, including Vodia Multi-Tenant PBX, Ubiquiti UniFi Talk (credentials
  and IP authentication), and the Fanvil H2U, H3, H3W/H5W, H5, and A32i IP phones.
  It covers prerequisites, SIP trunk configuration, codec selection, inbound routing,
  and assigning DIDs to users.
sources:
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
- url: https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup
- url: https://support.telnyx.com/en/articles/6122586-ubiquiti-trunk-unifi-talk-auth
- url: https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip
- url: https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip
- url: https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip
- url: https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip
- url: https://support.telnyx.com/en/articles/6303467-ubiquiti-trunk-unifi-talk-ip-auth
updated_at: 2026-08-05T13:35:17Z
---

# Telnyx PBX and IP Phone Setup Guides

*Part 2 of 2 — see also: [Part 1](telnyx-pbx-and-ip-phone-setup-guides--part-1.md)*

This page consolidates Telnyx setup instructions for several PBX platforms and IP phones, including Vodia Multi-Tenant PBX, Ubiquiti UniFi Talk (credentials and IP authentication), and the Fanvil H2U, H3, H3W/H5W, H5, and A32i IP phones. It covers prerequisites, SIP trunk configuration, codec selection, inbound routing, and assigning DIDs to users.

## Fanvil IP Phone Setup

The following Fanvil phones share a common configuration pattern: log into the web GUI, navigate to **Line > SIP**, populate the Register Settings (or Basic Settings on the H5), configure SIP Server 1, and adjust codec priorities.

### Common prerequisites

- Telnyx Mission Control Portal configured
- TLS encryption enabled (recommended)
- Phone running the latest firmware
- Web GUI access (default credentials are typically *admin* / *admin*; the A32i uses a default PIN of *123* for on-device configuration)

### Caller ID naming conventions

When setting the Display Name (caller ID):

- Use capital letters for better visibility on some devices
- Do not use special characters (spaces are allowed)
- Some Canadian providers truncate to 15 characters; keep the name short

### Configure a line with a Telnyx SIP trunk

1. Log into the web GUI and navigate to **Line > SIP**.
2. Use the **Line** dropdown to select a SIP line.
3. In the **Register Settings** section, provide:
   - **Username**: Telnyx SIP connection username
   - **Display Name**: Your caller ID (see naming conventions above)
   - **Realm**: Name of the realm to which the SIP interface is connected
   - **Authentication User** (or **Authentication Name**): Telnyx SIP connection username
   - **Authentication Password**: Telnyx SIP connection password
   - **Server Name**: *sip.telnyx.com* (international deployments should consult the [signaling addresses](https://sip.telnyx.com/#signaling-addresses) document)
4. In the **SIP Server 1** sub-section:
   - **Server Address**: *sip.telnyx.com*
   - **Server Port**: *5060* for TCP/UDP, *5061* for TLS
   - **Transport Protocol**: *TCP* or *UDP* (or *TLS* if encryption is configured)
   - **Proxy Server Address**: *sip.telnyx.com*

   ![SIP Server 1 sub-section.](_images/4824a0b4d660ea0c.png)
5. Optionally configure **SIP Server 2**.

### Fanvil H5 specific configuration

The H5 uses a slightly different layout with **Basic Settings** and **Advanced Settings** sections.

**Basic Settings:**

- **Username**: SIP connection username
- **Display Name**: Caller ID
- **Authentication Name**: SIP connection username
- **Authentication Password**: SIP connection password
- **SIP Proxy Address**: *sip.telnyx.com*
- **SIP Proxy Port**: *5060* (TCP/UDP) or *5061* (TLS)
- **Outbound Proxy Address**: *sip.telnyx.com*
- **Outbound Proxy Port**: *5060* (TCP/UDP) or *5061* (TLS)
- **Realm**: Name of the realm

**Advanced Settings:**

- **DTMF Type**: *RFC 2833*
- **Transport Protocol**: *TCP*, *UDP*, or *TLS* (if encrypting, also change **Lines > Dial Peer > Port** to *5061*)
- **SIP Encryption**: Enable if using TLS
- **SIP Encryption Key**: Obtain from [crt.sh](https://crt.sh/?id=1199354)

### Configure voice and video codecs

From the configured line, expand the **Codecs Settings** section and set the priority and availability of codecs. Telnyx supports:

**Audio:**

- *ulaw (g711u)*
- *alaw (g711a)*
- *g722*
- *g729*

**Video:**

- *H264*

### Fanvil phone model overview

- **Fanvil H2U Compact IP**: 2 SIP lines, 10 speed dial keys, 1 DSS key, HD audio, Opus support, PoE. Suitable for hotels, schools, hospitals, supermarkets, and residences.
- **Fanvil H3 Hotel IP**: HD audio, PoE, USB charging port, 6 programmable keys, call transfer.
- **Fanvil H3W WiFi IP**: Built-in 2.4G WiFi, HD audio, 2 SIP lines, USB charging port, 6 programmable keys, PoE.
- **Fanvil H5W WiFi IP**: Built-in 2.4G WiFi, 3.5-inch color screen, H.264 video decoding, HD audio, 2 SIP lines, PoE.
- **Fanvil H5 Hotel IP**: 3.5-inch color screen, HD audio, USB charging port, 6 programmable keys, call transfer, PoE. Available in white and black.
- **Fanvil A32i Android Console IP**: 20 SIP lines, gooseneck microphone, 10.1-inch touch screen with 112 DSS keys, optional 1080P Fanvil CM60 HD USB camera, three-way video conference, H.264 video codec, built-in Harman speaker, optional Fanvil PTM phone handle, built-in 2.4G/5G WiFi and Bluetooth, EHS wireless earphone support.

### Additional Fanvil resources

- [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
- [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
- [Fanvil support](https://www.fanvil.com/Support/ticket.html)

## Common Telnyx SIP Parameters

The following parameters are used across multiple setups. International deployments should consult the [Telnyx signaling addresses](https://sip.telnyx.com/#signaling-addresses) document for regional values.

| Parameter | Value |
| --- | --- |
| SIP Server / Proxy | *sip.telnyx.com* |
| SIP Port (TCP/UDP) | *5060* |
| SIP Port (TLS) | *5061* |
| Telnyx ACL IP | *192.76.120.10* (with */32* CIDR) |
| DTMF Type | *RFC 2833* |

## Related Articles

- [Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)
- [Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)
- [How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)
- [Asterisk: Configure an Asterisk IP trunk](https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk)
- [Elastix 5: FQDN Trunk Setup](https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup)
- [FreeSWITCH: Credentials Trunk](https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk)
- [Positron IP PBX](https://support.telnyx.com/en/articles/5790910-positron-ip-pbx)
- [ScopTEL IP PBX](https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx)
- [Fanvil X2CP/X2C/X2P: Call Center IP](https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip)
- [Fanvil V-Series: IP Phones](https://support.telnyx.com/en/articles/6209862-fanvil-v-series-ip-phones)
- [Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)
- [Fanvil XU Series: IP Phone](https://support.telnyx.com/en/articles/6210147-fanvil-xu-series-ip-phone)
