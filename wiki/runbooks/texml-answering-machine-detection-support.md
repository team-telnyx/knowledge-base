---
title: TeXML Answering Machine Detection Support
summary: Learn how to enable and configure Answering Machine Detection (AMD) for TeXML outbound calls, with synchronous and asynchronous detection modes.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine/index
    content_hash: 3e57a3a44aaa7b02430d1c6dfca4fc9da94f38f16fffd27254afbe93f6c53a4d
updated_at: 2026-04-10T00:00:00Z
---

# TeXML Answering Machine Detection Support

Learn how to enable and configure Answering Machine Detection (AMD) for TeXML outbound calls, with synchronous and asynchronous detection modes.

TeXML is an XML-based data structure you can use to control calls with Telnyx and is the quickest way to get started with Programmable Voice using a simple .xml file, allowing you to specify call instructions in your file using commands called verbs and nouns.

## Initiating a TeXML outbound call using REST endpoint with AMD enabled

There are 2 possible options for using Answering Machine Detection for outbound calls:

1. **Synchronous mode**: In this case, the TeXML instructions are not executed until the results of AMD process are provided in the status callback. The new instructions can be sent back as response to be processed by the TeXML engine.
2. **Asynchronous mode**: Here, the TeXML instructions are processed in parallel to the AMD process. The results of the AMD analysis are being provided in the AsyncAmdStatusCallback callback.

### Synchronous mode request

The outbound TeXML call with AMD support enable in the synchronous mode can be requested in the following way:

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```bash theme={null}
    curl --request POST \
      --url https://api.telnyx.com/v2/texml/calls/{connection_id} \
      --header 'Authorization: Bearer YOUR_API_KEY' \
      --header 'Content-Type: application/json' \
      --data '{
      "From": "+13127367421",
      "To": "your-sip-user@sip.telnyx.com",
      "Url": "https://your-server.example.com/texml/instructions",
      "FallbackUrl": "https://your-server.example.com/texml/fallback",
      "StatusCallback": "https://your-server.example.com/callback/status",
      "StatusCallbackMethod": "POST",
      "Method": "POST",
      "MachineDetection": "Enable",
      "DetectionMode": "Premium",
      "AsyncAmd": "false"
    }'
```

The results of the analysis will be sent as a value of the `AnsweredBy` parameter of the `StatusCallback` request.

#### `AnsweredBy` parameter values

| Value     | Description                       |
| --------- | --------------------------------- |
| `human`   | A human answered the call         |
| `machine` | An answering machine was detected |
| `fax`     | A fax machine was detected        |
| `unknown` | Detection was inconclusive        |

<Callout type="info">
  The `MachineDetection` parameter accepts the following values: `Enable`, `Disable` (default), and `DetectMessageEnd`. The `DetectionMode` parameter accepts `Regular` (default) or `Premium`.

### Asynchronous mode request

Similarly, the asynchronous AMD processing can be requested for outgoing TeXML calls:

```bash theme={null}
    curl --request POST \
      --url https://api.telnyx.com/v2/texml/calls/{connection_id} \
      --header 'Authorization: Bearer YOUR_API_KEY' \
      --header 'Content-Type: application/json' \
      --data '{
      "From": "+13127367421",
      "To": "your-sip-user@sip.telnyx.com",
      "Url": "https://your-server.example.com/texml/instructions",
      "FallbackUrl": "https://your-server.example.com/texml/fallback",
      "Method": "POST",
      "StatusCallback": "https://your-server.example.com/callback/status",
      "StatusCallbackMethod": "POST",
      "MachineDetection": "Enable",
      "DetectionMode": "Premium",
      "AsyncAmd": "true",
      "AsyncAmdStatusCallback": "https://your-server.example.com/callback/amd-status",
      "AsyncAMDStatusCallbackMethod": "POST"
    }'
```

The results of the AMD analysis will be sent as callback requests to the address provided as `AsyncAmdStatusCallback` parameter. Note that this can be used for basic and premium AMD.

#### `AsyncAmdStatusCallback` parameters

The callback to your `AsyncAmdStatusCallback` URL includes the following parameters:

| Parameter    | Description                                                          |
| ------------ | -------------------------------------------------------------------- |
| `AnsweredBy` | The result of AMD analysis (`human`, `machine`, `fax`, or `unknown`) |
| `CallSid`    | The unique identifier for the call                                   |
| `AccountSid` | Your Telnyx account SID                                              |


## Related Pages

- [Answering Machine Detection](../runbooks/answering-machine-detection.md)
