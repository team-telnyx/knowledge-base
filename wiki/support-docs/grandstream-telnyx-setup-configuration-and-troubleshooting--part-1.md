---
title: 'Grandstream + Telnyx: Setup, Configuration, and Troubleshooting'
summary: A consolidated guide to connect Grandstream phones, DECT systems, ATAs, UCM
  PBXs, and Wave Lite apps to Telnyx, with reusable settings, model-specific quick-starts,
  PBX routing, caller ID options, security, and troubleshooting tips.
sources:
- url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
  content_hash: dc376fbcbc86c87ffb1875c8d7d7ec4e85badbc920b1068234c1c17f29fd1af3
- url: https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup
  content_hash: d50376c2601304a91b94a7bbf79e90af7922ac34454460a0cf17162f2a8d52b7
- url: https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup
  content_hash: 95bf6dde541b4928a10520d21beedfc872f73fb0e2af85ad56e1ea8e506f59c7
- url: https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup
  content_hash: d2a1c8fd254b907b952bd320845ccee9babecdb94b45d30f00e7e5b5e1b110cd
- url: https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks
  content_hash: 2f739432e590d922818040ae4b40facf0133984560f8d1b835f72af0dde02039
- url: https://support.telnyx.com/en/articles/5808368-grandstream-dp752
  content_hash: 10e7008dd3bcc84f451255938ba6db8354077657b0981c06804fba0848b66ba8
- url: https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup
  content_hash: 75e33bf47137acad5e350ff43e05ff7bda5171a46c02a076cea3f3d47f00b46f
- url: https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx
  content_hash: 24f502376caf0af624316db7a8ea7718692d4c8d767f8f23eaca8835f7b5d892
- url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
  content_hash: ee2ab10a3b5059edd8c19cb6ca4c4e81c8cb94a40cf9a220b9a0ca41028ccb2f
- url: https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk
  content_hash: 537b4cde09dc2496dc373f178c2538a641227ed630475de38d41cde54a745be8
- url: https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk
  content_hash: 86abea91de77be48b943eb0a05856f490ef21cef43bab421d52e3762b75f1ec8
- url: https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone
  content_hash: b2d9544af0705d2d549817ce9d12a8dec0791bd7258031c22bd48dcb77840a8f
- url: https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android
  content_hash: 88be92a18cbe0dc5faf3a58e54f8b433a831fb8c978245f21c2202aa3a6a3222
- url: https://support.telnyx.com/en/articles/6187273-grandstream-gds3710-wave-lite-android
  content_hash: 44e55697e1cdda5d891beafbec4d6a1af4f0044f2ddb1d4099962646fadd3780
- url: https://support.telnyx.com/en/articles/6187411-grandstream-gds3710-wave-lite-ios
  content_hash: 312f510512d023a295cce20fefba527cba1088ae223056a85539ec1318fd7d70
updated_at: 2026-05-20T15:06:31Z
---

# Grandstream + Telnyx: Setup, Configuration, and Troubleshooting

*Part 1 of 2 — see also: [Part 2](grandstream-telnyx-setup-configuration-and-troubleshooting--part-2.md)*

A consolidated guide to connect Grandstream phones, DECT systems, ATAs, UCM PBXs, and Wave Lite apps to Telnyx, with reusable settings, model-specific quick-starts, PBX routing, caller ID options, security, and troubleshooting tips.

## Before you begin
- Create and configure in the Telnyx Mission Control Portal:
  - A Connection (Credentials or IP authentication, as required)
  - Buy and assign numbers (DIDs) to the Connection
  - Create an Outbound Voice Profile and associate it
- Update device firmware to the latest available from Grandstream.
- Recommended: enable TLS/SRTP in your Telnyx connection if you need encryption (see Telnyx encryption guide).
- Have each device’s IP address and admin credentials ready (many Grandstream devices default to admin/admin or have a unique password printed on the device label; change defaults on first login).

