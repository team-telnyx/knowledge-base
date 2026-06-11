---
source_url: https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log
scraped: 2026-06-11
---

Understand Telnyx SMS MDR Report Log | Telnyx Help Center

[Skip to main content](#main-content)

# Understand Telnyx SMS MDR Report Log

You can check your MDR (message detail record) for every message sent or received.

Written by Telnyx Sales

January 2, 2025

Table of contents

# What is an MDR?

For every sent or received message, an MDR (message detail record) will be written. You can access and generate these report logs under **Reports** (left hand side navigation bar) -> **Reporting** in your Mission Control Portal Account as seen below.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1318222616/1a32d07e67a710378cab921e3217/image.png?expires=1781167500&signature=cbf2c3ac6904d0468b957172f6f0f18b86381561ae8adc6e4840725674c7a54d&req=dSMmHst8n4deX%2FMW1HO4zcRXzxiLCzxxOx%2F8vHltDAv2gODMqxCxNResW%2B%2Bl%0AJaY4pmAjjMYrkPFqlSA%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1318222616/1a32d07e67a710378cab921e3217/image.png?expires=1781167500&signature=cbf2c3ac6904d0468b957172f6f0f18b86381561ae8adc6e4840725674c7a54d&req=dSMmHst8n4deX%2FMW1HO4zcRXzxiLCzxxOx%2F8vHltDAv2gODMqxCxNResW%2B%2Bl%0AJaY4pmAjjMYrkPFqlSA%3D%0A)

## What are the different fields of information available?

MDRs are stored as JSON objects. These are the most important fields contained in each MDR:

