---
title: JavaScript quickstart
summary: Get started with the Telnyx JavaScript SDK for WebRTC voice calls in web browsers.
sources:
  - url: https://developers.telnyx.com/development/webrtc/js-sdk/quickstart/index
    content_hash: 02601c8831985d2a91e2dc1e21b88951c6bf28c237f6fe2853eab50281c1c449
updated_at: 2026-04-10T00:00:00Z
---

# JavaScript quickstart

Get started with the Telnyx JavaScript SDK for WebRTC voice calls in web browsers.

The JavaScript SDK can be added to your application in the following ways:

* Installing it using npm package: [https://www.npmjs.com/package/@telnyx/webrtc](https://www.npmjs.com/package/@telnyx/webrtc).
* As a script in your web application using one of the external CDNs:
  * [https://unpkg.com/@telnyx/webrtc](https://unpkg.com/@telnyx/webrtc)
  * [https://cdn.jsdelivr.net/npm/@telnyx/webrtc](https://cdn.jsdelivr.net/npm/@telnyx/webrtc)

Depending on your preferred setup, the client can be initialized using a Node.js backend or via CDN bundle.

## Client initialization

### CDN example

```html theme={null}
<!-- Include the Telnyx WebRTC JS SDK -->
<script
   type="text/javascript"
   src="https://unpkg.com/@telnyx/webrtc@2.9.0/lib/bundle.js">
</script>
```

### Node.js example

```javascript theme={null}
// Initialize the client
const client = new TelnyxRTC({
 // Use a JWT to authenticate (recommended)
 login_token: login_token,
 // or use your connection credentials
   login: username,
   password: password,
});

// Attach event listeners
client
 .on('telnyx.ready', () => console.log('ready to call'))
 .on('telnyx.notification', (notification) => {
   console.log('notification:', notification)
 });
```

With client initialization you can also set custom ringtones setting the following parameters:

| Value          | Description                                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------------- |
| `ringbackFile` | A URL to a wav/mp3 ringback file that will be used when you disable "Generate Ringback Tone" in your SIP connection. |
| `ringtoneFile` | A URL to a wav/mp3 ringtone file.                                                                                    |

## Client authentication

The WebRTC client has two main ways of authentication. You can either use a JSON Web Token (Telnyx access token) or username and password (on-demand credentials).

### Authenticating with a JSON Web Token

```javascript theme={null}
const client = new TelnyxRTC({
 login_token: login_token,
});
```

### Authenticating with username and password credentials

```javascript theme={null}
const client = new TelnyxRTC({
 login: username,
 password: password,
});
```

## Client registration

The `.on` method allows the client to attach the event handler. When the client receives the `telnyx.ready` event, the client is ready to place phone calls.

```javascript theme={null}
const client = new TelnyxRTC(options);

client.on('telnyx.ready', (client) => {
  // Your client is ready!
}).on('telnyx.error', (error) => {
  // Got an error...
})
```

## Call events

When the client is initiated and in a ready state you can observe call events using `telnyx.notification`.

```javascript theme={null}
let activeCall;
client.on('telnyx.notification', (notification) => {
  if (notification.type === 'callUpdate') {
    activeCall = notification.call;
  }
});
```

And send commands to update your call state, for instance to answer an incoming call on the ringing event:

```javascript theme={null}
client.on('telnyx.notification', (notification) => {
  const call = notification.call;

  // Check the type of the notification
  if (notification.type === 'callUpdate' && call.state === 'ringing') {
    // Answer the call as soon as the notification is received.
    call.answer();
  }
});
```

For a full list of call methods, see the [Call class reference](webrtc-js-call.md).

## Call states

You can expect the following call states in `notification.call.state` attribute:

| Value        | Description                                                                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `new`        | New call has been created in the client.                                                                                                            |
| `trying`     | It's attempting to call someone.                                                                                                                    |
| `requesting` | The outbound call is being sent to the server.                                                                                                      |
| `recovering` | The previous call is recovering after the page refreshes. If the user refreshes the page during a call, it will automatically join the latest call. |
| `ringing`    | Someone is attempting to call you.                                                                                                                  |
| `answering`  | You are attempting to answer this inbound call.                                                                                                     |
| `early`      | It receives the media before the call has been answered.                                                                                            |
| `active`     | Call has become active.                                                                                                                             |
| `held`       | Call has been held.                                                                                                                                 |
| `hangup`     | Call has ended.                                                                                                                                     |
| `destroy`    | Call has been destroyed.                                                                                                                            |
| `purge`      | Call has been purged.                                                                                                                               |

## HTML audio element

To hear a voice call in a browser, you need to refer to an audio element in your code:

```javascript theme={null}
client.remoteElement = 'remoteMedia';
```

Pointing to the corresponding HTML element:

```html theme={null}
<audio id="remoteMedia" autoplay="true" />
```

## Sample Vanilla JS app

Check out our [sample Vanilla JavaScript application](https://github.com/team-telnyx/webrtc) for a full implementation of the Telnyx Voice SDK.

## Demo app

We built a [demo app](https://webrtc.telnyx.com/) using the Voice SDK for JavaScript to showcase the power of the SDK. Try it out to see WebRTC voice calls in action.


## Related Pages

- [React quickstart](../reference/react-quickstart.md)
- [Voice Assistant Quickstart](../runbooks/voice-assistant-quickstart.md)
- [Telnyx CLI Quickstart](../reference/telnyx-cli-quickstart.md)
- [JavaScript Video Tutorial](../tutorial/javascript-video-tutorial.md)
