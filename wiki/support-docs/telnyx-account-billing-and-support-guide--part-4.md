---
title: Telnyx Account, Billing, and Support Guide
summary: This page consolidates Telnyx account, billing, and support guidance, covering
  account types (including Freemium and Managed Accounts), billing setup, payment
  methods, invoices, billing groups, notification settings, the AI Chat Support Assistant,
  feature requests, bug reports, security vulnerability disclosure, and sending test
  messages via the Learn and Build feature in the Mission Control Portal.
sources:
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/4277896-notification-settings
- url: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups
- url: https://support.telnyx.com/en/articles/4283783-feature-requests
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
- url: https://support.telnyx.com/en/articles/6987563-invoice-overview
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
updated_at: 2026-07-17T09:04:25Z
---

# Telnyx Account, Billing, and Support Guide

*Part 4 of 5 — see also: [Part 1](telnyx-account-billing-and-support-guide--part-1.md), [Part 2](telnyx-account-billing-and-support-guide--part-2.md), [Part 3](telnyx-account-billing-and-support-guide--part-3.md), [Part 5](telnyx-account-billing-and-support-guide--part-5.md)*

This page consolidates Telnyx account, billing, and support guidance, covering account types (including Freemium and Managed Accounts), billing setup, payment methods, invoices, billing groups, notification settings, the AI Chat Support Assistant, feature requests, bug reports, security vulnerability disclosure, and sending test messages via the Learn and Build feature in the Mission Control Portal.

## AI Chat Support Assistant

The AI Assistant is accessible through the Mission Control Portal. Click "Ask our AI Assistant" in the left-hand side navigation bar, and the widget will pop up from the bottom right-hand side of your portal account.

### How to Interact

The AI Assistant pulls from the Support Center, Developer Docs, and main website to deliver relevant info instantly. It has read-only access to your portal account resources that can help troubleshoot. If the Assistant can't solve it, you can connect directly with a live agent from the widget or by clicking "Chat with us" on the left-hand side navigation.

After asking a question and receiving a response, you'll be given two buttons: **"Chat to Support"** or **"That helped"**. Select "Chat to Support" to speak with an agent, or "That helped" if the response resolved your question. To ask another question, type into the chat box and enter your next question.

### What the AI Assistant Can Cover

- **General Customer Support** — Answers to common questions about services from Support Center documentation.
- **Developer Support** — Questions about APIs, coding questions, SDKs, and more. The AI can provide code snippets (specify this in your question) and recommend relevant documentation.
- **Self-Service Support** — First-level support that can guide you through creating a support ticket or starting a chat with agents.
- **24/7 Availability** — Available around the clock, though as a third-party service it may experience degradation from time to time. The assistant is not designed to replace human interaction but complements the human support team by handling routine inquiries. Provide feedback via the thumbs up and thumbs down buttons on a per-message basis.

### Limitations

The AI Assistant may not handle complex queries or requests that require human intervention. In such cases, use the "Chat to Support" feature. Conversation history is not stored in the widget, so if you refresh your portal or log out, the conversation will not be retrieved.

### Data and Privacy

By using the AI Assistant:

- You agree to the processing of personal data necessary for the provision of chat services.
- You acknowledge and consent to have your data stored and processed by Telnyx in the United States.
- You agree to have your data transferred to OpenAI, a subprocessor located in the United States, who assists in processing interactions with the AI Assistant.
- Telnyx retains personal data as long as necessary to provide services or as required by law.
- Services involve automated decision-making, including the use of artificial intelligence to process interactions.
- The assistant may return incorrect or outdated information — contact a member of the support team to have queries clarified.

## Feature Requests

A feature request allows users to request helpful features that are not currently supported in the Mission Control Portal.

### How to Submit a Feature Request

1. Log in to the Telnyx Portal at portal.telnyx.com.
2. Locate the question mark (?) icon in the far-right corner of the portal's top navigation bar.
3. Click the question mark icon to open the drop-down menu.
4. Select "Feature Request" from the menu options.
5. Click **submit idea** in the top right corner of the page.
6. Enter the following details into the form and click **submit**:
   - Feature Request
   - Importance of Feature
   - Email Address

You can also view planned features, features being implemented, and features under consideration on this page. Clicking into these features allows you to select one of three options: **Nice-to-have**, **Important**, and **Critical**. You'll be notified via the email entered if any further developments are made with your feature request.

### Special Note

From time to time, users may also provide improvement suggestions via chat or email. Telnyx has a feedback loop where the support team can tag your case as a feature request, allowing product managers to be notified internally on your suggestions. This allows them to review your case and potentially have the improvement included on the public product board.

## Bug Reports

Telnyx is engineering focused, agile, and iterates quickly, shipping improvements and new features regularly. Customers are encouraged to identify any improvements, especially bugs, by contacting the support team at support@telnyx.com. A detailed description of the bug, as well as any screenshots or videos, is appreciated.

The Mission Control Portal user interface is built on top of the Telnyx API, so checking browser console logs (front-end issues) or network logs (back-end issues) can significantly help reproduce concerns.

### Step-by-Step Guide

1. Let the support team know what browser you are using and the version.
2. Open the developer tools by pressing F12 or right-clicking and selecting "Inspect" or "Inspect element".
3. Navigate to the website page with the issue.
4. For back-end issues, click the "Network" tab to inspect network traffic. Save a HAR file by right-clicking the failing request and clicking "save har file".
5. For front-end issues, click the "Console" tab to inspect console logs. Filter by type such as "Errors" or "Warnings". If you see red logs, right-click the whitespace and save the console logs.

If the bug is mission critical (service affecting), open a chat with support for immediate investigation.

### Security Related Bugs

If you believe you have found a security vulnerability, report it to security@telnyx.com rather than general support. Telnyx welcomes responsible security research on its products and infrastructure.

**In scope:** Telnyx-owned web applications, APIs, and infrastructure, including portal.telnyx.com, api.telnyx.com, and other *.telnyx.com properties.

**Out of scope:** Third-party services and integrations, physical security, social engineering against employees, and denial-of-service testing.

**What Telnyx is looking for:** Vulnerabilities with demonstrated, real-world security impact, such as remote code execution, injection flaws, authentication or authorization bypass, access to other users' data, and significant data exposure.

**What doesn't qualify:** Configuration hardening suggestions without a working exploit, informational findings with no demonstrated security impact, issues requiring unlikely user interaction, automated scanner output without manual validation, and telecom service abuse, carrier routing, or call quality issues.

**Report requirements:** A description of the vulnerability and affected component, step-by-step reproduction instructions, proof of concept (screenshots, requests and responses, video, or exploit code), and demonstrated impact.

**Rules:** Do not access or modify other users' data, do not degrade service availability, test only against your own accounts, do not disclose the issue publicly before Telnyx has had reasonable time to remediate, and stop and report immediately if you encounter customer data.

**Rewards:** Telnyx may offer rewards for qualifying reports at its sole discretion, based on severity, exploitability, and impact. Informational findings and out-of-scope reports are not eligible.

**Submission:** Send security reports to security@telnyx.com with the subject `[Vulnerability Report] <Brief Description>`.

**Safe Harbor:** Telnyx will not pursue legal action against researchers who act in good faith, follow this policy, and report findings to Telnyx before any public disclosure.
