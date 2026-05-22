---
title: 'TeXML Verbs: Voice Call Control Reference'
summary: A consolidated reference to core TeXML verbs for building programmable voice
  call flows on Telnyx—covering behavior, attributes, child nouns, callbacks, and
  concise examples for Dial, Say, Play, Gather, Record, Conference, Enqueue/Leave,
  Hangup, Pause, Redirect, Reject, Start/Stop, and Connect.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
  content_hash: a9a66c36cbc670f26744f26a62bc438d4481a60bb181f382c665fafab6c9d9bd
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
  content_hash: cfaef0151ebf26f9cc837267989c978faf995e201e2fd940e7c21ac8b45be04f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
  content_hash: c648ada8aba2dcde9b90da99dd57025be58c01c88abf029b56565e7b4bf6932c
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
  content_hash: eb0a4d7b3fd1833935ae0e922fe165daf591d378078505a18294177efd8c8611
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
  content_hash: a6d9e75ad8b2609983f94c6bd129ca5c3811a29f3751e4710297561dcd41e6b5
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
  content_hash: 489ddd73e8c9d930034215a47121a855333d05e5731aba02143727408f6ac88f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
  content_hash: 6a074bfbce54768841c3466bca774213f27e0ebe703ed02a07a7e17153e82927
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
  content_hash: db062801130cb924239be13233273efb6f414f70c57cc203e7eb5e5acc1da5fc
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
  content_hash: 1288cda57575422a7fd1244743627dab3d71792134a7bb0f9835dfaab2786d40
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
  content_hash: b3b33c465017ce623e9a922bbb22548f1d02d7d56d265a8d525c77b212b66ad4
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
  content_hash: 3478af66f8181e2d8f96532d8cfac6b9ec16da0af660fa83c5297fde1c54b64e
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
  content_hash: eba4b1eefd2e8e1ab2b9be6fae4888e0e249653368bde3961643fe46cadcbf2a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
  content_hash: c5e05b907be65e739bd1ece208da8eef1b1bf34df15a0ea3b1c9a4cedddcf58c
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
  content_hash: b182da81078b80a494a9d9bef2c1dcd0bd84eb227273c876b7bcac5ec64bb78c
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
  content_hash: 36de2c4787eeef92627335fb0c098feab0c8fa3705a1c39dd9ae62b64e4316f0
updated_at: 2026-05-20T09:38:14Z
---

# TeXML Verbs: Voice Call Control Reference

*Part 2 of 3 — see also: [Part 1](texml-verbs-voice-call-control-reference--part-1.md), [Part 3](texml-verbs-voice-call-control-reference--part-3.md)*

A consolidated reference to core TeXML verbs for building programmable voice call flows on Telnyx—covering behavior, attributes, child nouns, callbacks, and concise examples for Dial, Say, Play, Gather, Record, Conference, Enqueue/Leave, Hangup, Pause, Redirect, Reject, Start/Stop, and Connect.

## Play
Plays audio (MP3/WAV) fetched from a URL, or from Telnyx Media Storage, or DTMF tones instead of audio.

