---
title: Porting Numbers to Telnyx
summary: A consolidated reference for porting numbers to Telnyx from Skype, Twilio,
  Microsoft Teams, and VoIP resellers (Aircall, Intercom, RingCentral, Vonage, Grasshopper),
  including carrier-specific credentials, common porting errors (TN Not Portable,
  Invalid Reseller, Authorized Name Mismatch), and related voice features such as
  Repeat Call Guard, Branded Calling, and Inbound Call Screening.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
updated_at: 2026-07-17T09:01:08Z
---

# Porting Numbers to Telnyx

*Part 5 of 5 — see also: [Part 1](porting-numbers-to-telnyx--part-1.md), [Part 2](porting-numbers-to-telnyx--part-2.md), [Part 3](porting-numbers-to-telnyx--part-3.md), [Part 4](porting-numbers-to-telnyx--part-4.md)*

A consolidated reference for porting numbers to Telnyx from Skype, Twilio, Microsoft Teams, and VoIP resellers (Aircall, Intercom, RingCentral, Vonage, Grasshopper), including carrier-specific credentials, common porting errors (TN Not Portable, Invalid Reseller, Authorized Name Mismatch), and related voice features such as Repeat Call Guard, Branded Calling, and Inbound Call Screening.

## Inbound Call Screening

Inbound Call Screening protects Telnyx numbers from unwanted and spam calls by flagging or blocking suspicious incoming calls based on customizable conditions.

### Configuration

1. Log in to the Telnyx Mission Control Portal.
2. Navigate to **My Numbers** in the left-hand sidebar.
3. Choose the Telnyx number to update and select **Edit**.
4. Under Number Settings, click the **Voice** tab.
5. Check the box labeled **Enable Inbound Call Screening** to activate the screening options:
   - **Flag Calls:** Suspicious calls are allowed to reach your infrastructure but are clearly labeled. Recommended for users who want to perform custom routing (e.g., sending spam to a specific IVR or voicemail).
   - **Reject Calls:** Suspicious calls are automatically blocked at the network level and will not reach your servers.
6. Save your settings.

Inbound Call Screening is free as of March 17, 2026.

### How It Works

Inbound Call Screening uses three factors:

- **Number Reputation Database:** Telnyx aggregates data from multiple reputation providers — Nomorobo, YouMail, and CallerAPI — to define the reputation of a number and classify callers as potential spammers.
- **Number Validation:** Telnyx analyzes the validity and existence of originating numbers to ensure compliance with telecommunication standards and mitigate risks.
- **SHAKEN/STIR Attestation:** Inbound Call Screening employs the SHAKEN/STIR attestation protocol to validate the authenticity of Caller ID information.

Screening is applied to the following attestation levels:

- **Attestation C:** The originating carrier cannot authenticate the Caller ID or the Caller ID has been identified as invalid. Calls with C attestation are potentially suspicious and are subjected to Inbound Call Screening.
- **Attestation Invalid:** The SHAKEN/STIR attestation is deemed invalid — possibly due to certificate problems or technical errors — and indicates a potential risk of spam or fraud.

### Handling Unwanted Calls

- **Reject calls:** Suspicious calls as defined by the above criteria are rejected and not connected to your Telnyx number.
- **Flag calls:** Suspicious calls are flagged with clear indications. The name part of the From and P-Asserted-ID headers displays "*SPAM LIKELY,*" and a custom SIP header, `X-Telnyx-Call-Screening: SPAM LIKELY,`, is added to the SIP INVITE message. If webhooks are enabled, the `call.initiated` webhook includes the variable `call_screening_result` with the value `spam_likely`.

### Availability

Inbound Call Screening currently applies to calls originating from the United States or Canada for number reputation screening. SHAKEN/STIR attestation screening applies to calls from North America.

To maximize the benefits, ensure webhooks are enabled on your SIP Connection settings or through your programmable voice applications. Webhooks provide real-time notifications and detailed insights into the call screening process and outcomes.

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
