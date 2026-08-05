---
title: Telnyx Device Configuration Guides
summary: Step-by-step instructions for configuring Telnyx SIP trunks on a range of
  supported devices, including the Ribbon EdgeMarc 6000 SBC, Snom M100 KLE base station,
  Mitel 5320E/5330E/5340E and 6800/6900 SIP phones, and Alcatel SD601/SD602 SIP door
  phones. Each guide covers prerequisites, device access, SIP server settings, and
  registration parameters required to connect the device to the Telnyx Mission Control
  Portal.
sources:
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
updated_at: 2026-08-05T13:36:02Z
---

# Telnyx Device Configuration Guides

*Part 4 of 4 — see also: [Part 1](telnyx-device-configuration-guides--part-1.md), [Part 2](telnyx-device-configuration-guides--part-2.md), [Part 3](telnyx-device-configuration-guides--part-3.md)*

Step-by-step instructions for configuring Telnyx SIP trunks on a range of supported devices, including the Ribbon EdgeMarc 6000 SBC, Snom M100 KLE base station, Mitel 5320E/5330E/5340E and 6800/6900 SIP phones, and Alcatel SD601/SD602 SIP door phones. Each guide covers prerequisites, device access, SIP server settings, and registration parameters required to connect the device to the Telnyx Mission Control Portal.

## Alcatel SD601/SD602 SIP Door Phone Setup

The [Alcatel SD601](https://www.alcatel-home.com/en2/product/alcatel-sd601) and [SD602](https://www.alcatel-home.com/en2/product/alcatel-sd602) SIP door phones are heavy-duty access-control video solutions. The SD602 includes a 1280x760 CMOS camera, RFID reader, and relay access control, and supports up to 2 SIP accounts. Both support door opening via [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf), PIN code, RFID card, or indoor switch, and are IP65 rated for dust and water protection.

Additional resources: [SD601 user manual](https://www.alcatel-home.com/sites/default/files/product/1507/files/alcatel-sd601-qg.pdf), [SD601 connection guide](https://www.alcatel-home.com/sites/default/files/product/1507/files/alcatel-sd601-mountingdimensions.pdf), [SD602 user manual](https://www.alcatel-home.com/sites/default/files/product/1508/files/alcatel-sd602qg.pdf), [SD601 datasheet](https://www.alcatel-home.com/sites/default/files/product/1441/files/alcatelsd601en2021.pdf), [SD602 datasheet](https://www.alcatel-home.com/sites/default/files/product/1447/files/alcatelsd602en2021.pdf), [Alcatel product support](https://www.alcatel-home.com/en2/customer-service-after-sales-support).

### Connect to the Web Interface

1. Power on the door phone and press and hold the `#` key for 3 seconds. The device will announce its IP address.
2. From a computer on the same network, open a browser and enter `http://<IP_ADDRESS>`.
3. Log in with default credentials:
   - **Username:** `admin`
   - **Password:** `admin`

The device uses DHCP by default. To switch to a fixed IP address (default `192.168.1.128`), press and hold the DSS key for 10 seconds until a beep sounds, then press the DSS key 3 times.

### Configure the SIP Trunk

1. Navigate to **SYSTEM > SIP Accounts**.
2. Enter the following:
   - **Phone number:** A DID purchased from Telnyx
   - **Display name:** Caller ID for the door phone
   - **Authentication Name:** Telnyx portal username
   - **Authentication Password:** Telnyx portal password
   - **Activate:** Check to enable the SIP trunk
   - **SIP Proxy Server Address:** `sip.telnyx.com` (US; see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses))
   - **SIP Proxy Server Port:** `5060`

## Related Pages

- [Grandstream UMC6202: Auth Setup](grandstream-umc6202-auth-setup.md)
- [Sansay: SBC VSXi Setup](sansay-sbc-vsxi-setup.md)
- [Yeastar S-Series: Telnyx SIP](yeastar-s-series-telnyx-sip.md)
- [Xorcom PBX: SIP Trunk](xorcom-pbx-sip-trunk.md)
- [How to configure Yeastar P-series](how-to-configure-yeastar-p-series.md)
- [Konftel 300Wx: Telnyx Setup](konftel-300wx-telnyx-setup.md)
- [Snom C520: Telnyx Setup](snom-c520-telnyx-setup.md)
- [Grandstream GXP: Telnyx Setup](grandstream-gxp-telnyx-setup.md)
- [Konftel 300IPx: Telnyx Setup](konftel-300ipx-telnyx-setup.md)
- [MicroSIP: Setup with Telnyx](microsip-setup-with-telnyx.md)
- [Grandstream GRP2612: SIP Trunk](grandstream-grp2612-sip-trunk.md)
- [Grandstream GXP1700: SIP Trunk](grandstream-gxp1700-sip-trunk.md)
- [Fanvil H5: Hotel IP](fanvil-h5-hotel-ip.md)
- [Fanvil XU Series: IP Phone](fanvil-xu-series-ip-phone.md)
- [Mitel: 6800/6900 SIP](mitel-6800-6900-sip.md)
- [Grandstream GRP260x: SIP Trunk](grandstream-grp260x-sip-trunk.md)
- [Fanvil X-Series: IP Phone](fanvil-x-series-ip-phone.md)
- [Fanvil H3W/H5W: WiFi IP](fanvil-h3w-h5w-wifi-ip.md)
