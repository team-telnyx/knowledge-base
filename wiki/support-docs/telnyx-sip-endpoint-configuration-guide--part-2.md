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

*Part 2 of 4 — see also: [Part 1](telnyx-sip-endpoint-configuration-guide--part-1.md), [Part 3](telnyx-sip-endpoint-configuration-guide--part-3.md), [Part 4](telnyx-sip-endpoint-configuration-guide--part-4.md)*

This page consolidates Telnyx setup instructions for a range of SIP endpoints — softphones, conference phones, and desk IP phones — covering Acrobits, BuddyTalk, FortiFone, Gigaset, and Vtech devices. Each section walks through prerequisites, obtaining the device IP address, registering the device with the Telnyx SIP service at sip.telnyx.com, and configuring transport, audio, and caller ID settings.

## FortiFone FON-570

The [FortiFone FON-570](https://www.fortinet.com/products/business-phone-systems/fortivoice-fortifone/phones-softclients) is a top-line Fortinet desk phone with a 7" color screen, 7 dedicated feature keys, 109 programmable phone keys, full-duplex speakerphone, dual 10/100/1000 Ethernet ports, and integrated PoE.

### Get the device's IP address

1. On the phone, press **OK** or the **Menu** button on screen.
2. Tap **Status**.

   ![Main Menu button on the screen.](_images/bdbbb435b45430f5.jpg)
3. Note the IP address shown on the **Status** page.

   ![IP address status page.](_images/b48ebd830c937dd6.jpg)

### Set up the FortiFone for traffic flow

1. From a computer on the same network, open a browser and navigate to `http://<device-ip>`.
2. Log in with the default credentials (change them after first login):
   - **Username:** `admin`
   - **Password:** `23646`

   ![Login credentials input section.](_images/5a69dacd06c6f94e.jpg)
3. Click the **Account** tab and select **Register** in the left-hand navigation. Enter:
   - **Line Active:** `Enabled`
   - **Label:** A recognizable name for the account
   - **Display Name:** Your caller ID (follow the naming conventions above)
   - **Register Name:** Your Telnyx SIP account username
   - **User Name:** Your Telnyx SIP account username
   - **Password:** Your Telnyx SIP account password
   - **Server Host:** `sip.telnyx.com`
   - **Port:** `5060` for UDP, `5061` for TLS
   - **Transport:** `UDP` by default; choose `TLS` if you have enabled TLS/SRTP
   - **Server Expires:** `300`
   - **Server Retry Counts:** `3` (default)

   ![Fortinet Account Tab.](_images/5b475a1a2e9b4f73.jpg)
4. (Optional, required if encrypting traffic) Click **Advanced** in the left-hand navigation and set **RTP Encryption (SRTP)** to `Compulsory`.

   ![Fortinet Account tab for advanced settings.](_images/a4de47c6d3173f66.jpg)
5. Click the **Settings** tab and then **Date and Time** in the left-hand navigation. Configure:
   - **Time Synchronized via DHCP:** `Yes`
   - **Time zone:** Select from the drop-down
   - **Location:** Select your location for daylight saving
   - **Primary Server:** `pool.ntp.org` (optional)
   - **Time Format:** 12-hour or 24-hour
   - **Date Format:** As preferred

   ![Time and date settings.](_images/bdd6dd85bcabe4a9.jpg)
6. Click **Confirm**.

### Additional FortiFone resources

- [FortiFONE documentation](https://www.fortinet.com/search?q=fortifone)
- [Fortinet support](https://www.fortinet.com/support/contact)

---

## FortiFone FON-375 / FON-175 / FON-H25

This procedure also covers the FortiFone FON-175 and FON-H25 models. The FON-375 is a Fortinet desk phone with HD audio and PoE support.

### Get the device's IP address

1. On the phone, tap the **Menu** button on the LCD screen and select **Status**.

   ![FortiFone menu button.](_images/b79ff1fa8e26a66e.png)

   ![FortiFone status button.](_images/6f4a7ead89b71d0a.jpg)

   ![FortiFone mode button.](_images/6543bc1e5c27c7a5.jpg)
2. Note the IP address.

### Set up the FortiFone for traffic flow

1. From a computer on the same network, open a browser and navigate to `http://<device-ip>`.
2. Log in with the default credentials (change them after first login):
   - **Username:** `admin`
   - **Password:** `23656`

   ![Fortinet credentials settings section.](_images/e5e98bb96bc44a9a.jpg)
3. In the left-hand menu, click **Line** and select the **SIP** tab. In the **Line** section, enter:
   - **Username:** Your SIP main or sub account username
   - **Display Name:** Your caller ID (follow the naming conventions above)
   - **Authentication Name:** Your SIP main or sub account username
   - **Authentication Password:** Your SIP main or sub account password
   - **Server Name:** `sip.telnyx.com`
   - **Register Address:** `sip.telnyx.com`
   - **Register Port:** `5060` for UDP, `5061` for TLS
   - **Activate:** Checked

   ![Line button.](_images/a38c97efa00a5c0f.png)
4. In the **Advanced** section on the same tab:
   - **Transportation Protocol:** `UDP` by default; choose `TLS` if you have enabled TLS/SRTP.
5. (Optional, required if encrypting traffic) Still in **Advanced**:
   - **Transportation Protocol:** `TCP`
   - **RTP Encryption:** Checked

   ![SIP section of the Line section.](_images/d63dfe9ff96ad338.jpg)

### Additional FortiFone resources

- [FortiFONE documentation](https://www.fortinet.com/search?q=fortifone)
- [Fortinet support](https://www.fortinet.com/support/contact)

---

## Gigaset A510 IP

The [Gigaset A510 IP](https://gse.gigaset.com/fileadmin/legacy-assets/A31008-M2230-R301-2-6019_en_US_CA.pdf) is a versatile VoIP phone that supports up to 3 parallel calls (2 VoIP + 1 landline) and lets you switch between them at the press of a button.

### Get the device's IP address and log into the web portal

1. Press the paging button on the base station to display the device's IP address.

   ![Paging button.](_images/829be193ee2c6df5.png)
2. From a computer on the same network, open a browser and navigate to `http://<device-ip>`.
3. Enter the system PIN. The default PIN is `0000`.

   ![System PIN addition section.](_images/a786b5159458077c.png)
4. Click **OK**.

### Configure the IP phone

1. Click the **Settings** tab.

   ![Settings tab section of the Gigaset.](_images/a5e9d1f66e7dd9f1.png)
2. Expand **Telephony** in the left-hand navigation, click **Connections**, then click **Edit** next to the line to configure.

   ![Connections section in the Telephony hub.](_images/75a4e9494f6b92fd.png)
3. Enter:
   - **Connection Name or Number:** A descriptive name
   - **Authentication Name:** Your Telnyx SIP account username
   - **Authentication password:** Your Telnyx SIP account password
   - **Username:** Your Telnyx SIP account username
   - **Display name:** Your Telnyx SIP account username
   - **Domain:** `sip.telnyx.com`
   - **Proxy server address:** `sip.telnyx.com`
   - **Proxy server port:** `5060` for UDP, `5061` for TLS
   - **Registration server:** `sip.telnyx.com`
   - **Registration server port:** `5060` for UDP, `5061` for TLS
   - **Registration refresh time:** `300`
   - **STUN enabled:** `No`
   - **STUN server address:** (leave empty)
   - **Outbound proxy mode:** `Always`
   - **Outbound server address:** `sip.telnyx.com`
   - **Outbound proxy port:** `5060` for UDP/TCP, `5061` for TLS
   - **Select Network Protocol:** `UDP` by default; choose `TLS` if you have enabled TLS/SRTP

   ![A screenshot of the UDP setup.](_images/ee1b0373e442fa8f.png)
4. In **Telephony > Number Assignment > Handsets**, find the line you just created and check both:
   - **for outgoing calls**
   - **for incoming calls**

   ![A510 IP settings.](_images/8900b4a5db4900e8.png)

### Additional Gigaset A510 resources

- [Gigaset A510IP user guide](https://gse.gigaset.com/fileadmin/legacy-assets/A31008-M2230-R301-2-6019_en_US_CA.pdf)

---
