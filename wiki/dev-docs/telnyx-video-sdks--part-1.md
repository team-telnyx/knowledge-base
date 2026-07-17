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

*Part 1 of 5 — see also: [Part 2](telnyx-video-sdks--part-2.md), [Part 3](telnyx-video-sdks--part-3.md), [Part 4](telnyx-video-sdks--part-4.md), [Part 5](telnyx-video-sdks--part-5.md)*

Telnyx Video Rooms is a platform for adding real-time audio and video to Web, Android, and iOS applications, built on REST APIs and Client SDKs. This page covers the core concepts (Rooms, Participants, Streams, Subscriptions), server-side prerequisites (API key, Room creation, client token), and detailed usage of the JavaScript, iOS, and Android SDKs including installation, connecting, publishing and subscribing to streams, room events, and WebRTC stats.

## Overview

Telnyx Video Rooms is a platform that enables developers to add real-time audio and video capability to Web, Android, and iOS applications. The platform consists of REST APIs, Client SDKs, and the Mission Control portal, and makes it easy to capture, stream, record, and render live audio and video.

A video application built with Video Rooms has two parts:

- **Client:** The JavaScript, iOS, and Android SDKs used to interact with a `Room` instance.
- **Server:** The REST APIs and portal used to create and manage rooms and sessions, configure recording, and leverage the Participants API to moderate participants in a `Room`.

### Glossary

| Term | Definition |
| --- | --- |
| Room | Resource representing a virtual place where multiple endpoints using one of Telnyx's Programmable Video SDKs can connect. |
| Room Session | Resource representing a moment where multiple Room Participants were communicating within a given Room. |
| Room Participant | Resource representing an endpoint using one of Telnyx's Programmable Video SDKs to connect to a given Room. |
| JWT | JSON Web Token. A standard method for representing claims. |
| Client Join Token (JWT) | A JWT token which contains grants allowing the holder to join a Room. |
| Refresh Token (JWT) | A JWT token which permits obtaining a new Client Token with the same grants. |
| API Key | Secret API Key generated via Portal and used to authenticate Telnyx API calls. |
| Video SDK | A library used to provide Video features to your application using the Telnyx Video platform. |

### Core Concepts

These concepts apply across all Telnyx Video platforms:

- A `Room` represents a real-time audio/video/screen-share session with other people or participants. It is fundamental to building a video application.
- `Room State` tracks the state of the room as it changes, making it easy to understand what has happened to a `Room`. For example, Room State could change because a Local Participant has started publishing a stream or because a Remote Participant left.
- A `Participant` represents a person inside a `Room`. Each `Room` has one `Local Participant` and one or more `Remote Participants`.
- A `Stream` represents the audio/video media streams that are shared by `Participants` in a `Room`. A `Stream` is identified by its `participantId` and `streamKey`.
- A `Subscription` is used to subscribe to a `Stream` belonging to a `Remote Participant`.

## Prerequisites

Before connecting to a Room from any client SDK, you need three things from the server side.

### Get an API Key

You'll need an API key associated with your Mission Control Portal account under **API Keys**. See [Create API Keys](/development/api-fundamentals/create-api-keys) for instructions. An API key is your credential to access the Telnyx API and allows you to:

- Authenticate to the REST API
- Manage your access tokens

### Create a Room to join (if it doesn't exist)

In order to join a room you must create it, if it doesn't already exist. Use the [Rooms REST API](/api-reference/rooms/view-a-list-of-rooms) to create one. There are additional endpoints available to perform basic operations on a `Room`.

Example request:

```
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

The response includes an `id` field — that is the id for your newly created Room.

### Generate a client token to join a Room

In order to join a room you must have a client token for that `Room`. The `client token` is short-lived and you will be able to refresh it using the `refresh token` provided with it when you request a `client token`. See [Create client token to join a room](/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) for details.

Example request:

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"refresh_token_ttl_secs":3600,"token_ttl_secs":600}' \
  https://api.telnyx.com/v2/rooms/ROOM_ID/actions/generate_join_client_token
```

The `token` field in the response is the client access token you'll use to join the room.
