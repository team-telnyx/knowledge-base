---
title: SIPREC
summary: Manage SIPREC sessions for TeXML calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/texml/rest-api/siprec/index
    content_hash: e9d6f38c81fd07f896c374418fb245d1987c676d30fbc2f3cabb8c93ff741cd9
updated_at: 2026-04-10T00:00:00Z
---

# SIPREC

Manage SIPREC sessions for TeXML calls.

A SIPREC session represents an active SIP Client Recording (SIPREC) media session associated with a call. SIPREC sessions enable the delivery of call media to an external SIP recording server for compliance recording, monitoring, or archival purposes. Each SIPREC session object encapsulates the configuration, state, and lifecycle of a single recording session tied to a call. In order to use SIPREC, the SIPREC client connectors must be configured in your Telnyx account. See [SIPREC client tutorial](https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client) for more information.

## Creating SIPREC session

A SIPREC session can be started in the following ways:

1\. Starting a SIPREC session via the REST API

API reference: [Request a SIPREC session for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/request-siprec-session-for-a-call)

Using the REST API, an application can explicitly request the initiation of a SIPREC session for an active call. When this endpoint is invoked, Telnyx creates a SIPREC session object and begins streaming the call media to the configured SIP recording endpoint according to the supplied parameters. This approach allows SIPREC to be started dynamically at any point during the call lifecycle.

2\. Starting a SIPREC session via the TeXML `` verb

Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec)

The SIPREC session is initiated synchronously (nested to `` verb) as part of the sequential TeXML execution flow. Subsequent TeXML instructions are processed only after the SIPREC session has been stopped.

## Managing and Stopping a SIPREC Session

Once a SIPREC session has been started—either via the REST API or via TeXML - it can be managed throughout its lifecycle using the REST API.

API reference: [Update a SIPREC session for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/updates-siprec-session-for-a-call)

This endpoint allows an application to update the state of an active SIPREC session or explicitly stop the recording.


## Related Pages

- [Siprec](../runbooks/siprec.md)
