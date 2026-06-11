---
source_url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
scraped: 2026-06-11
---

Best Practices for Contacting Support | Telnyx Help Center

[Skip to main content](#main-content)

# Best Practices for Contacting Support

Get 24/7 international support and learn how to report call, messaging, portal, and API concerns with our efficient contact methods.

Written by Dillin

June 4, 2025

Table of contents

# How to Contact Telnyx Network Operation Center

**Chat:** click the "chat with us" link on the bottom of the left menu when signed into the Portal and the chat window will appear on the bottom right of the Mission Control Portal.  
​**Phone:** at +18889809750 or any of the international numbers listed below.

**Ticket:** Email us at [support@telnyx.com](mailto:support@telnyx.com).

At the beginning of your chat or email conversation, you will be provided a ticket number. If you wish to reference a previous chat or open ticket, please provide the ticket number that was given to you at the time of your conversation so that we can pick up right where we left off.

## When to Contact NOC

**Hours:** Always open 24 hours per day, 7 days a week, 365 days per year.

We are the team to reach out to whenever you have questions about call or message failures, the API, or other concerns regarding your account. In order for us to assist you as accurately as possible, it is important that you provide as many details as you can when you initially report your problem.

---

## Reporting Call or Message Failures

While the NOC is always happy to troubleshoot an issue with you, we do require some information in order to best assist you. For example, if you are reporting an issue when calling or messaging a specific destination, we will need to look at our logs to determine why this issue is taking place. In order for us to find the relevant entry in our logs, we will need a specific call or message example from you.

The best way to provide a call example is with a Call ID (SIP Call ID, Unique CDR ID or Call UUID) or MDR ID, which can be found in a [call detail request](https://portal.telnyx.com/#/app/reporting/detail-requests) generated within the Reporting section of your Portal. Alternatively, we always welcome the below information, which will allow us to identify the call or message:

### Call Example:

**SIP Connection Name & ID:** Name and ID of SIP Connection which can be found in the SIP Connection settings.

**Direction**: Inbound or Outbound  
​**CLI**: Source number  
​**CLD**: Destination number  
​**Date+Time**: Including timezone

### Messaging Example:

**Messaging Profile Name & ID:** Name and ID of the Messaging Profile which can be found in the messaging profiles settings.   
​**Direction:** Inbound / Outbound.  
​**From number / Alphanumeric Sender ID:** The senders number or name.  
​**To number:** The receivers number.  
​**Date Timestamp:** Including timezone.  
​**Error Code:** Found in the response but can be referenced [here](https://developers.telnyx.com/api/errors).

Telnyx NOC can troubleshoot most call quality or messaging issues up to 72 hours since occurrence, however should an escalation with any carrier partners be required -examples within 48 hours is necessary.

If the issue is not reproducible, examples within 24 hours to continue any escalations is required.

---

## Reporting API Issues

Unexpected API responses can be rather tricky to diagnose. The simplest way to report API issues is to send us as much of the following information as possible:  
​  
​**Issue:** The encountered issue in a few words, and the expected behavior from the endpoint(s).  
​**Endpoint(s):** The exact public URL endpoints you are sending requests to.  
​**Timestamp with timezone:** Preferably within the last 24 hours.  
​**Request:** The payload of the request you are sending.  
​**Response:** The payload of the response you are receiving from our API.  
​**Can you replicate the issue:** Yes/No

You can try the request [here](https://developers.telnyx.com). Additional information, such as explaining what function you were attempting to perform with your API request is also greatly appreciated. We require this information as API related issues are more complex than other products. The more information that’s provided, the easier we locate the root problem. Additionally, you are always welcome to reference [our error documentation](https://developers.telnyx.com/api/errors) to determine the source of the error you encountered.

---

## Reporting Portal Issues

If you experience an issue in the Portal, such as an unfamiliar error message, a screenshot of the error itself would always be appreciated. Alternatively, you can access the console window by using the “Inspect Element” tool in your browser. This is usually accessed by pressing F12 or right clicking in your browser and selecting “Inspect Element”.

You can attach a screenshot to an open Intercom chat by clicking the paperclip icon on the right-hand side of the chat window. You are also welcome to email us a screenshot at [support@telnyx.com](mailto:support@telnyx.com).

If it is not possible for you to capture a screenshot, we would love a description of what you were trying to do in the Portal and how that compares to what you experienced. For example, information such as the URL of the page you are on, error messages you received, buttons you have clicked, text-boxes you have filled out, etc. are all very helpful in understanding the issue.

For more information read our bug reports process [here](https://support.telnyx.com/en/articles/4283906-bug-reports-guide).

---

## International Support Numbers

If you have any other questions, please don’t hesitate to ask. The NOC can be reached by chat (by clicking the chat icon in the bottom right-hand side of the Portal), by email at [support@telnyx.com](mailto:support@telnyx.com), or by phone at:

* Estonia: +3726991435
* Finland: +358753255300
* Ireland: +353818123457
* Israel: +972772200092
* Mexico: +525588974917
* Netherlands: +31853018256
* New Zealand: +6498844134
* Philippines: +63322346319
* Poland: +48221530079
* Singapore: +6531594436
* United Kingdom: +443301900175
* United States & Canada: +18889809750

---

## NOTES ABOUT CONTACTING NOC SUPPORT

We receive feedback now and again where customer emails received at [support@telnyx.com](mailto:support@telnyx.com) go to spam. Based on our review, email providers are becoming more strict where domains without properly configured SPF / DMARC records are getting marked as spam.

There are other reasons where this can occur:

1. **Email content**: Spam filters are designed to identify and block emails that contain certain keywords, phrases, or types of content that are commonly associated with spam. If your emails contain any of these elements, they may be more likely to end up in the spam folder.
2. **Sender reputation**: Many email providers consider the reputation of the sender when deciding whether to deliver an email to the inbox or spam folder. If the sender's domain or IP address has a history of sending spam, then their emails may be more likely to be flagged as spam.
3. **User behaviour**: Spam filters also take into account how users interact with emails. If a large number of users mark an email as spam or delete it without opening it, your email provider may start to classify similar emails as spam in the future.

​**Recommendations**:

* Add our email address to your contacts or safe senders list.
* Avoid using spammy keywords or phrases in your email content.
* Send emails from a reputable domain and IP address.

We also do a daily review of emails that may have ended up in spam and push them to our ticketing system.

---

Related Articles

[SMS Long Code Deliverability Best Practices](https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices)[Troubleshooting Call Completion](https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion)[Best Practices for Contacting Porting](https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting)[3CX: Configuring a 3CX V18 PBX](https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx)[Mission Control Portal - AI Chat Support Assistant](https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant)

Did this answer your question?

😞😐😃

Table of contents
