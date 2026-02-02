## Alerting Stack — Design, Implementation, and Operations
### Purpose
This document describes the alerting stack implemented for the Linux monitoring environment, including:

- alert philosophy (what pages vs what does not)
- alert rule design
- routing and notification hygiene
- failure validation and recovery
- known pitfalls and corrections

The goal of this stack is actionable alerting without noise.

---

### Scope

Applies to:

- Ubuntu (prod-ubuntu)
- Rocky Linux (infra-rocky)
- Prometheus + Alertmanager running on the host via Docker
- Metrics collected via node_exporter

This stack is designed for early-stage production environments where correctness and clarity matter more than scale.

---

### Alerting Philosophy

### Severity Levels

Alerts are classified using a `severity` label:


| Severity | Meaning                        | Human Response               |
| -------- | ------------------------------ | ---------------------------- |
| `page`   | Active or imminent user impact | Immediate response           |
| `ticket` | Degradation without impact     | Business-hours investigation |
| `info`   | Contextual signal              | No action required           |


### Paging Rule of Thumb

An alert should page only if all of the following are true:

- User impact is active or imminent
- No automated remediation exists
- Time-to-detect matters
- There is a clear, immediate action to take

If any of the above are false, the alert should not page.

### Architecture Overview

### Components

- Prometheus
  - Scrapes metrics from Linux nodes
  - Evaluates alert rules

- Alertmanager
  - Receives alerts from Prometheus
  - Routes, groups, inhibits, and deduplicates alerts

- Webhook Receiver
  - Local HTTP endpoint for notifications
  - Used instead of email/Slack to avoid credentials and spam

- Docker Network
  - Prometheus and Alertmanager run on the same Docker network
  - Containers reference each other by name (not `localhost`)

### Key Design Decision

 Prometheus and Alertmanager must not reference `localhost` when running in separate containers.

They communicate via container DNS on a shared Docker network.

---

### Alert Rules

Alert rules are defined in Prometheus and encode operational intent, not just thresholds.

### Page-Level Alerts
- NodeExporterDown
  - Condition: up == 0 for 2 minutes
  - Rationale: exporter absence is a strong proxy for node unreachability
  - Action: investigate node, service, port, firewall
- DiskWillFillSoon
  - Condition: <10% disk free for 10 minutes
  - Rationale: predictive, actionable, time-sensitive
  - Action: cleanup, expand disk, or investigate growth

### Non-Page Alerts
- HighCpuUsage (ticket)
  - Sustained CPU >85% for 15 minutes
  - Informational unless correlated with impact
- NodeRebooted (info)
  - Contextual signal for operators
  - Never pages

---

### Alert Routing & Notification Hygiene

### Routing Strategy

Alertmanager routes alerts by `severity`

| Severity | Receiver         |
| -------- | ---------------- |
| `page`   | `webhook-page`   |
| `ticket` | `webhook-ticket` |
| `info`   | dropped          |

This ensures only page-worthy alerts notify immediately.

### Spam Prevention Controls

The following controls are applied globally:
- group_by: alertname, instance
- group_wait: delay initial notification to batch bursts
- group_interval: prevent frequent regrouping
- repeat_interval: limit repeated notifications

### Inhibition Rules
When a page alert is firing:
- suppress ticket and info alerts for the same alertname + instance
This prevents redundant noise during active incidents.

---

### Notification Mechanism (Webhook)

### Why Webhook (Not Email/Slack)
- avoids credentials in a lab environment
- provides deterministic, inspectable evidence
- mirrors real-world integrations (PagerDuty, OpsGenie, custom tooling)

### Behavior

- Alertmanager sends POST requests to:
  - `/page` for page alerts
  - `/ticket` for ticket alerts
  - Payloads are logged to a file for audit and verification
  - Resolved notifications are enabled (`send_resolved: true`)

---

### Operational Verification

### End-to-End Validation
The alerting stack is validated using a controlled failure drill:

1. Stop `node_exporter` on `infra-rocky`
2. Confirm alert fires in Prometheus
3. Confirm alert is received and routed by Alertmanager
4. Confirm webhook notification is logged
5. Restart service
6. Confirm alert resolves cleanly

### What This Proves

- rules evaluate correctly
- routing logic is correct
- notifications are not dropped or duplicated
- resolution events are handled

---

### Known Pitfalls & Corrections

### Docker `localhost` Misconfiguration
### Symptom
- Alertmanager UI shows “no alerts”
- Prometheus fires alerts but nothing is routed

### Cause
- Prometheus configured with `localhost:9093` while running in a container

### Correction
- Attach Prometheus and Alertmanager to the same Docker network
- Reference Alertmanager by container name (`alertmanager:9093`)

This correction is documented and validated in evidence.

---

### Evidence Captured

The following artifacts prove the alerting stack works as designed:

- Prometheus → Alertmanager connectivity
- Loaded alert rules
- Firing alerts
- Alertmanager routing decisions
- Webhook notification payloads
- Resolved alert behavior

Evidence files are stored under:

```bash
lab/evidence/
```
and referenced in `admin/PROGRESS-LOG.md`.

---

### Snapshot Strategy

Alerting is a baseline capability. Snapshots are taken at milestones:

- `post-alerting-corrected`
  - After Prometheus–Alertmanager wiring fix
- `post-notification-hygiene`
  - After routing, inhibition, and webhook validation

Snapshots preserve known-good operational states and allow safe iteration.

---

### Operational Summary

This alerting stack demonstrates:
- disciplined paging philosophy
- alert rules tied to real failure modes
- noise reduction through routing and inhibition
- validated, end-to-end alert delivery
- documentation suitable for on-call handoff

This is a production-grade foundation, intentionally minimal and extensible.

---

### Recommended Next Evolution
- Add real notification backends (email or SaaS)
- Add alert correlation across multiple nodes
- Introduce SLO-based alerting (burn rate)

---
