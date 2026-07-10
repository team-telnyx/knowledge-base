---
source_url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
scraped: 2026-07-08
content_hash: 9ff074e9d222aeaeefab4ef8a7b4f48bd3e2475aad3e16d893deda30e649308b
---

FAQs about MMS at Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# FAQs about MMS at Telnyx

Here you will find frequently asked questions about sending and receiving MMS, answered.

Written by Telnyx Engineering

October 30, 2024

Table of contents

# Telnyx MMS: Character Limits, File Types, and Sending Rules

## **What is the character limit for MMS?**

Multimedia Messaging Service (MMS) has different limits compared to SMS, primarily because MMS is designed to handle multimedia content like images, videos, and audio, along with extended text. The character limit for MMS messages is typically much higher than for SMS.

1. **Higher Character Limit**: MMS allows for a significantly higher number of characters per message compared to SMS. While there is no standardized character limit for MMS, many carriers allow several thousand characters per message. The exact limit can vary depending on the carrier and the device.
2. **Limitations Based on Carrier and Device**: Different mobile carriers and devices may have their own limitations for MMS size, including both the text and multimedia content. These limits can range from 300 KB to over 1 MB per message.
3. **Content Type Affects Size**: The total size of an MMS is not just determined by the length of the text but also by the size of the included multimedia files. High-resolution images, long videos, or audio files will take up more space, potentially limiting the amount of text that can be included.
4. **Network and Device Compatibility**: The ability to send and receive MMS messages also depends on network compatibility and the capabilities of the sender’s and recipient's devices. Older devices or certain network conditions may limit the effectiveness of sending large MMS messages.

## **What are the supported file types for MMS?**

* text/plain
* text/vcard
* image/jpeg
* image/png
* image/gif
* video/3gpp
* video/mp4

## **What should the “content-type” of my stored media be, and how does it differ case-by-case?**

Content type should equal to one of the above. It can also be application/octet-stream - in that case we try to guess the content type based on the media binary.

## **Are media files for outbound messages cached within Telnyx? If so, for how long?**

Yes, media files for outbound messages are cached within Telnyx for an hour. Changing the media url -- like adding a spurious query parameter -- will invalidate the cache.

## **How can I secure my media for outbound messages to only be read by Telnyx?**

Whitelist 192.76.120.192 and 192.76.120.193.

## ​**Does MMS work between countries (ie USA to Brazil)?**

No, we don't have this capability yet.

## **How do MMS DLRs function?**

There are three kinds of DLRs. Normally we expect each MMS to generate all of the following:

1. Internal DLR that is generated when we successfully submit MMS to the terminating carriers. This DLR changes the status of the stored MDR to “sent”.
2. MM4\_forward.RES - we get this when the terminating carriers pass our MMS message to the destination carrier. This DLR changes the status of the stored MDR to “delivered”.
3. MM4\_delivery\_report.REQ - we (sometimes) get it from the destination carrier and it indicates what happened to the message - usually it means it was delivered to the handset.

## **How does MMS differ when sending from a Toll-Free Number?**

MMS can be sent from a Toll-Free Number, at a rate limit of 1200 Messages Per Minute. However other rate limits like account wide rate limits can also come into play here. Account wide messaging rates is 15 messages per second.

## **How does MMS differ when sending from a Short-Code?**

We need a [short code](https://telnyx.com/products/sms-short-code) provisioned with our terminating carriers and the campaign must be approved by all major carriers.

## **How can I send a long-text message as a MMS (with no attachments)?**

Set the parameter as “type=MMS”.

## **What is the maximum file size of a single attachment?**

[Total attachment size must be less than 1 MB](https://developers.telnyx.com/api/messaging/send-message). Ideally, it should be 1MB minus 100KB to give some space for encoding overhead.

* Tier 1 Carriers (Verizon, T-Mobile, AT&T, Sprint): Up to 1 MB
* Tier 2 Carriers: Up to 600 KB
* Tier 3 Carriers: Up to 300 KB

## **What about total message size with multiple attachments?**

Total message size is capped at 1 MB, and no more than 10 **media\_urls** are allowed.

## **Is an SMS treated as an MMS if there are no media\_urls attachments included?**

Yes, please make sure to only include the **media\_urls** property in your request if you intend to send an MMS. Otherwise, doing so will result in your SMS being treated as an MMS, even without any url attachments included in the media\_urls property.

## **What is MMS Fallback?**

This feature is a part of the [messaging profile setting](https://portal.telnyx.com/#/app/programmable-messaging/profiles) and [API](https://developers.telnyx.com/docs/messaging/messages/mms-converter). When using Telnyx's MMS converter feature, if the destination number does not support MMS, your MMS will be automatically converted into an SMS message. This conversion ensures delivery even when MMS is not supported at the receiving end. Regular SMS messages are sent as usual without any conversion. Additionally, webhooks will provide information on the protocol used for each message: if MMS fallback occurs, the webhook will indicate that an SMS was sent; otherwise, it will show that an MMS was sent. In cases of fallback, the recipient will receive an SMS with each media URL from the original MMS message displayed on separate lines following the message body. This feature is a part of the messaging profile setting.

## **What is MMS Transcoding?**

This feature is a part of the [messaging profile setting](https://portal.telnyx.com/#/app/programmable-messaging/profiles) and [API](https://developers.telnyx.com/docs/messaging/messages/mms-transcoding). To meet various size restrictions imposed by destination carriers on MMS messages, a feature called mms\_transcoding is provided. When enabled, this setting adjusts the media size to comply with the size requirements of the destination carrier and phone number type. However, it's important to note that only images and videos are resized, and animated GIFs are not supported; they must be sent in a small enough size. Resizing typically results in a reduction in media quality. During this process, images are converted to JPEG format, and videos to H.264 MP4 format.

## MMS Limitations and Future Solutions

Currently, MMS messaging through Telnyx is only supported within the USA and Canada. For international multimedia messaging, we are actively exploring solutions to enhance our global reach. As a future-ready alternative, we are developing a Rich Communication Services (RCS) product, expected to enter beta testing by the end of year 2024 or early Q1 2025. RCS will provide a more versatile messaging experience with features beyond standard MMS, enabling richer multimedia content, improved interactivity, and support for a broader range of devices and carriers worldwide. Keep an eye out for this new capability to expand your messaging possibilities beyond traditional MMS.

---

Related Articles

[What is Telnyx?](https://support.telnyx.com/en/articles/1130637-what-is-telnyx)[MMS Sending and Receiving](https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving)[Telnyx Messaging Error Codes](https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes)[Group Messaging - Bulk Sending MMS](https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)

Did this answer your question?

😞😐😃

Table of contents
