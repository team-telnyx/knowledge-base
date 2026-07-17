---
title: Configuring Elastix PBX with Telnyx
summary: This page explains how to configure Elastix 4 and Elastix 5 PBX systems with
  Telnyx using IP-based, FQDN, and credentials-based SIP trunks, including installation,
  trunk setup, and inbound/outbound routing. It also covers integrating Chiro8000
  practice management software with Telnyx for SMS messaging and resetting a Telnyx
  account password.
sources:
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
- url: https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup
- url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
- url: https://support.telnyx.com/en/articles/7885470-chiro8000-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/7984661-how-to-reset-your-password
updated_at: 2026-07-17T09:03:10Z
---

# Configuring Elastix PBX with Telnyx

*Part 2 of 3 — see also: [Part 1](configuring-elastix-pbx-with-telnyx--part-1.md), [Part 3](configuring-elastix-pbx-with-telnyx--part-3.md)*

This page explains how to configure Elastix 4 and Elastix 5 PBX systems with Telnyx using IP-based, FQDN, and credentials-based SIP trunks, including installation, trunk setup, and inbound/outbound routing. It also covers integrating Chiro8000 practice management software with Telnyx for SMS messaging and resetting a Telnyx account password.

## Configure Elastix 4 Outbound and Inbound Routes

### Outbound routes

