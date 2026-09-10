# Advanced Challenges

## OCI Image Metadata

The Dockerfile defines standard OCI labels for image version, source revision, source repository, and build date. The release workflow passes the real GitHub tag, commit SHA, repository URL, and build timestamp as Docker build arguments. This means a published image can be connected back to the source revision that produced it.

## Commit SHA Image Tags

The release workflow also publishes a short commit-SHA tag. The registry shows `d3baae6` for v1.0.0 and `f8fa1a6` for v1.1.0. These tags improve traceability because they identify the exact source commit in addition to the semantic release version.

## Docker Cache Experiment

The image was built normally first. After changing only `app.py`, Docker showed the dependency installation layer as cached and rebuilt only the application layer. After making a temporary comment-only change to `requirements.txt`, Docker re-ran dependency installation. The temporary changes were removed after testing.

The result shows why the Dockerfile copies `requirements.txt` and installs dependencies before copying application code. Normal application changes can reuse the expensive dependency layer, while dependency changes correctly invalidate it.
