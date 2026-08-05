---
title: Voice AI Assistants
summary: Telnyx Voice AI Assistants let you build, configure, and operate conversational
  voice agents entirely from the Mission Control Portal or via API. This page covers
  the no-code quickstart, supported language and transcription models, voice and noise-suppression
  settings, built-in and library tools, integrations, scheduled outbound events with
  retries, and programmatic voice control.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
updated_at: 2026-08-05T13:45:11Z
---

# Voice AI Assistants

*Part 6 of 6 — see also: [Part 1](voice-ai-assistants--part-1.md), [Part 2](voice-ai-assistants--part-2.md), [Part 3](voice-ai-assistants--part-3.md), [Part 4](voice-ai-assistants--part-4.md), [Part 5](voice-ai-assistants--part-5.md)*

Telnyx Voice AI Assistants let you build, configure, and operate conversational voice agents entirely from the Mission Control Portal or via API. This page covers the no-code quickstart, supported language and transcription models, voice and noise-suppression settings, built-in and library tools, integrations, scheduled outbound events with retries, and programmatic voice control.

## Third-Party Integrations

By default, every component of a Telnyx AI Assistant runs on Telnyx infrastructure. You can, however, bring your own LLM or TTS using third-party providers.

### Vapi integration

If you have voice assistants configured in Vapi, you can [import them](https://developers.telnyx.com/docs/inference/ai-assistants/importing) as Telnyx AI Assistants in a single click. To use a Vapi voice in an existing Telnyx assistant:

1. Create a Vapi API Key (see [Vapi's guide](https://docs.vapi.ai/chat/web-widget#1-get-your-public-api-key)).
2. Reference the key in your Assistant voice configuration.

In the voice tab for your assistant, select Vapi as the provider. A new dropdown appears to reference your API key. Give the secret a friendly identifier and securely store your API key as the secret value. To enable a multilingual agent, set the transcription model to `deepgram/nova-3`.

You will not be able to access the value of a secret after it is stored. You can also manage all your secrets in the [Integration Secrets](https://portal.telnyx.com/#/integration-secrets) tab in the portal.

### ElevenLabs integration

If you have Conversational AI agents configured in ElevenLabs, you can [import them](https://developers.telnyx.com/docs/inference/ai-assistants/importing) as Telnyx AI Assistants in a single click. To use an ElevenLabs voice in an existing Telnyx assistant:

1. Create an ElevenLabs API Key (see [ElevenLabs' guide](https://help.elevenlabs.io/hc/en-us/articles/14599447207697-How-to-authorize-yourself-using-your-xi-api-key)).
2. Reference the key in your Assistant voice configuration.

Requests from a free plan are rejected; you will likely have to use a paid plan to set up this integration successfully. In the voice tab for your assistant, select ElevenLabs as the provider, give the secret a friendly identifier, and securely store your API key as the secret value. To enable a multilingual agent, set the transcription model to `deepgram/nova-3`.

### OpenAI integration

To use an LLM from OpenAI in your assistant:

1. Create an OpenAI API Key (see [OpenAI's guide](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)).
2. Configure the language model in your AI Assistant.

Requests from a free plan are rejected; you will likely have to use a paid plan to set up this integration successfully. In the [AI Assistants tab](https://portal.telnyx.com/#/ai/assistants), edit your assistant, change the model to an OpenAI model like `openai/gpt-4o`, then follow the same API Key steps as described in the ElevenLabs section above.

## Related Resources

- [Create an Assistant API Reference](/api-reference/assistants/create-an-assistant)
- [Voice AI Assistant API Reference](/api-reference/assistants/create-an-assistant)
- [STT WebSocket Streaming](/docs/tts-stt/stt-websocket-streaming)
- [Dynamic Variables](dynamic-variables.md)
- [Custom LLMs for Assistants](custom-llms-for-assistants.md)
- [Agent Handoff](agent-handoff.md)
- [Client-Side Tools](client-side-tools.md)
- [AI Assistant Integrations](/docs/inference/ai-assistants/integrations)
- [AI Insights documentation](https://developers.telnyx.com/docs/inference/ai-insights)
- [Voicemail Detection on Transfer](/docs/inference/ai-assistants/voicemail-detection-on-transfer)
- [Available Models](/docs/inference/models)
- [Text-to-Speech Available Voices](/docs/tts-stt/tts-available-voices/index#text-to-speech-available-voices)
- [Noise Suppression guide](/docs/voice/programmable-voice/noise-suppression)
