---
title: Message Encoding
summary: Understand SMS encoding types, character limits, segment calculations, and how to optimize message length to reduce costs.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
    content_hash: e3ac1e89ff892ba9451ad6267c9104b093909f7a4fbf2af96f8531b4081551d5
updated_at: 2026-04-10T00:00:00Z
---

# Message Encoding

Understand SMS encoding types, character limits, segment calculations, and how to optimize message length to reduce costs.

SMS messages are encoded into **segments** of 140 bytes each. You are billed per segment, so understanding encoding is key to controlling costs.

The encoding determines how many characters fit in each segment:

| Encoding    | Bits per char | Single segment | Multi-part segment |
| ----------- | ------------- | -------------- | ------------------ |
| GSM 7-bit   | 7             | 160 chars      | 153 chars          |
| ASCII 7-bit | 7             | 160 chars      | 153 chars          |
| ASCII 8-bit | 8             | 140 chars      | 134 chars          |
| UTF-16      | 16            | 70 chars       | 67 chars           |

> **Warning:** A single non-GSM-7 character (like an emoji or curly quote) switches the **entire message** to UTF-16, cutting capacity from 160 to 70 characters per segment. This can more than double your costs.

## Segment calculator

Use this interactive tool to check how your message will be encoded and segmented:

## How segments work

Every SMS message is transmitted in units of **140 bytes**. When a message exceeds one segment, a **6-byte header** (User Data Header, or UDH) is added to each segment for reassembly, reducing the usable space.

```
Single segment:   140 bytes available → 160 GSM-7 chars or 70 UTF-16 chars
Multi-part:       134 bytes per segment → 153 GSM-7 chars or 67 UTF-16 chars
Maximum:          10 segments per message
```

### Segment calculation formula

To calculate the number of segments for a message:

### GSM-7

    ```
    Characters ≤ 160  →  1 segment
    Characters > 160  →  ⌈characters / 153⌉ segments

    Examples:
    - 100 chars = 1 segment
    - 160 chars = 1 segment
    - 161 chars = 2 segments (153 + 8)
    - 306 chars = 2 segments (153 + 153)
    - 307 chars = 3 segments (153 + 153 + 1)
    - 1530 chars = 10 segments (maximum)
    ```

### UTF-16

    ```
    Characters ≤ 70   →  1 segment
    Characters > 70   →  ⌈characters / 67⌉ segments

    Examples:
    - 50 chars = 1 segment
    - 70 chars = 1 segment
    - 71 chars = 2 segments (67 + 4)
    - 134 chars = 2 segments (67 + 67)
    - 135 chars = 3 segments (67 + 67 + 1)
    - 670 chars = 10 segments (maximum)
    ```

### Cost impact example

Consider a 200-character message:

| Scenario                                                                     | Encoding | Segments | Relative cost |
| ---------------------------------------------------------------------------- | -------- | -------- | ------------- |
| All GSM-7 characters                                                         | GSM-7    | 2        | 2×            |
| Contains one emoji 😀                                                        | UTF-16   | 3        | 3×            |
| Contains one curly quote "                                                   | UTF-16   | 3        | 3×            |
| With [smart encoding](smart-encoding.md) enabled | GSM-7    | 2        | 2×            |

> **Note:** Enable [smart encoding](smart-encoding.md) to automatically replace common Unicode characters (like curly quotes and em dashes) with GSM-7 equivalents, reducing segment counts.

***

## Encoding by sender type

| Sender type  | Default encoding | Fallback |
| ------------ | ---------------- | -------- |
| Long Code    | GSM 7-bit        | UTF-16   |
| Toll-Free    | GSM 7-bit        | UTF-16   |
| Short Code   | ASCII 7-bit      | UTF-16   |
| Alphanumeric | GSM 7-bit        | UTF-16   |

If your message contains characters outside the default encoding's character set, the fallback encoding is used automatically for the entire message.

> **Note:** MMS and RCS messages use **UTF-8** encoding by default and are not affected by these limits.

***

## GSM 7-bit character set

Telnyx uses a GSM 7-bit encoding optimized for maximum carrier compatibility. Only characters in this set will keep your message in the efficient GSM-7 encoding.

