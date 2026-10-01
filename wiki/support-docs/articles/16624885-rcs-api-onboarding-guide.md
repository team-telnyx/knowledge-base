---
title: "RCS API Onboarding Guide"
summary: "Use the Telnyx API to register, test, and launch a US RCS agent. For agents launching outside the United States, please use the RCS application form from the Mission Control Portal.\\ ​\\ ​Before you begin"
sources:
- url: "https://support.telnyx.com/en/articles/16624885-rcs-api-onboarding-guide"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16624885-rcs-api-onboarding-guide.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16624885-rcs-api-onboarding-guide.md -->

# RCS API Onboarding Guide

Use the Telnyx API to register, test, and launch a US RCS agent. For agents launching outside the United States, please use the RCS application form from the Mission Control Portal.\
​\
​**Before you begin**

Gather the following information before starting:

- A Telnyx account with an API key
- A Messaging Profile ID
- Legal business details, including the legal name, tax identifier, registered address, website, and contact
- Public HTTPS URLs for the agent logo, hero image, privacy policy, and terms and conditions

RCS registration is asynchronous. A successful API response confirms that Telnyx accepted the request; it does not mean that external review is complete. Retrieve the brand or agent to monitor its current status.

Before submitting an agent, please review the [RCS Fees and Charges](https://support.telnyx.com/en/articles/16624343-rcs-fees-and-charges)

## **Stage 1: Create and test the agent**

## **Step 1: Create the brand**

API endpoints: POST /v2/rcs/brands; GET /v2/rcs/brands/{brand\_id}; PATCH /v2/rcs/brands/{brand\_id}

Create the brand record from the organization’s official registration details. The following fields are required:

- **display\_name** — The customer-facing brand name. Use the name recipients will recognize; it may differ from the registered legal name.
- **legal\_name** — The organization’s full registered name. It must match the name associated with the tax identifier and registered address.
- **legal\_entity\_type** — The legal structure of the business: LIMITED\_LIABILITY\_COMPANY, SOLE\_PROPRIETORSHIP, PARTNERSHIP, CORPORATION, or S\_CORPORATION.
- **organization\_type** — How the organization operates: PRIVATE\_PROFIT, PUBLIC\_PROFIT, NON\_PROFIT, GOVERNMENT, or UNKNOWN. Use UNKNOWN only when none of the other categories applies.
- **website\_url** — The organization’s public website. Use a working HTTPS page that clearly identifies the same business named in the registration.
- **identifiers** — The business identifiers used for verification. Provide the EIN under the ein key. For a PUBLIC\_PROFIT organization, also provide the stock symbol under stock\_symbol.
- **addresses** — The registered primary business address, including street, city, state or administrative area, postal code, and country code. Use the address associated with the legal entity and EIN.
- **contacts** — The authorized brand contact’s first name, last name, title, business email address, and phone number. Use a contact who can respond to verification questions. A personal email address must be used, group emails such as info@ or support@ are not permitted for brand verification. Freemails such as gmail are also not permitted.

profile\_id is optional. If provided, it must identify a Messaging Profile owned by your Telnyx organization. Agents can inherit this profile from the brand.\
​

## **Before submitting the brand**

Check the complete record before starting verification:

- The legal name, EIN, and registered address match the same legal entity.
- The website is live and clearly connected to that entity.
- The legal entity type and organization type describe different attributes and have both been selected correctly.
- A public company includes its stock symbol.
- The brand contact details are current and monitored.

Save the returned brand ID. The brand remains editable while its status is CREATED; its registration fields are locked after submission.

## **Step 2: Create the agent basics**

API endpoints: POST /v2/rcs/agents; GET /v2/rcs/agents/{agent\_id}; PATCH /v2/rcs/agents/{agent\_id}

Create the agent under the verified brand. The request requires an Idempotency-Key header and the following top-level fields:

- **brand\_id** — The verified brand that owns the agent.
- **display\_name** — The name recipients will see in their messaging application. The maximum length is 40 characters.
- **use\_case** — The type of traffic the agent will send. Select one of the supported values described below.
- **configuration.basics** — The agent’s visible identity, branding, legal pages, and contact options.

profile\_id and hosting\_region are optional. If profile\_id is omitted, the agent inherits the Messaging Profile assigned to the brand.

## **Use cases**

- **OTP** — One-time passwords and authentication codes only. Do not use this category for account notifications, order updates, support, or promotions.
- **TRANSACTIONAL** — Non-promotional messages tied to an existing transaction or service relationship, such as order updates, appointment reminders, and account alerts. Promotional content is not permitted under this category.
- **PROMOTIONAL** — Advertising, offers, product announcements, and other marketing traffic. The consent flow and sample messages must clearly cover promotional messaging.
- **MULTI\_USE** — A combination of transactional and promotional use cases. Describe every message type, include representative samples for each, and ensure the consent flow covers promotional traffic whenever promotions are included.

**N.B. Only select Mutli-Use if you will actually send promotional messages. You must show promotional samples for carrier verification and launch**\
​

Note that the use-case is visible on the Agent information screen on iOS devices.

## **Required basics fields**

- **description** — A plain-language description of the messages or interactions recipients will receive. Maximum 100 characters; do not use a marketing slogan.
- **logo\_url** — A public URL for a 224 × 224 pixel PNG or JPEG, maximum 50 KB.
- **hero\_url** — A public URL for a 1440 × 448 pixel PNG or JPEG, maximum 200 KB.
- **brand\_color** — A six-digit hex color. A color with at least 4.5:1 contrast against white is required.
- **privacy\_policy\_url** — A public page describing how personal data is collected and used.
- **terms\_and\_conditions\_url** — A public page containing the service terms that apply to the messaging program.

## **Contact options**

One of “phone number” or “email” must be provided. You may add all three:

- **phone\_number** — An E.164 phone number and a customer-facing label, such as “Support”.
- **website** — A public URL and a customer-facing label, such as “Website”.
- **email** — A monitored email address and a customer-facing label, such as “Customer Care”.

Each contact label can contain up to 25 characters. Use contact details that recipients can use to reach the business.\
​

## **Before creating the agent**

- Confirm that the brand is CREATED.
- Confirm that the display name, description, assets, legal pages, and contact options are final.
- Confirm that the selected use case matches every planned production message.
- Use one stable idempotency key for this logical agent creation. If the response is uncertain, retry with the same key and identical request body.

Save the returned agent ID and retrieve the agent to confirm the stored values. Agent fields can be updated while the agent status is CREATED.\
​

## **Step 3: Add test devices and test the integration**

API endpoints: POST /v2/rcs/agents/{agent\_id}/test\_devices; GET /v2/rcs/agents/{agent\_id}/test\_devices;

When your agent is in test status you can send messages to numbers that have been added as a tester and have accepted the invitation. Add each RCS-capable test number in E.164 format. For US agents, T-Mobile and AT&T numbers cannot be added as test devices.

Create or select a Telnyx Messaging Profile and configure the webhook URLs. During testing, confirm that your integration can:

- Send text and rich-content messages.
- Receive inbound messages and suggestion responses.
- Process delivery updates and read receipts.
- Process START, STOP, and HELP behaviour.

**Stage 2: Submit the agent for verification and launch**

**Step 4: Submit and verify the brand**

API endpoints: POST /v2/rcs/brands/{brand\_id}/submit; GET /v2/rcs/brands/{brand\_id}

When the agent has been tested, and you are ready to move forward submit the brand to begin verification, then retrieve it until its status is VERIFIED. Do not create or submit an agent under a brand that has not been verified. If the brand is REJECTED or FAILED, review the result before starting another registration.

**N.B. Submitting the brand triggers the $100 brand vetting fee. Do not submit the brand if you do not want to move ahead with carrier verification and launch.**

## **Step 5: Submit the agent basics**

API endpoints: POST /v2/rcs/agents/{agent\_id}/submit; GET /v2/rcs/agents/{agent\_id}

Submit the basics only after validating the complete agent record. This action starts carrier provisioning and agent review.

Submitting basics locks the basics section for review. The campaign and testing sections remain editable until they are submitted. Retrieve the agent and monitor basics\_status:

- **SUBMITTED** — The basics were accepted and provider processing is underway.
- **APPROVED** — The basic agent configuration passed review.
- **REJECTED** — The basics did not pass review. Telnyx will follow up by email with the rejection details and any required corrections before resubmission.

## **Step 6: Add the campaign and testing information**

API endpoint: PATCH /v2/rcs/agents/{agent\_id}

After submitting basics, add configuration.campaign and configuration.testing to the agent. You can patch either object independently and update it incrementally until that section is submitted. The basics section remains locked. Include the following carrier-review information:

- Company and agent overviews
- The interaction types supported by the agent
- Representative production message examples
- Opt-in methods, call-to-action text and URL, and any supporting media
- Opt-in, help, and opt-out responses
- A publicly accessible testing video that demonstrates the confirmation message, example interactions, HELP and STOP.

## **Step 7: Submit the agent for launch**

API endpoint: POST /v2/rcs/agents/{agent\_id}/launch

Submit the completed campaign and testing objects through the launch request. Include both objects in the request body as required by the Telnyx endpoint. The launch operation submits campaign before testing, starts asynchronous carrier launch, and tracks the external review process.

The launch request submits the campaign and testing information together, but their review results are tracked separately in campaign\_status and testing\_status. Retrieve the agent and monitor both fields:

- **SUBMITTED** — Telnyx accepted the section and provider review is underway.
- **APPROVED** — The section passed review.
- **REJECTED** — The section did not pass review. Telnyx will follow up by email with the rejection details and any required corrections before resubmission.

**N.B. Note that the T-Mobile launch fee of $500 will be applicable once the carrier approves the agent. This review is triggered by submitting the agent for launch.**\
​

## **Step 8: Monitor the launch status**

API endpoints: GET /v2/rcs/agents/{agent\_id}; GET /v2/rcs/agents/{agent\_id}/carrier\_approvals

Retrieve the agent until its status becomes LIVE. The agent response includes section statuses, test devices, carrier approvals, and provider capabilities. If the status is REJECTED or FAILED, review the returned details before correcting or resubmitting the agent.\
​

**N.B. Note that the T-Mobile launch fee of $500 will be applicable once the carrier approves the agent.**\
​

## **Step 9: Go live**

API endpoint: POST /v2/messages/rcs

Once the agent is LIVE, send production traffic using the Telnyx RCS messaging endpoint. Continue to monitor message webhooks and delivery results, and keep the published business and customer-care information current.\
​

## **Telnyx API documentation**

- [Register an RCS Agent — Quickstart](https://developers.telnyx.com/docs/messaging/rcs/agent-registration)
- [RCS Brands API](https://developers.telnyx.com/api-reference/rcs-brands/create-an-rcs-brand)
- [RCS Agents API](https://developers.telnyx.com/api-reference/rcs-agents/create-an-rcs-agent)
- [Send RCS Messages](https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started)
- [Receiving RCS Webhooks](https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks)

---

Related Articles

- [API Keys and How to Use Them](https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them)
- [Guide to Sole Proprietor 10DLC Brand and Campaign Registration](https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration)
- [Bot-to-Bot Support API: Ask Telnyx Knowledge Agent](https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent)
- [RCS Fees and Charges](https://support.telnyx.com/en/articles/16624343-rcs-fees-and-charges)
- [RCS Agent Submission Form — Field-by-Field Guide](https://support.telnyx.com/en/articles/16624919-rcs-agent-submission-form-field-by-field-guide)
