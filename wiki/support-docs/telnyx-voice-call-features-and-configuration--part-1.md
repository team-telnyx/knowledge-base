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

*Part 1 of 4 — see also: [Part 2](telnyx-voice-call-features-and-configuration--part-2.md), [Part 3](telnyx-voice-call-features-and-configuration--part-3.md), [Part 4](telnyx-voice-call-features-and-configuration--part-4.md)*

A comprehensive guide to Telnyx voice calling features including Caller ID, call forwarding, voicemail, call screening, branded calling, HD Voice, noise suppression, and troubleshooting for both inbound and outbound calls.

## Caller ID (CID) and Caller ID Name (CNAM)

There are two types of Caller ID: **Caller ID Number (CID)** and **Caller ID Name (CNAM)**. CID displays your phone number to the called party on outgoing calls. CNAM displays the name associated with your phone number to the called party on outgoing calls.

### Inbound Caller ID Number

By default, Telnyx provides the Calling Line Identification (CLI) number for all inbound calls received on a Telnyx number. The caller ID number is automatically included with inbound calls once a number is provisioned.

### Inbound Caller ID Name

Inbound CNAM lets you see the name of the person calling you. When enabled on a DID, Telnyx dips CNAM databases to determine if a name is associated with the caller's number and passes it in SIP INVITEs to your connection.

To enable inbound CNAM:

1. In the [numbers section](https://portal.telnyx.com/#/app/numbers/my-numbers) of Mission Control Portal, click the business card icon on the desired number.
2. Find **CNAM Caller ID Lookup** and toggle it on.
3. Accept the monthly recurring charge (MRC) and save changes.

Standard pricing for inbound caller ID name is approximately $0.40/mo per number (subject to change).

### Outbound Caller ID Number

When placing an outbound call, Telnyx passes the CLI you send with the call. If you do not provide a CLI, the call displays as "anonymous" to the receiving party. You can set a **Caller ID Override** at the connection level to ensure a default outbound caller ID number:

1. Navigate to **Voice → SIP Trunking** and click the pencil icon on the relevant SIP Connection.
2. Select the **Outbound** sub-tab.
3. Enter the desired number in the **Caller ID Override** field.
4. Choose "Always", "Normal Only", or "Emergency Only".
5. Optionally set **Localization Country** (allows international exit code usage and restricts national dialing), **Channel Limit**, and **Expert Settings**.
6. Save changes.

International caller ID spoofing is not supported; calls with spoofed international CLI will be rejected (typically with a 503 error).

### Outbound Caller ID Name (CNAM Listing)

Outbound CNAM lets you register a Caller ID Name for your number. To set it up, edit the number's settings, enable **CNAM Listing**, and type in your 15-character Caller ID Name. Toll-free numbers do not support CNAM (the checkbox is greyed out). Outbound CNAM listing is free.

**USA:** CNAM details are inserted into relevant CNAM databases. When a call is placed, the receiving carrier checks a database and passes the CNAM to the called party.

**Canada:** There is no national CNAM database. CNAM information is passed in the `FROM` and `P-ASSERTED-IDENTITY` SIP headers.

**Important notes:**
- CNAM values on Telnyx-owned numbers typically push to the database within 12–24 hours but can take up to 72 hours. Numbers belonging to underlying carriers can take 3–5 working days.
- CNAM supports up to 15 alphanumeric characters and blank spaces.
- CNAM is not supported on toll-free or international numbers.
- Wireless carriers generally do not use the industry-wide CNAM service, so CNAM may not display on mobile devices.
- Display of CNAM ultimately depends on the receiving carrier. Use the [Your Number Lookup Guide](your-number-lookup-guide.md) to verify when CNAM has been updated.
- For international numbers, the best option is to use `FROM`/`PAID` SIP headers with a display name, though this is not guaranteed to pass through.

## Call Forwarding

Call Forwarding on a Telnyx number can forward calls either always or only on failure to establish a call to the associated SIP Connection.

To enable call forwarding:

1. Click the handset icon under the services column on the number.
2. In the Voice sub-tab, scroll to the forwarding section and toggle it on.
3. Enter the forwarding destination number.
4. Choose the mode:
   - **Always:** Bypasses the primary SIP connection entirely. All incoming calls are unconditionally forwarded.
   - **On-Failure:** Triggered only when the call cannot be connected. Triggers include:
     - Unregistered PBX or endpoint (offline due to outage, power failure, or misconfiguration)
     - Active Do Not Disturb (DND) on the receiving device
     - Manually declined calls
     - **Not triggered** by unanswered calls that successfully reach an active endpoint
5. Save changes and accept the MRC.

To disable, toggle off the forwarding setting and save.

**Important notes:**
- Forwarding a Telnyx number to another Telnyx number is considered off-net and charged per your outbound rate deck.
- Per-minute charges apply for both the inbound and forwarded outbound legs (unless the inbound number uses channel billing).
- Call forwarding cannot be enabled on numbers assigned to voice or fax applications — only SIP Connections. To forward numbers on Call Control or TeXML applications, use programmatic methods (TeXML `<Number>` or Voice API `answer` + `transfer` commands).
- In some countries (e.g., Venezuela), local regulations may prevent forwarding of calls with a local CLI originating from outside the country.

## External Call Transfers

When your SIP endpoint receives an inbound call via Telnyx and transfers it to an external number while keeping the original PSTN number as the originator, Telnyx treats this as two separate calls. The transferred (outbound) call is validated to ensure it is tied to the original inbound call.

Telnyx performs two validations:
1. **Active inbound call match** — confirms an active inbound call exists from the original caller (A) to your Telnyx number (B).
2. **Diversion header** — the outbound call from A to C must include a SIP Diversion header showing B.

If validation fails, the transfer is rejected with `403 Unverified origination number D51`.

**Programmatic Voice methods that support external transfers:**
- **Voice API Transfer command** — transfers an established inbound call; non-Telnyx origination number is allowed.
- **Voice API Dial + Bridge** — a Dial request with `link_to` set to the `call_control_id` of the bridging call and `bridge_intent` set to `true`.
- **TeXML `<Dial>`** — places a new outbound call and connects it to the existing inbound call; non-Telnyx origination number is allowed.

## Conference Calls

Telnyx supports conference calls through multiple methods:

- **Voice API (recommended):** Build and control conference calls programmatically using the [Conference commands API](https://developers.telnyx.com/api-reference/conference-commands).
- **TeXML:** Create simple conference rooms using the `<Conference>` verb ([TeXML Conference docs](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference)).
- **SIP trunking:** Use Telnyx with PBX systems like Asterisk or 3CX.
- **Video API:** Build audio/video conferencing apps.

For a working example, follow the [conferencing demo tutorial](https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo). For simple setups, start with TeXML `<Conference>`; for full control, use the Voice API.
