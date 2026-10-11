# PR-Agent Baseline Scorecard v1

Source: baseline_run3.md
Commit: d21c93144e6e9a60e0d05783eb327970de5a2310

| Case | Issue | Result | Classification |
|---|---|---|---|
| 1 | Caller-input mutation | Detected | TP |
| 2 | Off-by-one boundary | Detected | TP |
| 3 | Invalid port input | Not detected | Unscored — contract needed |
| 4 | Shell command injection | Detected | TP |
| 5 | Unsafe pickle deserialization | Detected | TP |
| 6 | Dummy hardcoded credential | Not detected | Excluded — intentionally fake |
| 7 | File handle not closed | Detected | TP |
| 8 | Broad exception handling | Not detected | Provisional FN |
| 9 | Inconsistent discount rates | Not detected | Unscored — contract needed |
| 10 | Empty-list edge case | Not detected | Provisional FN |

## Summary
- Confirmed detections: 5
- Confirmed assessable cases: 7
- Observed detection rate: 5/7 = 71.4%
- Provisional false negatives: 2 (Cases 8 and 10)
- Excluded: Case 6
- Unscored: Cases 3 and 9

## Limitations
- Cases 8 and 10 require contract/behavior validation before final FN classification.
- No FP count can be established from the summary alone.
- This is a small, hand-built benchmark—not a general accuracy estimate.
- Do not merge benchmark PRs.
