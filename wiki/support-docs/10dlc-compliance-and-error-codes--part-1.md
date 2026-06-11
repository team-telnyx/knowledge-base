---
title: 10DLC Compliance and Error Codes
summary: A comprehensive reference for 10DLC campaign compliance, covering carrier
  error codes and their resolutions, required keywords and confirmation messages,
  privacy policy verbiage, brand verification requirements, campaign suspension for
  inactivity, and SMS porting considerations for ported-in phone numbers.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
  content_hash: 9b6044d0b967707a06966ae9c750424519d3d24b6d0118951e910d3ae8f1afb7
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
  content_hash: 517aa55bed935632cdb945d6eef7257cf50aa3e98ea893be02332ddfbddd55c8
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
  content_hash: d42dcbd08bb330e0aa10504286cf75d33dcd7460d03daf8b7b267d00291933e2
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
  content_hash: c58866e0f474718c88333b11758004e24d0a2a29cbe655c05b629857b4914695
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
  content_hash: f20137527fe8638e63a766e07a8ad4c54c633ca3245a0cf011db94ca1d6e4dcc
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
  content_hash: 37dc405587bd56e3e374454fbad57992200523b656a9c987ad3e34d2ee3999d9
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
  content_hash: df854549a7915277c5db4ee826ccd16ccb0ccdd7353f26fa06513efe8a2fc298
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
  content_hash: 0dc27d88780519b11066b2c9a4588a820a35121dafa4b43726b72789af48e692
updated_at: 2026-06-11T11:10:54Z
---

# 10DLC Compliance and Error Codes

*Part 1 of 3 — see also: [Part 2](10dlc-compliance-and-error-codes--part-2.md), [Part 3](10dlc-compliance-and-error-codes--part-3.md)*

A comprehensive reference for 10DLC campaign compliance, covering carrier error codes and their resolutions, required keywords and confirmation messages, privacy policy verbiage, brand verification requirements, campaign suspension for inactivity, and SMS porting considerations for ported-in phone numbers.

## Carrier Error Codes

When a 10DLC campaign is declined during carrier review, an error code is returned. Below is a reference of all carrier error codes, their reasons, and explanations.

### Prohibited Content Errors (70x)

| Code | Reason | Explanation |
|------|--------|-------------|
| 701 | Prohibited Content; Cannabis | Any submission related to cannabis, including CBD, hemp, teas, beauty products, or derivatives, is subject to automatic rejection. This also includes shipping services. |
| 702 | Prohibited Content; Guns/Ammo | The sale of firearms and ammunition should have age verification. Educational content is acceptable if it does not engage in sales. |
| 703 | Prohibited Content; Explicit Sexual | Content promoting illegal sexual themes, non-consensual acts, or underage exploitation is prohibited. Includes content appearing family-friendly but containing adult themes. |
| 704 | Prohibited Content; Gambling | Covers participation in games of chance, including casino games, sports betting, lottery, and online gambling. Bingo promotions may be allowed under certain conditions with age gating. |
| 705 | Prohibited Content; Hate | Any form of hate speech, inappropriate content, or profanity is prohibited. |
| 706 | Prohibited Content; Alcohol (Age-Gated) | All content must adhere to laws and include a functioning age gate requiring date of birth verification at opt-in. The website needs a DD/MM/YYYY age gate as opposed to a simple "Are you over 21?" button. |
| 707 | Prohibited Content; Tobacco/Vape (Age-Gated) | Similar to alcohol, requires an age gate and legal compliance. |

### Lead Gen and Registration Errors (708–713)

| Code | Reason | Explanation |
|------|--------|-------------|
| 708 | Lead Gen/Affiliate Marketing Prohibited | Prohibits the sharing or selling of information to third parties for lead generation. Any mention of lead generation or SEO on the website would lead to a decline. |
| 709 | Lead Gen/Affiliate Marketing Prohibited (High-Risk Financial Services) | Includes payday loans, non-direct lenders, debt collection, credit repair programs, debt forgiveness services, crypto-related traffic, and stock trading traffic. |
| 710 | Reseller / Non-compliant KYC | The brand sending the messages must be the one registered, not the agency behind it. |
| 711 | Repeated Use of Same EIN for Multiple Brands | Requires a valid explanation for the repeated use of EINs. |
| 712 | Misleading Registration | Direct lenders and regulated entities must mark themselves as such during campaign registration. |
| 713 | Large Companies Using Non-Official Email Domains | Large companies should use official email domains to prevent fraud risks. |

