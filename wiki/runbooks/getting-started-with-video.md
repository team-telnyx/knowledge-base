---
title: Getting Started with Video
summary: Telnyx's video documentation is the perfect place to start learning about our platform.
sources:
  - url: https://developers.telnyx.com/docs/video/get-started/index
    content_hash: dd1caa701526c5ca4427ea46ce1e787f54084e66c2a1e793ed90ba1cc6f3d91c
updated_at: 2026-04-10T00:00:00Z
---

# Getting Started with Video

Telnyx's video documentation is the perfect place to start learning about our platform. With step-by-step guides, you'll be up and running in no time!

Telnyx Video Rooms are enabled using the Rooms API. You can create as many rooms as needed using this API.

<p>
  To access a Telnyx Video Room, a Client Join Token will first need to be
  generated in JWT form. You can use our HTTPS API and authenticate using the
  API Key associated with your Mission Control account under API Keys. Find out
  more about authenticating with API V2 here.
</p>

<p>
  Adding Telnyx Rooms functionality to your app can be done using our JS SDK
  (mobile SDKs coming soon). To gain access to a live Video Rooms sample app,
  reach out to our sales team today!
</p>

Check out the full API reference today!

## Glossary

<table>
  <tbody>
    <tr>
      <td>Room</td>

      <td>
        Resource representing a virtual place where multiple endpoints using one
        of Telnyx’s Programmable Video SDKs can connect.
      </td>
    </tr>

    <tr>
      <td>Room Session</td>

      <td>
        Resource representing a moment where multiple Room Participants were
        communicating within a given Room.
      </td>
    </tr>

    <tr>
      <td>Room Participant</td>

      <td>
        Resource representing an endpoint using one of Telnyx’s Programmable Video
        SDKs to connect to a given Room.
      </td>
    </tr>

    <tr>
      <td>JWT</td>
      <td>JSON Web Token. A standard method for representing claims.</td>
    </tr>

    <tr>
      <td>Client Join Token (JWT)</td>

      <td>
        A JWT token which contains grants allowing in the Room usecase to join a
        Room.
      </td>
    </tr>

    <tr>
      <td>Refresh Token (JWT)</td>

      <td>
        A JWT token which permits to obtain a new Client Token with same grants.
      </td>
    </tr>

    <tr>
      <td>API Key</td>

      <td>
        Secret API Key generated via Portal and used to authenticate Telnyx API
        calls.
      </td>
    </tr>

    <tr>
      <td>Video SDK</td>

      <td>
        A library used to provide Video features to your application using Telnyx
        Video platform.
      </td>
    </tr>
  </tbody>
</table>

<h3>Configuration and usage</h3>

<div>
  Telnyx Video is enabled using <b>Video Rooms</b>. A Video Room represents
  communications session among multiple endpoints using one of Telnyx’s
  Programmable Video SDKs. Connected users (Participants) can share video and
  audio Tracks with the Room, and receive video and audio Tracks from other
  Participants in the Room. You can as many Rooms as you want. For example you
  could create a long lived Room such as "Daily Standup", or Rooms that you
  would delete after it's been used like "1-1 with X". To create a Video Room
  you can use the REST API V2 documented
  <a href="/api-reference/rooms/view-a-list-of-rooms">here</a>. A Video Room can only be joined
  if the client owns a <b>Client Join Token</b>, you can create it using the
  REST API V2 documented
  <a href="/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room">here</a>. The Client Join
  Token is short lived and you will be able to refresh it using the
  <b>Refresh Token</b> provided with it when you request for a Client Join
  Token. Once you have a Video Room and an Client Join Token for it, you can
  then use our Video SDK on your client side to connect your client to the Room
  you just created.
</div>

## Concepts

### Architecture

`Video Rooms` is a platform that enables developers to add audio and video capability to Web, Android, and iOS applications.

The platform consists of REST APIs, Client SDKs, and our mission control portal that makes it really easily to capture, stream, record, and render live audio and video.

A video application built with Video Rooms has to parts:

* **Client:** Our client side Javascript, iOS, and Android SDKs used to interact with a `Room` instance
* **Server:** Our REST APIs and portal to create/manage room and session, configuring recording, or leverage our `Participants API` to moderator participants in a `Room`.

### Terms

Understanding the basic concepts of the video SDK will help you understand how it works. These concepts apply in general across all of our platforms.

* A `Room` represents a real time audio/video/screen share session with other people or participants. It is fundamental to building a video application.

* `Room State` tracks the state of the room as it changes making it extremely easy to understand what's happened to a `Room`.
  * `For example`: Room State could change due to a Local Participant has started publishing a stream or because a Remote Participant left.
    A Stream represents the audio/video media streams that are shared by Participants in a Room

* A `Participant` represents a person inside a `Room`. Each `Room` has one `Local Participant` and one or more `Remote Participants`.

* A `Stream` represents the audio/video media streams that are shared by `Participants` in a `Room`
  * A `Stream` is indentified by it's `participantId` and `streamKey`

* A `Subscription` is used to subscribe to a `Stream` belonging to a `Remote Participant`

### Dive a bit deeper

Dive a little bit deeper into our `Video Rooms` platform to get a better understand of what its capable of, and what you can buid. Learn more about our Client SDKs and Server APIs.

### Client SDKs

Our [Javascript SDK API reference](getting-started-with-javascript-sdk-for-video.md) which details the API of our SDK including behaviors of the `Room` class and the `Events` that triggers and how they function.

* [Rooms Class API Reference](room-and-events.md#room)
* [Room Events Reference](room-and-events.md#room-events)

### Server APIs

* [Rooms](https://developers.telnyx.com/api-reference/rooms/view-a-list-of-rooms) - manage Rooms
* [Client Access Tokens](https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) - manage client access tokens needed to interact with a `Room`
* [Sessions](https://developers.telnyx.com/api-reference/room-sessions/view-a-list-of-room-sessions) - manage room sessions, end a session, and mute/unmute/kick all participants in a given session.
* [Participants](https://developers.telnyx.com/api-reference/room-participants/view-a-list-of-room-participants) - search for participants based on a number of filters like `session id`
* [Recordings](https://developers.telnyx.com/api-reference/room-recordings/view-a-list-of-room-recordings) - manage recordings, including bulk delete.
* [Compositions](https://developers.telnyx.com/api-reference/room-compositions/view-a-list-of-room-compositions) - create and manage compositions.


## Related Pages

- [Getting Started with 10DLC](../tutorial/getting-started-with-10dlc.md)
- [Getting started with port-in orders](../tutorial/getting-started-with-port-in-orders.md)
- [Getting Started with Telnyx Voice API](../runbooks/getting-started-with-telnyx-voice-api.md)
- [Getting Started with iOS Client SDK](../runbooks/getting-started-with-ios-client-sdk.md)
- [Getting Started with Android Client SDK](../runbooks/getting-started-with-android-client-sdk.md)
