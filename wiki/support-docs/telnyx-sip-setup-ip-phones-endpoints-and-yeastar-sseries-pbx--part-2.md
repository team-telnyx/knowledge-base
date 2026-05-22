---
title: 'Telnyx SIP setup: IP phones, endpoints, and Yeastar S‑Series PBX'
summary: A consolidated quick-start for configuring popular IP phones, specialty endpoints,
  and Yeastar S‑Series PBX with Telnyx. It highlights core Telnyx parameters (servers,
  ports, timers, codecs), caller ID rules, TLS/SRTP, and device-specific shortcuts
  for Yealink, Polycom, Cisco, AudioCodes, Algo, Alcatel, BuddyTalk, and Positron,
  plus Yeastar trunk/routing, star codes, dial plans, and troubleshooting tips.
sources:
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
  content_hash: 6bd3fdf01af5c0046a02e18c34928eb87a6f1c6fcdc673d892590473d3c714e4
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
  content_hash: 8097dcf7d76d24b4e3bf670d895e79bc0edeccbf1a3df48b37a1097face8609f
- url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
  content_hash: 4dde609c89f8f3fdf539c01bff8eb27664df5b8d4126f2a68809193d78aa221b
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
  content_hash: dfc83f4e304b931dbd33cf46203d0a52773c2131f424602ed1c72d36b6b6f086
- url: https://support.telnyx.com/en/articles/5724344-cisco-linksys-star-codes
  content_hash: 87d95bc34c050b8c414c2f78ebd45004e206a11c029b45e0c05e48a2a6cec4dd
- url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
  content_hash: c9efcba2bda6a2dd8c951e38d195432299e5b93c48012ad988a913c3aefa4ac6
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
  content_hash: 180199af0742da6a8339523d153a2e1d3671c9da1fafa474a71f2043cc250e8d
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
  content_hash: 50d113609f9c0b38057ba419e2c9268248ad9b347a77526b43d9b41cccb5c76e
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
  content_hash: 0eb872a1ec009e112693bb3bcffaee93ed382ce678d3c9e429600f86076d7857
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
  content_hash: 6ebce0de39763da5552ae522fbc45a47c3a704ab762deb790e08f14536065b9e
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
  content_hash: 264194ffab910315173f2b03e9acaeb61bb7e93f315e166d1e0b5e7dd92c6549
updated_at: 2026-05-20T15:12:59Z
---

# Telnyx SIP setup: IP phones, endpoints, and Yeastar S‑Series PBX

*Part 2 of 2 — see also: [Part 1](telnyx-sip-setup-ip-phones-endpoints-and-yeastar-sseries-pbx--part-1.md)*

A consolidated quick-start for configuring popular IP phones, specialty endpoints, and Yeastar S‑Series PBX with Telnyx. It highlights core Telnyx parameters (servers, ports, timers, codecs), caller ID rules, TLS/SRTP, and device-specific shortcuts for Yealink, Polycom, Cisco, AudioCodes, Algo, Alcatel, BuddyTalk, and Positron, plus Yeastar trunk/routing, star codes, dial plans, and troubleshooting tips.

## Cisco/Linksys star codes (popular examples)
- Call return: *69
- Redial last number: *07 (not in PAP2T)
- Blind transfer: *98
- Call forwarding: *72 (all) / *73 (cancel); *90/*91 (busy); *92/*93 (no answer)
- Call waiting: *56 (on) / *57 (off); per‑call *71 (on) / *70 (off)
- Caller ID block: *67 (block) / *68 (unblock); per‑call *81/*82
- Anonymous call block: *77 (on) / *87 (off)
- Do not disturb: *78 (on) / *79 (off)
- Speed dial program: *74
- Secure calling toggles: *16 (all secure), *17 (none), *18 (next secure), *19 (next not secure)

## Linksys ATA dial plan building blocks
- Digits: 0‑9, *, #; x matches any digit
- Ranges/lists: [2‑7*] permit only listed characters
- Wildcard repetition: . allows zero or more of the previous pattern (e.g., 01. matches 0, 01, 011…)
- Substitution: <:1555>xxxxxxx prefixes 1555 to 7‑digit dials
- Secondary dial tone: comma inserts an outside‑line tone after a trigger (e.g., 9,1x.)
- Exclusion: ! blocks a sequence (e.g., 1900xxxxxxx! blocks 1‑900)
- Timers: S0/L0 override inter‑digit timers; P# inserts a #‑second pause

## Troubleshooting checklist
- Registration rejected
  - Re‑enter Telnyx username/password (watch browser auto‑fill quirks)
  - Ensure device transport (UDP/TCP/TLS) matches your Telnyx connection setting
  - Confirm proxy/registrar is sip.telnyx.com and the correct port
- No reply from server
  - Verify Internet access/DNS, and that your firewall/NAT allows outbound SIP/RTP
  - Double‑check SIP domain spelling and port
- NAT/timeouts
  - Use 300‑second registration; enable keepalive ~50 seconds; enable NAT mapping
- TLS/SRTP failures
  - Install necessary CA/client certificates; verify TLS port 5061 and SRTP method (AES128/SDES) align on both ends
- After changes, save/apply and reboot if needed; confirm device status shows Registered before call tests

## External references
- Mission Control getting started: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- SIP signaling addresses (regional): https://sip.telnyx.com/#signaling-addresses
- Codecs overview: https://telnyx.com/resources/codecs-affect-voip-sound-quality
- Telnyx encryption overview (TLS/SRTP): https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- TLS certificate (example chain): https://crt.sh/?id=1199354
