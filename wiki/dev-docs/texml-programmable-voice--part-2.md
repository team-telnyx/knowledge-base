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

*Part 2 of 6 — see also: [Part 1](texml-programmable-voice--part-1.md), [Part 3](texml-programmable-voice--part-3.md), [Part 4](texml-programmable-voice--part-4.md), [Part 5](texml-programmable-voice--part-5.md), [Part 6](texml-programmable-voice--part-6.md)*

TeXML is Telnyx's XML-based markup language for controlling Programmable Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint parity, and detailed reference for the core verbs including Dial, Conference, Enqueue, Connect, AIAssistant, AIGather, and ConversationRelay.

## REST API Endpoint Compatibility

TeXML provides REST API endpoints that mirror Twilio's REST API. The following endpoints are fully compatible:

| Title | Compatibility | Method | Endpoint |
| --- | --- | --- | --- |
| Fetch a call | ✅ Compatible | GET | `/Accounts/{AccountSid}/Calls/{CallSid}` |
| Update call | ✅ Compatible | POST | `/Accounts/{AccountSid}/Calls/{CallSid}` |
| Fetch multiple call resources | ✅ Compatible | GET | `/Accounts/{AccountSid}/Calls` |
| Initiate an outbound call | ✅ Compatible | POST | `/Accounts/{AccountSid}/Calls` |
| Fetch a conference resource | ✅ Compatible | GET | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}` |
| Update a conference resource | ✅ Compatible | POST | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}` |
| List conference resources | ✅ Compatible | GET | `/Accounts/{AccountSid}/Conferences` |
| List conference participants | ✅ Compatible | GET | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants` |
| Dial a new conference participant | ✅ Compatible | POST | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants` |
| List conference recordings | ✅ Compatible | GET | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings` |
| Get conference participant resource | ✅ Compatible | GET | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}` |
| Update a conference participant | ✅ Compatible | POST | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}` |
| Delete a conference participant | ✅ Compatible | DELETE | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}` |
| Request recording for a call | ✅ Compatible | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Recordings` |
| Fetch recordings for a call | ✅ Compatible | GET | `/Accounts/{AccountSid}/Calls/{CallSid}/Recordings` |
| Update recording on a call | ✅ Compatible | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{RecordingSid}` |
| Fetch multiple recording resources | ✅ Compatible | GET | `/Accounts/{AccountSid}/Recordings` |
| Fetch recording resource | ✅ Compatible | GET | `/Accounts/{AccountSid}/Recordings/{RecordingSid}` |
| Delete recording resource | ✅ Compatible | DELETE | `/Accounts/{AccountSid}/Recordings/{RecordingSid}` |
| Fetch recordings for a conference | ✅ Compatible | GET | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings` |
| Start streaming media from a call | ✅ Compatible | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Streams` |
| Update streaming on a call | ✅ Compatible | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Streams/{StreamSid}` |
| Request siprec session for a call | ✅ Compatible | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Siprec` |
| Updates siprec session for a call | ✅ Compatible | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Siprec/{SiprecSid}` |
| List recording transcriptions | ✅ Compatible | GET | `/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions` |
| Fetch a recording transcription resource | ✅ Compatible | GET | `/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{TranscriptionSid}` |
| Delete a recording transcription | ✅ Compatible | DELETE | `/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{TranscriptionSid}` |
| Create a Queue resource | ✅ Compatible | POST | `/Accounts/{AccountSid}/Queues.json` |
| Fetch a Queue resource | ✅ Compatible | GET | `/Accounts/{AccountSid}/Queues/{Sid}.json` |
| Read multiple Queue resources | ✅ Compatible | GET | `/Accounts/{AccountSid}/Queues.json` |
| Update a Queue resource | ✅ Compatible | POST | `/Accounts/{AccountSid}/Queues/{Sid}.json` |
| Delete a Queue resource | ✅ Compatible | DELETE | `/Accounts/{AccountSid}/Queues/{Sid}.json` |
| Fetch a Member resource | ✅ Compatible | GET | `/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json` |
| Read multiple Member resources | ✅ Compatible | GET | `/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json` |

The following endpoints are **not** supported in TeXML:

| Title | Method | Endpoint |
| --- | --- | --- |
| Start a Real-Time Transcription | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions.json` |
| Stop a Real-Time Transcription | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions/{Sid}.json` |
| Starting a Pay session | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json` |
| Update a Pay session | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json` |
| Create a UserDefinedMessage | POST | `/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessages.json` |
| Create a UserDefinedMessageSubscription | POST | `Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions.json` |
