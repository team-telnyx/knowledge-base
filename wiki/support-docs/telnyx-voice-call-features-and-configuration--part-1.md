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
