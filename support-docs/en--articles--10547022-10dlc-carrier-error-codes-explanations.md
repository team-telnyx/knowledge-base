---
source_url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
title: "10DLC Carrier Error Codes Explanations"
description: "Explanation for Error Codes for 10DLC Campaign… See Telnyx guidance and requirements Learn more about 10DLC Carrier Error Codes Explanations with Telnyx."
scraped: 2026-07-08
content_hash: 9b6044d0b967707a06966ae9c750424519d3d24b6d0118951e910d3ae8f1afb7
---

# 10DLC Carrier Error Codes Explanations

Explanation for Error Codes for 10DLC Campaign… See Telnyx guidance and requirements Learn more about 10DLC Carrier Error Codes Explanations with Telnyx.

|  |  |  |
| --- | --- | --- |
| Code | Reason | Explanation or Scenarios Where This Can Be Used |
| 701 | Prohibited Content; Cannabis | Any submission related to cannabis, including CBD, hemp, teas, beauty products, or derivatives, is subject to automatic rejection. This also includes shipping services. |
| 702 | Prohibited Content; Guns/Ammo — Failure to age gate | Robust birthdate age-gate is required on the website and opt-in. Sample messages must not mention any specific brand of firearm/ammo. Age-gate attribute must also be selected. |
| 703 | Prohibited Content; Explicit Sexual | Content promoting illegal sexual themes, non-consensual acts, or underage exploitation is prohibited. Includes content appearing family-friendly but containing adult themes. |
| 704 | Prohibited Content; Gambling | Covers participation in games of chance, including casino games, sports betting, lottery, and online gambling. |
| 705 | Prohibited Content; Hate | Any form of hate speech, inappropriate content, or profanity is prohibited. |
| 706 | Prohibited Content; Alcohol — Failure to age gate | Robust birthdate age-gate is required on the website and opt-in. Sample messages must not mention any specific brand of alcohol. Age-gate attribute must also be selected. |
| 707 | Prohibited Content; Tobacco/Vape (Age-Gated) | Similar to alcohol, requires an age gate and legal compliance. |
| 708 | Lead Gen/Affiliate Marketing Prohibited | Prohibits the sharing or selling of information to third parties for lead generation.    Any mention of lead generation or SEO on the website would lead to a decline of this nature. |
| 709 | Lead Gen/Affiliate Marketing Prohibited; High-Risk Financial Services | Includes payday loans, same day loans, merchant cash advances, non-direct lenders, third-party debt collection, credit repair programs, and debt relief/forgiveness services.    This also includes Crypto related traffic or traffic related to stock markets, trading, commodities. |
| 601 | Campaign Attributes Do Not Match Website and/or Sample Message Content | If a campaign is connected to a direct lender and is providing lending services then the "Direct Lending or Loan Arrangement" attribute must be selected.    If a campaign is connected to alcohol, firearms or a dating site then the "Age-Gated Content" attribute must be selected.    If the Embedded Link/Embedded Phone number attributes are marked as YES, then the message samples must contain a link/phone number |
| 602 | Inaccurate Registration; Inconsistency between sample message, description, attributes and/or call to action with selected use-case | Sample messages, campaign description and call to action should align with the declared use-case.    Most common with a marketing use case chosen for the campaign that is not specifically mentioned in the call to action or campaign description. Also when a sample message includes a verification code but the 2FA use case has not been selected for the campaign. |
| 603 | Inaccurate Registration; Inconsistency between brand, description, website and/or sample messages | The Brand DBA Name registered needs to match the entity described in the campaign description, CTA, website and sample messages.    If the Brand DBA Name is different from the entity in the campaign details/messages a detailed explanation needs to be provided in the campaign description as to how the two entities are related. |
| 611 | Opt-in message/Confirmation MT must contain brand name, HELP, opt-out, message frequency and associated fees disclosures. Opt-out message must contain brand name and indicate that no further messages will be sent. HELP message must contain brand name and contain support contact (email, phone number, or support website). | Opt-in, Opt-out and Help confirmation messages must contain details provided here: <https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages> |
| 710 | Reseller / Non-compliant KYC | The brand sending the messages must be the one registered, not the agency behind it. |
| 711 | Repeated Use of Same EIN for Multiple Brands | Requires a valid explanation for the repeated use of EINs. |
| 712 | Misleading Registration; Campaign appears to be Direct Lending Arrangement but appropriate Content Attribute was not selected | Direct lenders must mark themselves as such during campaign registration. |
| 713 | Large Companies Using Non-Official Email Domains | Large companies should use official email domains to prevent fraud risks. |
| 801 | Not Sole Proprietor; Does not meet small business Sole Prop (EIN) criteria set by TCR and mobile carriers | If the company is an LLC, Inc, Ltd, Corp, etc, they must register a brand with an EIN. |
| 802 | Sole Proprietor Not Yet Authorized | Requires authorization to use Sole Proprietor cases. |
| 803 | Call to Action forces an Opt-In consent because it is missing the "Check Box"; Check box either not present or mandatory causing a forced opt in | If the phone number field and checkbox are both mandatory fields, one must be changed to an optional field.    If the phone number field is mandatory but there is no checkbox beside the opt-in language, one must be added (unchecked and an optional field) or the phone number field must be changed to an optional field. |
| 804 | Unable to verify, need working website or online presence provided for brand validation | No website link was provided in the Website/Online Presence field under the brand details.    Website link provided does not work.    Website provided does not provide any details about the brand. The carriers require validation of the brand's identifying information including the business address, phone number, and email on the home page, an about section, and a clear description of its core business activities and services. |
| 805 | Compliant privacy policy is required; add link and/or verbiage for compliant Privacy Policy disclosures (state that no mobile opt-in data will be shared with third parties) | The Call to Action does not contain privacy verbiage or a link to a compliant privacy policy.    The privacy policy must state that SMS opt-in data will not be shared with third parties. |
| 806 | Unable to verify, needs compliant and accurate CTA information. Update with specific path for mobile opt-in, HELP instructions, STOP instructions, message frequency disclosure, "message and data rates may apply" disclosure and link to the message program privacy policy, or language referring to the privacy policy | The Call to Action does not contain either HELP language, STOP language, message frequency, data rates, or privacy policy link or language. If the campaign has a marketing use case make sure the CTA mentions that marketing messages will be sent.    The message flow does not provide a path as to how someone gets to the opt-in form if it is not on the main webpage.    The digital opt-in form is giving an error message when submitting. |
| 851 | Privacy Policy and Opt-in Confirmation Requirements Not Met | Privacy policy must include disclaimers about third-party data sharing, and opt-in messages must include program name, opt-out instructions, and support contact details. |
| 852 | Privacy Policy Compliance Missing | Privacy policy must clearly indicate that mobile opt-in data is not shared with third parties. |
| 861 | Needs compliant and accurate CTA information; update with specific path for mobile opt-in, HELP instructions, STOP instructions, message frequency disclosure, "message and data rates may apply" disclosure and link to the message program privacy policy, or language referring to the privacy policy. Opt-in message/Confirmation MT must contain brand name, HELP, opt-out, message frequency and associated fees disclosures. Opt-out message must contain brand name and indicate that no further messages will be sent. HELP message must contain brand name and contain support contact (email, phone number, or support website). | The Call to Action does not contain either HELP language, STOP language, message frequency, data rates, or privacy policy link or language. If the campaign has a marketing use case make sure the CTA mentions that marketing messages will be sent.    Opt-in, Opt-out and Help confirmation messages must contain details provided here: <https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages> |
| 807 | Unable to Verify, Inauthentic Website | Specifically for real estate and insurance companies using incomplete websites that don't allow business verification. |

---

Related Articles

[How to create a 10DLC campaign](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign)[10DLC Campaign Approval Best Practices](https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices)[Messaging - 10DLC Campaign Checklist](https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist)[10DLC Campaign Compliance Requirements](https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements)[10DLC for Chiropractors](https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors)

Did this answer your question?

😞😐😃
