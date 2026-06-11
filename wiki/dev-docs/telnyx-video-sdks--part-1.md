---
title: Telnyx Video SDKs
summary: Telnyx Video Rooms provide a real-time audio, video, and screen-share platform
  accessible via JavaScript, Android, and iOS client SDKs. This page covers the core
  concepts, prerequisites, and SDK-specific usage for building video applications
  with Telnyx.
sources:
- url: https://developers.telnyx.com/docs/video/android-client-sdk
  content_hash: 7230b41146e3a6bdc50ae5c6906c158e5938177ce4916adf38f5246f0379789f
- url: https://developers.telnyx.com/docs/video/get-started/index
  content_hash: 4a8b12fd54cb2addeb6012b4c1270463b99c3588387686a479c204346139f963
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
  content_hash: aa7c3284af98900dfd128454c2f648435c50ce615b47b6596ce922fea3b2c74b
- url: https://developers.telnyx.com/docs/video/javascript-sdk/index
  content_hash: 2795b93096ae650de721364e955a12d28e8e7c18ee96e785b80795ffd89523f1
- url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial
  content_hash: 0bfd39b1a48ae6f3a85d0a8adb4744c20f4e74ab48b38b1624ee3e63edfd5ae8
- url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events
  content_hash: a433db2aded6a73e8472b085ebe3c98eac836ab39b4e7ec548b6d6813304d24e
- url: https://developers.telnyx.com/docs/voice/outbound-voice-profiles
  content_hash: 990ff92ea817f97ee8ee20fe8e3e95aa4a967e6d550f12368d8d3b1aa57b1cdc
- url: https://developers.telnyx.com/docs/voice/overview/index
  content_hash: 021018458a01a48106693b027d7ca00d5e0560ff763aa5557e854994cff10ec9
updated_at: 2026-06-11T10:40:58Z
---

# Telnyx Video SDKs

*Part 1 of 4 — see also: [Part 2](telnyx-video-sdks--part-2.md), [Part 3](telnyx-video-sdks--part-3.md), [Part 4](telnyx-video-sdks--part-4.md)*

Telnyx Video Rooms provide a real-time audio, video, and screen-share platform accessible via JavaScript, Android, and iOS client SDKs. This page covers the core concepts, prerequisites, and SDK-specific usage for building video applications with Telnyx.

## Concepts and Architecture

A video application built with Telnyx Video Rooms has two parts:

- **Client** — The JavaScript, iOS, or Android SDK used to interact with a Room instance.
- **Server** — The REST APIs and Mission Control Portal used to create/manage rooms and sessions, configure recording, and moderate participants.

### Core Terms

| Term | Description |
|------|------------|
| **Room** | A virtual place where multiple endpoints connect using a Telnyx Video SDK. Represents a real-time audio/video/screen-share session. |
| **Room Session** | A moment when multiple Room Participants were communicating within a given Room. |
| **Participant** | An endpoint using a Video SDK to connect to a Room. Each Room has one Local Participant and one or more Remote Participants. |
| **Stream** | Audio/video media streams shared by Participants. Identified by `participantId` and `streamKey`. A Participant can have multiple Streams. |
| **Subscription** | Used to subscribe to a Stream belonging to a Remote Participant. Subscriptions are opt-in — the Room does not automatically subscribe to remote streams. |
| **Client Join Token** | A short-lived JWT containing grants to join a Room. Can be refreshed using a Refresh Token. |
| **API Key** | Secret key generated via the Mission Control Portal, used to authenticate Telnyx REST API calls. |

### Room State

Room State tracks the state of the Room as it changes (e.g., a local participant starts publishing, a remote participant leaves). The state includes the room status, participants, streams, publishers, and subscriptions.

Room statuses follow this lifecycle:

- `initialized` — Room instance created
- `connecting` — Connection in progress
- `connected` — Successfully connected
- `disconnecting` — Disconnection in progress
- `disconnected` — Disconnected from the room

## Prerequisites

Before connecting to a room from any SDK, three things are needed:

### 1. API Key

Generate an API key from the **API Keys** section of your Mission Control Portal account. See [Create API Keys](https://developers.telnyx.com/development/api-fundamentals/create-api-keys) for instructions. The API key is used to authenticate REST API calls and manage access tokens.

### 2. Create a Room

Create a Room using the [Rooms REST API](https://developers.telnyx.com/api-reference/rooms/view-a-list-of-rooms). Example:

```bash
curl -X POST "https://api.telnyx.com/v2/rooms" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  --data-binary '{
  "unique_name": "My room",
  "max_participants": "10",
  "webhook_event_url": "https://example.com",
  "enable_recording": "false"
}'
```

The response includes an `id` field — this is your Room ID.

### 3. Generate a Client Token

A Client Join Token is required for a client to join a Room. It is short-lived and can be refreshed using the accompanying Refresh Token.

```bash
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"refresh_token_ttl_secs":3600,"token_ttl_secs":600}' \
  https://api.telnyx.com/v2/rooms/ROOM_ID/actions/generate_join_client_token
```

The response contains a `token` (the client access token) and a `refresh_token`. Client tokens must be refreshed before they expire; otherwise, the Room instance will automatically disconnect.
