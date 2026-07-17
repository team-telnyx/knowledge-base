---
title: SIP Connections
summary: This page covers Telnyx SIP Connections comprehensively, including connection
  types (credential, IP, FQDN, and Call Control authentication), telephony credentials
  (SIP Connection Credentials, On-Demand Credentials, and JSON Web Tokens), inbound
  and outbound settings (number formats, transport protocols, ringback, codecs, encryption,
  and timeouts), webhook configuration with Park Outbound Calls, AnchorSite® media
  anchoring, advanced settings (DTMF, T.38, comfort noise), RTCP settings, SIP URI
  Calling, Outbound Voice Profiles, concurrent outbound call limits, and the tagging
  feature for organizing services.
sources:
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
updated_at: 2026-07-17T09:06:41Z
---

# SIP Connections

*Part 3 of 4 — see also: [Part 1](sip-connections--part-1.md), [Part 2](sip-connections--part-2.md), [Part 4](sip-connections--part-4.md)*

This page covers Telnyx SIP Connections comprehensively, including connection types (credential, IP, FQDN, and Call Control authentication), telephony credentials (SIP Connection Credentials, On-Demand Credentials, and JSON Web Tokens), inbound and outbound settings (number formats, transport protocols, ringback, codecs, encryption, and timeouts), webhook configuration with Park Outbound Calls, AnchorSite® media anchoring, advanced settings (DTMF, T.38, comfort noise), RTCP settings, SIP URI Calling, Outbound Voice Profiles, concurrent outbound call limits, and the tagging feature for organizing services.

## Webhooks

The webhook settings allow you to send all connection events to a webhook of your choice. If Telnyx fails to receive a 200 response when delivering the webhook event to your Webhook URL, it will attempt to send the event to your Failover URL.

There are 5 different events that can be sent:

- Call Initiated
- Call Answered
- Call Bridged
- Call Hangup
- Call Voicemail Completed

**Important:** When setting a webhook URL, it treats the call type as programmable and not SIP trunking. This is because Telnyx delivers programmable webhook events of the call state. There is a limitation with this setup if you are using it only for notification purposes and not to actually programmatically control the call — the audio of your calls may be anchored in a media server (anchorsite) further away than intended because that region does not support programmable voice services yet (e.g., Australia). In such circumstances, remove the webhook URL from the SIP Connection settings.

You will need to use a voice API application to control calls programmatically. A common misconception occurs when customers have a SIP Connection associated with a number that has a webhook URL set at the SIP Connection — they receive an inbound call and attempt to issue the answer command with the call control ID from the webhook events, resulting in the error "Can not issue an answer command on an outbound call." Commands can only be triggered with the Voice API when a voice API application is associated with the numbers receiving the calls.

### Park Outbound Calls

The Park Outbound Calls feature provides a mechanism to "park" outbound calls instead of connecting them to their destination. The call awaits further orders from its connected voice API application. In the meantime, Telnyx generates a SIP 180 Ringing message to instruct the client to generate local ringback.

**Be careful enabling this setting** if you are not using a voice API application to control the calls.

Parked calls provide ring-back to the caller, waiting for a command via the Telnyx Voice API to define the call action. Typical commands include answer, play audio, bridge to another call, and transfer to another number.

A typical use case is where you have a voice API application that shares the same webhook URL as the SIP Connection, the SIP Connection uses credentials as the authentication type, callers use a WebRTC client to register with the WebRTC gateway (rtc.telnyx.com) using the connection's credentials, and the backend issues a dial command to connect the caller with their destination.

### Webhook API Versions

There are currently 3 webhook API Versions:

- **API V1** — No longer recommended and less maintained.
- **API V2** — Recommended and maintained. Receives callback webhook events from the Voice API as JSON payloads over HTTP.
- **TeXML** — When set with Park Outbound Calls, Telnyx creates a parked leg for the call and fetches XML instructions from the webhook URL. Callback content-type is sent as form-data over HTTP.

## AnchorSite®

