---
title: "RCS Fees and Charges"
summary: "Telnyx RCS charges fall into three categories: onboarding fees, recurring agent fees, and messaging usage.\\ ​\\ ​Onboarding fees"
sources:
- url: "https://support.telnyx.com/en/articles/16624343-rcs-fees-and-charges"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16624343-rcs-fees-and-charges.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16624343-rcs-fees-and-charges.md -->

# RCS Fees and Charges

Telnyx RCS charges fall into three categories: onboarding fees, recurring agent fees, and messaging usage.\
​\
​**Onboarding fees**

The following fees apply to US RCS agents. All amounts are in USD.

## **Carrier provisioning fee**

The fee applies once T-Mobile has approved the agent for launch.

- **T-Mobile/U.S. Cellular provisioning — $500**

## **Brand and agent vetting fees**

The following fee applies when the agent is submitted for vetting. Note that is triggered when basics object is submitted - <https://developers.telnyx.com/api-reference/rcs-agents/submit-rcs-agent-basics>

- **Brand and Agent Vetting Fee / Annual Renewal — $100**

The following fees may apply if there are issues with the initial vetting or if you request changes after vetting is completed.

- **Appeal Fee — $11**
- **Invalid Tax ID — $12:** Applies if Aegis rejects the brand because the tax ID is invalid or does not match.
- **POC Change — $12:** Applies if the brand is already in vetting and its point of contact changes.
- **Migration — $12**
- **Expired PIN — $54:** Aegis expires the PIN 45 days after submission if the brand does not respond. This fee applies if the PIN must be reissued.
- **RCS Logo Verification Update — $22:** Applies when a logo change is requested after vetting is complete.
- **RCS Banner Verification Update — $22:** Applies when a banner change is requested after vetting is complete.
- **Agent Name Change — $22**

For current onboarding fees for other markets, please reach out to your account manager or [rcscompliance@telnyx.com](mailto:rcscompliance@telnyx.com)\
​

## **Monthly agent maintenance fee**

For US Agents, a monthly maintenance fee of $100 applies per agent.

For current monthly fees for other markets, please reach out to your account manager or [rcscompliance@telnyx.com](mailto:rcscompliance@telnyx.com).

## **Messaging usage**

RCS message charges depend on the destination, message classification, direction, destination carrier, and any applicable carrier pass-through fee. The United States uses a different billing model from other countries:

## **Global definitions:**

- **Basic messages** – Text only, up to 160 characters (UTF-8). Emojis take up 2-4 characters.
- **Rich messages** – An RCS message type that includes multimedia elements such as images, videos, suggested replies and action buttons, or text over 160 characters.

**US-only definitions:**

- **Rich messages (former Basic messages)**  –

  - Text up to 160 characters (UTF-8). Emojis take up 2-4 characters. If text exceeds 160 characters then multiple message segments are charged (similar to SMS).
  - Suggested Replies
  - Suggest Action: Open URL (Browser only, no webview)
  - Suggested Action: Dial Number
- **Rich Media messages** **(former Rich messages)**– An RCS message type that includes multimedia elements such as images, videos, and suggested replies and actions other than those listed above.

## **Other usage charges**

- **Inbound traffic:** In the US, inbound messages are charged per the relevant message types listed above. In other markets, inbound messages are not charged.
- **Carrier pass-through fees:** In the US, carrier pass-through fees apply in addition to the Telnyx message rate.

Current pay-as-you-go message and carrier rates are published on the [Telnyx Messaging pricing page](https://telnyx.com/pricing/messaging). Your account's contracted pricing, if any, takes precedence.

Charges are generally non-refundable once the corresponding external provisioning or vetting action has started.

## **Billing model**

Currently all agents will be created with the non-conversational billing model by default. Telnyx does not currently support the conversational billing model.

---

Related Articles

- [Frequently asked questions about 10DLC](https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc)
- [10DLC Fees and Charges](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges)
- [10DLC: Trust Scores & Use Cases](https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases)
- [RCS API Onboarding Guide](https://support.telnyx.com/en/articles/16624885-rcs-api-onboarding-guide)
- [RCS Agent Submission Form — Field-by-Field Guide](https://support.telnyx.com/en/articles/16624919-rcs-agent-submission-form-field-by-field-guide)
