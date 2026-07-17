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

*Part 2 of 6 — see also: [Part 1](telnyx-voice-features-and-configuration--part-1.md), [Part 3](telnyx-voice-features-and-configuration--part-3.md), [Part 4](telnyx-voice-features-and-configuration--part-4.md), [Part 5](telnyx-voice-features-and-configuration--part-5.md), [Part 6](telnyx-voice-features-and-configuration--part-6.md)*

This page consolidates Telnyx support documentation covering call forwarding, conference calls, TeXML Bin voicemail and call forwarding, sending and receiving SMS with the Python SDK, debugging tools, configuring Call Control/TeXML applications, voicemail setup, TeXML and Voice API compatibility, Android and iOS push notification setup, webhook CA errors, and Voice API essentials.

## Sending and Receiving SMS with the Python SDK

The Telnyx Python SDK can be used to send and receive text messages. Video walkthroughs are available for both directions:

- **Sending a text:** Follow the video walkthrough to learn how to use the Telnyx Python SDK to start sending text messages.
- **Receiving a text:** Watch the video walkthrough to learn how to use the Telnyx Python SDK to receive an inbound text message.

For all things Python + Telnyx, visit the [Developer Docs](https://developers.telnyx.com/).

## Telnyx Debugging Tools

The Debugging section of your Telnyx portal account contains several tools used for debugging SIP calls and call control flows. It can be found on the left-hand list of portal modules and contains six headers: SIP Call Flow Tool, Prog. Voice Call Flow Tool, Web Dialer, Detail Record Search, Webhook Deliveries, and Call Recordings.

### SIP Call Flow Tool

Using the SIP Call Flow Tool is straightforward. You can specify a date range that extends back 3 days maximum, and the calling and/or destination numbers.

Additional filters include:

- **Billed duration** — filter calls with a billed duration greater than, equal to, or less than the value you specify.
- **Direction** — filter inbound or outbound calls.
- **Tags** — filter by calls from/to numbers that have a specific tag.
- **Result code** — filter based on the SIP response code received for the calls.

![](_images/b70ffece80d76536.png)

More info on SIP response codes can be found in the SIP Trunking Methods/Requests/Responses article.

Below is a screenshot of an example call flow found using the Call Flow Tool.

![](_images/4082b4fbf4c2673c.png)

### Programmatic Voice Call Flow Tool

The Programmatic Voice Call Flow Tool is much simpler, and can be used to view Call Control, TeXML, or Fax API flows provided you can supply the Call Session ID of the call in question.

![](_images/ee8af4e01b7a6147.png)

By clicking on the example that appears once you hit Search, you can open up the Call Inspector which illustrates the flow of the call. There is also a clickable drop-down beside each call event that will open up its associated webhook.

![](_images/164fbf8bb05945b1.png)

### Web Dialer

The Web Dialer is a powerful debugging tool that allows you to make test calls without needing to set up a softphone or PBX system. This is useful if you are having issues with calls and want to eliminate your PBX or softphone client as a potential source of the issue. To use the Web Dialer, you need a Credentials Connection, a DID number assigned to that connection, and you can assign a Caller ID name value if you wish to test that as well. Once these prerequisites are met, you can make test calls straight from the web interface.

You can also receive incoming calls from the Web Dialer — useful for testing inbound failures. To receive an inbound call, simply dial the DID number assigned to the SIP Connection that you have entered in the steps above.

![](_images/f7a6a2f9a46a9a27.png)

If you come across a `CALL_REJECTED` websocket response, check the specific call rejection within the message. A list of error responses and their resolutions is available in the Telnyx SIP Response Codes article.

### Webhook Deliveries

This tool shows a history of webhooks sent over a customer's account. You can either search by webhook delivery ID, or filter according to time, status, and webhook name (e.g., `call.initiated`).

To view webhook deliveries or logs for your voice application:

1. Log in to the Telnyx portal.
2. Select the **Debugging** tab. Here, you can view webhook deliveries and troubleshoot any issues related to webhook functionality.

You can use this tool to assist with debugging cases:

- Locate and analyze specific webhooks using their webhook ID.
- Verify the delivery of a webhook.
- Verify the contents of a webhook.
- Analyze all webhooks sent in a certain timeframe or containing a certain text string (e.g., `call.initiated`) to find anomalies.
- Analyze all webhooks with "failed" status.
- View logs alongside conversation transcripts and insights to gain a comprehensive understanding of webhook activity.

![](_images/b2c31caf228406a0.png)

The message content and metadata are also included in the webhook delivery tool.

#### Tips for Troubleshooting

- Ensure that your endpoint is correctly configured to receive webhook payloads.
- Use the filtering options to quickly identify and analyze failed webhook deliveries.
- Inspect the payload contents to verify that the data sent matches your expectations.
- Check for any anomalies or errors in the logs that could indicate issues with your webhook setup.

![](_images/aed0951f46ab4289.png)

### QoS (Quality of Service) Reports

**NOTE:** The customer must have RTCP Capture enabled on their SIP Connection settings.

This feature provides customers with a visual representation of the Quality of Service (QoS) of any given call on a timeline with two separate graphics, one for each of the RTP media streams that are established for each call.

The QoS report feature is available in the Mission Control Portal through the SIP Call Flow Tool. Search for your call, click the blue "Call Data Debugging" button to the right of the sample, and click the "QoS" tab. Reports are based on RTCP reports that are sent between SIP devices and Telnyx.

![](_images/778c8cd64fe77a93.png)

When a call is established, media starts flowing over two RTP streams, one in each direction. Periodically, each side also sends RTCP reports to report transmission and reception statistics during the interval. Each report includes the number of packets sent, the accumulated packets that were expected but never received (`packets_lost`), the jitter perceived from the received packets (`ia_jitter`), and more.

![QoS Reporting Streams.](_images/398f0ddd246b99c9.png)

The QoS report feature uses the data on these RTCP reports to display 4 different quality metrics on a timeline for each RTP stream:

#### MOS (Mean Opinion Score)

The QoS report shows MOS stats based only on network metrics; any other audio issues won't be captured by it. The scale goes from 1 (Bad) to 4.5 (Excellent).

![MOS](_images/81e06d1f4de245f4.png)

*Mean Opinion Score*

#### IA Jitter

`IA_jitter` represents the value of Interarrival Jitter, as measured by the reporter.

![IA Jitter](_images/278a2da4e3b6c3d6.png)

*IA Jitter*

#### Packets Lost

`Packets Lost` represents the accumulated number of RTP packets perceived as lost by the reporter.

![A packets lost diagram.](_images/25f22281799c8f62.png)

*Packets Lost*

#### Packets

`Packets` represents the accumulated number of RTP packets that were sent by the reporter.

![A graph showing a packet of RTPs.](_images/75f6d9583191cc07.png)

*Packets*
