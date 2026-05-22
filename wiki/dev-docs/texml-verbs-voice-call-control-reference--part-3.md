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
