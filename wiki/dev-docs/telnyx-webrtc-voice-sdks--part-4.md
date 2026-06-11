---
title: Telnyx WebRTC Voice SDKs
summary: Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture,
  authentication, push notifications across all platforms, call states, dialing, use
  cases, debugging, and costs.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
  content_hash: 3fedfc040ba32d2fc260b1a579cd1f8ac4753568e8ff8a2992a62e3f40868e8f
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
  content_hash: 37576f7c51e98e804c53c696f71d04a1f423e306cb42ed16c04b94bdce9c7194
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
  content_hash: 42c36618bb0701822e5ea49792d6cc08326c19f09163f9661402976d2af85313
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
  content_hash: a73f480aea535097057ca6c987ba62346ec058988dd0e032c1fb8e89f67ad638
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
  content_hash: a36b6cda308b54ac45a958bb0c47227e939f9cbb33579b5d4751525710f2be46
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
  content_hash: cdd95e464a79746264328e70ea199bf2fff9aa2aad036d53cd27a72e4fecc817
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
  content_hash: 2ca56f8d180406798028958d59f4592bbcdb16c001fed0275c36663b4f85f4f0
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
  content_hash: b87a3806edb676bb6f754a9a871f8bfde50507fff598e77ca7624259d53a0a25
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
  content_hash: f616744b0e7b693486449482bb769ac7c549642a4e62508f710b7821435b7967
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
  content_hash: ab112fd87bff5aee9d8cc7bd8252fd42b4e2f1dce43fd3a6ec95ebba4a288fc8
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/outbound-dialer
  content_hash: 9ef961c8750a0649f790a594d6b1b232f1e5d0e191fccd8f4d8678f237474526
updated_at: 2026-06-11T10:49:57Z
---

# Telnyx WebRTC Voice SDKs

*Part 4 of 4 — see also: [Part 1](telnyx-webrtc-voice-sdks--part-1.md), [Part 2](telnyx-webrtc-voice-sdks--part-2.md), [Part 3](telnyx-webrtc-voice-sdks--part-3.md)*

Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture, authentication, push notifications across all platforms, call states, dialing, use cases, debugging, and costs.

## Push Notification Troubleshooting

### Android Issues

- **FCM token not received:** Verify `Firebase.initializeApp()` is called before requesting the token. Ensure `google-services.json` is in the app module root and the package name matches. Check logs for the token value.
- **Notifications not showing in background:** Verify the background handler is annotated with `@pragma('vm:entry-point')` (Flutter) and registered via `FirebaseMessaging.onBackgroundMessage`. Ensure the Firebase messaging service is declared in the Android manifest.
- **Low-priority notifications:** Create a notification channel with `Importance.max` for incoming call heads-up alerts (Android 8.0+).
- **Wrong push credential on SIP Connection:** In the Portal, open SIP Connection → WebRTC → Android section and verify the correct credential is selected.
- **Invalid push credential:** If the service account JSON is malformed or from the wrong Firebase project, push delivery fails silently. Generate a fresh key from the Firebase Console and update the credential.

### iOS Issues

- **No push notifications:** Confirm the VoIP push certificate matches your Bundle ID and is uploaded to the Telnyx Portal. Verify it is not expired.
- **App terminated on push:** On iOS 13+, you must report every VoIP push to CallKit or the system kills your app.
- **APNS environment mismatch:** Use sandbox for debug builds (set `pushEnvironment` to `sandbox` in `TxConfig`) and production for release/TestFlight. Ensure the APNS environment matches your build signing profile. For different Bundle IDs (e.g., `com.myapp.dev` vs `com.myapp`), create separate certificates.

### General Issues

- **Push works but no call invitation:** The push notification only signals that a call is incoming. Your app must reconnect to the TelnyxClient socket after receiving the push so the actual invitation can be delivered.
- **Multidevice limit:** A user can register up to 5 push tokens. If a 6th is added, the oldest is removed.

### Testing Push Delivery

The SDK repositories include a testing tool in the `push-notification-tool/` directory that sends test push notifications independently of the Telnyx call flow:

```bash
cd push-notification-tool
npm install
npm start   # Android
npm run dev  # iOS
```

For iOS testing, you'll need your device token, Bundle ID, `cert.pem`, `key.pem`, and target APNS environment. Common error responses:

- **BadDeviceToken** — Token is invalid or expired
- **BadCertificate** — Certificate files are invalid or expired
- **BadTopic** — Bundle ID doesn't match certificate
- **TopicDisallowed** — Certificate doesn't have VoIP permissions

If test notifications arrive but calls don't trigger pushes, the issue is in your Portal or SIP Connection configuration rather than the push service itself.

## Costs

WebRTC call legs are billed at **$0.002/minute**. Other voice legs and add-on features are charged separately according to your price plan.

## API Reference

Push credentials can also be managed programmatically through the [Mobile Push Credentials API](https://developers.telnyx.com/api/webrtc/mobile-push-credentials).
