# Configure blind transfer confirmation

> **Draft for release review:** Publish only after the transfer-confirmation behavior and portal availability have been verified for the release. The behavior described below is not a statement of availability in every environment.

A blind transfer sends a caller to another destination without speaking to that destination first. **Confirm blind transfer** lets you wait for the transfer destination to answer before Telnyx reports that the transfer succeeded.

## Before you begin

You need access to edit the SIP connection used by your phone system. Your phone system must support blind transfers using SIP REFER.

## Enable or disable confirmation

1. In the **Telnyx Mission Control Portal**, open the SIP connection you want to edit.
2. Open **Configuration** and scroll to **Advanced**.
3. Find **Confirm blind transfer**.
4. Select the checkbox to enable confirmation, or clear it to disable confirmation.
5. Save your changes, then reopen the connection to confirm that the checkbox still shows your selection.

![Advanced settings showing the Confirm blind transfer checkbox unchecked](assets/confirm-blind-transfer-advanced-settings.png)

The screenshot shows the location of the setting with confirmation **disabled**.

## What changes

| What happens | Selected: confirmation enabled | Cleared: confirmation disabled |
| --- | --- | --- |
| While the destination rings | The original call stays connected while Telnyx waits for the result. | Telnyx reports success immediately and releases the person making the transfer. The caller stays on the line while the destination rings. |
| The destination answers | The caller connects to the destination, and the person making the transfer leaves the call. | The caller connects to the destination. |
| The destination rejects the call as busy | Telnyx reports the rejection and keeps the original call connected. | The person making the transfer has already left the call. The remaining caller is disconnected when the destination rejects the transfer. |

Enable confirmation when you want to keep the original call connected if the destination rejects the transfer. With confirmation disabled, an immediate success report does not mean the destination answered.

With confirmation enabled, ringing or early audio alone does not mean the transfer succeeded. An automated service or voicemail can answer a call; confirmation does not distinguish those answers from a person answering.

This option does not turn a blind transfer into an attended transfer, where you speak to the destination before transferring the caller.

## Test the setting

After saving, place a new test call and perform a blind transfer from your phone system. Test both a destination that answers and one that rejects the call. Confirm that your phone system handles each result as expected.

With confirmation enabled, check that a rejected transfer leaves you connected to the original caller. With confirmation disabled, expect the person making the transfer to leave the call before the destination answers; rejection then disconnects the remaining caller.

Saving the checkbox confirms the connection preference, not the outcome of a call. Your phone system also needs to handle the transfer result correctly.

## If you cannot find the setting

Make sure you are viewing the SIP connection's **Configuration** section, under **Advanced**. If **Confirm blind transfer** is not shown, contact Telnyx Support to check availability for your account.
