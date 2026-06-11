---
title: Third-Party PBX SIP Trunk Configurations
summary: Step-by-step guides for connecting a wide range of third-party IP PBX systems
  and gateways to Telnyx via SIP trunks, covering credentials-based and IP authentication,
  inbound/outbound routing, codecs, and device-specific settings.
sources:
- url: https://support.telnyx.com/en/articles/5728748-epygi-ip-pbx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5733572-mediatrix-c7-4100-telnyx-setup
- url: https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/5754445-vitalpbx-configuring-your-vitalpbx
- url: https://support.telnyx.com/en/articles/5790910-positron-ip-pbx
- url: https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx
- url: https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup
- url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
- url: https://support.telnyx.com/en/articles/5800936-phonesuite-voiceware
- url: https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
- url: https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config
- url: https://support.telnyx.com/en/articles/6145484-voice-elements-telnyx-sip
- url: https://support.telnyx.com/en/articles/6303467-ubiquiti-trunk-unifi-talk-ip-auth
updated_at: 2026-06-11T11:28:51Z
---

# Third-Party PBX SIP Trunk Configurations

*Part 1 of 3 — see also: [Part 2](third-party-pbx-sip-trunk-configurations--part-2.md), [Part 3](third-party-pbx-sip-trunk-configurations--part-3.md)*

Step-by-step guides for connecting a wide range of third-party IP PBX systems and gateways to Telnyx via SIP trunks, covering credentials-based and IP authentication, inbound/outbound routing, codecs, and device-specific settings.

## Common Prerequisites

Before configuring any PBX with Telnyx, ensure the following are in place:

