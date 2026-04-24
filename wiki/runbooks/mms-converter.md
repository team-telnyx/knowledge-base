---
title: MMS converter
summary: Optional automatic fallback to SMS when sending MMS to destinations that.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/mms-converter/index
    content_hash: 3806e4b04e7b78896de51b2edb3d127219c673d45094af39615ec3906a2c0b2c
updated_at: 2026-04-10T00:00:00Z
---

# MMS converter

Optional automatic fallback to SMS when sending MMS to destinations that
don't support it.

While your message's source number may support sending MMS, the destination
number might not support receiving it. Normally, this will prevent you from
sending MMS to this destination. When **MMS converter** is enabled on your
messaging profile, however, your MMS will be converted to an SMS message by
Telnyx and then sent to the destination. Messages sent as SMS are unaffected by
this feature and will be sent as usual.

The resultant webhooks for messages sent with this feature enabled will indicate
the protocol that was used to send the message. For example: when an MMS message
is sent and fallback happens, the webhook will indicate that an SMS message was
sent, and when an MMS message is sent and fallback doesn't happen, the webhook
will indicate that an MMS message was sent.

If fallback happens, the destination will receive an SMS formatted to contain
the media URLs specified in the request. Each media URL will appear on its own
line, immediately after the message body, if any.

## Examples

Note how the media URL(s) appear on the destination exactly as provided in the
request. No shortlinking or other transformations are applied on your behalf.

### Message body and one media URL

If your request includes:

* `"text": "message body that\nis potentially spread across multiple lines"`
* `"media_urls": ["https://example.com/image.png"]`

The message received on the destination will look like this:

```
message body that
is potentially spread across multiple lines
https://example.com/image.png
```

### Message body and two media URLs

If your request includes:

* `"text": "message body"`
* `"media_urls": ["https://example.com/one.png", "https://example.com/two.png"]`

The message received on the destination will look like this:

```
message body
https://example.com/one.png
https://example.com/two.png
```

### Only one media URL

If your request doesn't set `text` and includes:

* `"media_urls": ["https://example.com/image.png"]`

The message received on the destination will look like this:

```
https://example.com/image.png
```

## Enable MMS converter

This behavior is not enabled by default; if you want to make use of this feature
then you must enable it first. This is controlled at the messaging profile level
by an optional boolean field called `mms_fall_back_to_sms`, which you can either
set at [creation time][create] or [update later][update] if you'd like to change
an existing messaging profile.

[create]: /api-reference/profiles/create-a-messaging-profile

[update]: /api-reference/profiles/update-a-messaging-profile
