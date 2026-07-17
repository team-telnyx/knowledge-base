---
title: Telnyx Video SDKs
summary: Telnyx Video Rooms is a platform for adding real-time audio and video to
  Web, Android, and iOS applications, built on REST APIs and Client SDKs. This page
  covers the core concepts (Rooms, Participants, Streams, Subscriptions), server-side
  prerequisites (API key, Room creation, client token), and detailed usage of the
  JavaScript, iOS, and Android SDKs including installation, connecting, publishing
  and subscribing to streams, room events, and WebRTC stats.
sources:
- url: https://developers.telnyx.com/docs/video/android-client-sdk
- url: https://developers.telnyx.com/docs/video/get-started/index
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
- url: https://developers.telnyx.com/docs/video/javascript-sdk/index
- url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial
- url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events
updated_at: 2026-07-17T09:18:10Z
---

# Telnyx Video SDKs

*Part 5 of 5 — see also: [Part 1](telnyx-video-sdks--part-1.md), [Part 2](telnyx-video-sdks--part-2.md), [Part 3](telnyx-video-sdks--part-3.md), [Part 4](telnyx-video-sdks--part-4.md)*

Telnyx Video Rooms is a platform for adding real-time audio and video to Web, Android, and iOS applications, built on REST APIs and Client SDKs. This page covers the core concepts (Rooms, Participants, Streams, Subscriptions), server-side prerequisites (API key, Room creation, client token), and detailed usage of the JavaScript, iOS, and Android SDKs including installation, connecting, publishing and subscribing to streams, room events, and WebRTC stats.

## Server APIs

The following REST APIs are used to manage Video Rooms from the server side:

- [Rooms](/api-reference/rooms/view-a-list-of-rooms) — manage Rooms
- [Client Access Tokens](/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) — manage client access tokens needed to interact with a `Room`
- [Sessions](/api-reference/room-sessions/view-a-list-of-room-sessions) — manage room sessions, end a session, and mute/unmute/kick all participants in a given session
- [Participants](/api-reference/room-participants/view-a-list-of-room-participants) — search for participants based on a number of filters like `session id`
- [Recordings](/api-reference/room-recordings/view-a-list-of-room-recordings) — manage recordings, including bulk delete
- [Compositions](/api-reference/room-compositions/view-a-list-of-room-compositions) — create and manage compositions
