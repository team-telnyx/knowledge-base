---
title: WebRTC Voice SDKs
summary: The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate
  and control Telnyx call legs from browsers and mobile devices. They translate between
  the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage
  under the Programmable Voice API umbrella. This page covers SDK architecture, authentication
  options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces,
  and Android push notifications.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/architecture
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
updated_at: 2026-08-05T14:08:20Z
---

# WebRTC Voice SDKs

*Part 5 of 7 — see also: [Part 1](webrtc-voice-sdks--part-1.md), [Part 2](webrtc-voice-sdks--part-2.md), [Part 3](webrtc-voice-sdks--part-3.md), [Part 4](webrtc-voice-sdks--part-4.md), [Part 6](webrtc-voice-sdks--part-6.md), [Part 7](webrtc-voice-sdks--part-7.md)*

The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate and control Telnyx call legs from browsers and mobile devices. They translate between the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage under the Programmable Voice API umbrella. This page covers SDK architecture, authentication options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces, and Android push notifications.

## Client Options (IClientOptions)

The `IClientOptions` interface configures the `TelnyxRTC` client.

| Property | Type | Description |
| --- | --- | --- |
| `anonymous_login` | `Object` | Anonymous login options. Contains `target_id` (typically the ID of the AI assistant to connect to), optional `target_params` (forwarded to voice-sdk-proxy and mapped to custom headers on the SIP INVITE; use `target_params.conversation_id` only to join an existing Telnyx AI conversation), `target_type` (currently only `ai_assistant` is supported), and optional `target_version_id`. |
| `callReportFlushInterval` | `number` | Interval in milliseconds for submitting intermediate call reports while a call is active. Set to `0` to disable time-based intermediate reports. Default: `180000` (3 minutes). |
| `callReportInterval` | `number` | Interval in milliseconds for collecting call statistics after the initial high-resolution startup window. Default: `5000` (5 seconds). |
| `debug` | `boolean` | Enable debug mode for this client. Gathers WebRTC debugging information. |
| `debugOutput` | `"file" \| "socket"` | Debug output option. |
| `enableCallReports` | `boolean` | Enable automatic call quality reporting to voice-sdk-proxy. When enabled, WebRTC stats are collected periodically during calls and posted to the voice-sdk-proxy `/call_report` endpoint when the call ends. Default: `true`. |
| `env` | `Environment` | Environment to use for the connection. Internal use only. |
| `forceRelayCandidate` | `boolean` | Force the use of a relay ICE candidate. |
| `hangupOnBeforeUnload` | `boolean` | Controls whether the SDK attempts to send BYE for active calls during browser page unload. Default: `true`. |
| `iceServers` | `RTCIceServer[]` | ICE Servers to use for all calls within the client connection. Overrides the default ones. |
| `keepConnectionAliveOnSocketClose` | `boolean` | When `true`, the SDK attempts to keep the Peer connection alive when the WebSocket connection is closed unexpectedly (e.g. network interruption, device sleep). |
| `login` | `string` | The `username` to authenticate with your SIP Connection. `login` and `password` take precedence over `login_token`. |
| `login_token` | `string` | The JSON Web Token (JWT) to authenticate with your SIP Connection. This is the recommended authentication strategy. |
| `maxReconnectAttempts` | `number` | Maximum number of automatic socket reconnection attempts after an unexpected disconnect. When the limit is reached, a `telnyx.error` event with code `RECONNECTION_EXHAUSTED` (45003) is emitted. Set to `0` for unlimited attempts. Default: `10`. |
| `mediaPermissionsRecovery` | `Object` | Configuration for media permissions recovery on inbound calls. When enabled and the initial `getUserMedia` call fails while answering, the SDK emits a recoverable `telnyx.error` event with `resume()` and `reject()` callbacks. |
| `mutedMicOnStart` | `boolean` | Disable microphone by default when the call starts or when adding a new audio source. |
| `password` | `string` | The `password` to authenticate with your SIP Connection. |
| `prefetchIceCandidates` | `boolean` | Enable or disable prefetching ICE candidates. Default: `true`. |
| `region` | `string` | Region to use for the connection. |
| `ringbackFile` | `string` | A URL to a wav/mp3 ringback file used when "Generate Ringback Tone" is disabled in your SIP Connection. |
| `ringtoneFile` | `string` | A URL to a wav/mp3 ringtone file. |
| `rtcIp` | `string` | RTC connection IP address to use instead of the default one. Useful when using a custom signaling server. |
| `rtcPort` | `number` | RTC connection port to use instead of the default one. Useful when using a custom signaling server. |
| `skipLastVoiceSdkId` | `boolean` | When reconnecting with a stored `voice_sdk_id`, append `?skip_last_voice_sdk_id=true` to the WebSocket URL so VSP routes the connection to a different b2bua-rtc instance. Default: `false`. |
| `skipTrailing` | `boolean` | When `true`, appends `skip_trailing=true` to the VSP WebSocket URL so VSP skips pre-routing identity resolution. Intended for internal/test-infra usage. Default: `false`. |
| `trickleIce` | `boolean` | Enable or disable Trickle ICE. |
| `useCanaryRtcServer` | `boolean` | Use Telnyx's Canary RTC server. |

### Media Permissions Recovery Example

```javascript
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
    // event.recoverable === true, event.error.fatal === false
    showPermissionDialog({
      onContinue: () => event.resume(),
      onCancel: () => event.reject?.(),
    });
  } else if (event.error.fatal) {
    // Terminal error — give up on this call/session
  }
});
```
