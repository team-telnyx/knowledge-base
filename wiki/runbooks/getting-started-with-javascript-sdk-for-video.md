---
title: Getting Started with JavaScript SDK for Video
summary: Telnyx's JavaScript SDK is easy to use and makes it simple to get started with video calling.
sources:
  - url: https://developers.telnyx.com/docs/video/javascript-sdk/index
    content_hash: 8824d11f9cffa88e90dd0c9199f80cacc5f047a2fd20843ca9dd176f96a821bc
updated_at: 2026-04-10T00:00:00Z
---

# Getting Started with JavaScript SDK for Video

Telnyx's JavaScript SDK is easy to use and makes it simple to get started with video calling. With the SDK, you can quickly add video calling to your web app or website.

The Telnyx Video Client SDK provides all the functionality you need to join and interact with a video room from a browser.

![npm](https://img.shields.io/npm/v/@telnyx/video.svg?color=lightgrey\&style=flat)

## Adding Telnyx to your JavaScript client application

Include the `@telnyx/video` npm module as a dependency:

`npm install @telnyx/video --save`

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Then, import `@telnyx/video` in your application code.

```javascript theme={null}
// main.js
import { Room, createLocalParticipant } from '@telnyx/video';
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Now you are ready to connect to a video room that you created. In order to connect to a video room you will require a client token that has the necessary grants to join the room.

```javascript theme={null}
const room = new Room(roomId, {
  clientToken: '',
  localParticipant: createLocalParticipant({
    context: JSON.stringify({ name: 'Bob The Builder', id: 1 }), // send data that you can associate with this participant (for e.g., userId for this participant in your DB)
  }),
});

const stateCallback = (state) => {
  // the state object is immutable and can be easily integrated with most modern UI libraries like React, Vue etc.
};

room.on('state_changed', stateCallback);

room.connect().then(() => {
  console.log('You are connected to the room!');
});
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Understanding the state of the video room

The `state_changed` event callback contains the state of the SDK at that point in time. This is an immutable object that you can use in most modern UI libraries like React and Vue.

The Typescript definition of the State is helpful in understanding the structure of this object.

```javascript theme={null}
type Status =
  | 'initialized'
  | 'connecting'
  | 'connected'
  | 'disconnecting'
  | 'disconnected';

interface State {
  status: Status;
  localParticipantId: Participant['id'];
  participants: {
    [id: string]: Participant;
  };
  streams: {
    [id: string]: Stream;
  };
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Everytime the state of the SDK changes the `state_changed` callback is invoked with a new immutable state that represents the current state of the SDK. Since most modern UI libraries are able to compare the two immutable states and render only the components that changed it makes it easier to integrate the SDK with them rather than depending on multiple event callbacks.

For e.g., based on how we initialized it in the above code example the initial state of the SDK would result in an object give below. Note that the ID of the local participant is unique and are generated based on UUID v4 standard when you create the local participant.

```javascript theme={null}
{
  status: 'initialized',
  localParticipantId: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
  participants: {
    "8c3bacb5-2e90-4379-8ee8-d5446213fee9": {
      id: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
      context: "{\"name\":\"Bob The Builder\",\"id\":1}",
      streams: {},
    },
  },
  streams: {},
};
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

At this point there are no streams being published by the local participant. We will come to that shortly. The participant object follows the TypeScript interface given below.

```javascript theme={null}
interface Participant {
  id: string;
  context?: string;
  streams: {
    [key: string]: Stream['id'];
  };
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

When we called the `room.connect()` method in the example code the state of the SDK will change to the following ...

```javascript theme={null}
{
  status: 'connecting',
  localParticipantId: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
  participants: {
    "8c3bacb5-2e90-4379-8ee8-d5446213fee9": {
      id: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
      context: "{\"name\":\"Bob The Builder\",\"id\":1}",
      streams: {},
    },
  },
  streams: {},
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This new state will be available to your application via the `state_changed` callback. Since state is immutable the only difference between the initial state and the new state is the `status` property. If you are using a modern UI library like React you can easily rerender the components to show that the application is connecting to the room.

When successfully connected the state changes to ...

```javascript theme={null}
{
  status: "connected",
  localParticipantId: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
  participants: {
    "8c3bacb5-2e90-4379-8ee8-d5446213fee9": {
      id: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
      context: "{\"name\":\"Bob The Builder\",\"id\":1}",
      streams: {},
    },
  },
  streams: {},
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Now we are ready to start publishing streams on behalf of the local participant.

## Publishing your local camera and mic stream

In order to publish a stream you need to define the constraints of the media. The simplest form of the constraints is ...

```javascript theme={null}
const constraints = { audio: true, video: true };
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

With these constraints the SDK will try to obtain both audio and video from the local participant. In order to publish the stream as the local participant you have to use the `publish` method available to you via the room object.

```javascript theme={null}
room.publish('self', {
  constraints: { audio: true, video: true },
});
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

The first argument to `publish` is a string that acts as the key that you can use to refer to this specific stream. You can use any valid string for this as long as you are consistent in your application. For e.g. here we're using 'self' for the camera/mic stream but you could use 'presentation' as the key for when you publish video of the screen. We will get to how you can publish your screen in a short while.

When you make the request to publish a stream, the browser will ask for the necessary permissions required to access the camera and mic. Once the permissions are acquired the SDK will configure and publish the stream to the room you are connected to.

At this point you will receive the new state to the `state_changed` event callback with the newly created stream.

```javascript theme={null}
{
  status: "connected",
  localParticipantId: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
  participants: {
    "8c3bacb5-2e90-4379-8ee8-d5446213fee9": {
      id: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
      context: "{\"name\":\"Bob The Builder\",\"id\":1}",
      streams: {
        self: "a87dd242-de78-4c19-a09c-23b336c9f25e",
      },
    },
  },
  streams: {
    "a87dd242-de78-4c19-a09c-23b336c9f25e": {
      id: "a87dd242-de78-4c19-a09c-23b336c9f25e",
      key: "self",

      // the constraits that was provided by you
      constraints: {
        audio: true,
        video: true,
      },
      bitrate: 256000, // also configurable when you publish a stream

      audioActive: false, // whether the audio track is being published
      videoActive: false, // whether the video track is being published
      source: MediaStream, // an instance of MediaStream that can be used to render video/audio
      audioTrack: undefined, // this will be an instance of MediaStreamTrack when the track is available
      videoTrack: undefined, // this will be an instance of MediaStreamTrack when the track is available

      isSpeaking: false, // whether the audio level of the track is high enough to consider the participant who owns this stream is speaking or not
      isRemote: false, // whether the stream originates from a remote source or not

      isPublishing: true, // whether the stream is being published
      isConfiguring: false, // whether the SDK is currently negotiating the WebRTC connection

      participantId: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
    },
  },
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

The stream object is the most complex object in the state of the SDK. However you don't have to worry about all of these properties at the moment.

As you can see the `isPublishing` property of the stream is `true` now. This means that the stream is being published, which involves creating the SDP (Session Description Protocol) and establishing the WebRTC connection. You can't publish another stream of the same key ("self" in our case) until this stream is published or removed (by unpublishing).

Once the SDK acquires the media tracks from the camera and mic of the local participant a new state will be returned using the `state_changed` callback. This state will contain the audio and video track from the local media devices.

The streams object at this point will look like this

```javascript theme={null}
  streams: {
    "a87dd242-de78-4c19-a09c-23b336c9f25e": {
      id: "a87dd242-de78-4c19-a09c-23b336c9f25e",
      key: "self",

      // the constraits that was provided by you
      constraints: {
        audio: true,
        video: true,
      },
      bitrate: 256000,

      audioActive: true,
      videoActive: true,
      source: MediaStream,
      audioTrack: MediaStreamTrack,
      videoTrack: MediaStreamTrack,

      isSpeaking: false,
      isRemote: false,

      isPublishing: true,
      isConfiguring: true,

      participantId: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
    },
  },
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

As you can see at this point you can use the `source` or the media tracks individually from `audioTrack` and `videoTrack` to show the media in your UI.

You can also see that the `audioActive` and `videoActive` flags are now true indicating the stream is publishing audio and video respectively.

Another property that was updated in the new state is the `isConfiguring` flag. You can ignore this in most use-cases as this indicates if the WebRTC connection is being negotiated.

Once the WebRTC connection is negotiated and the stream is successfully published the stream state would look like this

```javascript theme={null}
  streams: {
    "a87dd242-de78-4c19-a09c-23b336c9f25e": {
      id: "a87dd242-de78-4c19-a09c-23b336c9f25e",
      key: "self",

      // the constraints provided by you
      constraints: {
        audio: true,
        video: true,
      },
      bitrate: 256000,

      audioActive: true,
      videoActive: true,
      source: MediaStream,
      audioTrack: MediaStreamTrack,
      videoTrack: MediaStreamTrack,

      isSpeaking: false,
      isRemote: false,

      isPublishing: false,
      isConfiguring: false,

      participantId: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
    },
  },
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

At this point the stream will be available to be subscribed by other clients connected to the same room.

## Knowing when a new participant joins the room

A video room can have multiple participants and you can get a list of all the participants connected to the room at the time by using the `participants` property in the state.

If the participant is not publishing any streams the `streams` property of that participant will be an empty object.

Let's imagine that another participant joins the same room from a different browser session with the following context

```javascript theme={null}
const room = new Room(roomId, {
  clientToken: '',
  localParticipant: createLocalParticipant({
    context: JSON.stringify({ name: 'Oswald', id: 2 }), // send data that you can associate with this participant (for e.g., userId for this participant in your DB)
  }),
});
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Since the room already contains a participant who is publishing a stream the state once this session is connected would look something like ...

```javascript theme={null}
{
  status: "connected",
  localParticipantId: "d42926f5-fe6c-48d5-b24b-7444048fa68e",
  participants: {
    "8c3bacb5-2e90-4379-8ee8-d5446213fee9": {
      id: "8c3bacb5-2e90-4379-8ee8-d5446213fee9",
      context: "{\"name\":\"Bob The Builder\",\"id\":1}",
      streams: {
        self: "a87dd242-de78-4c19-a09c-23b336c9f25e",
      },
    },
    "d42926f5-fe6c-48d5-b24b-7444048fa68e": {
      id: "d42926f5-fe6c-48d5-b24b-7444048fa68e",
      context: "{\"name\":\"Oswald\",\"id\":2}",
      streams: {},
    },
  },
  streams: {
    "a87dd242-de78-4c19-a09c-23b336c9f25e": {
      id: "a87dd242-de78-4c19-a09c-23b336c9f25e",
      key: "self",

      audioActive: true, // whether audio is being published by the remote stream
      videoActive: true, // whether video is bein published by the remote stream
      source: MediaStream,
      audioTrack: undefined, // will be an instance of MediaStreamTrack once subscribed
      videoTrack: undefined, // will be an instance of MediaStreamTrack once subscribed
      videoCodec: "vp8", // the codec used by the remote video
      audioCodec: "opus", // the codec used by the remote audio

      isRemote: true,
      isSpeaking: false, // whether the remote participant is speaking or not

      isConfiguring: false, // whether the WebRTC connection is being negotiated or not

      subscription: {
        status: "unsubscribed", // will change to 'subscribed' once the the client subscribes to this stream
      },

      participantId: "8c3bacb5-2e90-4379-8ee8-d5446213fee9", // the ID of the participant this stream belong to
    },
  },
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

As you can see there is already a participant in the `participants` object that maps to the remote particpant from the previous browser session. This remote participant also has a stream with the key "self".

The stream object for "self" has the structure very similar to the one we saw before but has a few new properties.

The ones that are particularly interesting are `subscription`, `videoCodec`, and `audioCodec`. The properties for video and audio codec can be used to decide if the browser has the capabilities to decode the video and audio tracks.

Then there is `subscription.status`, which is `unpublished` at the moment.

## Subscribing to a remote stream

At this point we are ready to subscribe to the remote stream published by the participant. In order to do that we use the `subscribe` method from the room object.

```javascript theme={null}
room.subscribe('a87dd242-de78-4c19-a09c-23b336c9f25e');
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This will start the WebRTC negotiation to receive the remote stream. Once successful the `subscription.status` will change to `subscribed`.

You can use the `source` property, which is an instance of MediaStream to render the media on the browser.

If the remote participant unpublishes this stream the SDK will automatically unsubscibe from the stream and the stream will disappear from the state.


## Related Pages

- [Getting Started with Video](../runbooks/getting-started-with-video.md)
- [Getting Started with iOS Client SDK](../runbooks/getting-started-with-ios-client-sdk.md)
- [Getting Started with Android Client SDK](../runbooks/getting-started-with-android-client-sdk.md)
- [Getting started with port-in orders](../tutorial/getting-started-with-port-in-orders.md)
- [Getting Started with Telnyx Voice API](../runbooks/getting-started-with-telnyx-voice-api.md)
