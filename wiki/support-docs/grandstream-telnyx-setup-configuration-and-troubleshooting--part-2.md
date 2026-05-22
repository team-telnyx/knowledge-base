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

*Part 2 of 2 — see also: [Part 1](grandstream-telnyx-setup-configuration-and-troubleshooting--part-1.md)*

A consolidated guide to connect Grandstream phones, DECT systems, ATAs, UCM PBXs, and Wave Lite apps to Telnyx, with reusable settings, model-specific quick-starts, PBX routing, caller ID options, security, and troubleshooting tips.

## Optional routing and resilience on UCM
- Time Conditions (Inbound/Outbound Routes): apply schedules to routes
- Trunk Groups (fw ≥1.0.20.17): group multiple accounts on the same SIP server for cleaner management
- Failover Trunks (Outbound Routes): add failover; UCM fails over when no response in ~32s, or on 403/407/408/503/603, or primary disabled/busy (analog)

## Wave Lite softphone (iOS and Android) with Telnyx
1) Install Wave Lite from the app store and open Settings > Account Settings > Generic Account > SIP Account (do not use the VoIP Provider list).
2) Account basics
- Activate Account: On
- Account Name: label
- SIP Server: sip.telnyx.com
- SIP User ID / SIP Authentication ID: Telnyx SIP username
- SIP Password: Telnyx SIP password
- VoiceMail UserID: *97 (example)
- Display Name (Caller ID Name): follow formatting rules above
3) Call/Network settings
- SIP Port: 5060 (UDP/TCP) or 5061 (TLS)
- Transmission Protocol: UDP/TCP or TLS when encrypting
- Preferred Vocoder (Wi‑Fi/Cellular): PCMU, PCMA, G722, G729; Video: H.264 (if used)
- Optional STUN: stun.telnyx.com:3478 (Advanced > General Settings)

## GDS3710 video door system with Wave Lite
1) On GDS3710 (web GUI > SIP Settings > SIP Basic Settings)
- Account Name: label (e.g., Doorbell)
- SIP Server: sip.telnyx.com
- SIP User ID / Authenticate ID: Telnyx SIP username
- Authenticate Password: Telnyx SIP password
2) Configure Wave Lite on iOS/Android as above and answer calls from the door system on your device.

## Troubleshooting tips
- Outgoing calls show “No response” (phones register and receive calls):
  - On the phone: disable Accounts > Account X > SIP > Custom SIP Header entries:
    - Use X‑Grandstream‑PBX Header; Use P‑Access‑Network‑Info Header; Use P‑Emergency‑Info Header
  - Prefer G729 (or G722) as first vocoder with PCMU/PCMA as fallbacks (per Grandstream guides)
- UCM trunk status Rejected: verify DNS/route to sip.telnyx.com, credentials, and transport/port (TLS uses :5061)
- One-way audio/NAT: enable OPTIONS/Heartbeat keepalive; use STUN (stun.telnyx.com:3478) or proper port forwarding; prefer RFC2833 DTMF
- Direct IP calls reaching ATA: on HT802 enable Check SIP User ID for Incoming INVITE = Yes and Allow Incoming SIP Messages from SIP Proxy Only = Yes
- HT802 inbound mapping: ensure Telnyx Connection inbound DNIS is set to SIP Username (not a phone number)

## Security and encryption essentials
- If encrypting, set Transport = TLS and append :5061 to the SIP server where required; set SRTP = Enabled and forced
- Limit inbound traffic to SIP proxy only (where available) and disable direct IP calling
- Change default admin passwords and keep firmware updated

## Finding device IPs and default credentials (quick reference)
- GXP/GRP/GXP21xx/GXP1700: Menu > Status > Network Status > IPv4 Address; default admin/admin (or device label password)
- DP752/DP750: Handset Menu > Status > Base Status; default admin/admin
- HT802: dial *** then 02 to hear IP; default admin/admin
- UCM62xx/6xxx: device shows IP on screen; browse https://<ip>:8089; default admin/admin on first login (prompted to change)

That’s it—use the core parameters, then follow the model‑specific steps above to register, route, and place encrypted, high‑quality calls with Telnyx.
