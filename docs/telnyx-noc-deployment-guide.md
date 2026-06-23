# Telnyx NOC deployment guide for bots

This guide exists because merging source code or handbook content to `main` is usually **not** the same as publishing it. Most NOC services build an image in the app repository, then require a separate deploy-repository bump in `team-telnyx/deploy-noc-main`, and some deploys create a generated follow-up PR that also must be merged.

If you are an AI agent or bot, do not stop after the source PR merge. Follow the whole chain and verify the live service.

## Repositories involved

- Source repositories live under `team-telnyx/*`, for example:
  - `team-telnyx/noc-handbook`
  - `team-telnyx/noc-ticket-analytics`
- Deployment repository:
  - `team-telnyx/deploy-noc-main`
- The deploy repo contains per-service folders such as:
  - `noc-handbook/`
  - `noc-ticket-analytics/`

## Standard deployment model

1. Merge the source-code/content PR in the app repository.
2. Wait for the app repository image workflow on `main` to finish successfully.
3. Extract the exact image tag from the successful image workflow.
4. Open a deploy-repo PR in `team-telnyx/deploy-noc-main` that updates the relevant `meta-*.yml` and any service-specific image references.
5. Wait for deploy-repo PR checks.
6. Merge the deploy-repo PR.
7. Watch the deploy workflow on `deploy-noc-main` for the merge commit.
8. Check for a bot-generated PR such as `chore: production changes detected in <service>`.
9. If the generated PR has the expected diff, merge it too.
10. Watch the final prod deploy workflow.
11. Verify the live URL or behavior that the original change was supposed to affect.

Skipping steps 8-11 is the common failure mode. The deploy repo can be merged while the live app is still serving the old base manifest.

## Required pre-flight checks

```bash
gh auth status
gh repo view team-telnyx/deploy-noc-main
```

Before editing any repo:

```bash
git fetch origin --prune
git checkout main
git reset --hard origin/main
git status --short --branch
```

If the app repo has bot handoff files such as `CLAUDE.md`, `AGENTS.md`, `.llm-repo-instructions`, or repo-local `.hermes/` plans, read them before touching deployment. They may contain service-specific deploy gotchas.

## Finding the image tag

List recent app-repo runs:

```bash
gh api 'repos/team-telnyx/<app-repo>/actions/runs?branch=main&event=push&per_page=5' \
  --jq '.workflow_runs[] | [.id,.head_sha,.conclusion,.created_at,.html_url] | @tsv'
```

Inspect the latest successful run logs for the image tag:

```bash
gh run view <run_id> --repo team-telnyx/<app-repo> --log | egrep -i 'image|tag|digest|service_version|promote|prod|registry' | tail -150
```

For NOC Handbook, the tag shape is:

```text
registry.internal.telnyx.com/jenkins/noc-handbook:<VERSION>
```

For NOC Ticket Analytics, the tag shape is usually:

```text
registry.internal.telnyx.com/<namespace>/noc-ticket-analytics-oci:<YYYY.MM.DD.HH.MM.sha7>
```

Use the exact tag from the successful workflow. Do not guess or synthesize it.

## Deploy-repo bump PR

Clone/update the deploy repo:

```bash
gh repo clone team-telnyx/deploy-noc-main ~/github/team-telnyx/deploy-noc-main || true
cd ~/github/team-telnyx/deploy-noc-main
git fetch origin --prune
git checkout main
git reset --hard origin/main
git checkout -b chore/deploy-<service>-<tag-or-sha>
```

Edit only the target service folder unless the service-specific docs say otherwise.

### NOC Handbook

Source repo:

```text
team-telnyx/noc-handbook
```

Live URL:

```text
http://noc-handbook.query.prod.telnyx.io
```

The source repo merge builds and pushes the image, but prod stays pinned in `deploy-noc-main` until these files are bumped:

```text
noc-handbook/meta-dev.yml
noc-handbook/meta-prod.yml
```

Update both to the new image ref:

```yaml
image_ref: registry.internal.telnyx.com/jenkins/noc-handbook:<VERSION>
```

Then commit, open, and merge the deploy PR:

