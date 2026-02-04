# Root Cause Analysis — infra-rocky Metrics Outage

## Problem Statement
Prometheus could not scrape node_exporter metrics from infra-rocky.

## Symptom
- `curl http://10.168.56.20:9100/metrics` failed from the host
- Alert `NodeExporterDown` fired

## Root Cause
Firewalld on Rocky Linux blocked inbound TCP/9100 by default.

## Contributing Factors
- OS-specific firewall defaults
- Monitoring setup assumed open local network

## Detection
Prometheus alert `NodeExporterDown`

## Corrective Action
Permanently allowed TCP/9100 via firewalld.

## Preventive Action
- Update monitoring runbook with firewall requirement
- Validate firewall rules during setup

