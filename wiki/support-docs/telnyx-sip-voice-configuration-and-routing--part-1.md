---
title: Telnyx SIP Voice Configuration and Routing
summary: This page consolidates Telnyx support guidance on SIP voice configuration,
  covering SRV record handling, call forwarding, external call transfers, SIP registration,
  post-dial delay, round-robin routing, and the role of Via and Record-Route headers
  in successful call setup.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1130657-call-forwarding
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
updated_at: 2026-08-05T13:25:14Z
---

# Telnyx SIP Voice Configuration and Routing

*Part 1 of 4 — see also: [Part 2](telnyx-sip-voice-configuration-and-routing--part-2.md), [Part 3](telnyx-sip-voice-configuration-and-routing--part-3.md), [Part 4](telnyx-sip-voice-configuration-and-routing--part-4.md)*

This page consolidates Telnyx support guidance on SIP voice configuration, covering SRV record handling, call forwarding, external call transfers, SIP registration, post-dial delay, round-robin routing, and the role of Via and Record-Route headers in successful call setup.

## SRV Records for SIP Calls

SRV (Service) records in DNS specify the location of servers for specific services. For SIP traffic, they enable distribution of SIP requests across multiple hosts, providing load balancing and failover. Telnyx honors SRV records in two scenarios: SIP FQDN Connections (where the FQDN indicates where to route inbound calls) and Voice API calls to external non-Telnyx domains.

When Telnyx routes a call to an external non-Telnyx FQDN, the behavior depends on whether a port is specified in the Request-URI (RURI), and Telnyx selects the appropriate SRV record based on the transport protocol used in the SIP request.

- **RURI with a port number** (e.g. `sip:+1234567890@sip.example.com:5060`): Telnyx performs an A-record lookup, bypassing the SRV record, and routes the call to the returned IP address.
- **RURI without a port number** (e.g. `sip:+1234567890@sip.example.com`): Telnyx performs an SRV-record lookup. If no SRV record exists, it falls back to an A-record lookup using the default SIP port (5060 for UDP/TCP or 5061 for TLS). If the first SRV target fails with a SIP 503 response, Telnyx attempts the next highest priority target in the SRV list.

To leverage SRV records, omit the port number from the `to` header. If an SRV record is not found and no A-record exists, the call fails with a `SIP 478 (Unresolvable Destination)` response. Ensure DNS records are globally resolvable and that SRV targets have resolvable A records.

For example, configuring `"to" => "sip:+1234567890@sip.example.com:5060"` results in an A-record lookup that fails because no A-record exists for `sip.example.com`. Removing the port to `"to":"sip:+1234567890@sip.example.com"` enables SRV lookup and correct routing.

## Call Forwarding

Call Forwarding is a per-number setting that can forward all calls or only calls that fail to reach the SIP Connection associated with the number. To enable it, click the handset icon under the services column for the number, scroll to the forwarding section in the voice sub-tab, toggle the setting on, and enter the destination number.

Two modes are available:

- **Always**: Bypasses the primary SIP connection entirely. All incoming calls are unconditionally forwarded to the designated number, regardless of whether the PBX is online, registered, or active.
- **On-Failure**: Triggered when the endpoint is unregistered (e.g. internet outage, power failure, or misconfiguration), when Do Not Disturb is active, or when the user manually declines the call. Unanswered calls that simply ring out are not considered failures and will not trigger forwarding.

Save changes and accept the monthly recurring charge (MRC) to activate. Toggle the setting off and save to disable.

Forwarding from a Telnyx number to another Telnyx number is treated as off-net and billed per the outbound rate deck, since the forwarded leg is sent outbound to the PSTN. The MRC does not waive per-minute charges for both the inbound and forwarded outbound legs; the only exception is when the receiving number uses channel billing instead of pay-per-minute. Call forwarding cannot be enabled on numbers assigned to voice or fax applications; only SIP Connections are supported. For numbers that must remain on a Call Control or TeXML application, forward programmatically — TeXML is the simplest by substituting `<NUMBER>` for `<SIP>` in the TeXML bin quickstart, or use the Voice API answer and transfer commands.

In some countries (such as Venezuela), local regulations require masking of calls originating from outside the country that display a local CLI. Telnyx may not be able to forward such calls.

## External Call Transfers

When a SIP endpoint receives an inbound call from the PSTN through Telnyx and transfers the caller to an external destination, the endpoint initiates a new outbound call. From Telnyx's perspective these are two different calls, and the transferred leg is considered an outbound call from a non-Telnyx number. Telnyx automatically allows and routes these outbound calls when it can verify they are tied to the original inbound call.

The flow is: caller A dials Telnyx number B, Telnyx delivers the call to the SIP endpoint, the endpoint decides to transfer to number C, and the endpoint places a new outbound call from A to C. For Telnyx to allow this, the outbound call must include proper diversion information indicating it is a transfer of the original inbound call from A to B.

Telnyx performs two validations on the outbound call attempt:

1. **Active inbound call match**: Telnyx confirms there is an active inbound call from A to B.
2. **Diversion header presence**: The new outbound call from A to C must include a SIP Diversion header showing B.

If the Diversion header is missing or incorrect, or Telnyx cannot match the outbound call to an active inbound call, Telnyx rejects the request by default with `403 Unverified origination number D51`, preventing unauthorized or spoofed calls.

Programmable Voice can also transfer an inbound call to an external PSTN number while preserving the non-Telnyx origination number:

- **Voice API Transfer command**: Instructs Telnyx to transfer an established inbound call to a new destination; the non-Telnyx origination number is allowed.
- **Voice API Dial + Bridge**: A Dial request triggers a new outbound call; if bridged to an existing inbound call, the non-Telnyx origination number is allowed. The Dial request must include `link_to` set to the `call_control_id` of the bridging call and `bridge_intent` set to `true`.
- **TeXML `<Dial>`**: Instructs Telnyx to place a new outbound call and connect it to the existing inbound call; the non-Telnyx origination number is allowed.
