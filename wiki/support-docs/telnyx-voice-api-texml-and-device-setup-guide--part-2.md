---
title: Telnyx Voice API, TeXML, and Device Setup Guide
summary: A consolidated reference covering Telnyx account basics, Voice API and TeXML
  application configuration, debugging tools, conference calling, and step-by-step
  setup instructions for several SIP desk and conference phones.
sources:
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
- url: https://support.telnyx.com/en/articles/5807663-panasonic-kx-tgp-550
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
updated_at: 2026-08-05T13:29:28Z
---

# Telnyx Voice API, TeXML, and Device Setup Guide

*Part 2 of 3 — see also: [Part 1](telnyx-voice-api-texml-and-device-setup-guide--part-1.md), [Part 3](telnyx-voice-api-texml-and-device-setup-guide--part-3.md)*

A consolidated reference covering Telnyx account basics, Voice API and TeXML application configuration, debugging tools, conference calling, and step-by-step setup instructions for several SIP desk and conference phones.

## Debugging Tools

The Debugging section of the Mission Control Portal contains tools for debugging SIP calls and call control flows. It includes six areas: SIP Call Flow Tool, Programmable Voice Call Flow Tool, Web Dialer, Detail Record Search, Webhook Deliveries, and Call Recordings.

### SIP Call Flow Tool

Specify a date range (up to 3 days back) and the calling and/or destination numbers. Additional filters include:

- **Billed duration:** Filter calls with a billed duration greater than, equal to, or less than the specified value.
- **Direction:** Filter inbound or outbound calls.
- **Tags:** Filter calls from/to numbers with a specific tag.
- **Result code:** Filter based on the SIP response code received.

![](_images/b70ffece80d76536.png)

An example call flow:

![](_images/4082b4fbf4c2673c.png)

### Programmable Voice Call Flow Tool

Use this simpler tool to view Call Control, TeXML, or Fax API flows by supplying the Call Session ID of the call in question.

![](_images/ee8af4e01b7a6147.png)

Clicking an example opens the Call Inspector, which illustrates the flow of the call. Each call event has a clickable drop-down that opens its associated webhook.

![](_images/164fbf8bb05945b1.png)

### Web Dialer

The Web Dialer lets you make test calls without setting up a softphone or PBX, which is useful for eliminating your PBX or softphone client as a source of issues. To use it, you need a Credentials Connection, a DID number assigned to that connection, and optionally a Caller ID name value. You can also receive inbound calls by dialing the DID number assigned to the SIP Connection.

![](_images/f7a6a2f9a46a9a27.png)

If you encounter a `CALL_REJECTED` websocket response, check the specific call rejection within the message. A list of error responses and resolutions is available in the SIP response codes article.

### Webhook Deliveries

This tool shows a history of webhooks sent over your account. Search by webhook delivery ID, or filter by time, status, and webhook name (for example, `call.initiated`). To view webhook deliveries or logs for your voice application:

1. Log in to the Telnyx portal.
2. Select the **Debugging** tab.

Use this tool to:

- Locate and analyze specific webhooks using their webhook ID.
- Verify the delivery of a webhook.
- Verify the contents of a webhook.
- Analyze all webhooks sent in a certain timeframe or containing a certain text string (for example, `call.initiated`) to find anomalies.
- Analyze all webhooks with "failed" status.
- View logs alongside conversation transcripts and insights.

![](_images/b2c31caf228406a0.png)

Tips for troubleshooting:

- Ensure your endpoint is correctly configured to receive webhook payloads.
- Use filtering options to quickly identify failed webhook deliveries.
- Inspect payload contents to verify the data sent matches expectations.
- Check for anomalies or errors in the logs that could indicate issues with your webhook setup.

![](_images/aed0951f46ab4289.png)

### QoS (Quality of Service) Reports

RTCP Capture must be enabled on your SIP Connection settings. QoS Reports provide a visual representation of call quality on a timeline with two graphics, one for each RTP media stream. Access them through the SIP Call Flow Tool by searching for your call, clicking the blue "Call Data Debugging" button, and selecting the "QoS" tab. Reports are based on RTCP reports sent between SIP devices and Telnyx.

![](_images/778c8cd64fe77a93.png)

When a call is established, media flows over two RTP streams (one in each direction). Each side periodically sends RTCP reports containing transmission and reception statistics, including packets sent, packets lost, and interarrival jitter.

![QoS Reporting Streams.](_images/398f0ddd246b99c9.png)

The QoS report displays four quality metrics on a timeline for each RTP stream:

- **MOS (Mean Opinion Score):** Based only on network metrics; other audio issues are not captured. Scale: 1 (Bad) to 4.5 (Excellent).

  ![MOS](_images/81e06d1f4de245f4.png)

- **IA Jitter:** The value of Interarrival Jitter as measured by the reporter.

  ![IA Jitter](_images/278a2da4e3b6c3d6.png)

- **Packets Lost:** The accumulated number of RTP packets perceived as lost by the reporter.

  ![Packets Lost](_images/25f22281799c8f62.png)

- **Packets:** The accumulated number of RTP packets sent by the reporter.

  ![Packets](_images/75f6d9583191cc07.png)
