---
title: SIP Connections
summary: A consolidated reference for configuring Telnyx SIP Connections in the Mission
  Control Portal, covering connection types (Credentials, IP, FQDN, UAC), authentication
  and routing, inbound and outbound settings, number formats, SIP URI calling, AnchorSite®
  media anchoring, webhooks, advanced options, and DID assignment.
sources:
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
updated_at: 2026-08-05T13:31:54Z
---

# SIP Connections

*Part 4 of 5 — see also: [Part 1](sip-connections--part-1.md), [Part 2](sip-connections--part-2.md), [Part 3](sip-connections--part-3.md), [Part 5](sip-connections--part-5.md)*

A consolidated reference for configuring Telnyx SIP Connections in the Mission Control Portal, covering connection types (Credentials, IP, FQDN, UAC), authentication and routing, inbound and outbound settings, number formats, SIP URI calling, AnchorSite® media anchoring, webhooks, advanced options, and DID assignment.

## SIP URI Calling

SIP URI Calling allows you to receive inbound calls directly to your SIP URI on connections using credential authentication. When enabled, callers can reach you by dialing your connection's username, removing the need for a phone number. To use this feature, you need a SIP device or softphone registered with the credentials set on the connection. SIP URI calling is disabled by default and can be enabled per connection.

To enable SIP URI Calling:

1. From the Telnyx portal, navigate to **Voice Suite → SIP Trunking**.
2. From the **SIP Connections** list, click the **edit** icon next to the connection you want to configure.
3. Open the **Authentication and routing** tab.
4. Under **Receive SIP URI calls**, select your preferred option from the dropdown (e.g., *From anyone* or *Only from my Connections*).

This setting was previously located under the **Inbound** tab but has since moved to **Authentication and routing**.

### Choosing Who Can Call Your SIP URI

- **From Anyone (unrestricted)** — allows calls from other Telnyx accounts and anyone on the public internet. Anyone who knows your SIP URI (`your-username@sip.telnyx.com`) can reach your SIP endpoint.
- **Only from my SIP Connections (internal)** — restricts inbound calls to those originating from connections on the same Telnyx account.

This setting can also be configured via the Telnyx API:

```
PUT https://api.telnyx.com/security/connections/{connection_id}
```

Set the `sip_uri_calling_preference` field to one of: `"disabled"`, `"unrestricted"`, or `"internal"`.

### Billing for SIP URI Calls

- SIP URI calls are billed at **$0.002 per minute**, charged to the owner of the connection that receives the call. This rate applies to any call originating from a source that Telnyx cannot identify.
- If the source matches a Telnyx SIP Connection, the call is treated as an **On-Net call** and billed according to your Telnyx rate deck.
- As a fraud-prevention measure against number spoofing, only SIP usernames beginning with a **non-numeric character** are considered valid.

## Webhooks

The webhook settings allow you to send all connection events to a webhook of your choice. If Telnyx fails to receive a 200 response when delivering the webhook event to your **Webhook URL**, it will attempt to send the event to your **Failover URL**.

There are 5 different events that can be sent:

- Call Initiated
- Call Answered
- Call Bridged
- Call Hangup
- Call Voicemail Completed

You will need to make sure that you use a voice API application to control the calls programmatically. A common misconception occurs when customers have a SIP Connection associated with a number that has a webhook URL set at the SIP Connection. They receive an inbound call and then attempt to issue the answer command with the call control ID from the webhook events, which results in the API error "Can not issue an answer command on an outbound call." Commands can only be triggered with the Voice API when a voice API application is associated with the numbers receiving the calls.

Some customers set the webhook URL on the SIP Connection because it's a public endpoint integrated with their PBX, which responds over SIP. Another typical use case relies on the **Park Outbound Calls** feature.

**Important:** When setting a webhook URL, it treats the call type as programmable and not SIP trunking. There is a limitation with this setup if you are using it only for notification purposes and not to programmatically control the call — the audio of your calls may be anchored in a media server (AnchorSite) further away than intended because that region does not support programmable voice services yet (e.g., Australia). In such circumstances, remove the webhook URL from the SIP Connection settings.

### Park Outbound Calls

The **Park Outbound Calls** feature provides a simple mechanism to "park" outbound calls instead of connecting them to their destination. The call then awaits further orders from its connected voice API application. In the meantime, Telnyx generates a **SIP 180 Ringing** message to instruct the client to generate local ringback.

Be careful enabling this setting if you are not using a voice API application to control the calls. Parked calls provide ring-back to the caller, waiting for a command via the Telnyx Voice API to define the call action. Typical commands include answer, play audio, bridge to another call, and transfer to another number.

The typical use case for enabling this feature on a SIP Connection with a webhook URL is where you have a voice API application that shares the same webhook URL as the SIP Connection, where the SIP Connection uses credentials authentication, where callers typically use a WebRTC client to register with the Telnyx WebRTC gateway (`rtc.telnyx.com`) using the connection's credentials, and where the events are posted to the webhook URL — which is essentially your voice API application backend webhook URL.

There are currently 3 webhook API versions you can specify:

- **API V1** — no longer recommended and less maintained.
- **API V2** — recommended and maintained; receives callback webhook events from the Voice API as JSON payloads over HTTP.
- **TeXML** — when set with Park Outbound Calls, Telnyx creates a parked leg for your call and fetches XML instructions from the webhook URL; the callback content-type is sent as **form-data** over HTTP.

## AnchorSite®

The **AnchorSite®** setting allows you to select the media server Telnyx uses to route your call's media packets. It can be found in the settings of your connections/applications.

No matter which AnchorSite® option you choose (latency or a specific site), should an issue arise Telnyx will always be able to re-route calls to the next closest AnchorSite®.

### Latency

When **Latency** is selected, Telnyx chooses the optimal Point of Presence (PoP) to route your call to ensure your media packets get off the internet as fast as possible. Telnyx regularly and proactively pings your Connection or Device using ICMP ping messages to calculate round trip timings from all Telnyx available sites. The site with the lowest latency is chosen as the AnchorSite®.

### Selecting the AnchorSite® Yourself

If you prefer not to receive pings from Telnyx and want to manually anchor your calls in the PoP you feel is best, select one of the available PoPs. This is recommended especially when your media IP address is not located in the same area as the signaling. There are limitations if you do not whitelist all Telnyx media IP addresses — in the rare event of unplanned maintenance or an outage at the selected AnchorSite®, media traffic will be re-routed through the next closest available site.

**Latency** is the default setting for AnchorSite® when SIP Connections are created.

### Special Notes

There are limitations to selecting **latency** depending on your SIP Connection's authentication type:

- For **IP-based or FQDN-based** authentication, if Telnyx cannot determine round trip times to your IP addresses, your calls may be anchored on a media server further away than is optimal. Make sure to whitelist Telnyx's media IP addresses on your firewall.
- For **credential-based** SIP Connections, include the SIP Connection's **username** in the contact header in your **first** SIP INVITE. This allows the SIP Proxy to identify the settings associated with your SIP Connection and ensure the AnchorSite® selected is chosen. If the username is not included in the first SIP INVITE attempt, there is no way to identify the optimal media server. Alternatively, include a new header in the first SIP INVITE: `X-Telnyx-Username: <username>`.
- For **applications**, the IP address associated with your webhook URL is used to determine which site has the lowest latency reaching you.
