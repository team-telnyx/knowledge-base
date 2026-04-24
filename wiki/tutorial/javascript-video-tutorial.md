---
title: JavaScript Video Tutorial
summary: Learn how to add video to your web page with Telnyx's easy-to-use JavaScript SDK.
sources:
  - url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial/index
    content_hash: f14798074120711e75bb14d578c1178bddaacbf80f1e05f8553b87496136d22e
updated_at: 2026-04-10T00:00:00Z
---

# JavaScript Video Tutorial

Learn how to add video to your web page with Telnyx's easy-to-use JavaScript SDK

## In 10 minutes we'll build

A simple web app in vanilla javascript to make a video with audio from a caller to a callee.

## Get an API Key

> You need a Telnx account to create an API key so you can interact with our Rooms API

* If you don't have one please: <a href="https://telnyx.com/sign-up">Sign up</a> for a free account
* Navigate to <a href="https://portal.telnyx.com/#/app/api-keys">API Keys</a> section and create an API Key by clicking `Create API Key`  button.
* Copy your API key

## Create a Room

Let's use our Rooms API to create a room.

**Request**

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```bash theme={null}
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

**Response**

```json theme={null}
{
	"data": {
		"active_session_id": null,
		"created_at": "2022-07-29T01:25:51.938184Z",
		"enable_recording": false,
		"id": "599e4d1e-d0aa-40ee-867a-a527f2b2dccd",
		"max_participants": 10,
		"record_type": "room",
		"unique_name": "Jons Room 2",
		"updated_at": "2022-07-29T01:25:51.940294Z",
		"video_codecs": ["h264", "vp8"],
		"webhook_event_failover_url": "",
		"webhook_event_url": "https://example.com",
		"webhook_timeout_secs": null
	}
}
```

Great, grab the response has an `id` field, this is the id for your newly created Room.

## Generate a client token

You'll need a client access token to join the room.

To create one use our [REST API `rooms/create` endpoint.](https://developers.telnyx.com/api-reference/rooms/create-a-room#create-a-room)

<Callout type="info">
  You'll need to replace ROOM\_ID in in the url of the command with your room id, above. As well as YOUR\_API\_KEY as you have in previous steps.

**Request**

```bash theme={null}
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"refresh_token_ttl_secs":3600,"token_ttl_secs":600}' \
  https://api.telnyx.com/v2/rooms/ROOM_ID/actions/generate_join_client_token
