---
title: Configuring PBX Systems and IP Phones with Telnyx
summary: Comprehensive guide for configuring a wide range of PBX platforms and IP
  phones to interoperate with Telnyx SIP trunks, covering authentication, trunk creation,
  inbound and outbound routing, caller ID, SMS, and version-specific considerations
  for systems including 3CX, Thirdlane, GOautodial, Grandstream, Yeastar, Vodia, Bicom,
  and Gigaset.
sources:
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
- url: https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a
- url: https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk
- url: https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
updated_at: 2026-06-11T11:29:02Z
---

# Configuring PBX Systems and IP Phones with Telnyx

*Part 1 of 4 — see also: [Part 2](configuring-pbx-systems-and-ip-phones-with-telnyx--part-2.md), [Part 3](configuring-pbx-systems-and-ip-phones-with-telnyx--part-3.md), [Part 4](configuring-pbx-systems-and-ip-phones-with-telnyx--part-4.md)*

Comprehensive guide for configuring a wide range of PBX platforms and IP phones to interoperate with Telnyx SIP trunks, covering authentication, trunk creation, inbound and outbound routing, caller ID, SMS, and version-specific considerations for systems including 3CX, Thirdlane, GOautodial, Grandstream, Yeastar, Vodia, Bicom, and Gigaset.

## Common Telnyx SIP Trunk Settings

Most devices and PBX platforms connecting to Telnyx share a core set of configuration parameters. The table below summarises the values you will need regardless of the platform you are configuring.

| Parameter | Value |
|---|---|
| SIP Server / Host | `sip.telnyx.com` |
| Outbound Proxy | `sip.telnyx.com` |
| From Domain | `sip.telnyx.com` |
| SIP Port (UDP/TCP) | 5060 |
| SIP Port (TLS) | 5061 |
| STUN Server | `stun.telnyx.com:3478` |
| Supported Audio Codecs | ulaw (G.711u), alaw (G.711a), G.722, G.729 |
| DTMF Mode | RFC2833 (default) |
| Authentication | Credentials-based (Register) or IP-based (Peer) |

