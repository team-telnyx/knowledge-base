---
title: Action ordering requirements
summary: Complete action requirements for international phone number orders that cannot be fulfilled through standard documentation.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement/index
    content_hash: 2c3dd6d156273cef8286b3167fc2873e09a92e8980b89e84688f6e677da399f0
updated_at: 2026-04-10T00:00:00Z
---

# Action ordering requirements

Complete action requirements for international phone number orders that cannot be fulfilled through standard documentation

## Overview

Action requirements are a special type of regulatory requirement for international phone number orders [that cannot be fulfilled by submitting documents or text information](https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements). Instead, these requirements need the end user to complete an external action, such as identity verification through a third-party service.

Each action requirement type may have different fulfillment steps depending on the specific verification needed. This guide provides detailed instructions for completing each action requirement. As new action requirement types are introduced, this guide will be updated with their specific fulfillment processes.

## Australia mobile ID verification

Australia mobile number orders require end user identity verification to comply with local telecommunications regulations. To facilitate a secure and efficient verification experience, Telnyx has partnered with [Onfido](https://onfido.com/), a trusted identity verification provider.

### Requirement ID

The Australia mobile ID verification requirement has the following identifier:

* **Requirement ID**: `b7c72fb8-fa08-4529-aaf6-b9117d3f3698`

This ID is used when initiating the verification process through the external requirements endpoint.

### Verification process

To complete ID verification for an Australia mobile number order:

1. Generate a unique verification link by making a request to the [POST /v2/external\_requirements//sub\_number\_orders/ endpoint](https://developers.telnyx.com/api/numbers). Include the end user's `first_name` and `last_name` in the request body.

2. The API returns a URL in the `requirement_action.value` field. Share this URL with the end user to access Onfido's secure ID verification portal.

3. The end user visits the provided URL and completes the identity verification process by submitting required identification documents through the Onfido portal.

4. Once submitted, the verification is reviewed. Upon approval, the requirement is automatically marked as completed on the number order.

5. The order's `requirements_met` field updates to `true`, allowing the order to proceed to the next stage.


## Related Pages

- [Port-in requirements](../runbooks/port-in-requirements.md)
- [Regulatory Requirements](../runbooks/regulatory-requirements.md)
