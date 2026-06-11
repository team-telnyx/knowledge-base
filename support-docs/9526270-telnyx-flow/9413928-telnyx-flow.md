---
source_url: https://support.telnyx.com/en/articles/9413928-telnyx-flow
scraped: 2026-06-11
---

Telnyx Flow | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Flow

Deprecation notice.

Written by Dillin

May 1, 2026

Table of contents

## Deprecation notice: Telnyx Flow sunset (July 3, 2026)

Telnyx Flow will sunset on **July 3, 2026**. After this date, Flow will no longer process traffic or execute workflows.

### What’s happening

As we focus our investment on **AI-first APIs**, including **AI Assistant** and **Voice AI** capabilities, we’ve made the decision to retire Telnyx Flow. With the rapid advancement of coding models, many customers are now building automation programmatically rather than maintaining visual workflows.

### What this means for you

On **July 3, 2026**:

* **Workflows in Flow will stop executing.**
* **Inbound webhook events will no longer be delivered to Flow.**
* **Any [Voice](https://portal.telnyx.com/#/call-control/applications) or [Messaging](https://portal.telnyx.com/#/programmable-messaging/profiles) applications pointing to Flow will stop receiving inbound traffic.**

### What you need to do

Before **July 3, 2026**, update any **Voice** and **Messaging** application webhooks currently pointing to Flow so they route to a new endpoint you control—either:

* Your own hosted service, or
* An alternative orchestration platform

### Your options

* **Build directly with Telnyx APIs**  
  Everything you do in Flow today can be replicated using our **[Voice](https://developers.telnyx.com/api-reference/overview)**[, **Messaging**, and **Chat Completions** APIs.](https://developers.telnyx.com/api-reference/overview) **AI Assistants ([No-Code Assistant](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant))** if you want a faster route to a deployable assistant without managing orchestration yourself. This provides maximum control and flexibility.
* **Use n8n with the Telnyx AI node**  
  If you prefer a visual workflow tool, **n8n** is a viable alternative for many use cases, and our **Telnyx AI node** is available there.

---

Related Articles

[What is Telnyx?](https://support.telnyx.com/en/articles/1130637-what-is-telnyx)[BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)[Forwarding SMS/MMS Automation using Telnyx Flow](https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow)[Telnyx + Vapi Integration](https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration)[Bot-to-Bot Support API: Ask Telnyx Knowledge Agent](https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent)

Did this answer your question?

😞😐😃

Table of contents
