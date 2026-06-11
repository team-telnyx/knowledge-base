---
source_url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
scraped: 2026-06-11
---

Inbound Call Screening | Telnyx Help Center

[Skip to main content](#main-content)

# Inbound Call Screening

Protect your business from unwanted spam calls with Inbound Call Screening.

Written by Telnyx Engineering

March 17, 2026

Table of contents

At Telnyx, we are committed to providing you with robust features to enhance your communication experience. We're excited to introduce Inbound Call Screening, a powerful feature designed to protect Telnyx numbers from unwanted and spam calls.

Inbound Call Screening, enables users to flag and block unwanted incoming calls based on customizable conditions to maintain the integrity of their communications.

## Inbound Call Screening features include:

1. **Enhanced Call Control:** Users can now reject or flag suspicious calls based on customizable conditions—empowering businesses to manage incoming calls with confidence.
2. **Spam Call Detection:** Effectively screen and identify potential spam calls to protect Telnyx numbers from unwanted solicitations and fraudulent activities, and avoid spam calls.

# How do I configure Inbound Call screening?

1. ### Login to your Telnyx [Mission Control Portal](https://portal.telnyx.com) account.

   1. Navigate to the "[My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers)" section on the left-hand sidebar in the portal.

      ​

      [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2173683959/859aadb77377686a0a27ac9d5712/Screenshot%2B2026-03-17%2Bat%2B23_02_18.png?expires=1781168400&signature=10ab26e6e5c24c1c062d214e5cf9d5f1b90a555c71d26e6cc26576c0ab74c947&req=diEgFc92nohaUPMW1HO4zTFzs5ytdr1VO4K8PK751q2tBy4apDbn%2FxUm3K79%0AmQ7L%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2173683959/859aadb77377686a0a27ac9d5712/Screenshot%2B2026-03-17%2Bat%2B23_02_18.png?expires=1781168400&signature=10ab26e6e5c24c1c062d214e5cf9d5f1b90a555c71d26e6cc26576c0ab74c947&req=diEgFc92nohaUPMW1HO4zTFzs5ytdr1VO4K8PK751q2tBy4apDbn%2FxUm3K79%0AmQ7L%0A)
   2. Choose the Telnyx number you wish to update from your list, then select 'Edit' to manage its Inbound Call Screening configuration.  
      ​

      [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2173710115/610e53c23bafed8c47318352d97e/Screenshot%2B2026-03-17%2Bat%2B23_03_02.png?expires=1781168400&signature=39060bb45bae9ce5d2386ff7d1a7de15b551464fea575376fde3526832d07d95&req=diEgFc5%2FnYBeXPMW1HO4zUDEm3rvZOaZmUzSejrhhwtOCyCiAoQKY6bE4PZH%0AxzMb%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2173710115/610e53c23bafed8c47318352d97e/Screenshot%2B2026-03-17%2Bat%2B23_03_02.png?expires=1781168400&signature=39060bb45bae9ce5d2386ff7d1a7de15b551464fea575376fde3526832d07d95&req=diEgFc5%2FnYBeXPMW1HO4zUDEm3rvZOaZmUzSejrhhwtOCyCiAoQKY6bE4PZH%0AxzMb%0A)
   3. Under Number Settings, click the **Voice** tab to enable or adjust your Inbound Call Screening preferences.
2. ### Enable call screening for the selected number

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2173778632/575dbc5017c6ebc8b30165e80166/Screenshot%2B2026-03-17%2Bat%2B23_03_15.png?expires=1781168400&signature=d8ec7c59cb1d7cffbe74ce8aec81343c1bad6b20f68e3641ad659f1561112448&req=diEgFc55lYdcW%2FMW1HO4zSJn63mohwpf7WF1NUmXiRt75a3HtCTGszFIU%2B2%2F%0Agdmz%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2173778632/575dbc5017c6ebc8b30165e80166/Screenshot%2B2026-03-17%2Bat%2B23_03_15.png?expires=1781168400&signature=d8ec7c59cb1d7cffbe74ce8aec81343c1bad6b20f68e3641ad659f1561112448&req=diEgFc55lYdcW%2FMW1HO4zSJn63mohwpf7WF1NUmXiRt75a3HtCTGszFIU%2B2%2F%0Agdmz%0A)

   By default, the screening options are **greyed out** and inactive. To modify these settings, you must first check the box labeled **"Enable Inbound Call Screening."** Once this box is checked, the following two configuration options will become available:  
   ​

   1. **Flag Calls**

      When this option is selected, suspicious calls are allowed to reach your infrastructure but are clearly labeled for identification. This is the recommended setting for users who wish to perform custom routing (e.g., sending spam to a specific IVR or voicemail).  
      ​
   2. **Reject Calls**

      When this option is selected, any call identified as suspicious is automatically blocked at the network level.  
       These calls will not reach your servers, reducing unwanted traffic and saving on processing resources.

      ​
3. ### Save your call screening settings.

Keep reading to learn more about how inbound call screening works.

# How much does Inbound Call Screening cost?

Inbound Call Screening is **free**.

