---
source_url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
scraped: 2026-06-11
---

TeXML Bin Simple Voicemail and Call Forwarding | Telnyx Help Center

[Skip to main content](#main-content)

# TeXML Bin Simple Voicemail and Call Forwarding

Get started quickly with Telnyx Programmable Voice and the TexML Bin feature. Explore our comprehensive documentation, tutorials, and quickstart guide to effortlessly integrate TexML Bin into your voice applications.

Written by Telnyx Engineering

January 14, 2026

Table of contents

TeXML Bin allows users to upload TeXML files to storage and use it for call flows without having to code. Developers can quickly and easily add programmable voice features into applications without having to worry about setting up application servers.

TeXML is an XML-based data structure you can use to control calls with Telnyx and is the quickest way to get started with Programmable Voice using a simple .xml file, allowing you to specify call instructions in your file using commands called verbs and nouns. TeXML Translator starts at the top of your TeXML file and executes your TeXML commands sequentially in the order they are arranged in the file.

In this guide, you’ll learn how to start using TeXML Bin and configure a simple voicemail and call forwarding TeXML application using Telnyx’s Voice API.

This tutorial assumes you’ve already [set up your developer account and environment](https://developers.telnyx.com/development).

Let’s get started:

## **Step 1: Create your XML**

To create XML documents, you can use the new [TeXML editor](https://portal.telnyx.com/#/app/call-control/texml-bin) in the Mission Control Portal. You’ll find the TeXML editor by navigating to the Programmable Voice section on the left menu and selecting ‘TeXML Bin’.

[![Simple Voicemail](https://downloads.intercomcdn.com/i/o/ltcafuzd/1940046258/37629dc384cfdc20652dc4265b88/texml_bin_create_voice_texml.png?expires=1781167500&signature=94d7f89848d6fcc069acbd93e21314b99828f347dc85c8a32d44f0d64f3f2125&req=dSkjFsl6m4NaUfMW1HO4zc6bgSRxnzFoUVoLWUxG9IEBV33ZzzRLpAY7TYtk%0ADbdmzXDWgeIpaDakRQQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1940046258/37629dc384cfdc20652dc4265b88/texml_bin_create_voice_texml.png?expires=1781167500&signature=94d7f89848d6fcc069acbd93e21314b99828f347dc85c8a32d44f0d64f3f2125&req=dSkjFsl6m4NaUfMW1HO4zc6bgSRxnzFoUVoLWUxG9IEBV33ZzzRLpAY7TYtk%0ADbdmzXDWgeIpaDakRQQ%3D%0A)

*Set a simple voicemail with TeXML Bin*

### **Simple voicemail**

```
<?xml version="1.0" encoding="UTF-8"?>   
<Response>  
   <Say>Thank you for calling YYZ co. Please leave a message.</Say>  
   <Record playBeep="true" finishOnKey="*9" />   
</Response>
```

### **Simple call forward**

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

## **Step 2: Set up your XML application in Mission Control**

You can set up your XML application to use the created script by selecting it from the drop-down list.

[![Editing your TeXML Application](https://downloads.intercomcdn.com/i/o/ltcafuzd/1940052112/c9a8ea6b1de001777553ffdca75f/texml_bin_edit_app.png?expires=1781167500&signature=039d8fda808fe5321c5246b0430f887f0174e25f47101ec10c805e56222a5276&req=dSkjFsl7n4BeW%2FMW1HO4zVupksAc3FmML1rHJXYrit8pnavw3prXgp5t97IQ%0A8gP14mM4BHnA5DRbaCo%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1940052112/c9a8ea6b1de001777553ffdca75f/texml_bin_edit_app.png?expires=1781167500&signature=039d8fda808fe5321c5246b0430f887f0174e25f47101ec10c805e56222a5276&req=dSkjFsl7n4BeW%2FMW1HO4zVupksAc3FmML1rHJXYrit8pnavw3prXgp5t97IQ%0A8gP14mM4BHnA5DRbaCo%3D%0A)

*Editing your TeXML application*

## **Step 3: Test your application**

Test your application by:

1. Assigning a phone number to the application

[![Assigning a number to an application](https://downloads.intercomcdn.com/i/o/ltcafuzd/1940101777/66629efcd75ef1bf8d85bf9c9f5a/texml_bin_assign_number.png?expires=1781167500&signature=7eab4f2cc7f1a7f936a04b76896f0b430a2a1c952d8cd6841d3df858591320b8&req=dSkjFsh%2BnIZYXvMW1HO4zZdbwUFwtE30fSZVdMeCm9YvqpNirmQ0F%2Fy%2FyvOY%0AcOqTB8g6bl2LaKwzS6w%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1940101777/66629efcd75ef1bf8d85bf9c9f5a/texml_bin_assign_number.png?expires=1781167500&signature=7eab4f2cc7f1a7f936a04b76896f0b430a2a1c952d8cd6841d3df858591320b8&req=dSkjFsh%2BnIZYXvMW1HO4zZdbwUFwtE30fSZVdMeCm9YvqpNirmQ0F%2Fy%2FyvOY%0AcOqTB8g6bl2LaKwzS6w%3D%0A)

*Assigning a number to an application*

2. Dialing the number from the PSTN and leave a message

3. Retrieving your voicemail

[![Retrieving your Voicemail](https://downloads.intercomcdn.com/i/o/ltcafuzd/1940105334/85a8eb7a8155af5fae77b5e8cead/texml_bin_call_recordings.png?expires=1781167500&signature=5caa6b72009786244d6ddba941a594d850f80be3b83611a4de608bda49179e8c&req=dSkjFsh%2BmIJcXfMW1HO4zXjyoY2SwgkxuvEWI%2B1k0tKWKs%2B7J0vo5K7t7LEI%0Aj32%2BKxaelYRMf9sLdF8%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1940105334/85a8eb7a8155af5fae77b5e8cead/texml_bin_call_recordings.png?expires=1781167500&signature=5caa6b72009786244d6ddba941a594d850f80be3b83611a4de608bda49179e8c&req=dSkjFsh%2BmIJcXfMW1HO4zXjyoY2SwgkxuvEWI%2B1k0tKWKs%2B7J0vo5K7t7LEI%0Aj32%2BKxaelYRMf9sLdF8%3D%0A)

*Retrieving your voicemail*

And that’s it! If you have any questions about this tutorial or any of our products, reach out to our support team through the chat in the bottom right-hand corner.

---

Related Articles

[Call Forwarding](https://support.telnyx.com/en/articles/1130657-call-forwarding)[Does Telnyx support conference calls?](https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls)[TeXML and Telnyx Voice API compatibility](https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility)[Real-Time Transcription](https://support.telnyx.com/en/articles/8292490-real-time-transcription)[Twilio TwiML Conference on Telnyx](https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx)

Did this answer your question?

😞😐😃

Table of contents
