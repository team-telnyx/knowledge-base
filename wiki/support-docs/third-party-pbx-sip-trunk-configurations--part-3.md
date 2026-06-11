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

*Part 3 of 3 — see also: [Part 1](third-party-pbx-sip-trunk-configurations--part-1.md), [Part 2](third-party-pbx-sip-trunk-configurations--part-2.md)*

Step-by-step guides for connecting a wide range of third-party IP PBX systems and gateways to Telnyx via SIP trunks, covering credentials-based and IP authentication, inbound/outbound routing, codecs, and device-specific settings.

## ScopTEL IP PBX

ScopTEL is a comprehensive all-in-one IP PBX and call manager with multi-tenant and unified communications support. Minimum software release: `scopserv-telephony25-6.9.1.6.20191218-1`.

### Configure SIP Channel

Under **Configuration > Telephony Settings: Channels > SIP Channel > Edit**, configure **Miscellaneous** settings for early audio and premature media as needed.

### (Recommended) Configure SIP TLS/SRTP

Under **Configuration > SIP Channel**, check **Enable support for SIP TLS (secure)** and **Don't verify servers certificate when acting as client**. SIP traffic encryption must also be activated in your Telnyx portal.

### Create SIP Trunk

Under **Interfaces > VoIP Accounts > Add a new VoIP Account**:

- **General tab:** Type *SIP*, Trunk Type *Friend*, Name (must be unique, alphanumeric; set to the username if receiving calls)
- **Server tab:** Username/password (Telnyx credentials), Host `sip.telnyx.com`, Port `5060`, **Register as User Agent** checked, **Enable TLS registration** checked if configured, **Contact Extension** = Telnyx username
- **Network tab:** Transport mode UDP/TCP (or TLS only if configured), **Insecure** = Invite checked
- **Options tab:** **DTMF Mode** *Automatic*, **Send Remote-Party-ID** checked, Codecs = ulaw, alaw, g722, g729, H264, **Disallowed Methods** = UPDATE checked

### Create Inbound Rules

Under **Lines > Incoming Lines > Add a new Incoming Line**:
- **Extension (DNIS):** Your Telnyx DID
- **Trunk:** Select the trunk created above