1. Go to **PBX > PBX Configurations > Outbound Routes** and click **Add Route**.
2. Configure:
   - **Route Name:** a meaningful identifier.
   - **Route CID:** the Telnyx number to assign to this route.
   - **Dial Patterns:** enter your dial patterns (use as many as necessary).
   - **Trunk Sequence:** `Telnyx`.
   - Configure any additional fields as needed.

   ![PBX configurations' page for outbound routes.](_images/6384e88d3b77a57b.png)
3. Click **Submit** and **Apply Config**.

### Inbound routes

1. Go to **PBX > PBX Configurations > Inbound Routes** and click **Add Incoming Route**.
2. Configure:
   - **Description:** a meaningful identifier.
   - **DID Number:** the Telnyx number to handle inbound calls.
   - **Extensions:** any extensions to register for inbound calling.
   - Configure any additional fields as needed.

   ![PBX configurations' page for inbound routes.](_images/b81da0baad63e49e.png)
3. Click **Submit** and **Apply Config**.

You can now make and receive calls using Telnyx as your SIP provider.

## Complete First-Time Setup of Elastix 5

1. After installation, choose to run the configuration tool from the **web browser** (recommended). A URL is provided for accessing the GUI.

   ![3CX configuration tool.](_images/3805bf7a131b62ee.png)
2. Enter your license key and click **Next** to create a new install.

   ![3CX installation interface.](_images/bc04289576e9d186.png)
3. Confirm or manually enter your public IP address, then click **Next**.
4. Choose whether your IP address is **static** or **dynamic**, then click **Next**.

   ![Public IP settings section.](_images/db16f19f5bbfba68.png)
5. Select the ports for the 3CX Management console (defaults are pre-populated).

   ![3CX installation interface.](_images/eee74b1cfbe01fc8.png)
6. Select the default network adapter.

   ![3CX installation interface.](_images/1fa57dc4b67a1e84.png)
7. Wait for the FQDN and certificates to be generated.

   ![3CX installation interface.](_images/4be2beba3b5845e9.png)
8. Select how many digits your extensions should have.

   ![3CX installation interface.](_images/b231c2701cec333e.png)
9. Enter an email for important system notifications.

   ![3CX installation interface.](_images/7e92f539933e2e1e.png)
10. Select your country and time zone.

    ![3CX installation interface.](_images/f480674f4cb0aa67.png)
11. Create an operator extension.

    ![Operator Extension tab on the 3CX installation interface.](_images/44f91a26a015c2ac.png)
12. Optionally restrict outbound calling to specific countries.

    ![Additional security measure on the 3CX installation interface.](_images/7f9559ffe077dfb5.png)
13. Select your preferred language.

    ![Language section on the 3CX installation interface.](_images/8806d3799c4cfeeb.png)
14. A congratulations page confirms the basic PBX setup. Note the details (a copy is also emailed to the admin address).
15. Access the PBX using the FQDN or public IP URL. If the PBX is on your local LAN behind a firewall, apply port forwarding for the ports selected in step 5.
16. Log in with the username and password you created.

    ![3CX management console administration portal.](_images/db555806817dd70e.png)
17. The dashboard appears.

    ![3CX dashboard.](_images/c15947baf44935a9.png)
18. Go to **Settings > Network** to confirm network settings.
19. On the **Ports** tab, set **SIP Port** to `5060`.
20. On the **Public IP** tab, verify your public IP and the selected network card interface under **External IP Configuration**.

    > Make sure the connection IP on the Telnyx Mission Control Portal matches your static public IP. You can also use the FQDN for inbound calls and the IP for outbound calls.

## Create a Telnyx SIP Trunk in Elastix 5

1. From the left-hand navigation, click **SIP Trunks**.
2. Click **+ Add SIP Trunk**.
3. In the pop-up, enter:
   - **Select Country:** `Worldwide`
   - **Select Provider in your Country:** `Telnyx LLC`
   - **Main Trunk No:** the number purchased on your Telnyx Mission Control Portal.

   ![SIP Trunk/VoIP Provider tab.](_images/2e0700ca6ed799ee.png)
4. Click **OK** to open the trunk configuration window.
5. On the **General** tab, in **Trunk Details**, enter:
   - **Enter name of Trunk:** `Telnyx LLC`
   - **Registrar/Server/Gateway Hostname or IP:** `sip-anycast1.telnyx.com:5060` or `sip.telnyx.com:5060`
   - **Outbound Proxy:** `sip.telnyx.com`
   - **Number of SIM Calls:** your preferred number of simultaneous calls.

   ![Trunk configuration window.](_images/f97c44de921a899b.jpg)
6. In the **Authentication** section, configure based on trunk type:
   - **IP/FQDN trunk:**
     - **Type of Authentication:** `Do not require - IP Based`
     - **Authentication ID (aka SIP user ID):** the number purchased on your Telnyx portal.
     - **Authentication Password:** leave blank.
   - **Credentials trunk:**
     - **Type of Authentication:** `Register/Account based`
     - **Authentication ID (aka SIP user ID):** your Telnyx account username.
     - **Authentication Password:** your Telnyx account password.

   ![Authentication section in 3CX.](_images/57b141d2cd35fc13.png)
7. In the **Route calls to** section, enter:
   - **Main Trunk number:** the number purchased on your Telnyx portal (verify the default).
   - **Destination for calls during office hours:** based on your requirement.
   - **Destination for calls outside office hours:** based on your requirement.

   !["Route Calls To" section.](_images/c7052e225eea6d5a.png)
8. On the **Options** tab:
   - **Require registration for:** `Do not require`.
   - Remove `GSM-FR` from **Assigned Codecs**.
9. Click **Apply**.
10. Open the **Outbound Parameters** tab. In the **SIP Field** section, set **Contact User Part** to `Custom Field` (leave the custom value blank).

    ![Options tab of the setup.](_images/ea6dfcbcc4a19821.png)
11. Click **Apply**, then **OK** at the top of the page.
12. The IP trunk is now live.

    ![Live IP trunk dashboard.](_images/520d4eff9d33c299.png)

## Create Elastix 5 Inbound Rules

1. From the left-hand navigation, click **Inbound Rules**.
2. Click **+ Add DID Rule**.
3. In the **General** section, enter:
   - **Name:** a meaningful name for the inbound rule.
   - **DID/DDI:** one of the DIDs provisioned from Telnyx.

   ![Inbound Rules settings section.](_images/798d2c7d44d9c5ce.png)
4. In the **Route calls to** section, enter:
   - **Main Trunk number:** the number purchased on your Telnyx portal (verify the default).
   - **Destination for calls during office hours:** based on your requirement.
   - **Destination for calls outside office hours:** based on your requirement.

   !["Route Calls To" section.](_images/c7052e225eea6d5a.png)
