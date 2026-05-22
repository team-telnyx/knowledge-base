---
title: 'Telnyx SIP Trunking: Configuration and Feature Guide'
summary: A consolidated guide to configuring Telnyx Elastic SIP Trunking, covering
  caller ID validation, outbound voice profiles, concurrency limits, network traversal,
  audio quality features, external transfers, SIP URI calling, Dynamic E911, and a
  LiveKit integration highlight—with links to vendor-specific configuration guides.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
  content_hash: 75e1f2120a0326435d4fe2c8168408451103663f7ef47300ccabe32ab0f3bd14
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
  content_hash: 11db8d311ae92c4169de23cd732bf069fe999bb17ba309fe74d8a5074106148f
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
  content_hash: 8ca80b5cfc972686988f5ff6367439f2f11cdbe27886d956ad7b2e842e41a745
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
  content_hash: 6044ad914c8bd31f108d77d84b994d826853b2ab7bf1cc063fe27af70ece2f4b
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
  content_hash: 4690dc8c8fb95a6ce3833047393557cabee30be45d802a3d38bb5004fc3d6765
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/stun-turn-servers
  content_hash: 6e45b22298b427df3beb3f26e9e351df15fed4326b46d8344f19af436d5495c9
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
  content_hash: a426210817d78e0c4eb3ed3f5e6326afba0cc42e573efb0407fd723a92fb641e
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
  content_hash: 9efccaed8690759a305438e3ea051a125d2464804ae09c93059ebf5c9a814aa4
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
  content_hash: 4daa0ab85c39b003fe9e111d2b57ed184efe348914babfacdff3fb36806b14fe
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
  content_hash: fbad3f92165614bcf8f2d814faad0adca7b8aea3d93fcff86e488d50accbb96b
- url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
  content_hash: b0ce8bb0b59639b316d8c4a9a507c6c315b249ac1f2803a26b17bb9ab13bba96
- url: https://developers.telnyx.com/docs/voice/sip-trunking/livekit-configuration-guide
  content_hash: 2ef2860c32eb957c0e29ac858c1acc5a1ff2554271c29fa00f9fc2fc7c80b0ce
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
