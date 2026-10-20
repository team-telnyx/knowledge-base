# CI/CD operations

## Pull request validation

`Pull request CI` runs on every PR. Its `Required CI` job summarizes the selected
website, support-artifact, and corpus/tooling jobs. An applicable job must finish
successfully; failure, cancellation, missing outputs, and unexpected skips fail
the gate. An unrelated documentation-only PR still produces `Required CI`.

The website job runs deployment unit tests, checks the source manifest, runs Bun
tests and type-checking, and builds/audits both preview and production indexing.
The support job checks deterministic manifest/wiki output, including newly
created files. The corpus job tests the Python tooling and validates committed
wiki Markdown and index targets. Source changes belong under `support-docs/`;
`wiki/` is generated.

### Activate Required CI

The workflow does not configure branch protection. Activate the rule **after**
the validation workflow has landed on `main` and a PR has reported a successful
`Required CI` check. Requiring it before the lower PRs in this stack contain the
workflow would prevent those PRs from landing.

The reviewed payload in `.github/required-ci-ruleset.json` adds a dedicated
main-branch rule requiring `Required CI` from the GitHub Actions integration
(app ID `15368`, verified against this repository's check runs). It requires an
up-to-date base and grants no bypass actors. It leaves existing review rules
untouched.

First inspect existing rules and make sure this named rule has not already been
created:

```sh
gh api repos/team-telnyx/knowledge-base/rulesets \
  --jq '.[] | {id, name, enforcement}'
gh api repos/team-telnyx/knowledge-base/rules/branches/main
```

If the named repository rule is absent, create it once with an administrator's
credentials:

```sh
gh api --method POST repos/team-telnyx/knowledge-base/rulesets \
  --input .github/required-ci-ruleset.json
```

If it already exists, inspect its current definition and update that rule ID
with `PUT /repos/team-telnyx/knowledge-base/rulesets/{rule_id}` using the same
payload rather than creating duplicates. Do not replace the organization's
review rules or the classic branch-protection object.

After activation, read the effective branch rules again. Verify a failing
validation blocks merge and an unrelated documentation PR reports successful
`Required CI`. Refresh existing PR branches so they contain the new workflow.
Repository settings and PR review are separate: the auto-merge workflow remains
in dry-run mode, and the reviewed payload does not enable automatic merging.

## Main deployment ordering

Every push to `main` schedules `Deploy website`. The `deploy-production`
concurrency group covers selection, build, upload, route updates, verification,
and rollback; `cancel-in-progress` remains false. GitHub may replace a pending
run and does not guarantee commit-order scheduling. Therefore the runner checks
out **current `main` after acquiring the lock**, not the triggering event SHA.
A delayed old event reconciles the latest approved tree.

Before AWS mutation, the workflow compares the selected SHA to current remote
`main`. A superseded build exits without publishing; the later main event's run
will select current main. A push arriving during publication queues a successor.
Every main push is eligible, including documentation-only changes, so the
successor is not filtered out. This trades some redundant builds for reliable
latest-state reconciliation. It does not cancel a partly published release.

Normal main changes must use the PR merge path. GitHub suppresses `push` workflows
for pushes made with `GITHUB_TOKEN`; such a push must not be used as an implicit
deployment trigger. If a run fails or is cancelled, or an external process
changes main without triggering Actions, dispatch a reconciliation explicitly:

```sh
gh workflow run deploy-website.yml --repo team-telnyx/knowledge-base --ref main
```

Deployment source SHA is recorded in the job summary and retained release
evidence. Because checkout selects current main, the Actions event SHA alone
is not authoritative for these releases.

## Failure recovery and rollback

Publication uploads content-hashed assets first, then mutable content and HTML,
then synchronizes routes, invalidates CloudFront, and checks live responses.
Production content currently uses stable S3 keys. This is **not an atomic
release switch**: a failed upload or verification can leave mixed content.

Uploads are inside the recovery boundary. On failure, the publisher attempts to
restore the prior routing snapshot and invalidate caches. It records whether
route recovery succeeded and explicitly reports that content was not restored.
Unexpected concurrent route changes are not overwritten. Inspect the job summary
and `release-report/failure.json`; route restoration is not a full rollback.

To restore content and routing together, choose a prior successful
`Deploy website` main run whose artifact contains a verified release and dispatch:

```sh
gh workflow run deploy-website.yml --repo team-telnyx/knowledge-base --ref main \
  -f rollback_run_id=PRIOR_SUCCESSFUL_RUN_ID
```

Rollback downloads generated `dist/` and `dist-edge/` artifacts before any current
content build. It skips Bun installation, generation, website tests/type-checks,
build, and content audit, so broken current content cannot block restoration.
Trusted deployment code still comes from current main; deployment unit tests,
archive validation, AWS account/distribution checks, and live verification still
run. Archived scripts are never executed. A failure in the trusted deployment
code itself must be repaired separately.

The selected archive's source SHA is distinguished from the current execution
code SHA. Older artifacts without a recorded source SHA fall back to their
original workflow event SHA. Artifacts are retained for 90 days; missing,
expired, unsuccessful, or unverified archives cannot be rollback targets.

A successful rollback reuploads the archived content and restores its routes;
it does not remove unrelated retained S3 objects. The next ordinary main release
will reconcile current source again. If a rollback must remain in place, also
revert or repair the source through a reviewed PR before further publication.
Longer-term atomic releases require versioned content roots and a compatible
routing cutover; the current recovery mechanism does not claim that property.

## Generated wiki PRs

Incremental generation maintains individual article projections and their
catalog entries. It preserves synthesized LLMWiki pages; removing a projection
does not recompile references inside the synthesized corpus. The monthly refresh
still performs a full synthesis and opens a separate reviewed PR.

Both generators create PRs with `GITHUB_TOKEN`. Keep the human workflow-approval
step explicit: a maintainer selects **Approve workflows to run** in the PR, waits
for `Required CI`, reviews the generated diff, and then approves/merges the PR.
Workflow approval and PR review approval are separate actions. If GitHub does not
provide the approval banner, inspect Actions for the blocked run; a maintainer
can close and reopen the PR to produce a fresh event using their own identity.
Do not assume a bot-created PR has passed CI because creation succeeded.

An unattended path would require a separately provisioned, narrowly scoped
GitHub App credential and a reviewed rollout. The current changes add no token
or automatic merge behavior.

## Rollout checklist for AITS-787

1. Merge the stack from bottom to top after its checks and reviews pass. Keep the
   generated corpus backfill separate so its content diff is reviewable.
2. Activate and verify `Required CI` only after its workflow is on main.
3. Approve the checks on the next bot-generated PR and confirm the documented
   generated-PR lifecycle works with the repository's Actions settings.
4. Dispatch normal deployment reconciliation. Confirm the recorded source SHA
   matches the selected approved main revision and live verification succeeds.
5. Retain the prior successful release ID, and review failure/recovery evidence.
   Mocked tests exercise rollback and partial uploads; they are not a claim that
   a production rollback drill has been performed.

GitHub references: [concurrency semantics](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency),
[token-triggered workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow),
and [repository rulesets](https://docs.github.com/en/rest/repos/rules#create-a-repository-ruleset).
