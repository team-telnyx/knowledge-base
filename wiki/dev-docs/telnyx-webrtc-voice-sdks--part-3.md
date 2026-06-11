---
title: Telnyx WebRTC Voice SDKs
summary: Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture,
  authentication, push notifications across all platforms, call states, dialing, use
  cases, debugging, and costs.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
  content_hash: 3fedfc040ba32d2fc260b1a579cd1f8ac4753568e8ff8a2992a62e3f40868e8f
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
  content_hash: 37576f7c51e98e804c53c696f71d04a1f423e306cb42ed16c04b94bdce9c7194
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
  content_hash: 42c36618bb0701822e5ea49792d6cc08326c19f09163f9661402976d2af85313
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
  content_hash: a73f480aea535097057ca6c987ba62346ec058988dd0e032c1fb8e89f67ad638
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
  content_hash: a36b6cda308b54ac45a958bb0c47227e939f9cbb33579b5d4751525710f2be46
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
  content_hash: cdd95e464a79746264328e70ea199bf2fff9aa2aad036d53cd27a72e4fecc817
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
  content_hash: 2ca56f8d180406798028958d59f4592bbcdb16c001fed0275c36663b4f85f4f0
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
  content_hash: b87a3806edb676bb6f754a9a871f8bfde50507fff598e77ca7624259d53a0a25
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
  content_hash: f616744b0e7b693486449482bb769ac7c549642a4e62508f710b7821435b7967
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
  content_hash: ab112fd87bff5aee9d8cc7bd8252fd42b4e2f1dce43fd3a6ec95ebba4a288fc8
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/outbound-dialer
  content_hash: 9ef961c8750a0649f790a594d6b1b232f1e5d0e191fccd8f4d8678f237474526
updated_at: 2026-06-11T10:49:57Z
---

# Telnyx WebRTC Voice SDKs

*Part 3 of 4 — see also: [Part 1](telnyx-webrtc-voice-sdks--part-1.md), [Part 2](telnyx-webrtc-voice-sdks--part-2.md), [Part 4](telnyx-webrtc-voice-sdks--part-4.md)*

Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture, authentication, push notifications across all platforms, call states, dialing, use cases, debugging, and costs.

## Use Cases

### Contact Center (CCaaS)

A contact center solution leverages SIP connection credentials with **Park Outbound Calls** and webhook events for real-time call control.

**Frontend — Agent Desktop Application:**

- **Agent status management** — agents report Available/Unavailable status; status is correlated with WebRTC client state.
- **Call control toolbar** — Answer, Hangup, Mute/Unmute, Hold/Unhold buttons.
- **Queue view** — monitor parked calls, pick up manually, display position and estimated wait time.
- **Audio device settings** — `client.getDevices()` to list devices, `client.setAudioSettings()` to select mic/speaker.

Key frontend methods:

```js
// Toggle mute
await call.toggleAudioMute()

// Toggle hold
await call.toggleHold()
```

**Backend — Call Flow via Webhooks:**

Monitor call event types on your webhook URL. Key events and actions:

- **`call.initiated`** — Answer the call and play a greeting/IVR prompt using `call.speak()`.
- **`call.dtmf.received`** — Route based on DTMF digit (e.g., transfer to number or enqueue to queue).
- **`call.enqueued`** — Play wait prompt, start hold music, emit queue update to frontend via WebSocket.
- **`call.answered`**, **`call.bridged`**, **`call.hangup`**, **`call.recording.saved`**, **`call.transcription`** — Handle accordingly.

### Outbound Dialer

An automated outbound dialer combines front-end WebRTC functionality with a backend voice application using Park Outbound Calls and webhook events.

**Required components:** WebRTC Client, Backend Server Application, and a SIP Connection with Park Outbound Calls enabled.

**Typical call flow (Voice API):**

