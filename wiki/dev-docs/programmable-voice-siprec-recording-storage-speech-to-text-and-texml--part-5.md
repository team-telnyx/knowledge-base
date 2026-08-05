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

*Part 5 of 6 — see also: [Part 1](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-1.md), [Part 2](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-2.md), [Part 3](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-3.md), [Part 4](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-4.md), [Part 6](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-6.md)*

A consolidated reference for Telnyx Programmable Voice features covering SIPREC client and server configuration, call recording storage backends, real-time speech-to-text transcription, and the TeXML markup language including applications, instruction fetching, dynamic templating, HTTP requests, and answering machine detection.

## Sending HTTP Requests in TeXML

Use the `<HTTPRequest>` verb to integrate with external systems from a TeXML file without needing your own server-side application, retrieve information for call flows from external systems, and send notifications to any REST API.

### Sending an HTTP request

```
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
            <![CDATA[
                    {
                        "key":"value"
                    }
                    ]]>
            </Body>
        </Request>
    </HttpRequest>
</Response>
```

You can define headers, the HTTP method (GET or POST), and the body.

### Synchronous requests

Requests are sent asynchronously by default — the TeXML process does not wait for the result and immediately executes the next instruction. Set the `async` attribute to `true` to make the TeXML process wait for the HTTP response and send a callback to the action URL immediately afterward:

```
<Response>
<HttpRequest>
    <Request url=”https://example.com” method=”POST” async=”true”>
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
                “from”:{{From}}
            }
            ]]>
    </Body>
    </Request>
</HttpRequest>
</Response>
```

Define new variables that will be sent with the callbacks using values from the HTTP response:

```
<Response>
    <HttpRequest>
        <Request url=”https://example.com” method=”POST” async=”true”>
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
                    “from”:{{From}}
                }
                ]]>
        </Body>
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

### Using secrets

Store API keys and other secrets in secure storage via a dedicated REST endpoint:

```
curl --location --request POST 'https://api.telnyx.com/v2/texml/secrets/' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"your_secret_name",
    "value":"your_secret_value"
}'
```

Stored secrets can be referenced in TeXML definitions and are redacted from all logs and callbacks:

```
<Response>
    <HttpRequest>
        <Request url=”https://example.com” method=”POST” async=”true”>
        <Headers>
            <Header>
                <Key>Authorization</Key>
                <Value>Bearer {{#secret}}your_secret_name{{/secret}}</Value>
            </Header>
            <Header>
                <Key>Content-Type</Key>
                <Value>application/json</Value>
            </Header>
        </Headers>
        <Body>
        <![CDATA[
                {
                    “from”:{{From}}
                }
                ]]>
        </Body>
        </Request>
    </HttpRequest>
</Response>
```

### Example: Slack notification with Salesforce caller lookup

1. Upload an API key to your Slack workspace under the name `slack_api_key`:

```
curl --location --request POST 'https://api.telnyx.com/v2/texml/secrets/' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"slack_api_key",
    "value":"your_api_key_value"
}'
```

2. Upload a token to the Salesforce API under the name `salesforce_token`:

```
curl --location --request POST 'https://api.telnyx.com/v2/texml/secrets/' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"salesforce_token",
    "value":"your_token_value"
}'
```

3. Create a TeXML file that sends a message to the Slack channel and calls your SIP account, named `slack_http_request`:

```
<Response>
    <HttpRequest async="true">
        <Request url="https://slack.com/api/chat.postMessage" method="POST">
            <Headers>
                <Header>
                    <Key>Authorization</Key>
                    <Value>Bearer {{#secret}}slack_api_key{{/secret}}</Value>
                </Header>
                <Header>
                    <Key>Content-Type</Key>
                    <Value>application/json</Value>
                </Header>
                </Headers>
            <Body>
            <![CDATA[
                        {
                            "Channel": channel_id,
                            "text":"You have a call from {{caller_name}}!"
                        }
                        ]]>
            </Body>
        </Request>
    </HttpRequest>
    <Dial>
        <Sip>
            sip:jack@example.com
        </Sip>
    </Dial>
</Response>
```

4. Create a TeXML file that retrieves the caller information and name from Salesforce:

```
<Response>
    <HttpRequest action="https://api.telnyx.com/v2/media/slack_http_request.xml" async="false">
        <Request url="https://your_salesforce _domain.my.salesforce.com/services/data/v56.0/query?q=SELECT%20name%20from%20Account%20WHERE%20Phone%3D%27{{#url_encode}}{{From}}{{/url_encode}}%27" method="GET" >
            <Headers>
            <Header>
                <Key>Authorization</Key>
                <Value>Bearer {{#secret}}salesforce_token{{/secret}}</Value>
            </Header>
            <Header>
                <Key>Content-Type</Key>
                <Value>application/json</Value>
            </Header>
            </Headers>
            <Body>
            </Body>
        </Request>
        <Response>
            <Type>JSON</Type>
            <StatusCode>200</StatusCode>
            <Content>
            <Field>
                <Name>records[0].Name</Name>
                <Value>caller_name</Value>
            </Field>
            </Content>
        </Response>
    </HttpRequest>
</Response>
```

5. Update your TeXML application webhook URL (see [TeXML Setup](texml-setup.md) for application creation).

![TeXML application setup](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/salesforce_slack_tutorial.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=99aacc1d3b0d3ff405735257aee84255)

6. Make a call to the number associated with the TeXML application and observe the notification in your Slack workspace.
