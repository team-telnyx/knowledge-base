---
title: Getting Started with Telnyx Programmable Fax
summary: Telnyx's Programmable Fax service makes it easy to send and receive faxes from your computer or mobile device.
sources:
  - url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
    content_hash: 596280691529cc2e5468d3a10fb3f51924d3aad3c09400390f09e5f47d60665e
updated_at: 2026-04-10T00:00:00Z
---

# Getting Started with Telnyx Programmable Fax

Telnyx's Programmable Fax service makes it easy to send and receive faxes from your computer or mobile device. With our service, you can easily connect to your fax number from anywhere in the world.

## Introduction

Welcome to Telnyx Programmable Fax, a powerful tool that allows you to send and receive faxes seamlessly through HTTP endpoints. This guide will introduce you to the basics of setting up and using the Programmable Fax API.

## Prerequisites

Before you begin, you'll need to:

* Set up a Telnyx account. [Sign up](https://telnyx.com/sign-up) here if you haven't already.
* Obtain a phone number and create a Programmable Fax Application following our [Quickstart guide](../tutorial/quickstart-guide-for-programmable-fax.md).
* Generate a Telnyx V2 API Authentication key via the [Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/api-keys).

## Core Concepts

* Programmable Fax Application: Configure inbound traffic and authentication for your phone numbers.
* Outbound Voice Profile: Manage outbound traffic, billing, and allowed destinations.
* Webhooks: HTTP callbacks that notify your server about fax events.

## Hello World Example

Send Your First Fax Using cURL:

1. Authenticate Your Request: Include your API key in the header for authentication.
2. Specify Fax Details: Provide the media URL, connection ID (use your application id), and the 'to' and 'from' fax numbers in E.164 format.
3. Send the Fax:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/faxes \
--data-raw '{
  "connection_id": "234423",
  "media_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
  "to": "+13127367276",
  "from": "+13125790015"
}' \
--header 'Authorization: Bearer YourAPIKey'
```

Replace placeholders with your actual data.

1. Verify the Response: Check for an HTTP 202 response indicating successful fax initiation

## Next Steps

* Explore advanced features like receiving faxes and detailed webhook management.
* Check out our detailed tutorials for comprehensive guidance.

## Additional Resources

* Visit our API documentation for in-depth understanding.
* Join our community forums for support and discussion

## Feedback

We value your feedback. If you have questions or need help troubleshooting, our support team is ready to assist. Contact us [here](https://support.telnyx.com/).

## Glossary

1. Programmable Fax Application: A configuration within the Telnyx platform used to manage inbound and outbound fax traffic. It includes settings for authentication and handling of fax transmissions.
2. Outbound Voice Profile: A setting in Telnyx that allows users to initiate outbound traffic, including faxes. It includes configurations for billing, traffic management, and permitted destinations.
3. Fax\_id: A unique identifier assigned to each fax transmission. It is used to track and manage specific fax communications within the Telnyx system.
4. Media\_url: The URL pointing to the document you wish to fax, typically in PDF format. This URL is included in the fax command to specify the fax content.
5. Connection\_id: An identifier for your specific application or connection within Telnyx, used to route the fax correctly and associate it with your account.
6. E.164 Format: An internationally-recognized format for phone numbers, used in specifying the 'to' and 'from' fields in fax commands.
7. Failure\_reason: A field in the webhook payload that provides the reason for a fax's failure, helping in troubleshooting and understanding delivery issues.
8. Ngrok: A tunneling tool used to expose a local server to the internet, often used for testing webhook endpoints in development environments.
9. cURL: A command-line tool used for sending requests to URLs, commonly used for interacting with APIs like Telnyx's Programmable Fax API.


## Related Pages

- [Getting Started with Telnyx Voice API](../runbooks/getting-started-with-telnyx-voice-api.md)
- [Getting Started with Video](../runbooks/getting-started-with-video.md)
- [Getting Started with Android Client SDK](../runbooks/getting-started-with-android-client-sdk.md)
- [Getting Started with 10DLC](../tutorial/getting-started-with-10dlc.md)
- [Quickstart Guide for Programmable Fax](../tutorial/quickstart-guide-for-programmable-fax.md)
