---
source_url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
scraped: 2026-07-08
content_hash: b3a35ac78a793ecd5294a1cc14ac87758b05d6dd76e5bd45f19eabcba1c81225
---

Configuring Call Control/TeXML Applications - Voice API | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring Call Control/TeXML Applications - Voice API

This article describes the in-depth setup of Call Control / TeXML Applications on our Mission Control Portal.

Written by David

May 14, 2026

Table of contents

# Configuration of Call Control/TeXML Voice Apps

The [Call Control / TeXML](https://portal.telnyx.com/#/app/next/call-control/applications) applications section is located on the left hand side of the portal under Voice > Programmable Voice.

Click on this button below and it will directly get you to the Voice Applications page.

[Call Control / TeXML Applications](https://portal.telnyx.com/#/app/next/call-control/applications)

---

## Voice Applications (Call Control Voice API Application)

![](_images/fbd7eb7ada42f5e3.png)

## Voice App Name

Click on " Create Voice App" and assign a name to this application to better manage the application.

**AnchorSite® Selection**

"Latency" directs Telnyx to route media through the site with the lowest round-trip time to the user's connection. Telnyx calculates this time using ICMP ping messages. This can be disabled by specifying a site to handle all media.

![](_images/23af2aee8a7dec57.png)

![](_images/a4aeb2e38966e6ec.png)

### Send a webhook to the URL

You will need to input a URL where all the [webhook](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks) events will be sent. Also, you can setup a fail-over URL. If two consecutive delivery attempts to the primary URL fail, Telnyx will attempt delivery to this URL. **NOTE**: Must include a scheme such as 'https'.

![](_images/1236f3a3ccd1779c.png)

### Use Webhook API version

Determines which webhook format will be used based on the API version V1 or V2.

We recommend using API V2, as it contains a richer feature set versus the initial version which will be deprecated in the future.

![](_images/a43c14f22ec1c74c.png)

### Enable "hang-up" on timeout

When enabled, you will specify the number of seconds Telnyx will wait for commands from your application before hanging up.

![](_images/d433e78bdd04d8cc.png)

### Custom webhook retry delay (seconds)

In this field, you will need to specify a delay in seconds for Telnyx to wait before retrying an unsuccessful webhook delivery attempt. If not set, Telnyx will retry immediately.

![](_images/a8046b816610fc52.png)

### DTMF Type

There are three types in this field: RFC 2833, Inband and SIP INFO.

1. **RFC 2833**: Default and preferred setting for most use cases, not audible on the call audio.
2. **Inband**: Digits are passed along just like the rest of your voice as normal audio tones.
3. **SIP INFO**: Mainly used for SIP to SIP calls. [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf) type is negotiated between parties on the call.

![](_images/83448c867623f8d2.png)

### RTCP Capture

Enable capture of RTCP reports to build QoS Reports (found under Debugging > SIP Call Flow Tool). By default it's not enabled, clicked the "yes" radio button to enable it.

### Call Cost Webhook Event

Specify if the call cost webhook should be sent. By default it's not enabled, clicked the "yes" radio button to enable it.   
​

![](_images/a93d9efb8a5a9d41.png)

---

## Inbound Settings

You can configure your global application settings for inbound calls over here.

![](_images/143a02149a8d36ff.png)

### Subdomain

Specify a **subdomain** that can be used to receive calls to a Connection, in the same way a phone number is used, from a SIP endpoint.

* Example: the subdomain "**example**.sip.telnyx.com" can be called from any SIP endpoint by using the SIP URI "sip:@**example**.sip.telnyx.com" where the user part can be any alphanumeric value.
* You only need to specify the subdomain in this field, there is no need to specify a Telnyx domain after it.
* **SIP subdomain receive settings**: In this field, either you setup your receive SIP subdomain connection from anyone or only connections.

### Inbound Channel Limit

You can limit the total number of inbound calls to phone numbers associated with this connection.

### Enable Shaken Stir headers

By default, the radio button for no is checked. Select yes and save your settings if you want receive attestation information in the webhooks for incoming calls.

### Codecs

Select the codes using the check mark boxes that you would like Telnyx to offer on your calls. You can force specific codecs by only checking one of the boxes.

---

## Outbound settings

You can configure your global application settings for outbound calls over here.

![](_images/f094dd99bd8f8444.png)

### Outbound Voice Profile

Assign your application to an outbound voice profile in order to make outbound calls.

### Outbound Channel Limit

You can limit the total number of outbound calls to phone numbers associated with this connection.

---

## Where can I find my Call Control application or app id?

Once you've successfully created your Call Control application, it is given an application id that can be seen within the application settings as seen in the below picture.

## AnchorSite® Selection

"Latency" directs Telnyx to route media through the site with the lowest round-trip time to the user's connection. Telnyx calculates this time using ICMP ping messages. This can be disabled by specifying a site to handle all media.

![](_images/1be16068b0154fdf.png)

## Why do I need an Call Control application or app id?

The application id is used to reference or trigger your API calls programmatically. Don't forget to reference our [developer documentation](https://developers.telnyx.com/api-reference/call-commands/dial) to see how you can control your calls with the different API commands available.

---

## TeXML Applications

![](_images/16e69884aa0e248c.png)

## TeXML App Name

Click on " Create TeXML App" and assign a name to this application to better manage the application.  
​

![](_images/ba50715e7c7d6c43.png)

### Voice Method

In this field, HTTP request method Telnyx will use to interact with your XML Translator webhooks. Either "GET" or "POST".

![](_images/c5de0069fc878d8e.png)

### Send a TeXML webhook to the URL

You will need to mention a URL where all the XML translator webhook events will be sent. Also, you can setup a fail-over URL. This URL to which Telnyx will deliver your XML Translator webhooks if we get an error response from your "Voice URL"

![](_images/a78a40bcea5c49d9.png)

### Status Callback Method

You will need to mention the HTTP request method Telnyx should use when requesting the "Status Callback" URL.

![](_images/6922f946a8586eb6.png)

### Send information about call progress events to the URL

Specify the URL for Telnyx to send requests to containing information about call progress events.

![](_images/bd849862ceade845.png)

### Enable "hang-up" on timeout

When enabled, you will specify the numbers of seconds to wait for actual application before hanging up.

![](_images/4fcd66fccebbcdf3.png)

**DTMF Type**

There are three types in this field: RFC 2833, Inband and SIP INFO.

1. **RFC 2833**: Default and preferred setting for most use cases, not audible on the call audio.
2. **Inband**: Digits are passed along just like the rest of your voice as normal audio tones.
3. **SIP INFO**: Mainly used for SIP to SIP calls. [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf) type is negotiated between parties on the call.

![](_images/630fa1f351e4622b.png)

### Call Cost Webhook Event

Specify if the call cost webhook should be sent. By default it's not enabled, clicked the "yes" radio button to enable it.   
​

![](_images/e509c2fc6109e61d.png)

---

## Inbound Settings

You can configure your global application settings for inbound calls over here.

![](_images/ff946b3f3b31840d.png)

### Subdomain

Specify a **subdomain** that can be used to receive calls to a Connection, in the same way a phone number is used, from a SIP endpoint.

* Example: the subdomain "**example**.sip.telnyx.com" can be called from any SIP endpoint by using the SIP URI "sip:@**example**.sip.telnyx.com" where the user part can be any alphanumeric value.
* You only need to specify the subdomain in this field, there is no need to specify a Telnyx domain after it.
* **SIP subdomain receive settings**: In this field, either you setup your receive SIP subdomain connection from anyone or only connections.

### Inbound Channel Limit

You can limit the total number of inbound calls to phone numbers associated with this connection.

### Enable Shaken Stir headers

By default, the radio button for no is checked. Select yes and save your settings if you want receive attestation information in the webhooks for incoming calls.

## Codecs

Select the codes using the check mark boxes that you would like Telnyx to offer on your calls. You can force specific codecs by only checking one of the boxes.

---

## Outbound settings

You can configure your global application settings for outbound calls over here.

![Outbound settings page.](_images/c8148dc2d1816793.png)

### Outbound Voice Profile

Assign your application to an outbound voice profile in order to make outbound calls.

### Outbound Channel Limit

You can limit the total number of outbound calls to phone numbers associated with this connection.

![](_images/6cd943ee05a494a0.png)

---

## Where can I find my TeXML application or app ID?

Once you've successfully created your TeXML application, it is given an application id that can be seen within the application settings as seen in the below picture.

![](_images/c2578ae6f15a3f64.png)

## Why do I need an TeXML application or app ID?

The application id is used to reference or trigger your API calls programmatically. Don't forget to reference our [developer documentation](https://developers.telnyx.com/docs/development/programmable-voice/texml-setup) to see how you can setup your XML instructions.

![Breaking Line](_images/682991ade0be9812.png)

---

Related Articles

[What is DTMF? and how to configure it on Telnyx](https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx)[Telnyx Debugging Tools](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[TeXML and Telnyx Voice API compatibility](https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility)[TeXML Bin Simple Voicemail and Call Forwarding](https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding)

Did this answer your question?

😞😐😃

Table of contents
