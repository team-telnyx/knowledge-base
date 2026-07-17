---
source_url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
title: "Porting Error Messages"
description: "Learn more about the various error conditions that may occur with… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 1547d42f6fbe11b633229dd67273051411b7e9e2a97c5839e49d256f7c5fe865
---







# Porting Error Messages

Learn more about the various error conditions that may occur with… See Telnyx guidance and requirements.




There is a wide range of potential error conditions that may occur during the porting process. Below is a list of potential errors with additional information that may be helpful in diagnosing porting problems.

## ACCOUNT\_NUMBER\_MISMATCH

The account number provided did not match what the losing carrier has on file. For some carriers, the account number may be the same as the Billing Telephone Number (BTN).

## ACCOUNT\_NUMBER\_REQUIRED

The account number was not provided but is required.

## AUTH\_NAME\_MISMATCH

The authorized user name provided did not match what the losing carrier has on file. The names must match exactly or the carrier will likely reject the port out.

## BTN\_ATN\_MISMATCH

The Billing Telephone Number (BTN) or Account Telephone Number (ATN) did not match what the losing carrier has on file. The BTN or ATN is rarely found on the invoice. In some cases it may be one of the phone numbers on the account.

## BUSINESS\_NAME\_MISMATCH

The business name or end user name provided did not match what the losing carrier has on file.

## DIFFERENT\_ACCOUNTS

One or more phone numbers specified in the port request were part of separate accounts. Carriers will only allow port requests for a single account at a time. It is up to the customer to identify which numbers belong to each account.

## DIFFERENT\_RATE\_CENTERS

One or more phone numbers specified in the port request were in different rate centers. Some carriers require that port requests be split into multiple requests by rate center. This type of error is typically corrected by Telnyx's porting team without customer assistance.

## FOC\_REJECTED

The FOC date requested was not accepted by the losing carrier.

## ILLEGIBLE\_LOA

The LOA provided was illegible or unreadable.

## INVALID\_RESELLER

For Canadian number porting, the reseller specified in the port request did not match what the losing carrier has on file.

## LOSING\_CARRIER\_NO\_RESPONSE

The losing carrier did not respond to the port out request. This type of error is typically corrected by Telnyx's porting team without customer assistance.

## OTHER

An unspecified error condition occurred when trying to validate the port out information.

## PASSCODE\_PIN\_INVALID

The passcode or pin number provided did not match what the losing carrier has on file.

## PENDING\_ORDER

One or more phone numbers specified in the port request are already in the process of being ported out or have another service change that is pending.

## PORTING\_MAIN\_BTN

The port request was specified as a partial port out but one of the phone numbers specified in the port request is the Billing Telephone Number (BTN). This would leave one or more stranded numbers on the account without a BTN.

## REQUEST\_INCORRECT

The port request was either incorrectly specified as a partial port out or a full port out.

## SERVICE\_ADDRESS\_MISMATCH

The service address specified in the port request did not match what the losing carrier has on file.

## TN\_HAS\_SPECIAL\_FEATURE

One of the phone numbers specified in the port request has a special feature that must be removed before the number can be ported. This might include a DSL line or special bundled pricing.

## TN\_MISMATCH

## One of the phone number specified in the port request is not on the account specified.

## TN\_NOT\_PORTABLE

One of the phone numbers specified in the port request is not portable.

## UNSUPPORTED\_RATE\_CENTER

Telnyx cannot port one of the phone number specified because the rate center is not supported. This typically happens with rural rate centers where the incumbent carrier has a monopoly.

## ZIP\_POSTAL\_CODE\_MISMATCH

The zip or postal code specified in the port request did not match what the losing carrier has on file.

---

Related Articles

[BTN or ATN Mismatch Error](https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error)[Porting Policy & Procedure](https://support.telnyx.com/en/articles/1130630-porting-policy-procedure)[Automated Port Request Validation](https://support.telnyx.com/en/articles/1516776-automated-port-request-validation)[Port numbers away from Telnyx](https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx)[Port Request Statuses](https://support.telnyx.com/en/articles/3284588-port-request-statuses)

Did this answer your question?

😞😐😃
