---
source_url: https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices
title: "SMS Long Code Deliverability Best Practices"
description: "In this article we will explain what you should do to make sure that your long code SMS messages are consistently… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 323a6b9825f680da66faad141e0ff0383bc3f6d168a68d1cf39ef435eea36127
---







# SMS Long Code Deliverability Best Practices

In this article we will explain what you should do to make sure that your long code SMS messages are consistently… See Telnyx guidance and requirements.




## **Ensuring your outbound SMS messages are delivered successfully**

## Use long codes for unique messages only

Long code SMS is intended for person-to-person (P2P) communication or application-to-person ([A2P](https://telnyx.com/resources/what-is-a2p-messaging)) use cases where a human is initiating the message. The message should contain content that is specific to the recipient.

Types of messages that are good candidates for long codes:

* An SMS chatting application where a customer is communicating with a sales or customer service representative.
* An SMS reminder about an upcoming appointment with a doctor.
* A notification that a taxi has arrived.

If the content you are sending is not unique to the customer then it's likely a marketing campaign which is better suited for [short code](https://telnyx.com/products/sms-short-code) messaging.

As mobile operators tighten their systems on what messages they allow to their network, you should heavily consider setting up [10DLC](https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc).

## Limit your send rate

Mobile operators generally only accept 10 messages per minute from any long code number (that's no more than a message every 6 seconds). The rule of thumb is that the rate shouldn't exceed what a human could reasonably do if they were using a phone. Please keep in mind, your overall Telnyx portal account is limited to sending 1 message / second.  If you require a higher limit, please reach out to [sales@telnyx.com](mailto:sales@telnyx.com) via email, and we can talk about raising your message rate limit.  If you attempt to send more quickly than 1 message / second overall or more than 10 messages/minute/number, Telnyx's SMS platform will throttle your deliverability so as not to exceed the maximum rate.

## Don't send a high volume of messages from consecutive numbers

You may want to purchase and use a consecutive number range to send long code messages. However, SPAM filters used by mobile operators identify this as suspicious and are apt to block these messages. Telnyx recommends that you purchase discontiguous numbers if you plan to send a higher volume of messages.

## Limit the length of URLs in the message

Lengthy URLs may not only cause your messages to be split into multiple parts (and being charged accordingly) but also are more likely to be flagged by SPAM filters.

* Be careful when sending multi-part messages that also have a URL.  If you don't know the length of the URL beforehand (since you may be dynamically creating it) try to minimise the rest of the text in your message to leave room for the URL.

* You should certainly consider the type of url domain you use, since there are URLs which are known to be related to spam or are often attributed to fraudulent activities.

  + Messages with "bitlylinks.com" and "bit.ly" urls will be blocked automatically.
    ​
* Our acceptable usage [policy](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging).

## Include Opt Out Language

Mobile operators, in conjunction with their spam filters, will watch out for A2P messaging that does not contain Opt Out language, especially unregistered traffic. In such instances, we have observed false delivery reports indicating the messages have been delivered but they were instead filtered as spam and the number one reason for this is due to excluding opt out language.

---

Related Articles

[Frequently asked questions about 10DLC](https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc)[Register for 10DLC Messaging](https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging)[Telnyx 10DLC Compliance Directory](https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory)[Telnyx Messaging Error Codes](https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes)[Norway: SMS Guidelines](https://support.telnyx.com/en/articles/6560704-norway-sms-guidelines)

Did this answer your question?

😞😐😃
