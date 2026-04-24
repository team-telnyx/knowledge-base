---
title: Getting Started with Android Client SDK
summary: Telnyx's Android client SDK is simple to use and makes it easy to get started with video calling.
sources:
  - url: https://developers.telnyx.com/docs/video/android-client-sdk/index
    content_hash: 5fdaac02a6e119f00fd674e580e92ef18995a3151300cdfed304b3d521fd27b1
updated_at: 2026-04-10T00:00:00Z
---

# Getting Started with Android Client SDK

Telnyx's Android client SDK is simple to use and makes it easy to get started with video calling. With this SDK, you can easily add video calling to your app with just a few lines of code.

The Telnyx Video Android SDK is simple to use and makes it easy to get started with video calling. With this SDK, you can easily add video calling to your app with just a few lines of code.

It provides all the functionality you need to join and interact with a Telnyx Room from an Android application.

#### A link to the repo can be found here:

<a href="https://github.com/team-telnyx/telnyx-video-android">Android SDK</a>

## Project structure

* SDK project: sdk module, containing all Telnyx SDK components as well as tests.
* Demo application: app module, containing a sample demo application utilizing the sdk module.

## Adding the SDK to your Android client application

Add Jitpack.io as a repository within your root level build file:

```
allprojects {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
}
```

Add the dependency within the app level build file:

```
dependencies {
    implementation 'com.github.team-telnyx:telnyx-video-android:<tag>'
}
```

Tag should be replaced with the release version.

Then, import the TelnyxVideo SDK into your application code at the top of the class:

```
import com.telnyx.video.sdk.*
```

The '\*' symbol will import the whole SDK which will then be available for use within that class.

<Callout type="info">
  Remember to add and handle INTERNET, RECORD\_AUDIO and ACCESS\_NETWORK\_STATE permissions in order to properly use the SDK.

```
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.CAMERA"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
```

## Before connecting to a Room

## Get an API Key

You'll need an API key which is associated with your Mission Control Portal account under **API Keys**. You can learn how to do that [here](../reference/create-and-manage-api-keys.md).

An API key is your credential to access our API. It allows you to:

* to authenicate to the Rest API
* to manage your access tokens

## Create a Room to join (if it doesn't exist)

In order to join a room you must create it, if it doesn't already exist. See our [Room Rest API](https://developers.telnyx.com/api-reference/rooms/view-a-list-of-rooms) to create one.

There's also additional resources on other endpoints available to perform basic operations on a `Room`.

## Generate an a client token to join a room

In order to join a room you must have a client token for that `Room`. The `client token` is short lived and you will be able to refresh it using the `refresh token` provided with it when you  request a `client token`.

Please see the [docs here](https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) to learn how to create a `client token`.

Now you are ready to connect to a video room that you previously created using the REST API.

## Connect to Room

To connect, you'll need to provide a **participantName** that will identify your user in that room.

You'll also need to provide an instance of *ExternalData* that will contain a *username* of type String and an Integer *id*. You will also provide your Android application's context in **context**

```
room = Room(
    context = context,
    roomId = UUID.fromString(roomId),
    roomToken = tokenInfo.token,
    externalData = ExternalData(id = 1234, username = "Android Participant")
    enableMessages = false
)
...

...
room.connect()

```

## Publish video/audio stream

To publish as video or audio stream, we will need an instance of *PublishConfigHelper* with the *application context*, camera *direction*, *streamKey* (unique for each stream published), and *streamId* (unique for each stream published)

```java theme={null}
//AUDIO
publishConfigHelper =
        PublishConfigHelper(
            context = requireContext(),
            direction = CameraDirection.FRONT,
            streamKey = SELF_STREAM_KEY // a key to identify this stream i.e: "self"
            streamId = SELF_STREAM_ID // RANDOM id to this stream i.e: "qlkj323kj423"
        )
    publishConfigHelper.createAudioTrack(true, // isTrackEnabled?
                                        AUDIO_TRACK_KEY // i.e: "myMic", "002"
                                        )
...

...
room.addStream(publishConfigHelper) // This stream is new. addStream() is called.
```

New streams can be created via the PublishConfigHelper class for both audio and video. They can be created together or added later independently.

```java theme={null}
//VIDEO

//NOTE: in this case, video is published in the same stream as above
publishConfigHelper.setSurfaceView(selfSurfaceRenderer) //Provide SurfaceRenderer

publishConfigHelper.createVideoTrack(
            CapturerConstraints.WIDTH.value,// i.e: 1280
            CapturerConstraints.HEIGHT.value,// i.e: 720
            CapturerConstraints.FPS.value, //i.e: 30 (fps)
            true, // isTrackEnabled?
            VIDEO_TRACK_KEY //i.e: i.e "cameraFeed", "001"
        )
...

...
room.updateStream(publishConfigHelper) // Stream already created, therefore updateStream is called.
```

