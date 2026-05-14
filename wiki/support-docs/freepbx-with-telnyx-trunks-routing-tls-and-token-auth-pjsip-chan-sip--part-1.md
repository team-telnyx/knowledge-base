---
title: 'FreePBX with Telnyx: Trunks, Routing, TLS and Token Auth (PJSIP/Chan_SIP)'
summary: Configure FreePBX to place and receive calls with Telnyx using PJSIP (recommended)
  or Chan_SIP, including NAT/SIP settings, trunks, dial patterns, caller ID and E.164
  tips, optional X-Telnyx-Token for IP-auth trunks, and concise quick-starts for Asterisk,
  FreeSWITCH, Cisco, Grandstream, Vicidial, and softphones.
sources:
- url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
  content_hash: 566e07d3a3f39027e64b72ea20edb3304e0641acd754bfad601776635399ad91
- url: https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk
  content_hash: ec6e13c20a1e7cf21d9ae768cec03db662ebe4f1cf4a1bba6c4dbf725b556182
- url: https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials
  content_hash: 4527776f41e7bd740d8331618ccad43f1fb4ae0251a7500b047c580064867097
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
  content_hash: adf3eff58d267e80905642d3bff1d0461e5f290fceb5e1dd2d95add4b071c535
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
  content_hash: 3b7dc4d18433b1b5095cfa6dc1edfdd8968a4db6d07f485ae773b71254f50084
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
  content_hash: 73bf24ecf0b3fd30e45fdc8f944dc6e33dcd84f9b204f676d1a4549a89ece40c
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
  content_hash: acc54c5742e78fb56ceaa86e0730df7b00407e8779457f1ba9ff1ca4d910bd9b
- url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
  content_hash: 2ff5b44a2ede094400e7a67da7d90de0c9238cc71b90e9da4fadc654a641d746
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
  content_hash: ffd411a3399a6bd44c1928f1e2bf4d8fd6e5ebefbee5575b4c2a148392a54b64
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
  content_hash: 7a2d8f8580d88e7371cf59953c7aa6fad6e2e39a36dfc55f9ddb9e4a03f7a3c6
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
  content_hash: 7a4ed58a6b64a4bb92095412c281e6abc2ef3aeee89f811905ef8c982529d372
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
  content_hash: 68ec4c01bd1b146596d7a339d414e9c6fd471bf612c683474c077bd79e7c0779
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
  content_hash: 01aacb937433577173910762c57a97918b12873f1b87f02e6d792fb833642584
updated_at: 2026-05-14T11:28:58Z
---

# FreePBX with Telnyx: Trunks, Routing, TLS and Token Auth (PJSIP/Chan_SIP)

*Part 1 of 2 — see also: [Part 2](freepbx-with-telnyx-trunks-routing-tls-and-token-auth-pjsip-chan-sip--part-2.md)*

Configure FreePBX to place and receive calls with Telnyx using PJSIP (recommended) or Chan_SIP, including NAT/SIP settings, trunks, dial patterns, caller ID and E.164 tips, optional X-Telnyx-Token for IP-auth trunks, and concise quick-starts for Asterisk, FreeSWITCH, Cisco, Grandstream, Vicidial, and softphones.

## What you need before you start
- A Telnyx Mission Control account configured: create a SIP Connection (Credentials or IP Auth), assign at least one DID to it, and attach an Outbound Voice Profile. See: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- SIP server: sip.telnyx.com
- Transports/ports: UDP/TCP 5060; TLS 5061 (enable TLS if desired: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
- Codecs: ulaw (G.711u), alaw (G.711a); also g722, g729, Opus (and H264 for video where supported)
- DTMF: RFC2833/RFC4733
- FreePBX note: Prefer PJSIP over Chan_SIP (Chan_SIP is deprecated). Chan_SIP typically listens on 5160.

## FreePBX core setup (v13–v15)
1) Settings > Asterisk SIP Settings
- Populate External Address and Local Networks (under General SIP and, if present, Chan_SIP Settings).
- Submit and Apply Config.

2) (Optional) Extensions
- Applications > Extensions. Create PJSIP extensions when possible. If using Chan_SIP, note it defaults to UDP 5160.

## Telnyx trunk — Credentials, PJSIP (recommended)
Connectivity > Trunks > Add Trunk > Add SIP (chan_pjsip)
- General
  - Trunk Name: e.g., Telnyx_userAuth
  - Outbound CallerID: your purchased Telnyx number (E.164 recommended)
  - CID Options: Allow Any CID (or as needed)
- PJSIP Settings > General
  - Username: your Telnyx SIP credentials username
  - Secret: your Telnyx SIP credentials password
  - Authentication: Outbound
  - Registration: Send
  - SIP Server: sip.telnyx.com
  - SIP Server Port: 5060 (or 5061 for TLS)
  - Context: from-pstn
  - Transport: UDP/TCP, or TLS/TCP if using TLS