```

**Response**

```json theme={null}
{
	"data": {
		"recort_type": "client_token",
		"refresh_token": "eyJhb***************************",
		"refresh_token_expires_at": "2022-07-29T02:29:07Z",
		"token": "eyJhb**********************************",
		"token_expires_at": "2022-07-29T01:39:07Z"
	}
}
```

The `token` field in the response is the client access token you'll use to join the room.

## 🏁 Checkpoint - run the app

At this point you should have the following:

* An API Key
* A room ID
* A room client access token

**Let's run the app in a sandbox**

There's a README with instructions inside the sandbox. We can use this sandbox as a template to build out the rest of our application.

<iframe title="first-telnyx-video-call-first-step" />

## Let's write some code

**Basic concepts of the video SDK**

Here are some basic concepts of the SDK that will help you better understand how it works.

* A `Room` represents a real time audio/video/screen share session with other people or participants. It is fundamental to building a video application.

* A `Participant` represents a person inside a `Room`. Each `Room` has one `Local Participant` and one or more `Remote Participants`.

* A `Stream` represents the audio/video media streams that are shared by `Participants` in a `Room`
  * A `Stream` is indentified by it's `participantId` and `streamKey`

* A `Participant` can have one or more `Stream`'s associated with it.

* A `Subscription` is used to subscribe to a `Stream` belonging to a `Remote Participant`

**Room Events**

There are a few events trigger on a `Room` instance that we'll need to finish building this app that makes a video call.

* `connected` - triggers when a room instance has connected to the server
* `participant_joined` - triggers when a remote participant joins the room
* `stream_published` - triggers when a stream has started being published to the room
* `subscription_started` - triggers when subscription to remote stream has started

Handling an event looks like this:

```javascript theme={null}
room.on("connected", async () => {
  ...
});
```

## 🏁 Checkpoint

> It might be helpful to take a look at the [full list of `Events` available on a `Room` instance.](../runbooks/room-and-events.md)

## Connect to the room and get local media

`NOTE: ` We can start implementing our code after the `room.initialize` block inside the sandbox above.

Let's connect to the room and use the standard WebRTC API to get the audio and video tracks from the device.

```javascript theme={null}
// connected to the room as the local participant
telnyxVideoClient.on("connected", async () => {
  // use the webrtc api to get media from devices
  let intercomStream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: true
  });
  console.log("got local stream using getUserMedia...");

  // Get audio and video tracks from the MediaStream's
  // since the sdk works with MediaStreamTrack
  let intercomAudioTrack = intercomStream.getAudioTracks()[0];
  let intercomVideoTrack = intercomStream.getVideoTracks()[0];
});
```

## Publish the stream and render it

We want to a add/publish a stream the room which consists of the audio and video track we received from the user's device, above.

We'll give the stream a key of "caller", which is how the stream is identified.

```javascript theme={null}
// add/publish a stream with a key "caller" to the room
await telnyxVideoClient.addStream("intercom", {
  audio: callerAudioTrack,
  video: callerVideoTrack
});
console.log("published local stream to the room...");
```

**Render the stream to the DOM**

Now, that we have the caller's stream we want to render it to the DOM.

The entire `room.connected` block looks like this:

```javascript theme={null}
// connected to the room as the local participant
room.on("connected", async () => {
  // use the webrtc api to get media from devices
  let callerStream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: true
  });
  console.log("got local stream using getUserMedia...");

  // Get audio and video tracks from the MediaStream's
  // since the sdk works with MediaStreamTrack
  let callerAudioTrack = callerStream.getAudioTracks()[0];
  let callerVideoTrack = callerStream.getVideoTracks()[0];

  // add/publish the stream with the key "caller" to the room
  await room.addStream("caller", {
    audio: callerAudioTrack,
    video: callerVideoTrack
  });
  console.log("published local stream to the room...");

  // render the caller stream to the page/DOM
  let videoElement = document.getElementById("caller");
  videoElement.srcObject = callerStream;
});
```

Great, we're now publishing the local partipants'/caller's stream, to the room which the callee can subscribe to.

## Subscribe to the callee's remote stream

As a caller, how do we know when the callee has joined the room or has started publishing a stream?

That's where the `participant_joined` and the `stream_published` [events that we went over earlier](#lets-write-some-code), come into play.

We need to listen for teh `stream_published` event like this:

```javascript theme={null}
// a stream has been published to the room
room.on(
  "stream_published",
  async (participantId, streamKey, state) => {
  ...
  }
);
```

**Understanding how subscriptions work**

\_\_The `stream_published` event is triggered for both local and remote streams. \_\_

In our case, we want to know when the callee's remote stream starts publishing so we can subscribe to it. We already know that the caller has published a "caller" stream so we can ignore that event.

**Subscribing to a stream**

When a stream is published in a room it doesn't mean it's audio and video tracks are accessible, yet. In order to access a remote stream's track we must explicitly subscribe to that stream and wait for the `subscription_started` event.

```javascript theme={null}
// a stream has been published to the room
room.on("stream_published", async (participantId, streamKey, state) => {
  // ignore streams that are published by the local participant
  // we only care about remote stream from other remote participant
  let participant = state.participants.get(participantId);
  if (participant.origin === "local") {
    return;
  }

  // the remote stream is identified using the participantId and streamKey
  // you need to subscribe to a remote stream in order to access it's `MediaStreamTrack`s
  await room.addSubscription(participantId, streamKey, {
    audio: true,
    video: true
  });
});
```

## Render the callee's remote stream

We're almost there! Now, we can listen to the `subscription_started` event and use args from that handler to get the callee's remote stream and render it to the DOM.

```javascript theme={null}
// a subscription to a remote stream has started
room.on("subscription_started", (participantId, streamKey, state) => {
  console.log(
    `subscription to the: ${participantId} ${streamKey} stream started...`
  );

  // use a helper method to easily access a remote participants' stream
  let remoteStream = room.getParticipantStream(participantId, streamKey);

  // create a MediaStream object from the remote stream's track so we can render it
  // to a video element
  let remoteMediaStream = new MediaStream([
    remoteStream.audioTrack,
    remoteStream.videoTrack
  ]);
  const calleeVideo = document.getElementById("callee");
  calleeVideo.srcObject = remoteMediaStream;
});
```

## Run the app

<iframe title="first-telnyx-video-call" />

To run the app:

* <a href="https://codesandbox.io/s/first-telnyx-video-call-zgk33u?file=/src/main.js">Open the sandbox</a>, the browser here represents the caller's app
* <a href="https://zgk33u.csb.app/">Open the app in another tab</a>, this represents the callee's application which you'll need to interact with.

**From the caller app**

* Click the call button
* You should be prompted by the browser for camera/micrphone access please allow.
* You should also see video from your device's camera and hear audio from the microphone
* You should see some console log, if things are working property
  * If you see errors your [client token has expired and you need to regenerate it.](#generate-a-client-token)

**From the callee's app**

* Click the call button
* Notice in the caller's app a stream subscription was logged
* The callee's video/audio stream is rendered.


## Related Pages

- [JavaScript quickstart](../reference/javascript-quickstart.md)
