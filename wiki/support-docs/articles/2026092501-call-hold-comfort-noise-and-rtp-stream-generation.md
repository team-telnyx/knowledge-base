---
title: "Call Hold, Comfort Noise, and RTP Stream Generation"
summary: "This article describes how Telnyx detects SIP call hold and handles RTP media, Music on Hold, comfort-noise packets, and RTP generation toward the other party during hold or gaps in audio."
sources:
- url: "https://support.telnyx.com/en/articles/2026092501-call-hold-comfort-noise-and-rtp-stream-generation"
updated_at: 2026-11-16T17:58:49Z
tags: [support-docs]
source_path: "support-docs/en--articles--2026092501-call-hold-comfort-noise-and-rtp-stream-generation.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--2026092501-call-hold-comfort-noise-and-rtp-stream-generation.md -->

# Call Hold, Comfort Noise, and RTP Stream Generation

This article describes how Telnyx detects SIP call hold and handles RTP media, Music on Hold, comfort-noise packets, and RTP generation toward the other party during hold or gaps in audio.

## Valid Hold Signaling

Regardless of whether the SIP user is on the A leg or B leg, Telnyx recognizes a SIP re-INVITE as a valid hold request when its SDP contains any of the following:

| SDP Attribute | Description |
| --- | --- |
| `a=sendonly` | The endpoint signals it will only send media (not receive). |
| `a=inactive` | The endpoint signals the media stream is temporarily inactive in both directions. |
| SDP media IP `0.0.0.0` | Legacy hold mechanism: the endpoint sets the connection IP to `0.0.0.0` to indicate hold. |

When Telnyx receives any of these signals, it accepts the hold request and responds with `200 OK`.

## Behavior During a Recognized Hold

When Telnyx recognizes a valid hold request, two things always happen:

1. **Telnyx does not enforce RTP timeout on the SIP user's leg.** The user's leg stays alive even if media stops flowing.
2. **Telnyx does not propagate the hold to the opposite leg.** The opposite leg is not placed on hold; it continues as an active call.

With **Generate Comfort Noise enabled** (the default), Telnyx handles the following media behaviors during hold:

### 1. No RTP media

If the user stops sending RTP entirely after signaling hold, Telnyx **generates a silent RTP stream** toward the opposite leg. This keeps the far side from detecting a media gap and ending the call due to RTP timeout.

### 2. RTP media continues (Music on Hold)

If the user continues sending RTP media during the hold (common when a PBX plays Music on Hold while signaling `a=sendonly`), **Telnyx bridges that media to the opposite leg** instead of generating its own silent RTP stream. The far side hears whatever the user is playing.

### 3. Comfort Noise packets (payload type 13)

If the user sends RTP Comfort Noise (CN) packets with payload type 13, Telnyx **generates a silent RTP stream** toward the opposite leg. The CN packets keep the user's leg alive, and Telnyx ensures the opposite leg also receives media to prevent timeout.

All three scenarios prevent the far side from ending the leg due to RTP timeout.

## Connection Setting: Generate Comfort Noise

The SIP Connection setting **Generate Comfort Noise** is available in the Mission Control Portal under **Advanced Settings** on your SIP Connection. This setting is **enabled (checked) by default**, and the default behavior is described above.

![Generate comfort noise enabled in the SIP Connection Advanced Settings](_images/call-hold-generate-comfort-noise.png)

When this setting and **Generate RTP on comfort-noise packets** are both disabled, Telnyx accepts the hold re-INVITE and responds with `200 OK`, but **does not generate a silent RTP stream** toward the opposite leg. The far side may terminate the leg if it enforces RTP timeout. This is especially common with termination carriers.

### When Generate Comfort Noise is disabled

This table assumes **Generate RTP on comfort-noise packets** is also disabled.

| Media sent by your endpoint | Media sent to the opposite leg | RTP timeout risk |
| --- | --- | --- |
| No RTP | No silent RTP generated | Yes |
| Music on Hold (`a=sendonly`) | Your Music on Hold is bridged | No |
| Comfort Noise (PT 13) | No silent RTP generated | Yes |

