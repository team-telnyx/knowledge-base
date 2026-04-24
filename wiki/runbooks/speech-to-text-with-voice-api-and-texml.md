---
title: Speech-to-Text with Voice API and TeXML
summary: Learn how to get a transcription from your calls using Voice API and TeXML.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
    content_hash: 45511805598b18aa128464b4e0d5f12dedd312ad746f33f841a647e357af05a9
updated_at: 2026-04-10T00:00:00Z
---

# Speech-to-Text with Voice API and TeXML

Learn how to get a transcription from your calls using Voice API and TeXML. Explore comprehensive documentation, tutorials, and examples to seamlessly integrate HTTP requests into your voice applications. Empower your voice communication with Telnyx's robust Programmable Voice solutions.

## Introduction

In this tutorial, we will cover how to get a speech-to-text transcription of your calls using Voice API and TeXML.

Before starting, please ensure your [Voice API](https://developers.telnyx.com/docs/voice/programmable-voice/get-started) or [TeXML](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup) application is correctly configured.

## Video Tutorial

Learn how to implement real-time Speech-to-Text recognition in your voice applications:

<iframe />

This video shows how to capture and process spoken input from callers using Telnyx's Speech-to-Text API.

## Supported engines

Telnyx offers several speech-to-text engines that can be used to process the audio from the call into a transcription:

* Google (default) - Google speech-to-text engine that offers additional features like interim results.
* Telnyx - In-house Telnyx speech-to-text engine with significantly better transcription accuracy and lower latency.
* Deepgram - Deepgram speech-to-text engine with 3 models (nova-2, nova-3 and flux) that can be set using `transcription_model` setting
* Azure - Azure speech-to-text engine with a strong support for multiple languages and accents

## Voice API

The transcription can be enabled for the Voice API calls using [a dedicated endpoint](https://developers.telnyx.com/api-reference/call-commands/transcription-start) in the following way:

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```bash theme={null}
curl -i -X POST \
'https://api.telnyx.com/v2/calls/{call_control_id}/actions/transcription_start' \
-H 'Authorization: Bearer YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
    "language": "en",
    "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
    "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
    "transcription_engine":  "Google/Telnyx/Deepgram "
}'
```

The results are sent as a webhook delivered to the webhook defined for the Voice API application:

```json theme={null}
"data": {
   "record_type": "event",
   "event_type": "call.transcription",
   "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
   "occurred_at": "2018-02-02T22:25:27.521992Z",
   "payload": {
        "call_control_id":           "v2:7subYr8fLrXmaAXm8egeAMpoSJ72J3SGPUuome81-hQuaKRf9b7hKA",
        "call_leg_id": "5ca81340-5beb-11eb-ae45-02420a0f8b69",
        "call_session_id": "5ca81eee-5beb-11eb-ba6c-02420a0f8b69",
        "client_state": null,
        "connection_id": "1240401930086254526",
        "transcription_data": {
        "confidence": 0.977219,
            "is_final": true,
            "transcript": "hello this is a test speech"
         }
    }
}
```

## TeXML

You can enable transcription on your TeXML calls by including a `` verb in the TeXML instructions:

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Transcription language="en" transcriptionCallback="/transcription" transcriptionEngine=”Telnyx” />

```

The transcription results are sent in the callback in the following format:

```json theme={null}
%{
    "AccountSid" : "6d547b4f-993a-4e87-b95c-2d9460b3824b",
    "CallSid" : "v3:xIscDTsILHoErg5d4BfFWITg7vHmTvTRm-4YEeOgrwESDQsDWQNxvw",
    "CallSidLegacy" : "v3:xIscDTsILHoErg5d4BfFWITg7vHmTvTRm-4YEeOgrwESDQsDWQNxvw",
    "Confidence" : "0.9822598695755005",
    "ConnectionId" : "1614262910593271041",
    "From" : "+18727726007",
    "IsFinal" : "true",
    "To" : "+48664087895",
    "Transcript" : "let's hear some music"
}
```


## Related Pages

- [Using SIPREC client for Voice API and TeXML calls](../runbooks/using-siprec-client-for-voice-api-and-texml-calls.md)
