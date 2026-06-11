---
title: 'WhatsApp with Telnyx: Embedded Signup, Templates, and Sending'
summary: 'End-to-end guide to set up WhatsApp Business with Telnyx: connect via Embedded
  Signup, provision a WABA and number, create and manage message templates, send messages
  (text, media, interactive, and templates), configure webhooks, and troubleshoot
  common issues.'
sources:
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-05-20T09:11:51Z
---

# WhatsApp with Telnyx: Embedded Signup, Templates, and Sending

*Part 1 of 2 — see also: [Part 2](whatsapp-with-telnyx-embedded-signup-templates-and-sending--part-2.md)*

End-to-end guide to set up WhatsApp Business with Telnyx: connect via Embedded Signup, provision a WABA and number, create and manage message templates, send messages (text, media, interactive, and templates), configure webhooks, and troubleshoot common issues.

## Overview and Requirements

WhatsApp Business messaging with Telnyx requires both Telnyx and Meta prerequisites:
- Telnyx: Active account with messaging enabled, valid payment method, admin Portal access (Messaging → WhatsApp).
- Meta: Facebook Business Manager with admin access; business verification recommended for production. Each phone number can be linked to only one Business Manager and must comply with Meta policies.
- Numbers: Use a Telnyx-owned number with an active messaging profile. Bring-your-own non-Telnyx numbers aren’t currently supported via the Portal flow.

Related: [WhatsApp Embedded Signup](whatsapp-embedded-signup.md), [Quickstart: Send Your First WhatsApp Message](quickstart-send-your-first-whatsapp-message.md).

## Embedded Signup Workflow

The Portal guides you through a finite set of states from start to completion:
- Initiation: Start at Portal → Messaging → WhatsApp → Getting Started → Connect WhatsApp Business → Begin Setup. Telnyx creates a signup session (state: initiated) and opens Meta OAuth.
- Facebook OAuth: Grant permissions for WhatsApp Business Management, Business Asset Management, and Webhook Management, then select the target Business Manager (state: facebook_auth). Ensure you’re Business Manager admin.
- WABA Creation: Telnyx provisions a WhatsApp Business Account (WABA) under your Business Manager, applies initial settings (e.g., timezone, category), and connects webhooks through your messaging profile (state: waba_created).
- Number Registration: Select a Telnyx number, associate it with the WABA, and submit registration (state: phone_registered). The number must not be registered with any other WhatsApp provider. WhatsApp uses a separate API path, so you can still use SMS/voice on the same number.
- Verification: Meta verifies ownership and reachability (carrier validation, test SMS, or automated voice call). Typical completion in minutes; complex cases may take up to 24 hours (state: verified).

Notes:
- Landlines: Prefer phone call verification over SMS for reliability.
- Monitoring: Session status may be available via GET /v2/whatsapp/signup/{signup_id}/status; webhook event whatsapp.signup.state_updated provides real-time state changes.

## WABA and Phone Number Provisioning Details

What’s configured on success:
- WABA: Created and linked to your Business Manager; Telnyx is granted partner permissions; settings synced to Telnyx.
- Phone number: Verified and enabled for WhatsApp messaging (can co-exist with SMS/voice). Status flows from pending_verification to verified.
- Webhooks: Use your messaging profile webhook settings; ensure your endpoint is reachable and signature validation is implemented.

Useful API surfaces (for reference):
- List WABAs: GET /v2/whatsapp/business_accounts
- List phone numbers: GET /v2/whatsapp/phone_numbers
- Signup status: GET /v2/whatsapp/signup/{signup_id}/status

## Post-Signup Readiness Checklist

- WABA shows Active/Approved.
- Phone number shows Verified and Enabled for WhatsApp.
- Messaging profile webhook URL is set and reachable (consider a failover URL).
- At least one approved message template exists for outbound initiation.

See also: [Send WhatsApp Messages](send-whatsapp-messages.md).

