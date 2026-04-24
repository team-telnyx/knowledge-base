---
title: Sending HTTP requests in TeXML - tutorial
summary: Learn how to send HTTP requests using Telnyx Programmable Voice and TeXML.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests/index
    content_hash: 65cf04b70c290f0f617e4ff4fdf24c534055baf2e70b053f4d60bc55b27428e5
updated_at: 2026-04-10T00:00:00Z
---

# Sending HTTP requests in TeXML - tutorial

Learn how to send HTTP requests using Telnyx Programmable Voice and TeXML. Explore comprehensive documentation, tutorials, and examples to seamlessly integrate HTTP requests into your voice applications. Empower your voice communication with Telnyx's robust Programmable Voice solutions.

In the [previous tutorial](texml-bin-dynamic-content.md), we explained how to use dynamic parameters in the TeXML instructions.

In this tutorial, we’ll cover how to integrate your systems using HTTP requests from a TeXML file without needing your own server-side application, as well as retrieve required information for call flows from external systems and send notifications to any REST API.

## Sending HTTP request

The requests can be sent using `` verb in the following way:

```xml theme={null}

            <Request url="https://example.com" method="POST">

                        Authorization
                        Bearer API_key

                        Content-Type
                        application/json

                <![CDATA[
                        {
                            "key":"value"
                        }
                        ]]>

```

As part of the verb structure you can define the following aspects of the request:

* Headers
* The method for the request (GET or POST)
* And the body

## Synchronous requests

The requests are sent asynchronously by default. The TeXML process does not wait for the result of the request and immediately executes the next instruction from the TeXML file.

It is possible to change that behavior by using the `async` attribute and setting it to true. In that case, the TeXML process will wait for the HTTP response and send a callback to the action URL immediately afterward.

```xml theme={null}

        <Request url=”https://example.com” method=”POST” async=”true”>

                Authorization
                Bearer API_key

                Content-Type
                application/json

        <![CDATA[
                {
                    “from”:{{From}}
                }
                ]]>

```

You can define new variables that will be sent with the callbacks using the values from the HTTP response.

```xml theme={null}

            <Request url=”https://example.com” method=”POST” async=”true”>

                    Authorization
                    Bearer API_key

                    Content-Type
                    application/json

            <![CDATA[
                    {
                        “from”:{{From}}
                    }
                    ]]>

                JSON
                200

                        contact.name.first
                        first_name

                        contact.name.last
                        last_name

```

## Using secrets

API keys or any other secrets can be stored in the secure storage. You can upload them using a dedicated REST endpoint.

```bash theme={null}
    curl --location --request POST 'https://api.telnyx.com/v2/texml/secrets/' \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name":"your_secret_name",
        "value":"your_secret_value"
    }'
```

Stored secrets can be used in the TeXML definitions. They will be redacted from all logs and won’t be sent in the callbacks as well.

```xml theme={null}

            <Request url=”https://example.com” method=”POST” async=”true”>

                    Authorization
                    Bearer {{#secret}}your_secret_name{{/secret}}

                    Content-Type
                    application/json

            <![CDATA[
                    {
                        “from”:{{From}}
                    }
                    ]]>

```

## Sending notifications about the call to your Slack workspace using information about the caller retrieved from Salesforce database

In this section we will present how to retrieve the information about the caller from the Salesforce database and send it as a message to the Slack channel.

1. Upload an api\_key to your Slack workspace under the name slack\_api\_key

```bash theme={null}
        curl --location --request POST 'https://api.telnyx.com/v2/texml/secrets/' \
        --header 'Authorization: Bearer YOUR_API_KEY' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "name":"slack_api_key",
            "value":"your_api_key_value"
        }'
```

2. Upload a token to the Salesforce API under the name salesforce\_token

```bash theme={null}
        curl --location --request POST 'https://api.telnyx.com/v2/texml/secrets/' \
        --header 'Authorization: Bearer YOUR_API_KEY' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "name":"salesforce_token",
            "value":"your_token_value"
        }'
```

3. Create a TeXML file that will send a message to the Slack channel and make a call to your SIP account and name it slack\_http\_request

```xml theme={null}

            <HttpRequest async="true">
                <Request url="https://slack.com/api/chat.postMessage" method="POST">

                            Authorization
                            Bearer {{#secret}}slack_api_key{{/secret}}

                            Content-Type
                            application/json

                    <![CDATA[
                                {
                                    "Channel": channel_id,
                                    "text":"You have a call from {{caller_name}}!"
                                }
                                ]]>

                    sip:jack@example.com

```

4. Create a TeXML file that will retrieve the information about the caller and their name from Salesforce.

```xml theme={null}

            <HttpRequest action="https://api.telnyx.com/v2/media/slack_http_request.xml" async="false">
                <Request url="https://your_salesforce _domain.my.salesforce.com/services/data/v56.0/query?q=SELECT%20name%20from%20Account%20WHERE%20Phone%3D%27{{#url_encode}}{{From}}{{/url_encode}}%27" method="GET" >

                        Authorization
                        Bearer {{#secret}}salesforce_token{{/secret}}

                        Content-Type
                        application/json

                    JSON
                    200

                        records[0].Name
                        caller_name

```

5. Update your TeXML application webhook URL (If you need to create your application, please take a look at this [tutorial](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup))

<img alt="TeXML application setup" />

6. Make a call to the number associated with the TeXML application and observe the notification in your Slack workspace
