---
title: "Understand Telnyx SMS MDR Report Log"
summary: "You can check your MDR (message detail record) for every message sent or received. See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--1130611-understand-telnyx-sms-mdr-report-log.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--1130611-understand-telnyx-sms-mdr-report-log.md -->

# Understand Telnyx SMS MDR Report Log

You can check your MDR (message detail record) for every message sent or received. See Telnyx guidance and requirements.




## What is an MDR?

For every sent or received message, an MDR (message detail record) will be written. You can access and generate these report logs under **Reports** (left hand side navigation bar) -> **Reporting** in your Mission Control Portal Account as seen below.

![](_images/9bb528340ef5c71d.png)

## What are the different fields of information available?

MDRs are stored as JSON objects. These are the most important fields contained in each MDR:

![The most important fields in Message Detail Records containing field name, type, and description. ](_images/8ac8381c94a87961.png)

The embedded **body** object contains the following fields:

![Picture of various fields contained in an embedded body object. ](_images/960604f91f0b336d.png)

For privacy reasons, a message’s body text is only stored for up to 10 days before it is wiped from our system. At that point, the hash fields can be used to identify messages.

## Status

For **sent messages**, the possible status values are:

![Pictorial representation of possible status values for sent messages. ](_images/49567343eec330b0.png)

For received messages, the possible status values are:

![Picture of the possible status values for received messages. ](_images/34901ef7f9fa8217.png)

The delivery\_status field is used to give further details about the delivery confirmation (outbound) or delivery attempt (inbound).

## Message coding

The coding field is an integer representing the message’s encoding. It will typically have one of the following values:

![A message coding field  with various values in a tabular form. ](_images/bcae8d1a1cce3439.png)

When you send messages, the encoding is determined on the basis of the characters in the message body. If possible, GSM 7-bit is used; otherwise, UTF-16 is used.

## Message parts

Long messages must be divided into parts for transmission. The size of each part depends on the encoding.

![Telnyx SMS MDR Report Log For Message Parts ](_images/443690d996a0bbbf.png)

For outbound messages, there is a maximum message size of 10 parts.

Don't forget that billing takes place on the number of message parts.

`rate` = price per message + carrier fee for one part.
​`cost` = rate \* message parts.

Billing and Rate Limiting are applied based on the number of parts per message.
