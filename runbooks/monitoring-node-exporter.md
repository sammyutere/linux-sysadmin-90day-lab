# Monitoring Runbook — node_exporter Metrics Unavailable

## Scope
This runbook covers troubleshooting when Prometheus node_exporter metrics
are unavailable or unreachable from the monitoring host.

Applies to:
- Ubuntu (prod-ubuntu)
- Rocky Linux (infra-rocky)

## Paging Philosophy

Alerts are classified by required human response:

### Page
- Active or imminent user impact
- No automated mitigation available
- Immediate, clear action exists

### Ticket
- Degraded performance without user impact
- Investigation required during business hours

### Info
- State changes or context (e.g., reboot detected)
- No immediate action required

This runbook focuses on PAGE-level alerts only.


---

## Symptom 1 — Metrics endpoint unreachable

## Procedure (Follow in Order)

### Step 1 — Confirm the symptom from the monitoring host
```bash
curl -v http://<node-ip>:9100/metrics
```
### Interpretation
- connection refused → service not listening on 9100 (service down or wrong port)
- connection timed out → firewall/network block (common on Rocky if firewalld rules missing)
- Prometheus text output → metrics healthy

### Step 2 — Check node_exporter service state (on target node)
```bash
systemctl status node_exporter --no-pager
```
### Interpretation
- inactive/failed → restart service (Step 5)
- active (running) → proceed to port check (Step 3)

### Step 3 — Confirm node_exporter is listening on TCP/9100 (on target node)
```bash
sudo ss -lntp | grep -E ':9100|node_exporter' || true
```
### Interpretation
- Listening on *:9100 → proceed to firewall check (Step 4)
- Listening on another port → configuration drift; fix unit ExecStart and restart
- Not listening → restart service (Step 5) and re-check

### Step 4 — Firewall check (Rocky/RHEL-family)
```bash
sudo systemctl is-active firewalld || true
sudo firewall-cmd --list-ports || true
```

### Interpretation
- If firewalld is active and 9100/tcp is missing, allow it:

```bash
sudo firewall-cmd --add-port=9100/tcp --permanent
sudo firewall-cmd --reload
```
- Re-test from the monitoring host after reload.

### Note
- Rocky may show preset: disabled for node_exporter; this is vendor preset policy and does not affect explicit enablement.

### Step 5 — Local verification on the node
```bash
curl -sSf http://localhost:9100/metrics | sed -n '1,10p'
```
### Interpretation
- Works locally but not remotely → firewall/routing issue
- Fails locally → service/binding issue; restart and check logs

### Recovery commands
```bash
sudo systemctl restart node_exporter
sudo ss -lntp | grep ':9100'
sudo journalctl -u node_exporter -n 50 --no-pager
```

## Notification Hygiene (Alert Routing)

Alert routing is based on the `severity` label:

- `severity="page"` → webhook page channel (urgent)
- `severity="ticket"` → webhook ticket channel (non-urgent)
- `severity="info"` → dropped (no notification)

Spam control:
- Alerts are grouped by `alertname` + `instance`
- Repeat notifications are limited via `repeat_interval`
- Inhibition suppresses `ticket/info` when a `page` alert is firing for the same target

## Planned Maintenance & Silences

Silences are used for **planned maintenance only**.
Alerts should never be disabled or deleted.

Guidelines:
- Silence only the specific alert and instance
- Always include a comment
- Always set an explicit end time
- Verify alerts recover after maintenance

Silences are created and audited via the Alertmanager API.
