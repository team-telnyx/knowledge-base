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

*Part 2 of 4 — see also: [Part 1](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-1.md), [Part 3](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-3.md), [Part 4](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-4.md)*

This page explains how to configure a Telnyx SIP trunk on several supported desk phones and door phones, including the Gigaset A510 IP, Gigaset A690/AS690, Gigaset DX800a, Dinstar C60, Mitel 6800/6900 series, and Alcatel SD601/SD602 SIP door phones. Each section covers prerequisites, how to access the device's web interface, and the SIP trunk configuration values to enter.

## Gigaset DX800a (legacy)

The Gigaset DX800a is a hybrid multiline desktop phone for small/home offices. It supports up to 4 parallel calls, up to 6 handsets, up to 1,000 vCard entries, Outlook contact sync, and three integrated answering machines with up to 55 minutes of combined recording time. See the [Gigaset DX800a user manual](https://gse.gigaset.com/fileadmin/legacy-assets/Gigaset%20DX800A%20all%20in%20one_Web_en_GBR.pdf) for full details.

### Configure the Telnyx SIP trunk

1. On the welcome screen of the web portal, enter the system PIN. The default PIN is `0000`.

   ![Gigaset web portal.](_images/7b749f696fa4758a.png)
2. Click the **Settings** tab, then click **Telephony** in the side menu.
3. Click **Edit** next to the connection you want to configure.

   ![Settings tab for Telephony.](_images/63857d4a3df85444.png)
4. Click **Show Advanced Settings** and enter the following:
   - **Connection Name or Number:** A descriptive name.
   - **Authentication Name:** Your SIP connection username.
   - **Authentication Password:** Your SIP connection password.
   - **Username:** Your SIP connection username.
   - **Display Name:** Your caller ID. Use capital letters, no special characters (spaces allowed), and keep it under 15 characters for compatibility with some Canadian providers.
   - **Domain:** `sip.telnyx.com`
   - **Proxy Server Address:** `sip.telnyx.com` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses) for non-US regions).
   - **Proxy Server Port:** `5060` for TCP/UDP, `5061` for TLS.
   - **Registration Address:** `sip.telnyx.com` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses) for non-US regions).
   - **Registration Refresh Time:** `600`
   - **STUN Enabled:** `Yes` or `No`.
   - **STUN Server:** `stun.telnyx.com:3478` (only if STUN is enabled).
   - **Outbound Proxy Mode:** `Always`
   - **Outbound Server Address:** `sip.telnyx.com` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses) for non-US regions).
   - **Outbound Server Port:** `5060` for TCP/UDP, `5061` for TLS.

   ![Show Advanced Settings button.](_images/b1444c94a54e42c1.png)
5. Click **Set** to save.

### Configure audio settings

1. Click the **Settings** tab, then click **Audio** in the side menu.
2. Click **Show Advanced Settings** and add the codecs you want to use. Telnyx supports:
   - `ulaw(g711u)`
   - `alaw(g711a)`
   - `g722`
   - `g729`

   ![Show Advanced Settings section.](_images/c08138a79d9840e3.png)

### Configure call routing

1. Click the **Settings** tab, then click **Number Assignment** in the side menu.
2. Select the **for outgoing calls** radio button for the Telnyx account.
3. Select the **for incoming calls** radio button for the Telnyx account.
4. Click **Set** to save.

   ![Call routing configuration section.](_images/e215dc25c99045ba.png)

### Create a dial plan

1. Click the **Settings** tab, then click **Dialing Plans** in the side menu.
2. Configure the dial plan:
   - **Phone number:** `911` (or your local emergency dial code).
   - **Use area code:** Leave unchecked.
   - **Connection:** The Telnyx connection you set up.
   - **Active:** Check this box.
3. Click **Set** to save.

You can check the connection status from **Settings > Telephony > Connections**.

## Dinstar C60

The Dinstar C60 series delivers SIP technology for business communications, with a 132x64 graphical LCD, HD voice, support for 2 SIP accounts, and 5-party conferencing. See [Dinstar downloads](https://www.dinstar.com/download/), [Dinstar FAQs](https://www.dinstar.com/faq/), and [Dinstar contact and support](https://www.dinstar.com/contact-us/) for additional resources.

### Obtain the device IP address and log into the web portal

1. Once the phone is connected to your local network, press **OK** on the phone screen, then select **IPV4**.
2. Record the IP address.
3. Open a browser and enter the IP address in the address bar.
4. Log in with the default credentials:
   - **Username:** `admin`
   - **Password:** `admin`

### Configure a Telnyx SIP trunk

1. From the web portal, navigate to **Account > Basic Page**.
2. In the **SIP Account** section, provide:
   - **Account:** Your account ID (main or sub-account).
   - **Active:** `Enabled`
   - **Display Label:** A name for the line.
   - **Display Name:** Your caller ID name. Use capital letters, no special characters (spaces allowed), and keep it under 15 characters for compatibility with some Canadian providers.
   - **Register Name:** Your main account or sub-account.
   - **Username:** The username associated with the Telnyx account.
   - **Password:** The password associated with the Telnyx account.
3. In the **SIP Server** section, provide:
   - **Server IP:** `sip.telnyx.com`
   - **Port:** `5060`
   - **Registration Expires:** `120`

   ![Account > Basic Page section.](_images/9138b2cd672bb55d.png)
