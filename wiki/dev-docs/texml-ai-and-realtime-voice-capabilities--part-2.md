---
title: TeXML AI and Real‑Time Voice Capabilities
summary: Build natural, interactive voice experiences on Telnyx using TeXML verbs
  for AI assistants, structured data collection, WebSocket conversations, real‑time
  media streaming, transcription, SIPREC recording, noise suppression, HTTP integrations,
  and call transfers.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
  content_hash: f10f4c3561eadcf6a96c01be07f43a5b9b596e83b0fa6767bde0c993b8eb999f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
  content_hash: 6b7d27457d6afbe022f10cd6fb869f091663913bde7c6d0a9180faab825a5898
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
  content_hash: f024265782dc4e08449f39f6d071d81f84116b0f5224b53f0182e3a7ec1cbef2
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
  content_hash: 0a1072716fca8dcfe298529d3e2858c151e359924f5534013eb4006a21e92ed7
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
  content_hash: 0059440d5255c9f7c0901c3e80c3ef95330a51f230d03ca13c201eab7108b64f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
  content_hash: 5f68ba1cb2cf7eca555762b38991cdcc70b3b0d37377f69d08769f422faedda4
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
  content_hash: e25a87117c0cd3a7af06dc3f2ddba6282786c3433ef04d696736d730db496817
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
  content_hash: 81813db23a8a46e4bd6080e72cc3b0dccc7e924dc0efeff9f7f069e9ee30fc20
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
  content_hash: c37b3aecde59854f5ef3d8d07b58fa9101de6c0ec75288622ee56a386707d27a
updated_at: 2026-05-20T09:39:10Z
---

# TeXML AI and Real‑Time Voice Capabilities

*Part 2 of 2 — see also: [Part 1](texml-ai-and-realtime-voice-capabilities--part-1.md)*

Build natural, interactive voice experiences on Telnyx using TeXML verbs for AI assistants, structured data collection, WebSocket conversations, real‑time media streaming, transcription, SIPREC recording, noise suppression, HTTP integrations, and call transfers.

## <Transcription> — real‑time speech‑to‑text
Enables STT on one or both legs with multiple providers and models.
- language: Recognition language (default en); see engine configs
- interimResults: If true, include interim hypotheses (applies to legacy engine A)
- transcriptionEngine: Google (default), Telnyx, Deepgram, Azure, xAI, AssemblyAI, Soniox, Speechmatics; legacy A→Google, B→Telnyx
- transcriptionTracks: inbound | outbound | both (default inbound)
- transcriptionCallback: URL for transcription events
- transcriptionCallbackMethod: GET | POST (default POST)
- model: Optional model for the chosen engine
- apiKeyRef: Reference to provider credentials (see Integration Secrets)
- region: Provider region (required for Azure)

Example — Google with interim results
```
<Response>
  <Start>
    <Transcription language="en" interimResults="true" transcriptionCallback="/transcription" />
  </Start>
</Response>
```

Callbacks: If transcriptionCallback is set, results stream as available (Transcription Callback: https://developers.telnyx.com/api-reference/callbacks/texml-transcription).

## <Siprec> — standards‑based recording to your SRS
Starts or stops a SIPREC session to a configured external connector.
- connectorName: Which SIPREC connector to use
- statusCallback: URL for SIPREC status webhooks
- statusCallbackMethod: GET | POST (default POST)
- track: inbound_track | outbound_track | both_tracks (default both_tracks)
- name: Session name (also used to stop)
- includeMetadataCustomHeaders: If false, custom params go to SIP headers instead of metadata (default false)
- secure: Use SRTP/TLS to encrypt media (requires SRS port 5061; default false)
- sessionTimeoutSecs: Session‑Expires header value; min 90, 0 disables; default 1800

Example — start and stop
```
<Response>
  <Start>
    <Siprec name="siprec_session" track="both_tracks" connectorName="my-connector" statusCallback="https://example.com/siprec_callback" />
  </Start>
</Response>
```
```
<Response>
  <Stop>
    <Siprec name="siprec_session" />
  </Stop>
</Response>
```

Callbacks: siprec-started, siprec-stopped, siprec-failed (SIPREC Callback: https://developers.telnyx.com/api-reference/callbacks/texml-siprec).

## <Suppression> — noise reduction on the call
Enables denoising for one or both directions.
- direction: inbound | outbound | both (default inbound)

Example
```
<Response>
  <Start>
    <Suppression direction="both" />
  </Start>
</Response>
```

## <HttpRequest> — call external APIs from TeXML
Sends an HTTP request mid‑flow. Structure:
- Attributes on <HttpRequest>:
  - async: If true (default), TeXML does not wait; if false, TeXML waits and then sends a callback to action when request is processed
  - action: Required only when async=false; where to send the completion callback
- Children:
  - <Request> with url, method, optional <Headers> and <Body> (use CDATA for raw payloads)
  - <Response> to map expected response data into variables (via <Headers> and <Body> content mapping)

Example — async request
```
<Response>
  <HttpRequest async="true">
    <Request url="https://example.com" method="POST">
      <Headers>
        <Header><Key>Authorization</Key><Value>Bearer API_key</Value></Header>
        <Header><Key>Content-Type</Key><Value>application/json</Value></Header>
      </Headers>
      <Body>
        <![CDATA[{"from": {{From}}}]]>
      </Body>
    </Request>
  </HttpRequest>
</Response>
```

Callback: When async=false, TeXML posts to action after processing (HTTP Request Callback: https://developers.telnyx.com/api-reference/callbacks/texml-http-request).

## <Refer> — transfer the call to external SIP
Transfers the current call to another SIP system; can occur at any point in the call.
- action: Optional URL to fetch new TeXML after the refer completes
- method: GET | POST for that follow‑up fetch (default POST)

Example
```
<Response>
  <Refer>
    <Sip>sip:john@example.com</Sip>
  </Refer>
</Response>
```

Callback: If action is set, Telnyx calls it when the refer finishes (Refer Status Callback: https://developers.telnyx.com/api-reference/callbacks/texml-refer-status).
