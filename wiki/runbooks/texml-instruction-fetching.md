---
title: TeXML Instruction Fetching
summary: How Telnyx fetches TeXML instructions for inbound and outbound calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching/index
    content_hash: d58c37ec0e022e630c3b0b89e8ec7eeaedbfddef869bc8afc688fe4537668b5c
updated_at: 2026-04-10T00:00:00Z
---

# TeXML Instruction Fetching

How Telnyx fetches TeXML instructions for inbound and outbound calls

On inbound calls (PSTN or External SIP to Telnyx), Telnyx fetches TeXML instructions from the URL defined on the TeXML Application associated with the SIP subdomain or phone number.

On outbound calls (Telnyx to PSTN or External SIP), there are two ways the user can trigger instructions fetching, the details of which are described below.

## Instruction Fetching on Inbound Calls

An instance of TeXML application can have a specific SIP subdomain or phone number assigned to it. When Telnyx
receives a call to that SIP subdomain or phone number, Telnyx will fetch the instructions from the URL defined on the TeXML Application.

## Instruction Fetching on Outbound Calls

### Using TeXML Application

Instructions fetching can be triggered by [TeXML Calls API](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call). In this case, a TeXML application is required.

Example:

```bash theme={null}
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

### Using SIP Trunking Connections

The user can configure a SIP trunking connection of any type to "Park Outbound Calls". When the user initiates an outbound call on that
SIP connection, Telnyx will "park" that call leg, fetch the instructions from the URL defined on the connection, and then process the
call based on the instructions.

In this use case, a TeXML application is not required.

## HTTP Request Details

When a call is being handled by a TeXML application, Telnyx makes HTTP requests to fetch instructions from the user's application. These requests include specific parameters that provide context about the call, allowing the user's application to generate appropriate TeXML responses.

* Method: Configurable (GET or POST, default is GET)
* URL: The URL configured for the user's TeXML application
* Failover URL: Used if the primary URL is unavailable (optional)

### Request Parameters

When Telnyx makes a request to fetch TeXML instructions, the following parameters are always included:

| Parameter        | Description                                             | Example                                                           |
| ---------------- | ------------------------------------------------------- | ----------------------------------------------------------------- |
| AccountSid       | The user's Telnyx account ID                            | 6a9a7976-012e-45d2-9258-6f5dc68d861e                              |
| CallSid          | Unique identifier for the call                          | fcc47bc6-e428-11ed-ad79-02420aef00b4                              |
| CallSidLegacy    | Legacy call ID format for backward compatibility        | fcc47bc6-e428-11ed-ad79-02420aef00b4                              |
| CallerId         | The identifier of the caller                            | +13122010091                                                      |
| CallingPartyType | The type of calling party. Possible values: sip or pstn | sip                                                               |
| From             | The phone number that initiated the call                | +13122010091                                                      |
| FromSipUri       | Sip Uri address of the caller                           | +13122010091\@10.239.182.10                                       |
| To               | The phone number that received the call                 | +13122010090                                                      |
| ToSipUri         | Sip Uri address that received the call                  | [+13122010090@sip.telnyx.com](mailto:+13122010090@sip.telnyx.com) |
| ConnectionId     | Telnyx connection ID used for the call                  | 1568109700606592442                                               |

### Optional Parameters

Depending on the call context, additional parameters are added to the request. Full list of the parameters can be found on the documentation page for each of the [TeXML verbs](texml-and-twiml-compatibility.md)

### Parameter Format

Depending on the HTTP method selected for the requests, the parameters are added in the following way:

* GET requests - as URL query parameters
* POST requests - in the request body as form-encoded data

### Response Requirements

The user's application should respond with valid TeXML. The response should:

* Be valid XML with a root `` element
* Not exceed size limits
* Return HTTP status code 200 OK

### Example

#### Request (GET method)

```bash theme={null}
GET /texml-instructions?
  AccountSid=6a9a7976-012e-45d2-9258-6f5dc68d861e&
  CallSid=fcc47bc6-e428-11ed-ad79-02420aef00b4&
  CallSidLegacy=fcc47bc6-e428-11ed-ad79-02420aef00b4&
  From=%2B13122010091&
  To=%2B13122010090&
  ConnectionId=1568109700606592442&
  CallStatus=in-progress
```

#### Response

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

  Welcome to the Telnyx TeXML service.
  <Gather timeout="5" numDigits="1">
    Press 1 to continue.

```

## Best Practices

Here are a few best practices to follow:

* Always verify the CallSid parameter to ensure the request is legitimate
* Include error handling in your application to handle unexpected parameters
* Keep response times low to avoid call delays
* Use the parameters to customize call flows based on caller information
* Test your application with various parameter combinations
* By properly handling these parameters, you can create dynamic, responsive TeXML applications that provide excellent caller experiences
