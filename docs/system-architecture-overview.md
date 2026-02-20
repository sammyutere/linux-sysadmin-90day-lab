# Linux Monitoring & Reliability Lab — Architecture Overview

## Infrastructure Layer
- VirtualBox
- Vagrant
- prod-ubuntu (10.168.56.10)
- infra-rocky (10.168.56.20)

## Monitoring Layer
- Prometheus (localhost:9090)
- node_exporter (both nodes)

## Alerting Layer
- Alertmanager (localhost:9093)
- Grouping and inhibition rules

## Automation Layer
- Webhook receiver (host)
- Restart script via vagrant ssh
- Audit logging

## Reliability Controls
- Multi-signal anomaly detection
- SLO-driven change gating
- Snapshot checkpoints

## Recovery Strategy
- VM-level snapshot restore
- Alert-based automated remediation
- Manual override available

## Operational Maturity Demonstrated
- Incident reconstruction
- Error budget awareness
- Deployment gating
- Drift detection and remediation
