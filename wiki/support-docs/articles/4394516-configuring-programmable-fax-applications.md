---
title: "Configuring Programmable Fax Applications"
summary: "This article describes the in-depth setup of Programmable Fax / Applications on your Mission Control Portal in order to send and receive faxes via our API."
sources:
- url: "https://support.telnyx.com/en/articles/4394516-configuring-programmable-fax-applications"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/4394516-configuring-programmable-fax-applications.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/4394516-configuring-programmable-fax-applications.md -->

# Configuring Programmable Fax Applications

This article describes the in-depth setup of Programmable Fax / Applications on your Mission Control Portal in order to send and receive faxes via our API.

## Configuration of Programmable Fax

The [Programmable Fax](https://portal.telnyx.com/#/app/fax/applications) applications section is located on the left hand side of the portal.

Click on this button below and it will directly get you to the Programmable Fax Applications page.

[Programmable Fax Applications](https://portal.telnyx.com/#/app/fax/applications)

## Step By Step Guide to Programmable Fax

There are 4 sections which you can configure:

1. ***App Info***
2. ***Custom Settings***
3. ***Inbound Settings***
4. ***Outbound Settings***.

## Fax Application Settings

## App Name

Click on " Create your first application" and assign a name to this application to better manage the application. You also have access to the quickstart guide on the top right as well as the Application ID which will be required for API Interactions.

[![](_images/4c0a66afd40bceb057855d068c9db5390959f479ae211d44dc28b9337cf12751.png)](/_images/4c0a66afd40bceb057855d068c9db5390959f479ae211d44dc28b9337cf12751.png)

## Send a webhook to the URL

You will need to input a URL where all the [webhook](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks) events will be sent. Also, you can setup a fail-over URL. If two consecutive delivery attempts to the primary URL fail, Telnyx will attempt delivery to this URL. **NOTE**: Must include a scheme such as 'https'.

[![](_images/8afde2272d0d9f51d71a5b63f88e7f8879011a77b7da9eb9bd8c228ed0b385cd.png)](/_images/8afde2272d0d9f51d71a5b63f88e7f8879011a77b7da9eb9bd8c228ed0b385cd.png)

## Custom webhook timeout (seconds)

Specify time, in seconds, for Telnyx to wait for a response to a webhook request.

​

[![](_images/b6a0652040afb78e8ecb40aa12ceeddc667d2b8eb9ec2282fc91041b852f44c1.png)](/_images/b6a0652040afb78e8ecb40aa12ceeddc667d2b8eb9ec2282fc91041b852f44c1.png)

## AnchorSite® Selection

"Latency" directs Telnyx to route media through the site with the lowest round-trip time to the user's connection. Telnyx calculates this time using ICMP ping messages. This can be disabled by specifying a site to handle all media.

[![](_images/b9f9669758a768ac993a415a876065e9d65ab6510db83fd152f330b9648c987b.png)](/_images/b9f9669758a768ac993a415a876065e9d65ab6510db83fd152f330b9648c987b.png)

## RTCP Capture

Enable capture of RTCP reports to build QoS Reports (found under Debugging > SIP Call Flow Tool)

[![](_images/7f39c90952196fddda3cec76e280816f76322664c37bab5df6329fe2e14ccbea.png)](/_images/7f39c90952196fddda3cec76e280816f76322664c37bab5df6329fe2e14ccbea.png)

---

## Custom Headers

[![](_images/18497ff58697d74702bf0812f44a1c8281803bf2c33ee6e82dade24670ca0f13.png)](/_images/18497ff58697d74702bf0812f44a1c8281803bf2c33ee6e82dade24670ca0f13.png)

Specify the timezone and customer name which will be included in your programmable outbound faxes on the recipients side.

## Inbound Settings

You can configure your global application settings for inbound calls over here.

[![](_images/941b13da788dd87d62d312028e97cc98f95a4c30a2c28e346a718dd03174649e.png)](/_images/941b13da788dd87d62d312028e97cc98f95a4c30a2c28e346a718dd03174649e.png)

## Subdomain

Specify a **subdomain** that can be used to receive calls to a Connection, in the same way a phone number is used, from a SIP endpoint.

- Example: the subdomain "**example**.sip.telnyx.com" can be called from any SIP endpoint by using the SIP URI "sip:@**example**.sip.telnyx.com" where the user part can be any alphanumeric value.
- You only need to specify the subdomain in this field, there is no need to specify a Telnyx domain after it.
- **SIP subdomain receive settings**: In this field, either you setup your receive SIP subdomain connection from anyone or only connections.

## Inbound Channel Limit

You can limit the total number of inbound calls to phone numbers associated with this connection.

## File Type

Specify whether you want Telnyx to deliver your inbound faxes as a PDF or TIFF file type.

---

## Outbound Settings

## Outbound Voice Profile

Assign your application to an outbound voice profile in order to make outbound calls.

## Outbound Channel Limit

You can limit the total number of outbound calls to phone numbers associated with this connection.

[![](_images/ff01c19c94400d1827f53bfe9b80ac8d184705be4c5771553f27b10374f2490d.png)](/_images/ff01c19c94400d1827f53bfe9b80ac8d184705be4c5771553f27b10374f2490d.png)

---

## Notes on Programmable Fax

Don't forget to assign the fax application to your purchased [numbers](https://portal.telnyx.com/#/app/numbers/my-numbers), in order to receive faxes to your application and for Telnyx to send the webhook events when faxes are received to our network.

Check out our fax API quick-start guide [here](https://developers.telnyx.com/docs/programmable-fax/get-started) and more detail on the API endpoints in our [developer center](https://developers.telnyx.com/docs/programmable-fax).

## Where can I find my Fax application or app id?

Once you've successfully created your Fax application, it is given an application id that can be seen within the application settings as seen in the below picture.

[![](_images/1a5bfb6f5186827f283d52f18c03a88343eedefd818c6b699700f9a014504ead.png)](/_images/1a5bfb6f5186827f283d52f18c03a88343eedefd818c6b699700f9a014504ead.png)

## Why do I need an Fax application or app id?

The Fax application id is used to reference or trigger your API calls programmatically. Don't forget to reference our [developer documentation](https://developers.telnyx.com/docs/programmable-fax) to see how you can control your faxes.

## Where can I find the developer documentation for your programmable fax product?

You can see the specific endpoints here:

1. Send a fax: <https://developers.telnyx.com/api-reference/programmable-fax/send-a-fax>
2. View a list of faxes: <https://developers.telnyx.com/api-reference/programmable-fax/list-faxes>
3. View a single fax: <https://developers.telnyx.com/api-reference/programmable-fax/view-a-fax>
4. Delete a fax: <https://developers.telnyx.com/api-reference/programmable-fax/delete-a-fax>
5. Refresh a fax: <https://developers.telnyx.com/api-reference/programmable-fax/refresh-a-fax>
6. Cancel a fax: <https://developers.telnyx.com/api-reference/programmable-fax/cancel-a-fax>

---

Related Articles

- [Fax service with Telnyx (via T.38 or G711)](https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711)
- [Configuring Call Control/TeXML Applications - Voice API](https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api)
- [SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)
- [Fax API - Error List](https://support.telnyx.com/en/articles/4967498-fax-api-error-list)
- [Grandstream HT802: Telnyx Setup](https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup)
