---
title: Configuring IP PBX Appliances and Phones with Telnyx
summary: This page provides step-by-step instructions for configuring several popular
  IP PBX appliances and IP phones to work with Telnyx as the SIP carrier, including
  the Grandstream UCM6202 (using both Registration and IP authentication), the broader
  Grandstream UCM6xxx series, the Synway UC-200, and the Cisco 68xx/88xx series IP
  phones. Each section covers logging into the device's web UI, creating a SIP trunk,
  configuring inbound and outbound routes, and setting an outbound caller ID where
  applicable.
sources:
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
- url: https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup
- url: https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks
- url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
updated_at: 2026-07-17T09:08:00Z
---

# Configuring IP PBX Appliances and Phones with Telnyx

*Part 2 of 3 — see also: [Part 1](configuring-ip-pbx-appliances-and-phones-with-telnyx--part-1.md), [Part 3](configuring-ip-pbx-appliances-and-phones-with-telnyx--part-3.md)*

This page provides step-by-step instructions for configuring several popular IP PBX appliances and IP phones to work with Telnyx as the SIP carrier, including the Grandstream UCM6202 (using both Registration and IP authentication), the broader Grandstream UCM6xxx series, the Synway UC-200, and the Cisco 68xx/88xx series IP phones. Each section covers logging into the device's web UI, creating a SIP trunk, configuring inbound and outbound routes, and setting an outbound caller ID where applicable.

## Grandstream UCM6xxx: SIP Trunks

The Grandstream UCM6xxx series (including the UCM6200 and UCM6510) is a centralized IP PBX solution that unifies voice, video, conferencing, surveillance, and mobility on a single network. Note that firmware 1.0.18.x is the last supported firmware for UCM61xx devices, which will continue to receive critical security updates and major bug fixes only.

### Pre-requisites

- Device running the most current firmware
- Telnyx Mission Control Portal configured properly
- TLS encryption enabled (recommended)

### Additional Setup Considerations

- Extension range on UCM6xxx in main office: 1000–1999
- International dialing prefix: 99 (no size limits)
- Local numbers: start with 06, 10 digits in length

### Log into the UCM Device

1. Ensure the UCM device is powered on and showing an IP address on its screen.
2. From a computer on the same network, open a browser and enter the IP address in the format `http(s)://ipaddress:portnumber`. Default protocol is HTTPS and default port is 8089.
3. Default credentials: `admin` / `admin`.

### Create SIP Trunks

You will need the following Telnyx information to register your trunk(s):

| Field | Value |
| --- | --- |
| Provider address | `sip.telnyx.com` |
| Username | Your Telnyx SIP username |
| Authenticate ID | Your Telnyx SIP username |
| Password | Your Telnyx SIP password |
| Main number | Your main 10-digit number |
| Provided DIDs | The 10-digit DIDs you have provisioned |

1. Navigate to **Extension/Trunk > VoIP Trunks**.
2. Click **Add SIP Trunk** and on the **Basic Settings** tab, configure:
   - **Type:** Register SIP trunk
   - **Provider Name:** Telnyx
   - **Host Name:** `sip.telnyx.com` (append `:5061` if using TLS)
   - **Keep Trunk CID:** Enable if the trunk should send its own CID; disable if extensions will send their own
   - **Caller ID Name:** Your chosen caller ID (see naming conventions below)
   - **From Domain:** `sip.telnyx.com`
   - **Username:** Your Telnyx account/sub-account username
   - **Password:** Your Telnyx account/sub-account password
   - **Transport:** TCP or UDP (or TLS if encrypting)