1. WebRTC client registers with Telnyx (`client.connect()`).
2. Client initiates a call (`client.newCall()`), which is parked on the SIP connection.
3. Backend dials the PSTN destination via the Voice API `POST /v2/calls`.
4. Telnyx sends `call.initiated` webhook to the backend.
5. Telnyx makes the outbound PSTN call.
6. When the PSTN side answers, Telnyx sends `call.answered` webhook.
7. Backend bridges the two call legs: `POST /v2/calls/{call_control_id_WebRTC}/actions/bridge`.
8. Telnyx sends `call.bridged` webhook. The call is now in progress.
9. On hangup, Telnyx sends `call.hangup` webhook with cause information.

**Typical call flow (TeXML):**

1–2. Same as above.
3. Backend dials via TeXML: `POST /v2/texml/Accounts/:account_sid/Calls` with a URL pointing to TeXML instructions.
4. The URL returns XML with a `<Dial><Number>` verb to connect the second PSTN leg.

## Debugging and Detail Records

### Call Detail Records

Every call between a voice SDK client and Telnyx produces a `webrtc` detail record, searchable via the [Detail Records API](https://developers.telnyx.com/api-reference/detail-records/search-detail-records):

```
GET /v2/detail_records?filter[record_type]=webrtc&filter[date_range]=today&filter[auth_username]=myagent01
```

Key ID fields:

- **`session_id`** — identifies a successful registration between an SDK client and Telnyx.
- **`call_id`** — identifies a call between an SDK client and Telnyx; has a many-to-one relationship to a session. Essential for locating debug logs.
- **`telnyx_leg_id`**, **`telnyx_session_id`**, **`fs_channel_id`** — identify the SIP leg.
- **`telnyx_call_control_id`** — present if programmable voice (Call Control or TeXML) is used in the call flow.

### Debug Logs

Debug data is collected on the SDK client and provides empirical data on the call leg between the SDK client and Telnyx. Available for JS, iOS Native, Android Native, and Flutter SDKs (beta feature).

**Enabling debug:** Initialize the SDK client with `debug` set to `true` and output set to `socket`.

**Locating debug data:** The SDK ships debug data frames over the WebSocket. They are assembled into a single JSON file stored in a Telnyx Cloud Storage bucket in `us-central-1` named `voice-sdk-debug-reports-[USER-ID]`. Objects follow the naming schema `[call_id]/rtc_stats_reports/[segment_id]`. When there is a reconnect, there may be more than one data segment.

You can locate data using the Telnyx Mission Control portal or a configured AWS CLI:

```bash
aws s3api list-objects-v2 \
  --bucket voice-sdk-debug-reports-22 \
  --profile "*.telnyxcloudstorage.com" \
  --endpoint-url https://us-central-1.telnyxcloudstorage.com \
  --output table \
  --prefix <call_id>
```

**Visualizing data:** Upload the JSON to [webrtc-debug.telnyx.com](https://webrtc-debug.telnyx.com/) for visualization.

### Interpreting Debug Data

The visualization includes these key sections:

- **Peer Configuration** — RTCPeerConnection settings. If `prefetchIceCandidates` is disabled, ICE candidate pool size is 0; otherwise 255. If `forceRelayCandidate` is enabled, transport policy is `relay`. Default ICE endpoints: `stun.l.google.com`, `stun.telnyx.com`, `turn.telnyx.com`.
- **ICE Candidates & Candidate Pair** — Lists all gathered ICE candidates. There is always one remote `host` candidate (Telnyx's end) and multiple local candidates unless relay-only. For a call to be established, at least one local candidate of type `prflx`, `srflx`, or `relay` must be present. `host` candidates cannot establish a peer connection over the internet. If no viable local candidates exist, the client is likely on a restrictive network blocking UDP and TURN access.
- **RTT** — High round-trip time indicates voice delay.
- **Packets Lost** — High packet loss indicates skipped audio.
- **Jitter** — High jitter indicates inconsistent audio quality.
- **Audio Levels** — Check inbound/outbound audio levels to diagnose one-way audio issues.
