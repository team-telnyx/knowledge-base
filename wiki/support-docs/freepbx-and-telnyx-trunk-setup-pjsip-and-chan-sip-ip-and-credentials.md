---
title: 'FreePBX and Telnyx: Trunk Setup (PJSIP and Chan_SIP, IP and Credentials)'
summary: This guide unifies Telnyx’s FreePBX setup instructions across versions 13–15,
  covering PJSIP (recommended) and Chan_SIP, for both IP-based and credentials-based
  trunks, plus routing, codecs, and key portal prerequisites.
sources:
- url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
- url: https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk
- url: https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials
- url: https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip
- url: https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip
- url: https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api
- url: https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial
- url: https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip
- url: https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip
updated_at: 2026-05-20T14:53:53Z
---

# FreePBX and Telnyx: Trunk Setup (PJSIP and Chan_SIP, IP and Credentials)

This guide unifies Telnyx’s FreePBX setup instructions across versions 13–15, covering PJSIP (recommended) and Chan_SIP, for both IP-based and credentials-based trunks, plus routing, codecs, and key portal prerequisites.

## Before you start

- Telnyx Mission Control Portal
  - Create a SIP Connection: IP-based (IP auth) or Credentials-based (username/password)
  - Purchase a DID and assign it to your SIP Connection (provision your number)
  - Create/assign an Outbound Voice Profile
- FreePBX
  - Install FreePBX (v13–v15 supported in these notes)
  - PJSIP is recommended over Chan_SIP (Chan_SIP is deprecated and typically listens on UDP 5160). PJSIP listens on 5060 by default and is actively maintained.
- Security and transport
  - Consider enabling TLS to encrypt signaling; use port 5061 for TLS. Otherwise use 5060 for UDP/TCP.