3. On the **Advanced Settings** tab, configure:
   - **Codec Preference:** Use only Telnyx-supported codecs — `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
   - **Send PPI Header** or **Send PAI Header:** Enable only one (not both) to send caller ID in the SIP INVITE
   - **Passthrough PAI Header:** Enable if Send PAI Header is disabled, to preserve PAI headers on calls passing through UCM
   - **DTMF Mode:** Default (RFC2833)
   - **Enable Heartbeat Detection:** Check this box to prevent your modem from closing local SIP ports
   - **Heartbeat Frequency:** 60
   - **SRTP:** Enabled and forced (if using TLS)
4. Click **Save**, then **Apply Changes**.
5. Check registration status under **System Status > Dashboard**. A "Rejected" status indicates the UCM was not registered with Telnyx — verify server reachability and credentials.

### Configure Outbound Routes

1. Click **Extension/Trunk > Outbound Routes**, then click **+Add**.
2. Configure:
   - **Calling Rule Name:** Any name you want
   - **Pattern:** The dial pattern (a dial-out prefix can be added after the `_` character)
   - **Trunk:** The Telnyx trunk to use
   - **Privilege Level:** Required privilege for extensions to use this route
   - **Strip:** Number of digits to strip after the `_` character (e.g., set to 1 if using `9` as a dial-out prefix with pattern `_9NXXXXXXXXX`)

### Configure Inbound Route

1. Click **Extension/Trunk > Inbound Routes**, then click **Add**.
2. Configure:
   - **Trunks:** Choose your Telnyx trunk
   - **Patterns:** Type your Telnyx DID prefixed with `_`
   - **Default Destination:** Choose the default destination for incoming calls

It is not recommended to use more than one Telnyx trunk on the same device.

### Optional: Time Conditions

Set time conditions on inbound/outbound rules to use different routes at different times. Navigate to **Extension/Trunk > Outbound Routes** (or **Inbound Rules**), find the **Time Condition** section, select the time, and click **Add**.

### Optional: Group Trunks

Starting from firmware 1.0.20.17, you can create VoIP Trunk Groups to apply the same settings across multiple accounts on the same SIP server. Create a trunk group instead of a new trunk and use the **+** button in the **Username** field to add multiple trunks.

### Optional: Failover Route

Failover trunks ensure calls go through an alternate route when the primary trunk is busy or down. UCM6xxx uses failover trunks when:

- No response from the first trunk after 32 seconds
- The UCM receives 403/407/408/503/603 SIP responses from the primary trunk
- The primary trunk is disabled
- The primary trunk is an analog trunk and is busy or not connected

To configure: go to **PBX > Basic/Call Routes > Outbound Routes**, click **Click to add failover trunk**, select the failover trunk, and configure strip/prepend digits as needed.

## Synway UC-200: Telnyx Setup

The Synway UC-200 is an IP PBX appliance that supports up to 500 registered users with features like customizable call routing, multi-level IVRs, call queues, auto-attendant, CDR, multi-site peering, and voicemail/fax forwarding to email.

### Pre-requisites

- Telnyx Mission Control Portal configured properly
- A DID provisioned from Telnyx

### Log into the Synway UC-200

1. From a PC on the same network segment, open a browser (Chrome 67, Firefox 60, or IE11 recommended) and enter `https://192.168.0.101`.
2. Default credentials: `admin` / `admin`. Change the username and password immediately after first login.

### Configure Network Settings

DNS must be configured to resolve the domain if the UC-200 is on your local network.

1. From the left-hand navigation, click **System**, expand **Network Settings**, and click **Network Settings**.
2. On the **Basic Settings** tab, set **Default interface** to **LAN** and configure LAN settings below.

### Create the SIP Trunk

1. From the left-hand navigation, click **PBX**, expand **Trunks**, and click **Create Trunk**.
2. Configure:
   - **Trunk Type:** SIP
   - **Trunk Name:** A name of your choice (numbers and letters)
   - **Transport:** UDP
   - **Register:** Yes
   - **Username:** Your Telnyx SIP username
   - **Password:** Your Telnyx SIP password
   - **RegFall Retry:** Default 30 seconds
   - **Keep Inbound CallerID:** Use the registered account as the caller ID
   - **Outbound CallerID Name:** Your chosen caller ID (capital letters, no special characters, max 15 characters)
   - **Record:** False (default)
   - **Enabled:** True (default)
   - **Profile:** LAN
   - **Trunk IP/Domain:** `sip.telnyx.com:5060`

### Configure Outbound Route

1. Click **PBX**, expand **Trunks**, and click **Outbound Routes**.
2. Click **Add** and configure:
   - **Name:** `Telnyx_outbound` or similar
   - **Dial/DID patterns:** Regex matching the dial pattern (see the Synway user manual for examples)
   - **Strip:** Number of digits to strip from the dialed number (e.g., 1 if using `9` as a dial-out prefix)
   - **Prepend:** Optional digits to prepend to the dialed number
   - **Member Extensions:** Extensions authorized to use this route (required)
   - **Member Gateways:** The trunk configured above (required)
   - **Password:** Optional, for safety

### Configure Inbound Route

1. Click **PBX**, expand **Trunks**, and click **Inbound Routes**.
2. Click **Add** and configure:
   - **Name:** `Telnyx_inbound` or similar
   - **Dial/DID patterns:** Regex matching the dial pattern
   - **Destination:** The default extension for incoming calls
   - **Member Trunks:** The trunk configured above (required)

### Run a Call Test

1. Log into the Synway portal and dial extension **1000** to perform a "ping" call from the UC-200 to Telnyx and back.
2. Click **CDR** in the left-hand navigation to view the call log and confirm the test call was recorded.
