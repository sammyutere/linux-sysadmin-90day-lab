# Alert Tuning — Day 23

## Objective
Reduce false positives while preserving meaningful alerting.

## Changes Made
- Increased `NodeExporterDown` alert duration to 5 minutes.
- Added operator-focused annotations.
- Adjusted burn-rate alert windows to reduce noise.

## Rationale
Short-lived failures observed during drills did not represent
reliability risk and should not trigger paging.

## Outcome
### Alert Behavior Verification
- `NodeExporterDown` remained in `pending` state and did not page during the transient failure.
- `SLOBurnRateFast` transitioned to `firing`, indicating sustained error budget burn and correctly triggering a page-level alert.
- `SLOBurnRateSlow` remained `pending`, as expected for longer-window degradation.

This confirms that alert tuning successfully reduced noise while preserving critical paging on genuine reliability risk.

## Review Policy
Alert behavior should be reviewed after incidents and load tests.

