---
title: WebRTC Flutter Client
summary: The TelnyxRTC client connects your application to the Telnyx backend, enabling you to make outgoing calls and handle incoming calls.
sources:
  - url: https://developers.telnyx.com/development/webrtc/flutter-sdk/classes/txclient/index
    content_hash: 9fc0d1d2e309a57941a8a4095d131525733dc9547693a5573e6190caba87c632
updated_at: 2026-04-10T00:00:00Z
---

# WebRTC Flutter Client

The TelnyxRTC client connects your application to the Telnyx backend, enabling you to make outgoing calls and handle incoming calls

### Telnyx Client

TelnyxClient() is the core class of the SDK, and can be used to connect to our backend socket connection, create calls, check state and disconnect, etc.

Once an instance is created, you can call the .connect() method to connect to the socket with either a token or credentials (see below). An error will appear as a socket response if there is no network available:

```dart theme={null}
    TelnyxClient _telnyxClient = TelnyxClient();
```

### Logging into Telnyx Client

To log into the Telnyx WebRTC client, you'll need to authenticate using a Telnyx SIP Connection. Follow our [quickstart guide](https://developers.telnyx.com/docs/v2/webrtc/quickstart) to create **JWTs** (JSON Web Tokens) to authenticate. To log in with a token we use the connectWithToken() method. You can also authenticate directly with the SIP Connection `username` and `password` with the connectWithCredential() method:

```dart theme={null}
   _telnyxClient.connectWithToken(tokenConfig)
                    //OR
   _telnyxClient.connectWithCredential(credentialConfig)             
```

**Note:** **tokenConfig** and **credentialConfig** are simple classes that represent login settings for the client to use they extend a base Config class with shared properties. They look like this:

```dart theme={null}
/// Creates an instance of CredentialConfig which can be used to log in
///
/// Uses the [sipUser] and [sipPassword] fields to log in
/// [sipCallerIDName] and [sipCallerIDNumber] will be the Name and Number associated
/// [notificationToken] is the token used to register the device for notifications if required (FCM or APNS)
/// The [autoReconnect] flag decided whether or not to attempt a reconnect (3 attempts) in the case of a login failure with
/// legitimate credentials
class CredentialConfig extends Config {
  CredentialConfig({
     required this.sipUser,
     required this.sipPassword,
     required super.sipCallerIDName,
     required super.sipCallerIDNumber,
     super.notificationToken,
     super.autoReconnect,
     required super.debug,
     super.ringTonePath,
     super.ringbackPath,
  });

  final String sipUser;
  final String sipPassword;
}

/// Creates an instance of TokenConfig which can be used to log in
///
/// Uses the [sipToken] field to log in
/// [sipCallerIDName] and [sipCallerIDNumber] will be the Name and Number associated
/// [notificationToken] is the token used to register the device for notifications if required (FCM or APNS)
/// The [autoReconnect] flag decided whether or not to attempt a reconnect (3 attempts) in the case of a login failure with
/// a legitimate token
class TokenConfig extends Config {
  TokenConfig({
     required this.sipToken,
     required super.sipCallerIDName,
     required super.sipCallerIDNumber,
     super.notificationToken,
     super.autoReconnect,
     required super.debug,
     super.ringTonePath,
     super.ringbackPath,
  });

  final String sipToken;
}
```

### Listening for events and reacting - Accepting a Call

In order to be able to accept a call, we first need to listen for invitations. We do this by getting the Telnyx Socket Response callbacks from our TelnyxClient:

```dart theme={null}
 // Observe Socket Messages Received
_telnyxClient.onSocketMessageReceived = (TelnyxMessage message) {
  switch (message.socketMethod) {
        case SocketMethod.CLIENT_READY:
        {
           // Fires once client has correctly been setup and logged into, you can now make calls. 
           break;
        }
        case SocketMethod.LOGIN:
        {
            // Handle a successful login - Update UI or Navigate to new screen, etc. 
            break;
        }
        case SocketMethod.INVITE:
        {
            // Handle an invitation Update UI or Navigate to new screen, etc. 
            // Then, through an answer button of some kind we can accept the call with:
            // This will return an instance of the Call class which can be used to interact with the call or monitor it's state.
            _incomingInvite = message.message.inviteParams;
            _call = _telnyxClient.acceptCall(
                _incomingInvite, "callerName", "000000000", "State");
            break;
        }
        case SocketMethod.ANSWER:
        {
           // Handle a received call answer - Update UI or Navigate to new screen, etc.
          break;
        }
        case SocketMethod.BYE:
        {
           // Handle a call rejection or ending - Update UI or Navigate to new screen, etc.
           break;
      }
    }
};
```


## Related Pages

- [WebRTC Flutter Call](../reference/webrtc-flutter-call.md)
- [WebRTC JS Client](../reference/webrtc-js-client.md)
- [WebRTC Flutter ChangeLog](../reference/webrtc-flutter-changelog.md)
- [WebRTC Flutter Client Configuration](../reference/webrtc-flutter-client-configuration.md)
- [WebRTC Android Client](../reference/webrtc-android-client.md)
