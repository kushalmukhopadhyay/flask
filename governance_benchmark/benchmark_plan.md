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
