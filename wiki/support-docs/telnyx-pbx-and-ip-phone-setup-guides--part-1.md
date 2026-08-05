---
title: Telnyx PBX and IP Phone Setup Guides
summary: This page consolidates Telnyx setup instructions for several PBX platforms
  and IP phones, including Vodia Multi-Tenant PBX, Ubiquiti UniFi Talk (credentials
  and IP authentication), and the Fanvil H2U, H3, H3W/H5W, H5, and A32i IP phones.
  It covers prerequisites, SIP trunk configuration, codec selection, inbound routing,
  and assigning DIDs to users.
sources:
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
- url: https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup
- url: https://support.telnyx.com/en/articles/6122586-ubiquiti-trunk-unifi-talk-auth
- url: https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip
- url: https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip
- url: https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip
- url: https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip
- url: https://support.telnyx.com/en/articles/6303467-ubiquiti-trunk-unifi-talk-ip-auth
updated_at: 2026-08-05T13:35:17Z
---

# Telnyx PBX and IP Phone Setup Guides

*Part 1 of 2 — see also: [Part 2](telnyx-pbx-and-ip-phone-setup-guides--part-2.md)*

This page consolidates Telnyx setup instructions for several PBX platforms and IP phones, including Vodia Multi-Tenant PBX, Ubiquiti UniFi Talk (credentials and IP authentication), and the Fanvil H2U, H3, H3W/H5W, H5, and A32i IP phones. It covers prerequisites, SIP trunk configuration, codec selection, inbound routing, and assigning DIDs to users.

## Overview

Telnyx provides SIP trunking that integrates with a variety of PBX systems and IP phones. This page consolidates setup guides for the following platforms:

- **Vodia Multi-Tenant PBX** (credentials-based trunk)
- **Ubiquiti UniFi Talk PBX** (credentials-based and IP authentication trunks)
- **Fanvil IP phones**: H2U Compact, H3 Hotel, H3W/H5W WiFi, H5 Hotel, and A32i Android Console

