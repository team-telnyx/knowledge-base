---
title: Keyword Boosting
summary: Boost recognition of specific terms (keyterm and keywords parameters).
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/keyword-boosting
    content_hash: deee43c457b0c38c56b9ed42b2bbf82c27d6407adaaaf65fac239f4e97fd9315
updated_at: 2026-04-10T00:00:00Z
---

# Keyword Boosting

Boost recognition of specific terms (keyterm and keywords parameters).

**Deepgram only.** Other engines ignore these parameters.

Two parameters control keyword boosting. They target different Deepgram model generations.

## `keyterm` — Nova-3 and Flux

Comma-separated list of terms to boost. Simple — no intensifiers.

```
?keyterm=Telnyx,WebRTC,SIP
```

Deepgram Nova-3 and Flux only. Ignored on older models.

## `keywords` — Nova (Legacy)

Terms with optional intensity scores. Format: `keyword:intensifier`.

```
?keywords=Telnyx:2
```

Deepgram Nova only. Not supported on Flux (silently ignored).

## Which To Use

| Model  | Parameter  |
| ------ | ---------- |
| Flux   | `keyterm`  |
| Nova-3 | `keyterm`  |
| Nova   | `keywords` |
| Nova-2 | `keywords` |

## Examples

Boost multiple terms on Nova-3:

```
?transcription_engine=Deepgram&model=nova-3&keyterm=Telnyx,SIP,RTP,WebRTC
```

Boost with intensifiers on legacy Nova:

```
?transcription_engine=Deepgram&model=nova&keywords=Telnyx:2&keywords=telephony:1
```