## Core Telnyx parameters you’ll reuse
- SIP Server (US): sip.telnyx.com (append :5061 when using TLS)
- Outbound Proxy: sip.telnyx.com (optional but recommended on some models)
- Secondary/Failover SIP Server: you may use sip.telnyx.com again or a Telnyx IP where supported (e.g., 64.16.250.10 on GRP/GXP series, 192.76.120.10 is also noted in some guides). DNS SRV is supported; A Record works broadly.
- SIP User ID / Authentication ID: your Telnyx SIP username (for credentials connections)
- Authentication Password: your Telnyx SIP password (for credentials connections)
- Transport and ports:
  - UDP/TCP: 5060
  - TLS: 5061 (enable SRTP "Enabled and forced" where available)
- Registration and keepalive:
  - SIP Registration: Yes; Register Expiration: 5 minutes; Enable OPTIONS/Heartbeat Keep Alive: Yes (e.g., 60s on UCM)
  - NAT Traversal/Keep-Alive: Enable (or STUN if needed: stun.telnyx.com:3478)
- Codecs supported by Telnyx: G.711u (PCMU), G.711a (PCMA), G.722, G.729; Video (where applicable): H.264
- DTMF: RFC2833 (Out-of-band). Some models allow In-audio + RFC2833.
- Voicemail access code (examples in guides): *97

## IP phones: GXP16xx, GXP21xx, GXP1700, GRP260x/GRP261x quick setup
1) Get device IP and log in
- From the handset menu, find IPv4 Address; browse to http://<device-ip> and log in (default often admin/admin; some units use a random printed password).

2) Create/Register the account (Accounts > Account X > General/Account Register)
- Account Active: Yes
- Account/Display Name: your label
- SIP Server: sip.telnyx.com
- Secondary SIP Server (if present): 64.16.250.10 (US) or leave blank/use DNS SRV
- Outbound Proxy: sip.telnyx.com (if present)
- SIP User ID: your Telnyx SIP username
- Authentication ID: your Telnyx SIP username (same as above)
- Authentication Password: your Telnyx SIP password
- Name/Display Name (Caller ID Name):
  - Use CAPITAL LETTERS; avoid special characters; spaces allowed; keep ≤15 chars for best display in Canada
- Optional per-model: Fallback Expiration (failback timer)

3) SIP basics (Accounts > Account X > SIP Settings > Basic)
- SIP Registration: Yes; Register Expiration: 5
- Enable OPTIONS Keep Alive/Heartbeat: Yes (where available)
- Local SIP Port: 5060 (UDP/TCP) or 5061 (TLS)
- SIP Transport: UDP or TCP; choose TLS/TCP when you’ve enabled TLS in Telnyx
- DNS Mode: A Record (SRV/NAPTR also supported on GRP/GXP if you prefer)

4) Audio/Codecs (Accounts > Account X > Audio Settings)
- Preferred Vocoder: select from PCMU, PCMA, G722, G729 (remove unsupported)
- DTMF: RFC2833 (default)

5) Save/Apply and verify registration (Status page should show Registered)

Note—Grandstream headers (for “No response” on outgoing):
- Disable in Accounts > Account X > SIP > Custom SIP Header:
  - Use X-Grandstream-PBX Header
  - Use P-Access-Network-Info Header
  - Use P-Emergency-Info Header

## DECT systems: DP752/DP750 quick setup
1) Find base IP (handset: Menu > Status > Base Status) and log in to the base web UI.
2) Profiles > Profile 1 > General Settings
- Profile Active: Yes; Name: label
- SIP Server: sip.telnyx.com
- Failover SIP Server: sip.telnyx.com; Prefer Primary: Yes
- Outbound Proxy: sip.telnyx.com
- Voice Mail Access Number: *97
3) SIP Settings > Basic Settings
- SIP Transport: UDP (or TLS if encrypting)
- Local SIP Port: 5060 (UDP) or 5061 (TLS)
4) Profiles > Profile 1 (Audio/DTMF/SRTP)
- Send DTMF: In-Audio and via RTP
- SRTP Mode: Enabled and Forced (when using TLS)
5) DECT > SIP Account Settings (for each account)
- SIP User ID / Authenticate ID / Password: Telnyx credentials
- Name (Caller ID Name): see formatting rules above
- Profile: Profile 1; HS Mode: choose your ring strategy; Active: Yes
6) DECT > Handset Line Settings: assign the SIP account to Line 1 for desired handsets. Save/Apply.

