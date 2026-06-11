---
title: Telnyx Portal Tools and Network Specifications
summary: A comprehensive guide to Telnyx's Mission Control Portal features including
  debugging tools, reporting, dashboards, and network specifications, as well as the
  status page for incident monitoring.
sources:
- url: https://support.telnyx.com/en/articles/1130599-telnyx-tech-specs
  content_hash: a7909fd9da64db0f973d0c0fd07d8a5b5b2365631813eccf5fbd43753fbcbc9f
- url: https://support.telnyx.com/en/articles/1130708-how-to-download-reports-at-telnyx
  content_hash: 0b3728a9ae0a1f2caf3012c645fb1d9843c2a91f96d795fca3483e82421b7fb8
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
  content_hash: 341002e45148401d2a67a440822b905946718a96fcdce6e8cbce5d54f0914fa3
- url: https://support.telnyx.com/en/articles/4305547-reporting-overview
  content_hash: 9fc160f8e420916d6634d100ddbeb777bdee708fb9bacaad7fb44b384e131be1
- url: https://support.telnyx.com/en/articles/4307059-telnyx-dashboards
  content_hash: e32513a252b1b8f3385424a74a449d2f6b1ee2a33766af144f26a19aac41c05c
- url: https://support.telnyx.com/en/articles/4424926-reporting-detail-requests
  content_hash: 3cdc92b1d0fcaf6c64cb28d6fbdab55332e1e61d8dcd9c50a4a046663a2dc441
- url: https://support.telnyx.com/en/articles/4425016-reporting-usage-reports
  content_hash: aa982f42ee65f0f2bed27901d3c4bc26ad9dbe60c3cfa15a10e32de89b87cc48
- url: https://support.telnyx.com/en/articles/4425088-reporting-monthly-charges
  content_hash: dc72e18b229c4623f5f799236dcd09b145ca7b931283b80cefabda858af78ec0
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
  content_hash: 29d42e44a7140e0a0b1bb3bdabee96aecb26165edf4dcc6ee5d783d62385fa0b
updated_at: 2026-06-11T11:42:46Z
---

# Telnyx Portal Tools and Network Specifications

*Part 1 of 2 — see also: [Part 2](telnyx-portal-tools-and-network-specifications--part-2.md)*

A comprehensive guide to Telnyx's Mission Control Portal features including debugging tools, reporting, dashboards, and network specifications, as well as the status page for incident monitoring.

## Network Points of Presence and Partners

Telnyx maintains several points of presence around the globe. For the latest and most authoritative information on telephony and network specifications, refer to these SIP endpoints:

- [sip.telnyx.com](https://sip.telnyx.com/) (US)
- [sip.telnyx.ca](https://sip.telnyx.ca/) (Canada)
- [sip.telnyx.eu](https://sip.telnyx.eu/) (Europe)
- [sip.telnyx.com.au](https://sip.telnyx.com.au/) (Australia)

**North America partners:** AT&T, Verizon, CenturyLink, Level 3 Communications, Comcast, Inteliquent, West Communications, Windstream, Earthlink, Peerless, Irsitel, Bandwidth.

**International partners:** AT&T, Verizon, CenturyLink, Level 3 Communications, Comcast, Inteliquent, Tata Communications, British Telecom, Telefonica, IDT.

## Interoperability

Telnyx supports interoperability with a wide range of platforms and PBX systems. Configuration guides are available in the [Telnyx configuration guides collection](https://support.telnyx.com/en/collections/133118-configuration-guides). Supported platforms include: 3CX, Adtran, AudioCodes, Asterisk, Avaya, Broadsoft, Cisco CallManager, Counterpath, Edgewater Networks, Elastix, Fonality, FreePBX, FreeSWITCH, Grandstream, IAUG, Mitel, Patton, PBX in a Flash, Switchvox, Thirdlane, Vicidial, Yealink, and [Zoiper Communicator](zoiper-communicator.md).

## Debugging Tools

The Debugging section of the Mission Control Portal contains several tools for debugging SIP calls and Call Control flows. It is accessible from the left-hand navigation and includes six sub-sections.

### SIP Call Flow Tool

The [SIP Call Flow Tool](https://portal.telnyx.com/#/debugging/sip-call-flow-tool) lets you search for calls by specifying a date range (up to 3 days back), calling number, and/or destination number. Additional filters include:

- **Billed duration** — filter by calls with billed duration greater than, equal to, or less than a specified value
- **Direction** — filter inbound or outbound calls
- **Tags** — filter by calls from/to numbers with a specific tag
- **Result code** — filter based on the SIP response code

Search results display a visual call flow diagram. For more on SIP response codes, see [Telnyx SIP Response Codes](telnyx-sip-response-codes.md).

### Programmatic Voice Call Flow Tool

The [Prog. Voice Call Flow Tool](https://portal.telnyx.com/#/debugging/call-control-texml-and-fax) is used to view Call Control, TeXML, or Fax API flows by supplying a Call Session ID. Clicking a result opens the Call Inspector, which illustrates the call flow. A clickable drop-down beside each call event opens its associated webhook payload.

### Web Dialer

The [Web Dialer](https://portal.telnyx.com/#/voice/web-dialer) allows you to make and receive test calls directly from the browser without setting up a softphone or PBX. This is useful for isolating whether issues stem from your PBX or softphone client.

**Prerequisites:** A Credentials Connection, a DID number assigned to that connection, and optionally a Caller ID name value.

You can also receive inbound calls on the Web Dialer by dialing the DID assigned to the SIP Connection configured above. If you encounter a websocket response of `done (CALL_REJECTED)`, check the specific rejection message; see [Telnyx SIP Response Codes](telnyx-sip-response-codes.md) for a list of error responses and resolutions.

### Webhook Deliveries

The Webhook Deliveries tool shows a history of webhooks sent over your account. You can search by webhook delivery ID, or filter by time, status, and webhook name (e.g., `call.initiated`). Use this tool to:

- Locate and analyze specific webhooks by ID
- Verify webhook delivery and contents
- Analyze all webhooks in a timeframe or containing a text string to find anomalies
- Analyze all webhooks with "failed" status
- View logs alongside conversation transcripts and insights

The tool includes message content and metadata for each delivery. **Troubleshooting tips:**

- Ensure your endpoint is correctly configured to receive webhook payloads
- Use filtering options to quickly identify failed deliveries
- Inspect payload contents to verify the data matches expectations
- Check for anomalies or errors indicating issues with your webhook setup

### Quality of Service (QoS) Reports

> **Note:** RTCP Capture must be enabled on your SIP Connection settings to use QoS Reports.

QoS Reports provide a visual representation of call quality on a timeline with two graphics — one for each RTP media stream established during a call. Access them through the SIP Call Flow Tool by searching for a call, clicking the blue "Call Data Debugging" button, and selecting the "QoS" tab.

When a call is established, media flows over two RTP streams (one in each direction). Each side periodically sends [RTCP reports](https://en.wikipedia.org/wiki/RTP_Control_Protocol) containing transmission and reception statistics. The QoS report uses this RTCP data to display four quality metrics per stream:

- **MOS (Mean Opinion Score)** — Scale of 1 (Bad) to 4.5 (Excellent), based on network metrics only. Audio issues from other sources are not captured.
- **IA Jitter** — The [Interarrival Jitter](https://en.wikipedia.org/wiki/Jitter) value as measured by the reporter.
- **Packets Lost** — The accumulated number of RTP packets perceived as lost by the reporter.
- **Packets** — The accumulated number of RTP packets sent by the reporter.
