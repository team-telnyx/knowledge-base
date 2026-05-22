---
title: 'Telnyx SIP setup: IP phones, endpoints, and Yeastar S‑Series PBX'
summary: A consolidated quick-start for configuring popular IP phones, specialty endpoints,
  and Yeastar S‑Series PBX with Telnyx. It highlights core Telnyx parameters (servers,
  ports, timers, codecs), caller ID rules, TLS/SRTP, and device-specific shortcuts
  for Yealink, Polycom, Cisco, AudioCodes, Algo, Alcatel, BuddyTalk, and Positron,
  plus Yeastar trunk/routing, star codes, dial plans, and troubleshooting tips.
sources:
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
- url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
- url: https://support.telnyx.com/en/articles/5724344-cisco-linksys-star-codes
- url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
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
