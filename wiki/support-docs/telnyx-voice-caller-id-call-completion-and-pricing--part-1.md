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

*Part 1 of 5 — see also: [Part 2](telnyx-voice-caller-id-call-completion-and-pricing--part-2.md), [Part 3](telnyx-voice-caller-id-call-completion-and-pricing--part-3.md), [Part 4](telnyx-voice-caller-id-call-completion-and-pricing--part-4.md), [Part 5](telnyx-voice-caller-id-call-completion-and-pricing--part-5.md)*

A consolidated reference for Telnyx voice services covering Caller ID Number (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing and billing, LRN and number lookup, US local and rural call completion, PSTN replacement and local calling, and troubleshooting inbound and outbound call failures.

## Caller ID Number (CID) and Caller ID Name (CNAM)

Telnyx distinguishes between two related but separate services: **Caller ID Number (CID)** and **Caller ID Name (CNAM)**. CID displays the calling party's phone number on the device of the person being called, while CNAM displays the name associated with that number. Both can be configured for inbound and outbound calls, and each behaves differently depending on the country.

### Inbound Caller ID Number

By default, Telnyx provides the CLI (Calling Line Identification) number for all calls received on a Telnyx number. Once a number is provisioned, the caller ID number is automatically included on inbound calls sent to your connection.

### Inbound Caller ID Name (CNAM Lookup)

Inbound CNAM allows the name of the calling party to appear on your phone when receiving calls. When enabled on a DID, Telnyx dips the CNAM databases to determine whether a name is associated with the caller's number and, if so, passes that name in the SIP INVITE to your connection.

To enable inbound CNAM:

1. In the Mission Control Portal, go to **Real-Time Communications → My Numbers**.
2. On the number you want to enable, click the business card icon.
3. In the **CNAM Caller ID Lookup** section, toggle the option on.
4. Accept the MRC (Monthly Recurring Charge) and click **Save Changes**.

Standard pricing for inbound caller ID name is **$0.40/mo per number**, subject to change.

### Outbound Caller ID Number

When placing an outbound call through Mission Control, Telnyx passes the caller ID number you send with the call. If no CLI is provided, the call goes through with "anonymous" displayed to the receiving party.

You can configure a **Caller ID Override** at the connection level so that a default outbound CLI is applied even when one is not supplied per call. To configure it:

1. Go to **Real-Time Communications → Voice → SIP Trunking** and click the pencil icon next to the SIP Connection/Trunk.
2. Open the **Outbound** sub-tab.
3. Enter the desired number in the **Caller ID Override** field.
4. Choose when the override applies: **Always**, **Normal Only**, or **Emergency Only**.
5. Select the **Localization Country** — this sets the international exit code and restricts national dialing to that country.
6. Optionally configure **Channel Limit** (caps total outbound calls from the connection) and **Expert Settings** (e.g., Ringback).
7. Save the changes.

### Outbound Caller ID Name (CNAM Listing)

Outbound CNAM Listing registers a Caller ID Name for a number so that the receiving party sees your chosen name. To set it up, edit the number's settings, enable **CNAM Listing**, and enter your 15-character Caller ID Name. Outbound CNAM listing is free.

Toll-free numbers do not support CNAM — the checkbox is greyed out for them.

### CNAM in the USA vs Canada

- **USA**: Several CNAM databases hold a record of every US number and its associated CNAM. When CNAM listing is enabled on a US number, the details are inserted into the relevant database. When a call is placed between two US numbers, the receiving carrier queries a database to retrieve the CNAM and passes it to the called party.
- **Canada**: There is no national CNAM database. Instead, CNAM information is passed in the SIP headers `FROM` and `P-ASSERTED-IDENTITY`.

### CNAM Propagation and Limitations

- For Telnyx-owned numbers, CNAM values are typically pushed to the database within **12–24 hours**, but can take up to **72 hours**.
- For numbers belonging to underlying carriers, propagation can take **3–5 working days**.
- CNAM supports up to **15 alphanumeric characters and blank spaces**.
- CNAM is not supported on toll-free or international numbers. Toll-free numbers do not participate in the CNAM registry or database. Some receiving carriers may maintain private databases to pass CNAM, but this is not guaranteed. The best alternative is to use the `FROM`/`PAID` SIP headers to include your own display name, though this may not always be passed through. Branded calling is an emerging solution that carriers are beginning to implement to guarantee the displayed name.
- Display of CNAM is ultimately up to the receiving carrier and the called party's subscription. If the subscriber has not enabled CNAM display with their carrier, your CNAM may not appear. By default, destination carriers may display the rate center or locality of the caller's number when no CNAM is found.
- The industry-wide CNAM service is generally not used by wireless carriers. When dialing a mobile device, your CNAM may not display unless the subscriber has saved your name as a contact.

You can use the [Your Number Lookup Guide](your-number-lookup-guide.md) tool from your account to verify when the CNAM listing has been updated on a number.