- Your [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account is [set up and configured](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- You have [provisioned at least one DID](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) and assigned it to a connection
- You have [configured an outbound voice profile](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles) and assigned your connection to it
- You have your SIP credentials (username and password) from your Telnyx account or sub-account

## Common Telnyx SIP Parameters

Most PBX configurations share these core settings:

| Parameter | Value |
|---|---|
| SIP Server / Registrar / Host | `sip.telnyx.com` (country-specific TLDs such as `.ca`, `.au`, `.eu` may apply) |
| SIP Port | `5060` (UDP/TCP); `5061` for TLS |
| Transport | UDP by default; TLS if encryption is enabled |
| Registration | Required for credentials-based auth; disabled for IP auth |
| DTMF Mode | Auto or RFC 2833 |
| Insecure | `Port, Invite` (where applicable) |

For international signalling addresses, refer to [Telnyx signalling addresses](https://sip.telnyx.com/#signaling-addresses).

## Caller ID Naming Conventions

Across all integrations, Telnyx recommends the following for outbound Caller ID Name:

- Use **CAPITAL LETTERS** for readability on devices
- **No special characters** (spaces are allowed)
- **Maximum 15 characters** (some Canadian carriers truncate longer names)
- For US numbers, Caller ID Name must be updated in the CNAM database by contacting Telnyx support

## Supported Codecs

Telnyx supports the following codecs for voice and video:

**Audio:**

- ulaw (G.711 µ-Law) — standard for North America and Japan
- alaw (G.711 A-Law) — standard for Europe and other regions
- g722
- g729

**Video:**

- H264

When using G.711 µ-Law, set packetization time (ptime) to 20–30 ms. In North America, disable G.711 A-Law unless specifically required.

## Epygi IP PBX (QX Series)

Epygi QX series IP PBX appliances (QX20, QX50, QX200, QX500, QX2000, QX3000, QX5000, QXISDN4+, ecQX, UC20, UC80) use a VoIP Carrier Wizard for configuration.

1. Access the QX web interface at `http://172.30.0.1` (default credentials: `admin` / `19`; change immediately)
2. Navigate to **Telephony** to open the VoIP Carrier Wizard
3. Set **VoIP Carrier** to *Manual* and **Description** to *Telnyx*
4. Configure carrier settings:
   - **Account Name:** Telnyx SIP username
   - **Password:** Telnyx SIP password
   - **SIP Registrar:** `sip.telnyx.com`
   - **SIP Server Port:** `5060`
   - **Use RTP Proxy:** Enabled
5. Set the **Access Code** (e.g., `011` for outgoing through Telnyx), **Emergency Code** (e.g., `911`), and **Route Incoming Calls To** the desired extension
6. Confirm and finish the wizard

Dial patterns: internal extensions directly; external calls use `9` + 10-digit number; emergency uses the configured code.

Additional resources: [Epygi website](https://www.epygi.com/about-us/), [Quick install guide](https://www.epygi.com/wp-content/uploads/2019/03/Install-Guide-20_500IPPBXs-v02.pdf)

## Mediatrix C7/4100

The Mediatrix C7 and 4100 series gateways combine a VoIP analog adaptor and media gateway with FXS, FXO, and BRI interfaces. Apply the latest firmware before configuration.

1. **Connect to network:** Use the ETH1 (WAN on 4100) port for network access (DHCP by default). Dial `*#*0` on a connected phone to hear the device IP.
2. **Access GUI:** Browse to the device IP. Default login: username `public`, password empty.
3. **Set Telnyx server FQDN:** Under **SIP > Servers**, set **Registrar Host** and **Proxy Host** to `sip.telnyx.com`. Click **Apply** and restart required services.
4. **Register telephony ports:** Under **SIP > Registrations**, enable each analog port, enter the Telnyx username, and set a friendly name. Click **Apply**.
5. **Set credentials:** Under **SIP > Authentications**, click **Edit All Entries**. For each port: set **Criteria** to *Endpoint*, select the port, set **Validate Realm** to *Disable*, enter Telnyx username and password. Click **Apply & Refresh Registration**.
6. **Configure auto-routing:** Under **Call Router > Auto-routing**, enable auto-routing and set **Criteria Type** to *SIP Username*. Verify routes under **Call Router > Status**.
7. **Disable G.711 A-Law (North America):** Under **Media > Codecs**, disable G.711 A-Law for Voice and Data. Restart services. Edit G.711 µ-Law advanced settings and set **Minimum Packetization** to `20ms` and **Maximum Packetization** to `30ms`.
8. **Set DTMF maps:** Under **Telephony > DTMF Maps**, add a second row with **DTMF Map** `*xx` and **Transformation** `x`. This enables standard star codes like `*97` for voicemail.
9. **(Optional) Set time server:** Under **Network > Host**, set **SNTP Configuration Source** to *Static* and **Primary SNTP** to `pool.ntp.org`.

Additional resources: [Mediatrix C7 technical documentation](https://documentation.media5corp.com/pages/viewpage.action?pageId=16547905)

## Xorcom CompletePBX

Xorcom CompletePBX supports traditional PSTN and VoIP, including multi-tenant and hospitality PBX.

### Create a SIP Trunk

1. Navigate to **PBX > External > Trunks** and configure:
   - **Technology:** SIP
   - **Trunk CID:** If entering a Caller ID Name, use CAPITAL LETTERS, no special characters, max 15 characters (works for Canadian numbers; US requires CNAM database update via support). Set **Overwrite CID** to *Always* if using Trunk CID.
   - **Outbound Username:** Telnyx username
   - **Host:** `sip.telnyx.com`
   - **Port:** `5060`
   - **Remote Username / From User:** Telnyx username
   - **From Domain:** `sip.telnyx.com`
   - **Remote Secret:** Telnyx password
   - **Insecure:** Port, Invite
   - **Allow Inbound Calls / Qualify:** Yes
   - **Use Default:** Yes (register string auto-generated)
2. On the **Advanced** tab, add: **Type** *Peer*, **Parameter** `sendrpid`, **Value** `PAI`, **Enabled** *On*

### Configure Outbound Route

Under **PBX > External > Outbound Routes**, set a description, select the Telnyx trunk, and define dial patterns. For North America, use patterns like `NXXNXXXXXX` / `1NXXNXXXXXX`. A prefix (e.g., `9`) can be stripped before sending to Telnyx.

### Configure Inbound Route

Under **PBX > External > Inbound Routes**, set **Routing Method** to *Default*, enter a description, the DID number (without formatting), and the inbound destination.

Additional resources: [CompletePBX reference guide](https://files.xorcom.com/techdocs/pm0618-completepbx-reference-guide.pdf)
