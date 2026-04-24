---
title: Calls
summary: Initiate and manage TeXML calls programmatically.
sources:
  - url: https://developers.telnyx.com/docs/voice/texml/rest-api/calls/index
    content_hash: 8cfd3cadbefd03e208010a99e49e3568193888a4b103af213db1e066fe2b0596
updated_at: 2026-04-10T00:00:00Z
---

# Calls

Initiate and manage TeXML calls programmatically.

A call object represents a single call leg. It contains all state, metadata, and lifecycle information of that call leg.

## Creating calls

A call object is instantiated in the following situations:

1\. When an outbound call is initiated through the [REST API](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call).

Telnyx immediately creates a call resource to represent this outbound call.

2\. When an inbound call reaches a phone number assigned to a TeXML application.

* Before processing any TeXML, a call resource is created to represent the inbound call itself.
* At that point, the call is answered and the instruction fetch request is sent. The lifecycle of this inbound call is driven by the instructions defined in the TeXML response.

3\. When a [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial) verb is executed inside a TeXML script.

Each execution of `` creates a new call resource. This call is logically associated with the parent call that initiated the TeXML request, and Telnyx manages both calls as part of a multi-leg call flow if needed.

## Fetching call details

The details of the call can be retrieved using [the calls endpoint](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-call) up to 30 days after the call has ended.
