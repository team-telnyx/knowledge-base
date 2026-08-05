---
title: Telnyx Device and PBX Setup Guides
summary: Step-by-step instructions for configuring a range of SIP-capable devices
  and IP PBX systems to work with the Telnyx Mission Control Portal, including Mediatrix
  C7/4100 gateways, Positron IP PBX and IP phones, Synway UC-200, ScopTEL IP PBX,
  Flyingvoice IP phones, and Dinstar C60 series phones.
sources:
- url: https://support.telnyx.com/en/articles/5733572-mediatrix-c7-4100-telnyx-setup
- url: https://support.telnyx.com/en/articles/5790910-positron-ip-pbx
- url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
- url: https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx
- url: https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
- url: https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config
updated_at: 2026-08-05T13:36:04Z
---

# Telnyx Device and PBX Setup Guides

*Part 2 of 3 — see also: [Part 1](telnyx-device-and-pbx-setup-guides--part-1.md), [Part 3](telnyx-device-and-pbx-setup-guides--part-3.md)*

Step-by-step instructions for configuring a range of SIP-capable devices and IP PBX systems to work with the Telnyx Mission Control Portal, including Mediatrix C7/4100 gateways, Positron IP PBX and IP phones, Synway UC-200, ScopTEL IP PBX, Flyingvoice IP phones, and Dinstar C60 series phones.

## ScopTEL IP PBX Setup

[ScopTEL](scoptel.md) is a multi-tenant IP PBX with a unified communications system and call contact center. Minimum software release: `scopserv-telephony25-6.9.1.6.20191218-1`.

### Configure the SIP channel

1. Navigate to **Configuration > Telephony Settings: Channels > Channels > SIP Channel**.
2. Click **Edit** and adjust the **Miscellaneous** section:
   - **Enable Session Progress and In-Band Audio:** Configure as needed.
   - **Enable Premature Media?:** Configure as needed.
3. Click **Save**.

### (Recommended) Configure SIP TLS/SRTP

Requires SIP traffic encryption to be activated on the Telnyx Mission Control Portal.

1. Navigate to **Configuration > Telephony Settings: Channels > SIP Channel**.
2. Check **Enable support for SIP TLS (secure)?** and **Don't verify servers certificate when acting as client?**.
3. Click **Save**.

### Create a new SIP trunk

1. Navigate to **Interfaces > Interfaces Manager > VoIP Accounts** and click **Add a new VoIP Account**.
2. On the **General** tab, set:
   - **Type:** `SIP`.
   - **Trunk Type:** `Friend`.
   - **Name:** Unique alphanumeric name (e.g., `TelnyxTrunk`). For inbound calls, the name should match the username.
3. On the **Server** tab, set:
   - **Username:** Telnyx account/sub-account username.
   - **Password:** Telnyx account/sub-account password.
   - **Host:** `sip.telnyx.com`.
   - **Port:** `5060`.
   - **Register as User Agent:** Checked.
   - **Enable TLS registration:** Checked if TLS was configured in the previous step.
   - **Contact Extension:** Telnyx account/sub-account username.
4. On the **Network** tab, set:
   - **Transport mode:** `UDP`, `TCP`, or both; only `TLS` if a TLS trunk was created.
   - **Insecure:** Check `Invite`.
5. On the **Options** tab, set:
   - **DTMF Mode:** `Automatic` (RFC 2833).
   - **Send Remote-Party-ID:** Checked.
   - **Codecs:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`, and `H264` for video.
   - **Disallowed Methods:** Check `UPDATE`.
6. Click **Add**.

### Create inbound rules

1. Navigate to **Lines > Lines Manager: Incoming Lines > Incoming Lines** and click **Add a new Incoming Line**.
2. On the **General** tab, set:
   - **Extension (DNIS):** Provisioned Telnyx DID.
   - **Trunk:** Select the Telnyx trunk from the dropdown.
3. Click **Add**.

## Flyingvoice IP Phone Setup

[Flyingvoice](flyingvoice.md) offers a range of VoIP phones, ATAs, gateways, and routers, including WiFi IP phones that eliminate the need for a hard-wired connection.

### Physically connect the phone

Connect the phone to the same network as the configuration computer following the standard network topology.

### Get the device IP and log into the web portal

1. Power on the phone; the LCD will display the IP address after initialization.
2. From a computer on the same network, open a browser and enter `http://<phone-ip>`.
3. Default credentials: **Username:** `admin`, **Password:** `admin`. Change these after first login.

### Configure the SIP account

