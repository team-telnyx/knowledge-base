---
title: Telnyx Voice Features and Configuration
summary: This page consolidates Telnyx support documentation covering call forwarding,
  conference calls, TeXML Bin voicemail and call forwarding, sending and receiving
  SMS with the Python SDK, debugging tools, configuring Call Control/TeXML applications,
  voicemail setup, TeXML and Voice API compatibility, Android and iOS push notification
  setup, webhook CA errors, and Voice API essentials.
sources:
- url: https://support.telnyx.com/en/articles/1130657-call-forwarding
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
- url: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
- url: https://support.telnyx.com/en/collections/5782829-webrtc-voice-sdk
updated_at: 2026-07-17T09:05:29Z
---

# Telnyx Voice Features and Configuration

*Part 4 of 6 — see also: [Part 1](telnyx-voice-features-and-configuration--part-1.md), [Part 2](telnyx-voice-features-and-configuration--part-2.md), [Part 3](telnyx-voice-features-and-configuration--part-3.md), [Part 5](telnyx-voice-features-and-configuration--part-5.md), [Part 6](telnyx-voice-features-and-configuration--part-6.md)*

This page consolidates Telnyx support documentation covering call forwarding, conference calls, TeXML Bin voicemail and call forwarding, sending and receiving SMS with the Python SDK, debugging tools, configuring Call Control/TeXML applications, voicemail setup, TeXML and Voice API compatibility, Android and iOS push notification setup, webhook CA errors, and Voice API essentials.

## Setting Up Telnyx Voicemail

**⚠️ This feature should only be enabled on numbers that are assigned to SIP Connections. ⚠️**

In this early version of the feature, you can forward incoming calls to a voicemail box when a call is rejected or missed.

![](_images/bfaa2b0856a88105.png)

You can then consult deposited voicemail messages by dialing `*98` from a voicemail-enabled number and authenticating with an access PIN that you set. Make sure that the device you are calling from has the voicemail-enabled number set as the Caller ID before dialing `*98`.

### Setting Voicemail PIN

Setting a voicemail PIN is required in order to enable the voicemail service.

To enable voicemail features through the number settings on your portal account:

1. Go to 'My Numbers' in the 'Numbers' section.
2. Filter for the number you wish to configure voicemail.
3. Click the pencil icon, under the actions column, to be brought to the number settings.
4. Click the "voice" sub tab to access the voice-related settings of your number.
5. Scroll down until you find the Voice Mail section.
6. Click the toggle to enable voicemail.
7. Set your PIN.

### Calls Voicemail Completed Event

If you have set a webhook URL on your SIP Connection, Telnyx delivers a new webhook event so you can stay informed about any voicemails that have been left through `calls.voicemail.completed`.

Example:

```json
{  
  "data": {  
    "event_type": "calls.voicemail.completed",  
    "id": "93958804-6787-4623-bb59-a4e4ce1c44de",  
    "occurred_at": "2023-11-15T08:00:33.589698Z",  
    "payload": {  
      "call_session_id": "036c8492-838d-11ee-b3bb-02420a0d3a69",  
      "connection_id": "1635420769989166414",  
      "from": "+13121234567",  
      "recording_url": "url of recording to download file",  
      "to": "+13127654321"  
    },  
    "record_type": "event"  
  },  
  "meta": {  
    "attempt": 1,  
    "delivered_to": "https://webhook.site/0a6718c8-e59a-4921-8119-c395d631a99b"  
  }  
}
```

### Limitations

- You cannot currently customize the voicemail box greeting message.
- You cannot trigger an email to be sent upon a voicemail being deposited.

These are two features that Telnyx is considering introducing in the future.

### Voicemail API

To programmatically update a phone number's voicemail settings, see the developer documentation:

- [Get Voicemail](https://developers.telnyx.com/api/voicemail/get-voicemail)
- [Create Voicemail](https://developers.telnyx.com/api/voicemail/create-voicemail)
- [Update Voicemail](https://developers.telnyx.com/api/voicemail/update-voicemail)

## TeXML and Voice API Compatibility

Avoid combining TeXML and Telnyx Voice API/Call Control commands in the same application. TeXML converts XML instructions into Voice API commands but also does other things in the background to keep track of the state of the call and execute instructions at the right time and in the correct order. Mixing the two products may work for some simple cases but will eventually lead to errors or some unexpected and confusing behaviour that will be hard to debug.

This also applies to AI Assistants, which use TeXML under the hood. Issuing Call Control commands on calls managed by an AI Assistant will cause the same state conflicts.

**Common scenarios to avoid:**

- Using `call_control_id` from a TeXML webhook to issue Voice API commands (e.g., transfer, bridge, hangup).
- Calling `streaming_start` on a call that's already using the TeXML `<Stream>` verb.
- Mixing TeXML `<Dial>` with Voice API bridge commands on the same call.
- Issuing Call Control commands on AI Assistant calls.

If you need Call Control flexibility, use the Voice API from the start rather than TeXML. If you need both paradigms for different parts of your application, use separate connections — a TeXML Application for TeXML calls and a Voice API Application for Call Control calls.

**Note:** TeXML webhooks use form-encoded parameters, while Voice API webhooks use JSON. If your application handles both, make sure your server can parse both formats correctly.

Learn more:

- [TeXML Fundamentals](https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals)
- [Voice API Getting Started](https://developers.telnyx.com/docs/voice/programmable-voice)
- [AI Assistants](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant)
- [Media Streaming](https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming)
