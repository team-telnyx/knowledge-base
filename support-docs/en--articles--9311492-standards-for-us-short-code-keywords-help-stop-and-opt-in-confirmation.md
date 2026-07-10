---
source_url: https://support.telnyx.com/en/articles/9311492-standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation
scraped: 2026-07-08
content_hash: 489d2501cf9bb0fd262d8c86074600bc5ad0da6e389742c399d7e817089208b9
---

Standards for US Short Code Keywords: HELP, STOP, and Opt-In Confirmation | Telnyx Help Center

[Skip to main content](#main-content)

# Standards for US Short Code Keywords: HELP, STOP, and Opt-In Confirmation

Managing Autoresponses for US Short Codes. Start building on Telnyx today.

K

Written by Klane Pedrie

June 26, 2024

Table of contents

# Standards for US Short Code Keywords

All US-based Telnyx short codes are required to respond appropriately to the HELP and STOP keywords, regardless of the sender's subscription status. This guide outlines the response obligations and industry norms for US-based short codes, and includes some examples.

## Introduction

According to the Telnyx [Acceptable Use Policy](https://telnyx.com/acceptable-use-policy), your company is obligated to adhere to carrier regulatory requirements, industry standards, and relevant laws. To meet industry standards, your US short code is required to acknowledge HELP and STOP keywords. Any user who opts out using the STOP keyword must be placed on a block list, prohibiting any further messages unless they choose to opt back in. Detailed industry standards for handling HELP and STOP keywords for US short codes are available in the [CTIA Short Code Monitoring Handbook](https://www.wmcglobal.com/us-resources).

### Administering Opt-Out Demands

You must let subscribers opt-out from receiving text messages from your short code by any legitimate means. One method for users to opt out of your campaign is by texting STOP, or equivalent keywords such as END, CANCEL, UNSUBSCRIBE, and QUIT to your short code.

When a user sends one of these keywords to your short code, your application must process this request and maintain the opt-out list. This allows your short code application to independently manage subscription lists and handle requests from users wishing to re-subscribe. If you need guidance on how to implement this with your short code, please contact your account manager.

**STOP Message**  
It's required by industry standards to send a compliant response whenever an end user texts STOP or similar keywords to your short code, regardless of whether they were previously subscribed.

Example:

Recipient message: STOP, END, QUIT, CANCEL, or UNSUBSCRIBE  
Short code response: You are unsubscribed from {Campaign Name} {Description} Alerts. No more messages will be sent. Reply HELP for help or {toll-free number}.

**HELP Messages**  
A compliant response is also necessary whenever recipients text HELP to your short code, regardless of their subscription status.

Example:

Recipient message: HELP  
Short code response: {Campaign Name} {Description} Alerts: Help available at {source of help #1} or {toll-free number}. Msg&data rates may apply. {Message frequency}. Text STOP to cancel.

**Important Notes**

* The "description" should succinctly define the type of alerts, e.g., "Account Alerts," "News Alerts," "Promo Alerts."
* The help source MUST be either a Toll-Free phone number or a support email address. Other forms of help are permissible, but one of these options is required at a minimum.
* The message frequency must be specific, e.g., "1 message per day," "4 messages per month," "2 messages per transaction." Alternatively, "Message frequency varies" is also acceptable.

### Regulatory Compliance and Audits

The standards outlined here adhere to industry norms as detailed in the CTIA Short Code Monitoring Handbook. You should anticipate that your short code initiative may be reviewed for compliance by a carrier or regulatory body at some stage.

Typically, U.S. short code initiatives undergo scrutiny to ensure they meet the compliance guidelines stipulated in the CTIA handbook. Moreover, it's crucial to understand that carriers have the discretion to terminate short code services for any user without notice.

Therefore, compliance with these standards does not fully safeguard against potential service interruption. Additionally, your text messaging campaign might be subject to further regulatory obligations under U.S. legislation, such as the Telephone Consumers Protection Act of 1991 (TCPA), depending on its nature.

These legal stipulations could require you to offer more comprehensive opt-out mechanisms than a mere STOP reply. It is advisable to seek guidance from your legal advisors to ensure your procedures conform to all relevant laws and industry practices.

For more questions please email us at [shortcode@telnyx.com](mailto:shortcode@telnyx.com)!

---

Related Articles

[SMS Opt-Out Keywords and Stop Words](https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words)[Messaging - 10DLC Campaign Checklist](https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist)[Regulatory Guidelines for US Short Code Marketing and Opt-in Procedures](https://support.telnyx.com/en/articles/9311566-regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures)[US Short Code Ordering Process](https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process)[Forbidden Messaging Use Cases in the US and Canada (10DLC, Toll-Free, and Short Code)](https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code)

Did this answer your question?

😞😐😃

Table of contents
