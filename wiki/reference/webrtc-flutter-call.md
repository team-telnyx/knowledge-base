---
title: WebRTC Flutter Call
summary: A Call is the representation of an audio or video call between two devices, SIP clients or phone numbers.
sources:
  - url: https://developers.telnyx.com/development/webrtc/flutter-sdk/classes/call/index
    content_hash: f0b2a29ba9ee26b743247ea16a361296a04306687dd0be080c226ab83dfe2a3f
updated_at: 2026-04-10T00:00:00Z
---

# WebRTC Flutter Call

A Call is the representation of an audio or video call between two devices, SIP clients or phone numbers.

### Call

The Call class is used to manage the call state and call actions. It is used to accept, decline, end, mute, hold, and send DTMF tones during a call.

### Accept Call

In order to accept a call, we simply retrieve the instance of the call and use the .acceptCall(callID) method:

```dart theme={null}
    _telnyxClient.call.acceptCall(_incomingInvite?.callID);
```

### Decline / End Call

In order to end a call, we can get a stored instance of Call and call the .endCall(callID) method. To decline an incoming call we first create the call with the .createCall() method and then call the .endCall(callID) method:

```dart theme={null}
    if (_ongoingCall) {
      _telnyxClient.call.endCall(_telnyxClient.call.callId);
    } else {
      _telnyxClient.createCall().endCall(_incomingInvite?.callID);
    }
```

### DTMF (Dual Tone Multi Frequency)

In order to send a DTMF message while on a call you can call the .dtmf(callID, tone), method where tone is a String value of the character you would like pressed:

```dart theme={null}
    _telnyxClient.call.dtmf(_telnyxClient.call.callId, tone);
```

### Mute a call

To mute a call, you can simply call the .onMuteUnmutePressed() method:

```dart theme={null}
    _telnyxClient.call.onMuteUnmutePressed();
```

### Toggle loud speaker

To toggle loud speaker, you can simply call .enableSpeakerPhone(bool):

```dart theme={null}
    _telnyxClient.call.enableSpeakerPhone(true);
```

### Put a call on hold

To put a call on hold, you can simply call the .onHoldUnholdPressed() method:

```dart theme={null}
    _telnyxClient.call.onHoldUnholdPressed();
```


## Related Pages

- [WebRTC Flutter Client](../reference/webrtc-flutter-client.md)
- [WebRTC Flutter ChangeLog](../reference/webrtc-flutter-changelog.md)
- [WebRTC JS Call](../reference/webrtc-js-call.md)
- [WebRTC Android Call](../reference/webrtc-android-call.md)
- [WebRTC Flutter SDK Error Handling](../reference/webrtc-flutter-sdk-error-handling.md)
