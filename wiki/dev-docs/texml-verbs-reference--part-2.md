---
title: TeXML Verbs Reference
summary: A consolidated reference for the TeXML verbs available in Telnyx Programmable
  Voice, covering call control, media playback, recording, transcription, conferencing,
  payments, and SIPREC. Each verb section lists attributes, child nouns, examples,
  and the callbacks that the platform emits.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/recording
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
updated_at: 2026-08-05T14:05:15Z
---

# TeXML Verbs Reference

*Part 2 of 7 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 3](texml-verbs-reference--part-3.md), [Part 4](texml-verbs-reference--part-4.md), [Part 5](texml-verbs-reference--part-5.md), [Part 6](texml-verbs-reference--part-6.md), [Part 7](texml-verbs-reference--part-7.md)*

A consolidated reference for the TeXML verbs available in Telnyx Programmable Voice, covering call control, media playback, recording, transcription, conferencing, payments, and SIPREC. Each verb section lists attributes, child nouns, examples, and the callbacks that the platform emits.

## HttpRequest

The `<HttpRequest>` verb sends a request to an external server. It consists of two child nodes: `<Request>` and `<Response>`.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `async` | Defines if TeXML should wait for the request response. When set to `false`, the callback will be sent to the action URL when the request is processed. | — | `false` |
| `action` | Defines the action URL that will be used to send the callback when the request is processed (only if `async` is set to `false`). | — | — |

### Child verbs/nouns

- `Request` — defines all the attributes of the request. It can have two child nodes: `<Headers>` and `<Body>`.
- `Response` — defines all the attributes of the response. It can have two child nodes: `<Headers>` and `<Body>`.

### Examples

```xml
<Response>
    <HttpRequest async="true">
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
            <![CDATA[
                {
                    "from":{{From}}
                }
            ]]>
            </Body>
        </Request>
    </HttpRequest>
</Response>
```

```xml
<Response>
    <HttpRequest async="false" action="https://example.com">
        <Request url="https://example.com" method="POST">
            ...
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
</Response>
```

### Expected callbacks

When the HTTP request completes, a callback is sent to the `action` URL. See the [HTTP Request Callback](https://developers.telnyx.com/api-reference/callbacks/texml-http-request) for the full payload reference.

## Leave

The `<Leave>` verb removes a call from the queue and continues with the next verb after the original `<Enqueue>`. `<Leave>` does not support any attributes.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Leave/>
</Response>
```

## Pause

The `<Pause>` verb waits silently for a specified number of seconds (one second by default). No nouns can be nested within `<Pause>`, and a self-closing tag must be used.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `length` | Seconds to pause. | `1`–`180` | `1` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pause length="5"/>
</Response>
```
