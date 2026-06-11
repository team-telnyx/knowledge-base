---
title: Telnyx Platform Guide
summary: A comprehensive reference for the Telnyx communications platform, covering
  account management, SIP trunking, voice calling, phone number provisioning and porting,
  messaging, webhooks, device configuration, regulatory compliance, and troubleshooting
  — synthesised from official Telnyx documentation.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/1130703-can-i-call-toll-free-with-my-telnyx-number
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- url: https://support.telnyx.com/en/articles/1311073-spain-did-requirements
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
- url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
- url: https://support.telnyx.com/en/articles/2906030-port-out-tracking
- url: https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
- url: https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card
- url: https://support.telnyx.com/en/articles/3505912-australia-did-requirements
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/4353862-creating-postman-collection-from-openapi
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/5120062-portugal-number-porting
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
- url: https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx
- url: https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx
- url: https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api
- url: https://support.telnyx.com/en/articles/5466658-jamaica-did-requirements
- url: https://support.telnyx.com/en/articles/5466851-north-macedonia-did-requirements
- url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
- url: https://support.telnyx.com/en/articles/5807457-nch-express-talk
- url: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal
- url: https://support.telnyx.com/en/articles/6122586-ubiquiti-trunk-unifi-talk-auth
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
- url: https://support.telnyx.com/en/articles/6531682-philippines-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545167-poland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545173-south-africa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6592454-american-samoa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596425-bhutan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6661387-cook-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665126-cuba-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670750-falkland-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670819-french-polynesia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670896-grenada-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674331-haiti-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674453-israel-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674794-kyrgyzstan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674807-lebanon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674989-libya-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675252-malta-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675683-martinique-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677919-mauritius-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678010-myanmar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679129-norfolk-island-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679378-reunion-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679451-samoa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680225-sudan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683365-tonga-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683429-tuvalu-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683454-uzbekistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683459-vanuatu-sms-guidelines
- url: https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
- url: https://support.telnyx.com/en/articles/7885470-chiro8000-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/articles/8520014-qatar-did-requirements
- url: https://support.telnyx.com/en/collections/12044103-regulatory
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/133103-telnyx-sms-guide
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
- url: https://support.telnyx.com/en/collections/3968237-telnyx-sip-trunking-configurations
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
updated_at: 2026-06-11T11:48:37Z
---

# Telnyx Platform Guide

*Part 4 of 4 — see also: [Part 1](telnyx-platform-guide--part-1.md), [Part 2](telnyx-platform-guide--part-2.md), [Part 3](telnyx-platform-guide--part-3.md)*

A comprehensive reference for the Telnyx communications platform, covering account management, SIP trunking, voice calling, phone number provisioning and porting, messaging, webhooks, device configuration, regulatory compliance, and troubleshooting — synthesised from official Telnyx documentation.

## Support

### Contact Methods

- **Chat:** Click "chat with us" in the portal.
- **Phone:** +1-888-980-9750 (US/Canada) or international numbers.
- **Email:** [support@telnyx.com](mailto:support@telnyx.com)

### Reporting Issues

**Call/Message failures:** Provide Call ID/MDR ID, direction, source/destination numbers, date/time with timezone.

**API issues:** Provide endpoint URLs, timestamps, request/response payloads, and whether the issue is reproducible.

**Portal issues:** Provide screenshots or console errors.

NOC can troubleshoot call quality issues up to 72 hours after occurrence; carrier escalations require examples within 48 hours.

### Push Notifications

**Android (Firebase Cloud Messaging):** Create a Firebase project, add FCM to your app, set up a Push Credential in the portal, and attach it to your SIP connection's WebRTC tab.

**iOS (APNS):** Create a VoIP push certificate via Apple Developer, export cert.pem and key.pem, create an iOS Push Credential in the portal, and attach it to your SIP connection.

### Developer Resources

- API v2 documentation: [developers.telnyx.com](https://developers.telnyx.com/api)
- OpenAPI/Postman: Import from [GitHub](https://github.com/team-telnyx/openapi/tree/master/openapi)
- Debugging tools: SIP Call Flow Tool available in the portal
