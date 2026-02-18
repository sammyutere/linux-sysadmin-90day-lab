# Incident Timeline — Day 28

## Preconditions
- node_exporter active
- Alert pipeline validated
- Automation verified
- Snapshot taken

## Timeline (UTC)

T0 — Service stopped manually  
T1 — Alert entered pending  
T2 — Alert firing  
T3 — Alertmanager delivered webhook  
T4 — Automation executed restart  
T5 — node_exporter active again  
T6 — Alert resolved  

## Detection Latency
T2 - T0

## Remediation Latency
T5 - T2

## Total Incident Duration
T6 - T0

## Root Cause
Intentional service stop (failure injection).

## Contributing Factors
None (controlled drill).

## Observations
- Alert delay governed by `for:` window.
- Automation executed immediately.
- No duplicate pages observed.

## Improvements
- Add retry logic.
- Add structured JSON audit logs.
- Add health verification before restart.

