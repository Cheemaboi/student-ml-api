# Implementation Evidence

This checklist is updated only with evidence actually produced during the workflow.

## Repository

- Repository: https://github.com/Cheemaboi/student-ml-api
- Main branch: `main`

## Pull Requests

- PR #1: https://github.com/Cheemaboi/student-ml-api/pull/1
- PR #2: https://github.com/Cheemaboi/student-ml-api/pull/2

## CI and Releases

- Failed CI: https://github.com/Cheemaboi/student-ml-api/actions/runs/34472796081 (intentional incorrect health assertion)
- Successful PR CI: https://github.com/Cheemaboi/student-ml-api/actions/runs/34472865633 and https://github.com/Cheemaboi/student-ml-api/actions/runs/34473141866
- v1.0.0 release: https://github.com/Cheemaboi/student-ml-api/actions/runs/34472979012
- v1.1.0 release: https://github.com/Cheemaboi/student-ml-api/actions/runs/34473221432

## Docker and Registry

- Local v1.0.0 image build, container run, `/health`, `/predict`, `docker images`, `docker ps`, `docker logs`, `docker inspect`, and `docker exec` were verified.
- Registry pull without rebuild: `ghcr.io/cheemaboi/student-ml-api:1.0.0` was pulled and returned v1.0.0 from `/health`.
- v1.0.0 digest: `sha256:15746b369ef5758285507ed55730da9fc9bc7250ed8b1e856b422a8d0bec3b34`.
- v1.1.0 digest: `sha256:43c95719c702ea8974cd98bc3fa9ccdf6b78d1736bbb6ec6b1af0884d512bc40`.
- Git tags: `v1.0.0`, `v1.1.0`.

## Branch Protection and Merge Strategy

`main` is intended to require a Pull Request with the `Pull Request CI / test-and-build` status check required before merge. Merge commits are selected to retain branch topology for assessment. Repository settings should be captured in the screenshot plan after confirming owner-level branch-protection configuration.
