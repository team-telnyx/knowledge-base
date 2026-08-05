---
title: Configuring Elastix and Epygi IP PBXs with Telnyx
summary: This page consolidates Telnyx support documentation for configuring Elastix
  4 (IP and credentials trunks), Elastix 5 (FQDN and credentials trunks), and Epygi
  QX-series IP PBXs to interoperate with Telnyx as a SIP provider. It covers prerequisites,
  installation, SIP trunk creation, and inbound/outbound routing for each platform.
sources:
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
- url: https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup
- url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
- url: https://support.telnyx.com/en/articles/5728748-epygi-ip-pbx-telnyx-setup
- url: https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage
updated_at: 2026-08-05T13:28:08Z
---

# Configuring Elastix and Epygi IP PBXs with Telnyx

*Part 2 of 5 — see also: [Part 1](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-1.md), [Part 3](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-3.md), [Part 4](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-4.md), [Part 5](configuring-elastix-and-epygi-ip-pbxs-with-telnyx--part-5.md)*

This page consolidates Telnyx support documentation for configuring Elastix 4 (IP and credentials trunks), Elastix 5 (FQDN and credentials trunks), and Epygi QX-series IP PBXs to interoperate with Telnyx as a SIP provider. It covers prerequisites, installation, SIP trunk creation, and inbound/outbound routing for each platform.

## Elastix 4 Credentials Trunk

Use this configuration when authenticating the Elastix 4 PBX to Telnyx with SIP credentials rather than by IP.

### Add a SIP trunk

1. Log in to the Elastix GUI.

   ![Elastic GUI homepage.](_images/c63852c416d6b299.png)
2. Navigate to **PBX > Tools > Asterisk File Editor** and filter for the `sip_nat.conf` file.
3. Enter your local network subnet and external IP in the `localnet=` and `externip=` fields.
4. Click **Save**, then **Reload Asterisk**.

   ![Asterisk file and reload page.](_images/637813fed2840116.png)
5. Navigate to **PBX > PBX Configurations > Extensions > Add SIP Extension** and enter:
   - **User Extension:** the extension you wish to use for this trunk.
   - **Display Name:** a meaningful name.
   - **Outbound CID:** the [Telnyx number](https://portal.telnyx.com/#/app/numbers/my-numbers) you want to assign to this extension. Use the user extension and password along with the internal IP of your Elastix server to register this SIP extension.
   - **Asterisk Dial Options:** `tr`.
   - **Queue State Detection:** `Use state`.
   - **Secret:** your Telnyx account password for this extension.
   - **DTMFmode:** `RFC 2833`.
   - **NAT:** `No- RFC 3581`.

   ![Page for adding SIP extension.](_images/557893c8891e5a14.png)
6. Click **Submit**, then **Apply Config**.
7. From **PBX > PBX Configurations**, click **Trunks** and add the following settings.

   **Outgoing SIP Settings:**
   - **Username:** your Telnyx account username.
   - **Secret:** your Telnyx account password.
   - **Host:** `sip.telnyx.com`.
   - **Type:** `friend`.
   - **Insecure:** `port, invite`.
   - **Qualify:** `Yes`.
   - **Disallow:** `All`.
   - **Allow:** `ulaw & alaw`.

   **Inbound SIP Settings:**
   - **Username:** your Telnyx account username.
   - **Secret:** your Telnyx account password.
   - **Fromdomain:** `sip.telnyx.com`.
   - **Host:** `sip.telnyx.com`.
   - **Type:** `friend`.
   - **Insecure:** `port,invite`.
   - **Qualify:** `Yes`.
   - **Disallow:** `All`.
   - **Allow:** `ulaw`.
   - **DTMFmode:** `RFC 2833`.
   - **NAT:** `force_rport,comedia`.
   - **Registration string:** `your_username:your_password@sip.telnyx.com`.
   - **Dialed number manipulation rules:**
     - prepend: `1`; match pattern: `NXXNXXXXXX`
     - prepend: blank; match pattern: `1NXXNXXXXXX`

   > The above dial patterns are for 10- and 11-digit destinations; your own dial patterns may differ.

   ![Inbound sip settings page for the trunk.](_images/336a3c5e11866825.png)
8. Click **Submit** and **Apply Config**.

### Configure outbound rules

1. Navigate to **PBX > PBX Configurations > Outbound Routes**, then **Add Route**.
2. Provide:
   - **Route Name:** a meaningful identifier.
   - **Route CID:** the [Telnyx number](https://portal.telnyx.com/#/app/numbers/my-numbers) to assign to this route.
   - **Dial Patterns:** enter your dial patterns as needed.
   - **Trunk Sequence:** `Telnyx`.
   - Configure any additional fields as required.

   ![Outbound rules configuration portal.](_images/6384e88d3b77a57b.png)
3. Click **Submit** and **Apply Config**.

### Configure inbound rules

1. Navigate to **PBX > PBX Configurations > Inbound Routes**, then **Add Incoming Route**.
2. Provide:
   - **Description:** a meaningful identifier.
   - **[DID Number](https://telnyx.com/resources/sip-did):** the [Telnyx number](https://portal.telnyx.com/#/app/numbers/my-numbers) to handle inbound calls.
   - **Extensions:** any extensions to register for inbound calling.
   - Configure any additional fields as required.

   ![Inbound rules configuration portal.](_images/b81da0baad63e49e.png)
3. Click **Submit** and **Apply Config**.

## Elastix 5 First-Time Setup

Elastix 5 is a high-performance turnkey PBX powered by 3CX. It is available on-premise on Windows, Linux, Raspberry Pi, or in the cloud. You will need an [Elastix license key](https://www.3cx.com/phone-system/download-phone-system/).

1. After installation, choose to run the configuration tool from the **web browser** (recommended) or the **command line**. A URL is provided for accessing the GUI.

   ![3CX configuration tool.](_images/3805bf7a131b62ee.png)
2. Enter your license key and click **Next** to create a new install.

   ![3CX installation interface.](_images/bc04289576e9d186.png)
3. Confirm or override the detected public IP address, then click **Next**.
4. Choose whether your IP address is **static** or **dynamic**, then click **Next**.

   ![Public IP settings section.](_images/db16f19f5bbfba68.png)
5. Select the ports required for the 3CX Management console (defaults are populated).

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
14. A congratulations page confirms the basic settings. Note the details — a copy is also emailed to the admin address.
15. Access the PBX interface using the FQDN or public IP. If the PBX is on your local LAN behind a firewall, apply port forwarding for the ports selected in step 5.
16. Log in with the username and password you created.

    ![3CX management console administration portal.](_images/db555806817dd70e.png)
17. The dashboard appears.

    ![3CX dashboard.](_images/c15947baf44935a9.png)
18. Go to **Settings > Network** to confirm your network settings.
19. On the **Ports** tab, set **SIP Port** to `5060`.
20. On the **Public IP** tab, verify the **External IP Configuration** and that the correct network card interface is selected.

    > Ensure the connection IP on the Telnyx Mission Control Portal matches your static public IP. You can also use the FQDN for inbound calls and the IP for outbound calls.
