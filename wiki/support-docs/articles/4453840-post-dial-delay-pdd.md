---
title: "Post Dial Delay (PDD)"
summary: "In this article we will explain post dial delay (PDD) and some of its causes. See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--4453840-post-dial-delay-pdd.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--4453840-post-dial-delay-pdd.md -->

# Post Dial Delay (PDD)

In this article we will explain post dial delay (PDD) and some of its causes. See Telnyx guidance and requirements.




## **What is PDD?**

Post Dial Delay (PDD) is experienced by the originating caller - as the time from the sending of the final dialed digit to the point at which they hear ring tone or other in-band information.

Where the originating network is required to play an announcement before completing the call then this definition of PDD excludes the duration of such announcements.

For SIP the PDD would be the time from Sending the **INVITE** to receiving the first ringing response for example: a **SIP/2.0 180 Ringing** response.

![Breaking Line](_images/682991ade0be9812.png)

## **Why does PDD occur?**

PDD can occur for a number a reasons, the most prevalent reason is because the carrier of the number you are dialing has not received an indication that the end users device is ringing. PDD is widely experienced on wireless devices that have low signal and are far away from their providers closest cell tower - so it takes longer for the connection to be established.

Most carriers within the telecommunications industry consider anything under 7 seconds as an acceptable amount of PDD, and most will not troubleshoot PDD that is less than 7 seconds.
​

At Telnyx, we partner with Tier 1 carriers and interconnects across the world. The better quality routes, the less likely there will be a delay. Our telephony operations team monitor and test our carriers and interconnects to ensure there are no underlying issues with call completion. Should you experience post dial delay over 7 seconds, please contact our support team ([support@telnyx.com](mailto:support@telnyx.com)) who can assist in verifying if there is an underlying issue and work with our internal teams to further optimize our routes and your experience.
