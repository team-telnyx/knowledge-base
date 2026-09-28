---
source_url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
title: "Mission Control Portal - AI Chat Support Assistant"
description: "Your new Telnyx AI Assistant here to help provide 24/7 support. See Telnyx guidance and requirements."
scraped: 2026-09-28
content_hash: d06216cefc44b24921b9e33b34ae68b1b40a5d637321bbe98513ce2a66a33718
updated_at: 2026-07-15T11:26:50Z
modified_at: 2026-07-15T11:26:50Z
---

# Mission Control Portal - AI Chat Support Assistant

# Mission Control Portal - AI Chat Support Assistant

We are delighted to introduce our latest digital offering, designed to enhance your customer service experience, while providing more efficient and personalised support. The advent of our new AI Assistant accessible through our [Mission Control Portal](https://portal.telnyx.com), marks another evolution in our service provision, complimenting our existing chat support service.

You can access the AI Assistant on the left hand side navigation bar, as seen in the image below. Simply click "Ask our AI Assistant" and the widget will pop up from the bottom right hand side of your mission control portal account.

![](_images/89cdbc243004f121.png)

![](_images/57ff75d8b75f1165.png)

## How to Interact with the AI Assistant

**Ask our AI Assistant:** Your go-to tool for answers about Telnyx products always at your fingertips.

It pulls from our **Support Center** (support.telnyx.com), **Developer Docs** (developers.telnyx.com), and **main website** (telnyx.com) to deliver the most relevant info instantly.

Whether it’s a simple question or a more technical one, the Assistant uses our documentation and has read-only access to your portal account resources that can help troubleshoot.

Get instant support anytime. And if the Assistant can’t solve it, you can still connect directly with a live agent from the widget or by clicking "**Chat with us**" on the left-hand side navigation.

![](_images/1bf4fdbf517004ba.png)

![](_images/9ba20d015d469710.png)

If you select "Ask our AI Assistant" and once you have asked a question and the assistant has responded you will be given two buttons: **"Chat to Support"** or **"That helped"**. If you want to speak with an agent then select "Chat to Support". If the response resolved your question then you select "That helped". If you want to ask another question then simply type into the chat box and enter your next question.

## What can the AI Assistant cover?

We list example topics the AI Assistant can cover below, and you can see common questions in the placeholder text box. To get the best out of the assistant it is of course recommended to provide context when asking questions. Otherwise, a few keywords may not be specific enough to provide you the answer you may be looking for.

Example Questions:

1. Hosted SMS?
2. Making calls?
3. How can I place an order for Hosted SMS?
4. How do I make calls with Call Control Voice API?

The first and second question will likely match a reference article across our websites but not specifically give you an answer to the information you may need for setup and configuration.

Instead, the third and fourth question will result in a specific set of instructions that can help you with the process on how to place an order for hosted SMS.

Elaborating on and mentioning the specific Telnyx products will help guide our assistant to providing you with the right answer!

In cases where the questions are considered to technical for the assistant to answer, you will be guided to our human support.

**General Customer Support**

- The assistant can provide answers to common questions about our services form our Support Center documentation.

#### **Developer Support**

- Developers can ask about our APIs, coding questions, SDKs, and much more. Our AI can provide code snippets (specify this in your question) and recommend relevant documentation.

#### **Self-Service Support**

- It's designed to provide first-level support. For more complex inquiries, our AI Assistant can guide you through the process of creating a support ticket or giving you the option to start a chat with our agents.

#### **24/7 Availability**

- Just like our Support team, our AI Assistant is available around the clock. However, as we're relying on a third party provider, it's possible it may experience degradation from time to time. We'll clearly display when the assistant is not performing at it's expected levels. It's important to note that while our AI assistant is highly capable, it's not currently designed to replace human interaction. Instead, it complements our human support team by handling more routine inquiries. However, Telnyx does have plans to continue to improve the assistant and user experience. The best way to provide feedback is by selecting the thumbs up and thumbs down buttons on a per message basis.

## Limitations and Complementary Use

While our AI Assistant is a powerful it may not be able to handle complex queries or requests that require human intervention. In such cases, we encourage you to use the "Chat to Support" feature to get in touch with our live support team but the goal is to continue to iterate.

Remember, our AI Assistant and our chat support system, work in synergy. They are designed to complement each other and ensure you receive efficient, accurate, and swift assistance whenever you need it. Conversation history is not stored in the widget at this time so if you refresh your portal or log out of your account, the conversation you had will not be retrieved.

---

## Accessing the AI Assistant through the A2A Protocol

In addition to accessing the AI Assistant through Mission Control Portal, customers can now connect their own AI agents directly to the Telnyx AI Assistant using the Agent-to-Agent, or A2A, protocol. A2A enables customer-built agents, applications, and automated workflows to programmatically ask the Assistant questions about Telnyx products, configuration, and account specific issues. This allows automated systems to receive the same first level support and troubleshooting guidance available to users in Mission Control Portal.

## What can customer agents do?

The A2A integration currently supports two primary capabilities:

**Ask documentation questions**

Customer agents can ask questions about Telnyx products, APIs, features, configuration, and recommended setup. Responses are generated using information from the Telnyx Support Center, Developer Documentation, and main Telnyx website.

**Troubleshoot account-specific issues**

When authenticated with a Telnyx API key, customer agents can ask the Assistant to investigate issues using read only access to relevant resources within the associated Telnyx account. Responses are scoped to the authenticated account.

The Assistant cannot make changes to an account, provision services, update configuration, or perform other write actions through the A2A interface.

## Connecting through A2A

Customer agents can send requests to the following endpoint:

`https://api.telnyx.com/v2/support_agent/support/a2a`

Requests must:

- Use the JSON-RPC 2.0 format.
- Be authenticated using a valid Telnyx API key.
- Include sufficient context for the Assistant to understand the product, resource, or issue being investigated.

Agents can also discover the Assistant’s available capabilities through its publicly accessible agent card:

`https://api.telnyx.com/v2/support_agent/support/a2a/.well-known/agent-card.json`

The agent card does not require authentication and describes the skills and functionality currently supported by the Telnyx AI Assistant.

## Why use A2A?

A2A support is designed for customers building AI agents that interact with Telnyx products and APIs. Instead of requiring a person to manually open Mission Control Portal whenever an automated system encounters an issue, the customer’s agent can query the Telnyx AI Assistant directly.

For example, an agent could:

- Ask how to configure a Telnyx product or API.
- Request relevant documentation for an implementation.
- Investigate why an account resource is not behaving as expected.
- Gather troubleshooting guidance before escalating an issue to a human operator or Telnyx Support.

This helps AI agents operate more independently while still giving customers a clear path to human support when an issue requires further investigation.

## Important considerations

The A2A interface is intended to complement, not replace, the Telnyx Support team. Responses may occasionally be incomplete, incorrect, or based on outdated information. Customers should validate important guidance before making production changes.

For complex issues, requests requiring account changes, or questions the Assistant cannot resolve, customers should contact Telnyx Support through Mission Control Portal or create a support ticket via support@telnyx.com, however the Assistant can also create one on your behalf if you request it.

Requests made through A2A may be processed using the same artificial intelligence systems and subprocessors described in this article. Customers should avoid including unnecessary personal, confidential, or sensitive information in their requests.

---

## By using our AI Assistant

- You agree to the processing of [personal data](https://telnyx.com/privacy-policy), which is necessary for the provision of our chat services.
- You acknowledge and consent to have your data stored and processed by Telnyx in the United States.
- You agree to have your data transferred to OpenAI, a subprocessor located in the United States, who assists in processing interactions with our AI Assistant and generating answers based on our publicly accessible documentation.
- We retain personal data as long as necessary to provide our services or as required by law, rule or regulation.
- Please note that our services involve automated decision-making, including the use of artificial intelligence to process interactions with our AI Assistant.
- It is possible that our assistant may return incorrect our outdated information, please do not hesitate to contact a member of our support team to have your queries clarified.
