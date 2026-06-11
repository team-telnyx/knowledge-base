---
source_url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
scraped: 2026-06-11
---

What are Short Duration Calls? | Telnyx Help Center

[Skip to main content](#main-content)

# What are Short Duration Calls?

Here we will explain short duration calls and how they may effect your business.

Written by Telnyx Sales

Updated over 3 weeks ago

Table of contents

# What are Short Duration Outbound Calls?

Short Duration Calls (SDCs) are outbound calls that are 6 seconds or less in duration. We allow 15% of your traffic to be SDCs on our platform. If your Short Duration call traffic goes above 15% at any time in the month you'll receive an email alerting you of the situation. If by the end of the month your Short Duration call traffic is still above the 15% of your total traffic you will be penalized for this traffic with [additional charges](https://telnyx.com/terms-and-conditions-of-service).

It's important to note that if your Short Duration call traffic is above 15% or above for the calendar month, the penalty will be applied to ALL Short Duration calls made that month and not only those above the 15% mark.

Short duration calls are calculate based on:

Count of short duration calls connected / Total count of connected calls (which includes the short duration call count). The time-frame will always be based in UTC from 00:00:00.

​**Example:**

* Start Date = 23rd January 2023 00:00:00
* End Date = 30th January 2023 00:00:00
* Short Duration Call Count = 200
* Total Connected Call Count = 1000
* 200 / 1000 = 20% of calls considered short duration.

## Does this apply to International calls?

Yes, as of the 1st of January 2024, short duration calls to international destinations will also be subject to a fee of $0.01 per call where it is determined that you have more than 15% of your total traffic as short duration.

## Does Telnyx support short duration calls?

We do not support use cases that require Short Duration calls through our network.   
​  
If you would like to locate the origin of Short Duration Calls within your traffic, you can:

* Download a detail report for your desired time-frame: <https://portal.telnyx.com/#/reporting/detailed-records> filtering **outbound** calls only.
* Sort the generated CSV file based on the call duration column.
* Remove any rows of calls with a duration of 0 seconds.
* Calculate how many calls were less than or equal to 6 seconds in duration.
* Check the column with the sip connection name to see which one shows up often to determine the source of the short duration traffic.

---

Related Articles

[What is DTMF? and how to configure it on Telnyx](https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx)[Distinguish your outbound profiles & DIDs](https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids)[Audio and Codecs](https://support.telnyx.com/en/articles/3192298-audio-and-codecs)

Did this answer your question?

😞😐😃

Table of contents
