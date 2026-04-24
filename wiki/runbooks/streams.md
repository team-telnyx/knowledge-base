---
title: Streams
summary: Manage media streams for TeXML calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/texml/rest-api/streams/index
    content_hash: 981f1c74f06129ccf0b64e4bbb449d541f464505c0cc0c24a626388fdb647cbc
updated_at: 2026-04-10T00:00:00Z
---

# Streams

Manage media streams for TeXML calls.

A stream object represents an active media streaming session originating from a call. Streams allow real-time audio from a call to be delivered to an external destination using WebSockets. Each stream object encapsulates the configuration, state, and lifecycle of a single streaming session associated with a call.

## Creating stream

A stream object can be started in the following ways:

1\. Starting a stream via the REST API

API reference: [Start streaming media from a call](https://developers.telnyx.com/api-reference/texml-rest-commands/start-streaming-media-from-a-call)

Using the REST API, an application can explicitly start streaming media from an active call. When this endpoint is invoked, a stream object is created and audio begins streaming from the specified call according to the provided configuration. This method allows streaming to be initiated dynamically at any point during the call lifecycle.

2\. Starting a stream via the TeXML `` verb

Streams can also be initiated as part of TeXML execution using the `` verb, which supports two operational modes:

* Asynchronous streaming via ``

When the `` verb is nested inside a `` verb, the stream is started asynchronously. In this mode, streaming begins in parallel with the ongoing call flow, allowing audio to be streamed without interrupting or blocking other TeXML instructions.

* Synchronous streaming via ``

When the `` verb is nested inside a `` verb, streaming is initiated synchronously. In this mode, the call flow waits for the streaming operation to stop before proceeding to the next TeXML instruction.

In both cases, execution of the `` verb results in the creation of a stream object associated with the active call.

## Managing and Stopping a Stream

Once a stream has been started—whether via the REST API or TeXML—it can be managed throughout its lifecycle using the REST API.

1.Updating or stopping a stream via the REST API.

API reference: [Update streaming on a call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-streaming-on-a-call)

When streaming is stopped, the associated stream object transitions to a completed state, and websockets are closed.
