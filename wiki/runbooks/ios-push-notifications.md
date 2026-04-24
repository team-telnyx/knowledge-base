---
title: iOS Push Notifications
summary: Configure APNS VoIP push certificates and the Telnyx Portal to receive push notifications for incoming calls on iOS.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios/index
    content_hash: 03fdc725c1650b267b3401289cb7bdedb449adac8db652d3a95279cd071495a8
updated_at: 2026-04-10T00:00:00Z
---

# iOS Push Notifications

Configure APNS VoIP push certificates and the Telnyx Portal to receive push notifications for incoming calls on iOS.

## Prerequisites

* A [Telnyx account](https://portal.telnyx.com) with a configured SIP Connection
* An [Apple Developer account](https://developer.apple.com/)
* The Telnyx iOS WebRTC SDK integrated into your application

## Portal setup

### 1. Create a VoIP push certificate

For official Apple documentation, see [Create VoIP Services Certificates](https://developer.apple.com/help/account/certificates/create-voip-services-certificates).

You will need:

* An Apple Developer account
* Your app's Bundle ID
* A Certificate Signing Request (CSR) from your Mac

**Generate the certificate:**

1. Go to [developer.apple.com](https://developer.apple.com/) and sign in.
2. Navigate to **Certificates, Identifiers & Profiles**.
3. Click the **+** button to create a new certificate.
4. Select **VoIP Services Certificate** and click **Continue**.
5. Choose the Bundle ID for your application and click **Continue**.
6. Upload a CSR file from your Mac.

**Generate a CSR** (if you don't have one):

1. Open **Keychain Access** on your Mac.
2. Go to **Keychain Access → Certificate Assistant → Request a Certificate from a Certificate Authority**.
3. Enter your email address, select **Save to disk**, and click **Continue**.

After uploading the CSR, download the generated certificate (usually named `voip_services.cer`) and double-click it to install it in your Keychain.

<Callout type="info">
  A single VoIP Services Certificate works for both APNS sandbox and production environments. You need a separate certificate for each Bundle ID.

### 2. Export cert.pem and key.pem

1. Open **Keychain Access** and search for "VoIP Services".
2. Verify the certificate is installed for your Bundle ID.
3. Right-click the certificate and select **Export**. Save as a `.p12` file (you'll be prompted for a password).
4. Run the following commands to extract the PEM files:

```bash theme={null}
openssl pkcs12 -in PATH_TO_YOUR_P12 -nokeys -out cert.pem -nodes -legacy
openssl pkcs12 -in PATH_TO_YOUR_P12 -nocerts -out key.pem -nodes -legacy
openssl rsa -in key.pem -out key.pem
```

### 3. Create an iOS push credential in the Telnyx Portal

1. Go to [portal.telnyx.com](https://portal.telnyx.com) and log in.
2. Navigate to **API Keys** in the left panel.
3. Select the **Credentials** tab, then click **Add → iOS Credential**.
4. Enter a credential name (using your Bundle ID makes it easy to identify).
5. Paste the full contents of `cert.pem` into the certificate field (include the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` markers).
6. Paste the full contents of `key.pem` into the key field (include the `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----` markers).
7. Click **Add Push Credential** to save.

### 4. Attach the credential to a SIP Connection

1. Navigate to **SIP Connections** in the left panel.
2. Open the SIP Connection you want to configure (or [create a new one](https://developers.telnyx.com/docs/voice/sip-trunking/quickstart)).
3. Select the **WebRTC** tab.
4. In the **iOS** section, select the push credential you created.
5. Save the SIP Connection.

***

## App setup

### Enable push notification capabilities

1. Open your Xcode project.
2. Select your app target in the Project Navigator.
3. Go to **Signing & Capabilities** and click **+ Capability**.
4. Add **Push Notifications**.
5. Add **Background Modes** and enable **Voice over IP**.

### Configure PushKit

Import PushKit and register for VoIP push notifications:

```swift theme={null}
import PushKit

private var pushRegistry = PKPushRegistry(queue: DispatchQueue.main)

func initPushKit() {
    pushRegistry.delegate = self
    pushRegistry.desiredPushTypes = Set([.voIP])
}
```

Implement the `PKPushRegistryDelegate` to capture the device token:

```swift theme={null}
extension AppDelegate: PKPushRegistryDelegate {

    func pushRegistry(_ registry: PKPushRegistry,
                      didUpdate credentials: PKPushCredentials,
                      for type: PKPushType) {
        if type == .voIP {
            let deviceToken = credentials.token.map { String(format: "%02X", $0) }.joined()
            // Store this token — you'll pass it to TelnyxClient on login
        }
    }

    func pushRegistry(_ registry: PKPushRegistry,
                      didReceiveIncomingPushWith payload: PKPushPayload,
                      for type: PKPushType,
                      completion: @escaping () -> Void) {
        if payload.type == .voIP {
            handleVoIPPushNotification(payload: payload)
        }
        completion()
    }
}
```

### Pass the token to the SDK

Include the APNS device token when connecting the `TelnyxClient`:

```swift theme={null}
let txConfig = TxConfig(
    sipUser: sipUser,
    password: password,
    pushDeviceToken: "DEVICE_APNS_TOKEN",
    logLevel: .all
)
```

Or with a JWT token:

```swift theme={null}
let txConfig = TxConfig(
    token: "MY_JWT_TELNYX_TOKEN",
    pushDeviceToken: "DEVICE_APNS_TOKEN",
    logLevel: .all
)
```

### Handle incoming VoIP push notifications

When a push notification arrives, reconnect the client and report the call to CallKit:

```swift theme={null}
func handleVoIPPushNotification(payload: PKPushPayload) {
    guard let metadata = payload.dictionaryPayload["metadata"] as? [String: Any] else { return }

    let callerName = (metadata["caller_name"] as? String) ?? ""
    let callerNumber = (metadata["caller_number"] as? String) ?? ""
    let caller = callerName.isEmpty ? (callerNumber.isEmpty ? "Unknown" : callerNumber) : callerName

    let txConfig = TxConfig(
        sipUser: sipUser,
        password: password,
        pushDeviceToken: "APNS_PUSH_TOKEN"
    )

    try? telnyxClient?.processVoIPNotification(
        txConfig: txConfig,
        serverConfiguration: serverConfig,
        pushMetaData: metadata
    )

    // Report incoming call to CallKit
    let callHandle = CXHandle(type: .generic, value: caller)
    let callUpdate = CXCallUpdate()
    callUpdate.remoteHandle = callHandle
    callUpdate.hasVideo = false

    if let callId = metadata["call_id"] as? String, let uuid = UUID(uuidString: callId) {
        provider.reportNewIncomingCall(with: uuid, update: callUpdate) { error in
            if let error = error {
                print("Failed to report incoming call: \(error.localizedDescription)")
            }
        }
    }
}
```

<Callout type="warning">
  On iOS 13.0 and later, you **must** report incoming VoIP push notifications to CallKit. If you fail to do so, the system will terminate your app. See [Apple's documentation](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/2875784-pushregistry) for details.

### Disable push notifications

To disable push notifications for the current user:

```swift theme={null}
telnyxClient.disablePushNotifications()
```

Signing back in with the same credentials re-enables push notifications.

***

## Troubleshooting

### VoIP certificate issues

* Verify your VoIP Services Certificate is not expired.
* Ensure the certificate matches the Bundle ID used in your app.
* For different Bundle IDs (e.g., `com.myapp.dev` vs `com.myapp`), create separate certificates.

### Push token not passed to login

Check that the APNS device token is captured in `pushRegistry(_:didUpdate:for:)` and included in `TxConfig` when calling `connect()`.

### Wrong credential on the SIP Connection

In the Telnyx Portal, open your SIP Connection → **WebRTC** tab → **iOS** section and verify the correct credential is selected.

### APNS environment mismatch

* **Debug builds** (Xcode): Use sandbox environment — set `pushEnvironment` to `sandbox` in `TxConfig`.
* **Release builds / TestFlight**: Use production environment — set `pushEnvironment` to `production`.
* Ensure the APNS environment matches your build signing profile.

### Testing push delivery

The SDK repository includes a testing tool in the `push-notification-tool/` directory:

```bash theme={null}
cd push-notification-tool
npm install
npm run dev
```

You'll need your device token, Bundle ID, `cert.pem`, `key.pem`, and the target APNS environment (sandbox or production).

Common error responses from the tool:

* **BadDeviceToken**: Token is invalid or expired
* **BadCertificate**: Certificate files are invalid or expired
* **BadTopic**: Bundle ID doesn't match certificate
* **TopicDisallowed**: Certificate doesn't have VoIP permissions

## Next steps

* [Push notifications overview](push-notifications-overview.md) — Multidevice support and architecture
* [iOS SDK reference](https://developers.telnyx.com/development/webrtc/ios-sdk) — Full SDK documentation
* [Mobile Push Credentials API](/api/webrtc/mobile-push-credentials) — Manage credentials programmatically


## Related Pages

- [iOS Push Notification Setup](../reference/ios-push-notification-setup.md)
- [Android Push Notifications](../runbooks/android-push-notifications.md)
- [Flutter Push Notifications](../runbooks/flutter-push-notifications.md)
- [React Native Push Notifications](../runbooks/react-native-push-notifications.md)
- [Data Usage Notifications](../runbooks/data-usage-notifications.md)
