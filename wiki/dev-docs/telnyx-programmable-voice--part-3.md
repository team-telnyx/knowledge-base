---
title: Telnyx Programmable Voice
summary: Telnyx Programmable Voice provides tools for building voice applications
  including SIPREC recording, speech-to-text transcription, call recording storage,
  SSML-based text-to-speech, and the TeXML markup language for declarative call control
  with TwiML compatibility.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
  content_hash: 5f20f9da47913df819e8853ce1bec7cc18ca3b72a65481e97e8d8abdb21b434a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
  content_hash: aef1769dcaf3a6fe330e8715353328de8017840a5721dd354fc9a3bf06365913
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ssml-tags/index
  content_hash: 743eececec66347e73b016b8e53fe085c9add6df952c4b1614da8b9f891f7d60
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
  content_hash: 6fe6973bbc0653ed56eeb8806cd7baf759741e9dfd020b80b419a85120b8bc7b
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
  content_hash: 21442960c192f1e45263da4b0688fc7e40876769ca13bb33818906d5cae00636
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
  content_hash: 1e29367f33838ffb5b350698efa550f61e565e89e5f3c84035a686753a439ce1
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
  content_hash: 2a4ce735c57a6005b294b5374901754f96446dcaf05589cd825071a79a3f204a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
  content_hash: 7d515a5f4f318ce48b9d85f83981ae2336cdb09ad210e839ce53ddd326b0d93b
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
  content_hash: 78104abb8c6285534e3c1bfa5d136d35aadce02101459fc4f5895ca46ec9d2ff
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
  content_hash: 5609b58aa97391f6557c477b6c5103aa53176e6473ae203722d8bd1dee7fca34
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
  content_hash: e14b54eae87e5ce08bd0427af6eecc57ec3adba060f6024566012b78153adb6f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
  content_hash: 7394df1156c0c5b3a487f470a9fd996bf976c78e759b5b414defe424c1d2f5c4
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
  content_hash: 5c10e721340bceb989599c29d93823ad1ac2980c05d2c116d3769e9375b08117
updated_at: 2026-06-11T10:43:02Z
---

# Telnyx Programmable Voice

*Part 3 of 3 — see also: [Part 1](telnyx-programmable-voice--part-1.md), [Part 2](telnyx-programmable-voice--part-2.md)*

Telnyx Programmable Voice provides tools for building voice applications including SIPREC recording, speech-to-text transcription, call recording storage, SSML-based text-to-speech, and the TeXML markup language for declarative call control with TwiML compatibility.

## TeXML Dynamic Parameters

