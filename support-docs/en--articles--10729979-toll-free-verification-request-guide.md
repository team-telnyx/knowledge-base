---
source_url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
scraped: 2026-06-11
---

Toll Free Verification Request Guide | Telnyx Help Center

[Skip to main content](#main-content)

# Toll Free Verification Request Guide

Toll Free Verification Request Process, Basic Criteria, Statuses, and Error Reasons

K

Written by Klane Pedrie

November 18, 2025

Table of contents

# **Toll-Free Verification Guide**

Before you can send your first outbound message from a Toll-Free phone number you must first "Verify" the number. Toll-Free Verification requires specific data to be submitted to ensure a successful verification process. The provided information helps identify the end business and ensures they have the proper measures in place to send compliant traffic. Below is a detailed guide on what is required for a submission. Incomplete submissions may be rejected if they do not contain the necessary fields.

Time line for approvals are normally 5 business days or less but can be faster or slower depending on volume of requests received.

## How do I submit a Toll Free Verification Request

You can do so by:

Telnyx Portal: portal.telnyx.com > Real Time Communications > Messaging > Compliance > [Toll Free Verification](https://portal.telnyx.com/#/programmable-messaging/toll-free-messaging) > Submit Verification Request

Telnyx API: [Submit Verification Request](https://developers.telnyx.com/api/messaging/toll-free-verification/submit-verification-request)

Once you have submitted the Toll Free Verification Statuses are:

Waiting for Telnyx - We review all submissions to determine if the traffic should be allowed on the platform and for compliance requirements.

Waiting for Customer - If the Telnyx review team has a change we would like you to make to your Verification Request then we will change the status to Waiting for Customer and the decline reason will have what steps we would like you to take.

Waiting for Vendor - Once Telnyx team approves the VR it goes to the carriers to get the final approval.

Rejected - If the carriers or Telnyx team reject the VR then the status will be rejected and the decline reason will have why it was rejected.

Verified - Once the Telnyx team and carriers have approved it, then the status will be "Verified" and you can begin sending outbound text messages from the toll free number.

It is important to know that you if you submit a new Verification Request for an already approved Toll Free number it will be overwritten and become unverified until the new Verification Request is approved.

## **Toll-Free Verification Form Explanation**

### **1. Business Identification**

* **Business Name:** The business name, website domain, and email domain should match or if they are different, the difference should be explained in the additional information field.
* **Corporate Website**: Please include a business website or social media page for the business. This is what we are looking for with business websites:  
  Business Name  
  Contact Information (address/email/etc)  
  Products/Services offered by the business  
  About page  
  Contact us page  
  Privacy and Terms page
* **Email Address**: The website domain should match the domain of the email address provided. Freemail contacts like Gmail can be cause for decline.
* **Business Address-** Valid business address
* **Contact Number:** Contact number for the business using the Toll Free number (not the toll free number being reviewed for this Verification Request).
* **Business Contact:** a common occurrence is business names/departments in those fields when it needs to be a persons first/last name

### **2. Messaging Details**

* **Expected Message Volume-** Approximate based on the available drop down options.
* **Use Case :** This refers to the specific purpose for which the business intends to use toll-free messaging. Examples include conversational, marketing, transactional notifications, or fraud alerts. If you use a mixed use case then please describe the actual use cases in the Use Case description field. Every sms use case mentioned on the opt in form should be present here in some way. The use cases selected and mentioned anywhere on the VR or opt in form should all be consistent.

  Options:  
  ​
* 2FA
* App Notifications
* Appointments
* Auctions
* Auto Repair Services
* Bank Transfers
* Billing
* Booking Confirmations
* Business Updates
* COVID-19 Alerts
* Career Training
* Chatbot
* Conversational / Alerts
* Courier Services & Deliveries
* Emergency Alerts
* Events & Planning
* Financial Services
* Fraud Alerts
* Fundraising
* General Marketing
* General School Updates
* HR / Staffing
* Healthcare Alerts
* Housing Community Updates
* Insurance Services
* Job Dispatch
* Legal Services
* Mixed
* Motivational Reminders
* Notary Notifications
* Order Notifications
* Political
* Public Works
* Real Estate Services
* Religious Services
* Repair and Diagnostics Alerts
* Rewards Program
* Surveys
* System Alerts
* Voting Reminders
* Waitlist Alerts
* Webinar Reminders
* Workshop Alerts
* **Description of the Use Case / Summary :** This section provides more details about how the business will use the toll-free number for messaging. It should explain the types of messages being sent, the intended audience, and any relevant compliance measures. This additional information helps verification teams assess whether the use case is legitimate and compliant with messaging policies. If you use a mixed use case then please describe the actual use cases in the Use Case description field. For mixed use cases every sms use case mentioned on the opt in form should be present here in some way.
* **Message content:** Please add samples for each use case you selected and described in the use case summary field.

### **3. Opt in Workflow Description / Opt-in Image URL:** Provide a link, a link to an image, or a link to a scanned copy of the opt-in.

Ensuring proper SMS consent is critical for verification. The opt-in process must be clearly documented in the Workflow Description explaining how the opt in process works. For example you could say subscribers opt in on my website at <https://exampleurl.com/opt-in>. There are 4 ways users can opt in to receive sms:  
1) Digital

2) Paper

3) Verbal

