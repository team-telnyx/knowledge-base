---
title: Getting Started with Video
summary: Telnyx Video Rooms is a platform for adding real-time audio and video to
  web and mobile applications. It combines REST APIs, client SDKs, and the Mission
  Control portal to let developers create rooms, issue join tokens, and manage participants,
  sessions, recordings, and compositions.
sources:
- url: https://developers.telnyx.com/docs/video/get-started/index
updated_at: 2026-08-05T14:01:54Z
---

# Getting Started with Video

Telnyx Video Rooms is a platform for adding real-time audio and video to web and mobile applications. It combines REST APIs, client SDKs, and the Mission Control portal to let developers create rooms, issue join tokens, and manage participants, sessions, recordings, and compositions.

## Overview

Telnyx Video Rooms are enabled using the Rooms API. You can create as many rooms as needed using this API.

To access a Telnyx Video Room, a Client Join Token will first need to be generated in JWT form. You can use the HTTPS API and authenticate using the API Key associated with your Mission Control account under API Keys.

Adding Telnyx Rooms functionality to your app can be done using the JS SDK (mobile SDKs coming soon). To gain access to a live Video Rooms sample app, reach out to the Telnyx sales team.

## Glossary

| Term | Definition |
| --- | --- |
| Room | Resource representing a virtual place where multiple endpoints using one of Telnyx's Programmable Video SDKs can connect. |
| Room Session | Resource representing a moment where multiple Room Participants were communicating within a given Room. |
| Room Participant | Resource representing an endpoint using one of Telnyx's Programmable Video SDKs to connect to a given Room. |
| JWT | JSON Web Token. A standard method for representing claims. |
| Client Join Token (JWT) | A JWT token which contains grants allowing in the Room use case to join a Room. |
| Refresh Token (JWT) | A JWT token which permits obtaining a new Client Token with the same grants. |
| API Key | Secret API Key generated via Portal and used to authenticate Telnyx API calls. |
| Video SDK | A library used to provide Video features to your application using the Telnyx Video platform. |

## Configuration and Usage

Telnyx Video is enabled using **Video Rooms**. A Video Room represents a communications session among multiple endpoints using one of Telnyx's Programmable Video SDKs. Connected users (Participants) can share video and audio Tracks with the Room, and receive video and audio Tracks from other Participants in the Room.

You can create as many Rooms as you want. For example, you could create a long-lived Room such as "Daily Standup", or Rooms that you would delete after they've been used, like "1-1 with X". To create a Video Room, use the [Rooms REST API V2](https://developers.telnyx.com/api-reference/rooms/view-a-list-of-rooms).

A Video Room can only be joined if the client owns a **Client Join Token**. You can create one using the [Client Tokens REST API V2](https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room). The Client Join Token is short-lived, and you can refresh it using the **Refresh Token** provided with it when you request a Client Join Token.

Once you have a Video Room and a Client Join Token for it, you can use the Video SDK on your client side to connect your client to the Room you just created.

## Architecture

Video Rooms is a platform that enables developers to add audio and video capability to web, Android, and iOS applications. The platform consists of REST APIs, Client SDKs, and the Mission Control portal, making it easy to capture, stream, record, and render live audio and video.

A video application built with Video Rooms has two parts:

- **Client:** The client-side JavaScript, iOS, and Android SDKs used to interact with a `Room` instance.
- **Server:** The REST APIs and portal to create and manage rooms and sessions, configure recording, or leverage the `Participants API` to moderate participants in a `Room`.

## Core Concepts

Understanding the basic concepts of the Video SDK will help you understand how it works. These concepts apply across all platforms.

- A `Room` represents a real-time audio/video/screen share session with other people or participants. It is fundamental to building a video application.
- `Room State` tracks the state of the room as it changes, making it easy to understand what has happened to a `Room`. For example, Room State could change because a Local Participant has started publishing a stream, or because a Remote Participant left.
- A `Participant` represents a person inside a `Room`. Each `Room` has one `Local Participant` and one or more `Remote Participants`.
- A `Stream` represents the audio/video media streams that are shared by `Participants` in a `Room`. A `Stream` is identified by its `participantId` and `streamKey`.
- A `Subscription` is used to subscribe to a `Stream` belonging to a `Remote Participant`.

## Client SDKs

The [JavaScript SDK](javascript-sdk.md) API reference details the API of the SDK, including behaviors of the `Room` class and the events that trigger and how they function.

- [Room Events](room-events.md)
- [Room Class API Reference](room-class-api-reference.md)

## Server APIs

- [Rooms](https://developers.telnyx.com/api-reference/rooms/view-a-list-of-rooms) — manage Rooms.
- [Client Access Tokens](https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) — manage client access tokens needed to interact with a `Room`.
- [Sessions](https://developers.telnyx.com/api-reference/room-sessions/view-a-list-of-room-sessions) — manage room sessions, end a session, and mute/unmute/kick all participants in a given session.
- [Participants](https://developers.telnyx.com/api-reference/room-participants/view-a-list-of-room-participants) — search for participants based on filters such as `session id`.
- [Recordings](https://developers.telnyx.com/api-reference/room-recordings/view-a-list-of-room-recordings) — manage recordings, including bulk delete.
- [Compositions](https://developers.telnyx.com/api-reference/room-compositions/view-a-list-of-room-compositions) — create and manage compositions.