Additional resources: [ScopServ user guides](http://www.scopserv.us/support/documentation/)

## sipXecs PBX

sipXecs is an open-source unified communications PBX by SIPfoundry, scaling to mid-size and large enterprises.

### Installation

Install on CentOS 6 or RHEL 6 (physical or VM) with minimum 4 GB RAM and 40 GB storage. Run:

```
bash -c "$(curl -L http://rpms.sipfoundry.org/canary-release/sipxecs-install)"
```

Or install via yum repo, then run `/usr/bin/sipxecs-setup`.

### Configure SIP Trunk

During setup, provide:
- **Domain / SIP Domain:** `sip.telnyx.com`
- **SIP Realm:** Your realm name

### Admin Console

Browse to the server IP (acknowledge certificate warning), set the superadmin password. Enable required services under **System > Servers** and add at least one user under **Users > Users**.

### Add Phones

Under **Users > Users**, select a user and click **Phones**. If auto-provisioning is configured, phones auto-discover. Otherwise, manually configure with: **User ID** (numeric extension), **Domain** `sip.telnyx.com`, **Password** (Telnyx account/sub-account password), **Auth Name** (numeric extension), and **Display Name** following caller ID conventions.

### Troubleshooting

If a manually configured phone is not working, check DNS under **System > DNS > Advisor**.

Additional resources: [sipXecs documentation](https://sipfoundry.atlassian.net/wiki/display/sipXecs/Home), [sipXecs download](http://www.sipfoundry.org/sipxecs-software-download/)

## Dinstar C60

The Dinstar C60 is a SIP desk phone supporting 2 SIP accounts and 5-party conferencing.

1. **Get IP address:** On the phone, press **OK**, select **IPv4**, and note the IP
2. **Log in:** Browse to the IP address (default: `admin` / `admin`)
3. **Configure SIP account:** Under **Account > Basic Page**:
   - **Account:** Your Telnyx account or sub-account ID
   - **Active:** Enabled
   - **Display Name:** Caller ID name (follow naming conventions)
   - **Register Name / Username:** Telnyx username
   - **Password:** Telnyx password
4. **Configure SIP server:**
   - **Server IP:** `sip.telnyx.com`
   - **Port:** `5060`
   - **Registration Expires:** `120`

Additional resources: [Dinstar downloads](https://www.dinstar.com/download/), [Dinstar support](https://www.dinstar.com/contact-us/)

## Voice Elements

Voice Elements is a Microsoft .NET development environment for building automated telephone systems (IVR, auto attendants, call centers, etc.).

1. Open the Voice Elements wizard, select the **Connectivity** tab
2. Under **Carrier/Gateway/Devices**, select *Other*
3. Under **Location**, select *External IP Authentication (SIP Carrier - Preferred)*
4. Enter connection information:
   - **Destination IP/URL:** `sip.telnyx.com`
   - **Registrar IP/URL:** `sip:sip.telnyx.com`
   - **AuthURI:** `your_telnyx_username@sip.telnyx.com`
   - **Username / Pwd:** Telnyx SIP credentials
   - Port `5060` for UDP/TCP; `5061` for TLS
5. **Firewall:** Restrict SIP port access to [Telnyx IP addresses](https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses) only to prevent SIP sniffer attacks

Additional resources: [Voice Elements documentation](https://www.voiceelements.com/docs/), [Voice Elements firewall configuration](https://www.voiceelements.com/docs/programmable-voice/configuration/firewall/)

## Ubiquiti UniFi Talk

UniFi Talk is a subscription-based VoIP solution requiring specific UniFi hardware (Dream Machine Pro or Cloud Key Gen 2 Plus, PoE switches, and Talk-compatible devices). This configuration uses IP authentication.

### Add a Telnyx SIP Trunk

1. From the Talk dashboard, click **Settings > System Settings > Third Party SIP Setup > Add Third Party SIP Provider**
2. Name the provider (e.g., *Telnyx*)
3. Add custom fields with **exact names**: `proxy`, `realm`, `context`, `password`, `register`, `username`, `extension`, `from-user`, `from-domain`, `retry_seconds`, `expire_seconds`
4. Set field values:
   - **proxy:** `192.76.120.10` (US; see [signalling addresses](https://sip.telnyx.com/#signaling-addresses) for other regions)
   - **realm:** `sip.telnyx.com`
   - **context:** `public`
   - **password:** Any value (required by UniFi even for IP auth)
   - **register:** `false`
   - **username / from-user:** Telnyx username
   - **from-domain:** `192.76.120.10` (or your UniFi Talk static IP if this doesn't work)
   - **retry_seconds:** `30`
   - **expire_seconds:** `120`

### Authorize International Calls

Under **System Settings**, click **Select Countries**, choose allowed destinations, and ensure your Telnyx account permits international calling.

### Configure Phone Numbers

Under **System Settings > DID Numbers**, enter Telnyx DIDs in E.164 format (`+1XXXXXXXXXX`). The `+` prefix is **required**. Numbers can be entered one by one or imported from a `.txt` file (one number per line, each starting with `+`).

### Set IP Address Range

Under **System Settings > IP Address Range**, add the Telnyx signalling IP (`192.76.120.10/32` for US; adjust for other regions).

### Assign a Phone Number to a User

Under the users section, edit a user, click **Manage > Change Number**, and select an unassigned DID.

Additional resources: [UniFi Talk FAQ](https://www.ui.com/new-integrations/managed-voip), [UniFi Console quick-start guide](https://dl.ui.com/qig/udm-pro/#index)
