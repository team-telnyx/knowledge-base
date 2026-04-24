---
title: HttpRequest
summary: The `` verb sends a request to the external servers.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest/index
    content_hash: 14ddd2c0ee8f4d08e55e0291388f562578bac2441eb7e80be501b1953f2ae539
updated_at: 2026-04-10T00:00:00Z
---

# HttpRequest

The `` verb sends a request to the external servers. It consists of 2 child nodes `` and ``

## Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>async</code></td>
      <td> Defines if TeXML process should wait for the request response. When it is set to false, the callback will be sent to the action URL, when the request is processed </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>action</code></td>
      <td> Defines the action url that will be used to send the callback when the request is processed (only if async is set to false) </td>

      <td />

      <td>-</td>
    </tr>
  </tbody>
</table>

## Child verbs/nouns

<table>
  <thead>
    <tr>
      <th>NOUN/VERB</th>
      <th>DESCRIPTION</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>Request</code></td>
      <td> The `` node defines all the attributes of the request. It can have 2 child nodes `` and `` </td>
    </tr>

    <tr>
      <td><code>Response</code></td>
      <td> The `` node defines all the attributes of the response. It can have 2 child nodes `` and `` </td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}

    <HttpRequest async=”true”>
        <Request url="https://example.com" method="POST">

                Authorization
                Bearer API_key

                Content-Type
                application/json

        <![CDATA[
                {
                    "from":{{From}}
                }
                ]]>

```

```xml theme={null}

    <HttpRequest  async=”false” action="https://example.com">
        <Request url="https://example.com" method="POST">
        ...

            JSON
            200

                    contact.name.first
                    first_name

                    contact.name.last
                    last_name

```

## Expected callbacks

When the HTTP request completes, a callback is sent to the `action` URL. See [HTTP Request Callback](https://developers.telnyx.com/api-reference/callbacks/texml-http-request) for the full payload reference.
