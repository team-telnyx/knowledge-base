---
title: Telnyx Programmable Voice
summary: Telnyx Programmable Voice provides tools for building voice applications
  including SIPREC recording, speech-to-text transcription, call recording storage,
  SSML-based text-to-speech, and the TeXML markup language for declarative call control
  with TwiML compatibility.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
  content_hash: 5f20f9da47913df819e8853ce1bec7cc18ca3b72a65481e97e8d8abdb21b434a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
  content_hash: aef1769dcaf3a6fe330e8715353328de8017840a5721dd354fc9a3bf06365913
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ssml-tags/index
  content_hash: 743eececec66347e73b016b8e53fe085c9add6df952c4b1614da8b9f891f7d60
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
  content_hash: 6fe6973bbc0653ed56eeb8806cd7baf759741e9dfd020b80b419a85120b8bc7b
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
  content_hash: 21442960c192f1e45263da4b0688fc7e40876769ca13bb33818906d5cae00636
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
  content_hash: 1e29367f33838ffb5b350698efa550f61e565e89e5f3c84035a686753a439ce1
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
  content_hash: 2a4ce735c57a6005b294b5374901754f96446dcaf05589cd825071a79a3f204a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
  content_hash: 7d515a5f4f318ce48b9d85f83981ae2336cdb09ad210e839ce53ddd326b0d93b
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
  content_hash: 78104abb8c6285534e3c1bfa5d136d35aadce02101459fc4f5895ca46ec9d2ff
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
  content_hash: 5609b58aa97391f6557c477b6c5103aa53176e6473ae203722d8bd1dee7fca34
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
  content_hash: e14b54eae87e5ce08bd0427af6eecc57ec3adba060f6024566012b78153adb6f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
  content_hash: 7394df1156c0c5b3a487f470a9fd996bf976c78e759b5b414defe424c1d2f5c4
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
  content_hash: 5c10e721340bceb989599c29d93823ad1ac2980c05d2c116d3769e9375b08117
updated_at: 2026-06-11T10:43:02Z
---

# Telnyx Programmable Voice

*Part 1 of 3 — see also: [Part 2](telnyx-programmable-voice--part-2.md), [Part 3](telnyx-programmable-voice--part-3.md)*

Telnyx Programmable Voice provides tools for building voice applications including SIPREC recording, speech-to-text transcription, call recording storage, SSML-based text-to-speech, and the TeXML markup language for declarative call control with TwiML compatibility.

## SIPREC Server Configuration

SIPREC (Session Initiation Protocol Recording) is a standardized mechanism for recording VoIP calls. A SIPREC server, also known as a Session Recording Server (SRS), captures and stores communications for compliance, quality assurance, and other purposes.

### Setting Up the SIPREC Server Environment

