# Failure Analysis

## Failure 1 - deliberately incorrect health assertion

### Symptom

The `Pull Request CI` run failed after the health test expected `"wrong"` instead of the API's actual `"healthy"` status.

### Root Cause

The assertion was intentionally changed to an invalid expected value to demonstrate that CI blocks an invalid change.

### Evidence

The failed workflow is https://github.com/Cheemaboi/student-ml-api/actions/runs/34472796081.

### Correction

The expected value was restored to `"healthy"` in commit `d7634c3`; the replacement run succeeded.

## Failure 2 - CI test import path

### Symptom

The initial PR CI run failed during test collection with `ModuleNotFoundError: No module named 'app'`.

### Root Cause

The hosted runner did not include the repository root on the import path used by the tests.

### Evidence

The failed workflow is https://github.com/Cheemaboi/student-ml-api/actions/runs/34472709150.

### Correction

Both workflows now run tests as `PYTHONPATH=. pytest`, which resolved collection before the intentional assertion failure and later successful run.
