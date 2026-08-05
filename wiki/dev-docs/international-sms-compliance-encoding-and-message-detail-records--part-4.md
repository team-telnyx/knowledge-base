---
title: International SMS Compliance, Encoding, and Message Detail Records
summary: A consolidated reference covering country-specific SMS compliance requirements
  for the top international destinations, SMS message encoding and segment calculation,
  and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
updated_at: 2026-08-05T13:56:16Z
---

# International SMS Compliance, Encoding, and Message Detail Records

*Part 4 of 6 — see also: [Part 1](international-sms-compliance-encoding-and-message-detail-records--part-1.md), [Part 2](international-sms-compliance-encoding-and-message-detail-records--part-2.md), [Part 3](international-sms-compliance-encoding-and-message-detail-records--part-3.md), [Part 5](international-sms-compliance-encoding-and-message-detail-records--part-5.md), [Part 6](international-sms-compliance-encoding-and-message-detail-records--part-6.md)*

A consolidated reference covering country-specific SMS compliance requirements for the top international destinations, SMS message encoding and segment calculation, and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.

## Message encoding and segmentation

SMS messages are encoded into **segments** of 140 bytes each. You are billed per segment, so understanding encoding is key to controlling costs.

| Encoding | Bits per char | Single segment | Multi-part segment |
| --- | --- | --- | --- |
| GSM 7-bit | 7 | 160 chars | 153 chars |
| ASCII 7-bit | 7 | 160 chars | 153 chars |
| ASCII 8-bit | 8 | 140 chars | 134 chars |
| UTF-16 | 16 | 70 chars | 67 chars |

A single non-GSM-7 character (like an emoji or curly quote) switches the **entire message** to UTF-16, cutting capacity from 160 to 70 characters per segment. This can more than double your costs.

### How segments work

Every SMS message is transmitted in units of **140 bytes**. When a message exceeds one segment, a **6-byte header** (User Data Header, or UDH) is added to each segment for reassembly, reducing the usable space.

```
Single segment:   140 bytes available → 160 GSM-7 chars or 70 UTF-16 chars
Multi-part:       134 bytes per segment → 153 GSM-7 chars or 67 UTF-16 chars
Maximum:          10 segments per message
```

### Segment calculation formula

**GSM-7:**

```
Characters ≤ 160  →  1 segment
Characters > 160  →  ⌈characters / 153⌉ segments
```

**UTF-16:**

```
Characters ≤ 70   →  1 segment
Characters > 70   →  ⌈characters / 67⌉ segments
```

### Cost impact example

Consider a 200-character message:

| Scenario | Encoding | Segments | Relative cost |
| --- | --- | --- | --- |
| All GSM-7 characters | GSM-7 | 2 | 2× |
| Contains one emoji 😀 | UTF-16 | 3 | 3× |
| Contains one curly quote " | UTF-16 | 3 | 3× |
| With smart encoding enabled | GSM-7 | 2 | 2× |

Enable [smart encoding](smart-encoding.md) to automatically replace common Unicode characters (like curly quotes and em dashes) with GSM-7 equivalents, reducing segment counts.

### Encoding by sender type

| Sender type | Default encoding | Fallback |
| --- | --- | --- |
| Long Code | GSM 7-bit | UTF-16 |
| Toll-Free | GSM 7-bit | UTF-16 |
| Short Code | ASCII 7-bit | UTF-16 |
| Alphanumeric | GSM 7-bit | UTF-16 |

If your message contains characters outside the default encoding's character set, the fallback encoding is used automatically for the entire message. MMS and RCS messages use **UTF-8** encoding by default and are not affected by these limits.

### GSM 7-bit character set

Telnyx uses a GSM 7-bit encoding optimized for maximum carrier compatibility. Only characters in this set will keep your message in the efficient GSM-7 encoding.

**Standard characters (1 character each):**

- Letters: `A–Z`, `a–z`
- Digits: `0–9`
- Symbols and punctuation: `! " # $ % & ' ( ) * + , - . / : ; < = > ? @`
- Special characters include: space, line feed, carriage return, `_`, `£`, `¥`, accented Latin characters (`è é ù ì ò Ø ø Å å Æ æ ß É ¡ Ä Ö Ñ Ü § ¿ ä ö ñ ü à`)

**Extended characters (2 characters each):**

These characters require an escape sequence and count as **2 characters** in segment calculations:

| Character | Description | Character count |
| --- | --- | --- |
| `~` | Tilde | 2 |
| `^` | Circumflex | 2 |
| `\|` | Pipe / vertical bar | 2 |
| `\\` | Backslash | 2 |
| `{` | Left curly bracket | 2 |
| `}` | Right curly bracket | 2 |
| `[` | Left square bracket | 2 |
| `]` | Right square bracket | 2 |
| `€` | Euro sign | 2 |

Extended characters are easy to overlook when estimating segment counts. A message with 155 standard characters and 3 pipe characters (`|`) uses 155 + (3 × 2) = 161 character slots, requiring **2 segments** instead of 1.

### Common encoding issues

**Message unexpectedly uses UTF-16 (too many segments):** A non-GSM-7 character is present, forcing the entire message to UTF-16. Common culprits include curly quotes (`" "`), curly apostrophes (`' '`), em dashes (`—`), and ellipses (`…`). Enable [smart encoding](smart-encoding.md) to auto-replace these characters, or manually replace them with GSM-7 equivalents before sending.

**Emojis dramatically increase segment count:** Emojis force UTF-16 encoding (70 chars/segment instead of 160). Most emojis use **surrogate pairs** and count as 2 UTF-16 characters. If cost is a concern, avoid emojis in SMS. Use emojis freely in MMS/RCS where encoding isn't a factor.

**Extended GSM-7 characters cause unexpected segment splits:** Characters like `[`, `]`, `{`, `}`, `|`, `\\`, `^`, `~`, and `€` are in the GSM-7 extended set and count as **2 characters** each. For example, `"Price: $100 [USD]"` is 18 visible chars but 20 GSM-7 chars.

**Copy-pasted text from Word/Google Docs causes issues:** Word processors often replace straight quotes with curly quotes, hyphens with em dashes, and three periods with an ellipsis character. Enable [smart encoding](smart-encoding.md), sanitize text before sending, or use the `encoding` parameter set to `gsm7` to get a `400` error if non-GSM-7 characters are present.

**Messages truncated or split incorrectly on recipient's phone:** Some older devices or carriers may not support reassembly for messages over a certain number of segments. Keep messages under 3-4 segments for maximum compatibility. Telnyx supports up to 10 segments, but recipient device support varies.

**Non-Latin scripts (Chinese, Arabic, Cyrillic) use too many segments:** Non-Latin characters have no GSM-7 equivalents, so the entire message uses UTF-16 encoding (70 characters per segment). This is expected behavior — plan for higher segment counts when messaging in non-Latin scripts.