As of March 17, 2026, there are no charges to enable or use Inbound Call Screening on any number in your Telnyx account.

# Inbound Call Screening FAQs

## How does Inbound Call Screening work?

There are 3 factors that we use to implement inbound call screening, Number Reputation Database, Number Validation and SHAKEN/STIR Attestation.

**Number Reputation Database**

Inbound Call Screening leverages a comprehensive number reputation database to assess the reputation score associated with incoming calls' Calling Line Identity (CLI).

Telnyx aggregates data from multiple reputation providers such as **Nomorobo**, **YouMail**, and **CallerAPI** to define the reputation of a number and uses that information to classify callers as potential spammers.

With three reputation providers now cross-referencing incoming call data, Telnyx can identify more spam and fraudulent numbers with greater confidence.  
​  
​

**Number Validation**

Telnyx analyzes the validity and existence of originating numbers to ensure compliance with telecommunication standards and mitigate risks. Invalid or non-existent numbers can be flagged or rejected, helping to classify and address potential fraud or misconfigured caller identities.

**SHAKEN/STIR attestation**

Inbound Call Screening employs the SHAKEN/STIR attestation protocol to validate the authenticity of Caller ID information to help ensure the legitimacy of incoming calls.

Inbound Call Screening will be applied to the following attestation levels:

* **Attestation C** - This is when the originating carrier cannot authenticate the Caller ID or the Caller ID has been identified as invalid.   
  Calls with C attestation are potentially suspicious and are subjected to Inbound Call Screening.
* **Attestation Invalid** - This is when the SHAKEN/STIR attestation for a call is deemed invalid—possibly due to certificate problems or technical errors—and indicates a potential risk of spam or fraud.

### How can I treat unwanted inbound calls?

Telnyx users can handle unwanted calls in 2 ways.

### Reject calls

By selecting the **Reject** option, suspicious calls as defined by the above criteria will be rejected.   
This ensures that calls identified as potentially unwanted or spam are not connected to your Telnyx number.

### Flag calls

By selecting the Flag option, you can flag suspicious calls that match the defined conditions. Flagged calls receive clear indications to help you identify them easily.

The name part of the From and P-Asserted-ID headers will display the text "*SPAM LIKELY,*" providing a visual indicator of the flagged call. In addition, a custom SIP header, "*X-Telnyx-Call-Screening: SPAM LIKELY,*" will be added to the SIP INVITE message, to highlight the call status.

If you have webhooks enabled, *the call.initiated* webhook will include the variable "call\_screening\_result" with the value "spam\_likely", providing detailed information about the call screening outcome.

## What are the benefits of using Inbound Call Screening?

Inbound Call Screening allows you to avoid spam calls by effectively screening and identifying potential spam callers, and gives you enhanced call control, allowing you to reject or flag suspicious calls based on customizable conditions.

## Where is Inbound Call Screening available?

Inbound Call Screening currently applies to calls originating from the United States or Canada for number reputation screening. SHAKEN/STIR attestation screening applies to calls from North America.

## Are there any additional requirements to make the most of Inbound Call Screening?

To maximize the benefits of Inbound Call Screening, ensure webhooks are enabled.

You can specify webhook urls on your SIP Connection settings or through your programmable voice applications.

Webhooks provide real-time notifications and detailed insights into the call screening process and outcomes. Enabling webhooks will include the "**call\_screening\_result**" variable in the ***call.initiated*** webhook, providing detailed information about the call screening outcome.

```
{  
   "event_type":"call.initiated",  
   "id":"901d2366-adcd-45f0-9fcf-c17ed5d1ecd7",  
   "occurred_at":"2023-06-29T13:01:50.423002Z",  
   "payload":{  
      "call_control_id":"v3:NA0M2_T5NkETExuhDFz0XyRJ2d4IEb1kdmfRRqFv2ils6id9RIxUkg",  
      "call_leg_id":"1cc5d164-167d-11ee-a812-02420a1f0d69",  
      "call_screening_result":{  
         "action":"flag_calls",  
         "reputation":null,  
         "shaken_stir_attestation":"A"  
      },  
      "call_session_id":"1cc5db28-167d-11ee-a1dc-02420a1f0d69",  
      "caller_id_name":"test",  
      "client_state":null,  
      "connection_id":"1542950386652912121",  
      "custom_headers":[  
         {  
            "name":"X-rtc_leg_uuid",  
            "value":"d72f7cf9-9b2d-411f-917c-0f85f251a488"  
         }  
      ],  
      "direction":"incoming",  
      "from":"+from-number",  
      "start_time":"2023-06-29T13:01:50.423002Z",  
      "state":"parked",  
      "to":"+to-number"  
   },  
   "record_type":"event"  
}
```

---

Related Articles

[Configuring Call Control/TeXML Applications - Voice API](https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api)[SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)[Canadian STIR/SHAKEN Implementation FAQs](https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs)[Making Calls with Branded Calling](https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling)[Understanding SIP 603+ carrier rejections](https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections)

Did this answer your question?

😞😐😃

Table of contents
