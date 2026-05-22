---
title: 'Telnyx SIP Connections: Authentication, Registration, Failover, and Advanced
  Headers'
summary: A practical guide to Telnyx SIP connection types and telephony credentials,
  how registration and authentication work, options for multi-tenant identification
  (tech prefixes, tokens, headers), failover and SRV behavior, UAC (SIP Attach) connections,
  key limitations, and troubleshooting best practices.
sources:
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
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
