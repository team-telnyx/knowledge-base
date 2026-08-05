---
title: Porting Numbers to Telnyx and Microsoft Teams Integration
summary: This page covers how to find a porting PIN or passcode from common carriers,
  port numbers away from specific providers (Twilio, voip.ms, Microsoft Teams) into
  Telnyx, and configure Microsoft Teams with Telnyx using Direct Routing, Operator
  Connect, or Call2Teams, including emergency call routing.
sources:
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
- url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
- url: https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms
- url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
- url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
- url: https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams
- url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
updated_at: 2026-08-05T13:34:20Z
---

# Porting Numbers to Telnyx and Microsoft Teams Integration

*Part 2 of 6 — see also: [Part 1](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-1.md), [Part 3](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-3.md), [Part 4](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-4.md), [Part 5](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-5.md), [Part 6](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-6.md)*

This page covers how to find a porting PIN or passcode from common carriers, port numbers away from specific providers (Twilio, voip.ms, Microsoft Teams) into Telnyx, and configure Microsoft Teams with Telnyx using Direct Routing, Operator Connect, or Call2Teams, including emergency call routing.

## Porting Microsoft Teams Numbers to Telnyx

To port your VoIP, Google Voice, or Skype number to Telnyx, submit a port request. See [Port numbers to Telnyx](port-numbers-to-telnyx.md).

### Porting from Microsoft Teams

1. Ensure that you have set a porting PIN in the Microsoft Teams admin center.
2. To set a porting PIN, in the left navigation of the **Microsoft Teams admin center**, go to **Voice** > **Phone numbers**, on the upper-right corner of the page, select **Manage porting PIN**, and then enter a 10-digit PIN.

Once you have set a porting PIN, proceed with submitting a port-in request to Telnyx.

### Information to Use in the Port Request

- **Account number** — If you do not have an account number, you can use one of the numbers you are looking to port as the account number.
- **Billing Telephone Number (BTN)** — If you do not have a BTN, you can use one of the numbers you are looking to port as the account number.

In the comments section of the port-in request to Telnyx, add a comment stating: "PIN is [10-digit PIN]". For example, if your porting PIN is 1234567890, add a comment "PIN is 1234567890".

### Time for Approval

Once the request is submitted to MS Teams along with the PIN, the port will most of the time be automatically approved to Telnyx and FOC (Firm Order Commitment) for porting will be received immediately. Porting from Microsoft Teams can be done in as little as 1 business day, depending on who the underlying provider of the number is.

### Microsoft Calling Plan for Teams

For numbers being ported in from Microsoft's Calling Plan for Teams, if the customer wishes for the number to be assigned to Operator Connect, the customer should open a ticket with Telnyx so that Telnyx can open one with Microsoft to have Microsoft port the number over to Operator Connect. Otherwise, Microsoft will not allow the number to be added to Operator Connect.

Details needed from the customer to open a ticket with Microsoft:

- ID of the external connection the number should be assigned to
- Numbers which the customer wants migrated over
- Whether they want the number as "Calling User Assignment" or "First Party App Assignment"
