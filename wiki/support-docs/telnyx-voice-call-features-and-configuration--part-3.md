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

*Part 3 of 4 — see also: [Part 1](telnyx-voice-call-features-and-configuration--part-1.md), [Part 2](telnyx-voice-call-features-and-configuration--part-2.md), [Part 4](telnyx-voice-call-features-and-configuration--part-4.md)*

A comprehensive guide to Telnyx voice calling features including Caller ID, call forwarding, voicemail, call screening, branded calling, HD Voice, noise suppression, and troubleshooting for both inbound and outbound calls.

## Outbound Voice Profiles and SIP Connection Organization

SIP Connections are the first layer of organization for inbound and outbound traffic. Usage reports can be aggregated by connection, and Customer Detail Records (CDRs) include the connection name.

CDRs can be filtered by: SIP Connection, Record Type (Complete, Incomplete, Errors), Call Type (Inbound, Outbound), CLI, CLD, and Tags.

### Tagging

Both numbers and outbound profiles support tags for additional filtering and organization. Tags can mark department, office location, purchase date, or client grouping. Tags appear in CDRs:
- **Inbound calls:** CDR shows the tag assigned to the DID.
- **Outbound calls:** CDR shows the tag assigned to the outbound voice profile (not the DID tag).

Common uses include tagging by department/end-user, office location, purchase date, client grouping, and troubleshooting identification.

## Repeat Call Guard

Repeat Call Guard controls how many times a destination number can be called within a specific time window. It applies only to calls made through SIP connections and is configured per Outbound Voice Profile (limits are tracked independently per profile).

To configure:

1. Go to **Voice → Outbound Voice Profiles** and select a profile.
2. Find the **Repeat Call Guard** section below the Audio File Channel Type field.
3. Enable the toggle and set:
   - **Start Time** / **End Time** (UTC) for the active calling window.
   - **Calls per CLD:** Maximum call attempts per destination number within a 24-hour rolling window.
4. Save.

Once the limit is reached, additional calls are blocked until the next rolling reset. The counter resets on a rolling 24-hour basis from the time of the first allowed call. Blocked calls receive: `Daily calling restriction to Destination Number exceeded D66 (code 403)`.

You can also configure via API by PATCHing the outbound voice profile with a `calling_window` object containing `start_time`, `end_time`, and `calls_per_cld`.

## Short Duration Calls

Short Duration Calls (SDCs) are outbound calls of 6 seconds or less. Telnyx allows up to 15% of your total outbound traffic to be SDCs. If SDCs exceed 15% in a calendar month, additional charges apply to **all** short duration calls made that month (not just those above the threshold).

As of January 1, 2024, short duration calls to international destinations are also subject to a $0.01 per call fee when the 15% threshold is exceeded.

Calculation: `Short Duration Call Count / Total Connected Call Count`, based on UTC timeframes.

Telnyx does not support use cases requiring short duration calls. To identify the source of SDCs:
1. Download a detail report from [reporting](https://portal.telnyx.com/#/reporting/detailed-records), filtering outbound calls only.
2. Sort the CSV by call duration.
3. Remove 0-second calls.
4. Count calls ≤ 6 seconds and check the SIP connection name column.

## Calls Per Second (CPS) Surcharge

SIP trunking outbound calls are subject to a limit of 20 CPS from the same IP address or SIP username (calls exceeding this are rejected with 503). Telnyx can extend this for legitimate use cases.

The CPS surcharge is based on the **95th percentile peak CPS** calculated per customer monthly:
1. Peak CPS per hour is determined for each hour where CPS > 0.
2. The 95th percentile of that monthly dataset is calculated.
3. This value determines the surcharge using graduated pricing:
   - First 5 CPS: free
   - 6–25 CPS: $12/CPS
   - 26–200 CPS: $16/CPS
   - 201–250 CPS: $24/CPS
   - 251+ CPS: $30/CPS

Example: 95th percentile peak CPS of 163 → (5 × $0) + (20 × $12) + (138 × $16) = $2,448.

CPS surcharges apply only to SIP trunking traffic (not programmable voice). Monitor your patterns using the [Outbound Peak CPS dashboard](https://portal.telnyx.com/#/app/reports/dashboard).

## CLI and CLD Validation

Telnyx validates Calling Line Identity (CLI — the originating number) and Calling Line Destination (CLD — the dialed number) against North American National Numbering databases for all outbound calls between NANPA numbers (excluding toll-free), effective June 6, 2022.

- **CLI validation failure:** Call rejected with SIP 403 — "The origination number does not have a subscriber assigned. The number is invalid."
- **CLD validation failure:** Call rejected with SIP 404 — "The destination number does not have a subscriber assigned. The number is invalid."

CLI validation applies to all numbers used for outbound calls through Telnyx, regardless of the number provider. Validation cannot be disabled. Use the [Your Number Lookup Guide](your-number-lookup-guide.md) tool to check numbers before calling. For blocked calls with valid CLI/CLD, contact support.

## Call Completion (US Rural and Local)

### Rural Call Completion

Long-distance calls to rural US areas can experience dead air, prolonged ringing, or intercept recordings. These issues are typically caused by least-cost routing models. To report rural call completion issues, contact support at support@telnyx.com or +1-888-980-9750 with:
- Description of the issue
- From and To numbers
- Date, time, and timezone
- Any testing the rural carrier has conducted
- Contact info for a rural carrier representative

### Local Call Completion

Local call failures within the US often result from translation issues after porting or at tandem switches. Call routing uses LERG, LATA, LRN, LNP, NPA, and Rate Center data.

- **Porting out:** The losing carrier may not have removed old routing information, causing calls to not reach the new destination.
- **Tandem switches:** Downstream or upstream tandem providers may not have mapped LRN NPA-NXX correctly.

Telnyx uses "seasoned" LRNs and has redundant tandem coverage. To report local calling issues, contact support with: description, From/To numbers, date/time/timezone, and any error messages heard by callers. Call examples should be within 48 hours of occurrence.

## Post Dial Delay (PDD)

PDD is the time from sending the final dialed digit (or SIP INVITE) to hearing ring tone (or receiving a SIP 180 Ringing response). PDD is commonly experienced on wireless devices with low signal. The industry considers under 7 seconds acceptable. If you experience PDD over 7 seconds, contact support at support@telnyx.com.

## UK TPS Register Guidelines

The UK Telephone Preference Service (TPS) is a register of consumers who opt out of unsolicited direct marketing calls. Under the Privacy and Electronic Communications (EC Directive) Regulations 2003 (PECR), businesses making direct marketing calls to the UK must:
- State who is calling (organization name)
- Display a traceable telephone number
- Provide contact details if asked

It is unlawful to call numbers registered with TPS or the Corporate TPS (CTPS), or anyone who has previously objected to your calls. The only exception is where the individual has consented to receive marketing calls from your organization. Lists must be cleaned against TPS/CTPS/FPS registers before making unsolicited calls. Data should be cleaned as frequently as possible to ensure anyone on the register 28+ days is not contacted.

Enforcement is by the Information Commissioner's Office (ICO). A TPS license is required to screen the register; see [TPS pricing](https://corporate.tpsonline.org.uk/prices).
