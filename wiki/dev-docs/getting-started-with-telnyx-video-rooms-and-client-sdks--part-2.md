---
title: Getting Started with Telnyx Video Rooms and Client SDKs
summary: Build real‑time video into web, Android, and iOS apps with Telnyx Video Rooms.
  This guide explains core concepts (rooms, participants, streams, subscriptions,
  state), how to create rooms and client join tokens, and how to connect, publish,
  and subscribe using the JavaScript, Android, and iOS SDKs—plus token refresh, events,
  and useful server APIs.
sources:
- url: https://developers.telnyx.com/docs/video/get-started/index
  content_hash: c7d68c97a3e46cefdf4574028c7bd485fe115e5d875ae892cdd79e15fbb060e7
- url: https://developers.telnyx.com/docs/video/android-client-sdk
  content_hash: b878e2927d6c3bce1f7ea0ab835de60fde832eede63e0f8f38dec4d64a19fdbe
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
  content_hash: 65bdfe9ab62c8f25d745dbceca91dee5fb27086f264273857a87ff69241054b2
- url: https://developers.telnyx.com/docs/video/javascript-sdk/index
  content_hash: 9eb0ba633a39e7750af7e5e6a1623da13e57cf109122e2e0566b9ba234b2d898
- url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial
  content_hash: dc31fcec993cc86014f9ff32b2dd46a35926e16027477a29c10a07d9f519d338
- url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events
  content_hash: c727756f4294ae3e95732c3e4efbaac94cfcc4f226a7309265fb01d4f100433c
updated_at: 2026-05-20T09:31:10Z
---

# Getting Started with Telnyx Video Rooms and Client SDKs

*Part 2 of 2 — see also: [Part 1](getting-started-with-telnyx-video-rooms-and-client-sdks--part-1.md)*

Build real‑time video into web, Android, and iOS apps with Telnyx Video Rooms. This guide explains core concepts (rooms, participants, streams, subscriptions, state), how to create rooms and client join tokens, and how to connect, publish, and subscribe using the JavaScript, Android, and iOS SDKs—plus token refresh, events, and useful server APIs.

## Server‑side controls and moderation
- Use server APIs for operations outside the client:
  - [Room Sessions](room-sessions.md): end a session; mute/unmute/kick all participants
  - [Room Participants](room-participants.md): list/search participants by filters (e.g., session id)
  - [Room Recordings](room-recordings.md) and [Room Compositions](room-compositions.md): record and render outputs
  - [Rooms](rooms.md): create/manage rooms
- Client events include participant_leaving (reason: 'kicked') and track_censored/track_uncensored for moderation actions (JavaScript), with analogous signals on mobile SDKs.

## WebRTC stats and network insights
- JavaScript: room.getWebRTCStatsForStream(participantId, streamKey) and network_metrics_report events.
- Android: room.getWebRTCStatsForStream(participantId, streamKey, callback) with parsed models for local/remote audio/video.
- iOS: room.getWebRTCStatsForStream(participantId, streamKey, completion: ...).

## Samples and further reading
- JS tutorial and sandbox: [JavaScript Video Tutorial](javascript-video-tutorial.md) (includes CodeSandbox links)
- JavaScript SDK overview: [Getting Started with JavaScript SDK for Video](getting-started-with-javascript-sdk-for-video.md) and [Room and Events](room-and-events.md)
- Android SDK repo and demo app: https://github.com/team-telnyx/telnyx-video-android
- iOS SDK repo and Telnyx Meet sample: https://github.com/team-telnyx/telnyx-video-ios and https://github.com/team-telnyx/telnyx-meet-ios

## Tips and troubleshooting
- Browser/mobile permissions: ensure CAMERA and MICROPHONE permissions are granted.
- Token errors/expiry: regenerate client tokens using the refresh token; update the SDK before expiry.
- Rendering video (Android): always removeSink(surface) and release surfaces when unmounting to avoid leaks.
- Subscriptions: you must explicitly subscribe to remote streams to receive their tracks; unsubscribe when not displayed to conserve bandwidth.
