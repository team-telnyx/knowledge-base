---
source_url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
title: "Toll-Free Opt-Out Words"
description: "Insights on Telnyx's opt-out process for toll-free numbers and the keywords involved. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: e938a054c25fede1e7d32bdb13b2a2d7df8d212a198955669db3148afc22a269
---







# Toll-Free Opt-Out Words

Insights on Telnyx's opt-out process for toll-free numbers and the keywords involved. See Telnyx guidance and requirements.




## **How do opt-out/opt-in keywords work with toll free numbers?**

If you've read our [previous article](https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words) on SMS opt-out keywords and stop rules, you'll know that Telnyx will block or allow communications to numbers that have sent stop or start keywords. We deal with handling opt-outs and opt-ins a little differently when it comes to toll free numbers.

**The only keyword recognized for opting out of communications with a Telnyx toll free number is "stop". The only keywords recognized for opting into communications with a Telnyx toll free number are still "start" and "unstop".**

When someone opts out of communications with a Telnyx toll free number, we'll send the following auto response:
​
"NETWORK MSG: You replied with the word "stop" which blocks all texts sent from this number. Text back "unstop" to receive messages again."

When someone opts in to communications with a Telnyx toll free number, we'll send this auto response:

"NETWORK MSG: You have replied "unstop" and will begin receiving messages again from this number."

Opting out and in otherwise works the same as opting out and in to communications with our 10 digit long code numbers. On opt-out, we'll block further communications from the toll free number to the opted out number, and on opt-in we'll allow those messaging again.

One last thing to note is you may have seen that it is possible to allow for custom block rules and auto responses on a per messaging profile. Unfortunately, because the logic of opt-outs and auto responses for toll free numbers are handled outside of Telnyx, it is not possible to change the opt-out or opt-in keywords and it is also not possible to change the content of the auto responses specifically for toll free numbers. If custom block rules and auto responses have already been set for one of your messaging profiles, it's advised to separate your toll free numbers from that profile so that you don't experience unintended behavior.

![Breaking Line](_images/682991ade0be9812.png)
