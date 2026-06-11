---
title: Telnyx Programmable Voice
summary: Telnyx Programmable Voice provides tools for building voice applications
  including SIPREC recording, speech-to-text transcription, call recording storage,
  SSML-based text-to-speech, and the TeXML markup language for declarative call control
  with TwiML compatibility.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ssml-tags/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
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
