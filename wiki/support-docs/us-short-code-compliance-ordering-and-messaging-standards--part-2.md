---
title: US Short Code Compliance, Ordering, and Messaging Standards
summary: This page consolidates Telnyx guidance on ordering US short codes, registering
  brands and content providers, complying with carrier and CTIA standards for HELP/STOP
  keywords and opt-in CTAs, and meeting short-code messaging requirements across subscription
  and one-off programs.
sources:
- url: https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process
- url: https://support.telnyx.com/en/articles/10245615-short-code-brand-and-content-provider-registration-process
- url: https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
- url: https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
- url: https://support.telnyx.com/en/articles/4967485-short-code-supported-carriers
- url: https://support.telnyx.com/en/articles/5724344-cisco-linksys-star-codes
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/9311492-standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation
- url: https://support.telnyx.com/en/articles/9311566-regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures
updated_at: 2026-08-05T13:24:16Z
---

# US Short Code Compliance, Ordering, and Messaging Standards

*Part 2 of 2 — see also: [Part 1](us-short-code-compliance-ordering-and-messaging-standards--part-1.md)*

This page consolidates Telnyx guidance on ordering US short codes, registering brands and content providers, complying with carrier and CTIA standards for HELP/STOP keywords and opt-in CTAs, and meeting short-code messaging requirements across subscription and one-off programs.

## HELP and STOP Keyword Standards

All US-based Telnyx short codes are required to respond appropriately to the HELP and STOP keywords, regardless of the sender's subscription status. This is required by the Telnyx [Acceptable Use Policy](https://telnyx.com/acceptable-use-policy) and aligns with the CTIA Short Code Monitoring Handbook.

### Administering Opt-Out Demands

Subscribers must be allowed to opt out from receiving text messages from a short code by any legitimate means. One method is by texting STOP, or equivalent keywords such as END, CANCEL, UNSUBSCRIBE, and QUIT to the short code. When a user sends one of these keywords, the application must process the request and maintain the opt-out list. This allows the short code application to independently manage subscription lists and handle requests from users wishing to re-subscribe.

**STOP Message** — A compliant response is required whenever an end user texts STOP or similar keywords, regardless of whether they were previously subscribed.

- Recipient message: STOP, END, QUIT, CANCEL, or UNSUBSCRIBE
- Short code response: *You are unsubscribed from {Campaign Name} {Description} Alerts. No more messages will be sent. Reply HELP for help or {toll-free number}.*

**HELP Message** — A compliant response is required whenever recipients text HELP, regardless of subscription status.

- Recipient message: HELP
- Short code response: *{Campaign Name} {Description} Alerts: Help available at {source of help #1} or {toll-free number}. Msg&data rates may apply. {Message frequency}. Text STOP to cancel.*

Important notes:

- The "description" should succinctly define the type of alerts, for example, "Account Alerts," "News Alerts," "Promo Alerts."
- The help source MUST be either a toll-free phone number or a support email address. Other forms of help are permissible, but one of these options is required at a minimum.
- The message frequency must be specific, for example, "1 message per day," "4 messages per month," "2 messages per transaction." Alternatively, "Message frequency varies" is also acceptable.

### Regulatory Compliance and Audits

The standards outlined adhere to industry norms as detailed in the CTIA Short Code Monitoring Handbook. Short code initiatives may be reviewed for compliance by a carrier or regulatory body at any stage. Carriers have the discretion to terminate short code services for any user without notice, so compliance does not fully safeguard against potential service interruption. Campaigns may also be subject to further regulatory obligations under U.S. legislation, such as the Telephone Consumers Protection Act of 1991 (TCPA), depending on their nature. Legal counsel should be consulted to ensure procedures conform to all relevant laws and industry practices.

## Marketing and Opt-In Procedures

To ensure a short code campaign meets Telnyx's expectations, as outlined in the [Acceptable Use Policy](https://telnyx.com/acceptable-use-policy), the company must adhere to carrier compliance mandates, industry benchmarks, and relevant laws.

Industry norms dictate that specific details must be included wherever the short code is promoted or when individuals opt in to receive short code messages. This includes any medium through which an individual provides their phone number to receive messages via a short code, such as paper forms or online platforms.

Promotions and opt-in forms are often referred to as Calls to Action, or CTAs. The phrasing of the CTA will differ based on the sign-up method, guiding users on how to subscribe to the campaign. When crafting a CTA, consult resources like the CTIA Short Code Monitoring Handbook and the MMA's Global Code of Conduct and Best Practices Guide.

For example, an SMS keyword Call to Action might be:

*Text {Keyword} to ##### to subscribe to alerts.*

Wherever the short code is advertised (online, in print, etc.), include the following mandatory information:

*Message and data rates may use. {Message frequency}. Text HELP to ##### for assistance. Text STOP to ##### to unsubscribe. For terms: {URL to SMS terms of service}. For privacy: {URL to privacy policy}*

Consider these points when drafting a Call to Action:

- Message frequency must be precise, such as "1 message/day" or "4 messages/month." If the frequency depends on user interaction, phrase it as "1 message/user request." For variable frequencies, "Message frequency varies" is permissible, but justification may be required.
- The privacy policy should be tailored to the text messaging campaign, detailing how data is managed. It should be accessible via the CTA and clearly marked.
- Link to the terms and conditions pertinent to the text messaging campaign within the CTA. These terms should clearly explain the operation of the campaign. Consult with legal counsel to ensure these documents contain all necessary legal notices.
- The word "STOP" should be emphasized in bold wherever it appears.
- The CTA may need additional language to comply with specific legal requirements depending on the campaign's nature.

Based on industry standards for short code services, be prepared for potential audits by carriers or regulatory bodies. U.S. short code campaigns frequently undergo such reviews according to the CTIA Short Code Monitoring Handbook. Carriers can suspend short code services at any time, so adhering to these guidelines does not guarantee uninterrupted service.

For more questions, email [shortcode@telnyx.com](mailto:shortcode@telnyx.com).

## Related Telnyx Resources

- [US Short Code Ordering Process](us-short-code-ordering-process.md)
- [Short Code Brand and Content Provider Registration Process](short-code-brand-and-content-provider-registration-process.md)
- [Short Code Compliance Quick Reference Guide](short-code-compliance-quick-reference-guide.md)
- [Standards for US Short Code Keywords: HELP, STOP, and Opt-In Confirmation](standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation.md)
- [Regulatory Guidelines for US Short Code Marketing and Opt-in Procedures](regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures.md)
- [Short Code - Supported Carriers](short-code-supported-carriers.md)
- [SMS Long Code Deliverability Best Practices](sms-long-code-deliverability-best-practices.md)
- [What are Short Duration Calls](what-are-short-duration-calls.md)
- [Limits on Concurrent Outbound Calls](limits-on-concurrent-outbound-calls.md)
- [Distinguish your outbound profiles & DIDs](distinguish-your-outbound-profiles-dids.md)
- [More About Outbound Voice Profiles](more-about-outbound-voice-profiles.md)
- [SIM Data Limits & Notifications](sim-data-limits-notifications.md)
- [International Coverage](international-coverage.md)
- [Cisco/Linksys Star Codes](cisco-linksys-star-codes.md)
- [Email Notification: International Spend Limit](email-notification-international-spend-limit.md)
