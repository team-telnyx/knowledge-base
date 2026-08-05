---
title: Messaging Features
summary: Overview of Telnyx messaging features including short codes, smart encoding,
  MMS SMIL templates, and sticky sender for consistent number assignment.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/short-code/index
- url: https://developers.telnyx.com/docs/messaging/messages/smart-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
updated_at: 2026-08-05T13:57:46Z
---

# Messaging Features

*Part 2 of 3 — see also: [Part 1](messaging-features--part-1.md), [Part 3](messaging-features--part-3.md)*

Overview of Telnyx messaging features including short codes, smart encoding, MMS SMIL templates, and sticky sender for consistent number assignment.

## Smart Encoding

Smart encoding automatically replaces Unicode characters with visually similar GSM-7 characters. This keeps your messages in the more efficient GSM-7 encoding, reducing segment counts and costs.

Smart encoding applies to SMS only. MMS and RCS messages use UTF-8 encoding by default and are not affected.

### Why use smart encoding

SMS messages using GSM-7 encoding fit **160 characters per segment**. When a message contains even one Unicode character outside GSM-7, the entire message switches to UTF-16 encoding, which only fits **70 characters per segment**.

A single smart quote (`"`) or em dash (`—`) can more than double your messaging costs.

**Example:**

| Message | Encoding | Segments | Cost impact |
| --- | --- | --- | --- |
| `Hello, how are you?` (150 chars) | GSM-7 | 1 | Base cost |
| `Hello, how are you?` (150 chars with "smart quotes") | UTF-16 | 3 | 3× cost |
| `Hello, how are you?` (same, smart encoding ON) | GSM-7 | 1 | Base cost |

Smart encoding is especially valuable when your message text originates from word processors, CMS platforms, or mobile keyboards that silently insert Unicode characters like curly quotes, em dashes, or non-breaking spaces.

### How it works

When smart encoding is enabled:

1. Your message text is scanned for Unicode characters that have GSM-7 equivalents.
2. Matching characters are automatically replaced (e.g., `"` → `"`, `—` → `-`, `…` → `...`).
3. The final encoding (GSM-7 or UTF-16) is determined **after** all substitutions.
4. The segment count is recalculated based on the transformed text.
5. The API response includes metadata about the transformation.

**Webhooks return the original text.** The `text` field in delivery webhooks contains your original message, not the smart-encoded version. This ensures your application's message tracking stays consistent.

### Enable smart encoding

You can enable smart encoding at two levels: on a **messaging profile** (applies to all messages) or on a **per-request** basis.

**On a messaging profile:**

Enable smart encoding as a default for all messages sent through a profile.

```
curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "smart_encoding": true
  }'
```

