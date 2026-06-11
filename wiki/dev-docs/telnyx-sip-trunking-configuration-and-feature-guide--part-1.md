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

*Part 1 of 2 — see also: [Part 2](telnyx-sip-trunking-configuration-and-feature-guide--part-2.md)*

A consolidated guide to configuring Telnyx Elastic SIP Trunking, covering caller ID validation, outbound voice profiles, concurrency limits, network traversal, audio quality features, external transfers, SIP URI calling, Dynamic E911, and a LiveKit integration highlight—with links to vendor-specific configuration guides.

## Using these guides and supported systems
Telnyx configuration guides help you connect IP-PBXs, SBCs, ATAs, softphones, and cloud platforms to Elastic SIP Trunking. Because PBX/SBC firmware and options vary widely, treat guides as reference, not exact templates. Telnyx can’t directly support third‑party products—contact their vendors for device-specific help. See the full vendor list (3CX, Asterisk/FreePBX, Cisco/CUBE, Grandstream, Microsoft Teams/Direct Routing, Ribbon, Oracle, Sansay, Wildix, Yeastar, etc.) and links to step‑by‑step articles here: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides

## Caller ID policy and validation
Telnyx enforces strict caller ID validation and rejects invalid CLIs with 403 Caller Origination Number is Invalid D35.
- Localization rules
  - USA: accepts 10‑digit national (e.g., 3129457420), 11‑digit (13129457420), or E.164 (+13129457420)
  - International: accepts national formats per country and E.164 (e.g., +3531xxxxxxx for IE)
  - Cross‑border: only E.164 is accepted when calling outside the connection’s localization country
  - If no localization is set, USA rules apply; failed validation may return 404 Invalid Destination
- Header precedence for caller ID (highest first): P-Preferred-Identity, P-Asserted-Identity, Remote-Party-Id, From
- Anonymization: include Privacy: id; a valid origination number is still required; emergency and toll‑free calls cannot be anonymized and will present the real CLI
- International spoofing: outbound international calls with spoofed CLIs are rejected with 503 (use client-side fallback routing)
- Caller ID Override: when enabled on a connection, outbound calls can bypass standard format validation
- Configure localization: set the outbound.localization property on your SIP connection via the API (PATCH the relevant credential/FQDN/IP connection)

## Outbound Voice Profiles (routing, limits, billing controls)
Outbound voice profiles define allowed destinations, routing, and safeguards for outbound calls. Each profile has a unique Profile ID for API/CDR reporting.
- Key components: Profile ID, tags, associated SIP connections, service plan (destinations/rate deck), per‑profile channel limit
- Destinations: enable by region or country (up to 255 destinations across 10 regions); many require Level 2 verification
- Channel limits: per‑profile concurrent call cap to protect capacity
- Billing controls
  - Rate deck: rating by destination prefix; download current rates or work with Telnyx for custom pricing
  - Max destination rate: reject calls above a per‑minute threshold you set
  - Daily spend limit: cap daily spend per connection (resets 00:00:00 UTC)
- Call recording: enable per profile (format WAV/MP3; mono/stereo; global or ANI‑scoped)

## Concurrent call limits (account‑wide)
A global concurrent outbound call cap applies across all profiles.
- Defaults: new accounts start at 2; Level 2 verification increases to 10; higher limits available on request
- Over‑limit signaling: 403 User channel limit exceeded D1
- Handling and monitoring
  - Implement exponential backoff/retries on 403 limit errors
  - Monitor active concurrency via GET /v2/calls (filter status=active)
  - Track lifecycle with webhooks (increment on call.initiated, decrement on call.hangup)
  - Best practices: alert at ~80% of limit; queue when near limit; test error paths
- Request increases: email support@telnyx.com with current needs, growth, and use case (required >100 channels)

## P‑Charge‑Info header (billing DID identification)
Identify the billing/attribution DID per call using P‑Charge‑Info.
- Format: P-Charge-Info: <sip:+15551234567@sip.telnyx.com>
- Requirements: DID must be E.164 and belong to your Telnyx connection
- Uses: multi‑DID attribution, per‑number CDRs/usage, carrier‑side routing
- Troubleshooting: ensure the DID is assigned to the connection and your PBX persists header changes across updates
- Alternatives for multi‑tenant/shared credentials: tech prefix or IP authentication token

