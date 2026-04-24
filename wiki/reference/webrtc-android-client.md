---
title: WebRTC Android Client
summary: The TelnyxClient connects your application to the Telnyx backend, enabling you to make outgoing calls and handle incoming calls.
sources:
  - url: https://developers.telnyx.com/development/webrtc/android-sdk/classes/txclient/index
    content_hash: 362b770f8ef8bab107ce5e0461d1b253ff110a1bd7551cd4860a37092f8dcac0
updated_at: 2026-04-10T00:00:00Z
---

# WebRTC Android Client

The TelnyxClient connects your application to the Telnyx backend, enabling you to make outgoing calls and handle incoming calls

`TelnyxClient` is the main entry point for interacting with the Telnyx WebRTC SDK. It handles connection management, call creation, and responses from the Telnyx platform.

## Core Functionalities

* **Connection Management**: Establishes and maintains a WebSocket connection to the Telnyx RTC platform.
* **Authentication**: Supports authentication via SIP credentials or tokens.
* **Call Control**: Provides methods to initiate (`newInvite`), accept (`acceptCall`), and end (`endCall`) calls.
* **Event Handling**: Uses `TxSocketListener` to process events from the socket, such as incoming calls (`onOfferReceived`), call answers (`onAnswerReceived`), call termination (`onByeReceived`), and errors (`onErrorReceived`).
* **State Exposure**: Exposes connection status, session information, and call events via `SharedFlow` (recommended: `socketResponseFlow`) and deprecated `LiveData` (e.g., `socketResponseLiveData`) for UI consumption.

## Key Components and Interactions

* **`TxSocket`**: Manages the underlying WebSocket communication.
* **`TxSocketListener`**: An interface implemented by `TelnyxClient` to receive and process socket events. Notably:
  * `onOfferReceived(jsonObject: JsonObject)`: Handles incoming call invitations.
  * `onAnswerReceived(jsonObject: JsonObject)`: Processes answers to outgoing calls.
  * `onByeReceived(jsonObject: JsonObject)`: Handles call termination notifications. The `jsonObject` now contains richer details including `cause`, `causeCode`, `sipCode`, and `sipReason`, allowing the client to populate `CallState.DONE` with a detailed `CallTerminationReason`.
  * `onErrorReceived(jsonObject: JsonObject)`: Manages errors reported by the socket or platform.
  * `onClientReady(jsonObject: JsonObject)`: Indicates the client is ready for operations after connection and initial setup.
  * `onGatewayStateReceived(gatewayState: String, receivedSessionId: String?)`: Provides updates on the registration status with the Telnyx gateway.
* **`Call` Class**: Represents individual call sessions. `TelnyxClient` creates and manages instances of `Call`.
* **`CallState`**: The client updates the `CallState` of individual `Call` objects based on socket events and network conditions. This includes states like `DROPPED(reason: CallNetworkChangeReason)`, `RECONNECTING(reason: CallNetworkChangeReason)`, and `DONE(reason: CallTerminationReason?)` which now provide more context.
* **`socketResponseFlow: SharedFlow<SocketResponse>`**: This SharedFlow stream is the recommended approach for applications. It emits `SocketResponse` objects that wrap messages received from the Telnyx platform. For `BYE` messages, the `ReceivedMessageBody` will contain a `com.telnyx.webrtc.sdk.verto.receive.ByeResponse` which is now enriched with termination cause details.
* **`socketResponseLiveData: LiveData<SocketResponse>`**: **\[DEPRECATED]** This LiveData stream is deprecated in favor of `socketResponseFlow`. It's maintained for backward compatibility but new implementations should use SharedFlow.

## Usage Example

**Recommended approach using SharedFlow:**

```kotlin theme={null}
// Initializing the client
val telnyxClient = TelnyxClient(context)

// Observing responses using SharedFlow (Recommended)
lifecycleScope.launch {
    telnyxClient.socketResponseFlow.collect { response ->
        when (response.status) {
            SocketStatus.MESSAGERECEIVED -> {
                response.data?.let {
                    when (it.method) {
                        SocketMethod.INVITE.methodName -> {
                            val invite = it.result as InviteResponse
                            // Handle incoming call invitation
                        }
                        SocketMethod.BYE.methodName -> {
                            val bye = it.result as com.telnyx.webrtc.sdk.verto.receive.ByeResponse
                            // Call ended by remote party, bye.cause, bye.sipCode etc. are available
                            Log.d("TelnyxClient", "Call ended: ${bye.callId}, Reason: ${bye.cause}")
                        }
                        // Handle other methods like ANSWER, RINGING, etc.
                    }
                }
            }
            SocketStatus.ERROR -> {
                // Handle errors
                Log.e("TelnyxClient", "Error: ${response.errorMessage}")
            }
            // Handle other statuses: ESTABLISHED, LOADING, DISCONNECT
        }
    }
}
```

**Deprecated approach using LiveData:**

