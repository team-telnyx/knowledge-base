---
title: Telnyx Fax Configuration & Errors
summary: Covers end-to-end setup of Telnyx fax service using T.38 or G711, including
  outbound and inbound configuration steps, fax machine optimization settings, and
  a complete reference of Programmable Fax API errors for both webhook payloads and
  CDR reports.
sources:
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-06-11T11:37:09Z
---

# Telnyx Fax Configuration & Errors

Covers end-to-end setup of Telnyx fax service using T.38 or G711, including outbound and inbound configuration steps, fax machine optimization settings, and a complete reference of Programmable Fax API errors for both webhook payloads and CDR reports.

## Outbound Fax Setup

Setting up outbound fax requires two components in the [Telnyx Mission Control Portal](https://portal.telnyx.com):

1. **Create a SIP Connection** — Navigate to the SIP Connections page, click **Add SIP Connection**, select your authentication method (User/Pass or IP Address), enter your details, and click **CREATE**.
2. **Create an Outbound Profile** — Navigate to the **OUTBOUND** page, click **+ADD OUTBOUND PROFILE**, give it a name, select the SIP connection you created for fax traffic, and click **ADD**.

By default, Telnyx sends a T.38 re-INVITE once a fax tone is detected. To change this behavior, edit your connection under Outbound and adjust the **T.38 Re-invite Initiated By** setting:

- **Telnyx** (default) — Telnyx initiates the re-INVITE
- **Customer** — The customer initiates the re-INVITE
- **Disabled** — T.38 is disabled; fax calls use G.711 instead

## Inbound Fax Setup

Setting up inbound fax requires three steps:

1. **Create a SIP Connection** — Navigate to the **CONNECTIONS** page, click **ADD CONNECTION**, select your authentication method, enter your details, and click **CREATE**.
2. **Purchase a number** — Go to the **NUMBERS** page, use the **SEARCH NUMBERS** tab to find numbers by Region, Area Code, Prefix, etc. Add selections to your cart and checkout.
3. **Assign a SIP Connection** — On the **MY NUMBERS** tab, use the Connection drop-down next to your purchased number and select the connection you created for receiving faxes.

By default, Telnyx expects the customer to send a T.38 re-INVITE. If no re-INVITE is received, the fax call continues with the G.711 codec.

### Enabling T.38 Re-Invites on a Number

To explicitly enable the T.38 Fax Gateway on a number:

1. Go to **NUMBERS** → **MY NUMBERS**
2. Click the **Advanced Options** (gear icon) next to the number
3. Expand **Expert Configuration**
4. Check **Enable T.38 Fax Gateway**

Unchecking the "Enable T.38 Fax Gateway" option on the Numbers page forces Telnyx to not accept a T.38 re-INVITE.

**Note:** SRTP encryption is not supported when T.38 is enabled.

## Fax Machine Settings for Reliability

Fax machines configured for copper lines may need adjustments when connected through an ATA over VoIP. Apply these settings if you experience reliability issues:

- **Set the baud rate to 9600 or below** — Menu options may refer to this as "transmission speed", "compatibility mode", or "VoIP mode". Slower speeds reduce failure from packet loss, jitter, and latency; the benefit increases with more pages.
- **Disable Error Correction Mode (ECM)** — ECM triggers retransmits on packet loss or jitter, which increases call duration and signal instability on VoIP. Disabling ECM prevents unnecessary retransmits.
- **Set fax resolution to "normal"** — Avoiding high/fine/ultra-fine resolution reduces the amount of data (packets) that must be transmitted.
- **Disable dial tone detection** — Only change this if the fax machine fails to dial outbound properly.

## Programmable Fax API Errors

Errors are surfaced in two ways: within webhook payload `failure_reason` fields and within Fax API CDR reports.

### Outbound Webhook Errors

| Error | Description |
|---|---|
| `file_size_limit_exceeded` | The PDF exceeds the size limit (greater than 50 MB) |
| `page_count_limit_exceeded` | The PDF exceeds the page count limit (more than 350 pages) |
| `fax_initial_communication_timeout` | The call did not connect to a valid fax machine or the destination is not sending fax tones |
| `fax_signaling_error` | Telephony engine error — includes no response after sending a page, bad response to a DCS fax message, or training failure |
| `file_download_failed` | The service could not download the PDF. Ensure there are no redirect responses (3XX HTTP); only 2XX responses are accepted |
| `file_format_invalid` | The file is not a PDF or is an invalid PDF |
| `receiver_call_dropped` | The call dropped prematurely |
| `receiver_communication_error` | General call failure or telephony routing error |
| `receiver_decline` | The destination declined the call attempt |
| `receiver_invalid_number_format` | The destination number is not in valid +E.164 format |
| `receiver_no_response` | The called party did not respond to call establishment within the prescribed period |
| `receiver_recovery_on_timer_expire` | Remote party sent a SIP 408 (expired/timed-out call) or there is an issue with the downstream carrier partner |
| `receiver_unallocated_number` | The called party number is valid in format but not currently allocated (assigned) |
| `service_unavailable` | Internal Telnyx error — a call to another service (e.g., to initiate the outbound call or retrieve the PDF) failed, or a non-typical media conversion failure |
| `success` | Telnyx to investigate further |

Retries for outbound faxes that result in errors must be configured on the client application; Telnyx does not automatically retry faxes with errors.

### Inbound Webhook Errors

| Error | Description |
|---|---|
| `carrier_lost` | The connection to the carrier dropped while receiving the fax |
| `fax_signaling_error` | Telephony engine error (inbound direction) — includes no further data after receiving a page, bad data sent from the sender, etc. |
| `received` | Telnyx to investigate further |
| `sender_call_dropped` | The call dropped prematurely |
| `sender_canceled` | The sender canceled the call before data transmission completed |
| `sender_communication_error` | General call failure or telephony routing error on the sender side |

### Other Webhook Fax Errors

Additional error values that may appear in webhook payloads:

- `account_disabled`
- `connection_channel_limit_exceeded`
- `destination_invalid`
- `destination_not_in_countries_whitelist`
- `destination_not_in_service_plan`
- `destination_unreachable`
- `invalid_ecm_response_from_receiver`
- `no_outbound_profile`
- `outbound_profile_channel_limit_exceeded`
- `outbound_profile_daily_spend_limit_exceeded`
- `receiver_incompatible_destination`
- `receiver_no_answer`
- `user_busy`
- `user_channel_limit_exceeded`
- `fax_initial_communication_timeout`

## Fax API CDR Error Codes

These result codes and messages appear in the last two columns of CSV files generated by the Telnyx Portal Reporting section (Report Type: "Fax API").

| Result Code | Message |
|---|---|
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
