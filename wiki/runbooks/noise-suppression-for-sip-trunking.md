---
title: Noise suppression for SIP Trunking
summary: Noise suppression enhances call quality by removing background noise from audio streams.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
    content_hash: ff1bd7c1f12fe40e23033aadf16215889f5054557fbf5fba49b00132cf9a0c58
updated_at: 2026-04-10T00:00:00Z
---

# Noise suppression for SIP Trunking

Noise suppression enhances call quality by removing background noise from audio streams. Configure this feature at the connection level or individual phone number level to reduce unwanted ambient sounds during calls.

## Configuration scope

Noise suppression can be configured at two levels:

* **Connection level**: Applied to all phone numbers associated with the SIP connection. This setting overrides individual number configurations.
* **Number level**: Applied to specific phone numbers for granular control.

<Callout type="info">
  Connection-level settings take precedence over number-level configurations, simplifying management and ensuring consistent audio quality across all calls.

## Configuration via API

### Configure at connection level

[PATCH /v2/ip\_connections/](https://developers.telnyx.com/api-reference/ip-connections/update-an-ip-connection) with the `noise_suppression` object:

```json theme={null}
{
  "noise_suppression": {
    "direction": "both"
  }
}
```

### Configure at number level

[PATCH /v2/phone\_numbers//voice](https://developers.telnyx.com/api-reference/phone-number-configurations/update-a-phone-number-with-voice-settings) with the `noise_suppression` object:

```json theme={null}
{
  "noise_suppression": {
    "direction": "inbound"
  }
}
```

## Direction options

The `direction` parameter controls which audio streams are processed:

| Value      | Description                                  | Use case                                                       |
| ---------- | -------------------------------------------- | -------------------------------------------------------------- |
| `inbound`  | Processes audio from the PSTN to your system | Clean up audio received by your users or applications          |
| `outbound` | Processes audio from your system to the PSTN | Reduce background noise from your users or applications        |
| `both`     | Processes audio in both directions           | Maximum call clarity when both sides may have background noise |
| `disabled` | Turns off noise suppression                  | Preserve natural ambient sounds when needed                    |

## Codec compatibility

Noise suppression works with standard SIP trunking codecs including:

* G.711 (μ-law and A-law)
* G.722
* Opus

## Performance considerations

* Each direction (inbound/outbound) is processed and billed independently
* Processing adds minimal latency (typically \< 20ms)
* Noise suppression is applied in real-time during the call
* Connection-level configuration provides consistent behavior across all numbers

## Best practices

1. **Use connection-level configuration** for consistent audio quality across all phone numbers
2. **Enable bidirectional suppression** (`both`) for optimal results in noisy environments
3. **Test with your specific use case** to balance noise reduction with audio naturalness
4. **Monitor call quality metrics** to validate the impact on your application


## Related Pages

- [Noise Suppression](../runbooks/noise-suppression.md)
- [Adaptive jitter buffer for SIP Trunking](../runbooks/adaptive-jitter-buffer-for-sip-trunking.md)