- PJSIP Settings > Advanced
  - From Domain: sip.telnyx.com
- PJSIP Settings > Codecs
  - Enable ulaw, alaw, g722, g729, Opus (H264 if doing video)
- Submit and Apply Config.

## Telnyx trunk — Credentials, Chan_SIP (if required)
Connectivity > Trunks > Add Trunk > Add New Chan_SIP Trunk
- General: Name, optional Outbound CID, Max Channels
- SIP Settings > Outgoing (PEER Details)
  - username: Telnyx SIP credentials username
  - secret: Telnyx SIP credentials password
  - type: friend
  - qualify: yes
  - insecure: port,invite
  - host: sip.telnyx.com
  - fromdomain: sip.telnyx.com
  - disallow: all
  - allow: ulaw&alaw (add others if needed)
- SIP Settings > Incoming (USER Details)
  - type: friend
  - insecure: port,invite
  - host: sip.telnyx.com
  - dtmfmode: rfc2833
  - disallow: all
  - allow: ulaw&alaw
- Registration String
  - username:password@sip.telnyx.com/username
- Submit and Apply Config.

## Telnyx trunk — IP Authentication (no registration)
Connectivity > Trunks > (Chan_SIP or PJSIP as appropriate)
- For Chan_SIP PEER/USER (or PJSIP endpoint), use:
  - type: friend
  - qualify: yes (outgoing)
  - insecure: port,invite
  - host: sip.telnyx.com
  - fromdomain: sip.telnyx.com (outgoing)
  - dtmfmode: rfc2833 (incoming)
  - disallow: all; allow: ulaw (and others as needed)
Note: Calls authenticate by source IP you’ve configured in the Portal.

## Outbound routes and dial patterns
Connectivity > Outbound Routes
- Route Name: e.g., Outbound_Telnyx; set Route CID (or rely on trunk/extension/portal override)
- Trunk Sequence: select your Telnyx trunk
- Dial Patterns (examples)
  - US 10-digit: prepend 1; match NXXNXXXXXX
  - US 11-digit: prepend blank; match 1NXXNXXXXXX
  - International (example): prepend country prefix; match NXXNXXXXXX (adjust to your plan/region)
Submit and Apply Config.

## Inbound routes and number formats
Connectivity > Inbound Routes
- Set DID Number to your E.164 (11-digit for NANPA) DID and choose a Destination (extension/IVR/etc.).
- Default Telnyx DNIS/ANI format is E.164; you can customize formats in the Portal: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats

## Caller ID: best practices and overrides
- Set Outbound CID at the trunk or per extension. If neither is set, enable a Caller ID Override on the SIP Connection in the Portal.
- Follow Telnyx caller ID policy (format/verification): https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- For non-Telnyx numbers, verify them before use: https://support.telnyx.com/en/articles/6988813-verified-numbers

## Optional: Add X-Telnyx-Token for IP-auth trunks (FreePBX)
Use a connection token to authorize private PBX calls over IP Auth by injecting a custom header.
1) Edit /etc/asterisk/extensions_custom.conf and add:
```
[macro-dialout-trunk-predial-hook]
exten => s,1,NoOp(Entering user defined context [macro-dialout-trunk-predial-hook])
same => n,GoSub(func-set-sipheader,s,1(X-Telnyx-Token,TOKENFROMPORTAL))
same => n,Verbose(2,Added X-Telnyx-Token universally)
same => n,MacroExit()
```
Replace TOKENFROMPORTAL with the token from the Telnyx Portal.
2) Reload: fwconsole reload
3) Verify on the Asterisk console (enable SIP debug) that INVITEs include: X-Telnyx-Token: TOKENFROMPORTAL
Note: If you have multiple IP trunks, scope your logic so the header only applies where intended.

## TLS, NAT and media tips
- Use TLS 5061 where supported; for softphones like Linphone, set transport TLS and enable SRTP if desired.
- Behind NAT: set External Address and Local Networks in Asterisk SIP Settings. For devices like Cisco SPA ATAs, enable STUN (stun.telnyx.com) and NAT keep-alives/mapping.
- DTMF: use RFC2833/4733.

## Troubleshooting pointers
- 403 invalid caller ID: ensure you send a valid, verified number per policy or enable a Portal caller ID override.
- Inbound DID matching: ensure FreePBX DID matches the format Telnyx delivers (default E.164). Adjust Portal number formats if needed.
- Grandstream “No response” on outbound: disable X-Grandstream-PBX/P-Access-Network-Info/P-Emergency-Info custom headers; prefer G729A/B then PCMU per device guidance.
- Chan_SIP vs PJSIP ports: Chan_SIP often listens on 5160; align endpoints accordingly.
- Asterisk debug: asterisk -rvv; for Chan_SIP: sip set debug on; for PJSIP: pjsip set logger on.
