---
title: FreePBX Trunk Settings with Telnyx
summary: Step-by-step instructions for configuring FreePBX (V13, V14, and V15) IP
  trunks with Telnyx using both Chan_SIP and PJSIP, including installation, SIP settings,
  extensions, trunk configuration, outbound/inbound routing, and dial pattern examples.
sources:
- url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
- url: https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip
- url: https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial
- url: https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip
- url: https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone
updated_at: 2026-08-05T13:27:33Z
---

# FreePBX Trunk Settings with Telnyx

*Part 1 of 2 — see also: [Part 2](freepbx-trunk-settings-with-telnyx--part-2.md)*

Step-by-step instructions for configuring FreePBX (V13, V14, and V15) IP trunks with Telnyx using both Chan_SIP and PJSIP, including installation, SIP settings, extensions, trunk configuration, outbound/inbound routing, and dial pattern examples.

## Overview

[FreePBX](https://www.freepbx.org/) is a web-based open source GUI that controls and manages Asterisk (PBX), an open source communication server. FreePBX is licensed under the GNU General Public License (GPL) and can be installed manually or as part of the pre-configured FreePBX Distro that includes the system OS, Asterisk, FreePBX GUI, and assorted dependencies.

> **Note:** We suggest using PJSIP as an upgrade from Chan_SIP, as Chan_SIP is outdated, and the majority of users are moving to PJSIP which provides a number of more future proof options, and is still actively being improved by the community. You can find out more about PJSIP [here](https://www.pjsip.org/about.htm).

PJSIP is an open source and separate extension of Asterisk (and Asterisk-derived systems). It provides a resource for assigning multiple trunks via SRV addresses, and more options. PJSIP also provides three main components of real-time multimedia application: signaling, media features, and NAT traversal, among other things.

Additional documentation and resources:

- [FreePBX support](https://www.freepbx.org/support/)
- [FreePBX documentation](https://wiki.freepbx.org/#all-updates)

## Pre-requisites

Before you begin, ensure the following are in place:

- [Download](https://www.freepbx.org/downloads/) and [install](https://sangomakb.atlassian.net/wiki/spaces/PP/pages/10682958/PBX+Platforms+Home) FreePBX (V13, V14, or V15)
- [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- [Set up an IP connection on your Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/connections)
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

## Install FreePBX

1. Load the ISO onto your server or virtual machine. For V13, do a full install via Asterisk 13. For V14 and V15, do a full install via Asterisk 16.

   ![A page showing ISO installation using asterisk 13](_images/9bb9534c01512c79.png)

   ![Installation Virtual Machine.](_images/d3a40ddeef2958cd.png)

   ![A virtual machine.](_images/0181966dde309a8c.png)
2. Confirm your network settings.

   ![Network setting confirmations page.](_images/521980f2990f58e4.png)
3. Choose and confirm your root password.

   ![Root password confirmation page.](_images/7fd40a8757cf47ea.png)

   ![Root password credentials confirmation page.](_images/3eccab3bc7c6c046.png)
4. Wait while your packages are installed. The FreePBX package itself can take 15 or more minutes to install and requires access to the internet.

   ![Package installation waiting page.](_images/4e9f624cbc7e062e.png)
5. Once the install has 100% completed, click on reboot. Your system is now installed.
6. After reboot, log in to the Linux console using the username `root` and the root password you selected earlier.
7. After you log in, take note of the IP address of your PBX. You will need it in the next step.

   ![Localhost credentials input point.](_images/7ca4ee3478ff63d8.png)
8. Enter the IP address of the new PBX into your web browser. The first time you do so, you'll be asked to create the admin username and the admin password. These credentials will be used in the future to access the FreePBX configuration screen.

   > **Note:** These passwords do not change the Root password! They are only used for access to the FreePBX web interface.

   ![The FreePBX Web Interface.](_images/a58d723836f225b2.png)

   ![FreePBX administration page.](_images/f1b313d0ae2f42a9.png)
9. Once submitted, log in to the admin panel with the username and password set up in the step above.

## Configure Basic Settings

The main FreePBX screen offers four options:

- **FreePBX Administration** — Configure your PBX. Use the admin username and admin password you configured above. This section is what most people refer to as "FreePBX."
- **User Control Panel** — Where a user can log in to make web calls, set up their phone buttons, view voicemails, send and receive faxes, use SMS & XMPP messaging, view conferences, and more, depending on what you have enabled for the user. See [User Control Panel (UCP) 14+](https://wiki.freepbx.org/pages/viewpage.action?pageId=74318855) for more information.
- **Operator Panel** — A screen that allows an operator to control calls (needs additional licensing).
- **Get Support** — Takes you to a web page about various official support options for FreePBX.

1. Enter the username, password, and admin email address to create your account.

   ![Administration credentials page.](_images/f1b313d0ae2f42a9.png)
2. Once your account is created, you'll be brought to the dashboard. Select **FreePBX Administration** and enter your username and password.
3. Follow the process to activate your FreePBX.

   ![FreePBX Administration dashboard.](_images/7845b20c6aa50373.png)

   ![Default locales selection.](_images/d837b94bacf96195.png)
4. Select your default locales.

   ![Page to select default locales.](_images/37dbf640f658de04.png)

   ![Default locales settings.](_images/22ab76536acbc54d.png)
5. You'll be presented with some firewall details and other suggestions. You are welcome to set this up based on your requirements.
6. Once you're back at the dashboard, you'll see more detail.

   ![Admin dashboard with more administration details.](_images/7476e5614800248d.png)

   ![FreePBX dashboard.](_images/3411ea2aba205df0.png)

## Configure SIP Settings

At this point you can now work on confirming network settings and configuring your [SIP trunks](https://telnyx.com/products/sip-trunks) and extensions.

1. Make your way to **Settings → Asterisk SIP Settings** to confirm your network settings.
2. Populate the **external** and **local** network addresses under **General SIP Settings** and either **Chan SIP Settings** (for Chan_SIP trunks) or **PJSIP Settings** (for PJSIP trunks).
3. Click **Submit** and then **Apply Config**.

   ![Asterisk SIP Settings for network settings confirmation.](_images/55db9cb34da2bcff.png)

   ![SIP settings configuration.](_images/847163dc3de1f096.png)

## Configure Extensions

### Chan_SIP Extensions

1. Make your way to **Applications → Extensions → Add Extension → Add New Chan SIP Extension**. The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extension's secret may need to be populated under the **Other** tab.

   ![New Chan SIP Extension Interface.](_images/02fd06b118aa7ac1.png)

   > **Note:** If you do not set an Outbound CID for your extension, you will need to enable this on your trunk.

   > **Note:** This device uses CHAN_SIP technology listening on Port 5160 (UDP — this is a NON STANDARD port).

2. Click **Submit** and **Apply Config**.

### PJSIP Extensions

1. Make your way to **Applications → Extensions → Add Extension → Add New Chan PJSIP Extension**. The **Outbound CID** is the [number you purchased](https://portal.telnyx.com/#/app/numbers/my-numbers) from your Telnyx Mission Control Portal. The extension's secret may need to be populated under the **Other** tab.

   ![Applications settings.](_images/747c99ce86d00a77.png)

   > **Note:** If you do not set an Outbound CID for your extension, you will need to enable this on your trunk.

   > This device uses **PJSIP** technology listening on Port 5060 (UDP).

2. Click **Submit** and **Apply Config**.

   ![PJSIP addition extension.](_images/22cdfd9140be6e55.png)

For testing purposes, you can now use your SIP client to register with FreePBX using the username, password/secret, and local IP address of your FreePBX.
