---
title: Conference participants
summary: Manage participants in TeXML conference calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/texml/rest-api/conference-participants/index
    content_hash: 6f38508f9b08a8082a61ce48b08261c0d7ded15da71fd228c4efe332df8fe98f
updated_at: 2026-04-10T00:00:00Z
---

# Conference participants

Manage participants in TeXML conference calls.

A conference participant object represents an individual call leg that has been added to a conference.

## Creating a conference participant

A conference participant is instantiated in the following situations:

1\. When a new participant is dialed and added to a conference via the REST API

API reference: [dial-a-new-conference-participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant).

When your application requests to dial a new party into an existing conference using the REST API, a conference participant resource for the new call leg is created.

2\. When a call leg is added to a conference via `` with `` in TeXML

Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference)

When a TeXML `` verb that contains a `` element is executed, the call leg joins the specified conference. At that point, Telnyx creates a conference participant object associated with that call leg.

## When Participant API Responses Return No Results

Certain situations cause the participant API to return no participant records, even if the call or conference previously existed. Telnyx will return no participant objects under the following conditions:

1\. The conference has been completed

Once a conference ends (e.g., all participants disconnect or the session is terminated), Telnyx no longer returns participant objects associated with that completed conference.

2\. A participant’s call leg is no longer active (i.e., has been hung up)

If a participant disconnects - whether intentionally, due to call failure, or because of application logic - their call leg is considered complete, and the participant object is no longer returned by the API.

3\. The participant has been explicitly removed via the REST API

API reference: [delete-a-conference-participant](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-conference-participant)

4\. The participant’s call leg has been given new TeXML instructions via the REST API

API reference: [update-call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-call)

If a call leg that was previously in a conference is updated with new TeXML instructions via the REST API, it effectively leaves the conference context. As a result, it is no longer included in participant API responses.


## Related Pages

- [Conference](../runbooks/conference.md)
