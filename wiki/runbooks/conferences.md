---
title: Conferences
summary: Create and manage TeXML conference calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/texml/rest-api/conferences/index
    content_hash: 8f578dd59ba3d2b56fe2dd7368ffe6d271feb7b0eee0ca3b62626af5ed388e22
updated_at: 2026-04-10T00:00:00Z
---

# Conferences

Create and manage TeXML conference calls.

A conference object represents a multi-participant audio session.

## Creating conference

A conference is instantiated in the following way:

1\. When a `` to a non-existent `` is executed

Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference)

2\. When Telnyx processes a TeXML response that includes a `` verb with a `` noun, it attempts to place the current call into a named conference.

Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial)

## Managing Existing Conferences

Once instantiated, conferences can be managed via REST API endpoints, including:

* [Fetch a conference resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-conference-resource)

* [List all conferences](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-resources)

* [Update a conference](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-conference-resource)

* [List associated recordings](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-recordings)
