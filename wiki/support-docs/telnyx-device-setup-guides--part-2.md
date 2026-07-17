---
title: Telnyx Device Setup Guides
summary: Consolidated Telnyx setup guides for SIP-capable desk phones, conference
  phones, and ATAs (Polycom VVX 300-series, Poly OBi300, FortiFone FON-570/375/175/H25,
  Flyingvoice, Snom C520, and Snom D7xx), plus a Linksys ATA dialplan reference. Each
  guide covers obtaining the device IP, logging into the web portal, and entering
  Telnyx SIP credentials (server sip.telnyx.com, ports 5060/5061, supported codecs,
  and caller ID naming conventions).
sources:
- url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
- url: https://support.telnyx.com/en/articles/5810226-fortifone-fon-570
- url: https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup
- url: https://support.telnyx.com/en/articles/5811545-fortifone-setup-fon-375-175-h25
- url: https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup
- url: https://support.telnyx.com/en/articles/5820183-plantronics-polycom-obi300-setup
- url: https://support.telnyx.com/en/articles/5822706-snom-d7xx-telnyx-setup
updated_at: 2026-07-17T09:10:21Z
---

# Telnyx Device Setup Guides

*Part 2 of 4 — see also: [Part 1](telnyx-device-setup-guides--part-1.md), [Part 3](telnyx-device-setup-guides--part-3.md), [Part 4](telnyx-device-setup-guides--part-4.md)*

Consolidated Telnyx setup guides for SIP-capable desk phones, conference phones, and ATAs (Polycom VVX 300-series, Poly OBi300, FortiFone FON-570/375/175/H25, Flyingvoice, Snom C520, and Snom D7xx), plus a Linksys ATA dialplan reference. Each guide covers obtaining the device IP, logging into the web portal, and entering Telnyx SIP credentials (server sip.telnyx.com, ports 5060/5061, supported codecs, and caller ID naming conventions).

## FortiFone FON-570