<Callout type="info">
  Since stream is already created, it is only necessary to add the video track to PublishConfigHelper, and "update" the stream.

## Remove video/audio track

To remove a video or audio track, publishConfigHelper has to be modified in order to remove the unwanted track

````java theme={null}
//Considering publishConfigHelper is the same instance as above

publishConfigHelper?.let {
            it.stopCapture()   //In case of video, we "stop the capture", update the stream, and release the surface
            roomsViewModel.updateStream(it)
            selfSurface?.let { surface -> it.releaseSurfaceView(surface) }
        }
...

```java
publishConfigHelper?.let {
            it.disposeAudio()    //In case of audio, we "dispose" audio and update the stream.
            roomsViewModel.updateStream(it)
        }
````

## Remove stream

By removing the stream, we will remove all tracks added to it.

```java theme={null}
room.removeStream(SELF_STREAM_KEY) // a key to identify this stream i.e: "self"
```

## Video/Audio Observables

The Telnyx Video SDK for android works with mutable live data, and all the information you need to build your UI is provided through **observables** that will contain the most up to date information of the state of the room, such as **current participant list**, **talking events**, **stream information**, **participants added**, **participants leaving**, etc

## State Observable

```java theme={null}
    room.getStateObservable()
    // MutableLiveData
```

This observable will provide the current state of a room at any given moment.
We will receive a State object that will contain:

```java theme={null}
data class State(
    val action: String,
    val status: String,
    val participants: List,
    val streams: HashMap<Long, Stream>,
    val publishers: List,
    val subscriptions: List
)
```

**action** -> \`\`val action: String\`
is the cause of the latest change of State

```java theme={null}
enum class StateAction(val action: String) {
    INITIALIZING_ROOM("initializing room"),
    STATUS_CHANGED("status changed"),
    ADD_PARTICIPANT("add participant"),
    REMOVE_PARTICIPANT("remove participant"),
    ADD_STREAM("add stream"),
    REMOVE_STREAM("remove stream"),
    ADD_SUBSCRIPTION("add subscription"),
    UPDATE_SUBSCRIPTION("update subscription"),
    REMOVE_SUBSCRIPTION("remove subscription"),
    PUBLISH("publish"),
    UNPUBLISH("unpublish"),
    UPDATE_PUBLISHED_STREAM("update published stream"),
    AUDIO_ACTIVITY("audio activity")
}
```

**status** -> `val status: String`
is the status of the Room session, when that action happened

<a />

```java theme={null}
enum class Status(val status: String) {
    INITIALIZED("initialized"),
    CONNECTING("connecting"),
    CONNECTED("connected"),
    DISCONNECTING("disconnecting"),
    DISCONNECTED("disconnected")
}
```

**participants** -> `val participants: List` <a />
is the list of participants present in a room. A Participant is a UI representation in variables, for an attendee to the room session.

<a />

```java theme={null}
data class Participant(
    var id: Long,
    val participantId: String,
    var externalUsername: String? = null,
    val isSelf: Boolean,
    var streams: MutableList = mutableListOf(),
    var isTalking: String?,
    var isAudioCensored: Boolean? = false,
    var audioBridgeId: Long? = null,
    var canReceiveMessages: Boolean = false
) : Serializable

data class ParticipantStream(
    val publishingId: Long? = null,
    var streamKey: String? = null,
    var audioEnabled: StreamStatus = StreamStatus.UNKNOWN,
    var videoEnabled: StreamStatus = StreamStatus.UNKNOWN,
    var audioTrack: AudioTrack? = null,
    var videoTrack: VideoTrack? = null
)

enum class StreamStatus(val request: String) {
    UNKNOWN("unknown"),
    ENABLED("enabled"),
    DISABLED("disabled")
}

```

**streams** -> `val streams: HashMap<Long, Stream>`
this hash map, contains a track of the currently available streams and the **id** of the **publisher** streaming them.
A stream, will contain tracks for video, audio or both.

```java theme={null}
data class Stream(
    val id: String,
    val key: String,
    val participantId: String,
    val origin: String,
    var isAudioEnabled: Boolean? = null,
    var isVideoEnabled: Boolean? = null,
    var isAudioCensored: Boolean? = null,
    var isVideoCensored: Boolean? = null
)
```

**publishers** -> `val publishers: List`

This will track all publishers in the room. A Publisher is an instance of an attendee or participant sharing some stream content in the room.

<Callout type="info">
  A single Participant, sharing multiple streams can be also linked to multiple Publisher ids.

```java theme={null}
data class Publisher(
    val audio_codec: String?,
    val video_codec: String?,
    val display: String, // see DisplayParameters.kt
    val id: Long,
    val talking: Boolean,
    val audio_moderated: Boolean? // aka Censored
)

