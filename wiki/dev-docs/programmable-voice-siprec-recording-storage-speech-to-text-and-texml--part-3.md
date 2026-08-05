---
title: 'Programmable Voice: SIPREC, Recording Storage, Speech-to-Text, and TeXML'
summary: A consolidated reference for Telnyx Programmable Voice features covering
  SIPREC client and server configuration, call recording storage backends, real-time
  speech-to-text transcription, and the TeXML markup language including applications,
  instruction fetching, dynamic templating, HTTP requests, and answering machine detection.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
updated_at: 2026-08-05T14:04:31Z
---

# Programmable Voice: SIPREC, Recording Storage, Speech-to-Text, and TeXML

*Part 3 of 6 — see also: [Part 1](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-1.md), [Part 2](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-2.md), [Part 4](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-4.md), [Part 5](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-5.md), [Part 6](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-6.md)*

A consolidated reference for Telnyx Programmable Voice features covering SIPREC client and server configuration, call recording storage backends, real-time speech-to-text transcription, and the TeXML markup language including applications, instruction fetching, dynamic templating, HTTP requests, and answering machine detection.

## TeXML Instruction Fetching

On inbound calls (PSTN or external SIP to Telnyx), Telnyx fetches TeXML instructions from the URL defined on the TeXML Application associated with the SIP subdomain or phone number. On outbound calls (Telnyx to PSTN or external SIP), there are two ways to trigger instruction fetching.

### Inbound calls

A TeXML application can have a specific SIP subdomain or phone number assigned to it. When Telnyx receives a call to that SIP subdomain or phone number, it fetches instructions from the URL defined on the TeXML Application.

### Outbound calls

**Using a TeXML Application** — Trigger instruction fetching via the [TeXML Calls API](/api-reference/texml-rest-commands/initiate-an-outbound-call). A TeXML application is required:

```
curl -L 'https://api.telnyx.com/v2/texml/Accounts/:account_sid/Calls' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer YOUR_API_KEY' \
-d '{
  "ApplicationSid": "xxxxxxxx",
  "To": "+13121230000",
  "From": "+13120001234",
  "Url": "https://www.example.com/texml.xml",
  "StatusCallback": "https://www.example.com/statuscallback-listener"
}'
```

**Using SIP Trunking Connections** — Configure a SIP trunking connection of any type to "Park Outbound Calls". When an outbound call is initiated on that SIP connection, Telnyx parks the call leg, fetches instructions from the URL defined on the connection, and processes the call accordingly. A TeXML application is not required.

### HTTP request details

When a call is handled by a TeXML application, Telnyx makes HTTP requests to fetch instructions from your application. These requests include specific parameters that provide context about the call.

- **Method** — Configurable (GET or POST, default is GET)
- **URL** — The URL configured for the TeXML application
- **Failover URL** — Used if the primary URL is unavailable (optional)

#### Request parameters

The following parameters are always included when Telnyx fetches TeXML instructions:

| Parameter | Description | Example |
| --- | --- | --- |
| AccountSid | The user's Telnyx account ID | 6a9a7976-012e-45d2-9258-6f5dc68d861e |
| CallSid | Unique identifier for the call | fcc47bc6-e428-11ed-ad79-02420aef00b4 |
| CallSidLegacy | Legacy call ID format for backward compatibility | fcc47bc6-e428-11ed-ad79-02420aef00b4 |
| CallerId | The identifier of the caller | +13122010091 |
| CallingPartyType | The type of calling party. Possible values: `sip` or `pstn` | sip |
| From | The phone number that initiated the call | +13122010091 |
| FromSipUri | SIP URI address of the caller | +13122010091@10.239.182.10 |
| To | The phone number that received the call | +13122010090 |
| ToSipUri | SIP URI address that received the call | +13122010090@sip.telnyx.com |
| ConnectionId | Telnyx connection ID used for the call | 1568109700606592442 |

Additional optional parameters may be added depending on the call context. See the documentation for each [TeXML verb](texml-twiml-compatibility.md) for the full list.

