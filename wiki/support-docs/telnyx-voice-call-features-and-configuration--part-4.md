---
title: Telnyx Voice Call Features and Configuration
summary: A comprehensive guide to Telnyx voice calling features including Caller ID,
  call forwarding, voicemail, call screening, branded calling, HD Voice, noise suppression,
  and troubleshooting for both inbound and outbound calls.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
  content_hash: c528f19b926475289c58f426f74de5c5b0f7d0bc9b3a76ac4447a1e418fbdd1e
- url: https://support.telnyx.com/en/articles/1130657-call-forwarding
  content_hash: 06a221cc61118e8a4ed6054e2cd69199c51765ce1ae603e8a8f4b3cad9e83394
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
  content_hash: 3ce8f652dc422e882716c166d2b79959dd11377e2eefe70bcc768ffc352b6a29
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
  content_hash: c6356ee782721ef1b775ebd301d8357e636db3d73e4ba26aa82b96b5b77aeeab
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
  content_hash: 6c7f98d860edd3148a05a731f3cf9539c3a8294d3d947e739fd0ab9e91ef9842
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
  content_hash: fc49a89b215526036cd37d5f46f2d353cd4a541b1b514ef04ea476a6c07de538
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
  content_hash: b81a6debe7f4abda3e0eedff7b0af5068b3e5de85a3e2a8f2540dfaf2416d471
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
  content_hash: 22096e195e4672434185e9a48d4a1da41061041be99197719f0e37caa8a8180b
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
  content_hash: b75a7d8cb01b14945d552db640cc088753425212fe25282bd5bf4046e187ea95
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
  content_hash: 364725267880910da6fb1735a9c9c06c41c9fdca24507b6bc11a52baa6325fd5
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
  content_hash: 72806e66610395f65d2ed50aad95b5d2996a37788584eebd568c6c611d4ecc4f
- url: https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd
  content_hash: 53d23553f01e3a99c91fbae5cca41af5bf1a659010803c368660ef16d33acc40
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
  content_hash: 4a33b5f00804e9dd9d93e3eaf8dbbb532fbc1096917077f7d09cb146967a9c3b
- url: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail
  content_hash: be12d25dbdd414bb249454339f30ec838feb595a35fd0cf77f13e0691cbdb2f1
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
  content_hash: 8a798961c704cd1d7b926726757a20993701385438822810b80f483578273bcf
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
  content_hash: 062dea8622f0e635c24d43af5b2d69a557a92d6e7c0a202ecba891f76a729fbd
- url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
  content_hash: 6159af15e436f7bc8f64d450c699b429d1a51f6e69409422049fbbd3c87b753e
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
  content_hash: dfe91bdb59c3e49f6a7be38f769b5d98d4f2ebd75e2f327b739d0ef562dc526d
- url: https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature
  content_hash: 6040b91d672503e1e9686689f54a4e09e4947844189f91933c9dce79fb1a68ba
- url: https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression
  content_hash: 5bd00506d36f3c33cf5a0bb6c42c184ea4565b6205acf016aab4dc0496484bdd
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
