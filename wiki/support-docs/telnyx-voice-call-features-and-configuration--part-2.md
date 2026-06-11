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

*Part 2 of 4 — see also: [Part 1](telnyx-voice-call-features-and-configuration--part-1.md), [Part 3](telnyx-voice-call-features-and-configuration--part-3.md), [Part 4](telnyx-voice-call-features-and-configuration--part-4.md)*

A comprehensive guide to Telnyx voice calling features including Caller ID, call forwarding, voicemail, call screening, branded calling, HD Voice, noise suppression, and troubleshooting for both inbound and outbound calls.

## Voicemail

Telnyx Voicemail forwards missed or rejected calls to a voicemail box. You can access messages by dialing `*98` from a voicemail-enabled number (set that number as your Caller ID first) and authenticating with a PIN.

> ⚠️ Voicemail should only be enabled on numbers assigned to SIP Connections.

To set up voicemail:

1. Go to **My Numbers** in the Numbers section.
2. Filter for the number and click the pencil icon.
3. Click the **Voice** sub-tab.
4. Scroll to the Voicemail section and toggle it on.
5. Set your PIN and save.

**Webhook event:** If a webhook URL is set on your SIP Connection, a `calls.voicemail.completed` event is delivered with details including the recording URL.

**Limitations:**
- Custom voicemail greeting messages are not currently supported.
- Email notifications upon voicemail deposit are not currently supported.

You can also manage voicemail programmatically via the [Voicemail API](https://developers.telnyx.com/api/voicemail/get-voicemail).

## Inbound Call Screening

Inbound Call Screening protects Telnyx numbers from unwanted and spam calls. It is free to use.

To configure:
1. Navigate to **My Numbers**, select a number, and click **Edit**.
2. Under the **Voice** tab, check **Enable Inbound Call Screening**.
3. Choose a screening mode:
   - **Flag Calls:** Suspicious calls are allowed through but labeled. The From/P-Asserted-ID name field displays "SPAM LIKELY", a custom SIP header `X-Telnyx-Call-Screening: SPAM LIKELY` is added, and the `call.initiated` webhook includes `call_screening_result` with value `spam_likely`.
   - **Reject Calls:** Suspicious calls are blocked at the network level and never reach your servers.
4. Save settings.

Call screening uses three factors:
- **Number Reputation Database:** Aggregates data from Nomorobo, YouMail, and CallerAPI to classify potential spammers.
- **Number Validation:** Analyzes the validity and existence of originating numbers.
- **SHAKEN/STIR Attestation:** Calls with Attestation C (originating carrier cannot authenticate the Caller ID) or Invalid attestation are flagged or rejected.

Inbound Call Screening currently applies to calls originating from the US or Canada for number reputation screening, and from North America for SHAKEN/STIR attestation screening. To maximize benefits, ensure webhooks are enabled on your SIP Connection.

## Branded Calling

Branded Calling displays verified brand information (business name, logo, call reason) on eligible receiving devices for outbound SIP trunking calls. It builds on STIR/SHAKEN by adding identity fields such as display name, call reason, logo, and business identifiers to call signaling.

> Branded Calling currently applies to US-to-US calls placed to US mobile numbers serviced by T-Mobile and Verizon only.

### Setup steps

1. Sign in to [Mission Control Portal](https://portal.telnyx.com/).
2. Navigate to **Other Products → Branded Calling**.
3. Accept the Branded Calling terms.
4. Create or select an **Enterprise** profile with your business information.
5. Create a **Display Identity Record (DIR)** under the Enterprise with display name, logo, call reasons, and business details.
6. Submit the DIR for review.
7. Wait for approval status updates in the portal.
8. After approval, add eligible Telnyx phone numbers to the DIR.
9. Place outbound calls from approved numbers through your SIP connection — no additional SIP headers or configuration changes are required.

### Why Branded Calling may not appear on every call

Approval means eligibility, not guaranteed display. Display depends on:
- Receiving carrier support (not all carriers have implemented the infrastructure)
- Device support (older devices may not render branded content)
- Network path differences (intermediate carriers may strip identity fields)
- Provisioning and propagation delays
- Destination and carrier limitations (landlines, international numbers, and smaller carriers are unlikely to display branded info)

A phone number can only be associated with one approved DIR at a time. Changes to an approved DIR (display name, logo, call reasons) may require another review.

## HD Voice

HD Voice enhances audio quality on PSTN calls using wideband codecs (OPUS, G.722, AMR-WB) instead of traditional narrowband codecs like G.711. HD Voice is free (no MRC as of July 2025).

### Conditions for HD Voice

- The call must involve a supported carrier: US (AT&T, T-Mobile, Verizon), Germany (Outbox), Austria (Yuutel), Australia (all major carriers).
- The called/calling mobile device must support wideband codecs and be on at least 4G/LTE.
- Your SIP connection must have a wideband codec enabled (OPUS, G.722, or AMR-WB) in the Inbound Expert Settings.
- The SIP device must support the selected codec.

For inbound HD Voice, the incoming call must originate from a supported carrier on an AMR-WB-enabled device in 4G/LTE coverage, the Telnyx number must have HD Voice enabled (in Number Voice settings), and the SIP connection must use a wideband codec.

For outbound HD Voice, the SIP device must use a wideband codec, the destination must be on a supported carrier with an AMR-WB-enabled device in 4G/LTE, and the Telnyx number (including CLI override) must have HD Voice enabled.

HD Voice is currently supported on +1 US longcode numbers (some area codes excluded). International, toll-free, and certain +1 US numbers may not be supported. You can search for HD-Voice-capable numbers in the Buy Numbers section.

If a codec mismatch occurs between two HD codecs, audio quality remains HD. If the mismatch is between an HD and non-HD codec, the call is transcoded and audio will not be HD. No interruptions occur during negotiation.

## Noise Suppression

Noise Suppression removes background noise, isolates the primary speaker, or both — improving audio for human listeners, speech-to-text transcription, and Voice AI Agent performance.

Setting Noise Suppression at the connection level affects all associated numbers and overrides per-number settings (recommended approach). Charges apply per direction, so selecting "Both" incurs charges for each direction separately.

### Configuration

1. In Mission Control Portal, navigate to **Voice → SIP Trunking**.
2. Select the SIP connection and open the **Configuration** tab.
3. Scroll to **Advanced** and find **Noise Suppression**.
4. Choose a model and direction.
5. Save.

You can also configure via API using the `noise_suppression` parameter or call `suppression_start` on an active call with a `noise_suppression_engine` value.

### Direction options

| Setting | Effect |
|---|---|
| **Inbound only** | Cleans audio entering the Telnyx network destined for the customer |
| **Outbound only** | Cleans audio leaving the Telnyx network from the customer |
| **Both** | Applies in both directions; billed per direction |
| **Disabled** | Turns the feature off |

### Model selection

| Model | Recommended use case |
|---|---|
| **Denoiser** | General-purpose, lightweight default |
| **Krisp Viva Tel Lite** | Standard SIP/telephony, contact centers, IVR |
| **Krisp Viva Pro** | WebRTC and browser-based calls, multi-talk scenarios |
| **Krisp Viva SS** | Smart speakers, conference rooms, far-field microphones |
| **AIcoustics Rook Small** | AI assistant calls, reverberation removal |
| **AIcoustics Rook Large** | Demanding acoustic conditions, high-value AI calls |
| **AIcoustics Quail Voice Focus S** | STT pipelines, Voice AI agents, close-mic setups; preserves phonetic structure for transcription |
