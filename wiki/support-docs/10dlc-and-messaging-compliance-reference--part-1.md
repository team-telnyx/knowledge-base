---
title: 10DLC and Messaging Compliance Reference
summary: This page consolidates Telnyx 10DLC and messaging compliance guidance, including
  carrier error codes for campaign declines, suspension and reactivation procedures,
  sole proprietor registration, shared campaign imports, toll-free verification requirements,
  and the full catalog of Telnyx messaging error codes.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
updated_at: 2026-07-17T09:00:38Z
---

# 10DLC and Messaging Compliance Reference

*Part 1 of 7 — see also: [Part 2](10dlc-and-messaging-compliance-reference--part-2.md), [Part 3](10dlc-and-messaging-compliance-reference--part-3.md), [Part 4](10dlc-and-messaging-compliance-reference--part-4.md), [Part 5](10dlc-and-messaging-compliance-reference--part-5.md), [Part 6](10dlc-and-messaging-compliance-reference--part-6.md), [Part 7](10dlc-and-messaging-compliance-reference--part-7.md)*

This page consolidates Telnyx 10DLC and messaging compliance guidance, including carrier error codes for campaign declines, suspension and reactivation procedures, sole proprietor registration, shared campaign imports, toll-free verification requirements, and the full catalog of Telnyx messaging error codes.

## 10DLC Carrier Error Codes

Carriers return specific error codes when a 10DLC campaign is declined. The codes fall into a few broad categories: prohibited content, inaccurate or inconsistent registration, opt-in and privacy policy issues, and brand/registration problems.

### Prohibited Content (700-series)

| Code | Reason | Explanation |
| --- | --- | --- |
| 701 | Prohibited Content; Cannabis | Any submission related to cannabis, including CBD, hemp, teas, beauty products, or derivatives, is subject to automatic rejection. This also includes shipping services. |
| 702 | Prohibited Content; Guns/Ammo | The sale of firearms and ammunition should have age verification. Educational content is acceptable if it does not engage in sales. |
| 703 | Prohibited Content; Explicit Sexual | Content promoting illegal sexual themes, non-consensual acts, or underage exploitation is prohibited. Includes content appearing family-friendly but containing adult themes. |
| 704 | Prohibited Content; Gambling | Covers participation in games of chance, including casino games, sports betting, lottery, and online gambling. Bingo promotions may be allowed under certain conditions with age gating. |
| 705 | Prohibited Content; Hate | Any form of hate speech, inappropriate content, or profanity is prohibited. |
| 706 | Prohibited Content; Alcohol (Age-Gated) | All content must adhere to laws and include a functioning age gate requiring date of birth verification at opt-in. A DD/MM/YYYY age gate is required rather than a simple "Are you over 21?" button. |
| 707 | Prohibited Content; Tobacco/Vape (Age-Gated) | Similar to alcohol, requires an age gate and legal compliance. |
| 708 | Lead Gen/Affiliate Marketing Prohibited | Prohibits the sharing or selling of information to third parties for lead generation. Any mention of lead generation or SEO on the website would lead to a decline of this nature. |
| 709 | Lead Gen/Affiliate Marketing Prohibited (High-Risk Financial Services) | Includes payday loans, non-direct lenders, debt collection, credit repair programs, and debt forgiveness services. This includes crypto-related traffic or traffic related to stock trading. |

### Inaccurate or Inconsistent Registration (600-series)

| Code | Reason | Explanation |
| --- | --- | --- |
| 601 | Campaign Attributes Do Not Match Website and/or Sample Message Content | Business details on the website, attributes, and sample messages must be consistent. If the Embedded Link/Embedded Phone number attributes are marked as YES, then the message samples must contain a link/phone number. |
| 602 | Inaccurate Registration; Inconsistent Sample Message and Use-Case | Sample messages should align with the declared use-case. Most common with a marketing use case chosen for the campaign that is not specifically mentioned in the Call to Action online or the Message Flow section in the campaign. |
| 603 | Inaccurate Registration; Inconsistent Website and Sample Messages | The business shown on the website should match the sample messages provided. |
| 611 | Opt-in Message Requirements Not Met | Opt-in confirmation messages must include program name, message frequency, HELP instructions, opt-out instructions, and message/data rate disclosures. Opt-in must also meet express consent standard (e.g., a checkbox next to the call to action verbiage). |

