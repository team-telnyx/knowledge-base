---
title: Telnyx SIP Trunk Setup for Supported Desk Phones and Door Phones
summary: This page explains how to configure a Telnyx SIP trunk on several supported
  desk phones and door phones, including the Gigaset A510 IP, Gigaset A690/AS690,
  Gigaset DX800a, Dinstar C60, Mitel 6800/6900 series, and Alcatel SD601/SD602 SIP
  door phones. Each section covers prerequisites, how to access the device's web interface,
  and the SIP trunk configuration values to enter.
sources:
- url: https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup
- url: https://support.telnyx.com/en/articles/6060646-gigaset-a690-as690
- url: https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config
- url: https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
updated_at: 2026-07-17T09:10:56Z
---

# Telnyx SIP Trunk Setup for Supported Desk Phones and Door Phones

*Part 4 of 4 — see also: [Part 1](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-1.md), [Part 2](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-2.md), [Part 3](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-3.md)*

This page explains how to configure a Telnyx SIP trunk on several supported desk phones and door phones, including the Gigaset A510 IP, Gigaset A690/AS690, Gigaset DX800a, Dinstar C60, Mitel 6800/6900 series, and Alcatel SD601/SD602 SIP door phones. Each section covers prerequisites, how to access the device's web interface, and the SIP trunk configuration values to enter.

## Alcatel SD601/SD602 SIP door phones

The Alcatel SD601 and SD602 are heavy-duty access-control video door phones. The SD602 includes a 1280x760 CMOS camera, an RFID reader, and relay access control, and supports up to 2 SIP accounts. Both support door opening via DTMF, PIN code, RFID card, or indoor switch, and are IP65-rated for dust and water protection. They are compatible with the [Alcatel SP2505G IP phone](https://www.alcatel-home.com/en2/product/alcatel-sp2505g). See the [SD601 user manual](https://www.alcatel-home.com/sites/default/files/product/1507/files/alcatel-sd601-qg.pdf), [SD601 connection guide](https://www.alcatel-home.com/sites/default/files/product/1507/files/alcatel-sd601-mountingdimensions.pdf), [SD602 user manual](https://www.alcatel-home.com/sites/default/files/product/1508/files/alcatel-sd602qg.pdf), [SD601 datasheet](https://www.alcatel-home.com/sites/default/files/product/1441/files/alcatelsd601en2021.pdf), [SD602 datasheet](https://www.alcatel-home.com/sites/default/files/product/1447/files/alcatelsd602en2021.pdf), and [Alcatel product support](https://www.alcatel-home.com/en2/customer-service-after-sales-support) for additional resources.

### Connect to the web interface

1. Power on the door phone and press and hold the `#` key on the keypad for 3 seconds. The device will announce its IP address.
2. On a computer on the same network, open a browser and enter `http://<IP ADDRESS>`.
3. Log in with the default credentials:
   - **Username:** `admin`
   - **Password:** `admin`

The system uses DHCP by default. To switch to a fixed IP address (default `192.168.1.128`), press and hold the DSS key for 10 seconds until you hear a beep, then press the DSS key 3 times. After 10 seconds, the IP address acquisition mode will change.

### Configure a SIP trunk

1. From the web interface, navigate to **SYSTEM > SIP Accounts**.
2. Provide the following configuration:
   - **Phone number:** One of the DIDs you purchased from Telnyx.
   - **Display name:** The name displayed when the door phone calls your phone (the door phone's caller ID).
   - **Authentication Name:** Your Telnyx portal username.
   - **Authentication Password:** Your Telnyx portal password.
   - **Activate:** Check this box to activate the SIP trunk.
   - **SIP Proxy Server Address:** `sip.telnyx.com` (US; see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses) for other regions).
   - **SIP Proxy Server Port:** `5060`

## Related wiki pages

- [Gigaset A510: Telnyx Setup](gigaset-a510-telnyx-setup.md)
- [Gigaset A690/AS690](gigaset-a690-as690.md)
- [Gigaset: Configuring the Gigaset DX800a](gigaset-configuring-the-gigaset-dx800a.md)
- [Dinstar C60: Setup & Config](dinstar-c60-setup-config.md)
- [Mitel: 6800/6900 SIP](mitel-6800-6900-sip.md)
- [Alcatel: SD601/SD602 SIP Door](alcatel-sd601-sd602-sip-door.md)
- [Telnyx Mission Control Portal](telnyx-mission-control-portal.md)
- [TLS and SRTP](tls-and-srtp.md)
- [SIP Connection Types](sip-connection-types.md)