For international signalling addresses, see [Telnyx SIP Signaling Addresses](https://sip.telnyx.com/#signaling-addresses).

### Common Prerequisites

Before configuring any device, ensure you have completed the following on the [Mission Control Portal](mission-control-portal.md):

1. Created a SIP connection (credentials-based or IP-based) under **Connections**.
2. Purchased and provisioned a DID number under **Numbers**.
3. Assigned the DID to your SIP connection.
4. Created an outbound voice profile under **Outbound Profiles**.
5. (Optional) Created a messaging profile under **Programmable Messaging > Profiles**.
6. (Recommended) Enabled TLS encryption on your connection.

### Caller ID Naming Conventions

When setting a Caller ID Name on any platform:
- Use **capital letters** for better visibility on some devices.
- **Do not use special characters**; they will not be displayed.
- Spaces are allowed.
- Some Canadian providers truncate display to 15 characters — keep names concise.
- Review the [Telnyx Caller ID Number Policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for accepted number formats.

## Thirdlane PBX

[Thirdlane](https://www.thirdlane.com/products/thirdlane-pbx) is a multi-tenant IP-PBX platform designed for Internet Telephony Service Providers managing multiple virtual PBXs.

### Thirdlane SIP Trunk Configuration

1. In the Thirdlane portal, go to **Telephony Settings > Trunks** and click **Create Trunk**.
2. Provide the following:
   - **Name**: Unique alphanumeric name (no spaces or special characters).
   - **Host**: IP address or `dynamic` for friend-type trunks.
   - **Outbound proxy**: `sip.telnyx.com`
   - **Context**: `from-outside` (for external inbound providers).
   - **User Name / Password**: Your Telnyx SIP credentials.
   - **Enabled codecs**: ulaw, alaw, g722, g729.
   - **Encryption**: Choose *Enforce*, *Reject*, or one of the *Negotiate* options.
   - **DTMF mode**: In-audio, RFC2833.
   - **Quality (ms)**: No.
   - **Registration**: Leave blank.
3. On the **Trunk Dialing** tab, configure digit stripping and prepending as needed (e.g., strip 1 digit if users dial 9 for an outside line).
4. On the **Caller ID** tab, configure caller ID digit stripping and prepending to match your trunk dialing configuration.

### Thirdlane Phone Numbers and Extensions

1. Go to **System Management > Telephony Settings > Phone Numbers** (or **DIDs**).
2. Add a range of numbers using the **From** and **To** fields. Optionally prepend a prefix and assign to a tenant.
3. Assign unassigned numbers to a tenant via **System Management > DIDs** — select the number and click **Assign Selected**.
4. To unassign, select the number and click **Unassign Selected** (you must first delete any inbound route using the number).
5. Create user extensions under **Selected Tenant Management > Extensions and Contacts > User Extensions**.
6. In each extension's **Phone** tab, note the **SIP User name** and **Password** for device registration.

### Thirdlane Inbound Routes

1. Go to **Selected Tenant Management > Call Routing > Inbound Routes**.
2. Select **Time Based Routes Group** then **Add Route**.
3. Configure the route destination and save.

### Thirdlane SMS Configuration

1. Go to **System Management > SMS Gateways** and click **Create**.
2. Set **Provider** to *Telnyx*, enter the **Domain** and your Telnyx **API Key**.
3. After creation, the Configuration Manager generates inbound SMS URLs — add these to your Telnyx Mission Control Portal messaging profile.
4. Enable SMS on specific numbers via **System Management > Phone Numbers** — select the numbers, choose an SMS gateway from the dropdown, and click **Set SMS Gateway for selected**.
5. Assign SMS-enabled numbers to users in **Inbound SMS Routes**.

### Thirdlane Post-Configuration

After Telnyx-specific setup, complete the following in Thirdlane:
- Configure extensions/contacts (Bulk Generator, User Extensions, Company Directory).
- Configure call routing (inbound routes, outbound routes, dialing permissions, day/night mode).
- Configure inbound SMS routing.
- Configure additional Thirdlane PBX features (pickup groups, hold music, etc.).

## GOautodial

[GOautodial](https://goautodial.com/) is an open-source omni-channel contact centre system with predictive, preview, and manual dialing, CRM, and real-time dashboards. Telnyx supports both IP-based and credentials-based (registration) authentication.

### GOautodial SIP Trunk — IP Authentication

1. In the GOautodial dashboard, go to **Settings > Carriers** and click **+** to add a new carrier. Choose **Manual** as the carrier type.
2. Provide:
   - **Carrier ID / Name**: `Telnyx`
   - **User Group**: All User Groups
   - **Authentication**: IP-Based
   - **SIP Server**: `sip.telnyx.com`
   - **Codecs**: ulaw, alaw, g722, g729
   - **DTMF Mode**: RFC2833
   - **Protocol**: SIP
   - **Server IP**: Your Telnyx-assigned IP (see [IP Authentication with X-Telnyx-Token](https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token))
   - **Active**: Yes

### GOautodial SIP Trunk — Registration Authentication

1. Follow the same initial steps as IP authentication, but set **Authentication** to *Registration*.
2. Provide:
   - **Username / Password**: Your Telnyx SIP credentials.
   - **Server IP/Host**: `sip.telnyx.com`
   - **Port**: 5060 (or 5061 if TLS is enabled)

### GOautodial Account and Dial Plan

On the Carrier page, click **Advance Configuration** and provide:

**Account Entry:**

```
[telnyx]
diallow=all
allow=ulaw
allow=alaw
type=friend
dtmfmode=rfc2833
qualify=yes
nat=yes
host=sip.telnyx.com
insecure=invite
```

**Dialplan Entry:**

```
exten => _X.,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)
exten => _1NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)
```

Adjust the last two lines for any internal extension mappings.

### GOautodial Outbound Campaign

1. Go to **Telephony > Campaigns**, click **+**, and select **Outbound**.
2. On the **Basic Settings** tab set:
   - **Dial Method**: Manual/Auto_Dial or Predictive.
   - **Auto Dial Level**: Slow, Normal, Max, or High.
   - **Carrier**: Telnyx.
3. Click **Update**.

### GOautodial Inbound Campaign

1. Go to **Telephony > Campaigns**, click **+**, and select **Inbound**.
2. Set **Call Route** to *Ingroup (default)*.
3. On the **Basic Settings** tab, set **Carrier** to *Telnyx*.
4. On the **Advanced Settings** tab, select the required **Inbound Groups** and **Allowed Transfer Groups** (e.g., AGENTDIRECT, AGENTDIRECT_CHAT).
5. Advise agents to always select the ingroup on the inbound campaign after logging in.

### GOautodial Lead Import

1. Go to **Telephony > List**, click **+**, and upload a `.csv` file formatted per GOautodial's lead file format (comma-delimited).
2. Confirm the upload status.
