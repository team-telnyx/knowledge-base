---
title: Command Retries
summary: Telnyx's Programmable Voice Resources page explain in detail how to configure your command retries for voice applications.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries/index
    content_hash: 4f60402b0c0990bccd89b7f6a0913ac6e93d45d7493b39b4270c1e78c29ed949
updated_at: 2026-04-10T00:00:00Z
---

# Command Retries

Telnyx's Programmable Voice Resources page explain in detail how to configure your command retries for voice applications.

User Applications may encounter the following situations:

* 5XX Error: Telnyx actively monitors and alerts on the rate of 500, 501, 503, or 504 errors.
* Duplicate Webhooks: Identical webhooks may occasionally be delivered.

## How to use command retries for better reliability

Telnyx carefully monitors the Voice API platform for 5XX errors, latency, and duplicate webhooks, and actively works to keep all of these to a minimum.

For added reliability, there are several steps developers can take to handle 5XX errors, latency, and duplicate webhooks, and automatically retry commands when such issues are encountered:

* `command_id`: send a unique `command_id` parameter as part of your commands. The `command_id` must be unique for each command. We suggest using UUIDv4.
* Retry on 5XX Errors: If your application receives a 500 error, immediately retry the command.
* Retry on Latency >500ms: If your application fails to receive a HTTP response from Telnyx within 500ms, send an identical command.


## Related Pages

- [Command Reference](../reference/command-reference.md)
- [Failover and Retries](../runbooks/failover-and-retries.md)
- [Legacy Command Reference](../reference/legacy-command-reference.md)