## Creating and Managing Templates

Meta requires pre-approved templates for business-initiated messages and for messages sent outside the 24-hour window.

Lifecycle and review:
- Create via POST /v2/whatsapp/message_templates. Meta review typically takes 24–48 hours.
- List/filter via GET /v2/whatsapp/message_templates (filter by status or name search).
- Get one via GET /v2/whatsapp/message_templates/{template_id}.
- Update via PATCH /v2/whatsapp/message_templates/{template_id} (status resets to PENDING and is temporarily unavailable for sending until re-approved).
- Delete via DELETE /v2/whatsapp/message_templates/{template_id}.

Critical requirements for approval:
- Set and get approval for the phone number display name before submitting any templates.
- Provide sample parameter values in components.example when your template contains variables like {{1}}, {{2}}.
- Complete your business profile (website, description, industry) to reduce rejections.

Categories and expectations:
- AUTHENTICATION: OTP/login verification. No media or URLs; must include a copy-code or one-tap OTP button; limited to one code parameter; generally lowest pricing; opt-in not required.
- UTILITY: Transactional updates (order, shipping, account alerts); opt-in required; mid-tier pricing.
- MARKETING: Promotions/newsletters; opt-in required; highest pricing.

Naming rules and reuse:
- Use lowercase letters, numbers, and underscores; max 512 characters; unique per language within your WABA.
- Avoid test/sample/demo terms; Meta flags these for extra review.
- Edit rejected templates instead of recreating—Meta enforces a 30-day restriction on reusing names.

Multi-language:
- Create one template name with multiple language variants; each is reviewed independently.

Common template API errors:
- 40008: Template operation failed (pending, rejected, paused, disabled, or usage issue). Check status and Meta details.
- 10004: Missing required parameter.
- 10032: Invalid enumerated value (e.g., category or language).

Further guidance: Telnyx Support center best practices and troubleshooting for WhatsApp templates (https://support.telnyx.com/en/articles/13986483).

Learn more: [Manage WhatsApp Message Templates](manage-whatsapp-message-templates.md).

## Sending WhatsApp Messages via API

Endpoint: POST https://api.telnyx.com/v2/messages/whatsapp

Required fields:
- from: Your WhatsApp-enabled Telnyx number (E.164). Messaging profile is auto-resolved from this.
- to: Recipient number (E.164).
- whatsapp_message: Object describing the content. Supported types include text, template, image, video, document, audio, sticker, location, contacts, interactive, reaction.
- webhook_url: Optional per-message callback URL override.

Template messages:
- Required to start conversations outside the 24-hour window. Use name + language or a template_id (Telnyx UUID from the templates list endpoint). Pass dynamic values via components (header/body/button parameters).
- Media headers are supported (image/video/document with link and optional caption/filename).

Non-template messages (within 24-hour window only):
- Text: 1–4096 bytes; optional preview_url for link previews.
- Media: One media object per message; each requires exactly one of link (URL) or id (Meta media ID). Captions up to 1024 bytes (not for audio/stickers).
- Location: latitude/longitude as strings; valid geographic ranges; optional name/address.
- Contacts: 1–257 contact cards per message.
- Interactive: button (quick replies), cta_url (open URL), list (sections/rows), location_request_message, and carousel.
- Reaction: React to a specific message by wamid.
- Reply context: Include context.message_id to reply to a specific inbound/outbound message.
- Callback tracking: biz_opaque_callback_data is echoed back in delivery webhooks for correlation.

Validation highlights:
- Text body: 1–4096 bytes; media captions/header text up to 1024 bytes.
- Latitude: -90 to 90; Longitude: -180 to 180 (as strings).
- Exactly one media per message; provide exactly one of link or id in media objects.

Common send-time error:
- 40008: Catch-all for template issues and delivery failures. Check template status, quality, and Meta error details.

Deeper dive: [Send WhatsApp Messages](send-whatsapp-messages.md).