Common prerequisites across all setups include a properly configured Telnyx Mission Control Portal account, available DIDs, and (recommended) TLS encryption for SIP traffic. International deployments should consult the [Telnyx signaling addresses](https://sip.telnyx.com/#signaling-addresses) document for the correct regional SIP server.

## Vodia Multi-Tenant PBX Setup

Vodia PBX supports both CPE and hosted deployments and runs on Windows, Linux, or macOS. It provides automatic provisioning for mainstream SIP phones including Polycom, Snom, Cisco, Grandstream, and Yealink.

### Prerequisites

- Telnyx Mission Control Portal configured
- A credentials-based connection created in Mission Control
- TLS encryption enabled (recommended)
- Vodia downloaded and installed

### Create a SIP trunk

1. Log into Vodia PBX, navigate to your Domain, and choose **TRUNKS > VoIP Providers** from the left-hand navigation.
2. Click **Add**.
3. From the **Provider** dropdown, select *Telnyx*.

   ![The personal domain on the Vodia PBX.](_images/ac3b16ab3da8cb3f.png)
4. Enter your Telnyx username and password when prompted.

   ![Administration credentials on the Vodia interface.](_images/14c6c3b07a355313.png)
5. Click **Create**.

Because Vodia has a built-in Telnyx template, you do not need to enter the SIP outbound proxy or trunk headers. Vodia also automatically creates a dial plan for the domain.

### Configure inbound routing

1. Navigate to your registered Telnyx trunk and scroll down to **Routing/Redirection**.
2. Vodia supports the following inbound methods:
   - Send all to the destination request URL
   - Send all calls to a specific account
   - Send to a 10-digit DID
   - Match extension after a prefix
   - Use a list of expressions

   For this exercise, choose **Send all calls to a specific account** so all inbound calls route to the specified extension.

   ![Routing/Redirection for inbound.](_images/f80dd813490340da.png)
3. To route multiple Telnyx phone numbers into Vodia, switch to Admin mode and navigate to **DID management**.

   ![Admin on the Vodia PBX.](_images/2b08ca39269c44b3.png)
4. Use DID management to assign multiple DIDs to specific extensions.

   ![DID Management portal on the Vodia PBX.](_images/f01342e8f420ec37.png)
5. Navigate back to your Telnyx trunk, scroll to **Routing/Redirection**, and choose *Send all to the destination request URL*.

### Additional Vodia resources

- [Vodia documentation](https://doc.vodia.com/)
- [Supported phones](https://web.vodia.com/supported-phones)
- [Vodia forums](https://forum.vodia.com/)
- [Vodia support](https://vodia.zammad.com/#login) (login required)
- [Vodia portal login](https://portal.vodia.com/)

## Ubiquiti UniFi Talk PBX Setup

The UniFi Talk PBX is a subscription-based VoIP solution from Ubiquiti designed for small to medium businesses. Only Ubiquiti Talk devices are compatible with the Talk application.

### Prerequisites

- Telnyx Portal configured for use
- SIP credentials (username/password for main or sub-account) for credentials-based setup
- DIDs available to assign
- A UniFi Console (Dream Machine Pro or Cloud Key Gen 2 Plus) set up and configured
- PoE switches to power Talk devices
- A Talk device
- Talk application set up and up to date
- All firmware updates completed on endpoints

### Add a Telnyx SIP trunk to Talk

1. From the UniFi Talk dashboard, click the settings icon in the right-hand navigation.

   ![Settings section on the Unifi Talk dashboard.](_images/44196d7abf120b99.png)
2. Under UniFi Talk settings, click **System Settings**.

   ![System settings section on the Unifi Talk dashboard.](_images/133f8439d44cf87e.png)
3. Find the **Third Party SIP Setup** section and click **Add Third Party SIP Provider**.
4. Enter the provider name (e.g., *Telnyx*).

   ![Third Party SIP Setup on the Unifi Talk dashboard.](_images/cbff4949d1bc848a.png)
5. Click **Add Fields** and add the custom field names exactly as written below.
6. Click **Done** when finished.
7. Populate the field values.

#### Credentials-based authentication fields

Field names to add:

- *proxy*
- *realm*
- *username*
- *password*
- *register*
- *sip_cid_type*
- *retry_seconds*
- *expire-seconds*

Field values:

- **proxy**: *sip.telnyx.com*
- **realm**: *sip.telnyx.com*
- **username**: Your Telnyx account or sub-account username
- **password**: Your Telnyx account or sub-account password
- **register**: *true*
- **sip_cid_type**: *rpd*
- **retry_seconds**: *30*
- **expire-seconds**: *120*

#### IP authentication fields

Field names to add:

- *proxy*
- *realm*
- *context*
- *password*
- *register*
- *username*
- *extension*
- *from-user*
- *from-domain*
- *retry_seconds*
- *expire-seconds*

Field values:

- **proxy**: *192.76.120.10* (international deployments should consult the [signaling addresses](https://sip.telnyx.com/#signaling-addresses) document)
- **realm**: *sip.telnyx.com*
- **context**: *public*
- **password**: Any value (UniFi requires a password field even with IP auth)
- **register**: *false*
- **username**: Your Telnyx username
- **extension**: Leave blank
- **from-user**: Your Telnyx username
- **from-domain**: *192.76.120.10* (if this fails, use the static IP of your UniFi Talk instead)
- **retry_seconds**: *30*
- **expire-seconds**: *120*

### Authorize international outgoing calls

1. From **System Settings**, click **Select Countries**. Ensure your Telnyx account allows international calling.

   ![System Settings configuration for Countries' selection.](_images/d31e1f3b0ab24501.png)
2. Click **Save**.

### Configure phone numbers

1. From **System Settings**, open the **DID Numbers** section.
2. To manually import numbers, enter each Telnyx DID in E164 format (e.g., +1XXXXXXXXXX) into the **Input Numbers** field. The leading `+` is required.

   ![DID Numbers section on the System settings.](_images/bd76b84a80aa3a30.png)
3. To auto-import, click **Import Numbers with .TXT File**. Each number must be on a separate line and include the leading `+`.

### Set the IP address range

1. From **System Settings**, click **IP Address Range**.
2. Click **Add IP Address Range**.
3. **CIDR Network Address**: *192.76.120.10* (international deployments should consult the [signaling addresses](https://sip.telnyx.com/#signaling-addresses) document). Leave */32* as is.
4. Click **Add**.

   ![IP Address Range option on the System Settings Configuration domain.](_images/778a0c7923996815.png)

### Assign a phone number to a user

1. Click the users icon in the left-hand navigation.

   ![Users icon.](_images/017927714d45480f.png)
2. Find the user and click **Edit** at the far right of their row.

   ![Edit button.](_images/b874b12fa525d787.png)
3. In the user edit popup, click the **Manage** dropdown.

   ![Manage dropdown on the user edit popup.](_images/78329c3a0ab8ccb0.png)
4. In the **Change Number** section, select a DID. Unassigned numbers are labeled "Unassigned".

   ![Change Number section.](_images/1129bfa043d4622b.png)

### Additional UniFi Talk resources

- [UniFi Talk FAQ](https://www.ui.com/new-integrations/managed-voip)
- [UniFi Talk community](https://community.ui.com/)
- [UniFi Talk support](https://help.ui.com/hc/en-us)
- [Talk device firmware](https://www.ui.com/download/)
- [UniFi Console quick-start guide](https://dl.ui.com/qig/udm-pro/#index)
