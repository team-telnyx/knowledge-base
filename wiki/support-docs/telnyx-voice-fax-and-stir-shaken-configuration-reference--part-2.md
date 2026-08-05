---
title: Telnyx Voice, Fax, and STIR/SHAKEN Configuration Reference
summary: A consolidated reference covering Cisco SPA112/122 ATA setup with Telnyx,
  fax service configuration via T.38 or G711, Fax API error codes, STUN/TURN server
  usage, STIR/SHAKEN attestation and verstat parameters, the Robocall Mitigation Database,
  and Noise Suppression configuration for SIP trunks.
sources:
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
- url: https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-08-05T13:30:57Z
---

# Telnyx Voice, Fax, and STIR/SHAKEN Configuration Reference

*Part 2 of 3 — see also: [Part 1](telnyx-voice-fax-and-stir-shaken-configuration-reference--part-1.md), [Part 3](telnyx-voice-fax-and-stir-shaken-configuration-reference--part-3.md)*

A consolidated reference covering Cisco SPA112/122 ATA setup with Telnyx, fax service configuration via T.38 or G711, Fax API error codes, STUN/TURN server usage, STIR/SHAKEN attestation and verstat parameters, the Robocall Mitigation Database, and Noise Suppression configuration for SIP trunks.

## Fax API Error List

### Webhook Payload Errors

Outbound errors appear in the `failure_reason` field of Fax API webhook events.

| Error | Description |
| --- | --- |
| `file_size_limit_exceeded` | PDF exceeds the size limit (e.g., 50MB). |
| `page_count_limit_limit_exceeded` | PDF exceeds the page limit (e.g., 350 pages). |
| `fax_initial_communication_timeout` | Call did not connect to a valid fax machine or no fax tones were sent. |
| `fax_signaling_error` | Telephony engine error such as no response after a page, bad DCS response, or training failure. |
| `file_download_failed` | PDF could not be downloaded; only 2XX HTTP responses are accepted (no 3XX redirects). |
| `file_format_invalid` | File is not a valid PDF. |
| `receiver_call_dropped` | Call dropped prematurely. |
| `receiver_communication_error` | General call failure or telephony routing error. |
| `receiver_decline` | Destination declined the call. |
| `receiver_invalid_number_format` | Destination number is not in valid +E.164 format. |
| `receiver_no_response` | Called party did not respond within the allotted time. |
| `receiver_recovery_on_timer_expire` | Remote party sent SIP 408 or downstream carrier issue. |
| `receiver_unallocated_number` | Number is in valid format but not currently allocated. |
| `service_unavailable` | Internal Telnyx error initiating the call or retrieving the PDF. |
| `success` | Reported as a failure reason; Telnyx investigates. |

Inbound errors include `carrier_lost`, `fax_signaling_error`, `received`, `sender_call_dropped`, `sender_canceled`, and `sender_communication_error`.

Other webhook fax errors include `account_disabled`, `connection_channel_limit_exceeded`, `destination_invalid`, `destination_not_in_countries_whitelist`, `destination_not_in_service_plan`, `destination_unreachable`, `invalid_ecm_response_from_receiver`, `no_outbound_profile`, `outbound_profile_channel_limit_exceeded`, `outbound_profile_daily_spend_limit_exceeded`, `receiver_incompatible_destination`, `receiver_no_answer`, `user_busy`, `user_channel_limit_exceeded`, and `fax_initial_communication_timeout`.

Retries for failed outbound faxes must be configured in the client application; Telnyx does not auto-retry.

### Fax API CDR Result Codes

These codes appear in the last two columns of the CSV generated from the portal's Reporting section when **Report Type** is set to **Fax API**.

| Code | Message |
| --- | --- |
| 0 | OK |
| 2 | Timed out waiting for initial communication |
| 3 | Timed out waiting for the first message |
| 5 | The HDLC carrier did not stop in a timely manner |
| 6 | Failed to train with any of the compatible modems |
| 13 | Unexpected message received |
| 14 | Received bad response to DCS or training |
| 15 | Received a DCN from remote after sending a page |
| 17 | Received a DCN while waiting for a DIS |
| 20 | Received no response to DCS or TCF |
| 23 | Invalid ECM response received from transmitter |
| 31 | Timer T2 expired while waiting for fax page |
| 32 | Timer T2 expired while waiting for next fax page |
| 48 | Disconnected after permitted retries |
| 49 | The call dropped prematurely |

