---
title: Telnyx WebRTC Voice SDK
summary: The Telnyx WebRTC Voice SDK enables client-side applications to instantiate
  and control a Telnyx call leg using native WebRTC APIs, eliminating the need for
  traditional SIP UAs. Available for JavaScript, iOS, Android, and Flutter, the SDKs
  handle signaling via JSON-RPC over Secure WebSocket and media via SRTP, authenticating
  through credential-based SIP connections or JWTs and leveraging Telnyx's full Programmable
  Voice platform for call orchestration.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/architecture
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
updated_at: 2026-06-11T10:48:20Z
---

# Telnyx WebRTC Voice SDK

*Part 2 of 3 — see also: [Part 1](telnyx-webrtc-voice-sdk--part-1.md), [Part 3](telnyx-webrtc-voice-sdk--part-3.md)*

The Telnyx WebRTC Voice SDK enables client-side applications to instantiate and control a Telnyx call leg using native WebRTC APIs, eliminating the need for traditional SIP UAs. Available for JavaScript, iOS, Android, and Flutter, the SDKs handle signaling via JSON-RPC over Secure WebSocket and media via SRTP, authenticating through credential-based SIP connections or JWTs and leveraging Telnyx's full Programmable Voice platform for call orchestration.

## Client Instantiation and Connection

The SDK client is instantiated with an `IClientOptions` object and connected via the `connect()` method:

```js
const client = new TelnyxRTC({ login: 'xxx', password: 'yyy' });
client.connect();
```

### IClientOptions Properties

| Property | Type | Description |
|---|---|---|
| `login` | `string` | Username for SIP Connection auth. Takes precedence over `login_token`. |
| `password` | `string` | Password for SIP Connection auth. |
| `login_token` | `string` | JWT for SIP Connection auth (recommended strategy). |
| `anonymous_login` | `object` | Anonymous login options (`target_id`, `target_type`, `target_params?`, `target_version_id?`). Currently supports `ai_assistant` target type. |
| `iceServers` | `RTCIceServer[]` | ICE servers for all calls. Overrides defaults. |
| `forceRelayCandidate` | `boolean` | Force relay ICE candidate. |
| `prefetchIceCandidates` | `boolean` | Enable/disable ICE candidate prefetching. Defaults to `true`. |
| `trickleIce` | `boolean` | Enable/disable Trickle ICE. |
| `keepConnectionAliveOnSocketClose` | `boolean` | Keep peer connection alive when WebSocket closes unexpectedly (network interruption, device sleep). |
| `mediaPermissionsRecovery` | `object` | Configuration for recovering media permissions on inbound calls. Contains `enabled`, `timeout` (ms, recommended max 25000), `onSuccess?`, `onError?`. When enabled and `getUserMedia` fails on answer, a recoverable `telnyx.error` event is emitted with `resume()` and `reject()` callbacks. |
| `debug` | `boolean` | Enable debug mode (gathers WebRTC debugging info). |
| `debugOutput` | `"file" \| "socket"` | Debug output destination. |
| `enableCallReports` | `boolean` | Enable automatic call quality reporting. Defaults to `true`. |
| `callReportInterval` | `number` | Interval in ms for collecting call statistics. Defaults to `5000`. |
| `region` | `string` | Region for the connection. |
| `env` | `Environment` | Environment (internal use). |
| `ringtoneFile` | `string` | URL to a wav/mp3 ringtone file. |
| `ringbackFile` | `string` | URL to a wav/mp3 ringback file (used when "Generate Ringback Tone" is disabled on the SIP Connection). |
| `mutedMicOnStart` | `boolean` | Mute microphone by default when a call starts. |
| `rtcIp` | `string` | Custom RTC signaling server IP. |
| `rtcPort` | `number` | Custom RTC signaling server port. |
| `useCanaryRtcServer` | `boolean` | Use Telnyx's Canary RTC server. |

### Media Permissions Recovery

When `mediaPermissionsRecovery` is enabled and `getUserMedia` fails during an inbound call answer, the SDK emits a recoverable `telnyx.error` event:

```js
import { isMediaRecoveryErrorEvent } from '@telnyx/webrtc';

const client = new TelnyxRTC({
  login_token: '...',
  mediaPermissionsRecovery: {
    enabled: true,
    timeout: 20000,
    onSuccess: () => console.log('Media recovered'),
    onError: (err) => console.error('Recovery failed', err),
  },
});

client.on('telnyx.error', (event) => {
  if (isMediaRecoveryErrorEvent(event)) {
    showPermissionDialog({
      onContinue: () => event.resume(),
      onCancel: () => event.reject?.(),
    });
  }
});
```

### Connection Lifecycle (Signaling)

When `connect()` is called, the following JSON-RPC message exchange occurs over the WebSocket:

