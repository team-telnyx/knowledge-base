---
title: 'Programmable Voice: SIPREC, Recording Storage, Speech-to-Text, and TeXML'
summary: A consolidated reference for Telnyx Programmable Voice features covering
  SIPREC client and server configuration, call recording storage backends, real-time
  speech-to-text transcription, and the TeXML markup language including applications,
  instruction fetching, dynamic templating, HTTP requests, and answering machine detection.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
updated_at: 2026-08-05T14:04:31Z
---

# Programmable Voice: SIPREC, Recording Storage, Speech-to-Text, and TeXML

*Part 4 of 6 — see also: [Part 1](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-1.md), [Part 2](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-2.md), [Part 3](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-3.md), [Part 5](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-5.md), [Part 6](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-6.md)*

A consolidated reference for Telnyx Programmable Voice features covering SIPREC client and server configuration, call recording storage backends, real-time speech-to-text transcription, and the TeXML markup language including applications, instruction fetching, dynamic templating, HTTP requests, and answering machine detection.

## TeXML Bin Quickstart

TeXML Bin lets you upload TeXML files to storage and use them for call flows without having to code your own server. The TeXML interpreter starts at the top of your TeXML file and executes commands sequentially in the order they are arranged.

### Step 1: Create your XML

Use the [TeXML editor](https://portal.telnyx.com/#/app/call-control/texml-bin) in the Mission Control Portal. Navigate to **Programmable Voice → TeXML Bin**.

![Simple Voicemail](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/texml_bin_create_voice_texml.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=7589fe4174aa28147e6099b9acf5946c)
*Set simple voicemail with TeXML Bin*

Simple voicemail:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Thank you for calling YYZ co. Please leave a message.</Say>
  <Record playBeep="true" finishOnKey="*9" />
</Response>
```

Simple call forward:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Sip>ext1@sip.xyzco.com</Sip>
    <Sip>ext3@sip.xyzco.com</Sip>
    <Sip>ext4@sip.xyzco.com</Sip>
   </Dial>
</Response>
```

### Step 2: Set up your XML application in Mission Control

Select the created script from the drop-down list in your XML application.

![Editing your TeXML Application](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/texml_bin_edit_app.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=812fd5c79746e55a879ef54ba45fb393)
*Editing your TeXML application*

### Step 3: Test your application

1. Assign a phone number to the application.

![Assigning a number to an application](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/texml_bin_assign_number.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=51ad5757fd1bc21779196f64e3f2a4ec)
*Assigning a number to an application*

2. Dial the number from the PSTN and leave a message.
3. Retrieve your voicemail.

![Retrieving your Voicemail](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/texml_bin_call_recordings.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=25f14c620e0092f446c0e383abcc652e)
*Retrieving your voicemail*

## TeXML Bin Dynamic Content

Use [Mustache Templates](https://mustache.github.io/mustache.5.html) to create dynamic parameters in TeXML Bin. See [TeXML Bin Quickstart](texml-bin-quickstart.md) for setup.

### Dynamic parameters

Insert content into TeXML instructions through HTTP request parameters in the webhook URL used to fetch the TeXML instructions. For example, to dial a phone number that is set when the HTTP request is made, create TeXML instructions using Mustache templating with `{{PhoneNumber}}` as a variable:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
     <Number>{{PhoneNumber}}</Number>    
  </Dial>
</Response>
```

The phone number is replaced at runtime by setting the TeXML webhook URL to include `PhoneNumber` as a parameter:

```
curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
--data-urlencode "To=+13121230000" \
--data-urlencode "From=+13120001234" \
--data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumber=+18771234567" \
--data-urlencode "StatusCallback=https://www.example.com/statuscallback-listener" \
--header "Authorization: Bearer YOUR_API_KEY"
```

Request parameters set by Telnyx (for example, `CallSid`, `From`, `To`) are also available for the Mustache template. See [TeXML Instruction Fetching](texml-instruction-fetching.md) for the full list of parameters per callback.

### Iterating through lists

Set arrays as parameters in the TeXML webhook URL and let Mustache handle them. For example, to dial two numbers, add a `Numbers` list parameter to the callback URL:

```
curl -X POST https://api.telnyx.com/v2/texml/calls/{connection_id} \
--data-urlencode "To=+13121230000" \
--data-urlencode "From=+13120001234" \
--data-urlencode "Url=https://www.example.com/texml.xml?PhoneNumbers[]=+18771234567&PhoneNumbers[]=+18771234568" \
--data-urlencode "StatusCallback=https://www.example.com/statuscallback-listener" \
--header "Authorization: Bearer YOUR_API_KEY"
```

Handle the `PhoneNumbers` parameter in the TeXML instructions:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    {{#PhoneNumbers}}
       <Number>{{.}}</Number>    
    {{/PhoneNumbers}}
  </Dial>
</Response>
```

This is parsed as:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Number>+18771234567</Number>
    <Number>+18771234568</Number>
  </Dial>
</Response>
```

### Conditional content

Use `if/else` statements to render conditional content. For example, dial a specific number depending on the `From` parameter:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
{{#if {{From}} == +18771234567}}
  <Dial>
    <Number>+18771234568</Number>
  </Dial>
{{#elseif {{From}} == +18771234568}}
  <Dial>
    <Number>+18771234567</Number>
  </Dial>
{{#else}}
  <Say>No valid number is present</Say>
{{/if}}
</Response>
```

Supported operators are `==` and `!=`. There is no operator for checking if a parameter value is not null.
