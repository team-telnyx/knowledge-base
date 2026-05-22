---
title: 'Telnyx WebRTC Voice SDKs: Fundamentals, Architecture, and Authentication'
summary: An end-to-end guide to Telnyx WebRTC Voice SDKs—what they are, how they work
  with Telnyx’s SIP and Voice APIs, available SDKs, core concepts, authentication
  options (Credential Connections, Telephony Credentials, JWTs), dialing behavior,
  common usage patterns, costs, and limits.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals/index
- url: https://developers.telnyx.com/docs/voice/webrtc/architecture
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
updated_at: 2026-05-20T10:23:34Z
---

# Telnyx WebRTC Voice SDKs: Fundamentals, Architecture, and Authentication

An end-to-end guide to Telnyx WebRTC Voice SDKs—what they are, how they work with Telnyx’s SIP and Voice APIs, available SDKs, core concepts, authentication options (Credential Connections, Telephony Credentials, JWTs), dialing behavior, common usage patterns, costs, and limits.

## Overview
Telnyx WebRTC Voice SDKs let your web and mobile apps instantiate and control a Telnyx call leg client-side, bypassing traditional SIP softphones. They provide native calling UX, device/media control, and end-to-end visibility while leveraging Telnyx’s global PSTN coverage and Voice APIs.

## How the SDKs work
- Media transport: WebRTC RTP over DTLS (SRTP / DTLS-SRTP)
- Signaling: JSON-RPC over secure WebSocket (WSS)
- Gateway: rtc.telnyx.com translates WebRTC on the SDK side to SIP on the Telnyx core, acting as a SIP UA to the Telnyx platform

## Where the WebRTC Voice SDKs fit (Architecture)
- SDKs alone cannot place calls to PSTN by themselves—they only instantiate a WebRTC call leg that enters Telnyx via rtc.telnyx.com
- All SDK client authentication is rooted in a SIP Connection on your Telnyx account
- Calls initiated via SDK legs inherit Telnyx’s global PSTN coverage and fall under the Programmable Voice APIs (Call Control, TeXML, Conferencing)
- SDKs provide local controls (answer/hang up, hold/mute, DTMF) but do not orchestrate server-side call flows—use Call Control API or TeXML for logic like IVR, prompts, bridging, queues, and conferences

Example orchestration path: For a prepaid flow, park the SDK leg on connect, handle Telnyx webhooks in your backend, play TTS about balance, originate a PSTN leg, then bridge—or hang up gracefully if funds are insufficient.

## SDK availability
- JavaScript SDK: https://github.com/team-telnyx/webrtc
- iOS SDK: https://github.com/team-telnyx/telnyx-webrtc-ios
- Android SDK: https://github.com/team-telnyx/telnyx-webrtc-android
- Flutter SDK: https://github.com/team-telnyx/flutter-voice-sdk

## Core SDK concepts and lifecycle
- Client class: Represents the session (WebSocket signaling + active call management); provides device selection, event subscription, and outbound call initiation
- Call class: Represents a WebRTC media connection; actions include answer, hang up, send DTMF
- Events: 
  - WebSocket state (connected/disconnected)
  - Client readiness (ready to make/receive calls)
  - Call lifecycle (e.g., ringing, answered)
- Call states: Common lifecycle across SDKs; platform additions exist (iOS/Android add RECONNECTING and DROPPED; Flutter/Android add ERROR)

## Authentication options and setup
A Client must be authenticated before placing or receiving calls. You can choose one method; avoid mixing unless required.

1) Credential-based SIP Connection (basic credentials)
- Create: POST /v2/credential_connections with fields like active, user_name, password, anchorsite_override (e.g., "Latency"), connection_name
- SDK login: user_name + password
- Pattern 1 (client-initiated, parked leg) connection settings (PATCH /v2/credential_connections/:id):
  - webhook_event_url and webhook_event_failover_url
  - webhook_api_version = 2, webhook_timeout_secs
  - outbound.call_parking_enabled = true
  - outbound.outbound_voice_profile_id = your profile ID
- Pattern 2 (inbound-first) connection setting (PATCH):
  - sip_uri_calling_preference = internal

2) Telephony Credentials (scoped SIP usernames)
- Prerequisite: An active credential-based SIP connection
- Create: POST /v2/telephony_credentials with connection_id (required), plus optional expires_at (recommended), name, tag
- Update: PATCH /v2/telephony_credentials/:id (cannot update after status becomes expired; expired can only be deleted)
- Revoke: DELETE /v2/telephony_credentials/:id to immediately remove client capability
- Manage at scale: 
  - filter[resource_id]=connection:<connection_id>
  - filter[status]=expired
  - filter[tag]=your-tag
- SDK login: sip_username (prefixed gencred...) + sip_password

3) JWTs (tokenize a telephony credential)
- Prerequisite: An active telephony credential
- Create token: POST /v2/telephony_credentials/:id/token
- Token validity: Until 24 hours after creation or until the parent telephony credential expires—whichever comes first
- SDK login: JWT as the credential

Limits
- Account-wide resource cap: The sum of Credential Connections, IP Connections, FQDN Connections, External Connections, TeXML Applications, and Call Control Applications may not exceed 10,000
- Telephony credentials: No per-connection or per-account count limits
- JWTs: No per-credential or per-account count limits

## Dialing registered clients
Use the registered SIP URI of the target client:
- Credential SIP Connection login: john1234@sip.telnyx.com
- Credential SIP Connection (phone number as destination): +1XXXXXXXXXX (requires the connection’s Inbound "Destination Number Format" set to "SIP Username")
- Telephony credential login: gencredXYZ@sip.telnyx.com
- JWT login: Use the SIP username of the parent telephony credential (gencredXYZ@sip.telnyx.com)

## Multi‑client registration behavior
- Prefer a single authentication method to avoid ambiguity
- Registrations are last-wins per SIP username. If multiple clients register the same SIP username (e.g., one via telephony credential and another via its JWT), the most recent registration will receive the call for that SIP URI

## Primitive usage patterns
Pattern 1 (client-initiated)
- App initiates a call; Telnyx parks the leg
- Telnyx sends webhooks to your backend
- Backend uses Call Control API, TeXML, or Conferencing to play prompts, enqueue, or create/bridge a second leg

Pattern 2 (inbound-first)
- External call (e.g., PSTN) arrives at Telnyx
- Telnyx processes via TeXML/Voice API; place caller in queue/conference
- Backend then dials a client app leg; bridge or join both legs

## Costs and account limits
- WebRTC legs: $0.002 per minute
- Other legs/features: Billed per your Telnyx price plan and independent of WebRTC leg cost
- Account resource cap: See Limits above for the 10,000 total cap across specified resource types
