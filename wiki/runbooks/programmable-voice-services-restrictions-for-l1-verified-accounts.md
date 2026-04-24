---
title: Programmable Voice services restrictions for L1 verified accounts
summary: The accounts with the L1 verification are restricted in the following way.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/l1-accounts-restirctions/index
    content_hash: 141976484287906fa10d09f47b8f759db102573e6c0e8c424c0840047f898d6e
updated_at: 2026-04-10T00:00:00Z
---

# Programmable Voice services restrictions for L1 verified accounts

The accounts with the L1 verification are restricted in the following way:

* All machine-generated speak commands are pre-pended with "This is an automated call generated on the Telnyx platform, please report any abuse to [fraud@telnyx.com](mailto:fraud@telnyx.com)". This currently includes:

  * /v2/calls
  * /v2/calls/:call\_control\_id/actions/transfer
  * /v2/calls/:call\_control\_id/actions/gather\_using\_audio
  * /v2/calls/:call\_control\_id/actions/gather\_using\_speak
  * /v2/calls/:call\_control\_id/actions/playback\_start
  * /v2/calls/:call\_control\_id/actions/speak
  * /v2/calls/:call\_control\_id/actions/gather\_using\_ai
  * /v2/calls/:call\_control\_id/actions/ai\_assistant\_start
  * and the TeXML verbs:
    * Play
    * Say
    * AIGather
* Limited to a maximum of 100 outbound calls a day.
* Limited to 10 outbound calls per hour.
