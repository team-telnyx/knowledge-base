---
title: Telnyx Platform Guide
summary: A comprehensive reference for the Telnyx communications platform, covering
  account management, SIP trunking, voice calling, phone number provisioning and porting,
  messaging, webhooks, device configuration, regulatory compliance, and troubleshooting
  — synthesised from official Telnyx documentation.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
  content_hash: 192b581a0df77e51790ff3ebdc060139e0b2825703054beefecc0f78fa4d77f8
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
  content_hash: 439dd1e25fc458a9b756b7969077eddfd9953006f14440f722c5d9b91f5409f3
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
  content_hash: 6bcd3a7433b54c5e0a0227aaa573b6389a41318bcee17dd868c08dc7f050510f
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
  content_hash: 38e9951445c88d8ef3718a7d3d37b463289803d20106b238f44cb02c0ad1e7c2
- url: https://support.telnyx.com/en/articles/1130703-can-i-call-toll-free-with-my-telnyx-number
  content_hash: 37e59e8ea352b1275a468eb6ad1665b47b0445db7f0516dcfce9b8a846139193
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
  content_hash: 081307e3b9fec612f03d51f0fabf36559d090161f9465f88a4f15189a185471c
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
  content_hash: 3e2fcec2e07c0d9d97ec9f8ab463d753694b525b25af0cafae412d594fce5f46
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
  content_hash: dcc802fbd76de6cd51ca8aa233add8b1620dc5005d8be92e19e670e7acd7bf02
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
  content_hash: f3c47f34626edf3edcdeadadd3caf0bea970e047cd00857c49527519aaabc3d3
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
  content_hash: 4dee0ecdbf42899aa846a9b07e64ea1f685c75f8af00ba317e5d63ec95d70415
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
  content_hash: 5e8e1cf8aa10a3e34339535088e67de5170094bfa9d4b7fe2d7fffe43bba081e
- url: https://support.telnyx.com/en/articles/1311073-spain-did-requirements
  content_hash: d87efa57f595f83054792bc600983b799edcf0fbf124ee17949578963375e539
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
  content_hash: ca987b60f15def8a87067e0a8250eaf599367bdc0ce20fe89af975be3956d347
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
  content_hash: 9cb26e9bb06a1e5c0b986f4206a3bab896f90a4c6cbce0d8a56f954978b32c32
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
  content_hash: ec9ec37794c02f311d3c16c1abcd12c09bb7759a9bbef4feac02f00a28d92c0f
- url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
  content_hash: 387c0b65bacba9dd506b55501ea898c01d696d41bdbd100200d0045371f2a842
- url: https://support.telnyx.com/en/articles/2906030-port-out-tracking
  content_hash: 259d05fb1d90b8a008f2193242a6cf58ddd906a12393bb3d5d00018c6c5702f9
- url: https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup
  content_hash: 4b8a4a6ecb3a37aad724d2373c810fd47c65258117a4c8ecc4f752ec69630124
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
  content_hash: f58a065d184803d7f6bc889234fa91c4a998ff062f2510bacb8129de19642816
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
  content_hash: d1046dcb7b3d12bab03cec3ceacd98ff6132720d2ab96d20189fae00415c1f78
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
  content_hash: a6d8cc59763e462c9ba42837c39338f274370b6bcc92894944eab8b941e45d84
- url: https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card
  content_hash: 0b1118734af918e570d414850d72ad5c85cde8497dffd153252f7ef68c6e3679
- url: https://support.telnyx.com/en/articles/3505912-australia-did-requirements
  content_hash: 2e5f452734704e5cb4a63c0196f81bbc84f2fcdf142d2b4940b28f16c43054c4
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
  content_hash: 2f329b4bad65e68226cce8ab4971597104cf266f54c736ffc0a5a6ef7a03f74c
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
  content_hash: fe996505acc9060e96208b663206ae161ec9c27affa2f47b1690f5982c91f22e
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
  content_hash: effdf77b4b9c3d790c495bdf1abcd404d8362f711458aa61d6ebe8f93c2b2295
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
  content_hash: 414d0ce574a1775a590108055eb70864c0667b090a876d431d45d47776264fca
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
  content_hash: 493d22b14e79076a35b31098865b21e8cdb0b6512f345ed7ed2a5e3980b8b393
