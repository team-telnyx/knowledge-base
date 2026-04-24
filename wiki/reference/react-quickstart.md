---
title: React quickstart
summary: Get started with the Telnyx React SDK for building WebRTC voice applications in React.
sources:
  - url: https://developers.telnyx.com/development/webrtc/react-sdk/index
    content_hash: f5da6a628e4ba6c1b3deb273070ea6e2d51994e3b856484e35b8aa6830518125
updated_at: 2026-04-10T00:00:00Z
---

# React quickstart

Get started with the Telnyx React SDK for building WebRTC voice applications in React.

The React SDK can be added to your application by installing the npm packages:

```bash theme={null}
npm install --save @telnyx/react-client @telnyx/webrtc
```

## Client initialization

In the `TelnyxRTCProvider` component, you can pass credentials and options objects with custom ringtones:

```jsx theme={null}
// App.jsx
import { TelnyxRTCProvider } from '@telnyx/react-client';

function App() {
  const credential = {
    login_token: 'mytoken',
  };

  const options = {
    ringtoneFile: "./ringtone.mp3",
    ringbackFile: "./ringback.mp3",
  };

  return (
    <TelnyxRTCProvider credential={credential} options={options}>

  );
}
```

## Phone component

In the `Phone` component, you would subscribe to the notifications from the WebRTC client, specify callbacks for Telnyx client event handlers, and define an Audio element.

First import the React client:

```jsx theme={null}
import { useNotification, Audio, useCallbacks } from "@telnyx/react-client";
```

Define a `Phone` function component where you will manage event handlers using callbacks and control audio stream in the `` element:

```jsx theme={null}
const Phone = () => {
  const notification = useNotification();
  const activeCall = notification && notification.call;

  useCallbacks({
    onReady: (status) => {
      console.log("WebRTC client ready");
      console.log(status);
    },
    onError: (error) => {
      console.log("WebRTC client error");
      console.error(error);
    },
    onSocketError: (error) => {
      console.log("WebRTC client socket error");
      console.error(error);
    },
    onSocketClose: () => {
      console.log("WebRTC client socket closed");
    },
    onNotification: (message) => {
      console.log("WebRTC client notification:", message);
      if (message.type === "callUpdate") {
        const call = message.call;
        console.log("Call state:", call.state);
      }
    },
  });

  return (
    <div>
      <Audio stream={activeCall && activeCall.remoteStream} />
    </div>
  );
};
```

## Sample React app

Check out our [sample React application](https://github.com/team-telnyx/webrtc-examples/tree/main/react-client/react-app) for a full implementation of the Telnyx Voice SDK with React components.


## Related Pages

- [Telnyx CLI Quickstart](../reference/telnyx-cli-quickstart.md)
- [JavaScript quickstart](../reference/javascript-quickstart.md)
- [Inference API Quickstart](../tutorial/inference-api-quickstart.md)
- [Number Reputation Quickstart](../tutorial/number-reputation-quickstart.md)
- [Voice Assistant Quickstart](../runbooks/voice-assistant-quickstart.md)
