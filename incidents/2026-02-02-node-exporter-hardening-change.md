# Change Record — node_exporter Service Hardening

## Change Description
Add basic systemd hardening and restart policy to node_exporter service.

## Reason for Change
Improve service resilience and reduce impact of unexpected failures.

## Risk Assessment
Low risk. Change affects only service runtime parameters.

## Impact
Monitoring service restart behavior only. No user impact.

## Rollback Plan
Restore previous systemd unit file or revert via snapshot
`pre-node-exporter-hardening`.

## Validation Plan
- node_exporter service active
- metrics endpoint reachable
- Prometheus target remains UP


## Validation Results
- node_exporter service active and restarting correctly
- Metrics endpoint reachable
- Prometheus target remained UP

## Outcome
Change successful. No rollback required.