## Analog adapter (ATA): HT802 for fax quick setup
1) Access the HT802 web UI (dial *** then 02 to hear IP; browse and log in).
2) FXS PORT1 key fields
- Primary SIP Server: sip.telnyx.com; Outbound Proxy: blank (or sip.telnyx.com on older fw)
- NAT Traversal: Keep-Alive; DNS Mode: A Record
- SIP User ID / Authenticate ID: Telnyx SIP username; Authenticate Password: Telnyx SIP password
- SIP Registration: Yes; Unregister on Reboot: No; Outgoing Call Without Registration: Yes
- Register Expiration: 5; Allow Incoming SIP Messages from SIP Proxy Only: Yes
- Preferred DTMF: In-audio, RFC2833
- Disable: Use P-Access-Network-Info Header; Use P‑Emergency‑Info Header
- Preferred Vocoder: PCMU, PCMA, G72x
- Fax Mode: T.38; Re-INVITE After Fax Tone: Disabled
- Optional (fax reliability): Jitter Buffer Type: Fixed; Length: High; Disable Echo Canceller/Suppressor: Yes
3) To block direct IP calls: enable Check SIP User ID for Incoming INVITE = Yes, and Allow Incoming SIP Messages from SIP Proxy Only = Yes.
4) Telnyx inbound mapping for HT802: set your Telnyx Connection inbound Number Format (DNIS) to SIP Username (Telnyx does not support using phone numbers as SIP usernames).

## Grandstream UCM PBXs (UCM62xx/UCM6xxx) using credentials registration
1) Log in to the UCM web UI (default https://<ip>:8089; admin/admin first login).
2) Create a VoIP trunk (Extension/Trunk > VoIP Trunks > Add SIP Trunk)
- Type: Register SIP Trunk; Provider Name: Telnyx
- Host/Select host: sip.telnyx.com (append :5061 if TLS)
- Username/Authenticate ID: Telnyx SIP username; Password: Telnyx SIP password
- From Domain: sip.telnyx.com; Transport: UDP/TCP or TLS if encrypting
- Keep Trunk CID: enable if trunk should send its own CID
3) Advanced SIP (on the trunk)
- Codec Preference: PCMU, PCMA, G722, G729
- Caller ID headers: choose ONE of Send PPI Header or Send PAI Header (not both). Optionally enable Passthrough PAI Header when Send PAI is disabled.
- DTMF Mode: RFC2833 (Default)
- Enable Heartbeat Detection: Yes; Frequency: 60s
- SRTP: Enabled and forced (when using TLS)
4) Inbound Routes (Extension/Trunk > Inbound Routes > Add)
- Trunks: select your Telnyx trunk
- Patterns: _<your DID exactly as in Telnyx Portal>
- Default Destination: choose Extension/IVR/etc.
5) Outbound Routes (Extension/Trunk > Outbound Routes > Add)
- Calling Rule Name; Pattern(s) for dialing (e.g., _NXXXXXXXXX, include prefixes as needed)
- Trunk: select Telnyx trunk; Privilege Level: match your policy
- If using a dial-out prefix, set Strip to remove it
6) Verify registration (System Status > Dashboard). If Rejected, check reachability and credentials.

## Grandstream UCM PBXs using IP authentication
- Create a Telnyx IP-auth Connection and allow your UCM’s public IP.
- On UCM, create a VoIP Trunk (peer/IP-based) pointing to Telnyx:
  - Provider/Host: you may use a Telnyx IP (e.g., 192.76.120.10) or sip.telnyx.com depending on your policy
- Build Inbound/Outbound Routes as in the credentials section above.

## Caller ID options on UCM
- Global (PBX Settings > General Settings): set a system-wide outbound CID
- Per Extension (Extension/Trunk > Extensions > CallerID Number)
- Per Outbound Route (Extension/Trunk > Outbound Routes > Outbound Route CID)
- Caller ID Name rules: CAPITAL LETTERS, no special chars, spaces allowed, ≤15 chars for Canadian providers
- Review Telnyx Caller ID number policy as applicable.
