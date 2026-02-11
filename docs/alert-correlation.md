# Alert Correlation — Day 24

## Objective
Reduce duplicate paging and speed root-cause identification.

## Correlation Strategy
- Primary signal: SLO burn-rate alerts
- Secondary signals: exporter availability, disk, resource alerts
- Correlate by node (`instance`) and job

## Validation & Evidence

### Alertmanager Evidence (Routing + Per-Instance Evaluation)

- Alertmanager `/api/v2/alerts` shows `SLOBurnRateSlow` active for both node instances:
  `10.168.56.10:9100` and `10.168.56.20:9100`.
- Both alerts routed to `ticket-receiver` as expected for `severity=ticket`.
- Grouping behavior verified via `/api/v2/alerts/groups`.
- Since `instance` is included in `group_by`, alerts are grouped per node.
- No unintended cross-node grouping observed.

## Inhibition Logic
- Suppress secondary alerts when `SLOBurnRateFast` is firing
- Page only once per node outage

## Outcome
- Single page for sustained outages
- Reduced alert noise during drills
- Faster diagnosis with clear primary signal

## Review Policy
Correlation rules reviewed after major incidents.

