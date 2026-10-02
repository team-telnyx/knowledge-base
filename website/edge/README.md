# Support-site routing and rollout

Production is served at `https://support.telnyx.com` by distribution
`E3TMOKZN8HQ7AZ`. Local builds default to a non-indexable preview; the deployment
workflow builds/verifies the public production origin. See ../DEPLOYMENT.md.

## Generated artifacts

`bun run build` writes complete pages to `dist/` and routing artifacts to
`dist-edge/` (never upload this directory as public website content):

- `routes.json`: canonical article/collection paths keyed by numeric Intercom ID.
- `key-value-store.json`: CloudFront KeyValueStore import data (`data`, `key`, `value`).
- `cloudfront-function.js`: JavaScript runtime 2.0 viewer-request function using
  the associated KeyValueStore. Missing entries pass through to the origin;
  store outages remain 503.

`routing.js` is the shared routing implementation used by tests, local HTTP
preview, and the generated CloudFront Function. The older standalone
`homepage-redirect.js` is superseded by this combined handler; do not attach both.

The store keeps the complete routing inventory outside CloudFront Functions'
10 KB code limit. The build fails if generated code exceeds that limit.

## Behavior

- `/en`, `/en/`, `/en/index.html`, `/index.html` → HTTP 301 `/`.
- Bare numeric article/collection IDs, old titles, and trailing slash variants →
  one HTTP 301 to the current canonical URL, on the same host.
- `/en/articles/<slug>.md` and `/en/collections/<slug>.md` → pass through to
  the origin where `.md` files are uploaded alongside HTML, served as
  `text/markdown; charset=utf-8`.
- PR 51 IDs 10646301 → 6339152 and 5617538 → 6339158.
- Previous `/article/en--articles--ID-title`, `/article/ID-title`, and
  `/collection/ID-title` paths resolve by ID. Known former synthetic collection
  paths have explicit mappings. Unmapped paths reach the origin unchanged;
  absent objects return 404 once the origin prerequisites are configured.
- Encoded/repeated query parameters are preserved. Browsers retain fragments
  when following a redirect with no fragment in Location; fragments never reach
  the server. The rendered HTML contains the verified heading/section aliases.
- Unmapped pages reach storage: an uploaded exact-key page returns 200, while
  a missing object returns 404. GET/HEAD supported; others 405.

## Local verification

```sh
bun run build
bun run type-check
bun test
bun run verify
bun run preview:edge
curl -I http://127.0.0.1:4173/en/
curl -I 'http://127.0.0.1:4173/en/articles/10646301-old-title?utm_source=test'
```

The preview serves exact S3 keys behind the actual routing function, without
an SPA fallback that could disguise missing objects. No JavaScript is needed to
read an article, follow collection links, or follow a heading anchor. Search and
filtering progressively enhance the static HTML.

## AWS rollout procedure (requires infrastructure access)

See [Deployment and recovery](../DEPLOYMENT.md) for the bundled initial bootstrap and activation,
automated route synchronization, validation, and rollback procedure.
The workflow owns route **data**. Infrastructure owns the function, store,
association, origin policy, and narrowly scoped deployment-role permissions.
It never installs or changes infrastructure during an article deployment.

Before any future approved public launch, rebuild with the production origin and
explicit indexability setting; that is deliberately outside this branch rollout.

References:

- [CloudFront Functions event/response format](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.html)
- [CloudFront KeyValueStore](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.html)
- [Default root object behavior](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html)

## Origin prerequisites for pages without route registration

This handler no longer decides that a missing route entry means missing content.
The production S3 REST origin must distinguish nonexistent objects from access
failures before this function is activated:

- Grant `s3:ListBucket` on the content bucket to the CloudFront origin identity
  (the existing OAI, or the configured OAC principal if migrated). Preserve
  `s3:GetObject` for the intended content. Do not grant public bucket access.
- Test both GET and HEAD for missing objects: S3 must return 404, not 403.
  Keep genuine permission failures as 403; do not blanket-map 403 to 404.
- Configure a CloudFront custom 404 response using `/404.html` with status 404.
  Remove homepage-body error substitutions for this distribution only.
- Preserve the default root object and prevent public bucket-list requests;
  do not forward S3 listing query parameters to the bucket root.
- Use a short documented error-cache TTL and invalidate stale cached errors
  on deployment, including errors cached before a newly published page existed.
- Publish and associate the generated function; uploading website files alone
  does not activate its revised behavior. The earlier registry-gated handler from closed infra PR #250 is superseded;
  use the generated origin-fallback handler in the dedicated routing change.

Local regression verification must include an uploaded article deliberately
absent from the lookup store (GET 200 / HEAD 200), unknown article/collection/
arbitrary paths (404), existing legacy mappings (301 then 200), and lookup
failure (503). Repeat the same checks on the temporary distribution after rollout.

This change removes the need to register a new canonical article, not the need
for historical redirect data. A stale entry for an existing renamed ID can still
redirect to the prior URL, so coordinate that mapping update with its content
release and retain the old destination until propagation completes. Missing
entries are distinct from an unavailable lookup service: service failures still
return 503 to avoid silently dropping established redirect behavior. This is
not a fully lookup-free architecture.

AWS reference: [S3 GetObject missing-key status and ListBucket permission](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html).
