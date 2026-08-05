---
title: 10DLC Campaign Use Cases and Event Notifications
summary: Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages,
  opt-in/opt-out requirements, and webhook event notifications for brands, campaigns,
  and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
updated_at: 2026-08-05T13:49:31Z
---

# 10DLC Campaign Use Cases and Event Notifications

*Part 5 of 8 — see also: [Part 1](10dlc-campaign-use-cases-and-event-notifications--part-1.md), [Part 2](10dlc-campaign-use-cases-and-event-notifications--part-2.md), [Part 3](10dlc-campaign-use-cases-and-event-notifications--part-3.md), [Part 4](10dlc-campaign-use-cases-and-event-notifications--part-4.md), [Part 6](10dlc-campaign-use-cases-and-event-notifications--part-6.md), [Part 7](10dlc-campaign-use-cases-and-event-notifications--part-7.md), [Part 8](10dlc-campaign-use-cases-and-event-notifications--part-8.md)*

Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages, opt-in/opt-out requirements, and webhook event notifications for brands, campaigns, and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.

## 10DLC Event Notifications

You can choose to be notified about events on your 10DLC Brands, Campaigns and Phone Numbers by configuring webhooks. For this mechanism to work, you'll need a publicly accessible HTTP server that can receive our webhook requests at one or more specified URLs. We highly recommend using HTTPS (instead of HTTP). The [Receive Webhooks](https://developers.telnyx.com/docs/messaging/messages/receive-message) tutorial walks through setting up a basic application for receiving webhooks.

### Configuring Webhooks