data class DisplayParameters(
    val participantId: String,
    val telephonyEngineParticipant: Boolean? = null,
    val external: String? = null,
    val stream: StreamData? = null,
    val canReceiveMessages: Boolean? = null
)
```

**subscriptions** -> `val subscriptions: List`

Each time a publisher starts streaming information, we will have the option of subscribe/unsubscribe to/from it. This list will track all the subscriptions.

```java theme={null}
data class Subscription(
    var publisherId: Long,
    var status: SubscriptionStatus
)

enum class SubscriptionStatus(val status: String) {
    NEVER_REQUESTED("never_requested"),
    PENDING("pending"),
    STARTED("started"),
    PAUSED("paused")
}

```

## Event observables

Some observables will have a MutableLiveData of Event. Event is a wrapper of LiveData, and provide the means to ensure we only handle an observable once, no matter how many times we're set to observe it.
If the contents have already been handled, we won't get that content again, unless we *peekContent()* instead.

```java theme={null}
/**
 * Used as a wrapper for data that is exposed via a LiveData that represents an event.
 */
open class Event<out T>(private val content: T) {

    var hasBeenHandled = false
        private set // Allow external read but not write

    /**
     * Returns the content and prevents its use again.
     */
    fun getContentIfNotHandled(): T? {
        return if (hasBeenHandled) {
            null
        } else {
            hasBeenHandled = true
            content
        }
    }

    /**
     * Returns the content, even if it's already been handled.
     */
    fun peekContent(): T = content
}
```

## Participants Observable

```java theme={null}
room.getParticipantsObservable()
// MutableLiveData<MutableList>
```

This mutable list will be received as soon as we join a Room session, and contains a list of the participants already present in the room, including yourself. The SDK will keep this list updated but won't post the changes, so this observer won't be fired again. See [Participant](#participant-header)

By receiving this list we can initialize a recycler adapter in order to show participants:

```java theme={null}
roomsViewModel.getParticipants().observe(viewLifecycleOwner) { participants ->
	participants.let { participantList ->
		participantAdapter.setData(participantList)
		if (participantList.size > 0){
			selfParticipantId = participantList[0].participantId
			selfParticipantHandleId = participantList[0].id
		}
	}
}
```

## Joined Room Observable

```java theme={null}
    room.getJoinedRoomObservable()
    // MutableLiveData<Event>
```

This mutable will fire an event as soon as we have connected to a room, and we have retrieved an *initial* list of [Participants](#participant-header)

It is useful when we want to update UI as soon as we have joined the room sucessfully.

<Callout type="info">
  This will be different to Status-CONNECTED that will be issued when we have successfully joined our plugins to handle session audio. See [Status](#status-header).

## Joined Participant Observable

```java theme={null}
    room.getJoinedParticipant()
    //MutableLiveData<Event>
```

We receive the participant that has joined the room after client has already joined.
We can add the this reference to the list used in our adapter as:

```java theme={null}
roomsViewModel.getJoinedParticipant().observe(viewLifecycleOwner) { participantJoined ->
	participantJoined?.let { joinedParticipantEvent ->
		joinedParticipantEvent.getContentIfNotHandled()?.let {
			participantsAdapter.addParticipant(it)
		}
	}
}
```

## Leaving participant id Observable

```java theme={null}
    room.getLeavingParticipantId()
    //MutableLiveData<Pair<Long, String>>
```

We receive the publisherId that has leaved the room, and a reason for its exit ("Left" or "Kicked").

```java theme={null}
roomsViewModel.getLeavingParticipantId()
    .observe(viewLifecycleOwner) { participantLeavingId ->
        participantLeavingId?.let { (id, reason) ->
            participantAdapter.removeParticipant(id)
            if (id == selfParticipantHandleId && reason == "kicked") {
                //It's ourselves, remove from the room.
                goBack(wasKicked = true)
                Toast.makeText(requireContext(), "You were kicked!", Toast.LENGTH_LONG).show()
            }
        }
    }
}
```

## Connected to room Observable

```java theme={null}
    room.getConnectionStatus()
    //LiveData
```

Receive true when we have opened a webSocket and connected to the room

```java theme={null}
roomsViewModel.connectedToRoomObservable().observe(this.viewLifecycleOwner) {
    it?.let { isConnected ->
        if (isConnected) {
            buttonCreateRoom.isEnabled = true
        }
    }
}
```

## Participant stream changed Observable

```java theme={null}
    room.getParticipantStreamChanged()
    //MutableLiveData<Event>
