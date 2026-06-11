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
