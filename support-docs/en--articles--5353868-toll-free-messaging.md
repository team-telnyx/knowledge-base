---
source_url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
scraped: 2026-06-11
---

Toll-Free Messaging | Telnyx Help Center

[Skip to main content](#main-content)

# Toll-Free Messaging

In this article we will explain the importance behind toll-free messaging and use case submission

Written by Alex Conroy

December 1, 2025

Table of contents

For those looking to make large messaging campaigns, Telnyx supports messaging on toll-free numbers. We support SMS. Toll-Free MMS is supported (US and Canada *only*). This article details valid use cases, best practices and the verification process.

# **In this article, find information about**

* [Toll-free messaging use case registration information](#h_05f7302391)
* [Appropriate message content](#h_dff85cc0ad)

  + [Message content length](#h_fdeada0b41)
  + [Valid use cases](#h_5786b80a9e)
  + [Inappropriate use cases](#h_b0fd456b1f)
* [Toll-free messaging best practices](#h_39795a9168)

## Toll-Free Messaging Use Case Registration Information

To get started with toll-free messaging it's necessary to first have your use case approved. Verifying Toll Free Numbers ensures compliance and alignment with new industry standards. Use of non verified toll free numbers may result in spam blocks at any time. The unblocking of the spam blocks can only be achieved through use case verification.

## **How do I register my toll free number's use case?**

* **As of 23rd Nov 2022:** You can now submit to register your use case for your toll free number from your [mission control portal account](https://portal.telnyx.com/#/app/programmable-messaging/toll-free-messaging).

## **What Information do I need to provide?**

You'll be asked to clarify your use case and provide information such as:

* Business Details
* The toll-free number being used for the campaign
* A summary of the use case
* Message Content Examples

  + Expected volume per month
* The Opt-in process
* Additional Use Case Details

  + Terms URL
  + Privacy Policy
* If you're a reseller or independent software vendor then add your business name in the Reseller / ISV field, if you are registering the toll free number for your own direct use then leave the field blank.

## **Can I register my toll free use case through the API?**

**Yes!** you can register via API, which allows for bulk use case submissions and ability to track status of submitted TFNs. Visit our [developer documentation](https://developers.telnyx.com/docs/messaging/toll-free) to set up toll-free use case registration by API.

## **How do I track the progress of my use case registration?**

|  |
| --- |
| ***Note:*** *It can potentially take 4 weeks for the use case to be approved and only one unique use case can be associated with one toll-free number. i.e multiple toll-free numbers can not send the same messaging content as this is considered an industry bad practice, where there is a higher chance of such numbers becoming spam blocked.*    ***Note:*** *From the **8th of November 2023**, any unverified toll-free numbers that attempt to send messages will be blocked. This is an industry wide change, so please make sure to register your toll-free number and it's use case through your [account](https://portal.telnyx.com/#/app/programmable-messaging/toll-free-messaging). If you have any toll free numbers that were in a pending verification state prior to this date, you will still be able to send traffic. However, please note that we expect industry wide changes, in the early new year, that toll free numbers will not be able to send messages unless a use case is in an approved state first.*    ***Note:*** *Customers using our messaging products will have received an email in the first week of December 2023 to notify them in advance of the industry wide change happening from the **31st of January 2024** where any unverified toll-free numbers that attempt to send messages will be automatically blocked. Please make sure to register your toll-free number and it's use case through your [account](https://portal.telnyx.com/#/app/programmable-messaging/toll-free-messaging) first before attempting to send any traffic.*    ***Note:*** *Current use case approval times is now 2 weeks.* ​  ***Note:*** *From the early new year (February), we also expect an improvement in the time to approve use case from 2 weeks to 1 week.* |

After you have completed the submission, you can track the status from the requests tab.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1313575459/818c819e313b7591c4e09bef9b12/image.png?expires=1781168400&signature=da279043fc281d5eefc387c1da33dc7d1027d91bfc76433c85a1e9fe12d51477&req=dSMmFcx5mIVaUPMW1HO4zZAc6xbIzuobiIGFIJL%2BBKKuZl8hg%2B%2B%2F0QAGqa6P%0AXNocQbVNRZf7NNZeaKM%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1313575459/818c819e313b7591c4e09bef9b12/image.png?expires=1781168400&signature=da279043fc281d5eefc387c1da33dc7d1027d91bfc76433c85a1e9fe12d51477&req=dSMmFcx5mIVaUPMW1HO4zZAc6xbIzuobiIGFIJL%2BBKKuZl8hg%2B%2B%2F0QAGqa6P%0AXNocQbVNRZf7NNZeaKM%3D%0A)

To amend the details of your Toll-Free Verification, click the small arrow icon circled in green to access the verification information. Make the necessary changes, and then click "Save Changes" to update your submission.

You can also receive updates via webhook about status changes by inputting a webhook url. This way we can inform you as to whether the use case was approved or if further amendments need to be clarified.

## Appropriate Message Content

### Message content length

* UCS-2 (16 bit) = 70 character maximum. For longer multi-part messages, a user data header (UDH) is added to the message to instruct the receiving device on how to reassemble the message, resulting in a maximum of 67 characters for the body of the message.
* Latin1 (8 bit) = 140 character maximum. For longer multi-part messages, a user data header (UDH) is added to the message to instruct the receiving device on how to reassemble the message, resulting in a maximum of 134 characters for the body of the message.
* \*Most Common\* GSM7 (7 bit) = 160 character maximum. For longer multi-part messages, a user data header (UDH) is added to the message to instruct the receiving device on how to reassemble the message, resulting in a maximum of 153 characters for the body of the message. Any message segment which has been broken up from a single message due to length will be treated as a single message as will messages to multiple recipients

When sending toll-free sms it's important to have an appropriate use case and adhere to best practices. Violation of best practice principals could result in:

* Blocking of individual messages
* Blocking of phone numbers
* Repeated violation may result in account termination or blocking

## Valid Use Cases

The Following are examples of acceptable use cases permitted on the Telnyx Toll-Free SMS service:

* 2FA
* Account Notification
* Customer Care
* Delivery Notification
* Fraud Alert Messaging
* Higher Education
* Low Volume Mixed
* Marketing
* Mixed
* Polling and Voting
* Public Service Announcements

## Inappropriate Use Cases

The Following are examples of content and behaviors that are not permitted using on the Telnyx Toll-Free SMS service. Messages found to be associated with the following content may be blocked ***regardless of opt-in status*:**

1. Social Marketing
2. Collections
3. Cryptocurrency and all Cryptocurrency related language (mentions of bitcoin and such)
4. Financial services whether account notifications, marketing, collections or billing for:

   * High-risk/subprime lending/credit card companies
   * Auto loans
   * Mortgages
   * Payday loans
   * Short-term loans
   * Student loans
   * Debt consolidation/reduction/forgiveness
5. Insurance

   * Car Insurance
   * Health Insurance
6. Gambling, Casino, and Bingo
7. Gift cards
8. Sweepstake's
9. Free prizes
10. Investment opportunities
11. Lead generation
12. SEO Services
13. Recruiting
14. Commission programs
15. Credit repair
16. Tax relief
17. Illicit or illegal substances (including Cannabis)
18. Work from home
19. Get rich quick
20. UGGS and RayBan campaigns
21. Phishing
22. Fraud or scams
23. Cannabis
24. Deceptive marketing
25. SHAFT: Sex, Hate, Alcohol, Firearms or Tobacco

Additionally, the following practices should also be avoided to ensure high deliverability rates for toll-free messaging campaigns:

* **High Frequency Messages**   
  Senders should also avoid sending a high frequency of messages to subscribers. Senders may not send more than 10 messages to a recipient in any 24 hour period unless the following conditions are met:

  + The recipient has engaged in two-way communication over SMS such as for a chat feature.
  + The customer has explicitly opted in to receiving frequent messages.

* **Spoofing**

  Senders may not represent or identify themselves as another individual or business in any way. More specifically, you may not use the message body or the phone number in a way that would lead the recipient to believe you are another individual or business.
* **Engaging in Fraud or Phishing For Information**

  Sending messages with fraudulent information or phishing to get confidential information from a recipient is explicitly prohibited.

## Toll-Free Messaging Best Practices

Before sending out messages it's important to obtain consent from receivers this means having a clear *call-to-action*. A call to action should ensure that receiver are aware of:

* The program or product description;
* The phone number(s) or [short code](https://telnyx.com/products/sms-short-code)(s) from which messaging will originate;
* The specific identity of the organization or individual being represented in the initial message;
* Clear and conspicuous language about opt-in and any associated fees or charges; and
* Other applicable terms and conditions (e.g., how to opt-out, customer care contact information and any applicable privacy policy)
* A clear opt-in mechanismis necessary to prevent unwanted messages to receivers. Receivers may also choose to unsubscribe from future messages by sending stop words such as *STOP* or *UNSUBSCRIBE*. Senders have up to 24 hours to remove the recipient from the list.

## Toll-Free Verification Webhook Notifications

Once a Toll-Free verification request is submitted, Telnyx provides real-time status updates via webhooks to help you monitor the lifecycle of the verification. These notifications are automatically sent to the webhook URL provided during submission.

### Webhook Event Types

You’ll receive webhook events when the status of your Toll-Free number verification changes. The `verification_status` field in the payload will reflect one of the following values:

* `Rejected`: The verification request was rejected.
* `Waiting For Vendor`: The request is pending vendor review.
* `Waiting For Customer`: Additional information is needed from the customer.
* `Verified`: The Toll-Free number has been successfully verified.

Each event includes helpful context such as the affected phone number(s), business name, and the reason for the current status (if applicable).  
​

## Sample Webhook Payloads

#### ✅ Verified

```
{  
 "business_name": "Telnyx LLC",  
 "id": "123654d6-e062-5f72-abf9-876354056324",  
 "organization_id": "uhy56356-50e7-4c09-8e89-h47473765dgt",  
 "phone_numbers": [  
  {  
   "phone_number": "+18773554398"  
  }  
 ],  
 "reason": null,  
 "verification_status": "Verified",  
 "webhook_url": "http://example-webhook.com"  
}
```

#### ❌ Rejected

```
{  
 "business_name": "Telnyx LLC",  
 "id": "123654d6-e062-5f72-abf9-876354056324",  
 "organization_id": "uhy56356-50e7-4c09-8e89-h47473765dgt",  
 "phone_numbers": [  
  {  
   "phone_number": "+18773554398"  
  }  
 ],  
 "reason": "1106 - business information could not be verified - contact, email, address, or url is invalid\n1205 - business website url must display branding,",  
 "verification_status": "Rejected",  
 "webhook_url": "http://example-webhook.com"  
}
```

#### ⏳ Waiting For Vendor

```
{  
 "business_name": "Telnyx LLC",  
 "id": "123654d6-e062-5f72-abf9-876354056324",  
 "organization_id": "uhy56356-50e7-4c09-8e89-h47473765dgt",  
 "phone_numbers": [  
  {   
   "phone_number": "+18773554398"  
  }  
 ],  
 "reason": " ",  
 "verification_status": "Waiting For Vendor",  
 "webhook_url": "http://example-webhook.com"  
}
```

#### 📩 Waiting For Customer

```
{   
 "business_name": "Telnyx LLC",  
 "id": "123654d6-e062-5f72-abf9-876354056324",  
 "organization_id": "uhy56356-50e7-4c09-8e89-h47473765dgt",  
 "phone_numbers": [  
  {  
   "phone_number": "+18773554398"  
  }  
 ],  
 "reason": "Opt In Work Flow Image Link - does not display compliant CTA Opt In\r\nPlease See this link section 3 for more info - https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide ",  
 "verification_status": "Waiting For Customer",  
 "webhook_url": "http://example-webhook.com"   
}
```

---

Related Articles

[How to Leverage Webhooks](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks)[Toll-Free Opt-Out Words](https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words)[US / CA Toll Free Number Porting](https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting)[Toll Free Verification Request Guide](https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide)[How to Pick a Toll Free Use Case](https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case)

Did this answer your question?

😞😐😃

Table of contents
