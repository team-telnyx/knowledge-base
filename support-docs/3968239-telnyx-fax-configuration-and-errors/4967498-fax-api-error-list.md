---
source_url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
scraped: 2026-06-11
---

Fax API - Error List | Telnyx Help Center

[Skip to main content](#main-content)

# Fax API - Error List

In this article find explanations for both outbound and inbound errors you might experience with Programmable Fax.

Written by Dillin

January 7, 2026

Table of contents

# 1) Fax - Errors contained in the Webhook Payload:

These error details will be included in the failure\_reason field contained in the Fax API Webhook event payloads. For tutorials and other details on the API Requests and Webhook payload formats, please refer to this [Documentation](https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api).

* ## **Outbound Programmable Fax Errors**

|  |  |
| --- | --- |
| **Error** | **Description** |
| **file\_size\_limit\_exceeded** | Error from Telnyx programmable FAX Application indicating the .pdf file provided is greater in size than the prescribed limits. (i.e. bigger than 50MB) |
| **page\_count\_limit\_exceeded** | Error from Telnyx programmable FAX Application indicating the .pdf file provided is containing more number pages than the prescribed limits. (i.e. more than 350 Pages) |
| **fax\_initial\_communication\_timeout** | This may indicate that the call did not connect to a valid fax machine/the destination is not sending fax tones. |
| **fax\_signaling\_error** | Error from Telnyx Telephony Engine. Includes scenarios such as no response after sending a page, receiving a bad response to a DCS fax message, or training. |
| **file\_download\_failed** | The non-telephony service responsible for downloading the customer's PDF prior to initiating the fax was unable to download the file. Please ensure that there are no redirect responses (3XX HTTP); only 2XX HTTP responses will ensure we download your file and process it. |
| **file\_format\_invalid** | The customer file format is not PDF or is an invalid PDF. |
| **receiver\_call\_dropped** | Error from Telnyx Telephony Engine. The call dropped prematurely. |
| **receiver\_communication\_error** | Error from Telnyx Telephony Engine. It may indicate a general call failure or a telephony routing error. |
| **receiver\_decline** | Error from Telnyx Telephony Engine. The destination declined the call attempt. |
| **receiver\_invalid\_number\_format** | Error from Telnyx Telephony Engine. The destination number is not in a valid +E.164 format. |
| **receiver\_no\_response** | Error from Telnyx Telephony Engine. This cause is used when a called party does not respond to a call establishment message with either an alerting or connect indication within the prescribed period of time allocated. |
| **receiver\_recovery\_on\_timer\_expire** | Error from Telnyx Telephony Engine. Remote party sends a SIP 408 for an expired/timed-out call or an issue with the downstream carrier partner. |
| **receiver\_unallocated\_number** | Error from Telnyx Telephony Engine. This cause indicates that the called party cannot be reached because, although the called party number is in a valid format, it is not currently allocated (assigned). |
| **service\_unavailable** | Internal Telnyx error. A call to another service, such as to initiate the outbound call or to retrieve the PDF for sending, failed. Could also be due to a non-typical media conversion failure. |
| **success** | Telnyx to investigate this further. |

**NOTE**: Retries for outbound faxes, which may result in an error must be configured on the client application; Telnyx does not automatically retry faxes with errors.

* ## **Inbound Programmable Fax Errors**

|  |  |
| --- | --- |
| **Error** | **Description** |
| **carrier\_lost** | The connection to the carrier dropped while receiving the fax |
| **fax\_signaling\_error** | Error from Telnyx Telephony Engine. Similar to outbound error, but in reverse. Includes scenarios such as no further data after receiving a page, bad data sent from the sender etc. |
| **received** | Telnyx to investigate this further. |
| **sender\_call\_dropped** | Error from Telnyx Telephony Engine. The call dropped prematurely. |
| **sender\_canceled** | Error from Telnyx Telephony Engine. The sender canceled the call prematurely or before the data had completed transmitting. |
| **sender\_communication\_error** | Error from Telnyx Telephony Engine. Can include a general call failure or a telephony routing error on the sender side. |

## Other Webhook Fax Errors Include:

* `account_disabled`
* `connection_channel_limit_exceeded`
* `destination_invalid`
* `destination_not_in_countries_whitelist`
* `destination_not_in_service_plan`
* `destination_unreachable`
* `invalid_ecm_response_from_receiver`
* `no_outbound_profile`
* `outbound_profile_channel_limit_exceeded`
* `outbound_profile_daily_spend_limit_exceeded`
* `receiver_incompatible_destination`
* `receiver_no_answer`
* `user_busy`
* `user_channel_limit_exceeded`
* `fax_initial_communication_timeout`

# 2) Fax - Errors in the Fax API CDR

These error codes and messages are contained in the last 2 columns in the CSV file generated by the Telnyx Portal Reporting Section, specifically, when selecting "Report Type": "Fax API".

* <https://portal.telnyx.com/#/reporting/detailed-records>

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1919202806/3ab353c210be7169fd3b7fc5dc8e/image.png?expires=1781168400&signature=66a75110cc7b82b29c9c452c2cd5f32ee95ef3e7add9b492d10b96fe2a5315b7&req=dSkmH8t%2Bn4lfX%2FMW1HO4zWHXZOsqDJ0b0ModIuHw1w2ZH254c191mA4RZCWX%0ANAb5qgmmdim%2FWBt3sXA%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1919202806/3ab353c210be7169fd3b7fc5dc8e/image.png?expires=1781168400&signature=66a75110cc7b82b29c9c452c2cd5f32ee95ef3e7add9b492d10b96fe2a5315b7&req=dSkmH8t%2Bn4lfX%2FMW1HO4zWHXZOsqDJ0b0ModIuHw1w2ZH254c191mA4RZCWX%0ANAb5qgmmdim%2FWBt3sXA%3D%0A)

|  |  |
| --- | --- |
| **Result Code** | **Message** |
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

---

Related Articles

[Fax service with Telnyx (via T.38 or G711)](https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711)[Global Number Types](https://support.telnyx.com/en/articles/1458084-global-number-types)[Port Request Statuses](https://support.telnyx.com/en/articles/3284588-port-request-statuses)[SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)[Troubleshooting Call Completion](https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion)

Did this answer your question?

😞😐😃

Table of contents
