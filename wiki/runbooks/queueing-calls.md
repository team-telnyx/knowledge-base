---
title: Queueing Calls
summary: how to use the Telnyx Call Queue API to create and manage call queues using Telnyx Voice API.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/queueing-calls/index
    content_hash: 8012903846c3baac3ae38a97189ce313adf5fcd6291e224db7d98db19eed64c4
updated_at: 2026-04-10T00:00:00Z
---

# Queueing Calls

how to use the Telnyx Call Queue API to create and manage call queues using Telnyx Voice API

\| [cURL](#curl) | [Python](#python) |

***

## cURL

In this tutorial you'll learn how to use the Telnyx Call Queue API to create and manage call queues with just a few API requests.

Call Queueing is fully integrated with the Telnyx Voice API, previously called Call Control. This tutorial assumes you've already [set up your developer account and environment](/development) and you know how to [send commands](sending-commands-for-programmable-voice.md) and [receive webhooks](receiving-webhooks-for-programmable-voice.md) using the Telnyx Voice API.

### Adding a call to a new or existing queue

A call can be placed into a queue using the [`enqueue` command](https://developers.telnyx.com/api-reference/call-commands/enqueue-call). Use the `queue_name` parameter to specify a queue into which the call should be placed.

* If the `queue_name` refers to a queue that already exists, the call will be placed at the **end** of the queue.
* If the `queue_name` hasn't been used before, a new queue with this name will be created and the call will be placed into it.

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```bash theme={null}
curl -X POST
  --header "Content-Type: application/json"
  --header "Accept: application/json"
  --header "Authorization: Bearer YOUR_API_KEY"
  --data '{"queue_name": "support"}'
  https://api.telnyx.com/v2/calls//actions/enqueue
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

> If the call for which the `enqueue` command was issued is bridged to another call leg (i.e. it is in an active conversation with someone) the call will be unbridged.

### Bridging an existing call to a queue

The [`bridge` command](https://developers.telnyx.com/api-reference/call-commands/bridge-calls) can be used to bridge a call to another call waiting in a queue. The queue's `queue_name` should be used as the bridge command's `queue` parameter.

For example, a customer support agent can be bridged to the first call from a queue of waiting customer calls. If the customer support agent's active call has a call\_control\_id `8899ad4a-de6f-11eb-a54c-02420a0d4168` and the support call queue has a name `support`, the command to bridge the call is as follows:

```bash theme={null}
curl -X POST
  --header "Content-Type: application/json"
  --header "Accept: application/json"
  --header "Authorization: Bearer YOUR_API_KEY"
  --data '{"queue": "support"}'
  https://api.telnyx.com/v2/calls/8899ad4a-de6f-11eb-a54c-02420a0d4168/actions/bridge
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

> When a `bridge` command is issued, the call at the top of the specified queue will be dequeued and a bridge will be attempted.

### Dequeuing calls

Calls can be removed from queues in four ways:

1. Ending the call by any means (e.g. a [`hangup` command](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index#hangup), or the call being disconnected by calling parties).
2. Issuing any command that results in the call being bridged elsewhere (e.g. [`bridge`](https://developers.telnyx.com/api-reference/call-commands/bridge-calls), [`transfer`](https://developers.telnyx.com/api-reference/call-commands/transfer-call), [conference `join`](https://developers.telnyx.com/api-reference/conference-commands/join-a-conference), [`refer`](https://developers.telnyx.com/api-reference/call-commands/sip-refer-a-call)).
3. A call is automatically removed from queues if the `max_wait_time_secs` parameter was used when adding the call to a queue and the specified maximum waiting time has elapsed. The automatically dequeued call will remain in a parked state and await further call commands.
4. Sending the [`leave_queue` command](https://developers.telnyx.com/api-reference/call-commands/remove-call-from-a-queue) with a call's `call_control_id` will remove that call from any queue it is in, leaving it parked awaiting further call commands.

```bash theme={null}
curl -X POST
  --header "Content-Type: application/json"
  --header "Accept: application/json"
  --header "Authorization: Bearer "
  https://api.telnyx.com/v2/calls//actions/leave_queue
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### Inspecting queue state

There are a number of endpoints that let you inspect your queues and enqueued calls:

* [Retrieve a queue](https://developers.telnyx.com/api-reference/queue-commands/retrieve-a-call-from-a-queue#retrieve-a-call-from-a-queue)
* [Retrieve a call from a queue](https://developers.telnyx.com/api-reference/queue-commands/retrieve-a-call-from-a-queue#retrieve-a-call-from-a-queue)
* [List calls in a queue](https://developers.telnyx.com/api-reference/queue-commands/retrieve-calls-from-a-queue#retrieve-calls-from-a-queue)

Empty queues will automatically be garbage collected after a period of inactivity.

### Receiving webhooks for call queueing events

The Telnyx API will send you a webhook for every major queue event, i.e.

* when a call is put in a queue,
* when a call leaves the queue for some reason.

Webhooks contain information about the call and the queue with which it is associated. Example webhooks are shown in the API reference for the [`enqueue` command](https://developers.telnyx.com/api-reference/call-commands/enqueue-call).

### Next steps

Now that you've set up simple call queueing functionality with the Telnyx Voice API, why not use call queueing to [build a contact center](call-center-demo.md)?

If you're interested in building something more complex or large-scale, our experts are standing by to help. <a href="https://telnyx.com/contact-us">Contact our team</a> today.

## Python

In this guide you'll learn how to use the Telnyx Call Queue API to create and manage call queues with just a few API requests.

Call Queueing is fully integrated with the Telnyx Voice API, the Telnyx Voice API. This guide assumes you've already [set up your developer account and environment](/development) and you know how to [send commands](sending-commands-for-programmable-voice.md) and [receive webhooks](receiving-webhooks-for-programmable-voice.md) using the Telnyx Voice API.

### Adding a call to a new or existing queue

A call can be placed into a queue using the [`enqueue` command](https://developers.telnyx.com/api-reference/call-commands/enqueue-call). Use the `queue_name` parameter to specify a queue into which the call should be placed.

* If the `queue_name` refers to a queue that already exists, the call will be placed at the **end** of the queue.
* If the `queue_name` hasn't been used before, a new queue with this name will be created and the call will be placed into it.

```python theme={null}
call.enqueue("tier_1_support")
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

> If the call for which the `enqueue` command was issued is bridged to another call leg (i.e. it is in an active conversation with someone) the call will be unbridged.

### Bridging an existing call to a queue

The [`bridge` command](https://developers.telnyx.com/api-reference/call-commands/bridge-calls) can be used to bridge a call to another call waiting in a queue. The queue's `queue_name` should be used as the bridge command's `queue` parameter.

For example, a customer support agent can be bridged to the first call from a queue of waiting customer calls. If the customer support agent's active call has a call\_control\_id `8899ad4a-de6f-11eb-a54c-02420a0d4168` and the support call queue has a name `support`, the command to bridge the call is as follows:

```python theme={null}
call.bridge(call_control_id="bridge_uuid", queue="tier_1_support")
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

> When a `bridge` command is issued, the call at the top of the specified queue will be dequeued and a bridge will be attempted.

### Dequeuing calls

Calls can be removed from queues in four ways:

1. Ending the call by any means (e.g. a [`hangup` command](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index#hangup), or the call being disconnected by calling parties).
2. Issuing any command that results in the call being bridged elsewhere (e.g. [`bridge`](https://developers.telnyx.com/api-reference/call-commands/bridge-calls), [`transfer`](https://developers.telnyx.com/api-reference/call-commands/transfer-call), [conference `join`](https://developers.telnyx.com/api-reference/conference-commands/join-a-conference), [`refer`](https://developers.telnyx.com/api-reference/call-commands/sip-refer-a-call)).
3. A call is automatically removed from queues if the `max_wait_time_secs` parameter was used when adding the call to a queue and the specified maximum waiting time has elapsed. The automatically dequeued call will remain in a parked state and await further call commands.
4. Sending the [`leave_queue` command](https://developers.telnyx.com/api-reference/call-commands/remove-call-from-a-queue) with a call's `call_control_id` will remove that call from any queue it is in, leaving it parked awaiting further call commands.

```python theme={null}
call.leave_queue()
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### Inspecting queue state

There are a number of endpoints that let you inspect your queues and enqueued calls:

* [Retrieve a queue](https://developers.telnyx.com/api-reference/queue-commands/retrieve-a-call-from-a-queue#retrieve-a-call-from-a-queue)
* [Retrieve a call from a queue](https://developers.telnyx.com/api-reference/queue-commands/retrieve-a-call-from-a-queue#retrieve-a-call-from-a-queue)
* [List calls in a queue](https://developers.telnyx.com/api-reference/queue-commands/retrieve-calls-from-a-queue#retrieve-calls-from-a-queue)

Empty queues will automatically be garbage collected after a period of inactivity.

### Receiving webhooks for call queueing events

The Telnyx API will send you a webhook for every major queue event, i.e.

* when a call is put in a queue,
* when a call leaves the queue for some reason.

Webhooks contain information about the call and the queue with which it is associated. Example webhooks are shown in the API reference for the [`enqueue` command](https://developers.telnyx.com/api-reference/call-commands/enqueue-call).

### Next steps

Now that you've set up simple call queueing functionality with the Telnyx Voice API, why not use call queueing to [build a contact center](call-center-demo.md)?

If you're interested in building something more complex or large-scale, our experts are standing by to help. <a href="https://telnyx.com/contact-us">Contact our team</a> today.
