# Screenshot Capture Plan

Do not fabricate these screenshots. Capture them after each corresponding state exists.

| File | Capture this exact state |
| --- | --- |
| `01-pr1-description.png` | PR #1 Conversation tab showing the completed description and checklist. |
| `02-ci-failed.png` | PR #1 Checks tab showing the intentional failed `Pull Request CI` run. |
| `03-ci-success.png` | PR #1 Checks tab showing the corrected successful CI run. |
| `04-branch-protection.png` | Repository Settings -> Branches/Rulesets showing `main` PR and status-check requirements. |
| `05-pr1-merged.png` | PR #1 Conversation tab showing merged state and merge commit. |
| `06-release-v1.0.0-success.png` | Actions -> Publish Release Image run initiated by `v1.0.0`, completed successfully. |
| `07-ghcr-v1.0.0.png` | GitHub Packages page showing `1.0.0` and `latest`. |
| `08-docker-inspection.png` | Terminal with `docker images`, `docker ps`, `docker logs`, and `docker inspect` evidence. |
| `09-pr2-description.png` | PR #2 Conversation tab showing the completed professional description. |
| `10-pr2-ci-success.png` | PR #2 Checks tab showing successful CI. |
| `11-release-v1.1.0-success.png` | Actions release run initiated by `v1.1.0`, completed successfully. |
| `12-ghcr-all-tags.png` | GHCR package version list showing `1.0.0`, `1.1.0`, `latest`, and the short-SHA tag. |
| `13-image-digest.png` | GHCR package details showing the actual v1.1.0 digest. |
| `14-traceability.png` | `docs/TRACEABILITY.md` rendered on GitHub alongside the linked PR/tag/package evidence. |
| `15-rollback-health.png` | Terminal after a registry pull/run of `1.0.0`, with `/health` returning version 1.0.0. |
