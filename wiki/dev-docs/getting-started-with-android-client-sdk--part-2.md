---
title: Getting Started with Android Client SDK
summary: The Telnyx Video Android SDK enables developers to add video calling to Android
  applications with minimal code, providing full functionality to join and interact
  with Telnyx Rooms. This guide covers installation, room connection, stream publishing
  and subscription, observables for UI updates, and WebRTC stats retrieval.
sources:
- url: https://developers.telnyx.com/docs/video/android-client-sdk
updated_at: 2026-08-05T14:02:07Z
---

# Getting Started with Android Client SDK

*Part 2 of 3 — see also: [Part 1](getting-started-with-android-client-sdk--part-1.md), [Part 3](getting-started-with-android-client-sdk--part-3.md)*

The Telnyx Video Android SDK enables developers to add video calling to Android applications with minimal code, providing full functionality to join and interact with Telnyx Rooms. This guide covers installation, room connection, stream publishing and subscription, observables for UI updates, and WebRTC stats retrieval.

## Video/Audio Observables

The Telnyx Video SDK for Android works with mutable live data. All the information needed to build your UI is provided through **observables** that contain the most up-to-date information of the state of the room, such as current participant list, talking events, stream information, participants added, and participants leaving.

### State Observable

```kotlin
room.getStateObservable()
// MutableLiveData<State>
```

This observable provides the current state of a room at any given moment. The `State` object contains:

```kotlin
data class State(
    val action: String,
    val status: String,
    val participants: List<Participant>,
    val streams: HashMap<Long, Stream>,
    val publishers: List<Publisher>,
    val subscriptions: List<Subscription>
)
```

**action** — `val action: String` is the cause of the latest change of State:

```kotlin
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

**status** — `val status: String` is the status of the Room session when that action happened:

```kotlin
enum class Status(val status: String) {
    INITIALIZED("initialized"),
    CONNECTING("connecting"),
    CONNECTED("connected"),
    DISCONNECTING("disconnecting"),
    DISCONNECTED("disconnected")
}
```

**participants** — `val participants: List<Participant>` is the list of participants present in a room. A `Participant` is a UI representation in variables for an attendee of the room session:

```kotlin
data class Participant(
    var id: Long,
    val participantId: String,
    var externalUsername: String? = null,
    val isSelf: Boolean,
    var streams: MutableList<ParticipantStream> = mutableListOf(),
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

**streams** — `val streams: HashMap<Long, Stream>` contains a track of the currently available streams and the **id** of the **publisher** streaming them. A stream contains tracks for video, audio, or both:

```kotlin
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

**publishers** — `val publishers: List<Publisher>` tracks all publishers in the room. A `Publisher` is an instance of an attendee or participant sharing some stream content in the room. A single participant sharing multiple streams can be linked to multiple publisher ids:

```kotlin
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

**subscriptions** — `val subscriptions: List<Subscription>` tracks all subscriptions. Each time a publisher starts streaming information, you have the option to subscribe or unsubscribe:

```kotlin
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

### Event observables

Some observables have a `MutableLiveData` of `Event`. `Event` is a wrapper of `LiveData` that ensures we only handle an observable once, no matter how many times we set to observe it. If the contents have already been handled, we won't get that content again, unless we call `peekContent()` instead:

```kotlin
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

### Participants Observable

```kotlin
room.getParticipantsObservable()
// MutableLiveData<MutableList<Participant>>
```

This mutable list is received as soon as you join a Room session and contains a list of the participants already present in the room, including yourself. The SDK keeps this list updated but won't post the changes, so this observer won't be fired again. By receiving this list you can initialize a recycler adapter to show participants:

```kotlin
roomsViewModel.getParticipants().observe(viewLifecycleOwner) { participants ->
    participants.let { participantList ->
        participantAdapter.setData(participantList)
        if (participantList.size > 0) {
            selfParticipantId = participantList[0].participantId
            selfParticipantHandleId = participantList[0].id
        }
    }
}
```

### Joined Room Observable

```kotlin
room.getJoinedRoomObservable()
// MutableLiveData<Event<RoomUI>>
```

This mutable fires an event as soon as you have connected to a room and retrieved an *initial* list of participants. It is useful when you want to update the UI as soon as you have joined the room successfully. This differs from `Status.CONNECTED`, which is issued when you have successfully joined your plugins to handle session audio.

### Joined Participant Observable

```kotlin
room.getJoinedParticipant()
// MutableLiveData<Event<Participant>>
```

You receive the participant that has joined the room after the client has already joined. You can add this reference to the list used in your adapter:

```kotlin
roomsViewModel.getJoinedParticipant().observe(viewLifecycleOwner) { participantJoined ->
    participantJoined?.let { joinedParticipantEvent ->
        joinedParticipantEvent.getContentIfNotHandled()?.let {
            participantsAdapter.addParticipant(it)
        }
    }
}
```

### Leaving participant id Observable

```kotlin
room.getLeavingParticipantId()
// MutableLiveData<Pair<Long, String>>
```

You receive the publisherId that has left the room, and a reason for its exit ("Left" or "Kicked"):

```kotlin
roomsViewModel.getLeavingParticipantId()
    .observe(viewLifecycleOwner) { participantLeavingId ->
        participantLeavingId?.let { (id, reason) ->
            participantAdapter.removeParticipant(id)
            if (id == selfParticipantHandleId && reason == "kicked") {
                // It's ourselves, remove from the room.
                goBack(wasKicked = true)
                Toast.makeText(requireContext(), "You were kicked!", Toast.LENGTH_LONG).show()
            }
        }
    }
}
```

### Connected to room Observable

```kotlin
room.getConnectionStatus()
// LiveData<Boolean>
```

Receives `true` when you have opened a webSocket and connected to the room:

```kotlin
roomsViewModel.connectedToRoomObservable().observe(this.viewLifecycleOwner) {
    it?.let { isConnected ->
        if (isConnected) {
            buttonCreateRoom.isEnabled = true
        }
    }
}
```

### Participant stream changed Observable

```kotlin
room.getParticipantStreamChanged()
// MutableLiveData<Event<Participant>>
```

You receive an event with the participant that has recently changed its video and/or audio stream status. The mutable list of participants is also updated with this change, but here the specific individual is received.

### Stream status

```kotlin
enum class StreamStatus(val request: String) {
    UNKNOWN("unknown"),
    ENABLED("enabled"),
    DISABLED("disabled")
}
```

These statuses apply for audio, video, and shared screen:

- **UNKNOWN**: initial status. No information on whether this participant is sharing audio/video/screen.
- **ENABLED**: the participant is sharing audio/video/screen and you can subscribe to a stream for it.
- **DISABLED**: the participant is not sharing audio/video/screen. If you were subscribed to that participant's audio/video/screen, you can unsubscribe from it.
