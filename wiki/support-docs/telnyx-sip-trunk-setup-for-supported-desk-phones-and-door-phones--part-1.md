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

*Part 1 of 4 — see also: [Part 2](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-2.md), [Part 3](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-3.md), [Part 4](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-4.md)*

This page explains how to configure a Telnyx SIP trunk on several supported desk phones and door phones, including the Gigaset A510 IP, Gigaset A690/AS690, Gigaset DX800a, Dinstar C60, Mitel 6800/6900 series, and Alcatel SD601/SD602 SIP door phones. Each section covers prerequisites, how to access the device's web interface, and the SIP trunk configuration values to enter.

## Overview

This page covers how to configure a Telnyx SIP trunk on several supported desk phones and door phones. The devices covered include the Gigaset A510 IP, Gigaset A690/AS690, Gigaset DX800a, Dinstar C60, Mitel 6800/6900 series, and Alcatel SD601/SD602 SIP door phones. Each section below walks through the prerequisites, how to access the device's web interface, and the SIP trunk configuration values to enter.

Before starting any of these setups, ensure your [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) is configured correctly and that you have provisioned a Telnyx SIP connection with credentials. It is also recommended to enable TLS to encrypt your traffic.

## Gigaset A510 IP

The Gigaset A510 IP is a versatile VoIP phone that supports up to 3 parallel calls (2 VoIP and 1 fixed line) and lets a caller switch between them at the press of a button. See the [Gigaset A510IP user guide](https://gse.gigaset.com/fileadmin/legacy-assets/A31008-M2230-R301-2-6019_en_US_CA.pdf) for additional documentation.

### Get the device IP address and log into the web portal

1. Press the paging button on the base station to display the device's IP address.

   ![Paging button.](_images/829be193ee2c6df5.png)
2. On a computer on the same network, open a browser and enter `http://` followed by the IP address.
3. Enter the system PIN. The default PIN for new devices is `0000`.

   ![System PIN entry screen.](_images/a786b5159458077c.png)
4. Click **OK**.

### Configure the IP phone

1. Click the **Settings** tab at the top of the page.

   ![Settings tab.](_images/a5e9d1f66e7dd9f1.png)
2. In the left-hand navigation, expand **Telephony**, click **Connections**, then click **Edit** next to the line you want to configure.

   ![Connections section in the Telephony hub.](_images/75a4e9494f6b92fd.png)
3. Enter the following information:
   - **Connection Name or Number:** A descriptive name for the connection.
   - **Authentication Name:** Your Telnyx SIP account username.
   - **Authentication Password:** Your Telnyx SIP account password.
   - **Username:** Your Telnyx SIP account username.
   - **Display Name:** Your Telnyx SIP account username.
   - **Domain:** `sip.telnyx.com`
   - **Proxy Server Address:** `sip.telnyx.com`
   - **Proxy Server Port:** `5060` for UDP, `5061` for TLS.
   - **Registration Server:** `sip.telnyx.com`
   - **Registration Server Port:** `5060` for UDP, `5061` for TLS.
   - **Registration Refresh Time:** `300`
   - **STUN Enabled:** `No`
   - **STUN Server Address:** Leave empty.
   - **Outbound Proxy Mode:** `Always`
   - **Outbound Server Address:** `sip.telnyx.com`
   - **Outbound Proxy Port:** `5060` for UDP/TCP, `5061` for TLS.
   - **Select Network Protocol:** `UDP` by default. Choose `TLS` if you have enabled TLS and your account uses SRTP encryption.

   ![UDP setup screenshot.](_images/ee1b0373e442fa8f.png)
4. Still in **Telephony**, click **Number Assignment** and find the **Handsets** section. Locate the line you just created (matching the **Connection Name or Number**) and check both:
   - **For outgoing calls:** Radio button checked.
   - **For incoming calls:** Checkbox checked.

   ![A510 IP settings.](_images/8900b4a5db4900e8.png)

## Gigaset A690/AS690

The Gigaset A690 IP supports up to 3 parallel calls (2 VoIP and 1 fixed line) and can register up to 6 handsets. The AS690 IP variant supports up to 6 SIP accounts from different providers. Additional features include HDSP voice, a 2" illuminated black-and-white display, a 150-entry phonebook, the "Contacts Push" app, and a day/night mode. See the [A690/AS690 user documentation](https://gse.gigaset.com/fileadmin/gigaset/images/CustomerCare/Manuals/A6xx/A690IP-AS690IP/A31008-M2813-R601-1a-TE19_en_IM-East-INT.pdf) and the [Gigaset service portal](https://service.gigaset.com/en/support/home) for more information.

### Update firmware (manual)

1. From the handset, press **Menu**.
2. Navigate to **Settings** and press **OK**.
3. Navigate to **System** and press **OK**.
4. Navigate to **Base Update** and press **OK**.
5. Enter the system PIN (default `0000`).
6. The unit will check for new firmware. If available, press **OK** to begin the base update.
7. Once the base update completes, press **Menu**, navigate to **Settings**, and press **OK**.
8. Navigate to **Firmware Update** and press **OK**.
9. Navigate to **Update** and press **OK**. The handset update can take up to 30 minutes.

### (Optional) Enable automatic firmware updates

1. Press **Menu**, navigate to **Settings**, and press **OK**.
2. Navigate to **Firmware Update** and press **OK**.
3. Navigate to **Automatic Check** and press **OK** to enable automatic updates.
4. If a new firmware update is available, press **OK** to install it now.

### Get the device IP address and log into the web portal

1. Briefly press the paging button on the base station to display the device's IP address.

   ![The paging button.](_images/829be193ee2c6df5.png)
2. On a computer on the same network, open a browser and enter `http://` followed by the IP address.
3. Enter the system PIN. The default PIN is `0000`.

   ![System PIN entry screen.](_images/a786b5159458077c.png)
4. Click **OK**.

### Configure the device from the web portal

If you have not yet set up a VoIP connection, run the Quick Start Wizard:

1. Click the **Home** tab, select **Quick Start Wizard**, and click **Next**.
2. Select your country and click **Next**.
3. Select your provider. If Telnyx is not listed, choose **Other Provider** and enter the IP account details you provisioned from Telnyx for each VoIP number.
4. Click the **Settings** tab.

   ![Settings tab on the Quick Start Wizard.](_images/a5e9d1f66e7dd9f1.png)

### Configure Telephony settings

1. Expand **Telephony** in the left-hand navigation, click **Connections**, then click **Edit** next to the line you want to configure.

   ![Telephony link on the Quick Start Wizard.](_images/75a4e9494f6b92fd.png)
2. Enter the following information:
   - **Connection Name or Number:** A descriptive name for the connection.
   - **Authentication Name:** Your Telnyx SIP account username.
   - **Authentication Password:** Your Telnyx SIP account password.
   - **Username:** Your Telnyx SIP account username.
   - **Display Name:** Your Telnyx SIP account username.
   - **Domain:** `sip.telnyx.com`
   - **Proxy Server Address:** `sip.telnyx.com`
   - **Proxy Server Port:** `5060` for UDP, `5061` for TLS.
   - **Registration Server:** `sip.telnyx.com`
   - **Registration Server Port:** `5060` for UDP, `5061` for TLS.
   - **Registration Refresh Time:** `300`
   - **STUN Enabled:** `No`
   - **STUN Server Address:** Leave empty.
   - **Outbound Proxy Mode:** `Always`
   - **Outbound Server Address:** `sip.telnyx.com`
   - **Outbound Proxy Port:** `5060` for UDP/TCP, `5061` for TLS.
   - **Select Network Protocol:** `UDP` by default. Choose `TLS` if you have enabled TLS and your account uses SRTP encryption.

   ![Settings section.](_images/ee1b0373e442fa8f.png)
3. In **Telephony**, click **Number Assignment** and find the **Handsets** section. Locate the line you just created and check both:
   - **For outgoing calls:** Radio button checked.
   - **For incoming calls:** Checkbox checked.

   ![Handsets section of the Telephony domain.](_images/8900b4a5db4900e8.png)
