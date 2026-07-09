---
source_url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
scraped: 2026-07-08
content_hash: a07287ba837141b8f0e37069b53fc5da33d276899f26ac72f6d67cddfd73acb6
---

TeXML and Telnyx Voice API compatibility | Telnyx Help Center

[Skip to main content](#main-content)

# TeXML and Telnyx Voice API compatibility

Avoid combining TeXML and Call Control commands in the same application

K

Written by Klane Pedrie

April 30, 2026

Table of contents

# TeXML and Telnyx Voice API/Call Control compatibility

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

---

Related Articles

[Telnyx Debugging Tools](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[Configuring Call Control/TeXML Applications - Voice API](https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api)[TeXML Bin Simple Voicemail and Call Forwarding](https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding)[Twilio TwiML Conference on Telnyx](https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx)

Did this answer your question?

😞😐😃

Table of contents
