---
title: 'TeXML Verbs: Voice Call Control Reference'
summary: A consolidated reference to core TeXML verbs for building programmable voice
  call flows on Telnyx—covering behavior, attributes, child nouns, callbacks, and
  concise examples for Dial, Say, Play, Gather, Record, Conference, Enqueue/Leave,
  Hangup, Pause, Redirect, Reject, Start/Stop, and Connect.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
updated_at: 2026-05-20T09:38:14Z
---

# TeXML Verbs: Voice Call Control Reference

*Part 1 of 3 — see also: [Part 2](texml-verbs-voice-call-control-reference--part-2.md), [Part 3](texml-verbs-voice-call-control-reference--part-3.md)*

A consolidated reference to core TeXML verbs for building programmable voice call flows on Telnyx—covering behavior, attributes, child nouns, callbacks, and concise examples for Dial, Say, Play, Gather, Record, Conference, Enqueue/Leave, Hangup, Pause, Redirect, Reject, Start/Stop, and Connect.

## Overview
TeXML verbs are XML instructions that control call flows on Telnyx. Verbs may have attributes and can nest nouns/verbs to perform actions like transferring calls, collecting input, streaming media, recording, conferencing, queueing, and integrating real-time services. This page summarizes each core verb’s purpose, key attributes, nesting rules, callbacks, and simple examples.

## Dial
Transfers the current call to one or more destinations (phone numbers, SIP URIs, or a queue). If the called party doesn’t answer, the number doesn’t exist, or a busy signal is received, the attempted call is ended.

- Attributes
  - action: URL to fetch next TeXML after the Dialed call ends.
  - method: GET or POST for action. Default POST.
  - callerId: E.164 caller ID to present.
  - fromDisplayName: Display name (max 128 chars; letters, numbers, spaces, -_~!.+). Defaults to callerId.
  - hangupOnStar: Allow the original caller to hang up by pressing *. Default false. (Not for Conference.)
  - timeout: Seconds to wait for answer (5–120). Default 30.
  - timeLimit: Max call duration in seconds (60–14400). Default 14400.
  - record: Record both legs when dialing Number/Sip. Options: do-not-record, record-from-answer, record-from-ringing, record-from-answer-dual, record-from-ringing-dual. Default do-not-record.
  - recordingChannels: single (mono) or dual (stereo). Default single.
  - recordMaxLength: Max recording seconds (0–14400). 0 = unlimited. Default 0.
  - recordingStatusCallback: URL for recording status webhooks.
  - recordingStatusCallbackMethod: GET or POST. Default POST.
  - recordingStatusCallbackEvent: in-progress, completed, absent (space-separated). Default completed.
  - sendRecordingUrl: Include recording URL in callbacks. Default true.
  - ringTone: Region-specific ringback (e.g., us, uk, de, fr, …). Default us.
  - audioUrl: Custom ringback audio URL. Overrides ringTone.
  - answerOnBridge: If true and the inbound call isn’t yet answered, answer only when the dialed call answers (preserves ringing to caller). Default false.
  - sequential: If true, dial multiple destinations one-by-one; otherwise, simultaneous dialing. Default false.
  - passDiversionHeader: Pass inbound Diversion header to outbound leg. Default false.
  - machineDetectionSpeechThreshold / machineDetectionSpeechEndThreshold / machineDetectionSilenceTimeout: Advanced thresholds used only with AMD when detectionMode is Premium.

- Child nouns
  - Number: Dial a phone number.
  - Sip: Dial a SIP endpoint.
  - Queue: Enqueue the call (before bridging later).

