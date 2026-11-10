---
source_url: "https://support.telnyx.com/en/articles/2026110901-video-on-sip-trunking"
title: "Video on SIP Trunking"
description: "Learn how to enable H.264 or VP8 video on a Telnyx SIP trunk, add the X-Telnyx-Video header to your SIP INVITE, and verify video on a test call."
collection_path: "3968237-telnyx-sip-trunking-configurations"
updated_at: "2026-11-09"
modified_at: "2026-11-09"
---

# Video on SIP Trunking

Telnyx SIP Trunking supports video on calls between compatible SIP endpoints, such as video phones and softphones. A SIP call can carry both audio and video. The Session Description Protocol (SDP) offer and answer negotiate each stream separately, so your devices can use their usual audio codec and agree on **H.264** or **VP8** for video.

## Before you begin

- Confirm that both endpoints can send and receive video and have at least one video codec in common. If you use H.264, check that the endpoints support compatible profiles and packetization modes.
- Identify the device that sends the SIP INVITE to Telnyx. If your phone sends calls through a private branch exchange (PBX) or session border controller (SBC), that device may control which headers and codecs Telnyx receives.

## Configure the caller to send video

1. Enable H.264 or VP8 on the calling endpoint. If a PBX or SBC handles the call, configure it to allow video and the selected codec on the trunk.
2. Add the following custom SIP header to the initial INVITE that your SIP client, PBX, or SBC sends to Telnyx for a video call.

   ```text
   X-Telnyx-Video: true
   ```

3. Configure the calling endpoint to start video calls with an SDP offer that includes an `m=video` section listing H.264 or VP8 alongside the usual `m=audio` section.

The header requests video handling from Telnyx. The SDP offer describes the video codecs available for the call, and the SDP answer indicates whether the receiving side accepts video and which offered codec it can use.

For example, these lines in an SDP offer show VP8 as a video option. The media port and payload type are example values.

```text
m=video 49172 RTP/AVP 96
a=rtpmap:96 VP8/90000
```

## Configure the callee to receive video

The callee's endpoint must have at least one video codec offered by the caller enabled, either **H.264** or **VP8**. Any PBX or SBC that handles the incoming call must allow that codec.

## Verify video on a test call

Place a call from your Telnyx SIP trunk to a video-capable SIP endpoint. Answer with video enabled and confirm that both participants can see and hear each other.

## Troubleshoot missing or one-way video

1. **Check the INVITE sent to Telnyx.** In your SIP trace, look for `X-Telnyx-Video: true` in the SIP headers and an `m=video` section in the SDP body. If the phone offers video but the trunk-facing INVITE lacks the header or video offer, check your PBX or SBC configuration.
2. **Check the INVITE received by the callee.** If its SDP offer is missing a compatible video codec, check the codec settings on the equipment that handles the incoming call.
3. **Check the SDP answer.** An `m=video` line with port `0` means the receiving side declined the video stream. Check that the receiving endpoint has video enabled and can use a codec from the offer. Audio can still connect if the receiving side accepts the audio stream.
4. **Check the media path.** If the answer accepts video but the picture is missing or visible on only one side, check the camera and its permissions on the affected device. Then check whether your firewall and any PBX or SBC allow video RTP to reach the addresses and ports negotiated for the call.

For details on interpreting an SDP answer, see [RFC 3264, Generating the Answer](https://www.rfc-editor.org/rfc/rfc3264.html#section-6).

For trunk setup, see [How to Configure a SIP Trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk).
