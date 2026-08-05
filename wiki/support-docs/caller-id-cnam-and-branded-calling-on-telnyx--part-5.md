---
title: Caller ID, CNAM, and Branded Calling on Telnyx
summary: A consolidated reference covering how Telnyx handles Caller ID Number (CID),
  Caller ID Name (CNAM), Branded Calling, CLI/CLD validation, and related call-completion
  troubleshooting. It explains the differences between inbound and outbound CID and
  CNAM, how to configure each in Mission Control Portal, regional behavior in the
  US and Canada, supported number formats, anonymization, international spoofing restrictions,
  branded calling setup and limitations, and how to mitigate spam-likely flags and
  SIP errors.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
updated_at: 2026-08-05T13:31:03Z
---

# Caller ID, CNAM, and Branded Calling on Telnyx

*Part 5 of 5 — see also: [Part 1](caller-id-cnam-and-branded-calling-on-telnyx--part-1.md), [Part 2](caller-id-cnam-and-branded-calling-on-telnyx--part-2.md), [Part 3](caller-id-cnam-and-branded-calling-on-telnyx--part-3.md), [Part 4](caller-id-cnam-and-branded-calling-on-telnyx--part-4.md)*

A consolidated reference covering how Telnyx handles Caller ID Number (CID), Caller ID Name (CNAM), Branded Calling, CLI/CLD validation, and related call-completion troubleshooting. It explains the differences between inbound and outbound CID and CNAM, how to configure each in Mission Control Portal, regional behavior in the US and Canada, supported number formats, anonymization, international spoofing restrictions, branded calling setup and limitations, and how to mitigate spam-likely flags and SIP errors.

## Troubleshooting Call Completion

### Outbound Call Failures

**Invalid caller ID** is the most common cause of call termination problems, particularly when setting up a new SIP connection. When a call is rejected due to an invalid caller ID, you receive the SIP response **403 Caller Origination Number is Invalid D35**.

Industry regulations mandate a strict policy regarding caller ID. For Telnyx to successfully terminate your call, a caller ID in +E.164 format must be passed. Many PBXs and softphones do not automatically pass a caller ID — it is often blank or, for credential-based SIP connections, your SIP username. As a result, the call is automatically rejected.

To append a valid caller ID, each softphone and PBX has its own method. You can also append a caller ID to any SIP connection using the **Caller ID Override** functionality in the Portal. To set a Caller ID Override, select the relevant SIP connection from the **SIP Connections** tab and select the **Outbound Options** icon. From there, include a phone number that will be displayed on all outgoing calls made from this SIP connection.

**Dialed number not in whitelisted countries/regions** — by default, all Outbound Voice Profiles allow traffic only to destinations in the United States and Canada. Calls to numbers outside this region return **403 Dialed Number is not included in whitelisted countries D13**. To resolve this, whitelist the region in the Outbound Voice Profile associated with the relevant SIP connection by selecting **Outbound Voice Profiles** in Mission Control Portal, selecting the relevant profile, and clicking the "+" button next to the relevant region. You may be prompted to request level 2 verification, which authorizes international calls. This can be requested by hovering over your initials in the top right of the Portal, selecting **My Account**, and clicking the **Verifications** tab.

**403 - Forbidden** can be caused by:

- Failure to authenticate your SIP connection (incorrect credentials on a credential-based connection, or placing a call from an IP address not yet added to an IP-based connection).
- A negative Telnyx account balance.
- The connection used to place calls does not have an Outbound Voice Profile configured.
- A token or tech prefix mismatch on an FQDN/IP-based connection.
- The caller origination number (caller ID) is a phone number that belongs to another Telnyx user.

**503 - No routes found (or service unavailable)** generally points to a routing issue for the specific destination. If you receive a 5xx response code, contact support with a call example including source and destination numbers and an approximate timestamp. 503s are expected in cases such as attempting to spoof caller ID on outbound calls to international destinations.

### General Hangup Reasons

- **NORMAL_CLEARING (16)** — the call was terminated in a regular, expected manner; no errors occurred.
- **USER_BUSY (17)** — the called party is currently engaged in another call and cannot accept new incoming calls.
- **INCOMPATIBLE_DESTINATION (88)** — the destination was not suitable or compatible for the call, often related to SDP from SIP INVITEs or 200 OK responses. A common scenario is enabling encryption (such as SRTP) on the Telnyx SIP connection without enabling it on the device, or having the SIP connection configured to offer codecs not supported by the device.
- **MANAGER_REQUEST (16)** — Telnyx's system terminated the call, either manually (when potential fraud is observed to limit further high-cost call usage) or automatically (when the account balance has gone negative).

