# PR-Agent Baseline — Run 2

PR: https://github.com/kushalmukhopadhyay/flask/pull/2
Commit: 16f2f1b69bcc368fc86660f09264aaba7cc9a8d4
Run status: Complete
Finding limit: 10

## Expected fixture issues
- Case 2 — Off-by-one boundary bug: detected
- Case 4 — Shell command injection: detected
- Case 5 — Unsafe pickle deserialization: detected
- Case 6 — Dummy hardcoded credential: not detected; value is explicitly fake
- Case 7 — File handle not closed: detected

## Additional finding
- Caller-input mutation in src/flask/review_example.py: detected

## Caveats
- Persistent review state includes findings from earlier runs.
- Duplicate findings must be deduplicated by issue and location.
- The fake credential is not a real secret.
- This is a small controlled benchmark, not a general accuracy estimate.
