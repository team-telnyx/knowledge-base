---
title: Redaction
summary: PII redaction in transcription results.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/redaction
    content_hash: e16d7f6d138adc41f8b0a584866b854b5b5a5531650a31a2b4ac4bbfaa9446d3
updated_at: 2026-04-10T00:00:00Z
---

# Redaction

PII redaction in transcription results.

**Deepgram only.** Other engines ignore this parameter.

Replaces sensitive data in transcripts with placeholder text.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?redact=pci
```

## Values

| Value     | Redacts                 |
| --------- | ----------------------- |
| `pci`     | Credit card numbers     |
| `ssn`     | Social Security numbers |
| `numbers` | All numeric sequences   |

Multiple values can be passed as comma-separated:

```
?redact=pci,ssn
```

## Output

Redacted content is replaced in the transcript text. The exact replacement format depends on the Deepgram model.

```json theme={null}
{"transcript": "My card number is [REDACTED]", "is_final": true}
```

> **Note:** Redaction applies to final and interim results. There is no way to get the un-redacted version once redaction is enabled for a session.
