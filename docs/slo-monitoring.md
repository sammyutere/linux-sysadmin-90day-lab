# Service Level Objective — Monitoring Availability

## Service
Node-level monitoring via Prometheus node_exporter.

## Indicator (SLI)
Percentage of successful scrapes (`up{job="node"}`).

## Objective (SLO)
99.9% availability measured over a rolling 30-day window.

## Error Budget
- 0.1% unavailability
- ≈43 minutes per 30 days

## Alerting Philosophy
- Page only on sustained exporter unavailability.
- Do not page on brief scrape gaps.
- Use error budget consumption to guide change velocity.

## Current Assessment
- Availability within SLO based on observed window.
- Error budget largely unused.

## Actions When Budget Is Burned
- Freeze non-essential changes.
- Investigate reliability regressions.
- Revisit alert sensitivity.