To enable via the portal, navigate to [Messaging > Messaging Profiles](https://portal.telnyx.com/#/app/messaging), select your profile, toggle **Smart Encoding** to enabled, and click **Save**.

**Per-request control:**

Override the profile setting on individual messages using the `encoding` parameter:

| Value | Behavior |
| --- | --- |
| `auto` | Follow the profile's `smart_encoding` setting (default). |
| `gsm7` | Force GSM-7 encoding. Smart encoding is applied. Returns `400` if the message contains characters that cannot be converted to GSM-7 (e.g., emoji). |
| `ucs2` | Force UCS-2 encoding. **Skips smart encoding entirely.** |

The request-level `encoding` parameter **takes precedence** over the messaging profile's `smart_encoding` setting.

```
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Don\u2019t miss our \u201cflash sale\u201d \u2014 50% off!",
    "encoding": "auto"
  }'
```

### Response metadata

When smart encoding is applied, the API response includes detailed metadata:

```
{
  "data": {
    "id": "8a0c35c0-5eed-4c0e-b1f0-abc123456789",
    "type": "SMS",
    "encoding": "GSM-7",
    "parts": 1,
    "smart_encoding": {
      "smart_encoding_applied": true,
      "final_encoding": "gsm7",
      "segment_count": 1,
      "character_count": 155,
      "replaced_character_count": 3,
      "length_change": 2
    }
  }
}
```

| Field | Description |
| --- | --- |
| `smart_encoding_applied` | Whether any characters were replaced. |
| `final_encoding` | The encoding used after transformation (`gsm7` or `ucs2`). |
| `segment_count` | Number of segments after smart encoding. |
| `character_count` | Message length after transformation. |
| `replaced_character_count` | Number of unique characters that were substituted. |
| `length_change` | Difference in length (positive means message grew, e.g., `…` → `...`). |

The `parts` field in the top-level response reflects the segment count **after** smart encoding, so you always see the actual billing impact.

### Precedence rules

Smart encoding behavior is determined by a combination of your messaging profile setting and the per-request `encoding` parameter:

| Profile `smart_encoding` | Request `encoding` | Behavior |
| --- | --- | --- |
| `true` | *(not set)* | Smart encoding **applied** |
| `false` | *(not set)* | Smart encoding **not applied** |
| `true` | `auto` | Smart encoding **applied** |
| `false` | `auto` | Smart encoding **not applied** |
| `true` or `false` | `gsm7` | Smart encoding **applied**, must result in GSM-7 or returns `400` |
| `true` or `false` | `ucs2` | Smart encoding **skipped**, forced UCS-2 |

The request-level `encoding` parameter always takes precedence over the messaging profile setting.

### Character substitutions

Smart encoding replaces 200+ Unicode characters with GSM-7 equivalents. Common categories include:

- **Quotation marks** — e.g., `«` (U+00AB), `»` (U+00BB), `"` (U+201C), `"` (U+201D) → `"`
- **Apostrophes and single quotes** — e.g., `'` (U+2018), `'` (U+2019), `` ` `` (U+0060) → `'`
- **Dashes and hyphens** — e.g., `—` (U+2014), `–` (U+2013), `•` (U+2022) → `-`
- **Slashes and division** — e.g., `÷` (U+00F7), `¼` (U+00BC), `½` (U+00BD) → `/` or `1/4`, `1/2`
- **Backslashes** — e.g., `⧹` (U+29F9), `＼` (U+FF3C) → `\`
- **Underscores and vertical lines** — e.g., `＿` (U+FF3F), `|` (U+FF5C) → `\_` or `|`
- **Symbols and punctuation** — e.g., `﹫` (U+FE6B), `＄` (U+FF04), `…` (U+2026) → `@`, `$`, `...`
- **Commas** — e.g., `‚` (U+201A), `，` (U+FF0C) → `,`
- **Parentheses and brackets** — e.g., `（` (U+FF08), `｛` (U+FF5B) → `(`, `{`
- **Asterisks** — e.g., `＊` (U+FF0A), `⁎` (U+204E) → `\*`
- **Math, comparison, periods, and colons** — e.g., `＋` (U+FF0B), `＝` (U+FF1D), `：` (U+FF1A) → `+`, `=`, `:`
- **Fullwidth digits** — e.g., `０` (U+FF10) through `９` (U+FF19) → `0`–`9`
- **Fullwidth and small capital letters** — Fullwidth A–Z and a–z map to ASCII; small capitals like `ᴀ` (U+1D00) → `A`
- **Greek letters** — Visually similar Greek capitals like `Α` (U+0391) → `A`, `Β` (U+0392) → `B`
- **Tildes and circumflex** — e.g., `ˆ` (U+02C6), `˜` (U+02DC) → `^`, `~`
- **Whitespace characters** — e.g., no-break space (U+00A0), en space (U+2002) → space; zero-width space (U+200B) removed
- **Control characters** — Tab (U+0009) → 7 spaces; null and other control characters removed

### Edge cases

- **Message length increases** — Some substitutions increase message length. For example, horizontal ellipsis (`…`) becomes three periods (`...`) — adds 2 characters; tab (U+0009) becomes 7 spaces — adds 6 characters; vulgar fractions like `½` become `1/2` — adds 2 characters. The segment count is calculated **after** these replacements, so a message near the 160-character limit may become multi-part after transformation.
- **Mixed replaceable and non-replaceable characters** — If your message contains both replaceable Unicode characters and non-replaceable ones (like emojis), smart encoding still applies all possible substitutions. However, the non-replaceable characters will keep the message in UTF-16 encoding. This is still beneficial — fewer Unicode characters means a shorter UTF-16 message and potentially fewer segments.
- **Extended GSM-7 characters** — The characters `~`, `^`, `|`, `\`, `{`, `}`, `[`, `]` are part of the GSM-7 extended set and count as **2 characters** each when calculating segment length. Smart encoding accounts for this when determining the final segment count.
- **Zero-width characters and empty messages** — Zero-width characters (like U+200B zero-width space) are removed entirely. If your message consists entirely of zero-width or control characters that all get removed, the API returns a `400` error — messages cannot be empty after transformation.
- **`encoding=gsm7` with non-convertible characters** — If you set `encoding=gsm7` on a request but the message contains characters that cannot be represented in GSM-7 (e.g., emoji), the API returns a `400` error rather than silently dropping characters.

### Limitations

- **SMS only** — MMS and RCS use UTF-8 encoding by default and are not affected by smart encoding.
- **Not all characters convert** — Emojis and non-Latin scripts (e.g., Chinese, Arabic, Cyrillic) have no GSM-7 equivalents and will still trigger UTF-16 encoding.
- **Visual differences** — Substitutions may slightly alter the appearance of your message. Review the character tables above to understand what changes will occur.
- **Length may increase** — Some substitutions produce longer output (e.g., `…` → `...`). Always check the response metadata for the actual segment count.