- url: https://support.telnyx.com/en/articles/4353862-creating-postman-collection-from-openapi
  content_hash: cf3e2dca4a9dbbb5b0ffa69498b105a7bbf126ed1330c974dfb86794b2984736
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
  content_hash: 95cabd02d1dcd5a9d9213a844bc09d66efe30b62318a3b1dd42c7d5557f06b45
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
  content_hash: 4135a69fe81e163118bd6599a0e1923f45c0dcfe19265f1617fa4a4adbdb6806
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
  content_hash: 969c476529b99eed7b5996b2f65d7793f2507c08dfdd062e01e98652645933b5
- url: https://support.telnyx.com/en/articles/5120062-portugal-number-porting
  content_hash: 1a4b52a39de7feef57e853ffce564abdf7a20fac142a4e7f79b1b2719beed69e
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
  content_hash: d10dfb19d9294085fdd76700669dca618b30f2aa7fc08ba68c583619e8501f9b
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
  content_hash: 946ce2b5bf3115aa0cc6e0bc7a80c4f46264cb582cccd722e5f360e68e945951
- url: https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup
  content_hash: dac91fd4cf3b7c2202a7a6592407b35ca0e1874e922de9a44f89043e430b76ba
- url: https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup
  content_hash: 3c899675164ca5ba593c8d474fd26feef8b323e2e22bc8db64f42a5ac69927a2
- url: https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup
  content_hash: 910c03b5bd22ab1ab791686cf0729144eec5fc993f802179a4c210a1dfb5dddc
- url: https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup
  content_hash: 5317a35292a58c5a76e0bc300b99dacfe5dce5f9a38d0b49a529cba208e0db70
- url: https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx
  content_hash: 438d44839b14293df479379d4b11cd107c0dea68ebe7a8f1047577c7704d0d1a
- url: https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx
  content_hash: f24bec023c83e5ae3dd8daf229620c1d5fb0b2d8c68c7016a30cb84d5647598b
- url: https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api
  content_hash: 0c55a4ebcb31688b5c9ee09f1959d9843e5414dca29534c1104b4c341adc79ac
- url: https://support.telnyx.com/en/articles/5466658-jamaica-did-requirements
  content_hash: 31af3cac275eea8c2d4561c48c3b8b9c26cf28e01b10cd46339e91a09a9a863c
- url: https://support.telnyx.com/en/articles/5466851-north-macedonia-did-requirements
  content_hash: 0793e0b9ac29aa70e858201c8b917d63cda40218118f7256b409de1fa5c4ba71
- url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
  content_hash: 8b9e940210a7a30a5d3a02558de0e80769238824c5357ebcb6576644b9db2b55
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
  content_hash: d62f6f616e1ec69b67604c8eb658ad9ba15359e4ca71bfae01e42abb99b61c99
- url: https://support.telnyx.com/en/articles/5807457-nch-express-talk
  content_hash: 34fd53b5d15ce95376cc447ba146d26c432d3f37e2ede80765e5edbe0daa5e32
- url: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal
  content_hash: c7869094ca3cedcf8d8cd22d3a8d08cbf8cd6d9a9ebf85cb7fbfe64f1f78f03c
- url: https://support.telnyx.com/en/articles/6122586-ubiquiti-trunk-unifi-talk-auth
  content_hash: 3acb23c1063c7f8cfeb5689c284712f2a6d922fdb79bafd079eaa33f672889fb
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
  content_hash: 61467cf750ed544de537426bc6f59355f05eab706beedebc04a2f3a86eaf4848
- url: https://support.telnyx.com/en/articles/6531682-philippines-sms-guidelines
  content_hash: 4dde866741ede75aaa91eb9f81b4aee576381ad030d775353f658e83e97f8a98
