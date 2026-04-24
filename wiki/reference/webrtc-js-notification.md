---
title: WebRTC JS Notification
summary: An event dispatched by Telnyx to notify the client of changes to the session or call.
sources:
  - url: https://developers.telnyx.com/development/webrtc/js-sdk/interfaces/inotification/index
    content_hash: 11e2e10f6d8ba5f0422a54d332675d820e4bfe124267381ef449953f771feffe
updated_at: 2026-04-10T00:00:00Z
---

# WebRTC JS Notification

An event dispatched by Telnyx to notify the client of changes to the session or call.

An event dispatched by Telnyx to notify the client of changes to the session or call.

The conditions of the event can be identified by the `type` property.

| `type`           | Description                                                  | Additional properties |
| ---------------- | ------------------------------------------------------------ | --------------------- |
| `callUpdate`     | A call has changed state                                     | `call`                |
| `userMediaError` | The browser does not have permission to access media devices | `error`               |

**`Examples`**

Usage with TelnyxRTC Client `.on`:

```js theme={null}
client.on('telnyx.notification', (notification) => {
  if (notification.type === 'callUpdate') {
    console.log(notification.call);

    // Do something with the call and update UI accordingly
  } else if (notification.type === 'userMediaError') {
    console.log(notification.error);

    // Handle the error and update UI accordingly
  }
});
```

### Data structure

The notification structure is determined by its `type`.

#### `callUpdate`

```js theme={null}
{
  type: 'callUpdate',
  call: Call // current call
}
```

#### `userMediaError`

```js theme={null}
{
  type: 'userMediaError',
  error: Error
}
```

**`Apialias`**

Notification

## Hierarchy

* `Omit`\<`INotificationEventData`, `"call"`>

  ↳ **`INotification`**

## Table of contents

### Properties

* [call](#call)
* [error](#error)
* [type](#type)

## Properties

### call

• `Optional` **call**: [`Call`](https://github.com/team-telnyx/webrtc/tree/main/packages/js/docs/ts/classes/Call.md)

The current call. Reference this call state to update your UI.
See `Call` documentation.

***

### error

• `Optional` **error**: `Error`

Error from the `userMediaError` event.
Check your `audio` and `video` constraints for browser support.

#### Overrides

Omit.error

***

### type

• **type**: `string`

Identifies the event case.

#### Overrides

Omit.type


## Related Pages

- [WebRTC JS Call Options](../reference/webrtc-js-call-options.md)
- [WebRTC JS Client Options](../reference/webrtc-js-client-options.md)
- [WebRTC JS Call](../reference/webrtc-js-call.md)
- [WebRTC Stats](../reference/webrtc-stats.md)
- [WebRTC Stats](../reference/webrtc-stats-2.md)