```

We will receive here an event with the participant that has recently changed its video and/or audio stream status. Mutable list of participants will also be updated with this change, but here the specific individual is received.

## Stream status

```java theme={null}
enum class StreamStatus(val request: String) {
    UNKNOWN("unknown"),
    ENABLED("enabled"),
    DISABLED("disabled")
}
```

These status apply for audio, video and shared screen:

***UNKNOWN*** : initial status. We don't have information on whether this participant is sharing audio/video/screen

***ENABLED*** : the participant is sharing audio/video/screen and we can subscribe to a stream for it like:

***DISABLED*** : the participant is not sharing audio/video/screen. If we were subscribed to that participant audio/video/screen we can unsubscribe from it.

## Subscribe to a video stream

In order to subscribe to a **video stream**, there are 3 actions that needs to be performed:

```java theme={null}
StreamStatus.ENABLED -> {
    // This notifies the WebRTC connection we're ready to receive stream information
    participantTileListener.subscribeTileToStream(model.participantId, "self")

    itemView.participant_tile_surface.visibility = View.VISIBLE
    itemView.participant_tile_place_holder.visibility = View.GONE

    // This ensures surfaces are initialized in an EglContext provided inside WebRTC connection
    participantTileListener.notifyTileSurfaceId(
        itemView.participant_tile_surface,
        model.participantId,
        "self"
    )

    model.streams.find { it.streamKey == "self" }?.videoTrack?.let {
        if (viewHolderMap[holder] != it) {  // NOTE: keep a map of surfaces to release

            // Updates only if previous register differs from what we need
            viewHolderMap[holder]?.removeSink(holder.itemView.participant_tile_surface)
            holder.itemView.participant_tile_surface.release()
            viewHolderMap[holder] = it

            it.addSink(itemView.participant_tile_surface)
            it.setEnabled(true)
        }
    }
}
```

1 Provide the SDK with the same instance of *SurfaceViewRenderer* you want to *init*:

```java theme={null}
    room.setParticipantSurface(
        participantId: String,
        surface: SurfaceViewRenderer,
        streamKey: String //Stream key to indentify the webrtc connection to init this surface
    )
```

This will use the proper **WebRTC Connection** to provide an *EglContext* for the surface to be *init*

2 Use method *addSink()* to add a *SurfaceViewRenderer* instance to the videoTrack provided for a [Participant](#participant-header), and set that track to enable *videoTrack?.setEnabled(true)*

3 Subscribe to the stream a participant is providing

```java theme={null}

    participantTileListener.subscribeTileToStream(model.participantId, "self")

    // Eventually calls:

    room.addSubscription(
        participantId: String,
        streamKey: String,
        streamConfig: StreamConfig,
    )
```

*participantId* is the participant id that uniquely identifies a single participant in the room

*streamKey* i.e: "SharingSubscriptions" "CameraSubscriptions"

*streamConfig* whether we want to subscribe to audio/video or both. By default we will attempt both.

## Remove subscription to a \*video stream

To remove a subscription we need to issue

```java theme={null}
    room.removeSubscription(participantId: String, streamKey: String)
```

A good practice when handling surfaces is to make sure you remove this surface properly from the rendering context before eliminating or removing the surface from the UI:

```
    // Here, order is important
    videoTrack.removeSink(surfaceViewRenderer)
    surfaceViewRenderer.release()

```

## Participant Talking Observable

```java theme={null}
    room.getParticipantTalking()
    MutableLiveData<Pair<Participant, String?>>