#### Parameter format

- **GET requests** — parameters are added as URL query parameters
- **POST requests** — parameters are added in the request body as form-encoded data

#### Response requirements

The application should respond with valid TeXML:

- Be valid XML with a root `<Response>` element
- Not exceed size limits
- Return HTTP status code 200 OK

#### Example

Request (GET method):

```
GET /texml-instructions?
  AccountSid=6a9a7976-012e-45d2-9258-6f5dc68d861e&
  CallSid=fcc47bc6-e428-11ed-ad79-02420aef00b4&
  CallSidLegacy=fcc47bc6-e428-11ed-ad79-02420aef00b4&
  From=%2B13122010091&
  To=%2B13122010090&
  ConnectionId=1568109700606592442&
  CallStatus=in-progress
```

Response:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Welcome to the Telnyx TeXML service.</Say>
  <Gather timeout="5" numDigits="1">
    <Say>Press 1 to continue.</Say>
  </Gather>
</Response>
```

### Best practices

- Always verify the `CallSid` parameter to ensure the request is legitimate
- Include error handling in your application to handle unexpected parameters
- Keep response times low to avoid call delays
- Use the parameters to customize call flows based on caller information
- Test your application with various parameter combinations

## TeXML Interpreter

### Basic syntax

A proper TeXML response comprises the following elements:

- **`<Response>` element** — tag defining the body of the TeXML document
- **verb** — an XML tag denoting the desired action
- **noun** — an XML tag denoting the object of the desired action

```
<?xml version="1.0" encoding="UTF-8"?>

<!-- TeXML files must contain the Response element -->
<Response>
 <!-- Say and Dial are Verbs -->
    <Say>Thank you for calling Telnyx. Please hold.</Say>
    <Dial>
   <!-- Number is a Dial Noun -->
        <Number>+13129457420</Number>
    </Dial>
</Response>
```

### Dynamic parameters

Use [Mustache Templates](https://mustache.github.io/mustache.5.html) to generate TeXML instructions dynamically at runtime.

#### Inserting dynamic content

Create TeXML instructions using Mustache templating and set a variable such as `{{PhoneNumber}}`:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Number>{{PhoneNumber}}</Number>
  </Dial>
</Response>
```

The phone number is replaced at runtime by setting the TeXML webhook URL to include `PhoneNumber` as a parameter:

```
curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
--data-urlencode "To=+13121230000" \
--data-urlencode "From=+13120001234" \
--data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumber=+18771234567" \
--data-urlencode "StatusCallback=https://www.example.com/statuscallback-listener" \
--header "Authorization: Bearer YOUR_API_KEY"
```

Request parameters set by Telnyx (for example, `CallSid`, `From`, `To`) are also available for the Mustache template. See the [TeXML applications API reference](https://developers.telnyx.com/api-reference/texml-applications/list-all-texml-applications) for the full list.

#### Iterating through lists

Set arrays as parameters in the TeXML webhook URL and let Mustache handle them. For example, to dial two numbers, add a `Numbers` list parameter to the callback URL:

```
curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
--data-urlencode "To=+13121230000" \
--data-urlencode "From=+13120001234" \
--data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumbers[]=+18771234567&PhoneNumbers[]=+18771234568" \
--data-urlencode "StatusCallback=https://www.example.com/statuscallback-listener" \
--header "Authorization: Bearer YOUR_API_KEY"
```

Handle the `PhoneNumbers` parameter in the TeXML instructions:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
  {{#PhoneNumbers}}
    <Number>{{.}}</Number>
  {{/PhoneNumbers}}
  </Dial>
</Response>
```

This is parsed as:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Number>+18771234567</Number>
    <Number>+18771234568</Number>
  </Dial>
</Response>
```

#### Conditional content

Use `if/else` statements to render conditional content. For example, dial a specific number depending on the `From` parameter:

```
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

Supported operators are `==` and `!=`. There is no operator for checking if a parameter value is not null.
