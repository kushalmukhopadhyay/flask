# PR-Agent Baseline Results — Run 1

PR: https://github.com/kushalmukhopadhyay/flask/pull/2
Commit: 576e4fa2
Run status: Partial / incomplete

| Case | Expected issue | Detected | Notes |
|---|---|---|---|
| 2 | Off-by-one boundary bug | Yes | Correct finding |
| 4 | Shell command injection | Yes | Correct finding |
| 5 | Unsafe pickle deserialization | Yes | Correct finding |
| 6 | Hardcoded dummy credential | No | Detection is ambiguous because value is explicitly fake |
| 7 | File handle not closed | No | Potential resource-management finding |

Do not calculate definitive precision/recall from this partial run.