The [FortiFone FON-570](https://www.fortinet.com/products/business-phone-systems/fortivoice-fortifone/phones-softclients) is a top-line model with a 7" color screen, 7 dedicated feature keys, 109 programmable phone keys, full-duplex speakerphone, dual 10/100/1000 Ethernet ports, and integrated PoE.

### Get the device IP address

1. Press the **OK** button on the phone, or the **Menu** button on the screen.
2. Click **Status** on-screen.

![Main Menu button on the screen](_images/bdbbb435b45430f5.jpg)

3. The IP address is shown on the **Status** page.

![IP address status page](_images/b48ebd830c937dd6.jpg)

### Set up the FortiFone for traffic flow

1. Open a browser and enter `http://<IP address>`. Default credentials: `admin` / `23646`.

![Login credentials input section](_images/5a69dacd06c6f94e.jpg)

2. Click the **Account** tab and select **Register** in the left-hand navigation. Enter:

- **Line Active:** `Enabled`.
- **Label:** a recognizable name.
- **Display Name:** caller ID (follow naming conventions).
- **Register Name:** Telnyx SIP account username.
- **User Name:** Telnyx SIP account username.
- **Password:** Telnyx SIP account password.
- **Server Host:** `sip.telnyx.com`.
- **Port:** `5060` (UDP) or `5061` (TLS).
- **Transport:** `UDP` by default; choose `TLS` if TLS/SRTP is enabled.
- **Server Expires:** `300`.
- **Server Retry Counts:** `3` (default).

![Fortinet Account tab](_images/5b475a1a2e9b4f73.jpg)

3. (Optional, required for TLS) Click **Advanced** in the left-hand navigation and set **RTP Encryption (SRTP):** `Compulsory`.

![Fortinet Account tab advanced settings](_images/a4de47c6d3173f66.jpg)

4. Click the **Settings** tab, then **Date and Time** in the left-hand navigation:

- **Time Synchronized via DHCP:** `Yes`.
- **Time zone:** select from the drop-down.
- **Location:** select for daylight saving.
- **Primary Server:** `pool.ntp.org` (optional).
- **Time Format:** 12-hour or 24-hour.
- **Date Format:** preferred format.

![Time and date settings](_images/bdd6dd85bcabe4a9.jpg)

5. Click **Confirm**.

Additional resources: [FortiFONE documentation](https://www.fortinet.com/search?q=fortifone) and [Fortinet support](https://www.fortinet.com/support/contact).

## FortiFone FON-375/175/H25

This guide also covers the FortiFone FON-175 and FortiFone FON-H25. The FON-570 is a top-line model with a 7" color screen, 7 dedicated feature keys, 109 programmable phone keys, full-duplex speakerphone, dual 10/100/1000 Ethernet ports, and integrated PoE.

### Get the device IP address

1. Tap the **Menu** button on the LCD screen and select **Status** to see the IP address.

![FortiFone menu button](_images/b79ff1fa8e26a66e.png)

![FortiFone status button](_images/6f4a7ead89b71d0a.jpg)

![FortiFone mode button](_images/6543bc1e5c27c7a5.jpg)

### Set up the FortiFone for traffic flow

1. Open a browser and enter `http://<IP address>`. Default credentials: `admin` / `23656`.

![Fortinet credentials settings section](_images/e5e98bb96bc44a9a.jpg)

2. Click **Line** in the left-hand menu and select the **SIP** tab. In the **Line** section, enter:

- **Username:** SIP main or sub-account username.
- **Display Name:** caller ID (follow naming conventions).
- **Authentication Name:** SIP main or sub-account username.
- **Authentication Password:** SIP main or sub-account password.
- **Server Name:** `sip.telnyx.com`.
- **Register Address:** `sip.telnyx.com`.
- **Register Port:** `5060` (UDP) or `5061` (TLS).
- **Activate:** checked.

![Line button](_images/a38c97efa00a5c0f.png)

3. In the **Advanced** section:

- **Transportation Protocol:** `UDP` by default; choose `TLS` if TLS/SRTP is enabled.

4. (Optional, required for TLS) Still in **Advanced**:

- **Transportation Protocol:** `TCP`.
- **RTP Encryption:** checked.

![SIP section of the Line section](_images/d63dfe9ff96ad338.jpg)

Additional resources: [FortiFONE documentation](https://www.fortinet.com/search?q=fortifone) and [Fortinet support](https://www.fortinet.com/support/contact).

## Flyingvoice IP Phones

[Flyingvoice](https://www.flyingvoice.com/) provides VoIP phones, ATAs, gateways, and routers. Their WiFi IP phones eliminate the need for a hard-wired internet connection. This guide covers the [entire range of Flyingvoice IP phones](https://www.flyingvoice.com/products.html).

Pre-requisites: Telnyx Mission Control Portal configured (with an extension/sub-account), TLS recommended.

### Physically connect the phone to a network

Connect the phone to the same network as the computer used for configuration.

![Network topology picture](_images/f2fed8dc10a564f9.jpg)

### Get the device IP address and log into the web portal

1. Turn on the phone. After initialization, the LCD shows the date, time, and IP address.
2. Open a browser and enter `http://<IP address>`. Default credentials: `admin` / `admin`.

![Phone's web portal](_images/bea52c1602d06277.jpg)

### Set up the Flyingvoice phone for traffic flow

1. Click the **SIP Account** tab, then the **Line 1** sub-tab. Configure:

- **Line Enable:** `Enable`.
- **Display Name:** caller ID (follow naming conventions).
- **Phone Number:** Telnyx username.
- **Account:** Telnyx username.
- **Password:** Telnyx password.
- **Proxy Server:** `sip.telnyx.com`.
- **Proxy Port:** `5060` (UDP) or `5061` (TLS).
- **Transport:** `UDP` by default; choose `TLS` if TLS/SRTP is enabled.

![SIP account tab](_images/3bf4132a1001341f.png)

- **Voice Mailbox Numbers:** `*97`.

![Voice mailbox settings](_images/2f8167932ade9777.png)

- **Register Refresh Interval (sec):** `180`.

![Refresh interval section](_images/921fb0733141cb3d.png)

- **RTP Port Min:** `100001`.
- **RTP Port Max:** `200000`.

![RTP Port Min section](_images/e86c7fd51b700d3d.png)

2. Click **Save & Apply**.

### (Optional) Set the Multiple Line button

1. Click the **Phone** tab, then the **Line Key** sub-tab.

![Phone tab section](_images/205cbdaae202e6b7.png)

2. In the **Dsskey** table, locate the LineKey number and provide:

- **Type:** `Line`.
- **Line:** `Line 1`.
- **Label:** e.g., `L1`, `Line1`, or the extension number.

![Dsskey section](_images/1e5ef7c2ce151093.png)

3. Click **Save**.

### (Optional) Set up a SIP trunk from the phone

1. From the phone screen, navigate to **Menu > Advanced**.
2. Enter the default password `admin`.
3. Go to **Accounts > Line 1** and enable **Registration**.
4. Enter:

- **Phone Number:** Telnyx username.
- **Account:** (Telnyx username).
- **Password:** Telnyx password.
- **Display Name:** caller ID (follow naming conventions).
- **Register Name:** Telnyx username.
- **User Name:** Telnyx username.
- **Password:** Telnyx password.
- **SIP Server:** `sip.telnyx.com`.
- **SIP Port:** `5060` (UDP) or `5061` (TLS).

![Menu > Advanced settings section of the web portal](_images/476b1b610f0c0bba.png)

![Menu > Advanced settings section of the web portal](_images/bea44c4d13bbac9d.png)

5. Press **OK**.

Additional resources: [Flyingvoice documentation, firmware, and product detail](https://www.flyingvoice.com/download.html), [Flyingvoice training videos](https://www.flyingvoice.com/training.html), and [Flyingvoice FAQs](https://www.flyingvoice.com/Faq/index.html).