- url: https://support.telnyx.com/en/articles/6545167-poland-sms-guidelines
  content_hash: 64a6aca6867f5d3138051dd0135f687b613f5496154b456a47652a71ea402f04
- url: https://support.telnyx.com/en/articles/6545173-south-africa-sms-guidelines
  content_hash: 2f67cec745e84207b195857204aac4f0ca32bea3c2b194c16236d2476b2e8ca2
- url: https://support.telnyx.com/en/articles/6592454-american-samoa-sms-guidelines
  content_hash: 71d35553bb7550a3e89dbf3e4abffcfc7c7cb70ea0458b04ce218cf86ffea110
- url: https://support.telnyx.com/en/articles/6596425-bhutan-sms-guidelines
  content_hash: a90c609fb908a7abadbfa9d62aaa4c4107d4ae4001b63bbcde1c8b0bc247832e
- url: https://support.telnyx.com/en/articles/6661387-cook-islands-sms-guidelines
  content_hash: 8126dafc564f79a57feaf23ed269975dd313593f32fdffafd257e7b326eee511
- url: https://support.telnyx.com/en/articles/6665126-cuba-sms-guidelines
  content_hash: 0a864ac0f39f8b53e5c5656757cf35df264356459a12543a630ee4f6c382e361
- url: https://support.telnyx.com/en/articles/6670750-falkland-islands-sms-guidelines
  content_hash: 83a2f7dce8b6595a695c98cea48f747670881434ac55b122684289f1fb05e65a
- url: https://support.telnyx.com/en/articles/6670819-french-polynesia-sms-guidelines
  content_hash: 59cb996358c5f9256383980353d8d586618ea32762e7ce6b46b8d945675835c2
- url: https://support.telnyx.com/en/articles/6670896-grenada-sms-guidelines
  content_hash: d3a1db447a92e4ef624acd72efc5236ee6d55858aa3dfbf9b1df3f62885740e4
- url: https://support.telnyx.com/en/articles/6674331-haiti-sms-guidelines
  content_hash: f88c516399be51d99254516fc86f0f2e60a9fde78315dbba8c110b85578c5b06
- url: https://support.telnyx.com/en/articles/6674453-israel-sms-guidelines
  content_hash: 98b8c5555bded763d530720ea314b08cef4bdcce4b1dab277da7e40e2176cbef
- url: https://support.telnyx.com/en/articles/6674794-kyrgyzstan-sms-guidelines
  content_hash: 0999adeb94b471f02918e5904dce84b1ea47c19dc7ee8f61fac7e267553ca6b2
- url: https://support.telnyx.com/en/articles/6674807-lebanon-sms-guidelines
  content_hash: b7264aecdf7922276b41d0e8efad1fef5f37271f2bd70d3fd489f5f6a54c19a2
- url: https://support.telnyx.com/en/articles/6674989-libya-sms-guidelines
  content_hash: aa8bca060689ffc83d493fd30fa3b7a1deb5294ad4f510a81388574f1c7067a5
- url: https://support.telnyx.com/en/articles/6675252-malta-sms-guidelines
  content_hash: 3b4044f946c12ced7c3041b3277beddec61d8eb40fd9a4d3b5e40f0db5a4eb24
- url: https://support.telnyx.com/en/articles/6675683-martinique-sms-guidelines
  content_hash: 0878da00bfafbc684b2955cb5b515d9dafb909692612798477e07da0c2f14ebe
- url: https://support.telnyx.com/en/articles/6677919-mauritius-sms-guidelines
  content_hash: 0904650f947ddbe919483d7ffe122dc297baefe7e712e61eb6d6b27fb4c3caf3
- url: https://support.telnyx.com/en/articles/6678010-myanmar-sms-guidelines
  content_hash: 3cf14a1aa3f4752a7927b5ea8fdb2a74fb97f53b59a8b0d6125ff840e520f713
