---
source_url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
title: "Limits on Concurrent Outbound Calls"
description: "Did you reach your limit for active concurrent outbound calls? See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 8317428c52a672cb918e6477183c4f2b0a7993e4d63fcc677f6801ff41381197
---







# Limits on Concurrent Outbound Calls

Did you reach your limit for active concurrent outbound calls? See Telnyx guidance and requirements.




## How many concurrent outbound calls or channels can be active at once?

When you have signed up to Telnyx's Mission Control Portal, by default you are set to a global value of 2 concurrent outbound calls. Upon approval for Level 2 verification, this will increase to 10 concurrent calls. We are happy to accommodate more based on your requirements, if you have been Level 2 verified you can reach out to us at [support@telnyx.com](mailto:support@telnyx.com) to increase your limit It is recommend to provide information on your use case should you wish to increase the channels beyond 100.

## How will I know when the concurrent outbound call channel limit has been reached?

You will know when you have reached this limit as Telnyx returns the SIP error response: **D1 -** ***403 User channel limit exceeded D1***

The number of concurrent **outbound** calls for the account is over the limit. This relates to the global account concurrent call limit set in your [outbound voice profile](https://portal.telnyx.com/#/app/outbound-profiles) section.

You can find more information on all of our SIP responses [here](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes#h_a272894b39).
