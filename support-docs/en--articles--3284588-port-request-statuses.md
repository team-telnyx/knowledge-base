---
source_url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
scraped: 2026-07-08
content_hash: b334b6b275900e7b374df31481407b799a9ac60ba6a1992283b6bf35de66c042
---

Port Request Statuses | Telnyx Help Center

[Skip to main content](#main-content)

# Port Request Statuses

Here you will find explanations of different Port Request statuses via API.

Written by Paul Cross

June 6, 2024

Table of contents

Our developer docs provide full information to Porting phone numbers via API with Telnyx. You can find all of the information needed for porting via API in our Developer docs [here](https://developers.telnyx.com/docs/numbers/porting).

# **Different porting statuses and what they mean:**

## **"draft"**

When a port request is created, it will begin in a "draft" status. During this stage, you will be able to fill out the porting order with all applicable information and documentation before eventually submitting it to Telnyx.

Please note, there is a retention policy on "draft" porting orders. If a porting order is still in a "draft" status 30 calendar days after it was created, then the order will be deleted. At which point, you would need to create a new order to continue the porting process.

## **"in-process"**

This is the status of a port request once it has been successfully submitted to Telnyx. When a port request is "in-process" this means that we have received the port request and it is currently waiting to be submitted to the losing provider. Generally, this status will change after a few hours (during business hours).

## **"submitted"**

This is the status of a port request once it has been successfully submitted to the losing provider. When a port request is "submitted" this means that we are awaiting the losing providers response. Generally, we will update the port request within 48-36 business hours once the losing provider has responded to us.

## **"exception"**

This is the status of a port request once the port request has been deemed invalid by the losing provider. When a port request is "exception" this means that the losing provider has responded with a rejection. Generally, this means that something that was submitted to Telnyx within the port request differs from the information that is on record with the losing carrier.   
For a full list of rejection reason, please see [Porting Error Messages](https://support.telnyx.com/en/articles/1618776-porting-error-messages)

## **"foc-date-confirmed"**

This is the status of a port request once the port request has been confirmed by the losing provider. When a port request is "foc-date-confirmed" this means that the losing provider has provided a port confirmation date. Generally, this means that the port is confirmed and it will port at the specified date/time as per the "foc\_date" field.

## **"activation-in-progress" (V2 API only)**

This status signifies the transition between the “foc-date-confirmed” and “ported” statuses. This is the status of a port request when the FOC date/time arrives and the port is in progress- when the port and internal activation of the number is occurring.

## **"ported"**

This is the status of a port request once the port request has been confirmed as ported away from the losing provider and now with Telnyx. When a port request is "ported" this means that calls should now be hitting Telnyx. Generally, this means that the port is fully complete and calls will now route via Telnyx.

## **"cancel-pending"**

This is the status of a port request once Telnyx receive the cancellation request for the port request. When a port request is "cancel-pending" this means that Telnyx now need to inform the losing carrier of the cancellation request. Generally, this means that the port will be confirmed as ported once we receive confirmation from the losing carrier that they have cancelled the original port request from Telnyx. Depending upon the losing carrier, this can take up to 48 hours.

## **"cancelled"**

This is the status of a port request once Telnyx receive the confirmation of the cancellation of the port request from the losing carrier. When a port request is "cancelled" this means that Telnyx have received confirmation from the losing carrier. Generally, this means that the port is confirmed as cancelled on the losing carrier's side and they will not remove the number(s) from routing on/after the requested/confirmed porting date.

​

---

Related Articles

[Porting Policy & Procedure](https://support.telnyx.com/en/articles/1130630-porting-policy-procedure)[Automated Port Request Validation](https://support.telnyx.com/en/articles/1516776-automated-port-request-validation)[Port-In Best Practices](https://support.telnyx.com/en/articles/2030770-port-in-best-practices)[United Kingdom Number Porting](https://support.telnyx.com/en/articles/3267693-united-kingdom-number-porting)[US / CA Toll Free Number Porting](https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting)

Did this answer your question?

😞😐😃

Table of contents
