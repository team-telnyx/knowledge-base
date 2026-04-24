---
title: Recordings
summary: Access and manage TeXML call recordings.
sources:
  - url: https://developers.telnyx.com/docs/voice/texml/rest-api/recordings/index
    content_hash: 3266a04140bb0dd5a85cfd142739c42717b11024cb4e067f7bce77c16a2be20d
updated_at: 2026-04-10T00:00:00Z
---

# Recordings

Access and manage TeXML call recordings.

A recording object represents an audio recording generated during a call or conference using TeXML application. Recording objects track metadata such as format, duration, start and end times, and storage locations.

## Creating recording

A recording can be created in the following situations:

1\. When an outbound call is initiated with record enabled via the REST API

API reference: [Initiate an outbound call](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call)

If your application initiates an outbound call and specifies the record attribute, Telnyx automatically begins recording the call when it is answered.

2\. When a `` verb is executed in a TeXML script

Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record)

Whenever a `` verb is encountered in a TeXML response, Telnyx initiates audio capture for the call leg that executed the verb. Each execution produces a distinct recording object that captures the audio during the `` period

3\. When a `` verb is executed with record attributes enabled

Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial)

If a `` verb includes recording parameters (e.g., to record the outbound leg created by the dial), Telnyx begins recording as soon as that outbound call leg is created.

4\. When a `` to `` is executed with record attributes

Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference)

When a `` connects a call into a `` and recording attributes are provided, Telnyx initiates conference recording.

5\. When recording is started manually via the REST API

API reference: [Request recording for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/request-recording-for-a-call)

The recording may be triggered dynamically on any existing call by making a request to the start recording endpoint. When the request is executed, Telnyx creates a new recording object associated with that ongoing call.

6\. When a conference participant is dialed and joined via the REST API with recording enabled

API reference: [Dial a new conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant)

If a new participant is added to a conference using the REST API and recording is enabled for that action, Telnyx begins capturing audio for the participant or the entire conference session.

## Fetching Recordings

Recording objects can be retrieved through several query paths depending on how the recording was initiated:

1\. By Recording ID - [API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recording-resource)

2\. By Conference ID - [API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-conference)

3\. By Call ID - [API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-call)

## Controlling Ongoing Recordings

Once recording is active, your application can manage or modify the recording session using the REST API:

1\. Update or stop an ongoing recording on a call - [API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/update-recording-on-a-call)


## Related Pages

- [Storing call recordings](../runbooks/storing-call-recordings.md)