1. **Client → rtc.telnyx.com:** `login` message with credentials and session ID.
2. **rtc.telnyx.com → Client:** `logged in` result with the session ID and `voice_sdk_id`.
3. **rtc.telnyx.com → Client:** `telnyx_rtc.clientReady` event (may include `reattached_sessions`).
4. **Client → rtc.telnyx.com:** `telnyx_rtc.gatewayState` query.
5. **rtc.telnyx.com → Client:** `REGED` result confirming registration.

At this point, the `telnyx.ready` event fires on the SDK client, and it is authenticated to make or receive calls.

## Call Flow

Calls are initiated with `client.newCall(options)` where `options` is an `ICallOptions` object.

### ICallOptions Properties

| Property | Type | Description |
|---|---|---|
| `destinationNumber` | `string` | Phone number or SIP URI to dial. |
| `callerName` | `string` | Caller ID name for outbound calls. |
| `callerNumber` | `string` | Caller ID number for outbound calls. Valid phone number required for PSTN. |
| `audio` | `boolean \| MediaTrackConstraints` | Override default audio constraints. Defaults to `true`. |
| `video` | `boolean` | Override default video constraints. Defaults to `false`. |
| `useStereo` | `boolean` | Use stereo audio instead of mono. |
| `micId` | `string` | Microphone `deviceId`. Overrides client default. |
| `camId` | `string` | Webcam `deviceId`. Overrides client default. |
| `speakerId` | `string` | Speaker `deviceId`. Overrides client default. |
| `localElement` | `string \| HTMLMediaElement` | Override client's default local media element. |
| `remoteElement` | `string \| HTMLMediaElement` | Override client's default remote media element. |
| `localStream` | `MediaStream` | Use this stream instead of retrieving a new one. |
| `remoteStream` | `MediaStream` | Use this stream instead of retrieving a new one. |
| `iceServers` | `RTCIceServer[]` | Override client's default ICE servers for this call. |
| `forceRelayCandidate` | `boolean` | Force relay ICE candidate for this call. |
| `prefetchIceCandidates` | `boolean` | Enable/disable ICE candidate prefetching. Defaults to `true`. |
| `trickleIce` | `boolean` | Enable/disable Trickle ICE. |
| `preferred_codecs` | `RTCRtpCodecCapability[]` | Preferred codecs for the call. |
| `customHeaders` | `{ name: string; value: string }[]` | Custom headers added to INVITE and ANSWER requests. |
| `clientState` | `string` | Call Control `client_state` (base64 encoded). Used with Connections that have Advanced → Events enabled. |
| `id` | `string` | Custom call ID (replaces UUID-generated `callID`). |
| `mediaSettings` | `object` | Media config: `sdpASBandwidthKbps?` (number), `useSdpASBandwidthKbps?` (boolean). |
| `onNotification` | `Function` | Override client's `telnyx.notification` handler for this call. |
| `telnyxSessionId` | `string` | Telnyx call session ID (Call Control). |
| `telnyxLegId` | `string` | Telnyx call leg ID (Call Control). |
| `telnyxCallControlId` | `string` | Telnyx Call Control ID. |
| `debug` | `boolean` | Enable debug mode for this call. |
| `debugOutput` | `"file" \| "socket"` | Debug output destination. |
| `keepConnectionAliveOnSocketClose` | `boolean` | **Deprecated** — use `IClientOptions.keepConnectionAliveOnSocketClose` instead. |

### Call Initiation Sequence

Under the hood, the SDK performs many steps before sending the INVITE:

1. **`RTCPeerConnection`** is instantiated.
2. **`getUserMedia`** is invoked to obtain user permission and the `MediaStream`.
3. **`addTransceiver`** adds the local stream to the `RTCPeerConnection` sender.
4. The **`negotiationneeded`** event fires.
5. **`createOffer`** is invoked, producing an `RTCSessionDescription` (SDP offer).
6. **`setLocalDescription`** sets the SDP of the client peer.
7. Concurrently, **ICE candidate gathering** begins.
8. When gathering completes (`icecandidate` with `candidate = null`), the local SDP is augmented with ICE candidates.

The signaling exchange then proceeds:

1. **Client → rtc.telnyx.com:** `telnyx_rtc.invite` with SDP and call parameters.
2. **rtc.telnyx.com → Client:** `CALL CREATED` result.
3. **rtc.telnyx.com → Client:** `telnyx_rtc.ringing` event (call is ringing, includes `telnyx_leg_id` and `telnyx_session_id`).
4. **Client → rtc.telnyx.com:** Acknowledgement of ringing.
5. **rtc.telnyx.com → Client:** `telnyx_rtc.media` event with the remote SDP.
6. **Client → rtc.telnyx.com:** Acknowledgement of media.
7. The SDK invokes **`setRemoteDescription`** with the remote SDP.
8. **rtc.telnyx.com → Client:** `telnyx_rtc.answer` event.
9. The `RTCPeerConnection` state transitions from `connecting` to `connected`.
10. **Media flows over UDP.**
