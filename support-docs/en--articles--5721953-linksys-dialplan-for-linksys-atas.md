---
source_url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
title: "Linksys: Dialplan for Linksys ATAs"
description: "Master the Linksys dialplan digit sequences for ATAs. See Telnyx guidance and requirements Learn more about Linksys: Dialplan for Linksys ATAs with Telnyx."
scraped: 2026-07-08
content_hash: c9efcba2bda6a2dd8c951e38d195432299e5b93c48012ad988a913c3aefa4ac6
---







# Linksys: Dialplan for Linksys ATAs

Master the Linksys dialplan digit sequences for ATAs. See Telnyx guidance and requirements Learn more about Linksys: Dialplan for Linksys ATAs with Telnyx.

C




[Jump to Dialplan](#h_2cb90844ea)

A dial plan (or dialplan) is a string of characters that determines how entered phone digits are are interpreted and transmitted by your ATA device. It also tells the device if it should accept or reject a call. It facilitates calling, as well as blocking of certain call profiles (such as long distance or international).

The basic dial plan provided in the configuration samples for the Linksys ATA devices should work with Telnyx.

---

## How the Telnyx dialplan works with Linksys

## Telnyx recommended dialplan:

Coming soon

## Linksys Dialplan Digit Sequence

|  |  |
| --- | --- |
| **Digit Sequence** | **Function** |
| 0 1 2 3 4 5 6 7 8 9 \* # | Characters available to use that map to a phone digit. |
| x | Any phone digit. |
| [sequence] | You can enter characters between brackets to create an allow-list of only certain digits. ​ For example, if you enter the range [1-5], the user may only press the digits from 1 to 5. ​ You can also use consecutive characters to denote skipping certain numbers.    For example [25-7\*] allows the user to press 2, 5, 6, 7 or \*. *(Note that 4 is missing, as are 8 and 9)* |
| . (period) | You can use a period to accept zero or more entries the number that precedes the zero. ​ For example, **01.** allows the user to enter 0, 01, 011 and so on. |
| <dialed:substituted> | This is used for sequence substitution, you can use this to indicate that the 1 + area code 555 will be followed by the next 7 digits of a phone number in that area code.  For example with this sequence **<:1555>xxxxxxx** if the user dial a 7 digit number, the number 1555 is added to the beginning of the sequence. If the user press 6782345, the system transmits 15556782345. |
| , (comma) | This can be used between digits to play an “outside line” dial tone after a trigger number or sequence.  For example, with this sequence **9, 1x.** an “outside line” dial tone is sounded after the user presses 9, and continues until the user presses 1 |
| ! (exclamation point) | You can use this character to prohibit a dial sequence.  For example the sequence **1900xxxxxxx!** will make the system reject any 1-900 number. |
| S0 or L0 | Overrides the Short or Long inter-digit timer to 0 seconds.  For example: ​**<:1555>[2-9]xxxxxxS2** on a seven-digit local call, wait two seconds to see if any more digits are dialed - after the delay expires, prefix the number with local area code +1-555 and send it  ​**1[2-9]xx[2-9]xxxxxxS0** indicates, if +1-areacode-number is dialed as eleven digits, do not wait for additional dialed digits and send immediately. |
| P# (where # is the duration of the pause in seconds) | Pauses # seconds. |

---

Related Articles

[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[Configuring your Cisco SPA112/122 ATA](https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata)[What is DTMF? and how to configure it on Telnyx](https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx)[Oracle: Acme Packet SBC Setup](https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup)[Flyingvoice: Telnyx Setup](https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup)

Did this answer your question?

😞😐😃
