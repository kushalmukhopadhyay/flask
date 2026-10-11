# PR-Agent Baseline — Run 3

PR: https://github.com/kushalmukhopadhyay/flask/pull/2
Commit: d21c93144e6e9a60e0d05783eb327970de5a2310
Run status: Complete
Finding limit: 10

## Findings
- Case 1 — Caller-input mutation: detected
- Case 2 — Off-by-one boundary: detected
- Case 3 — Invalid port input: not detected; contract needed
- Case 4 — Shell command injection: detected
- Case 5 — Unsafe pickle deserialization: detected
- Case 6 — Dummy credential: not detected; intentionally fake
- Case 7 — File handle not closed: detected
- Case 8 — Broad exception handling: not detected
- Case 9 — Inconsistent discount rates: not detected; contract needed
- Case 10 — Empty-list edge case: not detected

## Validation
- Flask test suite: 494 passed in 0.90 seconds
- Duplicate findings were deduplicated by issue and location.
- This small, hand-built benchmark is not a general accuracy estimate.