To receive notifications for brands you need to either provide the webhooks at the [creation](https://developers.telnyx.com/api-reference/brands/create-brand) of the brand or you may [update](https://developers.telnyx.com/api-reference/brands/update-brand) an existing brand. In both cases you have to pass your webhooks in the **webhookURL** and **webhookFailoverURL**. `webhookFailoverURL` is optional.

Example of updating the webhooks of a brand:

```
curl -X PUT https://api.telnyx.com/10dlc/brand/:brandid \
  -H 'Content-type: application/json' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -d '{"webhookURL":"https://mywebhooks.com/c5e5e598-95b3-4076-bfe2-c7d2c58ec57f", "webhookFailoverURL":"https://mywebhooks.com/ae20ec14-1c23-4275-add5-3290706b450f"}'
```

The same applies for campaign event notifications. Webhooks can be provided either upon campaign [creation](https://developers.telnyx.com/api-reference/campaign/submit-campaign) or through an [update](https://developers.telnyx.com/api-reference/campaign/update-campaign). Webhooks configured for a campaign are also leveraged for event notifications with phone numbers associated with that campaign. Phone number notifications are triggered for shared campaigns as well.

### Overall Structure of Events

Here is an example of a webhook event:

```json
{
  "data": {
    "event_type": "10dlc.brand.update",
    "id": "02d4f0e2-7a9d-4ebf-86b9-3df81e862d49",
    "occurred_at": "2024-08-07T17:22:37.328+00:00",
    "payload": {
      "brandId": "97091164-e814-435c-9c1b-14ab2d18e987",
      "brandName": "Some Brand LLC",
      "description": "Brand BBRAND1 is added",
      "eventType": "BRAND_ADD",
      "status": "success",
      "tcrBrandId": "BBRAND1",
      "type": "TCR_BRAND_UPDATE"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://mywebhooks.com/310fda1a-d415-4827-837b-5f7e72657b65"
  }
}
```

**`data` fields:**

| Field | Description |
| --- | --- |
| `event_type` | We currently support 3 types of events: `10dlc.brand.update`, `10dlc.campaign.update` and `10dlc.phone_number.update` for updates related to brands, campaigns and phone numbers respectively. |
| `id` | Unique ID of this event. |
| `occurred_at` | Timestamp of the event. |
| `payload` | The content of the payload varies according to the type of event. |
| `record_type` | Always `event` for webhook events. |

**`meta` fields:**

| Field | Description |
| --- | --- |
| `attempt` | The delivery attempt number, starting at 1. Useful for identifying retries. |
| `delivered_to` | The webhook URL where this event was sent. |

### Brand Events

| Payload type | Description |
| --- | --- |
| `REGISTRATION` | Failures during the registration process. The payload will contain a field called `reasons` with more details about the errors encountered. |
| `REVET` | Success of the revetting request operation. See the [revet brand endpoint](https://developers.telnyx.com/api-reference/brands/revet-brand) for more details. |
| `ORDER_EXTERNAL_VETTING` | Notification on the process of ordering an external vetting. The `status` field indicates if the order succeeded or failed. |
| `TCR_BRAND_UPDATE` | Notifications received from TCR. See table below for included events. |

**TCR events under `TCR_BRAND_UPDATE`:**

| TCR Event | Description |
| --- | --- |
| `BRAND_ADD` | Brand successfully added on TCR. |
| `BRAND_APPEAL_ADD` | A Brand appeal was added. |
| `BRAND_APPEAL_COMPLETE` | The result of a brand appeal. |
| `BRAND_REVET` | Result of a brand revet request. |

**Example `REGISTRATION` notification:**

```json
{
  "data": {
    "event_type": "10dlc.brand.update",
    "id": "456abc67-7a9d-4ebf-86b9-3df81e862d49",
    "occurred_at": "2024-08-07T17:22:37.328+00:00",
    "payload": {
      "brandId": "b0e2ec67-b26f-4c77-affc-d10f4d1780d3",
      "status": "failed",
      "type": "REGISTRATION",
      "reasons": [
        {
          "fields": ["ein"],
          "description": "Invalid EIN - EIN is a nine-digit number. The format is XX-XXXXXXX. The \"-\" symbol is also accepted."
        }
      ]
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://mywebhooks.com/310fda1a-d415-4827-837b-5f7e72657b65"
  }
}
```

### Campaign Events

| Payload type | Description |
| --- | --- |
| `REGISTRATION` | Notifications about failures during the registration process. The errors will be listed in the `reasons` field of the payload. |
| `TELNYX_REVIEW` | Telnyx internal compliance review notification. Sent when Telnyx approves or rejects a campaign. The `status` field contains `ACCEPTED` or `REJECTED`. The `description` field contains the TCR campaign ID (e.g., C6X6M95). |
| `NUMBER_POOL_PROVISIONED` | Success on provisioning a number pool. |
| `NUMBER_POOL_DEPROVISIONED` | Success on deprovisioning a number pool. |
| `TCR_EVENT` | Notification received from TCR. See table below for specific event types. |
| `MNO_REVIEW` | MNO/DCA review results. The `status` field contains `ACCEPTED` or `REJECTED`. In case of rejection, the `description` field provides a reason. |
| `TELNYX_EVENT` | Telnyx system events such as campaign suspension. The `status` field contains `DORMANT` for suspended campaigns. |
| `VERIFIED` | Campaign has been successfully provisioned with MNOs. Sent when campaign reaches `MNO_PROVISIONED` status. |

**TCR events under `TCR_EVENT`:**

| TCR Event | Description |
| --- | --- |
| `CAMPAIGN_ADD` | Campaign successfully added to TCR. |
| `CAMPAIGN_BILLED` | Campaign billing event from TCR. |
| `CAMPAIGN_DCA_COMPLETE` | DCA processing complete for campaign. |
| `CAMPAIGN_EXPIRED` | Campaign has expired. |
| `CAMPAIGN_NUDGE` | Nudge event sent by partner CSP to trigger campaign re-review after appeal or rejection. |
| `CAMPAIGN_RESUBMISSION` | Campaign has been resubmitted. |
| `CAMPAIGN_UPDATE` | Campaign has been updated. |
| `MNO_CAMPAIGN_OPERATION_APPROVED` | MNO has approved the campaign. |
| `MNO_CAMPAIGN_OPERATION_REJECTED` | MNO has rejected the campaign. |
| `MNO_CAMPAIGN_OPERATION_REVIEW` | Campaign is under MNO review. |
| `MNO_CAMPAIGN_OPERATION_SUSPENDED` | MNO has suspended the campaign. |
| `MNO_CAMPAIGN_OPERATION_UNSUSPENDED` | MNO has unsuspended the campaign. |

**Example campaign `REGISTRATION` failure notification:**

```json
{
  "data": {
    "event_type": "10dlc.campaign.update",
    "id": "c3d4e567-8901-4bcd-ef23-456789012345",
    "occurred_at": "2024-08-07T17:22:37.328+00:00",
    "payload": {
      "campaignId": "751c6a5c-907b-43a9-8ada-ba1dc8335b07",
      "status": "failed",
      "type": "REGISTRATION",
      "reasons": [
        {
          "fields": ["sample1"],
          "description": "Sample message does not contain required opt-out language"
        }
      ]
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://mywebhooks.com/310fda1a-d415-4827-837b-5f7e72657b65"
  }
}
```

**Example `VERIFIED` notification:**

```json
{
  "data": {
    "event_type": "10dlc.campaign.update",
    "id": "456abc67-7a9d-4ebf-86b9-3df81e862d49",
    "occurred_at": "2024-08-07T17:22:37.328+00:00",
    "payload": {
      "brandId": "97091164-e814-435c-9c1b-14ab2d18e987",
      "campaignId": "751c6a5c-907b-43a9-8ada-ba1dc8335b07",
      "createdDate": "2024-07-06T14:22:37.328+00:00",
      "cspId": "CSPID1",
      "type": "VERIFIED",
      "isTMobileRegistered": true
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://mywebhooks.com/310fda1a-d415-4827-837b-5f7e72657b65"
  }
}
```

**Example `TELNYX_REVIEW` notification (approval):**

```json
{
  "data": {
    "event_type": "10dlc.campaign.update",
    "id": "789def12-3a4b-5c6d-7e8f-9a0b1c2d3e4f",
    "occurred_at": "2024-08-07T17:22:37.328+00:00",
    "payload": {
      "campaignId": "751c6a5c-907b-43a9-8ada-ba1dc8335b07",
      "description": "C6X6M95 approved by Telnyx",
      "status": "ACCEPTED",
      "type": "TELNYX_REVIEW"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://mywebhooks.com/310fda1a-d415-4827-837b-5f7e72657b65"
  }
}
```

**Example `MNO_REVIEW` notification (rejection):**

```json
{
  "data": {
    "event_type": "10dlc.campaign.update",
    "id": "def45678-90ab-cdef-1234-567890abcdef",
    "occurred_at": "2024-08-07T17:22:37.328+00:00",
    "payload": {
      "campaignId": "751c6a5c-907b-43a9-8ada-ba1dc8335b07",
      "description": "Campaign rejected by T-Mobile due to insufficient opt-out instructions",
      "status": "REJECTED",
      "type": "MNO_REVIEW"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://mywebhooks.com/310fda1a-d415-4827-837b-5f7e72657b65"
  }
}
```

> **Note:** The `campaignId` field in webhooks contains the Telnyx UUID, not the TCR campaign ID. The TCR campaign ID (e.g., C6X6M95) may appear in the `description` field.

### Phone Number Events

| Payload type | Description |
| --- | --- |
| `ASSIGNMENT` | Notifications about the phone number assignment process. In case of failure, an error message is displayed in the `reasons` field. That field is empty in case of a successful assignment. |
| `DELETION` | Notifications about the phone number removal process. In case of failure, an error message is displayed in the `reasons` field. That field is empty in case of a successful removal. |
| `STATUS_UPDATE` | The status of the phone number was updated. The new status is shown in the `status` field. |

Phone numbers in webhook payloads use E.164 format (e.g., `+16715455939`), which includes the country code prefix.

The `status` field in `STATUS_UPDATE` notifications can be: `ADDED`, `DELETED`, `PENDING`, or `FAILED`.

**Example successful `ASSIGNMENT` notification:**

```json
{
  "data": {
    "event_type": "10dlc.phone_number.update",
    "id": "123abc67-7a9d-4ebf-86b9-3df81e862d49",
    "occurred_at": "2024-08-07T17:22:37.328+00:00",
    "payload": {
      "campaignId": "751c6a5c-907b-43a9-8ada-ba1dc8335b07",
      "phoneNumber": "+16715455939",
      "status": "success",
      "type": "ASSIGNMENT",
      "reasons": []
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://mywebhooks.com/310fda1a-d415-4827-837b-5f7e72657b65"
  }
}
```
