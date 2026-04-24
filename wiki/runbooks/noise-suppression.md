---
title: Noise Suppression
summary: In this tutorial, you'll learn how to enable noise suppression for the Voice API and TeXML calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression/index
    content_hash: 9fb56fa629109fa20ee292ce55d751c0372542daf205ee0df650f6f70fa43516
updated_at: 2026-04-10T00:00:00Z
---

# Noise Suppression

In this tutorial, you'll learn how to enable noise suppression for the Voice API and TeXML calls.

Noise suppression works for both AI-powered calls (like AI Assistants and Gather Using AI) and regular voice calls. While it improves audio quality across all call types by reducing background noise, **the biggest value comes from enhanced AI performance**—cleaner audio leads to more accurate speech recognition and better AI responses. This makes noise suppression especially valuable for AI use cases where audio quality directly impacts user experience.

## Voice API

The noise suppression can be enabled for the Voice API calls in the following way:

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

The only parameter required for the request is `direction` which can have one of the following options: inbound | outbound | both.

Please be aware that the charge is applied for each direction separately.

```bash theme={null}
    curl --request POST \
    --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer YOUR_API_KEY \
    --header 'Content-Type: application/json' \
    --data '{
        "direction": "inbound"
    }'
```

The noise suppression can be stopped at any time in the following way:

```bash theme={null}
    curl --request POST \
    --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_stop \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer YOUR_API_KEY \
    --header 'Content-Type: application/json' \
    --data '{}'
```

## Supported engines

Telnyx supports four noise suppression engines:

* Denoiser (default)
* DeepFilterNet
* Krisp
* AICoustics

The engine can be set using `​noise_suppression_engine` parameter

```bash theme={null}
    curl --request POST \
    --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer YOUR_API_KEY \
    --header 'Content-Type: application/json' \
    --data '{
        "direction": "inbound",
        "noise_suppression_engine": "Krisp" 
    }'
```

## TeXML

In TeXML there is a dedicated verb for enabling the noise suppression on the call.

```xml theme={null}

        <Suppression direction="inbound" noise_suppression_engine="Krisp"/>

...

```


## Related Pages

- [Suppression](../runbooks/suppression.md)
- [Noise suppression for SIP Trunking](../runbooks/noise-suppression-for-sip-trunking.md)