1. **Create a Voice API Application** — In the [Telnyx portal](https://portal.telnyx.com), navigate to Voice → Programmable Voice → Voice API and create a new application with a meaningful name and description.
2. **Assign an Inbound SIP Subdomain** — Within the application's Inbound Settings, assign a subdomain (e.g. `yourcompany.sip.telnyx.com`) that will route incoming SIP traffic to your SIPREC server.
3. **Configure the SIPREC Client (SRC)** — Point your SIPREC Client at Telnyx's SRS using the URI:
   ```
   sip:username@siprec.telnyx.com;secure=true
   ```
   The `username` portion is ignored. The destination host header must be sent as a custom SIP header: `X-DestHost`.
4. **Configure SIPREC Token Authentication** — Up to two authentication tokens can be configured per connection via the API:
   ```
   curl -X PATCH 'https://api.telnyx.com/v2/call_control_applications/:connection_id' \
     -H 'content-type: application/json' -H 'authorization: Bearer <api-key>' \
     --data-raw '{"siprec_tokens": ["test-token1", "test-token2"] }'
   ```
   Once tokens are created, every SIPREC INVITE must include the `X-Auth-Token` SIP header. The token is verified against the two configured values; only a match allows the call to proceed.
5. **Initiate and Record the SIPREC Call** — When the SIPREC session starts, two `call.initiated` webhooks are sent (one for each RTP stream). Each webhook includes a `call_control_id` and custom SIP headers with SIPREC metadata. Use the `call_control_id` to answer and start recording:
   ```
   curl -L 'https://api.telnyx.com/v2/calls/{call_control_id}/actions/answer' \
     -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{}'
   ```
   ```
   curl -L 'https://api.telnyx.com/v2/calls/{call_control_id}/actions/record_start' \
     -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' -d '{}'
   ```

### SIPREC Call Flow

1. A call is established on the user's SBC (with SIPREC SRC capabilities) with RTP streams A and B.
2. The SIPREC SRC initiates a SIPREC call toward Telnyx's SRS (`siprec.telnyx.com`) with two RTP streams.
3. The Telnyx SRS initiates two SIP calls toward `sip.telnyx.com`, one for each RTP stream, each with `a:sendonly`.
4. Telnyx sends two `call.initiated` webhooks to the Voice API application URL, each containing a `call_control_id` and the original SIPREC metadata.
5. The `call_control_id` values are used to issue Voice API commands to answer and record both calls.

### SIPREC Metadata

Telnyx passes metadata from the SIPREC INVITE as custom SIP headers on the resulting SIP calls. Each webhook contains:

- **to** — the content of the SIP URI
- **SIP Custom headers** — any SIP custom headers from the INVITE
- **SIPREC XML default metadata** — extracted fields include `DataMode`, `ParticipantID`, `NameID-AOR`, `Associate-Time`, `StreamID`, and `Label`
- **SIPREC XML custom metadata** — any custom variables extracted from the XML metadata

## Speech-to-Text Transcription

Telnyx provides real-time speech-to-text transcription for calls via both Voice API and TeXML.

### Supported Engines

| Engine | Notes |
|--------|-------|
| Google | Default engine; supports interim results |
| Telnyx | In-house engine with better accuracy and lower latency |
| Deepgram | Models: nova-2, nova-3, flux (set via `transcription_model`) |
| Azure | Strong multi-language and accent support |
| xAI | `xai/grok-stt` model |
| AssemblyAI | `assemblyai/universal-streaming` model |
| Speechmatics | `speechmatics/standard` model; multilingual and bilingual language packs |
| Soniox | `soniox/stt-rt-v4` model; automatic language detection with interim results and endpointing |

### Voice API Transcription

Use the dedicated [transcription start endpoint](https://developers.telnyx.com/api-reference/call-commands/transcription-start):

```curl -i -X POST \
  'https://api.telnyx.com/v2/calls/{call_control_id}/actions/transcription_start' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "language": "en",
    "transcription_engine": "Google"
  }'
```

Transcription results are delivered as `call.transcription` webhooks containing `transcription_data` with `confidence`, `is_final`, and `transcript` fields.

### TeXML Transcription

Include a `<Transcription>` verb inside a `<Start>` block:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription language="en" transcriptionCallback="/transcription" transcriptionEngine="Telnyx" />
  </Start>
</Response>
```

Results are sent to the `transcriptionCallback` URL with fields including `CallSid`, `Confidence`, `IsFinal`, `Transcript`, `From`, and `To`.

## SSML Tags for Text-to-Speech

Speech Synthesis Markup Language (SSML) is an XML-based language used to customize synthetic speech by adjusting pitch, volume, duration, and pronunciation.

### Available SSML Tags

| Tag | Purpose | Key Attributes |
|-----|---------|----------------|
| `<break>` | Add a pause | `time` (e.g. `3s`), `strength` (none, pause, x-weak, weak, medium, strong, x-strong) |
| `<emphasis>` | Emphasize words | `level` (strong, moderate, reduced) — affects speed and loudness |
| `<lang>` | Set a different language | `xml:lang` (e.g. `es`) |
| `<p>` | Pause between paragraphs | None — adds a longer pause than sentence-end |
| `<phoneme>` | Phonetic pronunciation | `alphabet` (ipa, x-sampa), `ph` (phonetic spelling) |
| `<prosody>` | Control volume, rate, pitch | `volume` (silent–x-loud, ±ndB), `rate` (x-slow–x-fast, n%) |
| `<s>` | Pause between sentences | None — same effect as a period |
| `<say-as>` | Control how special words are spoken | `interpret-as` (characters, cardinal, digits, fraction, unit, date, time, address, telephone) |
| `<sub>` | Pronounce acronyms/abbreviations | `alias` — substitutes a different word |

Example — adding a pause and emphasis:

```xml
<speak> Mary had a little lamb <break time="3s"/>Whose fleece was white as snow. </speak>
```

```xml
<speak> I already told you we're <emphasis level="strong">nearly</emphasis> there </speak>
```
