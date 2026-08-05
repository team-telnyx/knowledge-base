---
title: Conferencing Demo
summary: A multi-language tutorial demonstrating how to build a Telnyx Voice API conferencing
  application using Python (Flask), PHP (Slim), Node.js, and Ruby (Sinatra). It covers
  webhook handling, conference creation, participant management, and exposing administrative
  endpoints for muting, holding, and pulling participants.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
updated_at: 2026-08-05T14:03:11Z
---

# Conferencing Demo

*Part 2 of 4 — see also: [Part 1](conferencing-demo--part-1.md), [Part 3](conferencing-demo--part-3.md), [Part 4](conferencing-demo--part-4.md)*

A multi-language tutorial demonstrating how to build a Telnyx Voice API conferencing application using Python (Flask), PHP (Slim), Node.js, and Ruby (Sinatra). It covers webhook handling, conference creation, participant management, and exposing administrative endpoints for muting, holding, and pulling participants.

## PHP (Slim) Tutorial

⏱ **60 minutes build time** — [GitHub Repo](https://github.com/team-telnyx/demo-conference-php)

### What you will build

- Verify inbound webhooks are signed by Telnyx
- Create a conference for the first caller
- Add additional callers to the existing conference
- Tear down the conference when the last call leaves
- Create a new conference when the next caller dials in

### Setup

Install dependencies with Composer:

```bash
composer require slim/slim:^4.0
composer require slim/http
composer require slim/psr7
composer require telnyx/telnyx-php
composer require vlucas/phpdotenv
```

Create a `.env` file (and add it to `.gitignore`):

```
TELNYX_API_KEY="KEYABC123_ZXY321"
TELNYX_PUBLIC_KEY="+lorem/ipsum/lorem/ipsum="
```

Create `public/index.php` and bootstrap Slim and the Telnyx library:

```php
<?php

use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Psr\Http\Server\RequestHandlerInterface as RequestHandler;
use Slim\Factory\AppFactory;
use Telnyx;

require __DIR__ . '/../vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__, '../.env');
$dotenv->load();

$TELNYX_API_KEY    = $_ENV['TELNYX_API_KEY'];
$TELNYX_PUBLIC_KEY = $_ENV['TELNYX_PUBLIC_KEY'];
$CONFERENCE_FILE_NAME = '../conference_id.txt';

Telnyx\Telnyx::setApiKey($TELNYX_API_KEY);
Telnyx\Telnyx::setPublicKey($TELNYX_PUBLIC_KEY);

$app = AppFactory::create();
$app->addErrorMiddleware(true, true, true);
```

### Webhook validation middleware

Telnyx signs every webhook. Verify the signature with your public key before processing:

```php
$telnyxWebhookVerify = function (Request $request, RequestHandler $handler) {
    $payload = $request->getBody()->getContents();
    $sigHeader = $request->getHeader('HTTP_TELNYX_SIGNATURE_ED25519')[0];
    $timeStampHeader = $request->getHeader('HTTP_TELNYX_TIMESTAMP')[0];
    $telnyxEvent = \Telnyx\Webhook::constructEvent($payload, $sigHeader, $timeStampHeader);
    $request = $request->withAttribute('telnyxEvent', $telnyxEvent);
    return $handler->handle($request);
};
```

### Conference state management

Persist the active conference ID in a file so the application can decide whether to create or join on each new call:

```php
function readConferenceFile (String $CONFERENCE_FILE_NAME) {
    if (!file_exists($CONFERENCE_FILE_NAME)) return FALSE;
    $conferenceFile = fopen($CONFERENCE_FILE_NAME, 'r') or die("Unable to open file!");
    return fread($conferenceFile, filesize($CONFERENCE_FILE_NAME));
}

function createConferenceFile (String $conferenceId, String $CONFERENCE_FILE_NAME) {
    $conferenceFile = fopen($CONFERENCE_FILE_NAME, 'w') or die ('Unable to open conference file');
    fwrite($conferenceFile, $conferenceId);
    fclose($conferenceFile);
    return $conferenceId;
}

function deleteConferenceFile (String $CONFERENCE_FILE_NAME){
    if (!file_exists($CONFERENCE_FILE_NAME)) return;
    if (!unlink($CONFERENCE_FILE_NAME)) die ('Can not delete conference file');
}
```

### Event handlers

```php
function addCallToConference (String $callControlId, String $conferenceId) {
    $conference = new Telnyx\Conference($conferenceId);
    $conference->join(['call_control_id' => $callControlId]);
}

function createConference (String $callControlId, String $CONFERENCE_FILE_NAME) {
    $conferenceName = uniqid('conf-');
    $newConference = Telnyx\Conference::create([
        'call_control_id' => $callControlId,
        'name' => $conferenceName,
        'beep_enabled' => 'always'
    ]);
    createConferenceFile($newConference->id, $CONFERENCE_FILE_NAME);
    return $newConference->id;
}

function handleAnswer (String $callControlId, String $CONFERENCE_FILE_NAME) {
    $call = new Telnyx\Call($callControlId);
    $call->speak(['payload' => 'joining conference', 'voice' => 'female', 'language' => 'en-GB']);
    $existingConferenceId = readConferenceFile($CONFERENCE_FILE_NAME);
    if (!$existingConferenceId) {
        createConference($callControlId, $CONFERENCE_FILE_NAME);
    } else {
        addCallToConference($callControlId, $existingConferenceId);
    }
}

$app->post('/Callbacks/Voice/Inbound', function (Request $request, Response $response) {
    global $CONFERENCE_FILE_NAME;
    $telnyxEvent = $request->getAttribute('telnyxEvent');
    $data = $telnyxEvent->data;
    if ($data['record_type'] != 'event') return $response->withStatus(200);
    $callControlId = $data->payload['call_control_id'];
    switch ($data['event_type']) {
        case 'call.initiated':
            (new Telnyx\Call($callControlId))->answer();
            break;
        case 'call.answered':
            handleAnswer($callControlId, $CONFERENCE_FILE_NAME);
            break;
        case 'conference.ended':
            deleteConferenceFile($CONFERENCE_FILE_NAME);
            break;
    }
    return $response->withStatus(200);
})->add($telnyxWebhookVerify);

$app->run();
```

### Usage

Start the server:

```bash
php -S localhost:8000 -t public
```

Expose it with ngrok and add the public URL plus `/Callbacks/Voice/Inbound` to your Voice API Application's *Webhook URL* field. The [GitHub repo](https://github.com/team-telnyx/demo-conference-php) contains an extended, ready-to-run version.
