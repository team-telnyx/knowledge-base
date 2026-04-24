---
title: Stream
summary: The `` instruction starts streaming the media from a call to a specific WebSocket address in near-real-time.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream/index
    content_hash: 2c96a46f0ae4034b26f4cd17b8dadf3771f14259893260ff2ee514c824e60821
updated_at: 2026-04-10T00:00:00Z
---

# Stream

The `` instruction starts streaming the media from a call to a specific WebSocket address in near-real-time. Audio will be delivered as base64-encoded RTP payloads (no headers), wrapped in JSON payloads.

## Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>url</code></td>
      <td> The destination WebSocket address where the stream is going to be delivered. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>track</code></td>
      <td> Specifies which track should be streamed. </td>
      <td><code>inbound\_track</code>, <code>outbound\_track</code>, <code>both\_tracks</code></td>
      <td><code>inbound\_track</code></td>
    </tr>

    <tr>
      <td><code>name</code></td>
      <td> Specifies custom name for the stream instance </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>codec</code></td>
      <td> Specifies the codec to be used for the streamed audio. When set to 'default' or when transcoding is not possible, the codec from the call will be used. Currently, transcoding is only supported between PCMU and PCMA codecs. </td>
      <td><code>PCMU</code>, <code>PCMA</code>, <code>G722</code>, <code>OPUS</code>, <code>AMR-WB</code>, <code>default</code></td>
      <td><code>default</code></td>
    </tr>

    <tr>
      <td><code>bidirectionalMode</code></td>
      <td> Bidirectional streaming mode </td>
      <td><code>mp3</code>, <code>rtp</code></td>
      <td><code>mp3</code></td>
    </tr>

    <tr>
      <td><code>bidirectionalCodec</code></td>
      <td> Bidirectional streaming codec, used only with <code>bidirectionalMode=rtp</code> </td>
      <td><code>PCMU</code>, <code>PCMA</code>, <code>G722</code>, <code>OPUS</code>, <code>AMR-WB</code></td>
      <td><code>PCMU</code></td>
    </tr>

    <tr>
      <td><code>bidirectionalSamplingRate</code></td>
      <td> Bidirectional streaming sampling rate in Hz </td>
      <td><code>8000</code>, <code>16000</code>, <code>24000</code></td>
      <td><code>8000</code></td>
    </tr>

    <tr>
      <td><code>statusCallback</code></td>
      <td> A URL for Telnyx to send webhook requests to on stream status events (e.g. stream started, stopped, or failed). </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>statusCallbackMethod</code></td>
      <td> HTTP request type used for statusCallback. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>enableReconnect</code></td>
      <td> Whether the platform should automatically attempt to reconnect the WebSocket stream if disconnected. Defaults to `true`. </td>

      <td />

      <td><code>true</code></td>
    </tr>
  </tbody>
</table>

## Child verbs/nouns

<table>
  <thead>
    <tr>
      <th>NOUN/VERB</th>
      <th>DESCRIPTION</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>Parameter</code></td>
      <td> Custom key-value parameter to pass to the WebSocket server. Parameters are included in the `start` message sent over the WebSocket connection. </td>
    </tr>
  </tbody>
</table>

## Parameter Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>name</code></td>
      <td> The name of the custom parameter. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>value</code></td>
      <td> The value of the custom parameter. </td>

      <td />

      <td>-</td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Stream url="wss://yourdomain.com/stream" track="both_tracks" />

```

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Stream url="wss://yourdomain.com/stream" statusCallback="https://example.com/stream-events">
      <Parameter name="customer_id" value="12345" />
      <Parameter name="call_type" value="support" />

```

### Disabling automatic reconnection

By default, `enableReconnect` is `"true"`, and the platform will automatically attempt to reconnect the WebSocket stream if it is disconnected. Set `enableReconnect="false"` to disable this behavior, for example when a disconnection should immediately end the stream.

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Stream url="wss://yourdomain.com/stream" enableReconnect="false" />

```

## Expected callbacks

If `statusCallback` is set, stream status callbacks are sent for the following events:

* `stream-started` — Stream has started
* `stream-stopped` — Stream has stopped
* `stream-failed` — Stream failed to start or was interrupted

See [Stream Callback](https://developers.telnyx.com/api-reference/callbacks/texml-stream) for the full payload reference.