[![The most important fields in Message Detail Records containing field name, type, and description. ](https://downloads.intercomcdn.com/i/o/34825438/a6dbe17a4c67e0b126293038/image.png?expires=1781167500&signature=749bfd62fe3e6cd2386e14ce2ab0a2e7dbf9b82ac95f1cc1165c27d360b0f8c8&req=dyQvFMx6nokTWLcX3D%2B5hpSNEhXE4anJB2inCJ5atGQSLLYnRA0QQ8vhOvXs%0Ahmcb9hYpRG5R0oJN%0A)](https://downloads.intercomcdn.com/i/o/34825438/a6dbe17a4c67e0b126293038/image.png?expires=1781167500&signature=749bfd62fe3e6cd2386e14ce2ab0a2e7dbf9b82ac95f1cc1165c27d360b0f8c8&req=dyQvFMx6nokTWLcX3D%2B5hpSNEhXE4anJB2inCJ5atGQSLLYnRA0QQ8vhOvXs%0Ahmcb9hYpRG5R0oJN%0A)

The embedded **body** object contains the following fields:

[![Picture of various fields contained in an embedded body object. ](https://downloads.intercomcdn.com/i/o/34825527/adb39d7137946046fa8b6b84/image.png?expires=1781167500&signature=aa40c8ed563c3b8ffe18824f377e1ea47f0dbe7520c378783052f05c88bdd54b&req=dyQvFMx7n4YTWLcX3D%2B5hhMMtEi6%2FTbSZtzhhrR4JRR5NDKpKA9wXmBdzF4G%0A3G6e06PlVjf5PybI%0A)](https://downloads.intercomcdn.com/i/o/34825527/adb39d7137946046fa8b6b84/image.png?expires=1781167500&signature=aa40c8ed563c3b8ffe18824f377e1ea47f0dbe7520c378783052f05c88bdd54b&req=dyQvFMx7n4YTWLcX3D%2B5hhMMtEi6%2FTbSZtzhhrR4JRR5NDKpKA9wXmBdzF4G%0A3G6e06PlVjf5PybI%0A)

For privacy reasons, a message’s body text is only stored for up to 10 days before it is wiped from our system. At that point, the hash fields can be used to identify messages.

## Status

For **sent messages**, the possible status values are:

[![Pictorial representation of possible status values for sent messages. ](https://downloads.intercomcdn.com/i/o/34825565/934e2b82440d24194727a8a9/image.png?expires=1781167500&signature=8de49eb8603e43f1b351982fe27851ccb0d929e2143dc9c89574dd1e32657188&req=dyQvFMx7m4QTWLcX3D%2B5hk%2BxlkQJZTqmmhkg9A8tWHCnoJanJSOa2KKtWr11%0APz3DzNn8TTcgycLh%0A)](https://downloads.intercomcdn.com/i/o/34825565/934e2b82440d24194727a8a9/image.png?expires=1781167500&signature=8de49eb8603e43f1b351982fe27851ccb0d929e2143dc9c89574dd1e32657188&req=dyQvFMx7m4QTWLcX3D%2B5hk%2BxlkQJZTqmmhkg9A8tWHCnoJanJSOa2KKtWr11%0APz3DzNn8TTcgycLh%0A)

For received messages, the possible status values are:

[![Picture of the possible status values for received messages. ](https://downloads.intercomcdn.com/i/o/34825620/897e1d020c07bbf9d1a319d8/image.png?expires=1781167500&signature=eeb2e4a101a17eb88bb442e71fa5193cf2981b5451a9fbb1e2c63e38e7c1e058&req=dyQvFMx4n4ETWLcX3D%2B5hsrNDn84UC4JsD0R%2BKtUFUwDl9CgylW%2BnpzI3fnm%0AVR9jZ%2B7%2B60ls%2BLOb%0A)](https://downloads.intercomcdn.com/i/o/34825620/897e1d020c07bbf9d1a319d8/image.png?expires=1781167500&signature=eeb2e4a101a17eb88bb442e71fa5193cf2981b5451a9fbb1e2c63e38e7c1e058&req=dyQvFMx4n4ETWLcX3D%2B5hsrNDn84UC4JsD0R%2BKtUFUwDl9CgylW%2BnpzI3fnm%0AVR9jZ%2B7%2B60ls%2BLOb%0A)

The delivery\_status field is used to give further details about the delivery confirmation (outbound) or delivery attempt (inbound).

## Message coding

The coding field is an integer representing the message’s encoding. It will typically have one of the following values:

[![A message coding field  with various values in a tabular form. ](https://downloads.intercomcdn.com/i/o/34825681/dddf62cbde4d8ed7a8c6475a/image.png?expires=1781167500&signature=9a4d8710c81fa5df4adc8c90dfa0bf09306b3f96671ec782b37ce7d590e4e50e&req=dyQvFMx4lYATWLcX3D%2B5hsWNbMlfMqxRpmSBGgF8PWJ1maU%2FEUrDqLVPzExT%0AbZ0iU%2BJx1MVBJg8P%0A)](https://downloads.intercomcdn.com/i/o/34825681/dddf62cbde4d8ed7a8c6475a/image.png?expires=1781167500&signature=9a4d8710c81fa5df4adc8c90dfa0bf09306b3f96671ec782b37ce7d590e4e50e&req=dyQvFMx4lYATWLcX3D%2B5hsWNbMlfMqxRpmSBGgF8PWJ1maU%2FEUrDqLVPzExT%0AbZ0iU%2BJx1MVBJg8P%0A)

When you send messages, the encoding is determined on the basis of the characters in the message body. If possible, GSM 7-bit is used; otherwise, UTF-16 is used.

## Message parts

Long messages must be divided into parts for transmission. The size of each part depends on the encoding.

[![Telnyx SMS MDR Report Log For Message Parts ](https://downloads.intercomcdn.com/i/o/34825711/82ef92026146ee5a458400f1/image.png?expires=1781167500&signature=68a9d4855212322289ded4dab0af60a27e17cff601db000535e2d133128a6e5c&req=dyQvFMx5nIATWLcX3D%2B5hoLuACHvaEaTpeFz4On%2BaMc%2FIqpbzXfVpeHhfT5A%0Azh03gAdRqE8xummI%0A)](https://downloads.intercomcdn.com/i/o/34825711/82ef92026146ee5a458400f1/image.png?expires=1781167500&signature=68a9d4855212322289ded4dab0af60a27e17cff601db000535e2d133128a6e5c&req=dyQvFMx5nIATWLcX3D%2B5hoLuACHvaEaTpeFz4On%2BaMc%2FIqpbzXfVpeHhfT5A%0Azh03gAdRqE8xummI%0A)

For outbound messages, there is a maximum message size of 10 parts.

Don't forget that billing takes place on the number of message parts.

`rate` = price per message + carrier fee for one part.  
​`cost` = rate \* message parts.

Billing and Rate Limiting are applied based on the number of parts per message.

---

Related Articles

[How to Download Reports at Telnyx](https://support.telnyx.com/en/articles/1130708-how-to-download-reports-at-telnyx)[How to Leverage Webhooks](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks)[FAQs about MMS at Telnyx](https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx)[Forwarding SMS/MMS Automation using Telnyx Flow](https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow)[Bot-to-Bot Support API: Ask Telnyx Knowledge Agent](https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent)

Did this answer your question?

😞😐😃

Table of contents
