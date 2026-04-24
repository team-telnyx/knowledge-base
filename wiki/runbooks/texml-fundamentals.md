---
title: TeXML Fundamentals
summary: TeXML is an XML-based markup language to define call control and processing instructions.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
    content_hash: 01d04613a9f77b61c711ccbc0f33a22481988462b35d64fd88c8b4bef5539ade
updated_at: 2026-04-10T00:00:00Z
---

# TeXML Fundamentals

What is TeXML?

## Overview

TeXML is an XML-based markup language to define call control and processing instructions. When properly configured,
Telnyx will fetch TeXML instructions from the user's application and process the calls accordingly.

See [Verbs & Nouns](texml-and-twiml-compatibility.md).

## TeXML Application

An instance of TeXML Application is a collection of configuration parameters that defines the interaction between
Telnyx and the user's application:

| Field                        | Description                                                                                                                                                                                                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Application Name**         | A descriptive name to identify your TeXML application.                                                                                                                                                                                                       |
| **AnchorSite**               | Defines preferable data center for handling the traffic. In case of `latency` ICMP ping to the webhook URL address will be used to calculate the closed data center.                                                                                         |
| **Voice method**             | HTTP method that will be used to interact with your webhooks                                                                                                                                                                                                 |
| **Webhook URL**              | The URL where Telnyx will fetch TeXML instructions when a call is initiated. The instruction can be served by Telnyx. In that case select `TeXML bin URL`. See [TeXML bin quickstart](https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart) for more details. |
| **Webhook Failover URL**     | A backup URL that Telnyx will use if the primary webhook URL fails to respond                                                                                                                                                                                |
| **Call progress events URL** | URL where Telnyx will send event callbacks related to your calls                                                                                                                                                                                             |
| **Status Callback Method**   | HTTP method (GET or POST) used for status callbacks                                                                                                                                                                                                          |
| **Hang-up on timeout**       | Specifies the number of seconds Telnyx will wait for initial application response before hanging up                                                                                                                                                          |
| **DTMF Type**                | Configuration for how DTMF (touch-tone) inputs are handled                                                                                                                                                                                                   |
| **Enable Call Cost**         | Specify if the call cost webhook should be sent                                                                                                                                                                                                              |

A TeXML Application can be created through the [Telnyx Mission Control Portal](https://portal.telnyx.com/#/call-control/texml/new)
or via the [Telnyx API](https://developers.telnyx.com/api-reference/texml-applications/creates-a-texml-application#creates-a-texml-application).

## Instruction Fetching

See [Instruction Fetching](texml-instruction-fetching.md).

## Twilio Compatibility

See [Twilio Compatibility](texml-and-twiml-compatibility.md).


## Related Pages

- [WebRTC Voice SDKs Fundamentals](../runbooks/webrtc-voice-sdks-fundamentals.md)
- [TeXML Bin Dynamic Content](../runbooks/texml-bin-dynamic-content.md)
