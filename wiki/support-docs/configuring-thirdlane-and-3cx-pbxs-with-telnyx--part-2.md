---
title: Configuring Thirdlane and 3CX PBXs with Telnyx
summary: This page covers how to configure Telnyx as a SIP provider for Thirdlane
  and 3CX (V18 and V20) PBX systems, including trunk creation, inbound/outbound routing,
  caller ID, SMS gateway setup, and compatibility considerations between 3CX and Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
updated_at: 2026-07-17T09:04:30Z
---

# Configuring Thirdlane and 3CX PBXs with Telnyx

*Part 2 of 6 — see also: [Part 1](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-1.md), [Part 3](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-3.md), [Part 4](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-4.md), [Part 5](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-5.md), [Part 6](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-6.md)*

This page covers how to configure Telnyx as a SIP provider for Thirdlane and 3CX (V18 and V20) PBX systems, including trunk creation, inbound/outbound routing, caller ID, SMS gateway setup, and compatibility considerations between 3CX and Telnyx.

## Thirdlane PBX Configuration

[Thirdlane IP-PBX](https://www.thirdlane.com/products/thirdlane-pbx) is a multi-tenant business communications platform aimed at ITSPs and companies that need to host multiple virtual PBX instances from a single web interface. The following steps walk through configuring a Thirdlane PBX to make and receive calls (and SMS) over Telnyx.

### Pre-requisites

Before configuring the trunk, complete the following:

- [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account), which includes:
  - Setting up a connection
  - [Provisioning a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) (see [Requesting Numbers](https://support.telnyx.com/en/articles/3562148-requesting-numbers))
  - Creating an outbound voice profile
- Thirdlane (non-Telnyx) setup:
  - [Download](https://www.thirdlane.com/products/multi-tenant-pbx) and [install](https://www.dropbox.com/s/w3c5oamhsnp4s26/PBXManagerAdminGuide.pdf?dl=0) Thirdlane PBX (trial — contact Thirdlane to provision an account)
  - Follow the [Getting Started and Configuration Manager steps](https://www.thirdlane.com/docs/platform/installing)
  - Perform a [default setup on Thirdlane](https://www.thirdlane.com/docs/platform/default-values)
  - [Configure TLS transport](https://www.thirdlane.com/docs/platform/tls-transport)
  - [Configure security settings](https://www.thirdlane.com/docs/platform/trusted-ips)
  - [Create an ICE server](https://www.thirdlane.com/docs/platform/ice-servers) (as of version 10.0.1, Thirdlane automatically installs and configures a STUN and TURN server)
  - [Configure dialplan variables](https://www.thirdlane.com/docs/platform/dialplan-variables)
  - Optional but recommended: [Create a dialplan script](https://www.thirdlane.com/docs/platform/dialplan-scripts)
  - Optional but recommended: Configure [default hold music](https://www.thirdlane.com/docs/platform/default-music-on-hold)
  - Set basic [inbound](https://www.thirdlane.com/docs/platform/inbound-permissions) and [outbound](https://www.thirdlane.com/docs/platform/outbound-dialing-permissions) permissions

### Create a SIP Trunk

A [SIP trunk](https://telnyx.com/products/sip-trunks) connects Thirdlane PBX with Telnyx so you can make and receive calls, send SMS, configure routes, and more.

> **Note:** When you create a new trunk, Thirdlane Configuration Manager prefills the form with values from your [default setup](https://www.thirdlane.com/docs/platform/default-values).

1. In the Thirdlane PBX portal, expand **Telephony Settings** in the left-hand menu and click **Trunks**.
2. Select **Create Trunk** and provide the following:
   - **Name:** Unique alphanumeric name (no spaces or special characters). In some cases the IP trunk name is provided by your service provider.
   - **Status:** Referenced in default Thirdlane scripts for outbound routes; allows temporarily disabling the trunk.
   - **Description:** Optional description.
   - **Available to tenants:** Multi-tenant only. Trunks can be available to all tenants or restricted to a specific tenant.
   - **Host:** IP address of your VoIP provider's gateway or proxy. For "friend" trunk types, you can also enter "dynamic".
   - **Outbound proxy:** `sip.telnyx.com`
   - **Context:** For external inbound providers, set to the default `from-outside` context.
   - **User Name:** Your Telnyx SIP trunk/account username
   - **Password:** Your Telnyx SIP trunk/account password
   - **Enabled codecs:** Use Telnyx codec preferences — `ulaw (g711u)`, `alaw (g711a)`, `g722`, `g729`
   - **Disabled codecs:** Codecs not supported by Telnyx, or supported codecs you don't want to use
   - **Encryption:** Choose one of:
     - **Enforce** — all outbound calls encrypted; only encrypted inbound accepted
     - **Reject** — all outbound calls unencrypted; only unencrypted inbound accepted
     - **Negotiate, trying encrypted first** — try encrypted, fall back to unencrypted; accept both inbound
     - **Negotiate, trying unencrypted first** — try unencrypted, fall back to encrypted; accept both inbound
   - **DTMF mode:** `In-audio, RFC2833`
   - **Quality (ms):** `No` (the amount of time the server waits for keepalive packets from the endpoint)
   - **Other Options:** Additional options in `key=value` form, one per line
   - **Registration:** Leave blank

![Expanding telephony settings through Thirdlane PBX portal.](_images/058365c5624be832.png)

> **Note:** You can delete a trunk, but deleting a trunk used by an outbound route will make the route invalid.

### Configure Trunk Dialing

Configure how the trunk interprets dialed numbers (for example, whether users must dial 9 to reach an outside line).

1. Expand **System Management** in the left-hand menu and click **Trunks**.
2. Edit the trunk you want to configure.
3. Select the **Trunk Dialing** tab and provide:
   - **Number of digits to strip:** Digits stripped from the front of a dialed number (e.g., strip 1 digit if users press 9 to dial out)
   - **String to prepend:** String prepended to the dialed number (can also be specified in outbound routes)
   - **Dial command options:** Prepends specific options to the dial command options string
   - **SIP Header:** Up to 4 custom SIP headers, e.g., `X-Custom-Header:VALUE`

![Configuring trunk dialing through Thirdlane PBX portal.](_images/0a15e314eec8acdb.png)

### Configure Caller ID

Specify how to alter Caller ID on outbound calls based on the trunk dialing configuration.

1. Expand **System Management** in the left-hand menu and click **Trunks**.
2. Edit the trunk you want to configure.
3. Select the **Caller ID** tab and enter:
   - **Number of digits to strip:** Digits stripped from the front of a dialed number
   - **String to prepend:** String prepended to the dialed number (can also be specified in outbound routes)

### Set Up Phone Numbers Using Provisioned DIDs

Create phone numbers from the [DIDs you provisioned from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers).

1. Expand **System Management > Telephony Settings** in the left-hand menu and click **Phone Numbers** (some setups may show **DIDs** instead — click that if so).
2. To filter the number view, use the controls above the phone number list:
   - **Select from:** `All`, `Assigned to tenants`, `Unassigned numbers`, `Assigned to the currently selected tenant`, `Phone numbers in use`
3. To add a range of new phone numbers:
   - Enter your range using the **From** and **To** fields (from bottom of range to top of range)
   - **Prepend:** Prefix to prepend to numbers in the range (e.g., a leading 0 or +)
   - **Assign:** Check to assign the new phone numbers to the currently selected tenant
4. Click **Add Phone Numbers**.

![An interface to set up phone numbers using provisioned DIDs](_images/6bd505e1092904b2.png)

> **Note:** You can also add phone numbers in bulk by uploading them in `.csv` format.

### Configure Inbound Routes

Specify the inbound route a caller will take when they dial a number (e.g., routed to a user's extension or an IVR).

1. From the left-hand navigation, expand **Selected Tenant Management**.
2. Expand the **Call Routing** dropdown and select **Inbound routes**.

![An interface for configuring call routes.](_images/d1d0c0de05bdf96b.png)

3. Select **Time Based Routes Group**, then **Add Route**. Enter the details and press **Save**.

![Selecting time based routes group for inbound routes.](_images/3d503099f668b00b.png)

Inbound calling to your DID is now ready. Register your client to the PBX using the extension's username and password; the domain is the public IP of your PBX server.

### Assign and Unassign Numbers to the Tenant

**To assign unassigned numbers:**

1. Expand **System Management** and select **DIDs**.

![An interface to assign any unassigned numbers to the tenant](_images/021d6d871f97c376.png)

2. Find the number you want to enable and click the checkbox beside it.
3. Click **Assign Selected** in the top-right. The DID is assigned to the current tenant and becomes available to assign to an extension.

![An interface for assigning selected DIDs.](_images/a031f8cb709f0939.png)

**To unassign numbers:**

1. Select the number(s) using the checkbox next to them and click **Unassign Selected** in the top navigation.

![Page to unassign numbers from the tenant.](_images/ec8e6b0d4f809c8e.png)

> **Note:** You cannot unassign a number currently in use without first deleting its corresponding inbound route.

### Create Extensions for Assigned Numbers

1. From the left pane, navigate to **Selected Tenant Management** and expand the dropdown.
2. Click **Extensions and Contacts**, then select **User Extensions**.

![Page for creating extensions for your assigned numbers 1.](_images/7e005c0c02316805.png)

3. Click **Create Extension** and open the **Basic** tab.
4. Enter the first name, last name, and extension number for the user.

![Page for creating extensions for your assigned numbers 2.](_images/35d64b0b004bcc59.png)

5. Click **Save**. The extension appears in your extensions section.

![Page for creating extensions for your assigned numbers 3.](_images/05a77932c9586a42.png)

6. Open the new extension for editing (pencil icon) and click the **Phone** tab.
7. Find the **SIP User name** and **Password** fields. These values, along with your server IP address, are used to register other devices to the PBX so they can receive inbound calls to the associated DIDs.

![Page for creating extensions for your assigned numbers 4.](_images/9afe1698f6dc8cd5.png)

8. Return to the DID section. The DID you just set up should now show the **Used in Inbound Routes** checkbox enabled and be associated to the extension.

![Page for creating extensions for your assigned numbers 5.](_images/5ec2af059a091145.png)

### Configure SMS Gateway

1. Expand **System Management** in the left-hand menu and click **SMS Gateways**.
2. Click **Create** and provide:
   - **Name:** Unique alphanumeric name (no spaces or special characters)
   - **Provider:** `Telnyx`
   - **Description:** Optional
   - **Domain:** Domain used to receive inbound SMS messages and status information from your SMS provider
   - **API Key:** Provision from [API Keys](https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them)

Once created, the Configuration Manager generates a URL for receiving inbound SMS messages and status information from Telnyx. Specify these URLs in your Telnyx Mission Control Portal.

> **Note:** Deleting an SMS gateway used by an inbound route will make the route invalid.

### Enable SMS for Phone Numbers

1. Expand **System Management** and click **Phone Numbers**.
2. Select the number(s) you want to SMS-enable using the checkbox next to them.
3. Use the **SMS Gateway** dropdown to select a configured gateway.
4. Click **Set SMS Gateway for selected**.
5. After enabling SMS, assign numbers to users in **Inbound SMS Routes**.

![Interface for SMS enablement for your new numbers.](_images/172533199179785e.png)

### Post-Requisites

Before you can make calls, ensure the following are configured (refer to Thirdlane's documentation for the most current source of truth):

1. Extensions and contacts via the [Bulk Generator](https://www.thirdlane.com/docs/platform/bulk-generator), [User Extensions](https://www.thirdlane.com/docs/platform/user-extensions), and the [Company Directory](https://www.thirdlane.com/docs/platform/company-directory)
2. Call routing: [inbound routes](https://www.thirdlane.com/docs/platform/inbound-routes), [outbound routes](https://www.thirdlane.com/docs/platform/outbound-routes), [dialing permissions](https://www.thirdlane.com/docs/platform/tenant-outbound-dialing-permissions#!), and [day/night mode](https://www.thirdlane.com/docs/platform/daynight-mode)
3. [Inbound SMS routing](https://www.thirdlane.com/docs/platform/inbound-sms-routes)
4. Additional [Thirdlane-side PBX features](https://www.thirdlane.com/docs/platform/pickup-groups#!)
