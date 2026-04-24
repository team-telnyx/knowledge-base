---
title: Modifying MMS SMIL Template
summary: SMIL specifies how MMS media files are laid out in MMS.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/smil-template/index
    content_hash: 9cb4ceea5772da6403acdd8f4513d8afdef4b99fe0f3e54f0d92ae89c2dc5a57
updated_at: 2026-04-10T00:00:00Z
---

# Modifying MMS SMIL Template

SMIL specifies how MMS media files are laid out in MMS. Telnyx generates SMIL automatically based on `media_urls` and `text` fields.  Advanced users can add a `smil_template` parameter to the MMS message request. This template will then be used to generate a customized SMIL.

Example of SMIL template:

```xml theme={null}
<smil>
	<head>
		<region id="Text" top="70%" left="0%" height="30%" width="100%" fit="scroll"/>
		<region id="Image" top="0%" left="0%" height="70%" width="100%" fit="meet"/>
	</head>
	<body>
		<par dur="10s">
			<text src="{{ text }}" region="Text" />
			<img src="{{ 0 }}" region="Image" />
		</par>
	</body>
</smil>
```

Note that the template has parameters enclosed in double braces `{{ }}`. During the construction of SMIL these parameters will be automatically replaced with locations of text and media contents. In case of media, `{{ 0 }}` will be replaced with the location of the first URL in the `media_urls` list, `{{ 1 }}` will be replaced with the location of the second URL in the `media_urls` list, and so on. `{{ text }}` will be replaced with the location of the `text` content.

The SMIL template must be set in `smil_template` parameter of the MMS request. It must be properly JSON-escaped:

```json theme={null}
{
	"from": "+13125551234",
	"to": "+18655551234",
	"text": "Hello from Telnyx",
	"media_urls": ["https://example.com/media.jpg"],
	"smil_template": "<smil>\n\t<head>\n\t\t<region id=\"Text\" top=\"70%\"..."
}
```

Please note that many modern handsets (most notably iPhones) ignore SMIL and use their own layout algorithm.
