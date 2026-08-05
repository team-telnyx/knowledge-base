---
title: Caller ID, CNAM, and Branded Calling on Telnyx
summary: A consolidated reference covering how Telnyx handles Caller ID Number (CID),
  Caller ID Name (CNAM), Branded Calling, CLI/CLD validation, and related call-completion
  troubleshooting. It explains the differences between inbound and outbound CID and
  CNAM, how to configure each in Mission Control Portal, regional behavior in the
  US and Canada, supported number formats, anonymization, international spoofing restrictions,
  branded calling setup and limitations, and how to mitigate spam-likely flags and
  SIP errors.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
updated_at: 2026-08-05T13:31:03Z
---

# Caller ID, CNAM, and Branded Calling on Telnyx

*Part 1 of 5 — see also: [Part 2](caller-id-cnam-and-branded-calling-on-telnyx--part-2.md), [Part 3](caller-id-cnam-and-branded-calling-on-telnyx--part-3.md), [Part 4](caller-id-cnam-and-branded-calling-on-telnyx--part-4.md), [Part 5](caller-id-cnam-and-branded-calling-on-telnyx--part-5.md)*

A consolidated reference covering how Telnyx handles Caller ID Number (CID), Caller ID Name (CNAM), Branded Calling, CLI/CLD validation, and related call-completion troubleshooting. It explains the differences between inbound and outbound CID and CNAM, how to configure each in Mission Control Portal, regional behavior in the US and Canada, supported number formats, anonymization, international spoofing restrictions, branded calling setup and limitations, and how to mitigate spam-likely flags and SIP errors.

## Overview of Caller ID Concepts

Telnyx distinguishes between two related but separate pieces of identity information that travel with a phone call:

- **Caller ID Number (CID)** — the phone number displayed on the device of the person being called on an outbound call.
- **Caller ID Name (CNAM)** — the name associated with the calling number that is displayed on the device of the person being called on an outbound call.

A third layer, **Branded Calling**, extends standard caller ID by attaching verified business identity (display name, call reason, logo, business identifiers) to outbound SIP trunking calls using STIR/SHAKEN-based signaling.

## Inbound Caller ID

### Inbound Caller ID Number

By default, Telnyx provides the Calling Line Identification (CLI) number for all calls received on a Telnyx number. Once a number is provisioned, the caller ID number is automatically included on inbound calls sent to your connection.

### Inbound Caller ID Name (CNAM Lookup)

Enabling this feature on a DID instructs Telnyx to DIP the CNAM databases to determine whether a name is associated with the caller's number. If a name is found, it is passed along in the SIP INVITE to your connection.

To configure inbound CNAM lookup:

1. In Mission Control Portal, open the **Numbers** section under **Real-Time Communications** and locate the number you want to configure.
2. Click the business card icon on the number.
3. In the **CNAM Caller ID Lookup** section, toggle the option to enable the setting.
4. Accept the Monthly Recurring Charge (MRC) and click **Save changes**.

Standard pricing for inbound caller ID name is $0.40/mo per number, subject to change.

## Outbound Caller ID

### Outbound Caller ID Number

When placing an outbound call through Mission Control, Telnyx passes the caller ID number supplied with the call. Whatever CLI is sent is shown to the receiving party. If no CLI is provided, the call goes through with "anonymous" displayed.

Telnyx also supports a **Caller ID Override** at the connection level, which sets a default outbound caller ID number for all calls on a particular connection. This ensures that even if no CLI is provided on a given call, Telnyx sets the CLI to the configured override number.

To configure outbound Caller ID Override:

1. Under **Real-Time Communications**, click **SIP Trunking** under the **Voice** section, then click the **Pencil** icon next to the SIP Connection/Trunk you want to edit.
2. Select the **Outbound** sub-tab.
3. In the **Caller ID Override** field, enter the number you want displayed as your CLI.
4. Choose **Always**, **Normal Only**, or **Emergency Only** as preferred.
5. Select the **Localization Country** — this lets the caller use the international exit code of the chosen country and restricts national dialing to that country.
6. Optionally enable **Channel Limit** to cap the total number of outbound calls from the connection.
7. Optionally enable **Expert Settings** (for example, Ringback).
8. Save the changes.

### Outbound Caller ID Name (CNAM Listing)

Outbound Caller ID Name, also called CNAM or CNAM Listing, displays your caller ID name to the receiving party. To register CNAM, edit the number's settings, enable **CNAM Listing**, and enter a 15-character Caller ID Name. Toll-free numbers do not support CNAM, so the checkbox is greyed out for them. Outbound CNAM listing is free.

### CNAM in the USA vs Canada

- **USA** — Several CNAM databases hold a record of every US number and its associated CNAM. When CNAM listing is enabled on a US number, the CNAM details are inserted into the relevant database. When a call is placed between two US numbers, the receiving carrier checks one of the databases to retrieve the CNAM and passes it along to the called party.
- **Canada** — There is no national CNAM database. CNAM information is passed in the SIP headers `FROM` and `P-ASSERTED-IDENTITY`.

### CNAM Special Notes

- When enabling CNAM Listing on Telnyx-owned numbers, CNAM values are typically pushed to the database within 12–24 hours but can take up to 72 hours.
- CNAM supports up to 15 alphanumeric characters and blank spaces.
- CNAM is not currently supported on toll-free or international numbers. Toll-free numbers do not participate in the CNAM registry or database. Some receiving carriers may maintain private databases to pass CNAM info, but this is not guaranteed. The best alternative is to use the `FROM`/`PAID` SIP headers to include your own display name, although this may or may not be passed all the way through. Branded calling is an emerging solution that carriers are beginning to implement to help guarantee the displayed name.
- When enabling CNAM Listing on numbers belonging to underlying carriers, processing to industry databases can take 3–5 working days.
- Display of CNAM is up to the receiving carrier. If subscribers have not enabled this service with their carriers, your CNAM may not display. By default, destination carriers may display the rate center or locality of the caller's number when no CNAM value is found.
- The industry-wide CNAM service is not generally used by wireless carriers. If you dial a wireless/mobile device, your CNAM may not display unless the subscriber has saved the name as a contact in their phonebook.

You can use the [Your Number Lookup Guide](your-number-lookup-guide.md) tool from your account to verify when the CNAM listing has been updated on your number.
