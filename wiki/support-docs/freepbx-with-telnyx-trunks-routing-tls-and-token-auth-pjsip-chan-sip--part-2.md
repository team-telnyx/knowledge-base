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

*Part 2 of 2 — see also: [Part 1](freepbx-with-telnyx-trunks-routing-tls-and-token-auth-pjsip-chan-sip--part-1.md)*

Configure FreePBX to place and receive calls with Telnyx using PJSIP (recommended) or Chan_SIP, including NAT/SIP settings, trunks, dial patterns, caller ID and E.164 tips, optional X-Telnyx-Token for IP-auth trunks, and concise quick-starts for Asterisk, FreeSWITCH, Cisco, Grandstream, Vicidial, and softphones.

## Quick-starts for other platforms
- Asterisk (PJSIP)
  - pjsip_wizard.conf (trunk): endpoint allow !all,ulaw,alaw,G729,G722; dtmf_mode rfc4733; context from-pstn; remote_hosts sip.telnyx.com:5060; sends_registrations yes; outbound_auth username/password
  - pjsip.conf (NAT): set local_net and external_* if behind NAT
  - extensions.conf:
    - from-pstn: route inbound to your endpoint (e.g., Dial(PJSIP/1001))
    - from-internal: normalize to +E164 and send via Telnyx (e.g., Dial(PJSIP/+1${EXTEN}@telnyx))

- FreeSWITCH (Credentials)
  - sip_profiles/external/telnyx.xml: realm sip.telnyx.com, username/password, register=true
  - Outbound dialplan: bridge sofia/gateway/telnyx/$1 with your caller ID set
  - Inbound: match your DID and transfer to extension/context

- Cisco CME/CUBE (Credentials or IP)
  - dial-peer voice to sip.telnyx.com; destination/incoming patterns; voice-class codec (g711ulaw/alaw,g729)
  - NAT: use voice class sip-profiles to rewrite private IPs to public if needed
  - sip-ua registration for credentials auth
  - Ensure valid caller ID or enable Portal override

- Grandstream GXP16xx (endpoint)
  - Accounts: SIP Server/Outbound Proxy sip.telnyx.com; SIP User ID/Auth ID (Telnyx credentials)
  - Network: DNS Mode A Record; NAT Traversal Keep-Alive
  - SIP Settings: Local SIP Port 5060 (or 5061 TLS); Transport UDP/TCP/TLS
  - Codecs: ulaw, alaw, g722, g729

- Grandstream UCM6202 (PBX)
  - VoIP Trunks: Type Register; Host sip.telnyx.com; username/password
  - Inbound Routes: match DID patterns to Destinations
  - Outbound Routes: number patterns, privilege level per your Outbound Profile, select trunk
  - Caller ID: set globally, per extension, or per outbound route

- Cisco SPA112/122 (ATA)
  - Portal inbound DNIS: set to SIP Username for ATAs
  - Voice > SIP: STUN enable (stun.telnyx.com), STUN test enable
  - Quick Setup/Line: Proxy sip.telnyx.com; User ID/password (Telnyx); SIP Port 5060 (or TLS 5061); Register yes
  - NAT Mapping/Keep Alive yes (if behind NAT); RTP packet size 0.02 recommended; optional TLS requires CA import per device guide

- Vicidial (Carrier)
  - Admin > Carriers: host sip.telnyx.com; type friend; disallow=all; allow=ulaw,g729; username/password; dtmfmode rfc2833; context default; set Dial Plan to send calls via SIP/telnyx
  - Configure outbound caller ID per user or campaign

- Softphones
  - Bria Solo: Domain sip.telnyx.com; User ID/password; register with domain for inbound; set outbound proxy only if instructed
  - Linphone: Username/password; Domain sip.telnyx.com (append :5061 for TLS); Transport UDP/TCP or TLS; enable SRTP if using TLS; set Display Name to your compliant caller ID

That’s it—FreePBX is ready to make and receive calls via Telnyx. Adjust dial plans, codecs, and security to suit your environment, and use the token header for added IP-auth assurance where appropriate.
