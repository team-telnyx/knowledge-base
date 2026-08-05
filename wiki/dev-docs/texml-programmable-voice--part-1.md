---
title: TeXML Programmable Voice
summary: TeXML is Telnyx's XML-based markup language for controlling Programmable
  Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers
  the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint
  parity, and detailed reference for the core verbs including Dial, Conference, Enqueue,
  Connect, AIAssistant, AIGather, and ConversationRelay.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
updated_at: 2026-08-05T14:04:49Z
---

# TeXML Programmable Voice

*Part 1 of 6 — see also: [Part 2](texml-programmable-voice--part-2.md), [Part 3](texml-programmable-voice--part-3.md), [Part 4](texml-programmable-voice--part-4.md), [Part 5](texml-programmable-voice--part-5.md), [Part 6](texml-programmable-voice--part-6.md)*

TeXML is Telnyx's XML-based markup language for controlling Programmable Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint parity, and detailed reference for the core verbs including Dial, Conference, Enqueue, Connect, AIAssistant, AIGather, and ConversationRelay.

## Overview

TeXML is an XML-based data structure used to control calls with Telnyx Programmable Voice. It is the quickest way to get started using a simple `.xml` file, allowing you to specify call instructions using commands called **verbs** and **nouns**. The TeXML interpreter starts at the top of your TeXML file and executes commands sequentially in the order they are arranged.

TeXML was created to allow easy migration from Twilio to Telnyx, allowing the same verbs and nouns to be used on both platforms. The TeXML Translator seamlessly interprets existing TwiML verbs and nouns from other providers.

A TeXML file contains:

- **`<Response>` element** — the tag defining the body of the TeXML document
- **verb** — an XML tag denoting the action that Telnyx should take
- **noun** — the item for the action specified in the associated verb

## Quickstart: Simple Text-to-Speech Demo

### Step 1: Set up a Telnyx account, phone number, and TeXML application

This quickstart assumes you have already [set up your developer account and environment](https://developers.telnyx.com/docs/development) and know how to [send commands](https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands) and [receive webhooks](https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks) using the Voice API.

### Step 2: Create an XML file containing TeXML call instructions

Create an empty standard `.xml` file using your preferred editor. The following example answers an incoming call, plays text-to-speech, and hangs up using `<Say>` and `<Hangup>`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>This is TeXML text to speech setup in seconds! The call will now hangup.</Say>
    <Hangup />
</Response>
```

### Step 3: Make your TeXML file accessible on the internet

Upload the file to the TeXML Bin storage so it is available for the TeXML application:

1. Go to the **TeXML Bin** tab in the Voice → Settings section of the Mission Control Portal.
2. Click **Create new**.
3. Add a name and the content of the file.
4. Save it. The TeXML instructions will be available under the link provided in the URL field.

### Step 4: Configure your application to point at your TeXML file

In the Mission Control Portal:

- Select **Real-Time Communications → Voice → Programmable Voice** in the left-hand navigation and open the **TeXML Applications** tab.
- Edit the TeXML Application created in Step 1 by clicking the pencil ✎ icon.
- Set the **Voice Method** to `GET` to read the contents of the TeXML file.
- In the **Send a TeXML Webhook to the URL** field, enter the URL of the XML file created in Step 3.
- Assign a number to the TeXML application on the **Numbers** tab.
- Save all changes.

### Step 5: Dial your Telnyx number

Using any telephony client or device, dial the number purchased in Step 1 that is connected to the TeXML Application. The call answers automatically and the text-to-speech plays.

## Verb Compatibility

The following table compares verb support between TeXML and TwiML:

| Verb | TwiML Support | TeXML Support |
| --- | --- | --- |
| `<AIGather>` | ❌ Not supported | ✅ Supported |
| `<Dial>` | ✅ Supported | ✅ Supported |
| `<Enqueue>` | ✅ Supported | ✅ Supported |
| `<Gather>` | ✅ Supported | ✅ Supported |
| `<Hangup>` | ✅ Supported | ✅ Supported |
| `<HttpRequest>` | ❌ Not supported | ✅ Supported |
| `<Leave>` | ✅ Supported | ✅ Supported |
| `<Pause>` | ✅ Supported | ✅ Supported |
| `<Pay>` | ✅ Supported | ❌ Not supported |
| `<Play>` | ✅ Supported | ✅ Supported |
| `<Record>` | ✅ Supported | ✅ Supported |
| `<Redirect>` | ✅ Supported | ✅ Supported |
| `<Refer>` | ✅ Supported | ✅ Supported |
| `<Reject>` | ✅ Supported | ✅ Supported |
| `<Say>` | ✅ Supported | ✅ Supported |
| `<Siprec>` | ✅ Supported | ✅ Supported |
| `<Stop>` | ✅ Supported | ✅ Supported |
| `<Stream>` | ✅ Supported | ✅ Supported |
| `<Suppression>` | ✅ Supported | ✅ Supported |
| `<Transcription>` | ✅ Supported | ✅ Supported |

## Noun Compatibility

| Noun | TwiML Support | TeXML Support |
| --- | --- | --- |
| `<Client>` | ✅ Supported | ❌ Not supported |
| `<Conference>` | ✅ Supported | ✅ Supported |
| `<Number>` | ✅ Supported | ✅ Supported |
| `<Room>` | ✅ Supported | ❌ Not supported |
| `<Queue>` | ✅ Supported | ✅ Supported |
| `<Sip>` | ✅ Supported | ✅ Supported |
| `<VirtualAgent>` | ✅ Supported | ❌ Not supported |
