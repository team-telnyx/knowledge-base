---
source_url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
scraped: 2026-06-11
---

10DLC Number Assignment Status | Telnyx Help Center

[Skip to main content](#main-content)

# 10DLC Number Assignment Status

Having deliverability issues with a number recently assigned to an approved 10DLC campaign?

K

Written by Klane Pedrie

April 11, 2025

Even if you have taken the step of assigning a number to a 10DLC campaign does not mean you are ready to start sending right away.

The number assignment process can take any where from a few minutes to a few days. The normal timeline is around 2 hours.

You can check a number assignments status by using

<https://developers.telnyx.com/api/messaging/10dlc/get-all-phone-number-campaigns>

1. Open the test endpoint black box
2. Enter your api key for the bearer token. The api key is located on the homepage of your Telnyx account.
3. Enter your search parameters. Easiest is to use the Telnyx or TCR Campaign id that you assigned the number to.
4. If the status next to the number in question is `ASSIGNED` then the number is successfully assigned.
5. If it is assigned but you still had deliverability issues then check the timestamp of the undelivered message against the timestamp for the last update on the assigned number. Normally you will see that it was all messages that were sent prior to the assignment process being complete.
6. If you still have deliverability issues then reach out to [support@telnyx.com](mailto:support@telnyx.com).

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1471509919/3ccf8b1557c2caa3a8c945e9248a/screencapture-developers-telnyx-api-messaging-10dlc-get-all-phone-number-campaigns-2025-04-11-14_05_25.png?expires=1781167500&signature=4a80337fc994eff3ec4d85b787461aa2cd9a8ac72899627f0c612f8862fa1056&req=dSQgF8x%2BlIheUPMW1HO4zb1en9Z5BCrviuENzDOHdjjh28C%2B4SjMC24UScZ4%0AnQydIU2bTDSp1%2Fx4%2B%2BI%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1471509919/3ccf8b1557c2caa3a8c945e9248a/screencapture-developers-telnyx-api-messaging-10dlc-get-all-phone-number-campaigns-2025-04-11-14_05_25.png?expires=1781167500&signature=4a80337fc994eff3ec4d85b787461aa2cd9a8ac72899627f0c612f8862fa1056&req=dSQgF8x%2BlIheUPMW1HO4zb1en9Z5BCrviuENzDOHdjjh28C%2B4SjMC24UScZ4%0AnQydIU2bTDSp1%2Fx4%2B%2BI%3D%0A)

---

Related Articles

[10DLC Shared Campaigns](https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns)[How to create a 10DLC campaign](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign)[Assigning DID to a 10DLC Campaign Fails](https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails)[Telnyx 10DLC Process](https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process)[10DLC Campaign Suspended](https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended)

Did this answer your question?

😞😐😃