**Standard characters (1 character each)**

  **Letters:**

  ```
  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  a b c d e f g h i j k l m n o p q r s t u v w x y z
  ```

  **Digits:**

  ```
  0 1 2 3 4 5 6 7 8 9
  ```

  **Symbols and punctuation:**

  ```
  ! " # $ % & ' ( ) * + , - . / : ; < = > ? @
  ```

  **Special characters:**

  | Character | Description          |
  | --------- | -------------------- |
  | `space`   | Space                |
  | `\n`      | Line feed            |
  | `\r`      | Carriage return      |
  | `_`       | Underscore           |
  | `£`       | Pound sign           |
  | `¥`       | Yen sign             |
  | `è`       | e grave              |
  | `é`       | e acute              |
  | `ù`       | u grave              |
  | `ì`       | i grave              |
  | `ò`       | o grave              |
  | `Ø`       | O with stroke        |
  | `ø`       | o with stroke        |
  | `Å`       | A with ring          |
  | `å`       | a with ring          |
  | `Æ`       | AE ligature          |
  | `æ`       | ae ligature          |
  | `ß`       | Sharp s              |
  | `É`       | E acute              |
  | `¡`       | Inverted exclamation |
  | `Ä`       | A umlaut             |
  | `Ö`       | O umlaut             |
  | `Ñ`       | N tilde              |
  | `Ü`       | U umlaut             |
  | `§`       | Section sign         |
  | `¿`       | Inverted question    |
  | `ä`       | a umlaut             |
  | `ö`       | o umlaut             |
  | `ñ`       | n tilde              |
  | `ü`       | u umlaut             |
  | `à`       | a grave              |

---