TeXML supports dynamic content generation at runtime using [Mustache Templates](https://mustache.github.io/mustache.5.html). Parameters can be passed via the webhook URL query string.

### Inserting Dynamic Content

Define a placeholder in the TeXML and supply the value at request time:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Number>{{PhoneNumber}}</Number>
  </Dial>
</Response>
```

Then pass the value in the webhook URL:

```
curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
  --data-urlencode "To=+13121230000" \
  --data-urlencode "From=+13120001234" \
  --data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumber=+18771234567" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

Telnyx-set parameters (e.g. `CallSid`, `From`, `To`) are also available in Mustache templates.

### Iterating Through Lists

Pass array parameters using bracket notation (`PhoneNumbers[]`) and iterate with Mustache sections:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    {{#PhoneNumbers}}
       <Number>{{.}}</Number>
    {{/PhoneNumbers}}
  </Dial>
</Response>
```

### Conditional Content

Use `if/else` logic in TeXML instructions:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
{{#if From == +18771234567}}
  <Dial>
    <Number>+18771234568</Number>
  </Dial>
{{#elseif From == +18771234568}}
  <Dial>
    <Number>+18771234567</Number>
  </Dial>
{{#else}}
  <Say>No valid number is present</Say>
{{/if}}
</Response>
```

Supported operators are `==` and `!=`. There is no operator for checking if a value is not null.

## TeXML HTTP Requests

The `<HttpRequest>` verb enables sending HTTP requests from a TeXML file without a server-side application, allowing integration with external systems and REST APIs.

### Basic Request Structure

```xml
<Response>
  <HttpRequest>
    <Request url="https://example.com" method="POST">
      <Headers>
        <Header>
          <Key>Authorization</Key>
          <Value>Bearer API_key</Value>
        </Header>
        <Header>
          <Key>Content-Type</Key>
          <Value>application/json</Value>
        </Header>
      </Headers>
      <Body>
        <![CDATA[{ "key":"value" }]]>
      </Body>
    </Request>
  </HttpRequest>
</Response>
```

### Synchronous Requests

Requests are asynchronous by default. Set `async="true"` on the `<Request>` element to make the TeXML interpreter wait for the HTTP response before proceeding.

When synchronous, you can extract fields from the JSON response and assign them to variables:

```xml
<HttpRequest>
  <Request url="https://example.com" method="POST" async="true">
    <!-- headers and body -->
  </Request>
  <Response>
    <Type>JSON</Type>
    <StatusCode>200</StatusCode>
    <Content>
      <Field>
        <Name>contact.name.first</Name>
        <Value>first_name</Value>
      </Field>
      <Field>
        <Name>contact.name.last</Name>
        <Value>last_name</Value>
      </Field>
    </Content>
  </Response>
</HttpRequest>
```

### Using Secrets

API keys and other secrets can be stored securely and referenced in TeXML without appearing in logs or callbacks. Upload a secret via API:

```
curl --location --request POST 'https://api.telnyx.com/v2/texml/secrets/' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "name": "your_secret_name",
    "value": "your_secret_value"
  }'
```

Reference it in TeXML with the `secret` helper:

```xml
<Header>
  <Key>Authorization</Key>
  <Value>Bearer {{#secret}}your_secret_name{{/secret}}</Value>
</Header>
```

### Example: Salesforce Lookup and Slack Notification

A practical integration pattern uses two TeXML files: one that queries Salesforce for caller information (synchronously), extracts the caller name, and then invokes a second TeXML file that sends a Slack notification with that name and dials a SIP address. The `action` attribute on `<HttpRequest>` can reference another TeXML Bin URL to chain instructions.

## TeXML Answering Machine Detection

TeXML supports Answering Machine Detection (AMD) on outbound calls via the TeXML Calls API endpoint.

### Synchronous Mode

In synchronous mode, TeXML instructions are not executed until AMD results are available. The result is sent as the `AnsweredBy` parameter in the `StatusCallback` request.

```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/calls/{connection_id} \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "From": "+13127367421",
    "To": "your-sip-user@sip.telnyx.com",
    "Url": "https://your-server.example.com/texml/instructions",
    "StatusCallback": "https://your-server.example.com/callback/status",
    "MachineDetection": "Enable",
    "DetectionMode": "Premium",
    "AsyncAmd": "false"
  }'
```

### Asynchronous Mode

In asynchronous mode, TeXML instructions execute in parallel with AMD. Results are sent to the `AsyncAmdStatusCallback` URL.

```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/calls/{connection_id} \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "From": "+13127367421",
    "To": "your-sip-user@sip.telnyx.com",
    "Url": "https://your-server.example.com/texml/instructions",
    "StatusCallback": "https://your-server.example.com/callback/status",
    "MachineDetection": "Enable",
    "DetectionMode": "Premium",
    "AsyncAmd": "true",
    "AsyncAmdStatusCallback": "https://your-server.example.com/callback/amd-status"
  }'
```

### AnsweredBy Values

| Value | Description |
|-------|-------------|
| `human` | A human answered the call |
| `machine` | An answering machine was detected |
| `fax` | A fax machine was detected |
| `unknown` | Detection was inconclusive |

The `MachineDetection` parameter accepts `Enable`, `Disable` (default), or `DetectMessageEnd`. The `DetectionMode` parameter accepts `Regular` (default) or `Premium`.

The `AsyncAmdStatusCallback` includes `AnsweredBy`, `CallSid`, and `AccountSid` parameters.

## TeXML and TwiML Compatibility

TeXML was designed for easy migration from Twilio, supporting many of the same verbs and nouns.

### Verb Compatibility

| Verb | TwiML | TeXML |
|------|-------|-------|
| `<AIGather>` | ❌ | ✅ |
| `<Dial>` | ✅ | ✅ |
| `<Enqueue>` | ✅ | ✅ |
| `<Gather>` | ✅ | ✅ |
| `<Hangup>` | ✅ | ✅ |
| `<HttpRequest>` | ❌ | ✅ |
| `<Leave>` | ✅ | ✅ |
| `<Pause>` | ✅ | ✅ |
| `<Pay>` | ✅ | ❌ |
| `<Play>` | ✅ | ✅ |
| `<Record>` | ✅ | ✅ |
| `<Redirect>` | ✅ | ✅ |
| `<Refer>` | ✅ | ✅ |
| `<Reject>` | ✅ | ✅ |
| `<Say>` | ✅ | ✅ |
| `<Siprec>` | ✅ | ✅ |
| `<Stop>` | ✅ | ✅ |
| `<Stream>` | ✅ | ✅ |
| `<Suppression>` | ✅ | ✅ |
| `<Transcription>` | ✅ | ✅ |

### Noun Compatibility

| Noun | TwiML | TeXML |
|------|-------|-------|
| `<Client>` | ✅ | ❌ |
| `<Conference>` | ✅ | ✅ |
| `<Number>` | ✅ | ✅ |
| `<Room>` | ✅ | ❌ |
| `<Queue>` | ✅ | ✅ |
| `<Sip>` | ✅ | ✅ |
| `<VirtualAgent>` | ✅ | ❌ |

### REST API Endpoint Compatibility

Most Twilio REST API endpoints have compatible TeXML equivalents under `/Accounts/{AccountSid}/...`, including:

- **Calls** — Fetch, update, list, and initiate outbound calls
- **Conferences** — Fetch, update, list, manage participants
- **Recordings** — Request, fetch, update, delete (per call and per conference)
- **Streams** — Start and update media streaming
- **SIPREC** — Request and update SIPREC sessions
- **Queues** — Create, fetch, update, delete queue resources and members
- **Recording Transcriptions** — List, fetch, and delete

Endpoints **not** supported in TeXML include real-time transcriptions, Pay sessions, and UserDefinedMessages/UserDefinedMessageSubscriptions.

For full endpoint details see the [TeXML REST API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call).
