---
title: Getting Started with iOS Client SDK
summary: The Telnyx Video iOS SDK provides the functionality needed to join and interact
  with a video room from an iOS application. This page covers the core concepts of
  the Video API, the Room API surface, lifecycle events, installation, prerequisites,
  and code examples for connecting, publishing local media, subscribing to remote
  streams, and disconnecting.
sources:
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
updated_at: 2026-08-05T14:02:26Z
---

# Getting Started with iOS Client SDK

*Part 1 of 3 — see also: [Part 2](getting-started-with-ios-client-sdk--part-2.md), [Part 3](getting-started-with-ios-client-sdk--part-3.md)*

The Telnyx Video iOS SDK provides the functionality needed to join and interact with a video room from an iOS application. This page covers the core concepts of the Video API, the Room API surface, lifecycle events, installation, prerequisites, and code examples for connecting, publishing local media, subscribing to remote streams, and disconnecting.

## Overview

The Telnyx Video iOS SDK provides the functionality you need to join and interact with a video room from an iOS application.

- [iOS SDK repository](https://github.com/team-telnyx/telnyx-video-ios)
- Demo app: [Telnyx Meet](https://github.com/team-telnyx/telnyx-meet-ios)

## Core Concepts

These are the important concepts to understand when working with the Video API.

- A `Room` represents a real time audio/video/screen share session with other people or participants. It is fundamental to building a video application.
- A `Participant` represents a person inside a `Room`. Each `Room` has one `Local Participant` and one or more `Remote Participants`.
- `Room State` tracks the state of the room as it changes, making it easy to understand what has happened to a `Room`.
  - `Room State` could change because a `Local Participant` has started publishing a stream or because a `Remote Participant` left.
- A `Stream` represents the audio/video media streams that are shared by `Participants` in a `Room`.
  - A `Stream` is identified by its `participantId` and `streamKey`.
- A `Participant` can have one or more `Stream`s associated with it.
- A `Subscription` is used to subscribe to a `Stream` belonging to a `Remote Participant`.

## Room API

The following is a high level overview of the Room API and its functionality.

```swift
func connect(statusChanged: @escaping (_ status: RoomStatus) -> Void)

func disconnect(completion: @escaping () -> Void)

func updateClientToken(clientToken: String, completion: () -> Void)

func addStream(key: StreamKey, audio: RTCAudioTrack?, video: RTCVideoTrack?, completion:
@escaping OnSuccess, onFailed: @escaping OnFailed)

func updateStream(key: StreamKey, audio: RTCAudioTrack?, video: RTCVideoTrack?, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func removeStream(key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func addSubscription(participantId: ParticipantId, key: StreamKey, audio: Bool, video: Bool, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func pauseSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func resumeSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func updateSubscription(participantId: ParticipantId, key: StreamKey, audio: Bool, video: Bool, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func removeSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func getWebRTCStatsForStream(participantId: ParticipantId, streamKey: StreamKey, completion: @escaping (_ stats: [String: [String: Any]]) -> Void)

/// Helpers methods
func getState() -> State
func getLocalParticipant() throws -> Participant
func getLocalStreams() throws -> [StreamKey: Stream]
func getParticipantStream(participantId: ParticipantId, key: StreamKey) -> Stream?
func getParticipantStreams(participantId: ParticipantId) throws -> [StreamKey: Stream]
```

## Room Events

The following events fire as you make API calls.

```swift
/// Triggered each time the state is updated.
var onStateChanged: ((_ state: State) -> Void)?

/// Triggered when connected to a room.
var onConnected: (() -> Void)?

/// Triggered when disconnects from room / leaves room.
var onDisconnected: (() -> Void)?

/// Triggered when a remote participant joins the room.
var onParticipantJoined: ((_ participantId: ParticipantId, _ participant: Participant) -> Void)?

/// Triggered when a remote participant leaves the room.
var onParticipantLeft: ((_ participantId: ParticipantId) -> Void)?

/// Triggered after successfully registering a stream.
var onStreamPublished: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered after successfully unregistering a stream.
var onStreamUnpublished: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when a local stream or a remote stream track has been enabled.
/// Notifies consumers about remote stream tracks being enabled. For example: when audio is unmuted or video has started on a remote stream.
var onTrackEnabled: ((_ participantId: ParticipantId, _ streamKey: StreamKey, _ kind: String) -> Void)?

/// The opposite of `onTrackEnabled`. Triggers when a local stream or a remote stream track has been disabled.
/// Notifies consumers about remote stream tracks being disabled. For example: when audio is muted or video has stopped on a remote stream.
var onTrackDisabled: ((_ participantId: ParticipantId, _ streamKey: StreamKey, _ kind: String) -> Void)?

/// Triggered when subscribed to a remote participant's stream.
var onSubscriptionStarted: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when an ongoing subscription is paused.
var onSubscriptionPaused: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when a paused subscription is resumed.
var onSubscriptionResumed: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when the subscription is reconfigured.
var onSubscriptionReconfigured: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when subscription is ended for a remote participant's stream.
/// The subscription can be ended by calling `removeSubscription(ParticipantId,StreamKey)` or when the remote participant leaves.
var onSubscriptionEnded: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// onError
/// Triggered when there's an error processing incoming events from the server.
var onError: ((_ error: SdkError) -> Void)?
```

## Understanding Room State

Everything in the SDK centers around the `Room` object. When the state of the `Room` changes (for example, a new participant joins or a remote participant starts publishing a stream) the `onStateChanged` event is triggered. The event is invoked with a `state` parameter which contains the current state of the `Room`.

```swift
/// Triggered each time the state is updated.
var onStateChanged: ((_ state: State) -> Void)?
```

## Prerequisites

### Install the SDK

Currently, the Telnyx iOS Video SDK can be installed using CocoaPods. For instructions, see the [iOS releases repo](https://github.com/team-telnyx/telnyx-video-ios).

### Get an API Key

You will need an API key associated with your Mission Control Portal account under **API Keys**. See [Create API Keys](create-api-keys.md) for instructions. An API key is your credential to access the API and allows you to:

- Authenticate to the REST API
- Manage your access tokens

### Create a Room to Join

In order to join a room you must create it, if it does not already exist. See the [Rooms REST API](https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) to create one. Additional resources on other endpoints are available to perform basic operations on a `Room`.

### Generate a Client Token

In order to join a room you must have a client token for that `Room`. The `client token` is short lived and you can refresh it using the `refresh token` provided with it when you request a `client token`. See the [client token docs](https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) to learn how to create one.