## External call transfers (A→B→C)
Move an inbound PSTN call (A→B) to an external destination (A→C) while preserving the original caller’s identity.
- Validation requirements
  - There must be an active inbound call to your Telnyx number (B)
  - Include Diversion with your Telnyx number: Diversion: <sip:+12125551234@sip.telnyx.com>
  - Missing/unauthorized Diversion or no active call match → transfer rejected
- Transfer types: blind (REFER with Refer-To), or attended (hold, dial, announce, complete REFER)
- Programmable Voice options: use the transfer command, bridge parameters, or TeXML <Dial> with callerId

## SIP URI calling (no phone number required)
Receive calls to a SIP username at username@sip.telnyx.com.
- Prerequisites: credential‑authenticated SIP connection; device registered; feature enabled per connection
- Username rules: must start with a non‑numeric character
- Access control modes: disabled (default), unrestricted (public), internal (only from SIP connections in your account)
- Configure via API: set sip_uri_calling_preference to disabled | unrestricted | internal on the connection
- Billing: calls from unidentifiable external sources (unrestricted mode) are billed at $0.002/min to the connection owner
- Security: prefer internal for private use; monitor rates/volumes if unrestricted; ensure endpoints are registered and firewalls permit SIP

## NAT traversal with STUN/TURN
Use STUN/TURN when endpoints are behind NAT/firewalls or experiencing one‑way audio.
- Telnyx endpoints
  - STUN: stun.telnyx.com:3478 (UDP)
  - TURN: turn.telnyx.com:3478 (UDP/TCP; credentials required—request from Telnyx support)
- Alternatives: stun.l.google.com:19302 and related hosts
- Firewall allowances
  - STUN: UDP 3478 outbound
  - TURN: UDP/TCP 3478 outbound
  - RTP media: UDP 16384–32768 bidirectional
- ICE candidates: host (local), srflx (STUN), relay (TURN), prflx; ensure srflx/relay/prflx is available across NAT
- Troubleshooting: verify reachability, ports, client STUN/TURN support, and TURN credentials; on restrictive networks use TURN over TCP and consider SIP over TLS (5061)

## Audio quality features (adaptive jitter buffer and noise suppression)
- Adaptive jitter buffer (per connection; API only)
  - Enable with jitter_buffer.enable_jitter_buffer and set jitterbuffer_msec_min/max (default 60–200 ms; range 40–400; min ≤ max)
  - Tuning: higher max tolerates jitter with added latency; start with defaults and adjust based on observed conditions
- Noise suppression (connection‑ or number‑level)
  - Direction: inbound | outbound | both | disabled (each direction processed/billed independently; typical added latency <20 ms)
  - Engines: Denoiser (default), DeepFilterNet, Krisp Viva Tel Lite/Pro/SS, AI‑coustics Quail; for SIP trunking, Denoiser and Krisp Viva Tel Lite are most common
  - Connection‑level settings override number‑level settings

## Dynamic E911 (US)
Deliver location to PSAPs via pre‑provisioned addresses or real‑time GPS (PIDF‑LO).
- Methods
  - API‑based addresses: create dynamic emergency addresses/endpoints ahead of time; reference IDs in SIP (recommended to avoid activation delays)
  - GPS coordinates (PIDF‑LO): include latitude/longitude in a PIDF‑LO body; Telnyx supports LIS and ASSIST methods
- API flow (addresses/endpoints)
  - Create address → receive address id and sip_geolocation_id
  - Create endpoint → receive sip_from_id
  - Emergency INVITE must include Geolocation: {sip_geolocation_id} and From or P‑Asserted‑Identity using sip_from_id
- PIDF‑LO essentials
  - Use EPSG:4326; <gml:pos> is latitude then longitude (space‑separated); include ISO‑8601 timestamp
- Testing: dial 933 to test without dispatching
- Note: just‑in‑time provisioning may temporarily route to a national emergency call center until fully activated
