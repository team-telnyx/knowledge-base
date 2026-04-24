---
title: Queues
summary: Create and manage TeXML queues to handle waiting callers.
sources:
  - url: https://developers.telnyx.com/docs/voice/texml/rest-api/queues/index
    content_hash: 31ee589900175db08be83fdd83994c3ee4ce5a618c55eddaee62f2401e14651b
updated_at: 2026-04-10T00:00:00Z
---

# Queues

Create and manage TeXML queues to handle waiting callers.

A queue object represents a holding area for calls.

Calls in a queue are ordered by the time they were enqueued (First-In-First-Out).

## Creating queues

There are two ways to instantiate a new queue:

1\. Using the REST API

A queue can be explicitly created by sending a request to the [Create New Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/create-a-new-queue) endpoint.

2\. Using the `` Verb

A queue can also be created dynamically during call flow execution. When an [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue) verb is executed inside a TeXML script with a specific queue name, Telnyx checks if a queue with that name already exists.

If the queue exists, the call is added to it. If it does not exist, a new queue is automatically created with default settings, and the call is then added.

## Managing queues

Once a queue is instantiated, it can be managed using the TeXML REST API.

* **[Fetch a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-queue-resource)**

Get detailed information about a specific queue by its Queue SID or name. This returns the current state, including the number of calls currently waiting (current size), the average wait time, and the maximum size configuration.

* **[Update a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-queue-resource)**

Modify the properties of an existing queue. For example, you can change the maximum number of allowed calls (max size) to prevent overloading the system.

* **[Delete a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-queue-resource)**

Remove a queue from your account.