- url: https://support.telnyx.com/en/articles/6679129-norfolk-island-sms-guidelines
  content_hash: e89dda466b23b0087bf977276a3c2072c05c95b38aa8c79269590f6a084ebae5
- url: https://support.telnyx.com/en/articles/6679378-reunion-sms-guidelines
  content_hash: 7763801ca7ad359a14ebaf91fac3d473b1974411d31d9f163d257e33b7606b58
- url: https://support.telnyx.com/en/articles/6679451-samoa-sms-guidelines
  content_hash: 76baa49b4c36b91df82c939b795054c686adb424c59d346e35b7a615cf5288ff
- url: https://support.telnyx.com/en/articles/6680225-sudan-sms-guidelines
  content_hash: 3dffe65eedb3f1e6a6602fd3f23d5f0fef07b2f5a2651925a1db1cd1d4ceae0d
- url: https://support.telnyx.com/en/articles/6683365-tonga-sms-guidelines
  content_hash: 0e5562dc98b56a7cfab017860b7627b1394aba239ec26f706747b51f682e37a3
- url: https://support.telnyx.com/en/articles/6683429-tuvalu-sms-guidelines
  content_hash: 1447e818b0cafddda17fea55f6fa0b7b561afc15db491d3a6eed253ac96669d0
- url: https://support.telnyx.com/en/articles/6683454-uzbekistan-sms-guidelines
  content_hash: eda2b8125fdd5081ecf67b75b152464b8409d3c6a666ff3ade146429a01c203a
- url: https://support.telnyx.com/en/articles/6683459-vanuatu-sms-guidelines
  content_hash: b0b3da2921ac14f09b4d25d06cba82ca6fafc7fad448c3e86bb4dfab2889c85e
- url: https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide
  content_hash: 7ff582281f0bb7742fd78a12a5f1d231fdaff3e70cefb7998ac1de57f2c6300e
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
  content_hash: c6ee2679dd6f9407cfe582f6b212c4c3769befba629137122308cd6afc733986
- url: https://support.telnyx.com/en/articles/7885470-chiro8000-and-telnyx-integration
  content_hash: 272b0801f6233fa8f29f56c7cc207477331bf34c1a2c76a9a610a77fca474bdf
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
  content_hash: 1a98bc6c235d54d0047e2b330e2929b7869a9aef146400268514ca1bb87c1bdc
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
  content_hash: 37bd2be6cb5a6cf38fda259fdca19f9f733e0ea175c6ab4075827093f05f7855
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
  content_hash: 33f2a911f356445a83cfd50c5edc338ef9247777c8cbf29a8763ed2b29a74989
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
  content_hash: faf4e4dff1d59b5a6ec71ee7ff42f4f82ff35a41496adaceba3973a6609917d8
- url: https://support.telnyx.com/en/articles/8520014-qatar-did-requirements
  content_hash: 53740a164c1b44ab636d76568e074a829d0906f3b22e8e45656ed92808ad158a
- url: https://support.telnyx.com/en/collections/12044103-regulatory
  content_hash: 9cab461336fff010e61f86955de030a18ceca14ff09a62d71f2b53d3b18ff467
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
  content_hash: 0c6a3da6f44d6f425635270dfe48f84c31596b2c32804541f606c7c95ae73af6
- url: https://support.telnyx.com/en/collections/133103-telnyx-sms-guide
  content_hash: afba3278874edb03b7d54995fcbaef17cfa7750fb91550dd9282c163cb64005c
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
  content_hash: cc2a5003580a55972312e66f093b91bcaee45eda919fc9208e24d6f7cb8c7c87
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
  content_hash: efacf8e7fda375899eceabcc3b12714752c0a20ae983839e24f39a717c7a82f9
- url: https://support.telnyx.com/en/collections/3968237-telnyx-sip-trunking-configurations
  content_hash: c6d19a2e5bf33fb9b470fbd4439911db6d17c890018cbeb37c1fab4c88c9247f
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
  content_hash: e9b768658ebd30eae67e93aff27a13d8d4c8ec132a48ac83ae50ffbe834c71e0