- Number attributes
  - statusCallback: URL for outbound leg events.
  - statusCallbackEvent: initiated, ringing, answered, amd, dtmf, completed, deepfake (space-separated). Default completed.
  - statusCallbackMethod: GET or POST. Default POST.
  - url: TeXML URL for callee pre-connect flow (callee still hears ringback). Supports verbs like Gather/Hangup.
  - method: GET or POST for url. Default POST.
  - sendDigits: DTMF to play on answer (0–9, #, *, w=0.5s pause).
  - machineDetection: Enable, DetectMessageEnd, or Disable. Default Disable.
  - detectionMode: Regular, Premium, or PremiumCallScreening (iOS screening). Default Regular.
  - machineDetectionTimeout: Overall detection timeout ms (500–60000). Default 3500.
  - machineDetectionPromptEndTimeout: Silence ms after iOS screening prompt (1000–120000) for PremiumCallScreening.
  - deepfakeDetection: Enable to analyze voice authenticity.
  - deepfakeDetectionCallbackUrl: URL for deepfake detection results (or include "deepfake" in statusCallbackEvent to use statusCallback).

- Sip attributes
  - username / password: SIP authentication credentials (optional).
  - statusCallback / statusCallbackEvent / statusCallbackMethod: Same semantics as Number.
  - url / method: Optional callee pre-connect TeXML and HTTP method.
  - machineDetection / detectionMode / machineDetectionTimeout / machineDetectionPromptEndTimeout: AMD options (as above).

- Queue attributes (when used under Dial)
  - url: TeXML executed on the queued call before bridging (e.g., Play, Say, Gather, Pause, Redirect).
  - method: GET or POST for url. Default POST.

- Simultaneous dialing
  - Specify multiple Number/Sip nouns. All are dialed; first to answer is connected; others hang up.

- Sequential dialing
  - Set sequential="true" to try destinations one-by-one in order until answered.

- Expected callbacks
  - If action is set, a callback is sent when the Dialed call ends (see Dial Action Callback at https://developers.telnyx.com/api-reference/callbacks/texml-call-completed). Failed calls include error_code and error_message (see API Errors at https://developers.telnyx.com/development/api-fundamentals/api-errors/).
  - If statusCallbackEvent includes these events, webhooks are sent:
    - initiated: https://developers.telnyx.com/api-reference/callbacks/texml-call-initiated
    - ringing: https://developers.telnyx.com/api-reference/callbacks/texml-call-ringing
    - answered: https://developers.telnyx.com/api-reference/callbacks/texml-call-answered
    - completed: https://developers.telnyx.com/api-reference/callbacks/texml-call-completed
  - If machineDetection is enabled, AMD callback: https://developers.telnyx.com/api-reference/callbacks/texml-call-amd
  - If deepfakeDetection is enabled, Telnyx sends a deepfake detection callback (to deepfakeDetectionCallbackUrl or statusCallback when "deepfake" is in statusCallbackEvent) including DeepfakeResult (real, fake, or silence_timeout), DeepfakeScore (0.0–1.0), DeepfakeConsistency (0–100), or DeepfakeError on failure.
  - If recordingStatusCallbackEvent is set, recording webhooks:
    - in-progress: https://developers.telnyx.com/api-reference/callbacks/texml-recording-in-progress
    - completed: https://developers.telnyx.com/api-reference/callbacks/texml-recording-completed

- Examples
```xml
<Response>
  <Dial action="/nextinstructions.php" callerId="+13120001234">+19999999999</Dial>
</Response>
```
```xml
<Response>
  <Dial sequential="true">
    <Number>+18775551212</Number>
    <Sip>sip:connection@sip.telnyx.com</Sip>
    <Number>+18771234567</Number>
  </Dial>
</Response>
```

## Say
Speaks text to the caller using text-to-speech (TTS).

- Attributes
  - voice: Basic voices man, woman (en-US) or premium alice, or provider-specific voices:
    - Amazon Polly: Polly.VoiceId or Polly.VoiceId-Neural; AWS.Polly.VoiceId
    - Azure: Azure.VoiceId (supports gender and effect)
    - ElevenLabs: ElevenLabs.ModelId.VoiceId (requires api_key_ref)
    - Telnyx: Telnyx.ModelId.VoiceId
    - Resemble AI: Resemble.ModelId.VoiceId
    - Minimax: Minimax.ModelId.VoiceId
    - Rime: Rime.ModelId.VoiceId
    - Inworld: Inworld.ModelId.VoiceId
    Default: man.
  - language: ISO language (for alice). Ignored for man/woman and when a specific Polly voice is used.
  - loop: Repeat count (0–10; 0 = infinite). Default 1.
  - gender: Male or Female (Azure voices only).
  - effect: Audio effect (Azure voices). Values: eq_telecomhp8k, eq_car.
  - voiceSpeed: 0.1–2.0; default 1.
  - api_key_ref: Integration secret reference for provider auth (e.g., ElevenLabs, Azure).
  - region: Provider region (required for Azure with custom API key).
  - pronunciationDictId: UUID of pronunciation dictionary to apply.
  - languageBoost: Language hint for Telnyx Qwen3TTS (full names or ISO 639-1 codes: en, de, zh, fr, it, ja, ko, pt, ru, es; or Auto).

- Example
```xml
<Response>
  <Say voice="alice">Welcome to our service.</Say>
</Response>
```
