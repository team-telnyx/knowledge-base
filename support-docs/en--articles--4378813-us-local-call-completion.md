---
source_url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
title: "US Local Call Completion"
description: "This article describes local call completion issues and why it occurs. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: ae051f44e063122227d167a82852d5f8fe0b518792787c28b3ccbaa97b23a010
---







# US Local Call Completion

This article describes local call completion issues and why it occurs. See Telnyx guidance and requirements.




## **US Local Calling Experience**

![Breaking Line](_images/682991ade0be9812.png)

After purchasing or porting a local number for a client in a particular rate center across the US? Did your client reach out to you mentioning that other local callers within the same rate center or state receive intercept recordings, when dialing your clients number, such as "The number you have dialed cannot be completed at this time, please check the number and try again"?.

Much like [US Rural Call Completion](https://support.telnyx.com/en/articles/4096828-us-rural-call-completion), local distance calls across the United States, and especially to [VoIP numbers](https://telnyx.com/resources/voip-number) can be a frustrating experience, whether you are the caller or the callee. These issues are often the byproduct of how local carriers choose to route calls and it's usually due to following the least cost routing model, which can lead to this poor experience but there are many factors involved that can impact local calling failures. We aim to describe that process below and how Telnyx ensure's our numbers are flexible and reliable.

## **US Local Calling Components**

![Breaking Line](_images/682991ade0be9812.png)

Firstly, we must understand what a typical call flow entails and how carriers know where to route calls that their subscribers dial. Typically, in a local calling scenario, you have the following:
​
Originating Carrier -> Downstream Tandem -> LEC -> Upstream Tandem -> Destination Carrier.

* **Originating Carrier:** The carrier of the calling party.
* **Downstream Tandem**: The interconnect the originating carrier has in order to access the PSTN over TDM.
* **LEC**: The local exchange carrier (can be ILEC or CLEC) that owns the local telecoms equipment on the PSTN and has interconnections with the many different tandems providers.
* **Upstream Tandem**: The interconnect Telnyx has, in order to access the PSTN and receive calls over IP.
* **Destination Carrier**: The carrier of the receiving party, in this case Telnyx.

## **Terms for Local US Calls**

![Breaking Line](_images/682991ade0be9812.png)

Call routing works using ***LERG, LATA, LRN, LNP, NPA & Rate Center*** information.

* **LERG**: Local Exchange Routing Guide. A database managed by NPAC Iconectiv which provides information regarding owned NPA-NXX at the block level. The LERG is updated monthly and highlights the call routing activity that occurs over the PSTN (Public Switched Telephone Network) by service providers.
* **LATA**: Local Access Transport Area. This is the geographic area in which numbers are routed. Typically, LATA's do not cross states but states can have multiple LATA's.
* **LRN**: Location Routing Number. It's a unique identification phone number which tells the industry how to route calls through the PSTN. Each carrier has at least one LRN per LATA. They were created to provide local number portability by allowing numbers to route successfully when moving carriers. The only requirement is that the LRN changes.
* **LNP**: Local Number Portability. The ability to retain your local phone if you switch to another carrier.
* **NPA:** Number Planning Area. Calls to ported or pooled numbers are routed based on the NPA-NXX of the number’s associated LRN. The NPA is a 3 digit number that identifies the area code of the region. A single NPA can be available in more than one rate center.
  ​
* **Rate Center**: A rate center is a geographical area used to determine the boundaries for local calling, billing, and assigning specific phone numbers, which can encompass multiple area codes.
  ​

## **Relationship Between Components & Terms**

![Breaking Line](_images/682991ade0be9812.png)

Carriers are typically assigned thousand block NPA-NXX's they can then provide to their subscribers. When Telnyx loads numbers that our customers can purchase, our numbering team ensure that each NPA-NXX number is assigned a particular LRN.
​
This LRN is broadcasted to the industry via NPAC Iconetiv who administer the routing of phone calls. Telnyx also provides the NPA-NXX blocks and LRN information to our upstream tandems, so they can load the information into their switches and know how to route calls when they receive calls from the LEC at the PSTN.
​
The problem that we see from time to time is that our customers mention that their clients were unable to reach them. From our experience Call completion issues are likely caused by a translations issue. Translation issues typically occur after porting out or at the tandem switches.

* **Porting Out** - The originating (losing) carrier has not removed old routing information from their network, resulting in their subscribers calls never reaching the new destinations network. We typically see delays with legacy telco providers, where it can take at least one hour, post port out, for them to update their routing information across their network.
* **Tandem Switches** - Where either the downstream or upstream tandem provider hasn't mapped our LRN's NPA-NXX correctly to us.

For the above two reasons, usually local call failures occur only when we launch numbers in new markets or spin up new number blocks and typically, this occurs for most carriers as-well because not every carrier has the most up to date routing information yet.

## **Solution for Local US Calling**

![Breaking Line](_images/682991ade0be9812.png)

At Telnyx, we're looking to connect people globally, no matter where they reside. The good news is that we have a lot of "seasoned" LRN's, which increases the likelihood of connectivity because carriers are familiar with the routing information. Not only that but we have redundant coverage in most LATAs (and soon to be all LATAs) and can update our LRN's between tandems in-case of issues with our tandem providers.

The problem becomes more difficult when it's not an issue with our tandem providers, where they have verified the calls never reached their network from the PSTN. This means it could have been an intermittent issue, at the time of the call, either at the LEC or an actual issue at the downstream tandem or simply with the originating carrier.

Often attempts to reach out to the originating carriers, whether it be directly or with the assistance of our tandem providers, yield CPNI compliance restrictions and "Please have our subscriber reach out to our support to log a fault".
​
We're all about connectivity and we are willing to continue to troubleshoot local issues your client's callers may be having.

## **How to Report Local US Calling Issues**

![Breaking Line](_images/682991ade0be9812.png)

Should you have any call local call completion concerns, please contact our support team by email [support@telnyx.com](mailto:support@telnyx.com) or by phone [+1.888.980.9750](tel:+18889809750)

In your email, providing the following details will help our team in understanding the issue and working towards a solution. Ideally, call examples are within 48 hours of occurrence and reproducible.

* A description of the issue or concern.
* From and To telephone numbers.
* Date and time (including timezone) of the call during which the issues were experienced.
* Any Error messages the callers heard that may indicate switching errors.

---

Related Articles

[US Rural Call Completion](https://support.telnyx.com/en/articles/4096828-us-rural-call-completion)[SIP Connection: Fail-over and Retries](https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries)[The Rate Sheet and LRN explained](https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained)[CLI & CLD Validation FAQ](https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq)[PSTN Replacement / Local Calling with Telnyx](https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx)

Did this answer your question?

😞😐😃
