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

*Part 3 of 3 — see also: [Part 1](texml-verbs-voice-call-control-reference--part-1.md), [Part 2](texml-verbs-voice-call-control-reference--part-2.md)*

A consolidated reference to core TeXML verbs for building programmable voice call flows on Telnyx—covering behavior, attributes, child nouns, callbacks, and concise examples for Dial, Say, Play, Gather, Record, Conference, Enqueue/Leave, Hangup, Pause, Redirect, Reject, Start/Stop, and Connect.

## Leave
Removes the call from the queue and resumes the flow after the original Enqueue. No attributes.

- Example
```xml
<Response>
  <Leave/>
</Response>
```

## Hangup
Ends the call immediately.

- Expected callbacks
  - On call end, Telnyx sends Call Completed to the connection-level webhook: https://developers.telnyx.com/api-reference/callbacks/texml-call-completed

- Example
```xml
<Response>
  <Hangup/>
</Response>
```

## Pause
Waits silently for a number of seconds (default 1). No children; use as a self-closing tag.

- Attribute
  - length: Seconds to pause (1–180). Default 1.

- Example
```xml
<Response>
  <Pause length="5"/>
</Response>
```

## Redirect
Transfers control to another TeXML document. No child nouns allowed.

- Attribute
  - method: GET or POST for the Redirect URL. Default POST.

- Example
```xml
<Response>
  <Redirect method="POST">https://example.com/next-instructions</Redirect>
</Response>
```

## Reject
Rejects an incoming call to your Telnyx number. Acts as an exit—execution does not continue after Reject. If used as the first verb on an incoming call, the call is never answered (no cost). If used later, the call ends and usage up to that point is billed. Cannot be nested or contain children.

- Attribute
  - reason: rejected or busy. Default rejected.

- Example
```xml
<Response>
  <Reject reason="busy"/>
</Response>
```

## Start
Starts a service defined by the nested noun, then immediately continues with the next TeXML instructions (asynchronous start).

- Child nouns
  - Suppression: Start noise suppression.
  - Transcription: Start real-time transcription.
  - Stream: Start media stream over WebSocket.

## Stop
Stops a running instruction specified by the child noun.

- Child nouns
  - Suppression: Stop current suppression.
  - Transcription: Stop current transcription.
  - Stream: Stop current media stream.

- Example
```xml
<Response>
  <Stop>
    <Stream/>
  </Stop>
</Response>
```

## Connect
Starts the service defined by the nested noun in synchronous mode. TeXML pauses and only continues to subsequent instructions after the service stops.

- Child nouns
  - Stream: Start media streaming over WebSocket.
  - ConversationRelay: Route a call to a ConversationRelay service for voice interactions over WebSocket.
