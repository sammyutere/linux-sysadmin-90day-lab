# CPU Anomaly Detection — Day 25

## Objective
Detect statistically unusual CPU behavior compared to recent baseline.

## Detection Logic
- Current idle CPU compared to 1-hour rolling baseline
- Alert triggers if deviation exceeds 15%
- Sustained for 10 minutes

## Validation
- Generated 10-minute CPU load
- Alert triggered as expected
- No false positives during normal operation

## Assessment
Anomaly detection reduces dependence on static thresholds.

