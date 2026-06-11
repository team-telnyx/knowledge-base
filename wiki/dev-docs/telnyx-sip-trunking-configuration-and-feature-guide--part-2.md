---
title: 'Telnyx SIP Trunking: Configuration and Feature Guide'
summary: A consolidated guide to configuring Telnyx Elastic SIP Trunking, covering
  caller ID validation, outbound voice profiles, concurrency limits, network traversal,
  audio quality features, external transfers, SIP URI calling, Dynamic E911, and a
  LiveKit integration highlight—with links to vendor-specific configuration guides.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/stun-turn-servers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
- url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/livekit-configuration-guide
updated_at: 2026-05-20T09:45:51Z
---

# Telnyx SIP Trunking: Configuration and Feature Guide

*Part 2 of 2 — see also: [Part 1](telnyx-sip-trunking-configuration-and-feature-guide--part-1.md)*

A consolidated guide to configuring Telnyx Elastic SIP Trunking, covering caller ID validation, outbound voice profiles, concurrency limits, network traversal, audio quality features, external transfers, SIP URI calling, Dynamic E911, and a LiveKit integration highlight—with links to vendor-specific configuration guides.

## Integration spotlight: LiveKit
A practical example using an FQDN SIP connection to LiveKit for real‑time audio/video apps.
- Telnyx setup
  - Create an FQDN SIP connection and configure Outbound Calls Authentication with credentials
  - Associate an Outbound Voice Profile (create if needed) and assign numbers to the connection
  - Optionally create a Programmable Voice application (webhooks, inbound subdomain) and use its subdomain as a target for certain LiveKit trunks
- LiveKit setup (CLI‑driven)
  - Create inbound/outbound trunks and dispatch rules in LiveKit; set address to sip.telnyx.com (or your Voice App subdomain)
  - Authenticate outbound calls with your Telnyx SIP username/password
  - Important: ensure the first INVITE includes a custom header carrying your Telnyx SIP username (e.g., X‑Telnyx‑Username). Map this header to LiveKit’s authUsername so Telnyx challenges with 407 and authenticates the call against your FQDN connection rather than matching on shared IPs
- Testing and debugging
  - Use LiveKit CLI to originate a test call; in Telnyx Mission Control, use Reporting → Debugging → SIP Call Flow Tool for SIP traces, QoS, and PCAP export

## Troubleshooting quick reference
- 403 D35 (invalid caller ID): send E.164 or match localization; verify header precedence isn’t overriding your intended CLI
- 404 Invalid Destination: called number invalid (often non‑E.164 for cross‑border); set connection localization or normalize numbers
- 503 (international spoofing): use a valid CLI for the destination country
- 403 D1 (concurrency): account hit global concurrent limit; implement backoff/queueing and monitor active calls
- External transfers rejected: confirm active inbound call to your Telnyx number and include a valid Diversion header
- One‑way/no audio: verify STUN/TURN reachability and RTP ports; use TURN over TCP on restrictive networks
- SIP URI calling fails: ensure feature enabled, username starts with a non‑numeric character, access mode permits the caller, and the endpoint is registered

## Related resources
- Full SIP Trunking configuration guide index (including device‑specific how‑tos): https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides
- Telnyx STUN/TURN reference: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/stun-turn-servers
- Dynamic E911: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911
- SIP URI calling: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
- Noise suppression: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression
- Adaptive jitter buffer: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
- External transfers: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
- Caller ID policy: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy
- Outbound Voice Profiles: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
- Concurrent call limits: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
- P‑Charge‑Info: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
- LiveKit + Telnyx guide: https://developers.telnyx.com/docs/voice/sip-trunking/livekit-configuration-guide