```kotlin theme={null}
@Deprecated("Use socketResponseFlow instead. LiveData is deprecated in favor of Kotlin Flows.")
// Observing responses (including errors and BYE messages)
telnyxClient.socketResponseLiveData.observe(lifecycleOwner, Observer { response ->
    when (response.status) {
        SocketStatus.MESSAGERECEIVED -> {
            response.data?.let {
                when (it.method) {
                    SocketMethod.INVITE.methodName -> {
                        val invite = it.result as InviteResponse
                        // Handle incoming call invitation
                    }
                    SocketMethod.BYE.methodName -> {
                        val bye = it.result as com.telnyx.webrtc.sdk.verto.receive.ByeResponse
                        // Call ended by remote party, bye.cause, bye.sipCode etc. are available
                        Log.d("TelnyxClient", "Call ended: ${bye.callId}, Reason: ${bye.cause}")
                    }
                    // Handle other methods like ANSWER, RINGING, etc.
                }
            }
        }
        SocketStatus.ERROR -> {
            // Handle errors
            Log.e("TelnyxClient", "Error: ${response.errorMessage}")
        }
        // Handle other statuses: ESTABLISHED, LOADING, DISCONNECT
    }
})

// Connecting and Logging In (example with credentials)
telnyxClient.connect(
    credentialConfig = CredentialConfig(
        sipUser = "your_sip_username",
        sipPassword = "your_sip_password",
        // ... other config ...
    )
)

// Making a call
val outgoingCall = telnyxClient.newInvite(
    callerName = "My App",
    callerNumber = "+11234567890",
    destinationNumber = "+10987654321",
    clientState = "some_state"
)

// Observing the specific call's state
outgoingCall.callStateFlow.collect { state ->
    if (state is CallState.DONE) {
        Log.d("TelnyxClient", "Outgoing call ended. Reason: ${state.reason?.cause}")
    }
    // Handle other states
}
```

Refer to the SDK's implementation and specific method documentation for detailed usage patterns and configuration options.

## Telnyx Client

NOTE:
Remember to add and handle INTERNET, RECORD\_AUDIO and ACCESS\_NETWORK\_STATE permissions

<p>
  <img />
</p>

### Initialize

To initialize the TelnyxClient you will have to provide the application context.

```kotlin theme={null}
  telnyxClient = TelnyxClient(context)
```

### Connect

Once an instance is created, you can call the one of two available .connect(....) method to connect to the socket.

```kotlin theme={null}
fun connect(
    providedServerConfig: TxServerConfiguration = TxServerConfiguration(),
    credentialConfig: CredentialConfig,
    txPushMetaData: String? = null,
    autoLogin: Boolean = true,
)
```

Connects to the socket by credential and using this client as the listener. Will respond with 'No Network Connection' if there is no network available
Parameters:

* providedServerConfig, the TxServerConfiguration used to connect to the socket
* txPushMetaData, the push metadata used to connect to a call from push (Get this from push notification - fcm data payload) required fot push calls to work
* credentialConfig, represents a SIP user for login - credential based
* autoLogin, if true, the SDK will automatically log in with the provided credentials on connection established. We recommend setting this to true.

```kotlin theme={null}
fun connect(
        providedServerConfig: TxServerConfiguration = TxServerConfiguration(),
        tokenConfig: TokenConfig,
        txPushMetaData: String? = null,
        autoLogin: Boolean = true,
    )
```

Connects to the socket by token and using this client as the listener. Will respond with 'No Network Connection' if there is no network available

* providedServerConfig, the TxServerConfiguration used to connect to the socket
* txPushMetaData, the push metadata used to connect to a call from push (Get this from push notification - fcm data payload) required fot push calls to work
* tokenConfig, represents a SIP user for login - token based
* autoLogin, if true, the SDK will automatically log in with the provided credentials on connection established. We recommend setting this to true.

**Note:** **tokenConfig** and **credentialConfig** are data classes that represent login settings for the client to use. They belong to **TelnyxConfig** and can be found in Data part.

### Listening for events and reacting

We need to react for a socket connection state or incoming calls. We do this by getting the Telnyx Socket Response callbacks from our TelnyxClient.

**Recommended approach using SharedFlow:**

```kotlin theme={null}
val socketResponseFlow: SharedFlow<SocketResponse>
```

Returns the socket response in the form of SharedFlow (Kotlin Flows). The format of each message is provided in `SocketResponse` and `ReceivedMessageBody`.

* @see \[SocketResponse]
* @see \[ReceivedMessageBody]

**Deprecated approach using LiveData:**

```kotlin theme={null}
@Deprecated("Use socketResponseFlow instead. LiveData is deprecated in favor of Kotlin Flows.")
fun getSocketResponse(): LiveData<SocketResponse> = socketResponseLiveData
```

Returns the socket response in the form of LiveData. The format of each message is provided in `SocketResponse` and `ReceivedMessageBody`.

* @see \[SocketResponse]
* @see \[ReceivedMessageBody]

Response can be observed by implementation of abstract class `SocketObserver`.
In `onMessageReceived` we will receive objects of `ReceivedMessageBody` class.

```kotlin theme={null}
abstract class SocketObserver<T> : Observer<SocketResponse<T>> {

    abstract fun onConnectionEstablished()
    abstract fun onMessageReceived(data: T?)
    abstract fun onLoading()
    abstract fun onError(errorCode: Int?, message: String?)
    abstract fun onSocketDisconnect()

    override fun onChanged(value: SocketResponse<T>) {
        when (value.status) {
            SocketStatus.ESTABLISHED -> onConnectionEstablished()
            SocketStatus.MESSAGERECEIVED -> onMessageReceived(value.data)
            SocketStatus.LOADING -> onLoading()
            SocketStatus.ERROR -> onError(value.errorCode, value.errorMessage)
            SocketStatus.DISCONNECT -> onSocketDisconnect()
        }
    }
}
```


## Related Pages

- [WebRTC Android Call](../reference/webrtc-android-call.md)
- [WebRTC Android Config](../reference/webrtc-android-config.md)
- [WebRTC JS Client](../reference/webrtc-js-client.md)
- [WebRTC Android ChangeLog](../reference/webrtc-android-changelog.md)
- [WebRTC Android SocketResponse](../reference/webrtc-android-socketresponse.md)