## Unsignaled or Invalid Hold

Telnyx does **not** recognize a call as being on hold when the user stops sending media and either:

- Does not send a re-INVITE at all; or
- Sends a re-INVITE containing `a=sendrecv` (which is not a hold signal).

Without **Generate RTP on comfort-noise packets** enabled, Telnyx does not generate a silent RTP stream toward the opposite leg in this situation. The far side may terminate that leg if it enforces RTP timeout. Sending CN packets (payload type 13) keeps the user's media leg active, but does not by itself provide a continuous audio RTP stream to the other party.

## Connection Setting: Generate RTP on comfort-noise packets

Enable **Generate RTP on comfort-noise packets** to keep RTP flowing toward the other party during comfort noise or gaps in audio. This helps prevent the other party from ending the call because of an RTP timeout, including when your endpoint does not signal hold.

**A SIP hold request is not required.** Despite the setting's name, RTP generation is not limited to receiving CN packets: it also covers gaps when your endpoint stops sending audio. Normal audio, including Music on Hold, continues to be bridged when present.

This is separate from **Generate Comfort Noise**, which controls media generation during a recognized hold:

| Setting | API field | Default | Purpose |
| --- | --- | --- | --- |
| Generate Comfort Noise | `default_on_hold_comfort_noise_enabled` | Enabled | Generate RTP during a recognized SIP hold. |
| Generate RTP on comfort-noise packets | `bridge_generate_comfort_noise_on_cn` | Disabled | Keep RTP flowing during CN or gaps in audio, without requiring SIP hold signaling. |

### Configure in Mission Control

1. Open **Voice → SIP Trunking → SIP Connections** and select your connection.
2. Open **Configuration → Advanced Settings**.
3. Check **Generate RTP on comfort-noise packets** and save the connection.

### Configure through the API

Set `bridge_generate_comfort_noise_on_cn` to `true` in the update request for your credential, IP, FQDN, or UAC connection. For example, the JSON body for `PATCH /v2/credential_connections/{connection_id}` is:

```json
{
  "bridge_generate_comfort_noise_on_cn": true
}
```

Set the field to `false` to disable this behavior. This setting can be managed through the portal or API; it no longer requires a support-only configuration.

## Quick Reference

### Valid hold request

This table assumes **Generate RTP on comfort-noise packets** is disabled. When it is enabled, RTP generation during CN or gaps in audio does not depend on the **Generate Comfort Noise** setting.

| Media sent by your endpoint | Generate Comfort Noise | Media sent to the opposite leg | RTP timeout risk |
| --- | --- | --- | --- |
| No RTP | Enabled | Telnyx-generated silent RTP | No |
| No RTP | Disabled | No media generated | Yes |
| Music on Hold (`a=sendonly`) | Enabled or disabled | Your Music on Hold is bridged | No |
| Comfort Noise (PT 13) | Enabled | Telnyx-generated silent RTP | No |
| Comfort Noise (PT 13) | Disabled | No media generated | Yes |

### No valid hold request

The following applies when no hold re-INVITE is sent, or when a re-INVITE uses `a=sendrecv`:

| Media sent by your endpoint | Generate RTP on comfort-noise packets | Media sent to the opposite leg |
| --- | --- | --- |
| CN packets (PT 13) | Disabled | No audio RTP generated |
| CN packets (PT 13) | Enabled | Telnyx-generated RTP |
| No RTP | Disabled | No media generated |
| No RTP | Enabled | Telnyx-generated RTP |
| Normal audio or Music on Hold | Enabled or disabled | Your audio is bridged |

Generated RTP helps prevent an opposite-leg RTP timeout; it does not signal hold or replace normal audio from your endpoint.

RTP timeout risk in these tables refers to the opposite leg.

## Related Articles

- [SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)
- [SIP Connection Types](https://support.telnyx.com/en/articles/4245868-sip-connection-types)
- [Telnyx Debugging Tools](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools)