1. Navigate to **SIP Account > Line 1** and configure:
   - **Line Enable:** Enable.
   - **Display Name:** Caller ID in CAPITAL LETTERS, no special characters, max 15 characters.
   - **Phone Number:** Telnyx username.
   - **Account:** Telnyx username.
   - **Password:** Telnyx password.
   - **Proxy Server:** `sip.telnyx.com`.
   - **Proxy Port:** `5060` for UDP, `5061` for TLS.
   - **Transport:** `UDP` by default; choose `TLS` if SRTP encryption is enabled.
   - **Voice Mailbox Numbers:** `*97`.
   - **Register Refresh Interval (sec):** `180`.
   - **RTP Port Min:** `100001`.
   - **RTP Port Max:** `200000`.
2. Click **Save & Apply**.

### (Optional) Set the Multiple Line button

1. Navigate to **Phone > Line Key**.
2. In the **Dsskey** table, set:
   - **Type:** `Line`.
   - **Line:** `Line 1`.
   - **Label:** e.g., `L1`, `Line1`, or the extension number.
3. Click **Save**.

### (Optional) Configure the SIP trunk from the phone

1. From the phone, navigate to **Menu > Advanced** (default password: `admin`).
2. Go to **Accounts > Line 1** and enable **Registration**.
3. Enter:
   - **Phone Number:** Telnyx username.
   - **Account:** Telnyx username.
   - **Password:** Telnyx password.
   - **Display Name:** Caller ID following the naming conventions above.
   - **Register Name:** Telnyx username.
   - **User Name:** Telnyx username.
   - **Password:** Telnyx password.
   - **SIP Server:** `sip.telnyx.com`.
   - **SIP Port:** `5060` for UDP, `5061` for TLS.
4. Press **OK**.

## Positron IP Phone Setup

The Positron IP phone line (IP304/IP304C, IP408/IP408C, IP410C/IP410G) is a SIP phone with wideband audio, dual Ethernet ports, and integrated PoE. Configuration steps are identical across models aside from minor cosmetic UI differences.

### Get the IP address and log into the web portal

1. From the phone, press **Menu > Status > Information** to view the IP address.
2. From a computer, open a browser and enter `http://<phone-ip>`.
3. Default credentials: **Username:** `admin`, **Password:** `admin`. Change these after first login.

### Configure the SIP profile via the web portal

1. Navigate to **Account > Basic** and configure:
   - **Account:** Select the account (e.g., `Account 1`).
   - **Account Active:** `Yes`.
   - **Primary SIP Server:** `sip.telnyx.com`.
   - **SIP Transport:** `UDP` (default); choose `TLS` if call encryption is enabled on the Telnyx portal.
   - **SIP User ID:** Telnyx account ID.
   - **Authentication ID:** Telnyx account ID.
   - **Authentication Password:** Telnyx account password.
2. Click **Save**.

### Configure the SIP profile from the phone

1. From the phone, navigate to **Menu > Settings > Advanced Settings > Accounts**.
2. Configure:
   - **Account:** Select the account.
   - **Account Active:** `On`.
   - **Primary SIP Server:** `sip.telnyx.com`.
   - **Proxy SIP Server:** `sip.telnyx.com` or leave blank.
   - **SIP User ID:** Telnyx account ID.
   - **Authentication ID:** Telnyx account ID.
   - **Authentication Password:** Telnyx account password.

### (Optional) Import a TLS certificate

1. Navigate to **Management > TLS Certs** in the web portal.
2. Upload the TLS certificate document.

### (Recommended) Change default admin credentials

1. From the phone, navigate to **Menu > Settings > Advanced Settings > Password > Phone Settings > Set Password**.
2. Enter the current password, the new password, and confirm the new password.
3. Save the changes.

## Dinstar C60 Series Setup

The [Dinstar C60](dinstar-c60.md) series delivers SIP technology with a 132x64-pixel graphical LCD, HD voice quality, support for 2 SIP accounts, and 5-party conferencing.

### Obtain the device IP and log into the web portal

1. From the phone, press **OK** and select **IPV4** to view the IP address.
2. From a computer on the same network, open a browser and enter the IP address.
3. Default credentials: **Username:** `admin`, **Password:** `admin`.

### Configure a Telnyx SIP trunk

1. Navigate to **Account > Basic Page**.
2. In the **SIP Account** section, provide:
   - **Account:** Main account or sub-account ID.
   - **Active:** `Enabled`.
   - **Display Label:** Name for the line.
   - **Display Name:** Caller ID in CAPITAL LETTERS, no special characters, max 15 characters.
   - **Register Name:** Main account or sub-account.
   - **Username:** Username associated with the Telnyx account.
   - **Password:** Password associated with the Telnyx account.
3. In the **SIP Server** section, provide:
   - **Server IP:** `sip.telnyx.com`.
   - **Port:** `5060`.
   - **Registration Expires:** `120`.
