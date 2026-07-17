---
title: Telnyx SIP, Fax, and PBX Configuration
summary: This page consolidates Telnyx support documentation covering fax service
  setup and error handling (T.38 and G.711), Programmable Fax API webhook and CDR
  error codes, FreeSWITCH and FusionPBX trunk configuration, SIP Trunking FIPS support,
  and the meaning of SIP 603+ carrier rejections.
sources:
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
- url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-07-17T09:05:45Z
---

# Telnyx SIP, Fax, and PBX Configuration

*Part 1 of 5 — see also: [Part 2](telnyx-sip-fax-and-pbx-configuration--part-2.md), [Part 3](telnyx-sip-fax-and-pbx-configuration--part-3.md), [Part 4](telnyx-sip-fax-and-pbx-configuration--part-4.md), [Part 5](telnyx-sip-fax-and-pbx-configuration--part-5.md)*

This page consolidates Telnyx support documentation covering fax service setup and error handling (T.38 and G.711), Programmable Fax API webhook and CDR error codes, FreeSWITCH and FusionPBX trunk configuration, SIP Trunking FIPS support, and the meaning of SIP 603+ carrier rejections.

## Fax Service with Telnyx (T.38 or G.711)

Setting up fax service on the Telnyx Mission Control portal can be done in a few steps. By default, Telnyx sends a T.38 re-INVITE once a fax tone is detected, and falls back to G.711 if no re-INVITE is received.

### Setting up Outbound Fax

1. Create a SIP Connection: visit the SIP Connections page, click **Add SIP Connection**, choose an authentication method (User/Pass or IP Address), enter the credentials, and click **Create**.
2. Create an Outbound Profile: visit the **Outbound** page, click **+ADD OUTBOUND PROFILE**, name the profile, select the connection to use for fax traffic, and click **Add**.

By default, Telnyx sends a T.38 re-INVITE once a fax tone is detected. To change this behavior, edit the connection and adjust the **T.38 Re-invite Initiated By** setting to one of: Telnyx (default), Customer, or Disabled (which enables G.711 fax calls).

### Setting up Inbound Fax

1. Create a SIP Connection: visit the **Connections** page, click **Add Connection**, choose an authentication method, enter the credentials, and click **Create**.
2. Purchase a number: visit the **Numbers** page, use the **Search Numbers** tab to find a number by region, area code, prefix, or other criteria, click **+Add to Cart**, then check out from the shopping cart.
3. Assign a SIP Connection: on the **Numbers** page, open the **My Numbers** tab, click the **Connection** drop-down next to the purchased number, and select the connection created for receiving faxes.

By default, Telnyx expects the customer to send a T.38 re-INVITE. If no re-INVITE is received, the fax call continues with the G.711 codec. Unchecking **Enable T.38 FAX gateway** under the Numbers page forces Telnyx to not accept a T.38 re-INVITE.

To explicitly enable T.38 re-INVITES:

1. Visit the **Numbers** page and open the **My Numbers** tab.
2. Click the **Advanced Options** (gear icon) next to the number.
3. Click **Expert Configuration** to reveal additional options.
4. Check **Enable T.38 Fax Gateway**.

### Fax Machine Settings

Different fax machine manufacturers have varying default transmission settings, many originally designed for copper lines. The following settings help ensure reliability when using an ATA with any VoIP service. Most modern fax machines allow these values to be modified without difficulty; consult the device's user guide if changes are needed.

- **Set the baud rate to 9600 or below**: this may appear as "transmission speed", "compatibility mode", or "VoIP mode". Slower speeds reduce the chance of failure from packet loss, jitter, and latency, and the impact grows with the number of pages.
- **Disable Error Correction Mode (ECM)**: ECM causes retransmits when noise, poor signal, or packet loss is detected. Because packet loss, jitter, and latency are normal on the Internet, retransmits increase call duration and instability. Disabling ECM prevents this.
- **Set fax resolution to "normal"**: using normal quality instead of high, fine, or ultra-fine increases speed and reliability by reducing the amount of data transmitted.
- **Disable dial tone detection**: only change this if the fax machine fails to dial outbound properly.

Telnyx does not support SRTP encryption when T.38 is enabled.

## Programmable Fax API Errors

The Programmable Fax API surfaces errors in two places: the `failure_reason` field of webhook event payloads, and the result code/message columns of the Fax API CDR CSV export from the Telnyx Portal Reporting section.

### Outbound Webhook Errors

| Error | Description |
| --- | --- |
| `file_size_limit_exceeded` | The provided PDF is larger than the prescribed size limit (e.g., greater than 50 MB). |
| `page_count_limit_exceeded` | The provided PDF contains more pages than the prescribed limit (e.g., more than 350 pages). |
| `fax_initial_communication_timeout` | The call did not connect to a valid fax machine, or the destination is not sending fax tones. |
| `fax_signaling_error` | Telephony engine error. Includes no response after sending a page, a bad response to a DCS fax message, or training failure. |
| `file_download_failed` | The service that downloads the customer's PDF before initiating the fax was unable to download it. Only 2XX HTTP responses are accepted; 3XX redirects are not followed. |
| `file_format_invalid` | The customer file is not a PDF, or is an invalid PDF. |
| `receiver_call_dropped` | Telephony engine error. The call dropped prematurely. |
| `receiver_communication_error` | Telephony engine error. May indicate a general call failure or a telephony routing error. |
| `receiver_decline` | Telephony engine error. The destination declined the call attempt. |
| `receiver_invalid_number_format` | Telephony engine error. The destination number is not in a valid +E.164 format. |
| `receiver_no_response` | Telephony engine error. The called party did not respond with an alerting or connect indication within the prescribed period. |
| `receiver_recovery_on_timer_expire` | Telephony engine error. The remote party sent a SIP 408 for an expired/timed-out call, or there is an issue with the downstream carrier partner. |
| `receiver_unallocated_number` | Telephony engine error. The called party number is in a valid format but is not currently allocated. |
| `service_unavailable` | Internal Telnyx error. A call to another service (such as initiating the outbound call or retrieving the PDF) failed. May also indicate a non-typical media conversion failure. |
| `success` | Telnyx to investigate this further. |

Retries for outbound faxes that result in errors must be configured on the client application; Telnyx does not automatically retry failed faxes.

### Inbound Webhook Errors

| Error | Description |
| --- | --- |
| `carrier_lost` | The connection to the carrier dropped while receiving the fax. |
| `fax_signaling_error` | Telephony engine error. Includes no further data after receiving a page, or bad data sent from the sender. |
| `received` | Telnyx to investigate this further. |
| `sender_call_dropped` | Telephony engine error. The call dropped prematurely. |
| `sender_canceled` | Telephony engine error. The sender canceled the call prematurely or before data transmission completed. |
| `sender_communication_error` | Telephony engine error. May include a general call failure or a telephony routing error on the sender side. |

### Other Webhook Errors

Additional webhook error codes include: `account_disabled`, `connection_channel_limit_exceeded`, `destination_invalid`, `destination_not_in_countries_whitelist`, `destination_not_in_service_plan`, `destination_unreachable`, `invalid_ecm_response_from_receiver`, `no_outbound_profile`, `outbound_profile_channel_limit_exceeded`, `outbound_profile_daily_spend_limit_exceeded`, `receiver_incompatible_destination`, `receiver_no_answer`, `user_busy`, `user_channel_limit_exceeded`, and `fax_initial_communication_timeout`.

### Fax API CDR Result Codes

These codes appear in the last two columns of the CSV file generated from the Telnyx Portal Reporting section when **Report Type** is set to **Fax API**.

| Result Code | Message |
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