- Attributes
  - loop: Times to repeat. Default 1.
  - mediaStorage: true to fetch by media name from Telnyx storage; when true, provide media_name in the verb body instead of a URL. Default false.
  - digits: DTMF to play (0–9, *, #, w=0.5s pause). When set, tones play instead of an audio file.

- Example
```xml
<Response>
  <Play>https://example.com/welcome.mp3</Play>
</Response>
```

## Gather
Collects user input via DTMF and/or speech. You can nest Say/Play to prompt the caller. When Gather completes, TeXML requests the action URL with the result and message history and transfers control to the returned document.

- Attributes
  - action: URL to send the gathered result and message history; call control transfers to the returned TeXML.
  - timeout: Seconds between digits before sending (1–120). Default 5. Starts after nested verbs finish.
  - input: dtmf, speech, or dtmf speech. Default dtmf.
  - speechTimeout: Seconds to wait after speech ends.
  - partialResultCallback: URL for partial recognition results.
  - partialResultCallbackMethod: GET or POST. Default POST.
  - profanityFilter: Filter profanity from ASR results.
  - useEnhanced: Enable enhanced transcription (e.g., for phone_call/video models).
  - hints: Phrases to improve recognition.
  - transcriptionEngine: Google, Telnyx, Azure, Deepgram, xAI, AssemblyAI, Soniox, Speechmatics.
  - apiKeyRef: Integration secret reference (required for some engines; Azure may require it).
  - region: Region for engine (required for Azure). See regions in transcription_engine_config.
  - finishOnKey: One or more keys (0–9, *, #) that end the gather. Default #.
  - numDigits: Exact number of digits to collect (optional).
  - language: TTS/recognition language (default en-US). See supported values in REST speak-text docs.
  - validDigits: Restrict acceptable digits.
  - invalidDigitsAction: URL to receive invalid entries (transfers control like action).
  - minDigits: 1–128. Default 1.
  - maxDigits: 1–128. Default 128.

- Child nouns
  - Say
  - Play

- Example
```xml
<Response>
  <Gather timeout="5" numDigits="1" finishOnKey="#">
    <Say>Press 1 for sales, press 2 for support.</Say>
  </Gather>
</Response>
```

- Expected callbacks
  - Gather completion (with digits/speech) to action URL: https://developers.telnyx.com/api-reference/callbacks/texml-gather

## Record
Records call audio and optionally transcribes it. If recordingStatusCallback is provided, Telnyx delivers the recording URL after the call ends (recording URLs are valid for 10 minutes). All recordings are also available in the Telnyx Mission Control Portal.

- Attributes
  - action: URL to fetch next TeXML when Record ends (additional params are sent).
  - method: GET or POST for action. Default POST.
  - finishOnKey: Any of these keys end recording (digits, #, *). Default 1234567890*#.
  - timeout: Seconds to wait to auto-stop after silence is detected (0 = infinite). Timer starts on detected speech; transcription may be used for silence detection and billed accordingly. Default 0.
  - maxLength: Max recording length seconds (0–14400; 0 = infinite). Default 3600.
  - playBeep: Play a beep before recording starts. Default true.
  - trim: trim-silence to remove leading/trailing silence.
  - channels: single or dual. Default dual (A channel for first leg, B for others).
  - recordingStatusCallback: URL for recording webhooks.
  - recordingStatusCallbackMethod: GET or POST. Default POST.
  - transcription: true/false to enable transcription. Default false.
  - transcriptionCallback: URL to receive the transcription result.
  - transcriptionEngine: A or B. Default A.
  - transcriptionLanguage: Language for transcription. Default en-US.
  - format: mp3 or wav. Default mp3.
  - recordingStatusCallbackEvent: in-progress, completed (space-separated). Default completed.

- Expected callbacks
  - Recording status: in-progress, completed
    - https://developers.telnyx.com/api-reference/callbacks/texml-recording-in-progress
    - https://developers.telnyx.com/api-reference/callbacks/texml-recording-completed
  - Transcription (when enabled): https://developers.telnyx.com/api-reference/callbacks/texml-transcription

- Example
```xml
<Response>
  <Say voice="Telnyx.KokoroTTS.af">This call will be recorded and transcribed for quality purposes.</Say>
  <Record action="https://example.com/recording-complete"
          method="POST"
          maxLength="60"
          timeout="5"
          transcription="true"
          transcriptionEngine="A"
          transcriptionCallback="https://example.com/transcription-result"/>
</Response>
```

## Conference
Use the Conference noun inside Dial to connect the caller to a named conference room. If the room doesn’t exist, it’s created. Commonly used to implement hold, transfer, and barge use-cases.

- Conference attributes (under Dial)
  - muted: Mute the participant. Default false.
  - startConferenceOnEnter: If false, participant is muted and hears music until anyone with true joins. Default true.
  - endConferenceOnExit: If true for a participant, the conference ends when they leave (others drop) so each leg can continue its TeXML independently. Default false.
  - maxParticipants: 2–250. Default 250.
  - beep: Join/leave notification beep control: true, false, onEnter, onExit. Default true. (Does not affect recording start beep.)
  - participantLabel: Unique label to reference/update the participant via REST.
  - record: do-not-record or record-from-start. Default do-not-record.
  - recordBeep: Beep when recording starts. Independent of beep. Default true.
  - recordingStatusCallback / recordingStatusCallbackEvent / recordingStatusCallbackMethod: Recording webhook configuration. Events: in-progress, completed, absent. Default event completed; method POST.
  - recordingTimeout: Silence-based auto-stop seconds (0–14400; 0 = no timeout). May use transcription for silence detection and be billed.
  - trim: trim-silence or do-not-trim. Default do-not-trim.
  - sendRecordingUrl: Include recording URL. Default true.
  - statusCallback / statusCallbackMethod / statusCallbackEvent: Conference lifecycle webhooks; method default POST; events include start, end, join, leave, speaker.
  - waitUrl: MP3/WAV URL or an XML document to execute while waiting for the conference to start.
  - waitMethod: GET or POST for waitUrl. Default POST.

- Expected callbacks
  - start: https://developers.telnyx.com/api-reference/callbacks/texml-conference-start
  - end: https://developers.telnyx.com/api-reference/callbacks/texml-conference-end
  - join: https://developers.telnyx.com/api-reference/callbacks/texml-conference-join
  - leave: https://developers.telnyx.com/api-reference/callbacks/texml-conference-leave
  - speaker: https://developers.telnyx.com/api-reference/callbacks/texml-conference-speaker

- Example
```xml
<Response>
  <Dial action="/nextinstructions.php">
    <Conference>conference_name</Conference>
  </Dial>
</Response>
```

## Enqueue
Enqueues the current call in a queue.

- Attributes
  - action: URL called when the call leaves the queue. If dequeued via Leave, it’s sent immediately; if dequeued via Dial (bridging), it’s sent after the bridged call disconnects.
  - method: GET or POST for action. Default POST.
  - waitUrl: TeXML document executed while the call waits. After it finishes, Telnyx re-requests and repeats it. Supported verbs in waitUrl doc: Play, Say, Gather, Pause, Hangup, Redirect, Leave.
  - waitUrlMethod: GET or POST for waitUrl. Default POST.
  - maxWaitTimeSecs: Max seconds to remain in queue (min 1). Default 14400.

- Expected callbacks
  - Queue enter (if waitUrl is set): https://developers.telnyx.com/api-reference/callbacks/texml-queue

- Example
```xml
<Response>
  <Enqueue/>
</Response>
```
