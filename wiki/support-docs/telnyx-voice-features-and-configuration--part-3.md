---
title: Telnyx Voice Features and Configuration
summary: This page consolidates Telnyx support documentation covering call forwarding,
  conference calls, TeXML Bin voicemail and call forwarding, sending and receiving
  SMS with the Python SDK, debugging tools, configuring Call Control/TeXML applications,
  voicemail setup, TeXML and Voice API compatibility, Android and iOS push notification
  setup, webhook CA errors, and Voice API essentials.
sources:
- url: https://support.telnyx.com/en/articles/1130657-call-forwarding
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
- url: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
- url: https://support.telnyx.com/en/collections/5782829-webrtc-voice-sdk
updated_at: 2026-07-17T09:05:29Z
---

# Telnyx Voice Features and Configuration

*Part 3 of 6 — see also: [Part 1](telnyx-voice-features-and-configuration--part-1.md), [Part 2](telnyx-voice-features-and-configuration--part-2.md), [Part 4](telnyx-voice-features-and-configuration--part-4.md), [Part 5](telnyx-voice-features-and-configuration--part-5.md), [Part 6](telnyx-voice-features-and-configuration--part-6.md)*

This page consolidates Telnyx support documentation covering call forwarding, conference calls, TeXML Bin voicemail and call forwarding, sending and receiving SMS with the Python SDK, debugging tools, configuring Call Control/TeXML applications, voicemail setup, TeXML and Voice API compatibility, Android and iOS push notification setup, webhook CA errors, and Voice API essentials.

## Configuring Call Control / TeXML Applications

The Call Control / TeXML applications section is located on the left-hand side of the portal under Voice > Programmable Voice.

### Voice Applications (Call Control Voice API Application)

![](_images/fbd7eb7ada42f5e3.png)

#### Voice App Name

Click on "Create Voice App" and assign a name to this application to better manage the application.

#### AnchorSite® Selection

"Latency" directs Telnyx to route media through the site with the lowest round-trip time to the user's connection. Telnyx calculates this time using ICMP ping messages. This can be disabled by specifying a site to handle all media.

![](_images/23af2aee8a7dec57.png)

![](_images/a4aeb2e38966e6ec.png)

#### Send a Webhook to the URL

You will need to input a URL where all the webhook events will be sent. You can also set up a fail-over URL. If two consecutive delivery attempts to the primary URL fail, Telnyx will attempt delivery to this URL. **NOTE:** Must include a scheme such as `https`.

![](_images/1236f3a3ccd1779c.png)

#### Use Webhook API Version

Determines which webhook format will be used based on the API version V1 or V2. We recommend using API V2, as it contains a richer feature set versus the initial version which will be deprecated in the future.

![](_images/a43c14f22ec1c74c.png)

#### Enable "Hang-Up" on Timeout

When enabled, you will specify the number of seconds Telnyx will wait for commands from your application before hanging up.

![](_images/d433e78bdd04d8cc.png)

#### Custom Webhook Retry Delay (Seconds)

Specify a delay in seconds for Telnyx to wait before retrying an unsuccessful webhook delivery attempt. If not set, Telnyx will retry immediately.

![](_images/a8046b816610fc52.png)

#### DTMF Type

There are three types in this field: RFC 2833, Inband, and SIP INFO.

1. **RFC 2833:** Default and preferred setting for most use cases, not audible on the call audio.
2. **Inband:** Digits are passed along just like the rest of your voice as normal audio tones.
3. **SIP INFO:** Mainly used for SIP to SIP calls. DTMF type is negotiated between parties on the call.

![](_images/83448c867623f8d2.png)

#### RTCP Capture

Enable capture of RTCP reports to build QoS Reports (found under Debugging > SIP Call Flow Tool). By default it's not enabled; click the "yes" radio button to enable it.

#### Call Cost Webhook Event

Specify if the call cost webhook should be sent. By default it's not enabled; click the "yes" radio button to enable it.

![](_images/a93d9efb8a5a9d41.png)

### Inbound Settings

You can configure your global application settings for inbound calls here.

![](_images/143a02149a8d36ff.png)

#### Subdomain

Specify a **subdomain** that can be used to receive calls to a Connection, in the same way a phone number is used, from a SIP endpoint.

- Example: the subdomain `example.sip.telnyx.com` can be called from any SIP endpoint by using the SIP URI `sip:@example.sip.telnyx.com` where the user part can be any alphanumeric value.
- You only need to specify the subdomain in this field; there is no need to specify a Telnyx domain after it.
- **SIP subdomain receive settings:** In this field, either you set up your receive SIP subdomain connection from anyone or only connections.

