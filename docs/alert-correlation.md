# Alert Correlation — Day 24

## Objective
Reduce duplicate paging and speed root-cause identification.

## Correlation Strategy
- Primary signal: SLO burn-rate alerts
- Secondary signals: exporter availability, disk, resource alerts
- Correlate by node (`instance`) and job

## Inhibition Logic
- Suppress secondary alerts when `SLOBurnRateFast` is firing
- Page only once per node outage

## Outcome
- Single page for sustained outages
- Reduced alert noise during drills
- Faster diagnosis with clear primary signal

## Review Policy
Correlation rules reviewed after major incidents.

