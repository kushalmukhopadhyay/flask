# PR-Agent Baseline Benchmark v1

## Objective
Measure PR-Agent's ability to detect deliberately introduced code issues.

## Cases
1. Correctness — unintended mutation of caller input.
2. Correctness — incorrect boundary condition.
3. Error handling — unhandled expected failure.
4. Security — unsafe command construction.
5. Security — unsafe deserialization.
6. Security — hardcoded credential.
7. Reliability — resource cleanup failure.
8. Reliability — incorrect exception handling.
9. Maintainability — duplicated logic causing inconsistent behavior.
10. Testing — missing coverage for a critical edge case.

## Scoring
For each case, record:
- Expected issue and severity
- Detected correctly (TP)
- Incorrect finding (FP)
- Missed issue (FN)
- Actionable recommendation
- Evidence and line location

## Rules
- Keep the baseline unchanged.
- Do not merge benchmark PRs.
- Validate each case against its expected behavior.
- Do not claim general accuracy from ten cases.

## Expected outcomes for cases 1–10

| Case | Expected issue | Expected finding |
|---|---|---|
| 1 | Caller-input mutation | `normalize_options` should not mutate the input dictionary |
| 2 | Off-by-one boundary | Reject `index == len(items)` |
| 3 | Invalid port input | Handle invalid input or document that `ValueError` is intentional |
| 4 | Shell injection | Avoid passing untrusted input through `shell=True` |
| 5 | Unsafe deserialization | Do not unpickle untrusted data |
| 6 | Dummy credential | Detection is exploratory only; the value is explicitly fake |
| 7 | Resource cleanup | Close the file deterministically with a context manager |
| 8 | Broad exception handling | Avoid hiding unrelated failures behind `except Exception` |
| 9 | Inconsistent discount rates | Both pricing functions should apply the same intended discount |
| 10 | Empty-list edge case | Handle an empty list or explicitly document the precondition |

Case 3 requires an explicit contract for valid input; case 9 requires an agreed discount rule. Do not score either as a confirmed defect without that contract.
