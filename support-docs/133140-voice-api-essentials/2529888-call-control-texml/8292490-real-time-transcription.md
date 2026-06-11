---
source_url: https://support.telnyx.com/en/articles/8292490-real-time-transcription
scraped: 2026-06-11
---

Real-Time Transcription | Telnyx Help Center

[Skip to main content](#main-content)

# Real-Time Transcription

Enable real-time transcription for calls with Telnyx. Enhance user experience now.

Written by David

Updated over 3 weeks ago

Table of contents

# Real Time Transcription with Voice API and TeXML

Real-time transcription for a phone call refers to the process of converting spoken language into written text as the conversation is happening. Unlike traditional transcription services, which typically involve manually transcribing a recording after the call has ended, real-time transcription is automated and occurs instantaneously during the call. This allows participants to see a live, written version of the conversation as it unfolds.

## Key Features of Real-Time Transcription or Speech to Text:

1. **Instantaneous**: Text appears nearly simultaneously with the spoken words, offering immediate insights into the conversation.
2. **Automated**: Usually powered by advanced speech-to-text algorithms, the process doesn't require human intervention for transcription.
3. **Multi-Functional**: Real-time transcription can be useful for various applications such as accessibility for the hearing-impaired, legal compliance, documentation, or data analysis.
4. **Accuracy**: While generally very accurate, the quality of the transcription can vary based on the clarity of speech, background noise, and the sophistication of the transcription technology used.

   ### The Voice API parameters that you can select for Transcription are:

   call\_control\_id: Unique Id for controlling the call.

   client\_state: adds state of call to webhook.

   command\_id: Optional id you can set arbitrarily.

   interim\_results: Only available with Google, Engine A and returns transcription results more quickly but less accurately.

   language: Set language for transcription.

   transcription\_engine: Options are A or B. A is Google Transcription Engine and is the default, it is also the only engine which can use the feature `interim_results`. B is the Telnyx Transcription Engine which is more accurate and less costly.  
   transcription\_tracks: Indicates which leg of the call to transcribe - `inbound`, `outbound` or `both`.

   [![Path parameters section.](https://downloads.intercomcdn.com/i/o/818402609/67c6bc5e0a62a0356071e878/Screenshot+2023-08-29+at+3.12.10+PM.png?expires=1781168400&signature=89fd23978d5ec96225fbd9390c1b1c0ba788deca2eee28db7a534a7d4d67d5a9&req=fCEvEsl8m4FWFb4f3HP0gBENKF%2BRF4ZHeqsNvapJPzYbnWlv16OXX2n4cxA4%0AZ3I%3D%0A)](https://downloads.intercomcdn.com/i/o/818402609/67c6bc5e0a62a0356071e878/Screenshot+2023-08-29+at+3.12.10+PM.png?expires=1781168400&signature=89fd23978d5ec96225fbd9390c1b1c0ba788deca2eee28db7a534a7d4d67d5a9&req=fCEvEsl8m4FWFb4f3HP0gBENKF%2BRF4ZHeqsNvapJPzYbnWlv16OXX2n4cxA4%0AZ3I%3D%0A)

   ### The TeXML Attributes that you can select for Transcription are:

   [![TeXML Attributes section.](https://downloads.intercomcdn.com/i/o/818399688/0067df3d2664103f6d338cf7/Screenshot+2023-08-29+at+3.06.27+PM.png?expires=1781168400&signature=183dee6bd01b272cba1bd284926ef33b56892aa75fe102f5bbeb7089c7dd598e&req=fCEvFcB3m4lXFb4f3HP0gNt7EV81gIHipY9K1oq4Cn8Gji6s%2FVyOUcLwIgL6%0AgBo%3D%0A)](https://downloads.intercomcdn.com/i/o/818399688/0067df3d2664103f6d338cf7/Screenshot+2023-08-29+at+3.06.27+PM.png?expires=1781168400&signature=183dee6bd01b272cba1bd284926ef33b56892aa75fe102f5bbeb7089c7dd598e&req=fCEvFcB3m4lXFb4f3HP0gNt7EV81gIHipY9K1oq4Cn8Gji6s%2FVyOUcLwIgL6%0AgBo%3D%0A)

## Telnyx Real Time Transcription Product Options:

STT is available with the Telnyx Voice API or TeXML at this time. If you are a SIP Trunking user then you would have to convert to the one of the two programmatic voice options to use our Speech to Text capabilities.

## STT or Speech to Text Applications:

* **AI:** By using speech to text you can pass your call to an AI or LLM system to either evaluate, summarize, or participate in your calls. Read our [AI STT Blog](https://telnyx.com/resources/conversational-ai-speech-to-text) on this topic.

  [![Image of workflow of Speech to Text use between Callers and AI Bots](https://downloads.intercomcdn.com/i/o/818260752/f361450b25f91a07bf6536ae/Telnyx_Blog_Conversational-AI_Inline1_With-Direct-Pairing.jpg?expires=1781168400&signature=7cddd039822839bb3f7da9b6da7269979d6f37380450b971bea058475b01121e&req=fCEvFM9%2BmoRdFb4f3HP0gDDAZ5GCQM1edV63v8xEuet667OW1iDqs3fAeJyC%0Azzg%3D%0A)](https://downloads.intercomcdn.com/i/o/818260752/f361450b25f91a07bf6536ae/Telnyx_Blog_Conversational-AI_Inline1_With-Direct-Pairing.jpg?expires=1781168400&signature=7cddd039822839bb3f7da9b6da7269979d6f37380450b971bea058475b01121e&req=fCEvFM9%2BmoRdFb4f3HP0gDDAZ5GCQM1edV63v8xEuet667OW1iDqs3fAeJyC%0Azzg%3D%0A)

  [![A roadmap of AI answering service.](https://downloads.intercomcdn.com/i/o/825433970/4ff211817070ae94c20f63f6/Speech_To_Text_Support_Article_Customer_Service%402x.png?expires=1781168400&signature=fc14669ede38f7f28dd6241100e5e6ba96dac6313720cdef2117f7df43c55f5f&req=fCIiEsp9lIZfFb4f3HP0gO6MdnKHinVo7d0St0%2F8tWovTSKjawC8fn16%2FWEb%0ApVY%3D%0A)](https://downloads.intercomcdn.com/i/o/825433970/4ff211817070ae94c20f63f6/Speech_To_Text_Support_Article_Customer_Service%402x.png?expires=1781168400&signature=fc14669ede38f7f28dd6241100e5e6ba96dac6313720cdef2117f7df43c55f5f&req=fCIiEsp9lIZfFb4f3HP0gO6MdnKHinVo7d0St0%2F8tWovTSKjawC8fn16%2FWEb%0ApVY%3D%0A)
* **Voicemail**: it can save a lot of time to be able to read and share written transcripts of voicemails left by customers, employees, partners, and vendors.

  [![A man with his laptop transcribing a voicenote.](https://downloads.intercomcdn.com/i/o/825434550/52e37a741eceb70b424d80a3/Speech_To_Text_Support_Article_Voicemail%402x.png?expires=1781168400&signature=7191dcc2fb4a8a92d9ff516e1f2297f11b200cd55e082347ef7fbedc7371a340&req=fCIiEsp6mIRfFb4f3HP0gGSBJ0IidMmV2HHuV4PXKBFWn8QghyhHjtAjmFZY%0AKW8%3D%0A)](https://downloads.intercomcdn.com/i/o/825434550/52e37a741eceb70b424d80a3/Speech_To_Text_Support_Article_Voicemail%402x.png?expires=1781168400&signature=7191dcc2fb4a8a92d9ff516e1f2297f11b200cd55e082347ef7fbedc7371a340&req=fCIiEsp6mIRfFb4f3HP0gGSBJ0IidMmV2HHuV4PXKBFWn8QghyhHjtAjmFZY%0AKW8%3D%0A)
* **Business Meetings**: Provides a written record that can be reviewed later, helps participants focus on the discussion instead of note-taking.
* **Legal Requirements**: May be used to provide a live transcript of important legal proceedings over the phone.
* **Accessibility**: Helps the hearing-impaired to fully participate in the conversation.
* **Customer Service**: Allows for real-time analytics and quality control.

## How to use Real Time Transcription using the Voice API:

[Transcription start](https://developers.telnyx.com/api-reference/call-commands/dial) for Voice API

[Transcription stop](https://developers.telnyx.com/api-reference/call-commands/dial) for Voice API

[Transcription Start from Dial Command](https://developers.telnyx.com/api-reference/call-commands/dial) for Voice API

## How to use Real Time Transcription using the TeXML:

[Start Transcription Verb](https://developers.telnyx.com/voice/texml/texml-translator) for TeXML

[Stop Verb with Transcription Noun](https://developers.telnyx.com/voice/texml/texml-translator#stop) for TeXML

## Costs of Real Time Transcription:

You have 2 options when it comes to the cost of Speech to Text. The Speech to Text engine that is built using Telnyx technology is **$0.025 (USD)** per minute, please check up to date pricing at <https://portal.telnyx.com/#/pricing/voice> under Voice > Speech to Text. The STT engine that utilizes Google Technology is **$0.050 (USD)** per minute at the time of printing but up to date prices can be located at <https://portal.telnyx.com/#/pricing/voice>under Voice > Speech to Text. The default STT engine is A) Google because it has more features such as interim results, and secondary is B) Telnyx with significantly better transcription accuracy and lower latency. You can select which STT you want to use by following this [guide](https://developers.telnyx.com/docs/development/programmable-voice/speech-to-text). A Voice API example would be to use the "transcription\_engine" parameter when using the Transcription command such as

```
"transcription_engine" =  "A/B "
```

## Automatic Transcription with Timeout of Call Recording:

1. If you've set a timeout for your call recording—meaning the recording stops after a certain period of silence—Telnyx uses transcription to detect that silence. This will automatically trigger Real-Time Transcription even if you didn't explicitly enable it.
2. If transcription is triggered due to the timeout setting, you will be billed for it. Make sure to account for this in your budget.
3. If you're trying to create a voicemail system using the call recording command then transcription is nice to have to track the length of the silence to be able to trigger the stop recording command at the end of the voicemail. Alternatively, if you can trust your callers to hang up at the end of the message then that will end the recording as well.

[![A robot hand writing a transcription of a phone call.](https://downloads.intercomcdn.com/i/o/818320892/0c41b19579fdbe0c3fe36655/DALL%C2%B7E+2023-08-29+13.09.28+-+futuristic+technology+showing+a+robot+on+a+cell+phone+writing+down+the+conversation+with+a+fountain+pen+.png?expires=1781168400&signature=9acf320f4592591cc0d244939f2dc2499144798651b48409e1d65245f8182728&req=fCEvFct%2BlYhdFb4f3HP0gKkS6KyuUpLO8iBfuPDG321HWjcT46%2FUE6yoC1%2Bf%0ATRKO7CKuDojec4DOEg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/818320892/0c41b19579fdbe0c3fe36655/DALL%C2%B7E+2023-08-29+13.09.28+-+futuristic+technology+showing+a+robot+on+a+cell+phone+writing+down+the+conversation+with+a+fountain+pen+.png?expires=1781168400&signature=9acf320f4592591cc0d244939f2dc2499144798651b48409e1d65245f8182728&req=fCEvFct%2BlYhdFb4f3HP0gKkS6KyuUpLO8iBfuPDG321HWjcT46%2FUE6yoC1%2Bf%0ATRKO7CKuDojec4DOEg%3D%3D%0A)

​

---

Related Articles

[What is Telnyx?](https://support.telnyx.com/en/articles/1130637-what-is-telnyx)[Does Telnyx support conference calls?](https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls)[ElevateAI Proof-of-Concept Setup Guide](https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide)[Key Configuration Notes for Noise Suppression](https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression)[Twilio TwiML Conference on Telnyx](https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx)

Did this answer your question?

😞😐😃

Table of contents
