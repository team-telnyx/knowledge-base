---
title: Telnyx SIP Connection Configuration Guide
summary: This page consolidates Telnyx guidance on configuring SIP connections, including
  IP and credentials-based authentication, failover and retry behavior, multi-device
  registration, tech prefixes, X-Telnyx-Token authentication, P-Charge-Info headers,
  and PBX-specific setup examples for FreePBX, FreeSWITCH, and FusionPBX.
sources:
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
updated_at: 2026-08-05T13:32:19Z
---

# Telnyx SIP Connection Configuration Guide

*Part 4 of 5 — see also: [Part 1](telnyx-sip-connection-configuration-guide--part-1.md), [Part 2](telnyx-sip-connection-configuration-guide--part-2.md), [Part 3](telnyx-sip-connection-configuration-guide--part-3.md), [Part 5](telnyx-sip-connection-configuration-guide--part-5.md)*

This page consolidates Telnyx guidance on configuring SIP connections, including IP and credentials-based authentication, failover and retry behavior, multi-device registration, tech prefixes, X-Telnyx-Token authentication, P-Charge-Info headers, and PBX-specific setup examples for FreePBX, FreeSWITCH, and FusionPBX.

## FusionPBX Credentials Trunk

[FusionPBX](https://www.fusionpbx.com/) can be used as a highly available single or domain-based multi-tenant PBX, carrier-grade switch, call center server, fax server, VoIP server, voicemail server, conference server, voice application server, and appliance framework. It is built on FreeSWITCH.

### Pre-requisites

- Ensure your [Telnyx Mission Control Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account), including creating a [credentials-based connection](https://portal.telnyx.com/#/app/connections) assigned to a DID and outbound profile
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
- [Download](https://www.fusionpbx.com/download) and [install](https://docs.fusionpbx.com/en/latest/getting_started/quick_install.html) FusionPBX
- RECOMMENDED: Use Debian as the operating system (tested on Debian 9.9)

### Step 1: (Optional) Install a Virtual Machine

If running FusionPBX on a VM, install [VirtualBox](https://www.virtualbox.org/) and create a Debian VM:

1. Download and install the [Debian network installer disk image](https://www.debian.org/) and run it.
2. In VirtualBox, click the **New** icon to start the New Virtual Machine Wizard.
3. On the Name and operating system screen, provide:
   - **Name:** Any name you like
   - **Operating System:** *Linux*
   - **Version:** *Debian (64 bit)*

   ![Running Debian network installer disk image.](_images/36ef392fd0446eff.png)
4. Click **Continue**.
5. On the Memory size screen, use the default base memory setting.

   ![Memory size tab on the Debian network installer.](_images/53e750328c5a7ade.png)
6. Click **Continue**.
7. On the Hard disk screen, select **Create a virtual hard disk now**.

   ![Hard disk screen on the Debian network installer.](_images/a57d3f98729cf694.png)
8. Click **Create**.
9. Use the default VirtualBox disk image (VDI) format and click **Continue**.
10. On the Storage on physical hard disk screen, choose **Dynamically allocated**.

    ![Storage on physical hard disk screen.](_images/fbdee0b4d52cf7d1.png)
11. On the File location and size screen, use the defaults unless you need specific values.

    ![File location and size screen.](_images/165a843dbe76cde3.png)
12. Click **Create**.

    ![Virtual machine interface.](_images/991fef55a7761d0a.png)
13. Click the **Settings** gear and find **Storage** in the left navigation.
14. Select the Debian file under **Controller: IDE**.

    ![Settings gear on the newly launched Virtual Machine.](_images/ecf48bc4e2f957d4.png)
15. Start the VM; it will boot and begin the Debian Linux installation.
16. After installation, power on the VM from the VirtualBox homepage and configure language and other settings, then install FusionPBX.

### Step 2: Install FusionPBX

1. Follow the [FusionPBX install script](http://docs.fusionpbx.com/en/latest/getting_started/quick_install.html).
2. Run the following commands as root:

   ```
   #upgrade the packages
   apt-get update && apt-get upgrade -y

   #install packages
   apt-get install -y git lsb-release

   #get the install script
   cd /usr/src && git clone https://github.com/fusionpbx/fusionpbx-install.sh.git

   #change the working directory
   cd /usr/src/fusionpbx-install.sh/debian
   ```

   This installs FusionPBX, the FreeSWITCH release package and its dependencies, iptables, Fail2ban, NGINX, PHP-FPM, and PostgreSQL.
3. At the end of the install script, you will be instructed to open the server's IP address in a web browser to finish the install in the FusionPBX GUI.

   ![Script running interface.](_images/ecdbdd248bcb8b61.png)
4. Choose your language and click **Next**.

   ![GUI to configure FusionPBX.](_images/c06cf491c89bf050.png)
5. Event socket settings will be auto-detected. Click **Next**.

   ![Event Socket settings interface.](_images/a67f12fbf84515d1.png)
6. Enter a username and password as your FusionPBX login credentials.

   ![Admin configuration tab.](_images/1c4ea021c6186560.png)
7. Fill in any bolded required fields. Return to the terminal to retrieve the database username and password shown above the server IP.

   ![Database configuration tab.](_images/a2644fa037cc4886.png)
8. Click **Next**.
9. Sign in with the credentials from step 6.

   ![FusionPBX admin interface.](_images/fb360c8d0887ca2f.png)

### Step 3: Configure a FusionPBX Trunk

1. Go to **Advanced → Upgrade**, tick **App Defaults**, and click **Execute**.

   ![Upgrade section on the FusionPBX portal.](_images/cc6223603c2dcfb5.png)
2. Go to **Accounts → Gateway** and provide:
   - **Gateway:** *Telnyx*
   - **Username:** The username from your Telnyx credentials-based connection
   - **Password:** The password from your Telnyx credentials-based connection
   - **From User:** The username from your Telnyx credentials-based connection
   - **From Domain:** *sip.telnyx.com*
   - **Proxy:** *sip.telnyx.com*

   ![Accounts section on the FusionPBX portal.](_images/fe82952e69bc0321.png)
3. Click **Save**. FusionPBX will register with Telnyx.

   ![FusionPBX portal.](_images/767e9b4d4b052110.png)

### Step 4: Create Your Extensions

1. Go to **Accounts → Extensions** and click **Add**.

   ![Extensions section of the FusionPBX portal.](_images/7a62853ecad25dfa.png)
2. Optionally change the auto-generated password and configure an outbound caller ID via the **Outbound Caller ID Number** field. See [FusionPBX's extensions documentation](https://docs.fusionpbx.com/en/latest/accounts/extensions.html) for details.

   Caller ID naming conventions:
   - Use **capital letters** for the outbound Caller ID Name for clearer display on some devices.
   - Do **not use special characters**; they will not be displayed.
   - Some Canadian providers will not show more than 15 characters; consider shortening.
   - **Spaces are allowed** in a caller ID name.
   - Be familiar with [Telnyx's caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).

   ![Outbound Caller ID Number field.](_images/65ea6dde8a978f78.png)
3. Click **Save**.
4. Go to **Dialplan → Destinations** and click **Add**.

   ![Destinations section of the Dial Plan field.](_images/c62139d5d52aa79c.png)
5. Add a number you purchased on your Portal account to **Destination** (include the +1 prefix), and select an extension from the **Actions** dropdown.

   ![Destination section.](_images/8de8219094e03e5b.png)
6. Click **Save**.

### Step 5: Configure Inbound Routing

1. Go to **Dialplan → Inbound routes**. Inbound routes for your destinations should be added automatically.

   ![Inbound routes in the Dial Plan section.](_images/8f20e58162b43c30.png)
2. Click any number to view its dialplan. Ensure your number format is set to E.164 on the connection in your Mission Control Portal.

   ![Inbound routes in the Dial Plan section.](_images/9369f7b44853ee13.png)

### Step 6: Configure Outbound Routing

1. Go to **Dialplan → Outbound routes** and click **Add**.

   ![Outbound routes in the Dial Plan header.](_images/bc011be91b835fa9.png)
2. Create your outbound route with:
   - **Gateway:** *Telnyx*
   - **Dialplan Expression:** Select the region (for example, *North America*)

   ![Outbound routes credentials field.](_images/9dd16170772a5053.png)
3. Click **Save**.

### Step 7: Register Your Extensions with a Device

1. Go to **Status → Registrations** and register your extensions with a device (for example, [Zoiper](https://support.telnyx.com/en/articles/6133517-zoiper-communicator) or X-Lite softphone).

   ![Extension registration in the status field.](_images/50a22250f1253334.png)

Registered devices can make and receive calls internally (for example, by calling 1000 or 1001) and externally via the configured inbound and outbound routes.