```

We will receive the participant that has updated its talking status, and the stream key. This information is also modified in the [Participants list](#participants-observable)

```java theme={null}
data class Participant(
...
    var isTalking: String?, // Can either be "talking" or "stopped-talking"
...
) : Serializable
```

## Stats

We provide the method *getWebRTCStatsForStream()* to retrieve WebRTC stats
This request brings stats one time only, so if you want to keep receiving stats, you will need to use some sort of runnable or coroutine to recursively request for them such as:

```java theme={null}
mStatsjob = CoroutineScope(Dispatchers.Default).launch {
        while (isActive) {
            room.getWebRTCStatsForStream(participantId, streamKey, callback)
            delay(2000)
    }
```

We have to provide *participantId*, *streamKey* that is the key that identifies the stream we need the stats from, and *callback* that is an **RTCStatsCollectorCallback** we provide to the WebRTC peer connection in order to retrieve the stats.

In Kotlin, method call will look like this

```java theme={null}

room.getWebRTCStatsForStream(participantId, streamKey) { stats ->
    ...
    ...
}
```

We can later parse the information retrieved to obtain the specific information we go after.
In our sample app, you will see the models we use for audio and video, both local and remote

## Remote Video stats

WEBRTC's *RTCStatsReport* can be parsed and mapped to RemoteVideoStreamStats

```java theme={null}
data class RemoteVideoStreamStats(
    val bytesReceived: Int,
    val frameHeight: Int,
    val frameWidth: Int,
    val framesDecoded: Int,
    val framesDropped: Int,
    val framesPerSecond: Double,
    val framesReceived: Int,
    val packetsLost: Int,
    val packetsReceived: Int,
    val totalInterFrameDelay: Double
) : StreamStats()
```

```java theme={null}
stats.statsMap.values.filter { it.type == "inbound-rtp" }
    .findLast { it.toString().contains("mediaType: \"video\"") }
    ?.let { rtcVideoStats ->
        val videoStreamStats =
            gson.fromJson(
                rtcVideoStats.toString(),
                RemoteVideoStreamStats::class.java
            )
        videoStreamStats?.let {
            Timber.tag("RoomFragment")
                .d("ParticipantID: $participantId video STATS: $it")
            // Proceed to use stats
        }
    }
```

## Local Video stats

WEBRTC's *RTCStatsReport* can be parsed and mapped to LocalVideoStreamStats

```java theme={null}
data class LocalVideoStreamStats(
    val bytesSent: Int,
    val codecId: String,
    val frameHeight: Int,
    val frameWidth: Int,
    val framesEncoded: Int,
    val framesPerSecond: Double,
    val framesSent: Int,
    val headerBytesSent: Int,
    val nackCount: Int,
    val packetsSent: Int,
) : StreamStats()
```

```java theme={null}
stats.statsMap.values.filter { it.type == "outbound-rtp" }
    .findLast { it.toString().contains("mediaType: \"video\"") }
    ?.let { rtcVideoStats ->
        val videoStreamStats =
            gson.fromJson(
                rtcVideoStats.toString(),
                LocalVideoStreamStats::class.java
            )
        videoStreamStats?.let {
            Timber.tag("RoomFragment")
                .d("SelfParticipant video STATS: $it")
            // Proceed to use stats
        }
    }
```

## Remote audio stats

WEBRTC's *RTCStatsReport* can be parsed and mapped to RemoteAudioStreamStats

```java theme={null}
data class RemoteAudioStreamStats(
    val audioLevel: Double,
    val bytesReceived: Int,
    val codecId: String,
    val headerBytesReceived: Int,
    val jitter: Double,
    val packetsLost: Int,
    val packetsReceived: Int,
    val totalAudioEnergy: Double,
    val totalSamplesDuration: Double,
    val totalSamplesReceived: Int,
) : StreamStats()
```

```java theme={null}
stats.statsMap.values.filter { it.type == "inbound-rtp" }
    .findLast { it.toString().contains("mediaType: \"audio\"") }
    ?.let { rtcStats ->
        val audioStreamStats =
            gson.fromJson(
                rtcStats.toString(),
                RemoteAudioStreamStats::class.java
            )
        audioStreamStats?.let {
            // Proceed to use stats
        }
    }
```

## Local audio stats

WEBRTC's *RTCStatsReport* can be parsed and mapped to LocalAudioStreamStats

```java theme={null}
data class LocalAudioStreamStats(
    val bytesSent: Int,
    val codecId: String,
    val headerBytesSent: Int,
    val packetsSent: Int,
    val retransmittedBytesSent: Int,
    val retransmittedPacketsSent: Int,
) : StreamStats()
```

```java theme={null}
stats.statsMap.values.filter { it.type == "outbound-rtp" }
    .findLast { it.toString().contains("mediaType: \"audio\"") }
    ?.let { rtcStats ->
        val audioStreamStats =
            gson.fromJson(
                rtcStats.toString(),
                LocalAudioStreamStats::class.java
            )
        audioStreamStats?.let {
            // Proceed to use stats
        }
    }
```


## Related Pages

- [Getting Started with iOS Client SDK](../runbooks/getting-started-with-ios-client-sdk.md)
- [Getting Started with Video](../runbooks/getting-started-with-video.md)
- [Getting Started with 10DLC](../tutorial/getting-started-with-10dlc.md)
- [Getting Started with JavaScript SDK for Video](../runbooks/getting-started-with-javascript-sdk-for-video.md)
- [Getting Started with Telnyx Voice API](../runbooks/getting-started-with-telnyx-voice-api.md)
