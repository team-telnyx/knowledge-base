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

*Part 2 of 3 — see also: [Part 1](third-party-pbx-sip-trunk-configurations--part-1.md), [Part 3](third-party-pbx-sip-trunk-configurations--part-3.md)*

Step-by-step guides for connecting a wide range of third-party IP PBX systems and gateways to Telnyx via SIP trunks, covering credentials-based and IP authentication, inbound/outbound routing, codecs, and device-specific settings.

## VitalPBX

VitalPBX is an Asterisk-based unified communications PBX. It supports both credentials-based (user/pass) and IP authentication trunks.

### Credentials-Based Trunk (PJSIP)

1. Navigate to **External > Trunks** and create a new trunk:
   - **Technology:** PJSIP or SIP (not IAX)
   - **Codecs:** Select g722, g729, ulaw (Telnyx-supported from VitalPBX's list)
   - **Trunk CID:** One of your Telnyx DIDs
   - **Overwrite CID:** *If not provided* (allows external caller ID on call forwards)
   - **Local User:** A name for the trunk
   - **Contacts / Match:** `sip.telnyx.com`
   - **Remote Username:** Telnyx SIP username
   - **Remote Secret:** Telnyx password
   - **Require Registration:** Yes
   - **Permanent Auth Rejection:** Yes

### IP Authentication Trunk

Same as credentials-based, except:
- **Require Registration:** No
- **Permanent Auth Rejection:** No

### Outbound Routes

Under **Extensions > Outbound Routes**, configure routes for emergency, local, toll-free, mobile, international, special, and long-distance calls. Dial pattern syntax uses `X` (0–9), `Z` (1–9), `N` (2–9), `.` (one or more), `!` (zero or more), and bracket ranges. Tip: pattern `4443` for sound quality test, `4747` for DTMF test.

### Inbound Routes

Under **Extensions > Inbound Routes**, set the **Routing Method**, **DID Pattern** (must exactly match the format the provider sends, e.g., `+15555555555` or `5555555555`), **CID Pattern**, and destination module. The DID Pattern field supports patterns starting with `_` (e.g., `_555555123[45]`).

Additional resources: [VitalPBX user guide](https://wiki.vitalpbx.com/wiki-category/vitalpbx/)

## Positron IP PBX

Positron IP PBX offers VoIP systems for small and medium businesses.

1. Navigate to **PBX > Trunks/Lines > Trunks/Lines** and click **Add**:
   - **Name:** Telnyx (or similar)
   - **IP Address/Domain:** `sip.telnyx.com`
   - **Username:** Telnyx SIP username
   - **Password:** Telnyx SIP password
   - **Port:** `5060`
2. Click **Save**, then **Edit** the trunk:
   - **From User:** Remove the username from this field
   - **P-Asserted-Identity:** Set to *Custom* and enter your provisioned DID
3. Click **Save** then **Apply**

### Outbound Rules

Under **PBX > Trunks/Lines > Outgoing Line Groups**, create a group linked to your trunk. Then under **PBX > Call Handling > Outgoing Call Rules**, define the ruleset for extensions.

### Inbound Rules

Under **PBX > Trunks/Lines > Incoming Call Rules**, create a group linked to your trunk. Edit the group, enter the **DID** field with your provisioned DID, and choose the destination extension. If using another SIP trunk provider simultaneously, set **SIP Registration Timer** to a minimum of 600 under **PBX > PBX Settings > SIP**.

## PBXes

PBXes.org is a German-hosted PBX service. The website defaults to German; right-click and select **Translate to English** if needed.

### Add a SIP Trunk

1. Log into pbxes.com, expand **Trunks** and click **Add Trunk > Add SIP Trunk**
2. Under **General Settings**:
   - **Trunk Name:** Your choice
   - **DTMF mode:** Auto
   - **sendrpid:** No
3. Under **Account**:
   - **username / password:** Telnyx SIP credentials
   - **SIP server or proxy / domain:** `sip.telnyx.com`
   - **register:** Yes (inbound and outbound)

### Inbound Routing

Under **Inbound Routing > Add Route**, optionally set Outbound Caller ID (CAPITAL LETTERS, no special characters, max 15 characters). Set **Dial Rules** to `1+NXXNXXXXXX`.

### Outbound Routing

Under **Outbound Routing > Add Route**:
- **Route Name:** `Telnyx_out` or similar
- **Trunk Sequence:** Select `SIP/Telnyx`
- **Custom Dial Patterns:** `NXXNXXXXXX`

Additional resources: [PBXes documentation](https://www1.pbxes.com/community.php?display=wiki), [PBXes forum](https://www1.pbxes.com/community.php?display=forum)

## Wildix

Wildix is a browser-based WebRTC-compatible VoIP PBX.

### Basic SIP Trunk Settings

1. Navigate to **WMS > Trunks > Trunks**, click **+** under the SIP table
2. Configure:
   - **Title / Trunk Name:** Descriptive name
   - **Auth Login / From User:** Telnyx SIP username
   - **From Domain:** `sip.telnyx.com`
   - **Address or Host Name:** `sip.telnyx.com`
   - **Password:** Telnyx SIP password
   - **Dialplan:** Typically `main`
   - **Tone Zone / Country Code:** Your region
   - **Keep-Alive:** Enabled
   - **Enable Registration:** Checked
   - **Registration Proxy > Address or Host Name:** `sip.telnyx.com` with Telnyx credentials

### Advanced Settings

- **Audio codecs:** ulaw, alaw, g722, g729
- **Video codecs:** H264
- **T38:** Yes
- **Session timer:** Checked, min `90`, max `600`
- **Registration expiry:** `180` seconds
- **Transport:** UDP
- **DTMF mode:** RFC2833

Additional resources: [Wildix technical documentation](https://wildix.atlassian.net/wiki/spaces), [Custom config parameters](https://wildix.atlassian.net/wiki/spaces/DOC/pages/30285078/Custom+config+parameters+List)

## Synway UC-200

The Synway UC-200 is an IP PBX appliance supporting up to 500 users with no licensing fees.

1. **Log in:** Browse to `https://192.168.0.101` (default: `admin` / `admin`; change immediately)
2. **Network settings:** Under **System > Network Settings**, ensure DNS is configured for domain resolution
3. **Create SIP trunk:** Under **PBX > Trunks > Create Trunk**:
   - **Trunk Type:** SIP
   - **Transport:** UDP
   - **Register:** Yes
   - **Username / Password:** Telnyx SIP credentials
   - **Profile:** LAN
   - **Trunk IP/Domain:** `sip.telnyx.com:5060`
   - **Outbound CallerID Name:** Follow standard conventions (CAPITAL LETTERS, no special characters, max 15 characters)
4. **Outbound route:** Under **PBX > Trunks > Outbound Routes**, add a route with regex dial patterns, strip/prepend rules, member extensions, and member gateways
5. **Inbound route:** Under **PBX > Trunks > Inbound Routes**, add a route with a regex DID pattern, destination extension, and member trunks
6. **Test:** Dial extension `1000` for a loopback test, then check **CDR** for the call log

Additional resources: [Synway user documentation](https://wiki.synway.net/index.php/User_Manual)

## PhoneSuite Voiceware

PhoneSuite Voiceware is a software-based IP-PBX designed for the hospitality industry.

1. Open the Voiceware portal, go to the **Advanced** tab, and ensure **DTMF Mode** is set to *Auto*
2. Create a new SIP trunk:
   - **Type:** SIP
   - **Secret:** Telnyx password
   - **Username:** Telnyx account number
   - **Insecure:** Invite
   - **Host:** `sip.telnyx.com`
   - **Port:** `5060`
   - **NAT / Register:** Checked
   - **Audio Codecs:** Move ulaw, alaw, g722, g729 from Available to Allowed
   - **Usable as Trunk:** Checked
   - **Channels:** One channel per simultaneous call
   - **Credentials:** Same as Above
   - **Reg. Server:** `sip.telnyx.com`

Additional resources: [PhoneSuite contact](https://phonesuite.com/lets-get-started/)
