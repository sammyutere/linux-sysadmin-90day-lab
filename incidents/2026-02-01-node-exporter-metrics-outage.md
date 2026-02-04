# Postmortem — Node Exporter Metrics Unavailable (infra-rocky)

## Summary
Prometheus was unable to scrape node_exporter metrics from infra-rocky,
triggering a page-level alert. The issue was caused by firewalld blocking
TCP port 9100 on Rocky Linux.

## Impact
- Monitoring visibility for infra-rocky was lost.
- Page-level alert was triggered.
- No user-facing outage occurred.

## Timeline
- T0: Prometheus alert `NodeExporterDown` fired for infra-rocky
- T0+2m: Investigation began
- T0+5m: Service confirmed running; port confirmed listening
- T0+8m: Firewall identified as blocking inbound traffic
- T0+10m: Firewall rule added; metrics restored

## Root Cause
Rocky Linux enables firewalld by default.
TCP port 9100 was not explicitly allowed, preventing inbound access to
node_exporter despite the service running correctly.

## Resolution
Inbound TCP/9100 was permanently allowed via firewalld and rules reloaded.

## What Went Well
- Alerting detected the issue quickly
- Diagnosis followed a structured order (service → port → firewall)
- Resolution was low-risk and immediate

## What Could Be Improved
- Firewall requirements for monitoring services should be documented earlier
- Pre-flight checks could catch missing firewall rules

## Action Items
- Document Rocky Linux firewall requirements in runbooks
- Include firewall verification in monitoring setup checklist