## STIR/SHAKEN with Telnyx

STIR/SHAKEN (Secure Telephony Identity Revisited / Secure Handling of Asserted information using toKENs) is an FCC-mandated framework to reduce fraudulent and robocalls over IP networks. It was implemented on June 30, 2021. Starting June 30, 2022, small service providers are expected to sign their own outbound calls; Telnyx continues to sign calls it receives that are unsigned but is not responsible for customer FCC compliance.

Originating service providers assign an attestation level and a token in the SIP INVITE header; the terminating provider validates the signature before connecting the call.

### Attestation Levels

- **Full Attestation (A):** The provider knows the customer, knows they have the right to use the originating number, and that the call originated on their network. Numbers purchased in the Telnyx portal typically receive A attestation.
- **Partial Attestation (B):** The provider knows the customer but may not know the number they are using. Numbers not bought on the Telnyx portal typically receive B attestation.
- **Gateway Attestation (C):** The origination provider cannot verify the customer or the phone number.
- **Unavailable:** The origination provider did not add the necessary information, or the call hit the PSTN and the token was lost.
- **Invalid:** The origination provider did not properly authenticate the customer or number, and Telnyx could not verify the token.

Attestation values are available in CSV files from the [reporting section](https://portal.telnyx.com/#/reporting/detailed-records) in Mission Control.

### Customer Impact

Telnyx is fully STIR/SHAKEN compliant and approved by the STI-PA. All calls originating on the Telnyx network receive attestation with no customer action required and no additional charge. Inbound calls with A attestation and a valid token include the `verstat` parameter in P-Asserted-Identity headers.

To increase the chance of receiving A attestation, port numbers to Telnyx using [Fastport](https://telnyx.com/products/number-porting).

### Signing Your Own Calls

Customers eligible to sign their own calls can do so and Telnyx will pass the certificate to the terminating provider. Requirements include:

1. Approval by the [Secure Telephone Identity Policy Administrator (STI-PA)](https://authenticate.iconectiv.com/), vetted by the [STI-GA](https://sti-ga.atis.org/).
2. A 499A Telecommunications Reporting Worksheet on file with the FCC.
3. An Operating Company Number (OCN).
4. A robocall mitigation plan filed with the FCC.
5. Valid certificates from an approved Certificate Authority.
6. An implemented SHAKEN/STIR solution on the network.

### On-Net Calling

To receive identity headers on on-net calls between Telnyx customers, register credentials connections via TCP, or specify TCP as the inbound transport protocol for IP/FQDN connections. UDP is not supported because the Identity header is large and would cause packet fragmentation.

## Canadian STIR/SHAKEN

No customer action is required for Canadian STIR/SHAKEN compliance; Telnyx's Canadian partners sign outbound calls with Canadian CLI.

Attestation definitions match the US framework:

- **A:** Customer has the right to use the Canadian number (purchased from Telnyx or ported in).
- **B:** Customer is known but using another provider's number.
- **C:** Customer and number cannot be verified.

There is no additional charge for SHAKEN/STIR services. Customers are not directly notified of the attestation level received but can predict it based on whether their Canadian CLI is listed in Mission Control.

## SHAKEN/STIR verstat Parameters

Telnyx has expanded the `verstat` parameter in the P-Asserted-Identity SIP header to provide more granular attestation information for inbound and on-net calls.

| Verstat value | Description |
| --- | --- |
| `TN-Validation-Passed` | Identity header verification successful; A attestation. |
| `TN-Validation-Failed` | Certificate received was deemed invalid. |
| `No-TN-Validation` | No verification took place; Identity header not provided. |
| `TN-Validation-Passed-B` | Identity header verification successful; B attestation. |
| `TN-Validation-Passed-C` | Identity header verification successful; C attestation. |

Example header:

```
P-Asserted-Identity:"John Doe"<sip:+18889809750@sip.telnyx.com;verstat=TN-Validation-Passed>
```

For the identity header to be passed on the B leg, both `shaken_stir_enabled` must be `true` (from CPB connection settings) and `cpb_transport_protocol` must be `TCP` or `TLS`. Identity headers are not sent over UDP to prevent fragmentation.
