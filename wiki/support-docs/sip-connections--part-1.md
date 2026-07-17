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

*Part 1 of 4 — see also: [Part 2](sip-connections--part-2.md), [Part 3](sip-connections--part-3.md), [Part 4](sip-connections--part-4.md)*

This page covers Telnyx SIP Connections comprehensively, including connection types (credential, IP, FQDN, and Call Control authentication), telephony credentials (SIP Connection Credentials, On-Demand Credentials, and JSON Web Tokens), inbound and outbound settings (number formats, transport protocols, ringback, codecs, encryption, and timeouts), webhook configuration with Park Outbound Calls, AnchorSite® media anchoring, advanced settings (DTMF, T.38, comfort noise), RTCP settings, SIP URI Calling, Outbound Voice Profiles, concurrent outbound call limits, and the tagging feature for organizing services.

## Overview of SIP Connections

SIP Connections are the foundation of Telnyx's SIP trunking service, used for both inbound and outbound voice traffic. They can be assigned to DIDs to allow inbound calling and to [Outbound Voice Profiles](more-about-outbound-voice-profiles.md) for outbound calling. Each connection has a universally unique identifier (connection ID) used for API interactions, and connections can be distinguished by giving them unique names.

When pulling usage reports, you can select "By Connection" as your Aggregation Type to get a breakdown of inbound and outbound usage for each connection. Customer Detail Records (CDRs) can also be generated, with each record including the connection. CDRs can be filtered on SIP Connections, Record Type, Call Type, CLI (from number), CLD (to number), and Tags.

## SIP Connection Types

Telnyx offers four different authentication types for registering your switch:

- **Credential-based Authentication** — Used when you have a dynamic public IP address. A username and password are automatically generated (editable via the Authentication & Routing Configuration section). It is highly recommended to choose a strong password.
- **IP-based Authentication** — Used when you have a static IP address. You can add multiple IP addresses and select the order of preference, with two routing methods: Sequential and Round Robin.
- **FQDN-based Authentication** — Has separate inbound and outbound settings. You can assign multiple FQDN addresses on the inbound section and multiple IP addresses on the outbound section. Outbound calls authentication can use either Credentials or IP Address.
- **Call Control** — For setting up programmable voice connections/applications, configured in the programmable voice section of the Portal.

As a rule of thumb, use credential-based connections for dynamic public IPs and IP-based connections for static IPs.

### Creating a SIP Connection

To create a SIP Connection, click the "Create SIP Connection" button in the SIP Connections section of the Mission Control Portal. Enter a name, select the connection type, configure the relevant settings, and click next to save your details.

### Deactivating a SIP Connection

To deactivate or disable a SIP Connection, visit the SIP Connections page, select edit on the desired SIP Connection, and click the toggle under the "status" option. This will deactivate the SIP Connection, meaning inbound and outbound calls will not be processed.

## Telephony Credentials

Telnyx offers three Telephony Credential types for authenticating calls:

### SIP Connection Credentials

A one-stop authentication service for managing calls. The portal setup helps separate call traffic and allows easy integration with softphone clients such as Zoiper. A username and password are automatically generated when creating a credential-based SIP Connection.

### On-Demand Credentials

Created programmatically via the RESTful API. To create one:

1. Generate a V2 API key in the Keys & Credentials section under Account Settings.
2. Gather your Connection ID from your SIP Connection's settings.
3. POST to `https://api.telnyx.com/v2/telephony_credentials` with the connection_id and a name.

On-Demand Credentials are ideal for onboarding new customers or team members under your SIP connection, allowing you to separate each user with their own security credentials. This is perfect for integrating WebRTC into your own platforms. Inbound calls directly to on-demand generated credentials are not currently supported — they are intended purely for outbound calls.

### JSON Web Tokens (JWTs)

Created programmatically using the RESTful API and expire after 24 hours. To create a JWT, first generate an On-Demand Credential, then POST to `https://api.telnyx.com/v2/telephony_credentials/<credential_id>/token`. JWTs provide the same functionality as On-Demand Credentials with additional security thanks to the default expiry time, making them suitable for providing temporary access to onboarding users or guests.

## Authentication & Routing Configuration

For IP Auth SIP Connections, Telnyx offers three advanced authentication methods to further secure traffic:

- **Tech Prefix** — A 4-digit prefix that needs to be appended to the destination number.
- **Token** — A string that must be sent in a custom SIP header `X-Telnyx-Token` on the SIP INVITE message.
- **P Charge Info** — A telephone number associated with the connection must be sent in the `P-Charge-Info` SIP header on the SIP INVITE message.
