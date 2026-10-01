---
title: "RCS Agent Submission Form — Field-by-Field Guide"
summary: "You should use this guide if you want to launch an agent in a market other than the US. For US agents, please use the provisioning API - <https://developers.telnyx.com/docs/messaging/rcs/agent-registration"
sources:
- url: "https://support.telnyx.com/en/articles/16624919-rcs-agent-submission-form-field-by-field-guide"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16624919-rcs-agent-submission-form-field-by-field-guide.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16624919-rcs-agent-submission-form-field-by-field-guide.md -->

# RCS Agent Submission Form — Field-by-Field Guide

You should use this guide if you want to launch an agent in a market other than the US. For US agents, please use the provisioning API - <https://developers.telnyx.com/docs/messaging/rcs/agent-registration>

Before submitting an agent, please review the [RCS Fees and Charges](https://support.telnyx.com/en/articles/16624343-rcs-fees-and-charges)\
​\
​**Business Information**\
​

## **Organization Name**

The full legal name of your business as it appears on official registration documents.

- **Example:** "Acme Technologies Inc."
- **Used for:** Brand verification with Google and carriers

## **Brand Name**

Your customer-facing brand name, if different from your legal organization name. Leave blank if your brand name and legal name are the same.

- **Example:** Organization is "Acme Technologies Inc." but brand is "Acme"

## **Contact First Name / Last Name**

The name of the person responsible who can approve RCS agent submission in the Brand Vetting stage.\
​

**Contact Title**

The job title of the contact person.

- **Example:** "Product Manager", "Head of Marketing", "CTO"

## **Contact Email**

A business email address for the contact person. This must be from your business domain — free email providers are not accepted for brand verification.

- ✅ **Accepted:** [name@yourcompany.com](mailto:name@yourcompany.com)
- ❌ **Not accepted:** Gmail, Yahoo, Hotmail, Outlook, or other free email addresses
- ❌ **Not accepted:** Generic addresses like info@, support@, admin@, hello@

The email must be a personal address at your business domain (e.g. [firstname@yourcompany.com](mailto:firstname@yourcompany.com)).

## **Contact Phone Number**

A direct phone number for the contact person, in international format.

- **Format:** +1XXXXXXXXXX (US) or appropriate country code
- **Example:** +14155551234

## **Industry**

Select your industry from the drop down list available.\
​

## **National Tax ID / Business ID**

The company’s EIN or business registration ID. Used for brand verification.\
​

## **Registered Company Address**

The official registered address of the business as it appears on your incorporation or registration documents.\
​

## **Company Trading Address**

The primary operating address, if different from the registered address. Leave blank if they are the same.\
​

## **Legal Form**

The legal structure of the business.

**Options:** Private, Public, Non-Profit, Government, Sole Proprietor

## **Legal Entity Type (US Only)**

If the business is US-based, select the applicable entity type.

**Options:** LLC, Sole Proprietorship, Partnership, Corporation, S Corporation

## **Company Stock Symbol**

If your company is publicly traded, provide the stock ticker symbol. Leave blank for private companies.

##

---

**Agent Details**\
​

## **Agent Display Name**

The name that appears at the top of the conversation thread when users receive messages from your RCS agent — similar to a contact name in their messaging app. 40 characters max.

- The display name should clearly identify the brand
- It doesn't need to exactly match the legal name, but it should be recognizable to customers and in line with branding
- Avoid marketing language, taglines, or promotional terms — names like "Acme - Best Deals!" will be rejected

## **Agent Use Case**

The category that defines what types of messages your agent will send. Selecting the correct use case is important — selecting the wrong one can cause your submission to be delayed.

|  |  |  |
| --- | --- | --- |
| Use Case | What You Can Send | What You Cannot Send |
| **OTP** | Verification codes, 2FA, password resets | Product info, promotions, marketing |
| **Transactional** | Order confirmations, shipping updates, appointment reminders, account alerts, fraud notifications | Promotional offers, discounts, marketing |
| **Promotional** | Sales offers, discounts, product launches, abandoned cart reminders | OTP codes, time-sensitive transactional messages |
| **Multi-use** | Combination of transactional AND promotional in the same conversation | Standalone OTP, transactional-only, or promotional-only messaging |

**Common mistake:** Selecting "Multi-use" when your agent only sends transactional messages (like order updates or reminders) without any promotional content. If you won't be mixing promotional offers into your transactional conversations, select "Transactional" instead.

Note that the use case is visible on the Agent information screen on iOS devices.

## **Agent Description (Display)**

A short description that appears when a user taps on your agent's profile. This tells recipients what kind of messages to expect from your agent.

- **Maximum:** 100 characters
- **Must describe the interactions users will have with your agent** — not what your company does

Think of it as answering: "What will this agent send me?"

**Good examples:**

|  |  |
| --- | --- |
| Use Case | Description |
| E-commerce | "Order confirmations, shipping updates & delivery tracking" |
| Appointments | "Appointment reminders, schedule changes, and booking confirmations" |
| Account alerts | "Account alerts, notifications, and security verification codes" |
| Support | "Get account support — FAQs, transaction tracking, and live agent help" |
| Promotions | "Exclusive deals and personalized offers based on your preferences" |

**Descriptions that will be rejected:**

- "Your trusted financial partner" — this is a tagline, not a description of interactions
- "Leading provider of healthcare solutions" — describes the company, not what messages users receive
- "Banking made simple" — marketing slogan with no indication of expected messages

## **Agent Description (Carriers)**

A longer description used during the carrier review process. This can provide more detail about how you plan to use RCS messaging, including:

- The types of messages you'll send
- How users will opt in
- Expected message frequency
- Your target audience

This description is not shown to end users — it's for the carrier review team only.\
​

## **Agent Logo**

A small image that appears as your agent's avatar next to messages, similar to a profile picture in a messaging app.

- **Dimensions:** 224 × 224 pixels (exact)
- **Maximum file size:** 50 KB
- **Accepted formats:** JPEG, JPG, or PNG

Your logo will display as small as 48×48 pixels on some devices, so keep it simple. A clean icon or logomark works better than a detailed wordmark at this size. Avoid fine text or intricate details.\
​

## **Banner / Hero Image**

A wider image that appears at the top of your agent's profile when a user taps on your agent's name on Android devices. This image does not appear in iOS devices.

- **Dimensions:** 1440 × 448 pixels (exact)
- **Maximum file size:** 200 KB
- **Accepted formats:** JPEG, JPG, or PNG

Use a clean, high-quality image that represents your brand. Avoid placing important content near the edges, as different devices may crop slightly.\
​

## **Brand Color**

Your brand color is displayed in the conversation header and other UI elements.

- **Format:** Hex color code (e.g. #1A73E8)
- **Requirement:** Must have a contrast ratio of at least **4.5:1 against white** (this is a Google accessibility requirement)

Before submitting, check your color at [WebAIM's Contrast Checker](https://webaim.org/resources/contrastchecker). Enter your hex color as the foreground and #FFFFFF as the background. If the ratio is below 4.5:1, choose a darker shade.

Colors that commonly fail: light blues, yellows, pastels, light greens. If your submitted color doesn't meet the contrast requirement, we'll substitute it with black (#000000) and let you know — you can request a change later.\
​

## **Webhook URL**

The URL where Telnyx will send delivery receipts and inbound message events for your RCS agent.

- **Must be HTTPS**
- Should return a 200 response to webhook POST requests
- Leave blank if you plan to configure this later through the API

---

**Contact & Online Presence**\
​

## **Primary Phone Number**

A phone number displayed on your agent's profile that users can tap to call your business.

- **Format:** E.164 international format (e.g. +14155551234)

## **Primary Phone Number Label**

A short label for the phone number shown to users.

- **Example:** "Customer Support", "Sales", "Main Office"

## **Primary Email**

An email address displayed on your agent's profile.\
​

## **Primary Email Label**

A short label for the email shown to users

1. **Example:** "Support Email", "Contact Us"

## **Primary Website**

Your business website URL, displayed on your agent's profile.

- Must be HTTPS
- Should be your main business website, not a social media page

## **Primary Website Label**

A short label for the website link shown to users.

- **Example:** "Visit Our Website", "Learn More"

## **Terms of Use URL**

A link to your terms of service or terms of use, displayed on your agent's profile.

- **Must be HTTPS**
- Must be publicly accessible (no login required)

## **Privacy Policy URL**

A link to your privacy policy, displayed on your agent's profile.

- **Must be HTTPS**
- Must be publicly accessible (no login required)
- Should describe how you handle user data in the context of messaging

##

---

---

**Checklist Before Submitting**

Before submitting your RCS agent, verify:

- Logo is exactly **224 × 224 px**, under 50 KB, in JPEG/JPG/PNG format
- Banner is exactly **1440 × 448 px**, under 200 KB, in JPEG/JPG/PNG format
- Brand color has a **4.5:1+ contrast ratio** against white ([check here](https://webaim.org/resources/contrastchecker))
- Agent description is **under 100 characters** and describes what messages users will receive
- Contact email is from your **business domain** (not Gmail/Yahoo/Hotmail)
- Privacy policy and terms of use URLs are **HTTPS and publicly accessible**
- Agent use case correctly reflects your messaging plans (don't select Multi-use unless you'll send both transactional and promotional)

---

Related Articles

- [Guide to 10DLC Message Flow Field](https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field)
- [WhatsApp Message Templates Guide](https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide)
- [How to use Telnyx AI Inference with Hermes Agent](https://support.telnyx.com/en/articles/16221027-how-to-use-telnyx-ai-inference-with-hermes-agent)
- [Toll-Free Submission Guide](https://support.telnyx.com/en/articles/16290008-toll-free-submission-guide)
- [RCS API Onboarding Guide](https://support.telnyx.com/en/articles/16624885-rcs-api-onboarding-guide)