updated_at: 2026-06-11T11:48:37Z
---

# Telnyx Platform Guide

*Part 3 of 4 — see also: [Part 1](telnyx-platform-guide--part-1.md), [Part 2](telnyx-platform-guide--part-2.md), [Part 4](telnyx-platform-guide--part-4.md)*

A comprehensive reference for the Telnyx communications platform, covering account management, SIP trunking, voice calling, phone number provisioning and porting, messaging, webhooks, device configuration, regulatory compliance, and troubleshooting — synthesised from official Telnyx documentation.

## Messaging

### SMS Traffic Types

- **A2P (Application-to-Person)** — Used for domestic messaging and one-way campaigns. Does not support international messaging.
- **P2P (Person-to-Person)** — Ideal for two-way communication; supports international messaging.

### Alphanumeric Sender IDs

Alphanumeric Sender ID handling varies by destination. Some countries maintain the ID without registration, some require registration, and some overwrite it to ensure delivery. Registration requires Level 2 account verification. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for registration requests.

### Country-Specific SMS Guidelines

Guidelines vary significantly:

- **US/Canada (10DLC):** Must register brands and campaigns with the Campaign Registry.
- **Philippines:** Alphanumeric registration required; generic alpha Sender IDs not allowed.
- **Israel:** No registration required; religious, gambling, political, or adult traffic prohibited.
- **Mauritius:** Supported except toward Orange Mauritius; religious, political, or adult traffic prohibited.
- **South Africa:** All alphanumeric Sender IDs overwritten to random local long code.
- **Cuba:** Registration required; up to 6 months provisioning time; mixed letter-number Sender IDs not supported.
- **Bhutan, Lebanon, Libya, Myanmar, Uzbekistan:** Registration required; messages from unregistered IDs rejected.

### MMS

MMS is currently supported within the US and Canada only. Key details:

- Supported file types: text/plain, text/vcard, image/jpeg, image/png, image/gif, video/3gpp, video/mp4.
- Maximum single attachment: 1 MB (ideally 900 KB for encoding overhead).
- Maximum total message: 1 MB with up to 10 media URLs.
- **MMS Fallback** — Automatically converts MMS to SMS with media URLs listed in the body if the destination doesn't support MMS.
- **MMS Transcoding** — Resizes images/videos to meet carrier size requirements; animated GIFs are not resized.
- Toll-free MMS rate limit: 1,200 messages/minute.
- Account-wide messaging rate: 15 messages/second.
- Media files cached for 1 hour; change the URL to invalidate cache.
- To secure media, whitelist IPs 192.76.120.192 and 192.76.120.193.

### Acceptable Use Policy

Prohibited content and behaviors include:

- Sending unsolicited messages (valid opt-in required; purchased lists don't qualify).
- Inappropriate content (sexual, firearms, alcohol/tobacco/drugs, high-risk financial, gambling, etc.).
- Not honouring unsubscribe requests (STOP/UNSUBSCRIBE; must remove within 24 hours).
- High-frequency messaging (no more than 10 messages to a recipient in 24 hours without two-way communication or explicit opt-in).
- Misrepresenting identity (spoofing).
- Fraud or phishing.

Customers must comply with CAN-SPAM (US), CASL (Canada), and CTIA Messaging Principles.

## Webhooks

Webhooks deliver real-time event data. Requirements:

- A publicly accessible HTTP server (HTTPS recommended).
- Return a `2xx` status code to acknowledge receipt.
- Timeout threshold: 2,000 milliseconds; failed deliveries are retried once.
- Configure a failover URL as backup.

### Webhook Signing

Telnyx signs webhook events using public key encryption (API v2). The public key is available in the portal under **Account Settings → Keys & Credentials → Public Key**. Verify signatures using the `telnyx-signature-ed25519` and `telnyx-timestamp` headers.

### Rotating the Public Key

1. Create an inactive key: `POST /v2/inactive_key`
2. Activate it: `POST /v2/inactive_key/{id}/activate`

Only one inactive key can exist per organization. Activation takes up to 60 minutes to propagate; both old and new keys may be active during this period.

### CA Error

If webhooks fail with a certificate authority error and traffic goes to the failover URL, your server's SSL certificate must be signed by a known CA, or use HTTP instead of HTTPS.

## Device & PBX Configuration

### Grandstream UMC6202 (IP Auth)

1. Log into the web UI (default password: `admin` or printed on the unit sticker).
2. Add a SIP trunk pointing to `192.76.120.10`.
3. Create inbound routes with patterns directing to extensions.
4. Create outbound routes with privilege levels matching your Telnyx outbound profile.
5. Configure outbound caller ID (capitals, no special characters, max 15 characters for Canadian providers).

### Yealink T Series (Credentials)

Configure via keypad or web interface. Enter the Telnyx credentials-based connection username and password. Set the SIP server to `sip.telnyx.com`.

### Polycom VVX 300-series (IP Auth)

1. Access the web UI (default password: `456`).
2. Configure NTP settings.
3. Under Lines, set the server address to your Telnyx SIP server, port 5060, UDP transport.

### Ubiquiti UniFi Talk (Credentials Auth)

1. Add a third-party SIP provider in Talk settings with custom fields: proxy, realm, username, password, register, sip_cid_type, retry_seconds, expire-seconds.
2. Import DIDs in E.164 format (with `+` prefix).
3. Add IP address range `192.76.120.10/32`.
4. Assign numbers to users.

### NCH Express Talk

Configure via **File → Options → Lines**: set server to `sip.telnyx.com`, enter SIP account credentials.

## SIM Cards

1. Order a SIM from Telnyx and register it at the [SIM registration page](https://portal.telnyx.com/#/app/wireless/register-sims).
2. Insert into device and configure APN: Name `Telnyx`, APN `data00.telnyx`.
3. Enable data roaming.
4. Reboot the device if needed.

## Billing & Pricing

### Rate Sheets and LRN

Call rates are based on the Location Routing Number (LRN), not always the dialled number. Use the Number Lookup tool in the portal to find a number's LRN prefix and determine the correct rate.

### Global Conversational Rate Deck

Rate changes affect origination type classifications (Local, EEA, Non-surcharged, Surcharged), prefixes, and pricing. Notifications are sent 3 days before changes take effect.

- **Local origination** — Call to country X from a number of country X purchased on Telnyx.
- **EEA origination** — Call to EEA country from another EEA number.
- **Non-surcharged** — Call to country X from a number of a predefined country Z.
- **Surcharged** — None of the above apply.

### Canadian LRN Data

Canadian LRN data requires regulatory approval from the Canadian Local Number Portability Consortium (CNLPC). Annual fee ~$2,000 USD. Telnyx applies a minimum lookup requirement (~$225/month) on a case-by-case basis.

## Regulatory Compliance

### Texas Mini-TCPA (SB 140)

Effective September 1, 2025, Texas SB 140 expands the state's telemarketing framework to include text messages:

- Text solicitations are now regulated the same as telemarketing calls.
- Quiet hours apply to texts: Mon–Sat 9am–9pm, Sunday 12pm–9pm (recipient's local time).
- Businesses based in Texas or marketing to Texas residents must register with the Texas Secretary of State ($200 filing fee + $10,000 security deposit).
- Failure to register: civil penalties up to $5,000 per violation.
- Expanded private right of action for violations.
- Multiple exemptions apply (former customers, securities brokers, publicly traded corporations, licensed insurance, banks, utilities, newspapers, schools, nonprofits, etc.).

### FCC Requirements

- **SIP 603+** — Standardized notification for analytics-based call blocking.
- **Do-Not-Originate (DNO)** — Requirements effective December 15, 2025.
- **Reassigned Numbers Database** — Tracks permanently disconnected numbers.
- **STIR/SHAKEN** — Telnyx implements STIR/SHAKEN; using numbers you own results in A attestation.