### Inconsistency and Attribute Errors (60x)

| Code | Reason | Explanation |
|------|--------|-------------|
| 601 | Campaign Attributes Do Not Match Website and/or Sample Message Content | Business details on the website, attributes, and sample messages must be consistent. If Embedded Link/Embedded Phone number attributes are marked as YES, the message samples must contain a link/phone number. |
| 602 | Inaccurate Registration; Inconsistent Sample Message and Use-Case | Sample messages should align with the declared use-case. Most common when a marketing use case is chosen but not specifically mentioned in the Call to Action or the Message Flow section. |
| 603 | Inaccurate Registration; Inconsistent Website and Sample Messages | The business shown on the website should match the sample messages provided. |

If you receive error 602 or 603, carriers found inconsistency among your campaign fields. Check the following for consistency and accuracy:

1. Use cases selected at time of campaign creation
2. Website provided on the brand page and in the message flow (for digital opt-in)
3. Campaign description
4. Message flow and opt-in form
5. Sample messages

Each use case selected must have one representative sample message. A dedicated marketing use case or a mixed use case requires at least two sample messages. For example, if you select 2FA as a use case but your campaign description, opt-in form, and message flow describe Account Notifications or Marketing, that is inconsistent and will cause a decline. Similarly, if your campaign description describes traffic for a mechanic's shop but the website belongs to an accounting firm, the inconsistency will trigger a decline.

### Verification and Compliance Errors (80x)

| Code | Reason | Explanation |
|------|--------|-------------|
| 801 | Not Sole Proprietor | The business does not meet Sole Proprietor (EIN) criteria set by TCR and mobile carriers. |
| 802 | Sole Proprietor Not Yet Authorized | Requires authorization from Syniverse to use Sole Proprietor cases. |
| 803 | Opt-in Language Required on Website | If the website requires a phone number for contact, it must include opt-in language. |
| 804 | Unable to Verify Website/CTA Information | Incomplete or inaccessible call-to-action information on the website or broken links. |
| 805 | Non-Compliant Privacy Policy | The privacy policy must state that SMS opt-in data will not be shared with third parties. |
| 806 | Unable to Verify, Needs Compliant and Accurate CTA Information | The message flow or CTA does not contain HELP language, STOP language, message frequency, data rates, or privacy policy link/language. |
| 807 | Unable to Verify, Inauthentic Website | Specifically for real estate and insurance companies using incomplete websites that don't allow business verification. |

### Detailed Resolution for Error 806

Error 806 relates to the message flow field where the opt-in workflow is described. It means the message flow did not sufficiently document or contain a compliant opt-in process. To resolve:

- Update the message flow to follow the formats described in [Guide to 10DLC Message Flow Field](guide-to-10dlc-message-flow-field.md)
- Update the opt-in form to include all required disclaimers

For verbal opt-in, ensure the message flow section contains all necessary language. For online opt-in, make sure the CTA contains all of the following elements:

- Program (Brand) Name / Product Description
- Message frequency disclosure (e.g., "Message frequency may vary")
- "Standard Message and Data Rates may apply" (if non-FTEU)
- "Reply STOP to opt out" (opt-out information may appear in terms and conditions)
- "Reply HELP for help"
- Terms and conditions, or a link to terms and conditions (not a pop-up)
- Privacy policy, or a link to a privacy policy

### CTA and Privacy Policy Errors (85x–86x)

| Code | Reason | Explanation |
|------|--------|-------------|
| 851 | Privacy Policy and Opt-in Confirmation Requirements Not Met | Privacy policy must include disclaimers about third-party data sharing, and opt-in messages must include program name, opt-out instructions, and support contact details. |
| 852 | Privacy Policy Compliance Missing | Privacy policy must clearly indicate that mobile opt-in data is not shared with third parties. |
| 861 | CTA Information Incomplete | The CTA must contain program name, message frequency, opt-in disclosures, and links to terms and conditions. |
