---
title: 'Telnyx Voice: Caller ID, Call Completion, and Pricing'
summary: A consolidated reference for Telnyx voice services covering Caller ID Number
  (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing
  and billing, LRN and number lookup, US local and rural call completion, PSTN replacement
  and local calling, and troubleshooting inbound and outbound call failures.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/2185372-where-can-i-see-pricing-options
- url: https://support.telnyx.com/en/articles/3317613-billing-decimal-values-considered
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
updated_at: 2026-07-17T09:05:14Z
---

# Telnyx Voice: Caller ID, Call Completion, and Pricing

*Part 5 of 5 — see also: [Part 1](telnyx-voice-caller-id-call-completion-and-pricing--part-1.md), [Part 2](telnyx-voice-caller-id-call-completion-and-pricing--part-2.md), [Part 3](telnyx-voice-caller-id-call-completion-and-pricing--part-3.md), [Part 4](telnyx-voice-caller-id-call-completion-and-pricing--part-4.md)*

A consolidated reference for Telnyx voice services covering Caller ID Number (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing and billing, LRN and number lookup, US local and rural call completion, PSTN replacement and local calling, and troubleshooting inbound and outbound call failures.

## Troubleshooting Call Completion

### Outbound Call Failures

#### Invalid Caller ID

The most common cause of outbound call termination problems, particularly when setting up a new SIP connection, is caller ID. When a call is rejected due to an invalid caller ID, the SIP response is **"403 Caller Origination Number is Invalid D35"**.

Industry regulations require a strict caller ID policy. For Telnyx to terminate a call, a caller ID in **+E.164** format must be passed. Many PBXs and softphones do not automatically pass a caller ID — it is often blank or, for credential-based SIP connections, the SIP username. As a result, the call is automatically rejected.

To append a valid caller ID, use the **Caller ID Override** functionality in the Portal. Select the relevant SIP connection from the **SIP Connections** tab and click the **Outbound Options** icon. From there, include a phone number that will be displayed on all outgoing calls made from this SIP connection.

#### Dialed Number Not in Whitelisted Countries/Regions

By default, all Outbound Voice Profiles allow traffic only to destinations in the United States and Canada. Calls to numbers outside this region return **"403 Dialed Number is not included in whitelisted countries D13"**.

To resolve this, whitelist the region in the Outbound Voice Profile associated with the relevant SIP connection. In the Mission Control Portal, select **Outbound Voice Profiles**, choose the relevant profile, and click the **+** button next to the relevant region. You may be prompted to request level 2 verification, which authorizes international calls. This can be requested by hovering over your initials in the top right of the Portal, selecting **My Account**, and clicking the **Verifications** tab, or directly at the [Verifications page](https://portal.telnyx.com/#/app/account/verifications).

#### 403 - Forbidden

A **"403 Forbidden"** can be returned for several reasons. The most straightforward cause is a failure to authenticate the SIP connection — using incorrect credentials on a credential-based connection or placing a call from an IP address not yet added to an IP-based connection. Telnyx returns "403 Forbidden" to protect the account from being charged for unauthorized use.

Other potential causes include:

- The Telnyx account is negative in balance.
- The connection does not have an Outbound Voice Profile configured.
- A token or tech prefix (if enabled on the FQDN/IP-based connection) does not match the one supplied in the SIP INVITE.
- The caller origination number (caller ID) belongs to another Telnyx user.

#### 503 - No Routes Found (or Service Unavailable)

A "503" error generally points to a routing issue for the specific destination. Contact support via the chat bubble in the Portal or by emailing [support@telnyx.com](mailto:support@telnyx.com), as this tends to require manual intervention. Provide a call example with source and destination numbers and an approximate timestamp. 503 errors are expected in cases such as attempting to spoof caller ID on outbound calls to international destinations.

### General Hangup Reasons

SIP error responses include a reason header with a high-level reason for the error, sometimes accompanied by a cause code.

- **NORMAL_CLEARING (16)**: The call was terminated in a regular, expected manner — typically because one party hung up.
- **USER_BUSY (17)**: The called party is engaged in another call and cannot accept new calls.
- **INCOMPATIBLE_DESTINATION (88)**: The destination was not suitable or compatible for the call — the calling party's channel was incompatible with the channel type requested at the destination. This is generally related to SDP from SIP INVITEs or 200 OK responses. A common scenario is encryption (e.g., SRTP) enabled on the Telnyx SIP connection but not on the device, or the SIP connection configured to offer codecs not supported by the device.
- **MANAGER_REQUEST (16)**: Telnyx's system terminated the call — manually when potential fraud is observed to limit high-cost usage, or automatically when the account balance has gone negative.

### Inbound Hangup Reasons

- **RECOVERY_ON_TIMER_EXPIRE (102)**: The call or session was terminated because a necessary response was not received before a timer expired. For inbound calls, this occurs after Telnyx sends three SIP INVITEs to a customer's SIP Connection with no response — usually indicative of a firewall or NAT issue. Verify that Telnyx IPs are whitelisted and that the IP address is listening on the specified port.
- **MANDATORY_IE_MISSING (96)**: A mandatory information element was expected in a message but was not present. This typically indicates an issue with the system or equipment sending the message. On inbound calls to customer devices, this can occur when Telnyx sends a SIP INVITE and the customer device responds with a 407 proxy authentication, suggesting the device is not expecting communication from Telnyx's SIP Proxy IP addresses.
- **UNALLOCATED_NUMBER (1)**: The called number is not assigned to any user or service. For inbound calls, this means the number is either not assigned to a SIP connection, the SIP connection is credentials-based and not currently registered, or the customer's system returned a valid response indicating the number is not assigned to any extension. Check the inbound rules of the device to ensure the number is expected in the correct dialled format (10, 11, or +E.164 digits).
- **PROGRESS_TIMEOUT (16)**: Telnyx did not receive ringback from the customer's phone system. By default, the call times out if no 180/183 is received within 5 seconds. This can be modified via the **No Ringback Timeout** parameter in the SIP connection's inbound options.
- **ALLOTTED_TIMEOUT (602)**: The server canceled the call because the destination channel took too long to answer. This occurs when the answer timeout setting on the SIP Connection's inbound settings is reached, or when the **Enable "hang-up" on timeout** option is set on a Call Control application.

### Outbound Hangup Examples

- **CALL_REJECTED (21)**: The SIP proxy returned a 4xx error code (usually 403) to the customer. Investigate the SIP signalling for the specific reason — invalid caller ID, destination not whitelisted in the outbound profile, etc.
- **NORMAL_TEMPORARY_FAILURE (41)**: Usually associated with a 5xx error code returned to the customer, often the result of a routing issue with downstream carriers. Contact Telnyx support.

### Further Troubleshooting

An exhaustive list of SIP response codes is available in the [Telnyx SIP Response Codes](telnyx-sip-response-codes.md) article. In general, a 403 error results from a discrepancy between what you are attempting to do and what your Telnyx account or PBX is configured to do. Other 4xx response codes (such as "404 Not Found" or "486 User Busy") generally indicate an issue with the destination device. 5xx errors, while much less common, are often the result of a routing issue.

The Debugging tool within the Portal can be used to view SIP logs and call flow for a specific call. The Debugging menu also contains features such as the Web Dialer for making calls directly from the Portal.

### Inbound Call Failures

Inbound calls are susceptible to fewer problems than outbound calls. If calls are not being received when expected, the issue is generally with SIP registration or the authentication method selected when setting up the SIP connection.

#### SIP Registration (Credential-Based Connections)

Telnyx maintains a registrar of devices associated with SIP connections. When SIP credentials are authenticated on a softphone or PBX, a SIP REGISTER request is sent to Telnyx, telling it where to send calls directed to the SIP URI. If inbound calls are not being received on a credential-based SIP connection, Telnyx is likely not receiving the SIP REGISTER requests. Ensure that traffic to and from the IP addresses and subnets listed in the [Whitelisting Telnyx IP Addresses](whitelisting-telnyx-ip-addresses.md) article is whitelisted.

#### IP and FQDN Authentication

For IP- or FQDN-based authentication, calls destined for the SIP URI are sent to the user-provided IP address(es) and network ports. If there is a discrepancy between the provided IP/port and the IP/port the PBX is actively listening on, calls will not reach the PBX.

Firewall and NAT configuration can also affect inbound calls. Whitelist traffic to and from the IP addresses and subnets listed in the [Whitelisting Telnyx IP Addresses](whitelisting-telnyx-ip-addresses.md) article. For IP or FQDN authentication, the PBX should be publicly exposed, or the router should have the necessary port forwarding configuration enabled for both the signalling (SIP) and media (RTP) streams.

If further troubleshooting is necessary, use the Debugging tool in the Portal to view SIP logs and call flow for a specific call, including those destined for the SIP URI that never reached the end device. Contact support via the chat bubble in the Portal or by emailing [support@telnyx.com](mailto:support@telnyx.com).
