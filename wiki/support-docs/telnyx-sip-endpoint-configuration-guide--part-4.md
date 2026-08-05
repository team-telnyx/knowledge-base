---
title: Telnyx SIP Endpoint Configuration Guide
summary: This page consolidates Telnyx setup instructions for a range of SIP endpoints
  — softphones, conference phones, and desk IP phones — covering Acrobits, BuddyTalk,
  FortiFone, Gigaset, and Vtech devices. Each section walks through prerequisites,
  obtaining the device IP address, registering the device with the Telnyx SIP service
  at sip.telnyx.com, and configuring transport, audio, and caller ID settings.
sources:
- url: https://support.telnyx.com/en/articles/5761112-acrobits-softphone
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
- url: https://support.telnyx.com/en/articles/5810226-fortifone-fon-570
- url: https://support.telnyx.com/en/articles/5811545-fortifone-setup-fon-375-175-h25
- url: https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup
- url: https://support.telnyx.com/en/articles/6060646-gigaset-a690-as690
- url: https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a
updated_at: 2026-08-05T13:36:59Z
---

# Telnyx SIP Endpoint Configuration Guide

*Part 4 of 4 — see also: [Part 1](telnyx-sip-endpoint-configuration-guide--part-1.md), [Part 2](telnyx-sip-endpoint-configuration-guide--part-2.md), [Part 3](telnyx-sip-endpoint-configuration-guide--part-3.md)*

This page consolidates Telnyx setup instructions for a range of SIP endpoints — softphones, conference phones, and desk IP phones — covering Acrobits, BuddyTalk, FortiFone, Gigaset, and Vtech devices. Each section walks through prerequisites, obtaining the device IP address, registering the device with the Telnyx SIP service at sip.telnyx.com, and configuring transport, audio, and caller ID settings.

## Vtech VCS754 ErisStation

The [Vtech VCS754 ErisStation](https://www.vtechphones.com/support/technical-support) is a compact all-in-one conference phone with built-in charging stations and magnetic bays for portable DECT 6.0 microphones using Orbitlink Wireless Technology.

### Get the device's IP address and log into the web portal

1. Press the **Menu** button on the phone.
2. Scroll to **Status** and select **Network**. Note the IP address.
3. From a computer on the same network, open a browser and navigate to `http://<device-ip>`.
4. Log in with the default credentials:
   - **User:** `admin`
   - **Password:** `admin`

### Configure the VCS754 conference phone

1. Click the **System** tab.
2. In the left-hand navigation, select the account to configure to open the editor.
3. In **General Account Settings**, enter:
   - **Account Label:** A descriptive name
   - **Display Name:** Your caller ID (follow the naming conventions above)
   - **User Identifier:** Your Telnyx account ID
   - **Authentication Name:** Your Telnyx account ID
   - **Authentication Password:** Your Telnyx account password
   - **Dial Plan:** `x+P` (default)
4. In the **SIP Server** section, enter:
   - **Server Address:** `sip.telnyx.com`
   - **Port:** `5060` (no TLS) or `5061` (TLS enabled)
5. Use the same values in the **Registration**, **Outbound Proxy**, and **Backup Outbound Proxy** sections.

   ![Registration, Outbound Proxy, Backup Outbound Proxy sections.](_images/074bbca14409d4f6.png)
6. In the **Audio** section, configure:
   - **Ringer Tone:** As preferred
   - **Codec Priority:** Set in priority order — `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - **Enable Voice Encryption (SRTP):** Checked if using TLS/encryption

   ![Audio section](_images/28eef1e4a20879dd.png)

### Configure signaling settings

1. Click the **System** tab.
2. In the left-hand navigation, select **Signaling Settings** and enter:
   - **Local SIP Port:** `5060` (no TLS) or `5061` (TLS enabled)
   - **Transport:** `UDP` or `TCP` (no TLS); `TLS/TCP` if TLS is enabled

### Additional Vtech VCS754 resources

- [Administrator and provisioning manual](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_Admin_Provisioning_Manual%20-%20Rev%204.pdf)
- [User manual](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_User_Guide%20-%20Rev%204.pdf)
- [Quick start guide](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_QSG%20-%20Rev%203.pdf)
- [Quick start guide (WM version)](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754-WM_QSG%20-%20Rev%203.pdf)
- [Vtech product support](https://www.vtechphones.com/support/technical-support)

---

## Related wiki pages

- [Configuring Linphone with Telnyx](configuring-linphone-with-telnyx.md)
- [MicroSIP: Setup with Telnyx](microsip-setup-with-telnyx.md)
- [Grandstream Wave Lite (iPhone)](grandstream-wave-lite-iphone.md)
- [Grandstream Wave Lite (Android)](grandstream-wave-lite-android.md)
- [Grandstream DP752](grandstream-dp752.md)
- [Audiocodes 400HD](audiocodes-400hd.md)
- [Vtech VCS754: Telnyx Setup](vtech-vcs754-telnyx-setup.md)
- [Algo 8xxx: Telnyx Endpoints](algo-8xxx-telnyx-endpoints.md)
- [FortiFone Setup: FON-375/175/H25](fortifone-setup-fon-375-175-h25.md)
- [Panasonic KX-HDV: Telnyx setup](panasonic-kx-hdv-telnyx-setup.md)
- [Gigaset A510: Telnyx Setup](gigaset-a510-telnyx-setup.md)
- [Gigaset A690/AS690](gigaset-a690-as690.md)
- [Gigaset: Configuring the Gigaset DX800a](gigaset-configuring-the-gigaset-dx800a.md)
- [Snom C520: Telnyx Setup](snom-c520-telnyx-setup.md)
- [Konftel 300IPx: Telnyx Setup](konftel-300ipx-telnyx-setup.md)
- [Fanvil A32i: Telnyx Setup](fanvil-a32i-telnyx-setup.md)
- [Fanvil H2U: Compact IP](fanvil-h2u-compact-ip.md)
- [Fanvil H3: Hotel IP](fanvil-h3-hotel-ip.md)
- [Fanvil H5: Hotel IP](fanvil-h5-hotel-ip.md)
- [Fanvil X-Series: IP Phone](fanvil-x-series-ip-phone.md)
- [Fanvil X2CP/X2C/X2P: Call Center IP](fanvil-x2cp-x2c-x2p-call-center-ip.md)
- [Flyingvoice: Telnyx Setup](flyingvoice-telnyx-setup.md)
