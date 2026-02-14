# Multi-Signal Anomaly Detection — Day 26

## Objective
Detect systemic degradation using correlated signals.

## Signals Used
- CPU deviation from 1-hour baseline
- Disk utilization > 85%

## Correlation Logic
Alert triggers only when both conditions are sustained for 10 minutes.

## Validation
- Generated disk pressure and CPU load simultaneously.
- Confirmed MultiSignalDegradation alert fired.
- No alert triggered when signals occurred independently.

## Assessment
Correlated anomaly detection reduces false positives and highlights systemic risk.