Carriers look for consistency and accuracy when reviewing campaigns. If you select a marketing use case when creating the campaign, that must be consistent throughout the campaign description, message flow, opt-in form, website, and sample messages. For example, if you select the use case 2FA and your campaign description, opt-in form, and message flow describe a different use case such as Account Notifications or Marketing, that is inconsistent and is cause for decline. Similarly, if your campaign description says the traffic will be customer care and appointment reminders for a Mechanic's shop but the website in the brand details or the website provided for the opt-in is for an Accounting Firm, that is inconsistent and will be cause for decline.

Sample messages also have to be consistent with all the other fields, website, and use cases. If you select only a 2FA use case and put anything other than a 2FA use case in the sample message, that would be inconsistent and cause for decline. Each use case you select must have one representative sample message. A dedicated marketing use case or a mixed use case requires at least two sample messages, or more.

If you receive a 602 or 603 error, check the following fields for consistency and accuracy:

1. Use cases selected at time of campaign creation.
2. Website you gave on brand page and in the message flow if it was a digital opt-in.
3. Campaign description.
4. Message Flow and Opt-in Form.
5. Sample Messages.

### Brand and Registration Issues (700/800-series)

| Code | Reason | Explanation |
| --- | --- | --- |
| 710 | Reseller / Non-compliant KYC | The brand sending the messages must be the one registered, not the agency behind it. |
| 711 | Repeated Use of Same EIN for Multiple Brands | Requires a valid explanation for the repeated use of EINs. |
| 712 | Misleading Registration | Direct lenders and regulated entities must mark themselves as such during campaign registration. |
| 713 | Large Companies Using Non-Official Email Domains | Large companies should use official email domains to prevent fraud risks. |
| 801 | Not Sole Proprietor | The business does not meet Sole Proprietor (EIN) criteria set by TCR and mobile carriers. |
| 802 | Sole Proprietor Not Yet Authorized | Requires authorization from Syniverse to use Sole Proprietor cases. |
| 803 | Opt-in Language Required on Website | If the website requires a phone number for contact, it must include opt-in language. |
| 804 | Unable to Verify Website/CTA Information | Incomplete or inaccessible call-to-action (CTA) information on the website or broken links. |
| 805 | Non-Compliant Privacy Policy | The privacy policy must state that SMS opt-in data will not be shared with third parties. |
| 806 | Unable to Verify, Needs Compliant and Accurate CTA Information | The Message flow in the campaign or the Call to Action (in the website) do not contain HELP Language, STOP language, message frequency, data rates, or privacy policy link or language. For verbal opt-in, the message flow section of the campaign must have all the necessary language. For online opt-in, the CTA must contain: program (brand) name/product description, message frequency disclosure (e.g., "Message frequency may vary."), "Standard Message and Data Rates may apply" (if non-FTEU), "Reply STOP to opt out" (opt-out information may appear in the terms and conditions), "Reply Help for help", terms and conditions or link to terms and conditions (not a pop up), and privacy policy or link to a privacy policy. |
| 807 | Unable to Verify, Inauthentic Website | Specifically for real estate and insurance companies using incomplete websites that don't allow business verification. |
| 851 | Privacy Policy and Opt-in Confirmation Requirements Not Met | Privacy policy must include disclaimers about third-party data sharing, and opt-in messages must include program name, opt-out instructions, and support contact details. |
| 852 | Privacy Policy Compliance Missing | Privacy policy must clearly indicate that mobile opt-in data is not shared with third parties. |
| 861 | CTA Information Incomplete | The CTA must contain program name, message frequency, opt-in disclosures, and links to terms & conditions. |
