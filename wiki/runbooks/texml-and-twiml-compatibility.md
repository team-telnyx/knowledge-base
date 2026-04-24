---
title: TeXML and TwiML Compatibility
summary: Comparison of TeXML and TwiML verb support.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility/index
    content_hash: 551846ad828d995015cbeb8d0234e1156e37a18f17a92dad12bbea0886ac3f16
updated_at: 2026-04-10T00:00:00Z
---

# TeXML and TwiML Compatibility

Comparison of TeXML and TwiML verb support

TeXML services was created to allow the easy migration from Twilio to Telnyx, allowing you to use the same verbs and nouns in both platforms.

This page provides a comparison of verb support between TeXML and TwiML, helping you understand which features are available in each platform.

## Verb Compatibility

| Verb                                                                          | TwiML Support   | TeXML Support   |
| ----------------------------------------------------------------------------- | --------------- | --------------- |
| [``](aigather.md)           | ❌ Not supported | ✅ Supported     |
| [``](dial.md)                   | ✅ Supported     | ✅ Supported     |
| [``](enqueue.md)             | ✅ Supported     | ✅ Supported     |
| [``](gather.md)               | ✅ Supported     | ✅ Supported     |
| [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup)               | ✅ Supported     | ✅ Supported     |
| [``](httprequest.md)     | ❌ Not supported | ✅ Supported     |
| [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave)                 | ✅ Supported     | ✅ Supported     |
| [``](pause.md)                 | ✅ Supported     | ✅ Supported     |
| ``                                                                       | ✅ Supported     | ❌ Not supported |
| [``](play.md)                   | ✅ Supported     | ✅ Supported     |
| [``](record.md)               | ✅ Supported     | ✅ Supported     |
| [``](redirect.md)           | ✅ Supported     | ✅ Supported     |
| [``](refer.md)                 | ✅ Supported     | ✅ Supported     |
| [``](reject.md)               | ✅ Supported     | ✅ Supported     |
| [``](say.md)                     | ✅ Supported     | ✅ Supported     |
| [``](siprec.md)               | ✅ Supported     | ✅ Supported     |
| [``](stop.md)                   | ✅ Supported     | ✅ Supported     |
| [``](stream.md)               | ✅ Supported     | ✅ Supported     |
| [``](suppression.md)     | ✅ Supported     | ✅ Supported     |
| [``](transcription.md) | ✅ Supported     | ✅ Supported     |

For detailed information about particular TeXML verb click the link under the name of the verb in the table.

## Noun Compatibility

| Noun                                                                           | TwiML Support | TeXML Support   |
| ------------------------------------------------------------------------------ | ------------- | --------------- |
| ``                                                                     | ✅ Supported   | ❌ Not supported |
| [``](conference.md)        | ✅ Supported   | ✅ Supported     |
| [``](dial.md#child-verbsnouns) | ✅ Supported   | ✅ Supported     |
| ``                                                                       | ✅ Supported   | ❌ Not supported |
| [``](dial.md#child-verbsnouns)  | ✅ Supported   | ✅ Supported     |
| [``](dial.md#child-verbsnouns)    | ✅ Supported   | ✅ Supported     |
| ``                                                               | ✅ Supported   | ❌ Not supported |

More information about the nouns can be found on [`` documentation page](dial.md)

## REST API Endpoint Compatibility

The following table outlines the compatibility between Twilio's REST API endpoints and Telnyx's TeXML API endpoints.

| Title                                                                                                                   | Compatibility   | Method | Endpoint                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | --------------- | ------ | ------------------------------------------------------------------------------------ |
| [Fetch a call](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-call)                                                         | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Calls/{CallSid}`                                             |
| [Update call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-call)                                                           | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}`                                             |
| [Fetch multiple call resources](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-multiple-call-resources)                       | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Calls`                                                       |
| [Initiate an outbound call](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call)                               | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Calls`                                                       |
| [Fetch a conference resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-conference-resource)                           | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}`                                 |
| [Update a conference resource](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-conference-resource)                         | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}`                                 |
| [List conference resources](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-resources)                               | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Conferences`                                                 |
| [List conference participants](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-participants)                         | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants`                    |
| [Dial a new conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant)               | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants`                    |
| [List conference recordings](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-recordings)                             | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings`                      |
| [Get conference participant resource](https://developers.telnyx.com/api-reference/texml-rest-commands/get-conference-participant-resource)           | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}`          |
| [Update a conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-conference-participant)                   | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}`          |
| [Delete a conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-conference-participant)                   | ✅ Compatible    | DELETE | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}`          |
| [Request recording for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/request-recording-for-a-call)                         | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Recordings`                                  |
| [Fetch recordings for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-call)                           | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Calls/{CallSid}/Recordings`                                  |
| [Update recording on a call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-recording-on-a-call)                             | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{RecordingSid}`                   |
| [Fetch multiple recording resources](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-multiple-recording-resources)             | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Recordings`                                                  |
| [Fetch recording resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recording-resource)                                 | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Recordings/{RecordingSid}`                                   |
| [Delete recording resource](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-recording-resource)                               | ✅ Compatible    | DELETE | `/Accounts/{AccountSid}/Recordings/{RecordingSid}`                                   |
| [Fetch recordings for a conference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-conference)               | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings`                      |
| [Start streaming media from a call](https://developers.telnyx.com/api-reference/texml-rest-commands/start-streaming-media-from-a-call)               | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Streams`                                     |
| [Update streaming on a call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-streaming-on-a-call)                             | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Streams/{StreamSid}`                         |
| [Request siprec session for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/request-siprec-session-for-a-call)               | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Siprec`                                      |
| [Updates siprec session for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/updates-siprec-session-for-a-call)               | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Siprec/{SiprecSid}`                          |
| [List recording transcriptions](https://developers.telnyx.com/api-reference/texml-rest-commands/list-recording-transcriptions)                       | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions`                    |
| [Fetch a recording transcription resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-recording-transcription-resource) | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{TranscriptionSid}` |
| [Delete a recording transcription](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-recording-transcription)                 | ✅ Compatible    | DELETE | `/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{TranscriptionSid}` |
| Create a Queue resource                                                                                                 | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Queues.json`                                                 |
| Fetch a Queue resource                                                                                                  | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Queues/{Sid}.json`                                           |
| Read multiple Queue resources                                                                                           | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Queues.json`                                                 |
| Update a Queue resource                                                                                                 | ✅ Compatible    | POST   | `/Accounts/{AccountSid}/Queues/{Sid}.json`                                           |
| Delete a Queue resource                                                                                                 | ✅ Compatible    | DELETE | `/Accounts/{AccountSid}/Queues/{Sid}.json`                                           |
| Fetch a Member resource                                                                                                 | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json`                    |
| Read multiple Member resources                                                                                          | ✅ Compatible    | GET    | `/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json`                              |
| Start a Real-Time Transcription                                                                                         | ❌ Not supported | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions.json`                         |
| Stop a Real-Time Transcription                                                                                          | ❌ Not supported | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions/{Sid}.json`                   |
| Starting a Pay session                                                                                                  | ❌ Not supported | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json`                               |
| Update a Pay session                                                                                                    | ❌ Not supported | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json`                         |
| Create a UserDefinedMessage                                                                                             | ❌ Not supported | POST   | `/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessages.json`                    |
| Create a UserDefinedMessageSubscription                                                                                 | ❌ Not supported | POST   | `Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions.json`         |

For detailed information about TeXML REST API endpoints and their usage, please use the links to the documentation from the table.


## Related Pages

- [Compatibility](../runbooks/compatibility.md)
