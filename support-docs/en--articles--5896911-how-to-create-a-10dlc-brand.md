---
source_url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
scraped: 2026-06-11
---

How to create a 10DLC brand | Telnyx Help Center

[Skip to main content](#main-content)

# How to create a 10DLC brand

Creating a brand is the first step to becoming compliant with 10DLC rules. Read on to learn how you can create your brand.

Written by Telnyx Engineering

July 24, 2025

Table of contents

# **How to create a 10DLC brand**

If your business is sending outbound text messages using 10-digit long code (10DLC) Local phone numbers in the US, you're required to register for 10DLC approval. In this guide, we'll show you how to complete the first step of this process by registering your brand, using tools provided in the Telnyx Mission Control Portal.

**Pre-requisites:**

Telnyx provides APIs and services that you can use to send text messages. We also provide a set of tools—available via our Mission Control Portal and our APIs—that you can use to register the messaging campaigns you send using the Telnyx platform for 10DLC. If you don't already have a Telnyx account, you can [sign up](https://telnyx.com/sign-up) and leverage these tools and resources to send 10DLC-compliant text messages.

## Creating a 10DLC brand in the Mission Control Portal

Once you're logged into the [Mission Control Portal](https://portal.telnyx.com), head to the Messaging section and then to the [10DLC Brand](https://portal.telnyx.com/#/messaging-10dlc/brands) tab. From here, you can get started by selecting "Create a brand".

## Creating a 10DLC brand using the Telnyx API

If you'd prefer to create your brand using a simple API command, you can find details in our [API reference documentation](https://developers.telnyx.com/api/messaging/10dlc/create-brand-post).

## Information you'll need to register your 10DLC brand

You'll be asked for the following information about your business when registering a 10DLC brand. Please note that this information is used by mobile network operators to verify your brand and can affect the throughput allowed to your campaigns. You should ensure that all of the information supplied as part of 10DLC brand registration is correct, complete, and free of typos, as these issues can limit your throughput or cause delays when verifying your brand.

**Business Information**

For US brands, if the information entered does not match the IRS Form CP-575 then the brand will remain permanently unverified. If the brand is uverified then please follow: <https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand>

|  |  |
| --- | --- |
| **Item** | **Description** |
| Legal Company Name | The official, legal name of your business. This should match the name under which your EIN is issued. |
| DBA or Brand Name | Doing Business As (DBA) or any trade names. This field is required, even if your brand name is the same as your Legal Company name. |
| What type of legal form is the organization? | The type of legal entity your brand represents. Choose from:  * *Charity / Non-Profit Organization* * *Government* * *Private Company* * *Publicly Traded Company* |
| Vertical | The industry vertical which best matches your business. |
| Country of Registration | The country in which your business is registered. |
| Website | A URL directing to your business' website. |
| EIN Issuing Country | The country that issued your business' EIN or identification number. |
| EIN | Your business' Employer Identification Number. [EINs are issued by the Internal Revenue Service in the US.](https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers) If your business does not have an EIN, use this field for an alternative business identification number supplied by your relevant issuing country. |
| Stock Symbol *(required only for Publicly Traded Companies)* | Your business' stock symbol. |
| Stock Exchange *(required only for Publicly Traded Companies)* | The stock exchange on which your business is listed. |
| Reseller | This box should be checked if your business re-sells products and services to other end users who are also businesses. Resellers are also known as Independent Service Vendors (ISVs). Learn more about [10DLC for ISVs](https://support.telnyx.com/en/articles/5593977-isvs-10dlc). |
| Business Address, City, State / Region, and Postal Code / Zip Code | The official, legal address of your business. This should match the name under which your EIN is issued. |

**Brand Contact Details**

|  |  |
| --- | --- |
| Email Address | The email address of an authorized representative for your business. Should be an individual's email and not a group alias. |
| Phone Number | The phone number of an authorized representative for your business. |

### Publicy Traded Brands and the Auth+ Process

If you create a brand and select the Public\_Profit entity type because that brand is publicly traded on the US stock market then you will be required to complete a 2fa process to verify the brand.

The Auth+ process entails including a representative individual's email address that matches the web domain of the brand when creating a new brand.

Once you submit your brand then the contact email you entered will receive an email from [noreply@auth.campaignregistry.com](mailto:noreply@auth.campaignregistry.com) within a few days. Once the email is received open it and click the link and fill out a short form with your name, title, and contacts and save. That completes the Auth+ process.

If you have an existing Public\_Profit brand that you need to create a new campaign for then please send the brand id and brand business contact to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) and we will trigger the 2fa email for you.

Until the Auth+ process is completed no new campaigns will be able to be created for Public\_Profit brands.

As of Aug 1, 2025 there will be a $15 fee for Auth+ attempts but for up to date pricing please refer to the Telnyx portal.

**A Note about Canadian Brands**

Here is some additional advice when registering a Canadian brand:

* In place of the EIN, provide your Provincial or Federal Corporation/Registry ID Numbers (Private Profit, Public Profit brand types). These are the identification numbers created when a business is initially formed and registered in their home province or with Corporations Canada as a federal corporation (these are not the same as the Canada federal business number, which is created for taxation purposes).
* Please avoid using your Canadian Federal Business Number (BN) or Canadian Revenue Agency Tax Account Numbers in the EIN section. However, if this is the only identifier you have available, you can still create the brand with this information, just have your official registration documents prepared as the brand will need to be manually vetted.
* When using your Provincial identification number, we have seen that sometimes provinces make changes over time which cause the original business registration to be misaligned with the currently posted information on the business. Have your official registration documents handy for your business in case a manual vet of your brand needs to take place.

**Billing Details**

There is a one-time, non-refundable cost of $4 for registering a brand. This is a pass-through fee applied by the Campaign Registry.

*Reminder: The Campaign Registry is an independent organization that manages 10DLC brands and campaigns, working with mobile network operators.*

**Next steps after registering your brand for 10DLC**

After you register your brand, it will automatically go through an identity verification process. During this process, the Campaign Registry validates the information provided to confirm the validity of the brand. Your brand's identity status will be immediately available in the Mission Control Portal.

**What if my brand is not verified?**

The most likely cause of a brand not being verified is an error in the information provided. If your brand is not verified, be sure to review all of the brand information for correctness. If there is an error in the brand's EIN, please reach out to our team for assistance.

**Third-party vetting to enhance your brand**

It's possible to achieve better commercial terms for your brand by submitting it for third-party vetting. Once you've created a brand following the steps in this guide, you'll see an option to request third-party verification in your brand settings in the Mission Control Portal.

---

Related Articles

[Register for 10DLC Messaging](https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging)[How to create a 10DLC campaign](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign)[Telnyx 10DLC Compliance Directory](https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory)[10DLC Mock Brands and Campaigns](https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns)[Guide to Sole Proprietor 10DLC Brand and Campaign Registration](https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration)

Did this answer your question?

😞😐😃

Table of contents
