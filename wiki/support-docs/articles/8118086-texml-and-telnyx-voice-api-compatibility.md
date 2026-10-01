---
title: "TeXML and Telnyx Voice API compatibility"
summary: "Avoid combining TeXML and Call Control commands in the same… See Telnyx guidance and requirements Learn more about TeXML and Telnyx Voice API compatibility."
sources:
- url: "https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--8118086-texml-and-telnyx-voice-api-compatibility.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--8118086-texml-and-telnyx-voice-api-compatibility.md -->

# TeXML and Telnyx Voice API compatibility

Avoid combining TeXML and Call Control commands in the same… See Telnyx guidance and requirements Learn more about TeXML and Telnyx Voice API compatibility.

K




## TeXML and Telnyx Voice API/Call Control compatibility

Avoid combining TeXML and Telnyx Voice API/Call Control commands in the same application. TeXML converts XML instructions into Voice API commands but also does other things in the background to keep track of the state of the call and execute instructions at the right time and in the correct order. Mixing the two products may work for some simple cases but will eventually lead to errors or some unexpected and confusing behaviour that will be hard to debug.

This also applies to AI Assistants, which use TeXML under the hood. Issuing Call Control commands on calls managed by an AI Assistant will cause the same state conflicts.
​

**Common scenarios to avoid:**

* Using `call_control_id` from a TeXML webhook to issue Voice API commands (e.g. transfer, bridge, hangup)
* Calling `streaming_start` on a call that's already using the TeXML `<Stream>` verb
* Mixing TeXML `<Dial>` with Voice API bridge commands on the same call
* Issuing Call Control commands on AI Assistant calls

**If you need Call Control flexibility**, use the Voice API from the start rather than TeXML. If you need both paradigms for different parts of your application, use separate connections — a TeXML Application for TeXML calls and a Voice API Application for Call Control calls.

**Note:** TeXML webhooks use form-encoded parameters, while Voice API webhooks use JSON. If your application handles both, make sure your server can parse both formats correctly.

Learn more:

* [TeXML Fundamentals](https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals)
* [Voice API Getting Started](https://developers.telnyx.com/docs/voice/programmable-voice)
* [AI Assistants](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant)
* [Media Streaming](https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming)

Please join us at <https://joinslack.telnyx.com/> to discuss or give feedback around your TeXML or Voice API use case if you run into any api/application issues.
