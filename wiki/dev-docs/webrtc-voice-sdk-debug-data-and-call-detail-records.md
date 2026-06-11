---
title: WebRTC Voice SDK Debug Data and Call Detail Records
summary: How to enable, find, visualize, and interpret Telnyx WebRTC SDK debug data,
  and how it ties to WebRTC detail records and common call-control use cases like
  contact centers and outbound dialers.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/outbound-dialer
updated_at: 2026-05-20T10:27:54Z
---

# WebRTC Voice SDK Debug Data and Call Detail Records

How to enable, find, visualize, and interpret Telnyx WebRTC SDK debug data, and how it ties to WebRTC detail records and common call-control use cases like contact centers and outbound dialers.

## What the debug data is
Debug data is collected on the SDK client and describes the WebRTC call leg between the SDK client and Telnyx. It’s intended for troubleshooting quality and connectivity. This feature is in beta and the data schema or presentation may change. Available in: JS, iOS (native), Android (native), and Flutter SDKs.

## Enable and ship debug data
- Initialize your SDK client with the debug option enabled and output set to socket (for JS, see ClientOptions “debug” and “output”).
- When enabled, the client sends debug frames to Telnyx over the WebSocket during the call.

## Where the files are stored
- Telnyx assembles frames into a single JSON file per segment and stores it in your Telnyx Cloud Storage bucket in us-central-1.
- Bucket name: voice-sdk-debug-reports-[USER-ID] (USER-ID is your Telnyx account ID).
- Object key pattern: [call_id]/rtc_stats_reports/[segment_id].json
- Most calls have a single segment. If the SDK reconnects mid-call, you may see multiple segments under the same call_id.
- Access via Mission Control or an S3-compatible client (for AWS CLI setup, see Telnyx Cloud Storage quick start: https://developers.telnyx.com/docs/cloud-storage/quick-start#option-2-using-aws-cli). Use endpoint https://us-central-1.telnyxcloudstorage.com.

Example list objects (replace placeholders):
- aws s3api list-objects-v2 \
  --bucket voice-sdk-debug-reports-[USER-ID] \
  --endpoint-url https://us-central-1.telnyxcloudstorage.com \
  --prefix [call_id]

## Visualize the data
Upload the JSON file(s) at https://webrtc-debug.telnyx.com/ to see ICE, network stats, and audio levels plotted over time.

## Find the right call_id with detail records
Every SDK↔Telnyx call produces a WebRTC detail record. Use the Detail Records API to search with filters such as record_type=webrtc, date_range, and auth_username, then take the call_id from the result to locate the debug file(s).
- session_id identifies a registration session; one session can have many calls.
- call_id identifies the SDK↔Telnyx call and is required to find the debug data.
- SIP-side identifiers you may also see: telnyx_leg_id, telnyx_session_id, fs_channel_id.
- If you use programmable voice (Call Control or TeXML), telnyx_call_control_id may also appear and can help correlate with webhook events.
See [WebRTC Voice SDKs Call Detail Records](webrtc-voice-sdks-call-detail-records.md).

## Interpreting the debug data
Use the visualizer to inspect these areas:

- Peer configuration
  - Shows the RTCPeerConnection configuration captured by the SDK.
  - If prefetchIceCandidates is disabled, the reserved pool size is 0; otherwise 255.
  - If forceRelayCandidate is enabled, ICE transport policy is relay.
  - Default ICE servers used by Telnyx SDKs: stun.l.google.com, stun.telnyx.com, turn.telnyx.com.

- ICE candidates and selected pair
  - You’ll always see one remote host candidate representing Telnyx.
  - You should see multiple local candidates unless relay-only is enforced.
  - A successful connection requires at least one viable local candidate of type prflx, srflx, or relay. host alone cannot connect across the internet.
  - If no viable local candidates appear, the network may block UDP and/or restrict access to turn.telnyx.com.
  - The visualizer highlights the candidate pair selected for the call.

- Network KPIs
  - RTT: Elevated values correlate with mouth-to-ear delay.
  - Packets lost: High loss correlates with choppy or skipped audio.
  - Jitter: High jitter correlates with inconsistent audio quality.

- Other useful signals
  - In suspected one-way audio, compare inbound vs outbound audio levels to confirm directionality.

For a walkthrough of the charts and what to look for, see [Interpreting WebRTC Voice SDKs Debug Data](interpreting-webrtc-voice-sdks-debug-data.md).

## How this ties into call-control workflows
WebRTC debug data helps you diagnose the SDK leg while Voice APIs (Call Control/TeXML) orchestrate PSTN legs and agent flows. In these flows you’ll also correlate with: telnyx_call_control_id, webhook timelines (call.initiated, call.answered, call.bridged, call.hangup), and queue/park states.

- Contact center (CCaaS)
  - Use Park Outbound Calls and webhooks to hold and route calls while agents register via WebRTC.
  - Backend issues actions (answer, speak, bridge, transfer, enqueue) based on webhook events; frontend surfaces agent status, queue views, and call controls.
  - Useful frontend functions: getDevices, setAudioSettings, toggleAudioMute, toggleHold.
  - See [Contact center (CCaaS) implementation](contact-center-ccaas-implementation.md).

- Outbound dialer
  - Frontend registers and places an SDK call; backend dials PSTN via Call Control or TeXML, then bridges legs on answer.
  - Webhooks (initiated/answered/bridged/hangup) define the lifecycle; correlate those with the WebRTC detail record and debug segments for end-to-end visibility.
  - See [Outbound dialer implementation](outbound-dialer-implementation.md).

## Troubleshooting playbook
1) Reproduce the issue with SDK debug enabled (output=socket).
2) Search WebRTC detail records, identify the relevant call_id, and note session_id and any telnyx_call_control_id for correlation.
3) Retrieve the debug JSON file(s) from voice-sdk-debug-reports-[USER-ID]/[call_id]/rtc_stats_reports/…
4) Upload to https://webrtc-debug.telnyx.com/.
5) Check ICE:
   - Are there viable local candidates (srflx/prflx/relay)? If not, suspect strict egress rules; verify UDP and access to stun.telnyx.com/turn.telnyx.com.
   - Consider enabling forceRelayCandidate in restrictive environments.
6) Inspect KPIs:
   - High RTT → latency symptoms; consider geographic proximity and network path.
   - High packet loss/jitter → choppy/inconsistent audio; look for Wi‑Fi congestion, VPNs, or traffic shaping.
7) Verify audio levels for one-way audio and compare against call-control events (e.g., bridge timing).
8) If multiple segments exist, a reconnect occurred; examine each segment’s ICE pair and KPIs around the transition.

## Related pages
- [WebRTC Voice SDKs Call Detail Records](webrtc-voice-sdks-call-detail-records.md)
- [Interpreting WebRTC Voice SDKs Debug Data](interpreting-webrtc-voice-sdks-debug-data.md)
- [Contact center (CCaaS) implementation](contact-center-ccaas-implementation.md)
- [Outbound dialer implementation](outbound-dialer-implementation.md)
