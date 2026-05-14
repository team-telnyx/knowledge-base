---
title: 'FreePBX with Telnyx: Trunks, Routing, TLS and Token Auth (PJSIP/Chan_SIP)'
summary: Configure FreePBX to place and receive calls with Telnyx using PJSIP (recommended)
  or Chan_SIP, including NAT/SIP settings, trunks, dial patterns, caller ID and E.164
  tips, optional X-Telnyx-Token for IP-auth trunks, and concise quick-starts for Asterisk,
  FreeSWITCH, Cisco, Grandstream, Vicidial, and softphones.
sources:
- url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
- url: https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk
- url: https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
- url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
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