The AnchorSite® settings allow the user to select the media server in which calls are anchored. In most cases, the closer the server is geographically, the better the latency. This setting defaults to Latency if not modified.

When set to Latency, Telnyx proactively monitors latency from your endpoints to points of presence (PoP) to determine where media should be anchored. There are limitations depending on the authentication type — calls may be anchored on a media server further away if Telnyx is unable to identify latency between media servers and the IPs associated with the SIP Connection through ICMP requests. Make sure to whitelist Telnyx's media IP addresses on your firewall.

For credential-based SIP Connections, include the SIP Connection's username in the contact header in your first SIP INVITE. This allows the SIP Proxy to identify the settings associated with your SIP Connection and ensure the correct AnchorSite® is chosen.

## Advanced Settings

### Encode Contact Header

Encodes the SIP contact header sent by Telnyx to avoid issues with NAT and ALG scenarios.

### DTMF Types

Specifies the type of DTMF to be used on the call. Three options:

- **RFC 2833 (Recommended)** — Standards-based mechanism to send DTMF digits in-band (RTP).
- **Inband** — Sending of information within the same band or channel used for voice or video. Most prone to issues.
- **SIP Info** — Used by SIP network elements to transmit digits out-of-band as telephone-events.

### Enable On-Net T.38 Passthrough

Enable if you prefer the sender and receiver negotiating T.38 directly. If disabled, Telnyx will use T.38 on just one leg of the call depending on each leg's settings.

### Enable Comfort Noise for Call on Hold

When checked, Telnyx generates comfort noise when you place a call on hold. If unchecked, you will need to generate comfort noise or on-hold music to avoid RTP timeouts.

## RTCP Settings

RTP is used to transmit media between endpoints. RTCP packets are generated periodically by both parties to report statistics about the ongoing call. Telnyx provides the ability to use either RTCP+1 or RTCP mux at the connection level. Checking "RTCP Capture and Storage" enables the feature.

### Report Frequency

Specifies the interval in seconds between sending RTCP packets back to the user's media IP while the call is in progress.

### RTCP Port

Defaults to RTCP+1. The other option, RTCP mux, multiplexes both RTP and RTCP through a single UDP port, simplifying NAT traversal.

## SIP URI Calling

SIP URI Calling allows you to receive inbound calls directly to your SIP URI on connections using credential auth. When enabled, callers can reach you by dialing your connection's username, removing the need for a phone number. To use this feature, you need a SIP device or softphone registered with the credentials set on the connection. SIP URI calling is disabled by default and can be enabled per connection.

### Enabling SIP URI Calling

1. Navigate to **Voice Suite → SIP Trunking** in the Telnyx portal.
2. Click the edit icon next to the connection you want to configure.
3. Open the **Authentication and routing** tab.
4. Under **Receive SIP URI calls**, select your preferred option from the dropdown (e.g., *From anyone* or *Only from my Connections*).

**Note:** This setting was previously located under the Inbound tab but has since moved to Authentication and routing.

### Choosing Who Can Call Your SIP URI

- **From Anyone (unrestricted)** — Allows calls from other Telnyx accounts as well as anyone on the public internet. Anyone who knows your SIP URI (`your-username@sip.telnyx.com`) can reach your SIP endpoint.
- **Only from my SIP Connections (internal)** — Restricts inbound calls to those originating from connections on the same Telnyx account.

This setting can also be configured via the API:

```
PUT https://api.telnyx.com/security/connections/{connection_id}
```

Set the `sip_uri_calling_preference` field to one of: `"disabled"`, `"unrestricted"`, or `"internal"`.

### Billing for SIP URI Calls

- SIP URI calls are billed at **$0.002 per minute**, charged to the owner of the connection that receives the call. This rate applies to any call originating from a source that Telnyx cannot identify.
- If the source matches a Telnyx SIP Connection, the call is treated as an On-Net call and billed according to your Telnyx rate deck.
- As a fraud-prevention measure against number spoofing, only SIP usernames beginning with a non-numeric character are considered valid.
