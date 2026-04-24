---
title: Sending Commands
summary: Telnyx's Programmable Fax offers an easy way to send faxes from your applications.
sources:
  - url: https://developers.telnyx.com/docs/programmable-fax/sending-commands/index
    content_hash: 744df12620479b17af72310eb6fa61c873d8dfba6fd57c50f2bd6c48475b61fc
updated_at: 2026-04-10T00:00:00Z
---

# Sending Commands

Telnyx's Programmable Fax offers an easy way to send faxes from your applications. With our RESTful API, you can easily send faxes anywhere in the world.

A Programmable Fax API command is sent with a fax\_id. The fax\_id allows a user to communicate to Telnyx the fax the user wants to take an action on.

The Telnys Programmable Fax API supports PDF files. To initiate sending the fax, we need to send the request to the Telnyx Programmable Fax API endpoint [https://api.telnyx.com/v2/faxes](https://api.telnyx.com/v2/faxes).

## Authentication

With the request we need to send additional parameters containing authentication information so Telnyx knows which account to send the fax from and information about the destination and file being sent.

<table>
  <tbody>
    <tr>
      <td>HEADER</td>
      <td>DESCRIPTION</td>
    </tr>

    <tr>
      <td>media\_url</td>
      <td>Authorization: Bearer YOUR\_API\_KEY</td>
    </tr>

    <tr>
      <td>connection\_id</td>
      <td>Authorization: Bearer YOUR\_API\_KEY</td>
    </tr>

    <tr>
      <td>to</td>
      <td>Authorization: Bearer YOUR\_API\_KEY</td>
    </tr>

    <tr>
      <td>from</td>
      <td>Authorization: Bearer YOUR\_API\_KEY</td>
    </tr>

    <tr>
      <td>Authorization: Bearer</td>
      <td> The prefix to your API V2 key created in Step 2.</td>
    </tr>
  </tbody>
</table>

## Available commands and their expected Webhooks

Telnyx sends webhooks to update on the status of Programmable Fax. Webhooks will also be sent in response to requests to list and delete faxes.

<table>
  <tbody>
    <tr>
      <td>COMMAND</td>
      <td>ASSOCIATED WEBHOOKS</td>
    </tr>

    <tr>
      <td>Send a fax</td>
      <td>fax.queued<br />
      fax.media.processed<br />
      fax.sending.started<br />
      fax.delivered<br />
      fax.failed</td>
    </tr>
  </tbody>
</table>

## Response when sending command

When you send a Programmable Fax API Command, you will immediately receive an http response. Responses include, but are not limited to:

<table>
  <tbody>
    <tr>
      <td>HTTP STATUS CODE</td>
      <td>MESSAGE</td>
      <td>DESCRIPTION</td>
    </tr>

    <tr>
      <td>202</td>
      <td>OK</td>
      <td>The request succeeded.</td>
    </tr>

    <tr>
      <td>403</td>
      <td>Forbidden</td>
      <td>The request was valid, however the user is not authorized to perform this action.</td>
    </tr>

    <tr>
      <td>404</td>
      <td>Not Found</td>
      <td>The requested resource could not be found.</td>
    </tr>

    <tr>
      <td>422</td>
      <td>Invalid Parameters</td>
      <td>The request has invalid parameters.</td>
    </tr>
  </tbody>
</table>

## Example: Sending commands

To send a fax, send a POST request to the [https://api.telnyx.com/v2/faxes](https://api.telnyx.com/v2/faxes) endpoint as shown in the example below.

## WITH A API V2 KEY

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/faxes \
--data-urlencode "media_url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" \
--data-urlencode "connection_id=1232154810234" \
--data-urlencode "to=+13129457420" \
--data-urlencode "from=+19459457421" \
--header "Authorization: Bearer APIAuthKey_fromPortal"
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added


## Related Pages

- [AT Commands](../runbooks/at-commands.md)