### Inbound Hangup Reasons

- **RECOVERY_ON_TIMER_EXPIRE (102)** — the call or session was terminated due to a timer expiration; a necessary response was not received in time. For inbound calls, this occurs after Telnyx sends three SIP INVITEs to a customer's SIP Connection with no response, usually indicative of a firewall or NAT issue. Verify that Telnyx IPs are whitelisted and that the IP address is listening on the specified port.
- **MANDATORY_IE_MISSING (96)** — a mandatory information element was expected in a message but was not present. This typically indicates an issue with the system or equipment sending the message. It has been observed on inbound calls where Telnyx sends the SIP INVITE and the customer device responds with a 407 proxy authentication, suggesting the device is not expecting communication from Telnyx's SIP Proxy IP addresses.
- **UNALLOCATED_NUMBER (1)** — the called number is not assigned to any user or service. For inbound calls, this typically means the number is not assigned to a SIP connection, the SIP connection is credentials-based and not currently registered, or the customer's system returned a valid response indicating the number is not assigned to any extension. Check the inbound rules of your device to ensure you are expecting the number in the correct dialed format (10, 11, or +E.164 digits).
- **PROGRESS_TIMEOUT (16)** — Telnyx did not receive ringback from the customer's phone system. By default, the call times out if no 180/183 is received from the customer within 5 seconds. This can be modified by changing the **No Ringback Timeout** parameter in the SIP connection's inbound options.
- **ALLOTTED_TIMEOUT (602)** — the server canceled the call because the destination channel took too long to answer. This occurs when the answer timeout setting on the SIP Connection's inbound settings is reached, or when using the Call Control Voice API with **Enable "hang-up" on timeout** set on the call control application.

### Outbound Hangup Examples

- **CALL_REJECTED (21)** — usually affects outbound calls when the SIP proxy returns a 4xx error code (usually 403) to the customer. Investigate the SIP signaling for the specific reason.
- **NORMAL_TEMPORARY_FAILURE (41)** — usually associated with a 5xx error code returned to the customer, often the result of a routing issue with downstream carriers. Contact Telnyx support for these instances.

### Further Troubleshooting

An exhaustive list of SIP response codes is available in [Telnyx SIP Response Codes](telnyx-sip-response-codes.md). In general, a 403 error is the result of a discrepancy between what you are attempting to do and what your Telnyx account or PBX is configured to do. Other 4xx response codes, such as 404 Not Found or 486 User Busy, generally indicate an issue with the destination device. 5xx errors are often the result of a routing issue.

To gain additional insight, use the debugging tool within the Portal to view SIP logs and call flow for a specific call. The Debugging menu also contains features such as the Web Dialer, which can be used to make calls directly from the Portal.

### Inbound Call Failures

Inbound calls are susceptible to fewer problems than outbound calls, but they can still be difficult to troubleshoot. If you are not receiving calls when you know you should be, this is generally an issue with SIP registration or the authentication method selected when setting up your SIP connection.

**SIP Registration (for credential-based connections)** — Telnyx maintains a registrar of devices associated with SIP connections. When you authenticate your SIP credentials on your softphone or PBX, a SIP REGISTER request is sent from your device to Telnyx, telling Telnyx where to send calls directed to your SIP URI. If you are not receiving inbound calls on a credential-based SIP connection, Telnyx is likely not receiving the SIP REGISTER requests from your device. Ensure that traffic to and from the IP addresses and subnets listed in the [Whitelisting Telnyx IP Addresses](whitelisting-telnyx-ip-addresses.md) article is whitelisted.

**IP and FQDN authentication** — calls destined for your SIP URI are sent to the user-provided IP address(es) along with the provided network ports. If there is a discrepancy between the IP address/port provided and the IP address/port your PBX is actively listening on, calls will not reach your PBX. Firewall and NAT configuration can also affect inbound calls. Ensure that traffic to and from the IP addresses and subnets listed in the [Whitelisting Telnyx IP Addresses](whitelisting-telnyx-ip-addresses.md) article is whitelisted. If using IP or FQDN authentication, ensure that your PBX is publicly exposed or that your router has the necessary port forwarding configuration enabled for both the signaling (SIP) stream and the media (RTP) stream.

For further troubleshooting, use the debugging tool in the Portal to view SIP logs and call flow for a specific call, including those destined for your SIP URI that never reached your end device. You can also contact support by starting a chat from the chat bubble on the lower right-hand corner of the Portal or by emailing [support@telnyx.com](mailto:support@telnyx.com).