**Extended characters (2 characters each)**

  These characters require an escape sequence and count as **2 characters** in segment calculations:

  | Character | Description          | Character count |
  | --------- | -------------------- | --------------- |
  | `~`       | Tilde                | 2               |
  | `^`       | Circumflex           | 2               |
  | `\|`      | Pipe / vertical bar  | 2               |
  | `\`       | Backslash            | 2               |
  | `{`       | Left curly bracket   | 2               |
  | `}`       | Right curly bracket  | 2               |
  | `[`       | Left square bracket  | 2               |
  | `]`       | Right square bracket | 2               |
  | `€`       | Euro sign            | 2               |

  > **Warning:** Extended characters are easy to overlook when estimating segment counts. A message with 155 standard characters and 3 pipe characters (`|`) uses 155 + (3 × 2) = 161 character slots, requiring **2 segments** instead of 1.

---

***

## Detecting encoding in your application

Before sending, you can check if a message will use GSM-7 or UTF-16 encoding to estimate costs. Here are helper functions for each language:

  ```python
  import re

  # GSM-7 basic character set
  GSM7_BASIC = set(
      "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ ÆæßÉ"
      " !\"#¤%&'()*+,-./0123456789:;<=>?"
      "¡ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      "ÄÖÑܧ¿abcdefghijklmnopqrstuvwxyz"
      "äöñüà"
  )
  GSM7_EXTENDED = set("^{}\\[~]|€")

  def calculate_segments(text: str) -> dict:
      """Calculate encoding and segment count for an SMS message."""
      is_gsm7 = all(c in GSM7_BASIC or c in GSM7_EXTENDED for c in text)

      if is_gsm7:
          # Count extended chars as 2
          char_count = sum(2 if c in GSM7_EXTENDED else 1 for c in text)
          if char_count <= 160:
              segments = 1
          else:
              segments = -(-char_count // 153)  # ceiling division
          return {"encoding": "GSM-7", "char_count": char_count, "segments": segments}
      else:
          # UTF-16: emojis count as 2 chars (surrogate pairs)
          char_count = 0
          for c in text:
              char_count += 2 if ord(c) > 0xFFFF else 1
          if char_count <= 70:
              segments = 1
          else:
              segments = -(-char_count // 67)
          return {"encoding": "UTF-16", "char_count": char_count, "segments": segments}

  # Example usage
  result = calculate_segments("Hello, world!")
  print(f"Encoding: {result['encoding']}, Segments: {result['segments']}")
  # Output: Encoding: GSM-7, Segments: 1

  result = calculate_segments("Hello 😀")
  print(f"Encoding: {result['encoding']}, Segments: {result['segments']}")
  # Output: Encoding: UTF-16, Segments: 1
  ```

  ```javascript
  const GSM7_BASIC = new Set(
    '@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ ÆæßÉ' +
    ' !"#¤%&\'()*+,-./0123456789:;<=>?' +
    '¡ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
    'ÄÖÑܧ¿abcdefghijklmnopqrstuvwxyz' +
    'äöñüà'
  );
  const GSM7_EXTENDED = new Set('^{}\\[~]|€');

  function calculateSegments(text) {
    const chars = [...text];
    const isGsm7 = chars.every(c => GSM7_BASIC.has(c) || GSM7_EXTENDED.has(c));

    if (isGsm7) {
      const charCount = chars.reduce(
        (sum, c) => sum + (GSM7_EXTENDED.has(c) ? 2 : 1), 0
      );
      const segments = charCount <= 160 ? 1 : Math.ceil(charCount / 153);
      return { encoding: 'GSM-7', charCount, segments };
    } else {
      const charCount = chars.reduce(
        (sum, c) => sum + (c.codePointAt(0) > 0xFFFF ? 2 : 1), 0
      );
      const segments = charCount <= 70 ? 1 : Math.ceil(charCount / 67);
      return { encoding: 'UTF-16', charCount, segments };
    }
  }

  // Example usage
  console.log(calculateSegments('Hello, world!'));
  // { encoding: 'GSM-7', charCount: 13, segments: 1 }

  console.log(calculateSegments('Hello 😀'));
  // { encoding: 'UTF-16', charCount: 8, segments: 1 }
  ```

  ```ruby
  GSM7_BASIC = Set.new(
    "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ ÆæßÉ" \
    " !\"#¤%&'()*+,-./0123456789:;<=>?" \
    "¡ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
    "ÄÖÑܧ¿abcdefghijklmnopqrstuvwxyz" \
    "äöñüà"
  ).flat_map(&:chars).to_set
  GSM7_EXTENDED = Set.new("^{}\\[~]|€".chars)

  def calculate_segments(text)
    chars = text.chars
    is_gsm7 = chars.all? { |c| GSM7_BASIC.include?(c) || GSM7_EXTENDED.include?(c) }

    if is_gsm7
      char_count = chars.sum { |c| GSM7_EXTENDED.include?(c) ? 2 : 1 }
      segments = char_count <= 160 ? 1 : (char_count.to_f / 153).ceil
      { encoding: "GSM-7", char_count: char_count, segments: segments }
    else
      char_count = chars.sum { |c| c.ord > 0xFFFF ? 2 : 1 }
      segments = char_count <= 70 ? 1 : (char_count.to_f / 67).ceil
      { encoding: "UTF-16", char_count: char_count, segments: segments }
    end
  end

  puts calculate_segments("Hello, world!")
  # {:encoding=>"GSM-7", :char_count=>13, :segments=>1}
  ```

  ```go
  package main

  import (
  	"fmt"
  	"math"
  	"unicode/utf8"
  )

  var gsm7Basic = map[rune]bool{
  	'@': true, '£': true, '$': true, '¥': true, 'è': true, 'é': true,
  	'ù': true, 'ì': true, 'ò': true, 'Ç': true, '\n': true, 'Ø': true,
  	'ø': true, '\r': true, 'Å': true, 'å': true, 'Δ': true, '_': true,
  	'Φ': true, 'Γ': true, 'Λ': true, 'Ω': true, 'Π': true, 'Ψ': true,
  	'Σ': true, 'Θ': true, 'Ξ': true, ' ': true, 'Æ': true, 'æ': true,
  	'ß': true, 'É': true, '¡': true, 'Ä': true, 'Ö': true, 'Ñ': true,
  	'Ü': true, '§': true, '¿': true, 'ä': true, 'ö': true, 'ñ': true,
  	'ü': true, 'à': true,
  }

  var gsm7Extended = map[rune]bool{
  	'^': true, '{': true, '}': true, '\\': true,
  	'[': true, '~': true, ']': true, '|': true, '€': true,
  }

  func init() {
  	// Add printable ASCII
  	for c := '!'; c <= '~'; c++ {
  		gsm7Basic[c] = true
  	}
  }

  type SegmentResult struct {
  	Encoding  string
  	CharCount int
  	Segments  int
  }

  func CalculateSegments(text string) SegmentResult {
  	isGSM7 := true
  	for _, r := range text {
  		if !gsm7Basic[r] && !gsm7Extended[r] {
  			isGSM7 = false
  			break
  		}
  	}

  	if isGSM7 {
  		charCount := 0
  		for _, r := range text {
  			if gsm7Extended[r] {
  				charCount += 2
  			} else {
  				charCount++
  			}
  		}
  		segments := 1
  		if charCount > 160 {
  			segments = int(math.Ceil(float64(charCount) / 153))
  		}
  		return SegmentResult{"GSM-7", charCount, segments}
  	}

  	charCount := 0
  	for _, r := range text {
  		if r > 0xFFFF {
  			charCount += 2
  		} else {
  			charCount++
  		}
  	}
  	_ = utf8.RuneCountInString(text) // ensure valid UTF-8
  	segments := 1
  	if charCount > 70 {
  		segments = int(math.Ceil(float64(charCount) / 67))
  	}
  	return SegmentResult{"UTF-16", charCount, segments}
  }

  func main() {
  	fmt.Println(CalculateSegments("Hello, world!"))
  	// {GSM-7 13 1}
  }
  ```

  ```java
  import java.util.Set;

  public class SmsEncoding {

      private static final Set GSM7_EXTENDED =
          Set.of('^', '{', '}', '\\', '[', '~', ']', '|', '€');

      private static final String GSM7_CHARS =
          "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ ÆæßÉ"
          + " !\"#¤%&'()*+,-./0123456789:;<=>?"
          + "¡ABCDEFGHIJKLMNOPQRSTUVWXYZ"
          + "ÄÖÑܧ¿abcdefghijklmnopqrstuvwxyz"
          + "äöñüà^{}\\[~]|€";

      private static final Set GSM7_BASIC = new java.util.HashSet<>();
      static {
          for (char c : GSM7_CHARS.toCharArray()) {
              GSM7_BASIC.add(c);
          }
      }

      public record SegmentResult(String encoding, int charCount, int segments) {}

      public static SegmentResult calculateSegments(String text) {
          boolean isGsm7 = text.chars()
              .mapToObj(c -> (char) c)
              .allMatch(c -> GSM7_BASIC.contains(c) || GSM7_EXTENDED.contains(c));

          if (isGsm7) {
              int charCount = text.chars()
                  .map(c -> GSM7_EXTENDED.contains((char) c) ? 2 : 1)
                  .sum();
              int segments = charCount <= 160 ? 1 : (int) Math.ceil(charCount / 153.0);
              return new SegmentResult("GSM-7", charCount, segments);
          } else {
              int charCount = text.codePoints()
                  .map(cp -> cp > 0xFFFF ? 2 : 1)
                  .sum();
              int segments = charCount <= 70 ? 1 : (int) Math.ceil(charCount / 67.0);
              return new SegmentResult("UTF-16", charCount, segments);
          }
      }

      public static void main(String[] args) {
          System.out.println(calculateSegments("Hello, world!"));
          // SegmentResult[encoding=GSM-7, charCount=13, segments=1]
      }
  }
  ```

  ```csharp .NET theme={null}
  using System;
  using System.Collections.Generic;
  using System.Linq;

  public record SegmentResult(string Encoding, int CharCount, int Segments);

  public static class SmsEncoding
  {
      private static readonly HashSet<char> Gsm7Extended =
          new("^{}\\[~]|€");

      private static readonly HashSet<char> Gsm7Basic = new(
          "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ ÆæßÉ"
          + " !\"#¤%&'()*+,-./0123456789:;<=>?"
          + "¡ABCDEFGHIJKLMNOPQRSTUVWXYZ"
          + "ÄÖÑܧ¿abcdefghijklmnopqrstuvwxyz"
          + "äöñüà"
      );

      public static SegmentResult CalculateSegments(string text)
      {
          bool isGsm7 = text.All(c => Gsm7Basic.Contains(c) || Gsm7Extended.Contains(c));

          if (isGsm7)
          {
              int charCount = text.Sum(c => Gsm7Extended.Contains(c) ? 2 : 1);
              int segments = charCount <= 160 ? 1 : (int)Math.Ceiling(charCount / 153.0);
              return new SegmentResult("GSM-7", charCount, segments);
          }
          else
          {
              int charCount = 0;
              for (int i = 0; i < text.Length; i++)
              {
                  charCount += char.IsHighSurrogate(text[i]) ? 2 : 1;
                  if (char.IsHighSurrogate(text[i])) i++; // skip low surrogate
              }
              int segments = charCount <= 70 ? 1 : (int)Math.Ceiling(charCount / 67.0);
              return new SegmentResult("UTF-16", charCount, segments);
          }
      }
  }

  // Usage:
  // var result = SmsEncoding.CalculateSegments("Hello, world!");
  // Console.WriteLine($"{result.Encoding}, {result.Segments} segment(s)");
  ```

  ```php
  <?php

  function calculateSegments(string $text): array
  {
      $gsm7Extended = str_split('^{}\\[~]|€');
      $gsm7Basic = str_split(
          "@£\$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ ÆæßÉ"
          . " !\"#¤%&'()*+,-./0123456789:;<=>?"
          . "¡ABCDEFGHIJKLMNOPQRSTUVWXYZ"
          . "ÄÖÑܧ¿abcdefghijklmnopqrstuvwxyz"
          . "äöñüà"
      );
      $basicSet = array_flip($gsm7Basic);
      $extSet = array_flip($gsm7Extended);

      $chars = mb_str_split($text);
      $isGsm7 = true;
      foreach ($chars as $c) {
          if (!isset($basicSet[$c]) && !isset($extSet[$c])) {
              $isGsm7 = false;
              break;
          }
      }

      if ($isGsm7) {
          $charCount = array_sum(array_map(
              fn($c) => isset($extSet[$c]) ? 2 : 1, $chars
          ));
          $segments = $charCount <= 160 ? 1 : (int) ceil($charCount / 153);
          return ['encoding' => 'GSM-7', 'char_count' => $charCount, 'segments' => $segments];
      }

      $charCount = 0;
      foreach ($chars as $c) {
          $charCount += mb_ord($c) > 0xFFFF ? 2 : 1;
      }
      $segments = $charCount <= 70 ? 1 : (int) ceil($charCount / 67);
      return ['encoding' => 'UTF-16', 'char_count' => $charCount, 'segments' => $segments];
  }

  // Usage
  $result = calculateSegments("Hello, world!");
  echo "{$result['encoding']}, {$result['segments']} segment(s)\n";
  // GSM-7, 1 segment(s)
  ```

***

## Common encoding issues

**Message unexpectedly uses UTF-16 (too many segments)**

    **Symptom:** Your message uses more segments than expected.

    **Cause:** A non-GSM-7 character is present, forcing the entire message to UTF-16. Common culprits:

    | Character                   | Source                            | GSM-7?                      |
    | --------------------------- | --------------------------------- | --------------------------- |
    | `"` `"` (curly quotes)      | Word processors, mobile keyboards | ❌                           |
    | `'` `'` (curly apostrophes) | Auto-correct, CMS platforms       | ❌                           |
    | `—` (em dash)               | Word processors                   | ❌                           |
    | `…` (ellipsis)              | Mobile keyboards                  | ❌                           |
    | `€` (euro sign)             | Manual entry                      | ✅ (extended, costs 2 chars) |

    **Fix:**

    1. Enable [smart encoding](smart-encoding.md) to auto-replace these characters
    2. Or manually replace them with GSM-7 equivalents before sending

---

**Emojis dramatically increase segment count**

    **Symptom:** Adding a single emoji doubles or triples the number of segments.

    **Cause:** Emojis force UTF-16 encoding (70 chars/segment instead of 160). Additionally, most emojis use **surrogate pairs** and count as 2 UTF-16 characters.

    **Example:**

    ```
    "Thanks for your order!"        → GSM-7, 1 segment (22 chars)
    "Thanks for your order! 🎉"     → UTF-16, 1 segment (25 chars)
    "Thanks for your order! ... 🎉" → UTF-16, 2 segments (71+ chars)
    ```

    **Fix:** If cost is a concern, avoid emojis in SMS. Use emojis freely in MMS/RCS where encoding isn't a factor.

---

**Extended GSM-7 characters cause unexpected segment splits**

    **Symptom:** A 155-character message that looks like it should fit in one segment actually requires two.

    **Cause:** Characters like `[`, `]`, `{`, `}`, `|`, `\`, `^`, `~`, and `€` are in the GSM-7 extended set and count as **2 characters** each.

    **Example:**

    ```
    "Price: $100 [USD]" → 18 visible chars but 20 GSM-7 chars ([ and ] each cost 2)
    ```

    **Fix:** Account for extended characters when calculating message length. Use the segment calculator above or the SDK helpers in this guide.

---

**Copy-pasted text from Word/Google Docs causes issues**

    **Symptom:** Text that looks like normal ASCII actually contains Unicode characters.

    **Cause:** Word processors often replace straight quotes with curly quotes, hyphens with em dashes, and three periods with an ellipsis character. These are invisible differences that force UTF-16.

    **Fix:**

    1. Enable [smart encoding](smart-encoding.md) — this handles the most common substitutions automatically
    2. Sanitize text before sending by replacing known problem characters
    3. Use the `encoding` parameter set to `gsm7` to get a `400` error if non-GSM-7 characters are present (fail-fast approach)

---

**Messages truncated or split incorrectly on recipient's phone**

    **Symptom:** The recipient sees a message split in unexpected places, or parts arrive out of order.

    **Cause:** Multi-part messages are reassembled by the recipient's device using the UDH (User Data Header). Some older devices or carriers may not support reassembly for messages over a certain number of segments.

    **Fix:**

    * Keep messages under 3-4 segments for maximum compatibility
    * Telnyx supports up to 10 segments, but recipient device support varies
    * Consider using MMS for longer content

---

**Non-Latin scripts (Chinese, Arabic, Cyrillic) use too many segments**

    **Symptom:** Messages in non-Latin scripts use significantly more segments than English messages of similar visible length.

    **Cause:** Non-Latin characters have no GSM-7 equivalents, so the entire message uses UTF-16 encoding (70 characters per segment). Smart encoding cannot help here.

    **Fix:**

    * This is expected behavior — plan for higher segment counts when messaging in non-Latin scripts
    * Keep messages concise
    * Consider MMS for longer non-Latin content

---

***

## Best practices

1. **Enable smart encoding**

    Turn on [smart encoding](smart-encoding.md) on your messaging profile to automatically handle Unicode-to-GSM-7 substitutions. This is the single biggest cost-saving measure.

2. **Validate before sending**

    Use the encoding detection helpers above to check segment counts before sending. Alert your application when messages will be unexpectedly expensive.

3. **Sanitize input text**

    If you accept user-generated content, sanitize it before sending. Strip or replace invisible Unicode characters, curly quotes, and other common problem characters.

4. **Keep messages concise**

    Stay under 160 characters (GSM-7) or 70 characters (UTF-16) to avoid multi-part message overhead. Each additional segment adds 7 characters of UDH overhead.

5. **Use the right channel**

    For messages that need emojis, rich formatting, or non-Latin scripts, consider [MMS](https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index) or [RCS](send-rcs-messages.md) instead of SMS.

***

## Related resources

  - [Smart Encoding](smart-encoding.md) — Automatically replace Unicode characters with GSM-7 equivalents to reduce costs.

  - [Send Your First Message](send-your-first-message.md) — Get started with the Telnyx Messaging API.

  - [Messages API Reference](https://developers.telnyx.com/api-reference/messages/send-a-message) — API reference for sending messages with encoding options.

  - [Messaging Profiles](https://developers.telnyx.com/api-reference/messaging-profiles/update-a-messaging-profile) — Configure smart encoding and other profile settings.


## Related Pages

- [Smart Encoding](../runbooks/smart-encoding.md)
- [Message Detail Records](../runbooks/message-detail-records.md)
