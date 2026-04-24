---
title: Commands and Resources
summary: The following endpoints can be used with the Voice API applications.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources/index
    content_hash: 18508c5774feb203ad6efa7e9e9a5e79859c4bc9b87b74b6960545e50a62a1e1
updated_at: 2026-04-10T00:00:00Z
---

# Commands and Resources

The following endpoints can be used with the Voice API applications.

## Call

| Endpoint                                                                                                                                                               | Description                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [/v2/calls](https://developers.telnyx.com/api-reference/call-commands/dial)                                                                                                                         | Initiate a new call                                                                                    |
| [/v2/calls/:call\_control\_id/actions/answer](https://developers.telnyx.com/api-reference/call-commands/answer-call)                                                                                | Answer an incoming call                                                                                |
| [/v2/calls/:call\_control\_id/actions/fork\_start](https://developers.telnyx.com/api-reference/call-commands/forking-start)                                                                         | Start a media fork for a call                                                                          |
| [/v2/calls/:call\_control\_id/actions/fork\_stop](https://developers.telnyx.com/api-reference/call-commands/forking-stop)                                                                           | Stop a media fork for a call                                                                           |
| [/v2/calls/:call\_control\_id/actions/hangup](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index#hangup)                             | Terminate a call                                                                                       |
| [/v2/calls/:call\_control\_id/actions/reject](https://developers.telnyx.com/api-reference/call-commands/reject-a-call)                                                                              | Reject an incoming call                                                                                |
| [/v2/calls/:call\_control\_id/actions/transfer](https://developers.telnyx.com/api-reference/call-commands/transfer-call)                                                                            | Transfer a call to another destination                                                                 |
| [/v2/calls/:call\_control\_id/actions/suppression\_start](https://developers.telnyx.com/api-reference/call-commands/noise-suppression-start-beta)                                                   | Start noise suppression for a call                                                                     |
| [/v2/calls/:call\_control\_id/actions/suppression\_stop](https://developers.telnyx.com/api-reference/call-commands/noise-suppression-stop-beta)                                                     | Stop noise suppression for a call                                                                      |
| [/v2/calls/:call\_control\_id/actions/client\_state\_update](https://developers.telnyx.com/api-reference/call-commands/update-client-state)                                                         | Update client state information for a call                                                             |
| [/v2/calls/:call\_control\_id/actions/bridge](https://developers.telnyx.com/api-reference/call-commands/bridge-calls)                                                                               | Bridge a call with another destination                                                                 |
| [/v2/calls/:call\_control\_id/actions/ai\_assistant\_start](https://developers.telnyx.com/api-reference/call-commands/start-ai-assistant)                                                           | Start an AI assistant on the call                                                                      |
| [/v2/calls/:call\_control\_id/actions/ai\_assistant\_stop](https://developers.telnyx.com/api-reference/call-commands/stop-ai-assistant)                                                             | Stop an AI assistant on the call                                                                       |
| [/v2/calls/:call\_control\_id/actions/enqueue](https://developers.telnyx.com/api-reference/call-commands/enqueue-call)                                                                              | Add a call to a queue                                                                                  |
| [/v2/calls/:call\_control\_id/actions/leave\_queue](https://developers.telnyx.com/api-reference/call-commands/remove-call-from-a-queue)                                                             | Remove a call from a queue                                                                             |
| [/v2/calls/:call\_control\_id/actions/gather\_using\_audio](https://developers.telnyx.com/api-reference/call-commands/gather-using-audio)                                                           | Play an audio file on the call until the required DTMF signals are gathered to build interactive menus |
| [/v2/calls/:call\_control\_id/actions/gather\_using\_speak](https://developers.telnyx.com/api-reference/call-commands/gather-using-speak)                                                           | Play a speech on the call until the required DTMF signals are gathered to build interactive menus      |
| [/v2/calls/:call\_control\_id/actions/gather\_using\_ai](https://developers.telnyx.com/api-reference/call-commands/gather-using-ai)                                                                 | Collect request information using AI agent                                                             |
| [/v2/calls/:call\_control\_id/actions/gather\_stop](https://developers.telnyx.com/api-reference/call-commands/gather-stop)                                                                          | Stop an ongoing gather operation                                                                       |
| [/v2/calls/:call\_control\_id/actions/playback\_start](https://developers.telnyx.com/api-reference/call-commands/play-audio-url)                                                                    | Start playing audio to a call                                                                          |
| [/v2/calls/:call\_control\_id/actions/playback\_stop](https://developers.telnyx.com/api-reference/call-commands/stop-audio-playback)                                                                | Stop playing audio to a call                                                                           |
| [/v2/calls/:call\_control\_id/actions/record\_start](https://developers.telnyx.com/api-reference/call-commands/recording-start)                                                                     | Start recording a call                                                                                 |
| [/v2/calls/:call\_control\_id/actions/record\_stop](https://developers.telnyx.com/api-reference/call-commands/recording-stop)                                                                       | Stop recording a call                                                                                  |
| [/v2/calls/:call\_control\_id/actions/record\_pause](https://developers.telnyx.com/api-reference/call-commands/record-pause#record-pause)                                                           | Pause recording a call                                                                                 |
| [/v2/calls/:call\_control\_id/actions/record\_resume](https://developers.telnyx.com/api-reference/call-commands/record-resume#record-resume)                                                        | Resume recording a call                                                                                |
| [/v2/calls/:call\_control\_id/actions/refer](https://developers.telnyx.com/api-reference/call-commands/sip-refer-a-call)                                                                            | Send a SIP REFER request for a call                                                                    |
| [/v2/calls/:call\_control\_id/actions/send\_dtmf](https://developers.telnyx.com/api-reference/call-commands/send-dtmf)                                                                              | Send DTMF tones to a call                                                                              |
| [/v2/calls/:call\_control\_id/actions/send\_sip\_info](https://developers.telnyx.com/api-reference/call-commands/send-sip-info)                                                                     | Send a SIP INFO message for a call                                                                     |
| [/v2/calls/:call\_control\_id/actions/speak](https://developers.telnyx.com/api-reference/call-commands/speak-text)                                                                                  | Speak text to a call                                                                                   |
| [/v2/calls/:call\_control\_id/actions/streaming\_start](https://developers.telnyx.com/api-reference/call-commands/streaming-start)                                                                  | Start media streaming for a call                                                                       |
| [/v2/calls/:call\_control\_id/actions/streaming\_stop](https://developers.telnyx.com/api-reference/call-commands/streaming-stop)                                                                    | Stop media streaming for a call                                                                        |
| [/v2/calls/:call\_control\_id/actions/transcription\_start](https://developers.telnyx.com/api-reference/call-commands/transcription-start)                                                          | Start transcription for a call                                                                         |
| [/v2/calls/:call\_control\_id/actions/transcription\_stop](https://developers.telnyx.com/api-reference/call-commands/transcription-stop)                                                            | Stop transcription for a call                                                                          |
| [/v2/calls/:call\_control\_id/actions/siprec\_start](https://developers.telnyx.com/api-reference/call-commands/siprec-start)                                                                        | Start SIPREC recording for a call                                                                      |
| [/v2/calls/:call\_control\_id/actions/siprec\_stop](https://developers.telnyx.com/api-reference/call-commands/siprec-stop)                                                                          | Stop SIPREC recording for a call                                                                       |
| [/v2/connections/:connection\_id/active\_calls](https://developers.telnyx.com/api-reference/call-information/list-all-active-calls-for-given-connection#list-all-active-calls-for-given-connection) | List all active calls for given connection                                                             |
| [/v2/calls/:call\_control\_id](https://developers.telnyx.com/api-reference/call-information/retrieve-a-call-status#retrieve-a-call-status)                                                          | Retrieve a call status                                                                                 |

## Call events

| Endpoint                                                                       | Description                                     |
| ------------------------------------------------------------------------------ | ----------------------------------------------- |
| [/v2/call\_events](https://developers.telnyx.com/api-reference/debugging/list-call-events#list-call-events) | Provide a list of call events based on a filter |

## Conference

| Endpoint                                                                                                                                                   | Description                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [/v2/conferences](https://developers.telnyx.com/api-reference/conference-commands/list-conferences)                                                                                     | List all conferences                             |
| [/v2/conferences/:id](https://developers.telnyx.com/api-reference/conference-commands/retrieve-a-conference)                                                                            | Get details of a specific conference             |
| [/v2/conferences/:id/participants](https://developers.telnyx.com/api-reference/conference-commands/list-conference-participants)                                                        | List participants in a conference                |
| [/v2/conferences/:id/participants/:participant\_id](https://developers.telnyx.com/api-reference/conference-commands/update-conference-participant)                                      | Update a participant in a conference             |
| [/v2/conferences](https://developers.telnyx.com/api-reference/conference-commands/create-conference)                                                                                    | Create a new conference                          |
| [/v2/conferences/:id/actions/join](https://developers.telnyx.com/api-reference/conference-commands/join-a-conference)                                                                   | Join a call to a conference                      |
| [/v2/conferences/:id/actions/leave](https://developers.telnyx.com/api-reference/conference-commands/leave-a-conference)                                                                 | Remove a call from a conference                  |
| [/v2/conferences/:id/actions/record\_start](https://developers.telnyx.com/api-reference/conference-commands/conference-recording-start)                                                 | Start recording a conference                     |
| [/v2/conferences/:id/actions/record\_stop](https://developers.telnyx.com/api-reference/conference-commands/conference-recording-stop)                                                   | Stop recording a conference                      |
| [/v2/conferences/:id/actions/record\_pause](https://developers.telnyx.com/api-reference/conference-commands/conference-recording-pause)                                                 | Pause recording a conference                     |
| [/v2/conferences/:id/actions/record\_resume](https://developers.telnyx.com/api-reference/conference-commands/conference-recording-resume)                                               | Resume recording a conference                    |
| [/v2/conferences/:id/actions/mute](https://developers.telnyx.com/api-reference/conference-commands/mute-conference-participants)                                                        | Mute all participants in a conference            |
| [/v2/conferences/:id/actions/unmute](https://developers.telnyx.com/api-reference/conference-commands/unmute-conference-participants)                                                    | Unmute all participants in a conference          |
| [/v2/conferences/:id/actions/hold](https://developers.telnyx.com/api-reference/conference-commands/hold-conference-participants#hold-conference-participants)                           | Put all participants on hold in a conference     |
| [/v2/conferences/:id/actions/unhold](https://developers.telnyx.com/api-reference/conference-commands/unhold-conference-participants#unhold-conference-participants)                     | Remove hold for all participants in a conference |
| [/v2/conferences/:id/actions/play](https://developers.telnyx.com/api-reference/conference-commands/play-audio-to-conference-participants)                                               | Play audio to a conference                       |
| [/v2/conferences/:id/actions/speak](https://developers.telnyx.com/api-reference/conference-commands/speak-text-to-conference-participants#speak-text-to-conference-participants)        | Speak text to a conference                       |
| [/v2/conferences/:id/actions/stop](https://developers.telnyx.com/api-reference/conference-commands/stop-audio-being-played-on-the-conference#stop-audio-being-played-on-the-conference) | Stop all ongoing activities in a conference      |
| [/v2/conferences/:id/actions/update](https://developers.telnyx.com/api-reference/conference-commands/update-conference-participant)                                                     | Update conference participant                    |

## Connection

| Endpoint                                                                                                                                                               | Description                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| [/v2/connections/:connection\_id/active\_calls](https://developers.telnyx.com/api-reference/call-information/list-all-active-calls-for-given-connection#list-all-active-calls-for-given-connection) | List active calls for a connection |

## Queue

| Endpoint                                                                                                                                    | Description                      |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| [/v2/queues/:queue\_name](https://developers.telnyx.com/api-reference/queue-commands/retrieve-a-call-from-a-queue#retrieve-a-call-from-a-queue)                          | Get details of a specific queue  |
| [/v2/queues/:queue\_name/calls](https://developers.telnyx.com/api-reference/queue-commands/retrieve-calls-from-a-queue#retrieve-calls-from-a-queue)                      | List calls in a queue            |
| [/v2/queues/:queue\_name/calls/:call\_control\_id](https://developers.telnyx.com/api-reference/queue-commands/retrieve-a-call-from-a-queue#retrieve-a-call-from-a-queue) | Get details of a call in a queue |

## Recording

| Endpoint                                                                       | Description                         |
| ------------------------------------------------------------------------------ | ----------------------------------- |
| [/v2/recordings](https://developers.telnyx.com/api-reference/call-recordings/list-all-call-recordings)      | List all recordings                 |
| [/v2/recordings/:id](https://developers.telnyx.com/api-reference/call-recordings/retrieve-a-call-recording) | Get details of a specific recording |
| [/v2/recordings/:id](https://developers.telnyx.com/api-reference/call-recordings/delete-a-call-recording)   | Delete a recording                  |

## Custom storage

| Endpoint                                                                                                                         | Description                                         |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [/v2/custom\_storage\_credentials](https://developers.telnyx.com/api-reference/call-recordings/create-a-custom-storage-credential)                            | Create custom storage credentials                   |
| /v2/custom\_storage\_credentials                                                                                                 | List all custom storage credentials                 |
| [/v2/custom\_storage\_credentials/:id](https://developers.telnyx.com/api-reference/call-recordings/retrieve-a-stored-credential#retrieve-a-stored-credential) | Get details of a specific custom storage credential |
| [/v2/custom\_storage\_credentials/:id](https://developers.telnyx.com/api-reference/call-recordings/delete-a-stored-credential#delete-a-stored-credential)     | Delete a custom storage credential                  |

## Recording transcription

| Endpoint                                                                                                                                                 | Description                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [/v2/recordings/:recording\_id/transcriptions](https://developers.telnyx.com/api-reference/call-recordings/list-all-recording-transcriptions#list-all-recording-transcriptions)       | List all transcriptions for a recording           |
| [/v2/recordings/:recording\_id/transcriptions/:id](https://developers.telnyx.com/api-reference/call-recordings/retrieve-a-recording-transcription#retrieve-a-recording-transcription) | Get details of a specific recording transcription |
| [/v2/recordings/:recording\_id/transcriptions/:id](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-recording-transcription#delete-a-recording-transcription) | Delete a recording transcription                  |
