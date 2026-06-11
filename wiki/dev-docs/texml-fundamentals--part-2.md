---
title: TeXML Fundamentals
summary: TeXML is Telnyx’s XML-based markup language for building programmable voice
  call flows with simple, sequential “verbs” and “nouns.” This page explains what
  TeXML is, how TeXML Applications fetch and run your instructions, quick ways to
  host XML with TeXML Bin, using dynamic templates and HTTP requests, and how TeXML
  aligns with Twilio’s TwiML for fast migration.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
updated_at: 2026-05-20T09:36:55Z
---

# TeXML Fundamentals

*Part 2 of 2 — see also: [Part 1](texml-fundamentals--part-1.md)*

TeXML is Telnyx’s XML-based markup language for building programmable voice call flows with simple, sequential “verbs” and “nouns.” This page explains what TeXML is, how TeXML Applications fetch and run your instructions, quick ways to host XML with TeXML Bin, using dynamic templates and HTTP requests, and how TeXML aligns with Twilio’s TwiML for fast migration.

## Best practices
- Keep instruction fetch latency low; consider AnchorSite latency routing for optimal data center selection.
- Validate CallSid and expected parameters; implement webhook error handling and use a Failover URL.
- Return HTTP 200 with well‑formed XML (<Response> root) and keep responses small.
- Use Telnyx-provided parameters (for example, From, To) to personalize flows.
- For outbound: prefer TeXML Calls API when you want application‑level control; use parked outbound on SIP trunking for trunk‑level control.
- Use TeXML Secrets for credentials; never hardcode keys in XML.
- Test with varied parameter combinations and edge cases (timeouts, unavailable URLs, invalid inputs).

## See also
- [TeXML Quickstart: Simple Text-to-Speech Demo](texml-quickstart-simple-text-to-speech-demo.md)
- [TeXML Bin Simple Voicemail and Call Forwarding](texml-bin-simple-voicemail-and-call-forwarding.md)
- [TeXML Bin Dynamic Content](texml-bin-dynamic-content.md)
- [Sending HTTP requests in TeXML - tutorial](sending-http-requests-in-texml-tutorial.md)
- [TeXML Instruction Fetching](texml-instruction-fetching.md)
- [TeXML Interpreter](texml-interpreter.md)
- [TeXML and TwiML Compatibility](texml-and-twiml-compatibility.md)
