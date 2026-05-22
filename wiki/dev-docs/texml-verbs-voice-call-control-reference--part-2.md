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
