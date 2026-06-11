---
title: Telnyx Voice Call Features and Configuration
summary: A comprehensive guide to Telnyx voice calling features including Caller ID,
  call forwarding, voicemail, call screening, branded calling, HD Voice, noise suppression,
  and troubleshooting for both inbound and outbound calls.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130657-call-forwarding
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
- url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
- url: https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature
- url: https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression
updated_at: 2026-06-11T11:37:22Z
---

# Telnyx Voice Call Features and Configuration

*Part 4 of 4 — see also: [Part 1](telnyx-voice-call-features-and-configuration--part-1.md), [Part 2](telnyx-voice-call-features-and-configuration--part-2.md), [Part 3](telnyx-voice-call-features-and-configuration--part-3.md)*

A comprehensive guide to Telnyx voice calling features including Caller ID, call forwarding, voicemail, call screening, branded calling, HD Voice, noise suppression, and troubleshooting for both inbound and outbound calls.

## Troubleshooting Call Failures

### Outbound Call Failures

**Invalid Caller ID (SIP 403 D35):** The most common cause. Caller ID must be in +E.164 format. Use the Caller ID Override feature on your SIP connection to append a valid number.

**Dialed number not in whitelisted countries (SIP 403 D13):** Outbound Voice Profiles default to US and Canada only. Whitelist additional regions in your Outbound Voice Profile. International calling may require Level 2 verification (accessible from My Account → Verifications).

**SIP 403 Forbidden:** Common causes include authentication failure, negative account balance, no Outbound Voice Profile configured, token/tech prefix mismatch, or using a caller ID number belonging to another Telnyx user.

**SIP 503 No Routes Found:** Usually indicates a routing issue for the specific destination. Contact support with call examples. Expected in cases of international caller ID spoofing.

### General Hangup Reasons

| Cause | Code | Meaning |
|---|---|---|
| NORMAL_CLEARING | 16 | Call ended normally (party hung up) |
| USER_BUSY | 17 | Called party is on another call |
| INCOMPATIBLE_DESTINATION | 88 | Endpoint incompatibility (e.g., SRTP mismatch, codec mismatch) |
| MANAGER_REQUEST | 16 | Telnyx terminated the call (fraud prevention or negative balance) |
| CALL_REJECTED | 21 | Telnyx rejected the call (4xx error, e.g., invalid caller ID) |
| NORMAL_TEMPORARY_FAILURE | 41 | Routing issue with downstream carriers (5xx error) |

### Inbound Hangup Reasons

| Cause | Code | Meaning |
|---|---|---|
| RECOVERY_ON_TIMER_EXPIRE | 102 | No response to SIP INVITEs; usually a firewall/NAT issue |
| MANDATORY_IE_MISSING | 96 | Missing mandatory SIP headers; may indicate customer device requires authentication from unexpected IPs |
| UNALLOCATED_NUMBER | 1 | Number not assigned to a SIP connection, credentials-based connection not registered, or number not assigned to an extension |
| PROGRESS_TIMEOUT | 16 | No 180/183 received within default 5 seconds; adjustable via "No Ringback Timeout" in SIP connection inbound settings |
| ALLOTTED_TIMEOUT | 602 | Destination took too long to answer; triggered by answer timeout setting on SIP Connection inbound settings or Call Control application |

### Inbound Call Failures

If you are not receiving inbound calls:
- **Credential-based connections:** Ensure SIP REGISTER requests are reaching Telnyx. Whitelist Telnyx IP addresses.
- **IP/FQDN-based connections:** Verify the IP address and port match what your PBX is listening on. Ensure firewall/NAT configuration allows traffic and port forwarding is enabled for both SIP (signaling) and RTP (media).

Use the Portal's debugging tool to view SIP logs and call flows. Contact support at support@telnyx.com for further assistance.
