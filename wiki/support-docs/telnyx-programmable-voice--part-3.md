---
title: Telnyx Programmable Voice
summary: 'Telnyx Programmable Voice provides multiple paradigms for building voice
  applications: the Voice API (Call Control) for programmatic call management, TeXML
  for XML-driven call flows, and AI Assistants for no-code conversational AI. This
  page covers configuration, compatibility, real-time transcription, third-party integrations,
  and migration guidance.'
sources:
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
  content_hash: 8ad66d6c9ea440951f259f45a6639b7abdbc3762c8808b57774d2fe4d60f2783
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
  content_hash: 79afc77e4a975867133c6229080f1870df4e29203581a2478b9a3fc0d2156692
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
  content_hash: 796dc56257808f5e02f4e076a2b65788bfa9d791ab06a565014e8c8345ef7344
- url: https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx
  content_hash: d3098961d17ae5558a906b63a69ef91d005647ce75cf01b844d239258b3718c7
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
  content_hash: b446fc44af8df4f3f3b7050ef415b1fadccc6aa4e17e7af6463f1d2c863bfde2
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
  content_hash: 7f026b4e298be9c1cdbc1d17345b7f469b7d6c5245fb4dc81a485ebb089163d8
- url: https://support.telnyx.com/en/articles/8292490-real-time-transcription
  content_hash: 76a7beabc40726462c19c585a7ec962f8b56840817ff7da0a189c6186943a562
- url: https://support.telnyx.com/en/articles/9413928-telnyx-flow
  content_hash: 61bba2d7c7e49fcb586998819a9bd3107405f5a685d462e3cc484f5efe30ad1f
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
  content_hash: b11a5bdfb665e039b8a9927cebf7acbfdb5f7c8a5f1fd43631989d2e8b27a947
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
  content_hash: 95152862fbcb84bca63783a9ab66c43f144b2976be4888290a32c7a9b312d6d9
- url: https://support.telnyx.com/en/collections/9526270-telnyx-flow
  content_hash: da5c6979781c13f828bafee007d84d826b44739ecd4cba8ef4c0f7f8c1efbc0b
updated_at: 2026-06-11T11:40:11Z
---

# Telnyx Programmable Voice

*Part 3 of 3 — see also: [Part 1](telnyx-programmable-voice--part-1.md), [Part 2](telnyx-programmable-voice--part-2.md)*

Telnyx Programmable Voice provides multiple paradigms for building voice applications: the Voice API (Call Control) for programmatic call management, TeXML for XML-driven call flows, and AI Assistants for no-code conversational AI. This page covers configuration, compatibility, real-time transcription, third-party integrations, and migration guidance.

## Third-Party Integrations

### Telnyx + Vapi

Connect a Telnyx phone number to a Vapi assistant for inbound and outbound calls.

**Two setup paths:**

1. **Import an existing Telnyx number into Vapi** (recommended): Keep the number in Telnyx, add it from the Vapi dashboard by selecting Telnyx as the provider and pasting a dedicated Telnyx API v2 key.
2. **BYO Telnyx SIP trunk with Vapi**: For custom SIP routing, SIP trunk credentials, or advanced SIP configuration. Involves configuring inbound SIP routing to Vapi, setting translated numbers to Vapi SIP URIs, creating outbound SIP credentials, and attaching the trunk to an Outbound Voice Profile. Use IP addresses for inbound-enabled gateways — do not use `sip.telnyx.com`.

**Prerequisites**: Active Telnyx and Vapi accounts, a voice-capable Telnyx number, a Vapi assistant or squad, a dedicated Telnyx API v2 key, and (for outbound) an Outbound Voice Profile with required destinations enabled.

**Outbound calling**: In the Telnyx portal, go to **Voice > Outbound Voice Profiles**, enable destination countries, and add Vapi as a connection. Outbound calls may fail if destinations aren't enabled, verification is incomplete, Vapi isn't attached to the correct profile, or caller ID is invalid.

### Migrating from Twilio

Telnyx is compatible with existing TwiML code and Twilio SDKs. You can run your TwiML-based applications on Telnyx by pointing a TeXML Application at your existing TwiML URL. The Twilio SDK generates TwiML that Telnyx interprets as TeXML. This enables migration with minimal code changes while benefiting from lower costs.

## Telnyx Flow (Deprecated)

Telnyx Flow sunset on **July 3, 2026**. After this date:

- Workflows in Flow stop executing.
- Inbound webhook events are no longer delivered to Flow.
- Voice and Messaging applications pointing to Flow stop receiving inbound traffic.

**Migration options:**

- Build directly with Telnyx Voice, Messaging, and Chat Completions APIs, or use [AI Assistants](ai-assistants.md) for a faster no-code route.
- Use **n8n** with the Telnyx AI node as a visual workflow alternative.

Before the sunset date, update any Voice and Messaging application webhooks currently pointing to Flow so they route to a new endpoint you control.
