---
title: Text-to-Speech
summary: In this tutorial, you will learn how to get a Text-To-Speech service on your calls using Voice API and TeXML.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/tts/index
    content_hash: c3e71915e5b46965437c7fd5f35877e44cbf03aef8c32ee3565a9de9f3c5caa0
updated_at: 2026-04-10T00:00:00Z
---

# Text-to-Speech

In this tutorial, you will learn how to get a Text-To-Speech service on your calls using Voice API and TeXML.

Before starting, please ensure your [Voice API](https://developers.telnyx.com/docs/voice/programmable-voice/get-started) or [TeXML](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup) application is correctly configured.

## Video Tutorial

Watch this comprehensive video demonstration to see Text-to-Speech features in action:

<iframe />

This video demonstrates how to use Telnyx's Text-to-Speech capabilities to create dynamic voice interactions in your applications.

## Telnyx Ultra

Telnyx Ultra is a next-generation text-to-speech engine delivering **ultra-quality** voice synthesis with **low latency** and support for **44 languages**. It produces highly natural and expressive speech, making it a great choice for premium voice experiences.

You can request Telnyx Ultra voices for your calls using the Voice API:

```shell theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data '{
    "voice": "Telnyx.Ultra.3e1ed423-17e5-4773-b87c-25b031106e41"
}'
```

You can integrate Telnyx Ultra into TeXML scripts using the following format:

```xml theme={null}

    <Say voice="Telnyx.Ultra.3e1ed423-17e5-4773-b87c-25b031106e41">The text that should be said on the call!

```

## Telnyx internal Text-to-Speech engine

Telnyx provides a high-quality, low-latency Text-to-Speech (TTS) engine, offering a seamless experience for integrating speech synthesis into your calls. The Telnyx TTS engine ensures a clear and natural-sounding voice, making it an excellent choice for real-time voice applications.

You can request Telnyx TTS for your calls using the Voice API. Below is an example of how to trigger speech synthesis with Telnyx TTS:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Telnyx.KokoroTTS.af"
}'
```

You can integrate Telnyx TTS into TeXML scripts using the following format:

```bash theme={null}

    <Say voice="Telnyx.KokoroTTS.af">The text that should be said on the call!

```

With its high-quality voices and low latency, Telnyx TTS is an excellent choice for users seeking to integrate natural-sounding speech into their applications.

## Telnyx Natural

Telnyx Natural voices provide enhanced speech quality with improved naturalness and clarity. These voices offer a significant upgrade from basic text-to-speech options, delivering more human-like speech patterns and better pronunciation accuracy.

You can request Telnyx Natural voices for your calls using the Voice API:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Telnyx.Natural.abbie"
}'
```

You can integrate Telnyx Natural voices into TeXML scripts using the following format:

```xml theme={null}

    <Say voice="Telnyx.Natural.abbie">The text that should be said on the call!

```

## Telnyx NaturalHD

Telnyx NaturalHD voices deliver premium-quality speech synthesis with exceptional clarity and richness. These high-definition voices are ideal for applications where audio quality is critical, such as customer service, media production, or premium user experiences.

You can request Telnyx NaturalHD voices for your calls using the Voice API:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Telnyx.NaturalHD.andersen_johan"
}'
```

You can integrate Telnyx NaturalHD voices into TeXML scripts using the following format:

```xml theme={null}

    <Say voice="Telnyx.NaturalHD.andersen_johan">The text that should be said on the call!

```

## AWS Polly

Telnyx offers both levels of quality for AWS Polly Text-To-Speech services: neural and standard. The list of voices can be found under the [link](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html).

It can be requested on the call using the Voice API command similar to:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Polly.Brian" || "Polly.Amy-Neural" 
}'
```

It should be used in the following way from TeXML script:

```xml theme={null}

    <Say voice="Polly.Amy-Neural">The text that should be said on the call!

```

The neural voice can be used by adding the prefix to the voice name - `Polly.*-Neural`

