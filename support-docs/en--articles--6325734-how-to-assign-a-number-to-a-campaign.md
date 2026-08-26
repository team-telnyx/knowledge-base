---
source_url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
title: "How to assign a number to a campaign"
description: "Assigning numbers to your campaign is the third step to becoming compliant with 10DLC rules. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 4caed8cd015a30d79c2ee940484b391c6429b638ee595e620920bae6fc0fc427
---

# How to assign a number to a campaign

Assigning numbers to your campaign is the third step to becoming compliant with 10DLC rules. See Telnyx guidance and requirements.

## **How to Assign a Number to a Campaign**

Once you have set up your campaign and it has been approved, you need to assign a number (or numbers) to it. Messages sent from numbers not assigned to an approved campaign may be filtered or blocked by carriers.

*Note: This guide assumes you have already:*

1. Created a 10DLC Brand — [Guide](https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand)
2. Created a 10DLC Campaign and received "MNO Approved" status — [Guide](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign)
3. Have an SMS-capable 10-digit phone number on your Telnyx account ([purchase](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) or [port](https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx) one if not)

**Important notes about assignment:**

* A number can only be associated to one campaign, but a campaign can have up to 49 numbers
* The 49 number maximum is due to T-Mobile limitations
* If you wish to exceed this maximum, you must complete a T-Mobile Number Pool Request form, incurring additional charges. Telnyx Support can help you with this process. Further details on [this topic here](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges#h_647771465f).

---

## **Assigning a Number via the Mission Control Portal**

Follow these steps to assign a number in the portal. If you would prefer to complete this step via the API, you can find details on how to do that in our [API documentation](https://developers.telnyx.com/docs/messaging/10dlc/concepts).

1. Log in to the [Mission Control Portal](https://portal.telnyx.com/).
2. Navigate to **Messaging > 10DLC Campaigns**.
3. Select your approved campaign from the list.
4. Go to the **Phone Numbers** tab within the campaign.
5. Select the number(s) you want to assign from your available numbers.
6. Click **Assign to Campaign**.
7. The assignment status will show as **PENDING** while processing.
8. Once complete, the status will change to **ASSIGNED** — you can now send messages.

**Timeline:** Assignment typically takes about 2 hours but can range from a few minutes to a few days.

---

## **Troubleshooting**

|  |  |
| --- | --- |
| Issue | Solution |
| Assignment stuck in PENDING for >24 hours | Contact [support@telnyx.com](mailto:support@telnyx.com) |
| Status shows FAILED | Ensure the number is SMS-capable, the campaign is approved, and the number is not already assigned to another campaign |
| Messages not delivering after assignment | Check that the assignment timestamp is before the message send timestamp. Assignment may still have been processing when you sent. |
| Cannot find number in assignment list | Ensure the number is on your Telnyx account and is SMS-capable (not voice-only) |

For more troubleshooting, see [Assigning DID to a 10DLC Campaign Fails](https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails).

---

## **Important Notes**

* Keep at least one active number assigned to your campaign at all times to avoid dormancy suspension
* Inactive campaigns (no numbers for 15+ days) may be automatically suspended — see [10DLC Campaign Suspended](https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended)
* Each number can only be assigned to one campaign at a time
* If you need to move a number to a different campaign, unassign it first, then assign it to the new campaign

---

Related Articles

[How to create a 10DLC brand](https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand)[How to create a 10DLC campaign](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign)[Bring Campaigns to Telnyx](https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx)[10DLC Campaign Suspended](https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended)[10DLC Number Assignment Status](https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status)

Did this answer your question?

😞😐😃
