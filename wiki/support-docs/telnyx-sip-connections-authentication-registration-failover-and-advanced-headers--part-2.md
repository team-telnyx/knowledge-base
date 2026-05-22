---
title: 'Telnyx SIP Connections: Authentication, Registration, Failover, and Advanced
  Headers'
summary: A practical guide to Telnyx SIP connection types and telephony credentials,
  how registration and authentication work, options for multi-tenant identification
  (tech prefixes, tokens, headers), failover and SRV behavior, UAC (SIP Attach) connections,
  key limitations, and troubleshooting best practices.
sources:
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
  content_hash: 5394d6701465d8ca3900b3d8636dc9ced071befcef4398620b7a3f9ddeb2de83
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
  content_hash: 2afe255354eecaab1534b4ae58169d43a675675a1965c9bfe029e017bd8e0eee
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
  content_hash: c3dfd71ef927474f85106933bb60015e68eb92c77cfd3669acef3f0a707be100
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
  content_hash: 0432bb9a78778d046b967e3944518383e60d66d7c3cf21b4217daa3daecfe008
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
  content_hash: e9b125cbde126ea5caa6f0cc9b3a3c44ebdbb42db54fd50b5018d4f67abbaef1
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
  content_hash: 573cf2d780105837dc9eb2504818c1293fa0c87ed8a952aa67aa47f1822629d7
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
  content_hash: 2e64361cd74f2dccf9129a1e84a762b6a49886421607571cad194dfe32041661
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
  content_hash: 83b81a4661f76b9a5ca2ad328228fb5945ee2135926802d610e504e1d67db372
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
  content_hash: ca465c0513776f64ebc2cfe29909d73f991b52b58c660ebbf2a5378c86d018ba
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
  content_hash: a62e24305a9bbf2be8d1de1347675001f3b7095af2c1d933f5799e750744375f
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
  content_hash: 84da88f44f54426474f0019a86163d2d81fdd7adc02496b76539c4ecb8da2d48
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
  content_hash: 4c324258c169f61fa57cf923dc0fd567e4c8620f2eeeadb25c862f0b21131958
updated_at: 2026-05-20T14:36:02Z
---

# Telnyx SIP Connections: Authentication, Registration, Failover, and Advanced Headers

*Part 2 of 2 — see also: [Part 1](telnyx-sip-connections-authentication-registration-failover-and-advanced-headers--part-1.md)*

A practical guide to Telnyx SIP connection types and telephony credentials, how registration and authentication work, options for multi-tenant identification (tech prefixes, tokens, headers), failover and SRV behavior, UAC (SIP Attach) connections, key limitations, and troubleshooting best practices.

## Limitations and gotchas
- Credentials-based connection registration is single-active: only the most recent device registration receives inbound calls.
- On-Demand Credentials are for outbound and WebRTC; inbound directly to these credentials isn’t supported.
- The legacy Access Control List feature in the portal is deprecated; do not rely on it for IP allowlisting.
- The siphv.telnyx.com domain does not accept SIP REGISTER (SIP 405) for inbound.

## Troubleshooting and verification
- Asterisk/FreePBX:
  - Reload after dialplan changes: fwconsole reload.
  - Inspect SIP signaling: asterisk -rvv then enable SIP debug (for chan_sip) or PJSIP set logger on (for PJSIP).
  - Verify headers in INVITEs (X-Telnyx-Token, P-Charge-Info) and confirm they’re applied to the intended trunk(s).
- Packet tools: Use sngrep to trace REGISTER and INVITE flows and confirm 401/200 authentication handshakes.
- WebRTC quick test: https://webrtc.telnyx.com/ supports login with SIP credentials or JWT to place test calls.

## Security best practices
- Use strong, unique passwords (12–16+ chars, mixed complexity; avoid reuse and common patterns).
- Keep tokens globally unique and scoped to the intended connection; rotate if exposed.
- Prefer TLS for signaling where possible; ensure firewalls allow Telnyx signaling/media IPs as required by your topology.
- For UAC, confirm your PBX is reachable from Telnyx and restrict registration/INVITE sources to Telnyx ranges where feasible.

External references
- SIP Connection types and setup: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- Failover and retries: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- IP/FQDN failover configuration: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- Tech prefix: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- X-Telnyx-Token (IP auth): https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
- FreePBX token header example: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- P-Charge-Info example: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- SIP Registration details: https://support.telnyx.com/en/articles/4363904-sip-registration
- UAC (SIP Attach): https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- Telephony Credentials types: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