#### Inbound Channel Limit

You can limit the total number of inbound calls to phone numbers associated with this connection.

#### Enable Shaken Stir Headers

By default, the radio button for no is checked. Select yes and save your settings if you want to receive attestation information in the webhooks for incoming calls.

#### Codecs

Select the codecs using the check mark boxes that you would like Telnyx to offer on your calls. You can force specific codecs by only checking one of the boxes.

### Outbound Settings

You can configure your global application settings for outbound calls here.

![](_images/f094dd99bd8f8444.png)

#### Outbound Voice Profile

Assign your application to an outbound voice profile in order to make outbound calls.

#### Outbound Channel Limit

You can limit the total number of outbound calls to phone numbers associated with this connection.

### Application ID

Once you've successfully created your Call Control application, it is given an application ID that can be seen within the application settings.

The application ID is used to reference or trigger your API calls programmatically. See the developer documentation to learn how to control your calls with the different API commands available.

### TeXML Applications

![](_images/16e69884aa0e248c.png)

#### TeXML App Name

Click on "Create TeXML App" and assign a name to this application to better manage the application.

![](_images/ba50715e7c7d6c43.png)

#### Voice Method

In this field, the HTTP request method Telnyx will use to interact with your XML Translator webhooks. Either "GET" or "POST".

![](_images/c5de0069fc878d8e.png)

#### Send a TeXML Webhook to the URL

You will need to mention a URL where all the XML translator webhook events will be sent. You can also set up a fail-over URL. This URL is where Telnyx will deliver your XML Translator webhooks if we get an error response from your "Voice URL".

![](_images/a78a40bcea5c49d9.png)

#### Status Callback Method

You will need to mention the HTTP request method Telnyx should use when requesting the "Status Callback" URL.

![](_images/6922f946a8586eb6.png)

#### Send Information About Call Progress Events to the URL

Specify the URL for Telnyx to send requests to containing information about call progress events.

![](_images/bd849862ceade845.png)

#### Enable "Hang-Up" on Timeout

When enabled, you will specify the number of seconds to wait for actual application before hanging up.

![](_images/4fcd66fccebbcdf3.png)

#### DTMF Type

There are three types in this field: RFC 2833, Inband, and SIP INFO.

1. **RFC 2833:** Default and preferred setting for most use cases, not audible on the call audio.
2. **Inband:** Digits are passed along just like the rest of your voice as normal audio tones.
3. **SIP INFO:** Mainly used for SIP to SIP calls. DTMF type is negotiated between parties on the call.

![](_images/630fa1f351e4622b.png)

#### Call Cost Webhook Event

Specify if the call cost webhook should be sent. By default it's not enabled; click the "yes" radio button to enable it.

![](_images/e509c2fc6109e61d.png)

### TeXML Inbound Settings

You can configure your global application settings for inbound calls here.

![](_images/ff946b3f3b31840d.png)

#### Subdomain

Specify a **subdomain** that can be used to receive calls to a Connection, in the same way a phone number is used, from a SIP endpoint.

- Example: the subdomain `example.sip.telnyx.com` can be called from any SIP endpoint by using the SIP URI `sip:@example.sip.telnyx.com` where the user part can be any alphanumeric value.
- You only need to specify the subdomain in this field; there is no need to specify a Telnyx domain after it.
- **SIP subdomain receive settings:** In this field, either you set up your receive SIP subdomain connection from anyone or only connections.

#### Inbound Channel Limit

You can limit the total number of inbound calls to phone numbers associated with this connection.

#### Enable Shaken Stir Headers

By default, the radio button for no is checked. Select yes and save your settings if you want to receive attestation information in the webhooks for incoming calls.

#### Codecs

Select the codecs using the check mark boxes that you would like Telnyx to offer on your calls. You can force specific codecs by only checking one of the boxes.

### TeXML Outbound Settings

You can configure your global application settings for outbound calls here.

![Outbound settings page.](_images/c8148dc2d1816793.png)

#### Outbound Voice Profile

Assign your application to an outbound voice profile in order to make outbound calls.

#### Outbound Channel Limit

You can limit the total number of outbound calls to phone numbers associated with this connection.

![](_images/6cd943ee05a494a0.png)

### TeXML Application ID

Once you've successfully created your TeXML application, it is given an application ID that can be seen within the application settings.

![](_images/c2578ae6f15a3f64.png)

The application ID is used to reference or trigger your API calls programmatically. See the developer documentation to learn how to set up your XML instructions.