4) Inbound Message

For whichever opt in method you select the subscriber must receive these disclaimers at some point before the first message (except for an inbound text opt in which can have the disclaimers in the first message):  
​  
You are subscribing to [brand name] for [use case (transactional or marketing)]. Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].

For a digital opt in you need to include the url or link to a screenshot of the branded opt in form (as much of the form as possible) and how subscribers reach it.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1579335113/67613d127dad2e151f97d6da5fb7/image+%2835%29.png?expires=1781167500&signature=8ee7bfc99dcdfdb273442d01daa1e8a24d20d5aa4f29ab8f460a9905b5c5157b&req=dSUgH8p9mIBeWvMW1HO4zapr%2BCkYjcboEul9uVEgZTP%2F841eJPrGJPIf9oz%2F%0A%2FoKv1ndO53tQzIlbwc0%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1579335113/67613d127dad2e151f97d6da5fb7/image+%2835%29.png?expires=1781167500&signature=8ee7bfc99dcdfdb273442d01daa1e8a24d20d5aa4f29ab8f460a9905b5c5157b&req=dSUgH8p9mIBeWvMW1HO4zapr%2BCkYjcboEul9uVEgZTP%2F841eJPrGJPIf9oz%2F%0A%2FoKv1ndO53tQzIlbwc0%3D%0A)

For a paper opt in you need to include a link to the uploaded branded file and how subscribers receive it.

For a verbal opt in you need to include the script users hear when opting in and how they receive it and where for instance if it over the phone then what number do they call. If it is in person then how do they learn the address and all the standard disclaimers shared above.

For an inbound message please give the phone number they text into and how they learn it.

If you do not have a link for the opt in image url field, like for a verbal consent opt in, then put a link to a publicly accessible google doc or dropbox file which diagrams how the opt in process works.

If Marketing is a selected use case then on the opt in, marketing sms opt in must have its own compliant checkbox separate from the other use cases.

Opt in form for both transactional and marketing use cases:

* **[Checkbox 1]** By checking this box and submitting this form, you consent to receive transactional text messages for [use case(s)] from (Company Name). Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].
* **[Checkbox 2]** By checking this box and submitting this form, you consent to receive text messages for marketing from (Company Name). Reply STOP to opt out. Reply HELP for help. Message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].  
  ​  
  Note: In the privacy policy the carriers typically require verbiage to the effect of "We will not share or sell your mobile information with third parties for promotional or marketing purposes."

  Note: Checkboxes must be optional and cannot be pre-checked.

  Note: The opt in form should be branded with the same brand which is being registered.

**Important Note:**

* The **business name** should be included on the opt in form within the message content to make sure the consumer knows who they are interacting with.
* The SMS opt-in checkbox should be **unchecked** by default.
* SMS consent should be **separate** from other communication consents (e.g., email). This means having distinct checkboxes for SMS and email opt-in.
* Previously, the opt-in message and privacy policy were combined into a single checkbox for consent. Now, accepting **SMS opt-in and privacy policy must have separate checkboxes**.

### **4. ISV/Reseller Information**

* **ISV/Reseller**: If the Telnyx account username domain does not match the domain for the business website and business email address in the business contact section of the Toll Free Verification Request then it will be put into a Waiting For Customer status until the Reseller field has been accurately filled out with the Reseller name. If the Telnyx account is for the same domain as the business being registered then you should leave the Reseller field blank.

### **5. Additional Supporting Details**

If you are submitting more than 5 Toll Free Numbers in a single Verification Request then please include a detailed valid explanation for why multiple numbers are needed. Be very specific about these details, such as if you need multiple toll free numbers because there are multiple store locations then explain that in depth like this: The reason this VR has 6 Toll Free numbers being requested is because we have 6 locations and there will be 1 toll free number for each location so the local team can field specific customer service questions such as inventory checks. +1800XXX-XXXX will be for the Austin, Texas location on 123 Main St. +1888XXX-XXXX will be for the Houston, Texas location on 321 Broadway St.

A commonly used explanation is:

We need multiple toll-free SMS numbers because we have several employees who regularly communicate with clients. Having enough numbers ensures that each employee can manage conversations efficiently without delays or overlap.. All communication is client-initiated, and these numbers help us manage those conversations efficiently while maintaining our privacy standards.

Also, if there are any other details you would like Telnyx or the carriers to know you can include that here!

If you run out of characters then please use a publicly accessible google doc and put the explanation in the google doc and paste the link to the google doc into the VR. Then describe the content of the google doc in the VR as well.

### Age Gating

The opt in form or website need an age gate anytime you are marketing something that is not legal to consume under a certain age in any of the 50 states, such as Alcohol. If it is a restaurant that offers alcohol for example but will not promote alcohol over sms then you do not need an age gate but you do need to include in the VR that no alcohol will be promoted via sms. The age gate should not be a YES/NO age gate, it should be enter your birthdate age gate which does not allow user to proceed if the date is less than the required age.