Useful links (external): FreePBX downloads/docs (https://www.freepbx.org/downloads/), Telnyx account setup (https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)

## Snapshot: installing FreePBX

- Boot the FreePBX ISO, choose Full Install (Asterisk 13 on v13 or Asterisk 16 on v14/v15), set the root password, wait for package install, reboot.
- Access the web UI via the PBX IP, create the FreePBX admin user, log in, activate, set locales, and review firewall prompts.

## Prepare Asterisk SIP settings (NAT and networking)

- In FreePBX: Settings > Asterisk SIP Settings
  - Populate your External Address and Local Networks.
  - For v13 with Chan_SIP and/or PJSIP enabled, confirm both sections (General, Chan_SIP; or General, PJSIP). Click Submit and Apply Config.

## Create your user extensions

- Preferred: Applications > Extensions > Add New PJSIP Extension
  - Outbound CID: your Telnyx number (optional if trunk will override)
  - PJSIP listens on port 5060 (UDP); set the secret as needed.
- If you must use Chan_SIP: Add New Chan_SIP Extension
  - Chan_SIP typically listens on UDP 5160 (non‑standard). Set secret and optional Outbound CID.
- If you don’t set an Outbound CID per extension, configure caller ID at the trunk or enable Caller ID Override in the Telnyx Connection’s Outbound Options.

## Configure your Telnyx trunk

Decide between IP-based or Credentials-based trunking, then choose PJSIP (recommended) or Chan_SIP. Field names below match FreePBX screens.

### IP-based trunk (PJSIP)

Connectivity > Trunks > Add Trunk > Add New PJSIP Trunk
- General
  - Trunk Name: Telnyx_IP
  - Outbound CallerID: your_Telnyx_number (optional)
- PJSIP Settings > General
  - Registration: None (IP auth requires no registration)
  - SIP Server: sip.telnyx.com (or your preferred Telnyx proxy)
  - SIP Server Port: 5060 (or 5061 for TLS)
- PJSIP Settings > Advanced
  - From Domain: sip.telnyx.com (when available in your UI)
- Codecs
  - Enable: ulaw, alaw, gsm, g722, g729, opus; for video, H264 supported by Telnyx
- Submit and Apply Config

### IP-based trunk (Chan_SIP)

Connectivity > Trunks > Add Trunk > Add New Chan_SIP Trunk
- SIP Settings > Outgoing (PEER Details)
  - type=friend
  - qualify=yes
  - insecure=port,invite
  - host=sip.telnyx.com
  - fromdomain=sip.telnyx.com
  - disallow=all
  - allow=ulaw
- SIP Settings > Incoming (USER/USER Details as applicable)
  - type=friend
  - insecure=port,invite
  - host=sip.telnyx.com
  - dtmfmode=rfc2833
  - disallow=all
  - allow=ulaw
- Submit and Apply Config

### Credentials-based trunk (PJSIP)

Connectivity > Trunks > Add Trunk > Add New PJSIP Trunk
- General
  - Trunk Name: Telnyx_userAuth
  - Outbound CallerID: your_Telnyx_number (optional)
- PJSIP Settings > General
  - Username: your Telnyx SIP credentials username
  - Auth Username: your Telnyx SIP credentials username
  - Secret: your Telnyx SIP credentials password
  - Authentication: Outbound (if shown)
  - Registration: Send
  - SIP Server: sip.telnyx.com
  - SIP Server Port: 5060 (5061 for TLS)
  - Context: from-pstn (if available)
  - Transport: UDP or TCP (TLS/TCP if using TLS)
- PJSIP Settings > Advanced
  - From Domain: sip.telnyx.com
- Codecs
  - Enable: ulaw, alaw, gsm, g722, g729, opus; H264 if video is needed
- Submit and Apply Config

### Credentials-based trunk (Chan_SIP)

Connectivity > Trunks > Add Trunk > Add New Chan_SIP Trunk
- Settings (General/Advanced as available)
  - Username: your Telnyx SIP credentials username
  - Secret: your Telnyx SIP credentials password
  - Authentication: Outbound; Registration: Send (where applicable)
  - SIP Server: sip.telnyx.com; Port: 5060 (5061 for TLS)
  - Context: from-pstn (if available)
  - Transport: UDP/TCP (TLS if enabled)
  - From Domain: sip.telnyx.com
- SIP Settings > Outgoing (PEER Details)
  - username=your Telnyx username
  - secret=your Telnyx password
  - type=friend
  - qualify=yes
  - insecure=port,invite
  - host=sip.telnyx.com
  - fromdomain=sip.telnyx.com
  - disallow=all
  - allow=ulaw&alaw
- SIP Settings > Incoming (USER/USER Details)
  - username=your Telnyx username
  - secret=your Telnyx password
  - fromdomain=sip.telnyx.com
  - host=sip.telnyx.com
  - type=friend
  - insecure=port,invite
  - qualify=yes
  - disallow=all
  - allow=ulaw&alaw
  - dtmfmode=rfc2833
  - Register String (format): username:password@sip.telnyx.com/username
- Submit and Apply Config

## Outbound routing (placing calls)

Connectivity > Outbound Routes > Add Outbound Route
- Route Settings
  - Route Name: e.g., Outbound_Telnyx
  - Route CID: your Telnyx number (optional)
  - Trunk Sequence: select your Telnyx trunk
- Dial Patterns
  - US/NANPA examples
    - prepend: 1; match: NXXNXXXXXX (10-digit dialing → 1+10)
    - prepend: (blank); match: 1NXXNXXXXXX (11-digit)
  - International (example patterning)
    - prepend: Country prefix; match: NXXNXXXXXX
    - prepend: (blank); match: <country prefix>NXXNXXXXXX
- Submit and Apply Config
- Note: If you see “WARNING: This trunk is not used by any routes”, finish route setup so outbound calls can use the trunk.

## Inbound routing (receiving calls)

Connectivity > Inbound Routes > Add Inbound Route
- Route name/description
- DID Number: your Telnyx DID (E.164 by default)
- Set the Destination (e.g., extension, ring group, IVR)
- Submit and Apply Config

Number format note: By default, Telnyx sends ANI/DNIS in E.164 (11 digits in US, e.g., +1NXXNXXXXXX). Ensure your FreePBX DID/matching patterns accept E.164 or adjust your Telnyx SIP Connection number format in the portal if needed (https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats).

## Codec and DTMF recommendations

- Audio: ulaw and/or alaw are safe defaults; Telnyx also supports gsm, g722, g729, opus
- Video: H264
- DTMF: rfc2833 on Chan_SIP; PJSIP handles out‑of‑band per defaults

## Version-specific notes and defaults

- FreePBX v13
  - Defaults to chan_pjsip for endpoints/trunks; both Chan_SIP and PJSIP can be enabled.
- FreePBX v14/v15
  - Use PJSIP whenever possible; Asterisk 16 underpins many v14/v15 builds.
- Ports
  - PJSIP typically on 5060 (UDP/TCP) or 5061 (TLS)
  - Chan_SIP commonly on 5160 (UDP) in FreePBX distributions

## Quick reference: Telnyx values you’ll use

- SIP domain/host: sip.telnyx.com
- From Domain: sip.telnyx.com
- SIP ports: 5060 (UDP/TCP), 5061 (TLS)
- Registration
  - IP-based: None (PJSIP) / no register string (Chan_SIP)
  - Credentials: Registration Send (PJSIP) / Register String (Chan_SIP)
- Common flags (Chan_SIP): type=friend, insecure=port,invite, qualify=yes, disallow=all, allow=ulaw

You’re done. Place a test outbound call, then call your DID to confirm inbound routing. If calls fail, recheck Asterisk SIP Settings (external/local networks), trunk registration (for credentials), and that your outbound route points to the Telnyx trunk.
