---
title: 10DLC Campaign Registration and Compliance Guide
summary: A consolidated reference for registering and maintaining 10DLC (10-Digit
  Long Code) A2P messaging campaigns on Telnyx, covering message flow, opt-in forms,
  keywords, privacy policy, sample messages, vetting, shared campaigns, and common
  carrier errors.
sources:
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-08-05T13:25:10Z
---

# 10DLC Campaign Registration and Compliance Guide

*Part 5 of 5 — see also: [Part 1](10dlc-campaign-registration-and-compliance-guide--part-1.md), [Part 2](10dlc-campaign-registration-and-compliance-guide--part-2.md), [Part 3](10dlc-campaign-registration-and-compliance-guide--part-3.md), [Part 4](10dlc-campaign-registration-and-compliance-guide--part-4.md)*

A consolidated reference for registering and maintaining 10DLC (10-Digit Long Code) A2P messaging campaigns on Telnyx, covering message flow, opt-in forms, keywords, privacy policy, sample messages, vetting, shared campaigns, and common carrier errors.

## Consistency and Accuracy (Errors 602 and 603)

Carriers review campaigns for consistency and accuracy. If you receive one of the following errors after submitting a campaign for carrier review, check the listed fields for consistency:

- **Inaccurate Registration. Inconsistency between Brand, website, description, Call to Action and/or sample messages (603).**
- **Inaccurate Registration. Inconsistency between sample message, description, attributes and/or call to action with selected use-case. (602).**

For example, selecting a marketing use case but having the campaign description, message flow, opt-in form, website, and sample messages describe a different use case is inconsistent and will be declined. A campaign description for a mechanic's shop paired with a website for an accounting firm is also inconsistent.

Check the following fields for consistency and accuracy:

1. Use cases selected at the time of campaign creation.
2. Website provided on the brand page and in the message flow (if digital opt-in).
3. Campaign description.
4. Message flow and opt-in form.
5. Sample messages.

## Error 806: Non-Compliant CTA

**10DLC Error (806): Unable to verify, needs compliant and accurate CTA information. Update with specific path for mobile opt-in, HELP instructions, STOP instructions, message frequency disclosure, "message and data rates may apply" disclosure and link to the message program privacy policy, or language referring to the privacy policy.**

This error relates to the Message Flow field. In plain terms, the carriers checked the message flow and it either did not sufficiently document or did not contain a compliant opt-in process. Make sure the opt-in path is clear and the opt-in method has the required disclaimers. Update the message flow to follow one of the standard formats and update the opt-in form to contain all necessary disclaimers.

## Shared Campaigns

A shared campaign is a campaign registered directly through The Campaign Registry rather than created through the Telnyx account. In shared campaigns, a connectivity partner (CNP) is selected to provide messaging services. When bringing a shared campaign to Telnyx from the Campaign Registry, Telnyx acts as the upstream CNP for the campaign, the organization is the downstream CNP, and Telnyx in turn shares the campaign with MNOs (the upstream CNPs for Telnyx).

![Shared campaign diagram](_images/5f11b6e430a16d3d.png)

Using shared campaigns limits Telnyx's ability to troubleshoot issues with 10DLC campaigns and throughput. In most cases, Telnyx recommends creating brands and campaigns through the Telnyx portal.

### Importing Campaigns from The Campaign Registry

To import campaigns from The Campaign Registry to Telnyx, first provide your CSP ID to Telnyx. The CSP ID is set by The Campaign Registry and can be found in the [Campaign Registry CSP Portal](https://csp.campaignregistry.com/login). Share the ID with your account manager or support representative, or email [support@telnyx.com](mailto:support@telnyx.com). The team will associate the CSP ID with the Telnyx account, which usually takes up to two business days.

Once confirmed, in the Campaign Registry CSP Portal, choose the campaign to share and select Telnyx as the connectivity partner. This submits a request to the Telnyx team to review and approve the shared campaign. After approval, Telnyx will show as the connectivity partner for the campaign in the CSP Portal.

### Adding Telnyx Numbers to Shared Campaigns

Once Telnyx is verified as the connectivity partner, Telnyx numbers can be assigned to the shared campaign. The only way to associate Telnyx numbers with shared campaigns is via the [Bulk Phone Number Campaigns endpoint of the Telnyx API](https://developers.telnyx.com/api/messaging/10dlc/post-assign-messaging-profile-to-campaign). Before making the request, ensure all numbers to add are associated with the same Messaging Profile in the Telnyx account. The Messaging Profile ID can be found in the [portal](https://portal.telnyx.com/#/app/messaging) or [by API](https://developers.telnyx.com/api/messaging/list-messaging-profiles). The TCR ID of the shared campaign is available in the Campaign Registry CSP Portal.

After the API request, the status of the [entire request](https://developers.telnyx.com/api/messaging/10dlc/post-assign-messaging-profile-to-campaign) or [individual numbers](https://developers.telnyx.com/api/messaging/10dlc/post-assign-messaging-profile-to-campaign) can be checked via the Telnyx API.

### Shared Campaign FAQ

- **Telnyx CSP ID:** SS4XJ6D.
- **Updating TCR Brand/Campaign through the Telnyx portal:** Shared campaigns cannot be updated through the Telnyx portal. All brand and campaign information is maintained directly through the Campaign Registry CSP Portal. Telnyx has limited visibility into the details of the campaign and corresponding brand.
- **Editing a campaign sharing request:** Once the organization has submitted a shared campaign by selecting Telnyx as the upstream CNP, and while the sharing status is in the `PENDING` state, the organization (as the downstream CNP) cannot rescind the sharing request or change the upstream CNP.

## Telnyx Privacy Policy

Telnyx's privacy policy provides important information about how Telnyx handles personal information in line with the General Data Protection Regulation 2016/679. The full privacy statement is available at [telnyx.com/privacy-policy](https://telnyx.com/privacy-policy) and details how personal data is collected and treated. By supplying personal data through the Telnyx website or via staff email addresses, you implicitly declare that you have taken notice of the privacy policy and concur with the use of your personal data.

GDPR and CCPA rights requests are responded to within one month. To exercise any applicable rights, submit a request at [telnyx.com/request-to-control-review-data](https://telnyx.com/request-to-control-review-data).

![Breaking Line](_images/682991ade0be9812.png)

## Related Articles

- [Guide to 10DLC Message Flow Field](guide-to-10dlc-message-flow-field.md)
- [10DLC Keywords and Confirmation Messages](10dlc-keywords-and-confirmation-messages.md)
- [10DLC Privacy Policy](10dlc-privacy-policy.md)
- [10DLC Opt in Form](10dlc-opt-in-form.md)
- [10DLC Inaccurate or Inconsistency Error](10dlc-inaccurate-or-inconsistency-error.md)
- [10DLC Error (806)](10dlc-error-806.md)
- [Telnyx Privacy Policy](telnyx-privacy-policy.md)
- [10DLC Shared Campaigns](10dlc-shared-campaigns.md)
- [Bring Campaigns to Telnyx](bring-campaigns-to-telnyx.md)
- [10DLC: Trust Scores & Use Cases](10dlc-trust-scores-use-cases.md)
- [10DLC Campaign Approval Best Practices](10dlc-campaign-approval-best-practices.md)
- [Messaging - 10DLC Campaign Checklist](messaging-10dlc-campaign-checklist.md)
- [10DLC Campaign Compliance Requirements](10dlc-campaign-compliance-requirements.md)