```bash
git diff -- noc-handbook/meta-dev.yml noc-handbook/meta-prod.yml
git add noc-handbook/meta-dev.yml noc-handbook/meta-prod.yml
git commit -m "chore: deploy noc-handbook <VERSION>"
git push -u origin HEAD
gh pr create --base main --title "chore: deploy noc-handbook <VERSION>" --body "Bumps noc-handbook dev/prod image refs to <VERSION>."
gh pr checks --watch --interval 10
gh pr merge --squash --delete-branch
```

After merge, watch the `Deploy noc-handbook to prod` workflow:

```bash
gh run list --repo team-telnyx/deploy-noc-main --workflow deploy-noc-handbook-prod.yml --limit 5
gh run watch <run_id> --repo team-telnyx/deploy-noc-main --exit-status
```

Check whether a generated production PR appeared:

```bash
gh pr list --repo team-telnyx/deploy-noc-main --state open \
  --search 'production changes detected in noc-handbook in:title'
```

If one appears, inspect the diff and merge it only if it is the expected generated manifest update for the target image.

Verify the live handbook after workflows finish:

```bash
curl -i http://noc-handbook.query.prod.telnyx.io/health
curl -i http://noc-handbook.query.prod.telnyx.io/<new-or-changed-page>/
```

For a new page, a `200` from the new route is the real proof. A green health check alone only proves that some version of the service is up.

### NOC Ticket Analytics

Source repo:

```text
team-telnyx/noc-ticket-analytics
```

Live URL:

```text
http://noc-ticket-analytics.query.prod.telnyx.io
```

Read `CLAUDE.md` in that repo before deploying. Its key warning: deployment is **three steps, not two**.

After the source PR merge and image build, update both of these in `deploy-noc-main`:

```text
noc-ticket-analytics/meta-prod.yml
noc-ticket-analytics/deployments/k8s/prod/overlays/backend-dc2-prod/noc-extras.yaml
```

The first deploy-repo PR updates worker / beat / migrate images. It does **not** necessarily update the API pod base deployment. The deploy bot should then open:

```text
chore: production changes detected in noc-ticket-analytics
```

Inspect and merge that bot PR too. Until the bot PR updates the base `kubernetes_deploy.yaml`, the API pod can remain on the old image even though your deploy PR merged.

Common command:

```bash
gh pr list --repo team-telnyx/deploy-noc-main --state open \
  --search 'production changes detected in noc-ticket-analytics in:title'
```

`mergeStateStatus` may show `UNSTABLE` because there are no required checks. If the diff is exactly the expected generated manifest bump and `mergeable` is true, merging is normal.

After deploy, verify behavior-specific endpoints, not just `/health`. For dashboard changes, check the exact API/UI symptom that motivated the deploy.

## Watching deploy workflows by commit

After merging a deploy PR:

```bash
git checkout main
git pull --ff-only origin main
MERGE_SHA=$(git rev-parse HEAD)
gh run list --repo team-telnyx/deploy-noc-main --commit "$MERGE_SHA" --limit 20
```

Watch the relevant run:

```bash
gh run watch <run_id> --repo team-telnyx/deploy-noc-main --exit-status
```

If `gh run view` has trouble with reusable workflows, list jobs and retrieve logs through the API:

```bash
gh run view <run_id> --repo team-telnyx/deploy-noc-main --json jobs
gh api repos/team-telnyx/deploy-noc-main/actions/jobs/<job_id>/logs
```

## Generated production PR handling

Generated deploy PRs usually have branches like:

```text
deployments/<service>-prod-patch
```

Rules:

- Always inspect the diff before merging.
- Confirm the target image tag appears in the generated Kubernetes manifests.
- Confirm unrelated services are not changed.
- Merge the generated PR if it is the expected manifest bump.
- Watch the prod deploy workflow that runs after that merge.
- Re-check for additional generated PRs; usually there should be none after the second run.

## Final verification checklist

Before telling the user deployment is done, collect real evidence:

- App repo source PR is merged.
- App repo image workflow on `main` succeeded.
- Exact image tag is recorded.
- Deploy-repo metadata PR is merged.
- Deploy workflow completed successfully.
- Generated production PR, if created, was inspected and merged.
- Final deploy workflow completed successfully.
- Live `/health` responds.
- The specific new page, route, API endpoint, or UI behavior is live.

If any step fails, report the blocker and do not claim deployment completed.
