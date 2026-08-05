---
title: Telnyx Voice Services Overview
summary: This page consolidates Telnyx support documentation covering company locations,
  voice termination coverage, call completion (local and rural), rate sheets and LRN-based
  pricing, N11 and emergency dialing, inbound call screening, and PSTN replacement
  / local calling features.
sources:
- url: https://support.telnyx.com/en/articles/1130646-where-is-telnyx-located
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
- url: https://support.telnyx.com/en/articles/1130664-countries-that-telnyx-offers-termination-in
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/4567969-united-states-n11-codes
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
- url: https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
- url: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
- url: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
updated_at: 2026-08-05T13:30:13Z
---

# Telnyx Voice Services Overview

*Part 5 of 5 — see also: [Part 1](telnyx-voice-services-overview--part-1.md), [Part 2](telnyx-voice-services-overview--part-2.md), [Part 3](telnyx-voice-services-overview--part-3.md), [Part 4](telnyx-voice-services-overview--part-4.md)*

This page consolidates Telnyx support documentation covering company locations, voice termination coverage, call completion (local and rural), rate sheets and LRN-based pricing, N11 and emergency dialing, inbound call screening, and PSTN replacement / local calling features.

## Inbound Call Screening

Inbound Call Screening protects Telnyx numbers from unwanted and spam calls by flagging or blocking incoming calls based on customizable conditions.

### Features

- **Enhanced Call Control** — Reject or flag suspicious calls based on customizable conditions.
- **Spam Call Detection** — Screen and identify potential spam calls to protect numbers from unwanted solicitations and fraudulent activity.

### Configuration

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Navigate to the "My Numbers" section in the left-hand sidebar.
3. Choose the Telnyx number to update and select **Edit** to manage its Inbound Call Screening configuration.
4. Under Number Settings, click the **Voice** tab to enable or adjust Inbound Call Screening preferences.

By default, screening options are greyed out and inactive. Check the box labeled **"Enable Inbound Call Screening"** to activate two configuration options:

- **Flag Calls** — Suspicious calls are allowed to reach the infrastructure but are clearly labeled. Recommended for users who want to perform custom routing (e.g., sending spam to a specific IVR or voicemail).
- **Reject Calls** — Calls identified as suspicious are automatically blocked at the network level and never reach the servers.

Save the call screening settings when finished.

### Cost

Inbound Call Screening is free. As of March 17, 2026, there are no charges to enable or use Inbound Call Screening on any number in a Telnyx account.

### How it works

Three factors are used to implement inbound call screening:

- **Number Reputation Database** — Telnyx aggregates data from multiple reputation providers such as **Nomorobo**, **YouMail**, and **CallerAPI** to define the reputation of a number and classify callers as potential spammers. Cross-referencing three providers allows Telnyx to identify more spam and fraudulent numbers with greater confidence.
- **Number Validation** — Telnyx analyzes the validity and existence of originating numbers to ensure compliance with telecommunication standards and mitigate risks. Invalid or non-existent numbers can be flagged or rejected.
- **SHAKEN/STIR attestation** — Inbound Call Screening employs the SHAKEN/STIR attestation protocol to validate the authenticity of Caller ID information. Screening applies to:
  - **Attestation C** — The originating carrier cannot authenticate the Caller ID or the Caller ID has been identified as invalid. Calls with C attestation are potentially suspicious and are subjected to Inbound Call Screening.
  - **Attestation Invalid** — The SHAKEN/STIR attestation is deemed invalid (possibly due to certificate problems or technical errors), indicating a potential risk of spam or fraud.

### Handling unwanted calls

- **Reject calls** — Suspicious calls as defined by the above criteria are rejected and not connected to the Telnyx number.
- **Flag calls** — Suspicious calls matching the defined conditions are flagged. The name part of the From and P-Asserted-ID headers displays "*SPAM LIKELY,*" and a custom SIP header "*X-Telnyx-Call-Screening: SPAM LIKELY,*" is added to the SIP INVITE. If webhooks are enabled, the *call.initiated* webhook includes the variable `call_screening_result` with the value `spam_likely`.

### Availability

Inbound Call Screening currently applies to calls originating from the United States or Canada for number reputation screening. SHAKEN/STIR attestation screening applies to calls from North America.

### Additional requirements

To maximize the benefits of Inbound Call Screening, ensure webhooks are enabled. Specify webhook URLs on SIP Connection settings or through programmable voice applications. Webhooks provide real-time notifications and detailed insights into the call screening process and outcomes. Enabling webhooks includes the `call_screening_result` variable in the *call.initiated* webhook.

Example webhook payload:

```
{
   "event_type":"call.initiated",
   "id":"901d2366-adcd-45f0-9fcf-c17ed5d1ecd7",
   "occurred_at":"2023-06-29T13:01:50.423002Z",
   "payload":{
      "call_control_id":"v3:NA0M2_T5NkETExuhDFz0XyRJ2d4IEb1kdmfRRqFv2ils6id9RIxUkg",
      "call_leg_id":"1cc5d164-167d-11ee-a812-02420a1f0d69",
      "call_screening_result":{
         "action":"flag_calls",
         "reputation":null,
         "shaken_stir_attestation":"A"
      },
      "call_session_id":"1cc5db28-167d-11ee-a1dc-02420a1f0d69",
      "caller_id_name":"test",
      "client_state":null,
      "connection_id":"1542950386652912121",
      "custom_headers":[
         {
            "name":"X-rtc_leg_uuid",
            "value":"d72f7cf9-9b2d-411f-917c-0f85f251a488"
         }
      ],
      "direction":"incoming",
      "from":"+from-number",
      "start_time":"2023-06-29T13:01:50.423002Z",
      "state":"parked",
      "to":"+to-number"
   },
   "record_type":"event"
}
```

## Accessing Canadian LRN Data

Canadian LRN (Local Routing Number) data is subject to regulatory restrictions and is not freely available.

1. **Regulatory Approval** — Customers must first apply for and receive approval from the **Canadian Local Number Portability Consortium (CNLPC)** to access Canadian LRN data through Telnyx. Contracted customers can submit applications for Non-Member Access to CA LRN data via the form on the [CNLPC non-member access page](https://clnpc.ca/non-member-access/). This offering only applies for contracted customers.
2. **Associated Costs** — There is an annual fee of approximately **$2,000 USD**, payable directly to the CNLPC. At this time, default Telnyx Number Lookup pricing applies — there is no special pricing for CA LRN lookups.
3. **Usage Requirements** — Due to the costs Telnyx incurs in facilitating access, Telnyx applies a minimum lookup requirement for customers. Access is reviewed and granted on a **case-by-case basis**. The minimum monthly spend on LRN lookups would need to be ~$225 to cover costs, which works out to about 150k LRN lookups at base price ($0.0015).

Once the above criteria have been met, Telnyx only needs proof of the CNLPC non-member access approval. Contact your CSM or [support@telnyx.com](mailto:support@telnyx.com) for more information.