### If you select a Political Use Case:

Make sure to include if donations will be solicited in the use case summary.

The opt in form needs a separate checkbox from transactional or marketing consent for political consent if you have a mixed use case.

Privacy Policy must explicitly state that "No mobile information will be sold or shared with third parties for promotional or marketing purposes.

### For a Charity raising donations:

You select a Fundraising Use Case unless you have multiple use cases in which case you do mixed.

On the opt in form a fundraising or charity checkbox separate from the other consents would be needed and in the checkbox disclaimers it should mention donations will be solicited.

Also in the Use Case summary of the VR it should mention that donations will be solicited.

### Prohibited

This is not a comprehensive list but we will add to it over time:  
- Loan soliciting/promotion

- CBD related

- Gambling

### Canadian Toll Free Numbers

Canadian Toll Free numbers must do all the above plus collect double opt in, which means that after the initial opt in process a confirmation message must be sent and the subscriber must reply with an affirmative they are subscribing to the program.

## Toll Free Error Codes: ​ ​

|  |  |
| --- | --- |
| **Reason** | **Eligibility for Resubmission** |

|  |  |
| --- | --- |
| **No Reason Provided** | Not Eligible |

|  |  |
| --- | --- |
| **Content Violation - SHAFT (Sex, Hate, Alcohol, Firearms, Tobacco/Vape, Marijuana/CBD)** | Not Eligible |

|  |  |
| --- | --- |
| **Campaign Violation - Age Gate Not Present / Not Acceptable** | Eligible with Robust Age Gate Implemented |

|  |  |
| --- | --- |
| **Known Spam Campaign** | Not Eligible |

|  |  |
| --- | --- |
| **Disallowed Content - Loan Marketing, 3rd Party Debt Collection, Gambling, Sweepstakes, Stock Alerts, Cryptocurrency, Risk Investment, Debt Reduction, Credit Repair, 3rd Party Lead Generation, Federally Illegal Substances** | Not Eligible |

|  |  |
| --- | --- |
| **Known Phishing Campaign** | Not Eligible |

|  |  |
| --- | --- |
| **High Risk - Fraud** | Not Eligible |

|  |  |
| --- | --- |
| **High Risk - Deceptive Marketing** | Not Eligible |

|  |  |
| --- | --- |
| **High Risk - Public URL Shortener** | Eligible if changed to a branded URL domain |

|  |  |
| --- | --- |
| **High Risk - Non-secured URL** | Eligible if corrected to HTTPS |

|  |  |
| --- | --- |
| **Invalid Information - Can't Verify Business Information** | Eligible if business details are corrected |

|  |  |
| --- | --- |
| **Invalid Information - Can't Validate URL (Website inaccessible)** | Eligible if website access is restored |

|  |  |
| --- | --- |
| **Invalid Information - ISV Contact Provided Instead of End User** | Eligible if corrected |

|  |  |
| --- | --- |
| **Opt-in - Not sufficient for campaign type (Express Consent Required)** | Eligible if express consent is provided |

|  |  |
| --- | --- |
| **Opt-in - Consent for messaging is a requirement for service** | Eligible if consent is documented |

|  |  |
| --- | --- |
| **Opt-in - No opt-in provided** | Eligible if opt-in is provided |

|  |  |
| --- | --- |
| **Opt-in - Shared with 3rd Parties** | Eligible if language is updated to remove 3rd-party sharing |

|  |  |
| --- | --- |
| **Campaign Violation - Single Number Used for Multiple Businesses** | Eligible if each business is assigned a unique toll-free number |

|  |  |
| --- | --- |
| **Opt-in - List Opt-in Relies on Organizational/Government Exemption** | Not Eligible |

|  |  |
| --- | --- |
| **Additional Information Requested - Justification for more than 5 numbers per business** | Eligible if justification is provided |

|  |  |
| --- | --- |
| **Additional Information Requested - Opt-in Information Not Provided** | Eligible if updated |

|  |  |
| --- | --- |
| **Additional Information Requested - Business Information Not Valid** | Eligible if corrected |

|  |  |
| --- | --- |
| **Submission Editing Timed Out** | You have 7 days from when it is submitted to the carriers for Telnyx to resubmit without any changes. This is not a big problem for portal users because if you make a small change to your existing Verification Request and hit save then it creates a new VR Id without you having to fill it out from scratch. More of a challenge for API users to address. |

|  |  |
| --- | --- |
| **Number Not Provisioned to Your Organization** | Not Eligible |

---

Related Articles

[Toll-Free Messaging](https://support.telnyx.com/en/articles/5353868-toll-free-messaging)[Toll-Free Opt-Out Words](https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words)[US / CA Toll Free Number Porting](https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting)[How to Pick a Toll Free Use Case](https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case)[Toll-Free Carrier Rejections](https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections)

Did this answer your question?

😞😐😃

Table of contents
