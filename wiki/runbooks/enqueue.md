---
title: Enqueue
summary: The `` verb enqueues the current call in a call queue.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue/index
    content_hash: 118dd16923cd9a6613a506ae8618ef029ca8a73655ca579b1acccb702df5a465
updated_at: 2026-04-10T00:00:00Z
---

# Enqueue

The `` verb enqueues the current call in a call queue.

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
      <td><code>action</code></td>
      <td> Defines an absolute or relative URL used to send a request when the call leaves the queue. It will be sent right away when the call is dequeued using <code>``</code> verb. When a call is dequeued using <code>``</code> verb, the request will be sent once the bridged calls disconnect. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>method</code></td>
      <td> HTTP request type used for <code>action</code>. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>waitUrl</code></td>
      <td> Specifies the URL to the TeXML document that will be executed when the call is waiting in the queue. Once all the commands from the flow are executed, the waitUrl is re-requested, and the TeXML document is run once again. Verbs that are supported in the waitUrl TeXML document: <code>``</code>, <code>``</code>, <code>``</code>, <code>``</code>, <code>``</code>, <code>``</code>, <code>``</code>. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>waitUrlMethod</code></td>
      <td> HTTP request type used for <code>waitUrl</code>. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>maxWaitTimeSecs</code></td>
      <td> Maximum time in seconds a call can stay in the queue. If the call is not dequeued within this time, it will be removed from the queue and the action URL will be called. Must be at least 1 second. </td>

      <td />

      <td><code>14400</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

```

## Expected callbacks

If `waitUrl` is set, a callback is sent when the call enters the queue. See [Queue Callback](https://developers.telnyx.com/api-reference/callbacks/texml-queue) for the full payload reference.