Before you use it, please take a look at the price list under the [link](https://telnyx.com/pricing/call-control).

## Azure AI Speech

Telnyx supports Azure AI Speech as a text-to-speech provider.
You can find the list of supported voices and languages at the following [link](https://speech.microsoft.com/portal/voicegallery).

To use Azure AI Speech, the process is the same as with AWS Polly. Voices should be specified using the following format:  <code>Azure.en-CA-ClaraNeural</code>.

Azure AI Speech supports two service levels via Telnyx:

* Neural

  * These voices use deep neural networks to generate highly natural and expressive speech.
  * Ideal for most general applications, they offer high-quality output with support for SSML to customize pronunciation, pitch, rate, and more.
  * Example: <code>Azure.en-CA-ClaraNeural</code>

* Neural HD (High Definition)

  * HD voices deliver enhanced clarity and richness for scenarios where audio quality is critical—such as media production or premium customer engagement.
  * These voices provide finer prosody control, improved phonetic detail, and natural pauses, yielding more lifelike speech.
  * Example: <code>en-US-Emma:DragonHDLatestNeural</code>

Here’s an example of using the Telnyx Voice API to synthesize speech with Azure AI Speech:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Azure.en-CA-ClaraNeural" 
}'
```

The corresponding TeXML script would look like this:

```bash theme={null}

    <Say voice="Azure.en-CA-ClaraNeural">The text that should be said on the call!

```

## ElevenLabs

Users get many voice options with ElevenLabs; however, response latency may exceed what you’d see from AWS Polly or Azure AI Speech.

To use the integration, you must provide an API key to your ElevenLabs account.

Telnyx offers to store it in a [secure storage](https://developers.telnyx.com/docs/inference/ai-assistants/importing/index#secrets). The API key can be saved in the following way:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/integration_secrets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key'' \
--data '{
    "identifier":"your_api_key_ref",
    "value":"api_key"
}'
```

The `speak` command should look as follows for the Voice API application:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should said on the call",
    "voice": "ElevenLabs.Default.cgSgspJ2msm6clMCkdW9",
    "voice_settings": {"api_key_ref": "your_api_key_ref"}
}'
```

A similar effect can be achieved from TeXML using the following script:

```xml theme={null}

    <Say voice="ElevenLabs.Default.cgSgspJ2msm6clMCkdW9" api_key_ref="your_api_key_ref">The text that should said on the call!

```

*Please note: only a premium ElevenLabs can be used for the integration. The freemium account is not supported*

## MiniMax

MiniMax offers high-quality text-to-speech with expressive voices across multiple languages and accents.

The `speak` command should look as follows for the Voice API application:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Minimax.speech-2.6-turbo.English_expressive_narrator"
}'
```

A similar effect can be achieved from TeXML using the following script:

```xml theme={null}

    <Say voice="Minimax.speech-2.6-turbo.English_expressive_narrator">The text that should be said on the call!

```

## ResembleAI

ResembleAI voices, built on the Chatterbox model, delivering AI voices that preserve emotion, style, and accent for natural sounding delivery.

The `speak` command should look as follows for the Voice API application:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Resemble.Pro.Aaron_en-US"
}'
```

A similar effect can be achieved from TeXML using the following script:

```xml theme={null}

    <Say voice="Resemble.Pro.Aaron_en-US">The text that should be said on the call!

```

## Inworld

Inworld offers expressive multilingual AI voices with two model tiers: Mini and Max.

The `speak` command should look as follows for the Voice API application:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Inworld.Mini.Loretta"
}'
```

A similar effect can be achieved from TeXML using the following script:

```xml theme={null}

    <Say voice="Inworld.Mini.Loretta">The text that should be said on the call!

```

## Rime

Rime Arcana V3 voices provide multilingual AI speech with native codeswitching across 10 languages: Arabic, English, French, German, Hebrew, Hindi, Japanese, Portuguese, Spanish, and Tamil. Voices use the `Rime.ArcanaV3.` format — check the [Available Voices](https://developers.telnyx.com/docs/tts-stt/tts-available-voices) page for specific voice names.

The `speak` command should look as follows for the Voice API application:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Rime.ArcanaV3.astra"
}'
```

A similar effect can be achieved from TeXML using the following script:

```xml theme={null}

    <Say voice="Rime.ArcanaV3.astra">The text that should be said on the call!

```


## Related Pages

- [Text-to-Speech (TTS)](../runbooks/text-to-speech-tts.md)
- [Text-to-Speech Overview](../concepts/text-to-speech-overview.md)
