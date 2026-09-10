# Implementation Evidence

This checklist is updated only with evidence actually produced during the workflow.

## Repository

- Repository: https://github.com/Cheemaboi/student-ml-api
- Main branch: `main`

## Planned Evidence

- Pull Requests: populated after the two real PRs are created.
- CI: a deliberately failed run followed by successful PR CI runs.
- Release: successful tag-triggered v1.0.0 and v1.1.0 workflows.
- Docker: local build, running container, health, predict, inspect, exec, logs, and image/PS output.
- Registry: semantic tags, `latest`, short-SHA tags, and real digests.
- Git: v1.0.0 and v1.1.0 tags.
- Reproducibility and rollback: registry pull and execution without rebuild.
- Traceability: populated in `TRACEABILITY.md` using actual values.

## Branch Protection and Merge Strategy

The intended setting for `main` is a required Pull Request with the `Pull Request CI / test-and-build` status check required before merge. Merge commits are selected to retain branch topology for assessment. The final observed settings are added after GitHub configuration succeeds.
