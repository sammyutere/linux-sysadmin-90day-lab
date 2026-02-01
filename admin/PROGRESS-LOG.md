# Progress Log — Linux Sysadmin 90-Day Lab

## 2026-01-13 — Day 1 — Lab Bring-up & Verification

### Environment Setup Note
- Vagrantfile resides in `~/linux-labs/vagrant-lab`.
- `VAGRANT_CWD` was set to allow Vagrant commands to be run from the
  documentation repository without changing directories.

**Goal:** Build the Vagrant + VirtualBox lab and verify basic connectivity.

### What I did
- Booted both virtual machines using `vagrant up`.
- Verified SSH access to both nodes.
- Verified IP addresses, kernel version, and operating system details.

### Evidence
- lab/evidence/2026-01-13_day1_baseline.txt

### Verification Checklist
- prod-ubuntu reachable at 10.168.56.10
- infra-rocky reachable at 10.168.56.20

## 2026-01-14 — Day 2 — OS Updates and Baseline Tooling

**Goal:** Patch both systems and install core administration tools.

### What I did
- Updated Ubuntu and Rocky Linux to current patch levels.
- Installed standard Linux administration and troubleshooting tools.
- Installed nginx on Ubuntu for future service labs.
- Installed Ansible and Borg on Rocky for automation and backups.

### Evidence
- lab/evidence/2026-01-14_day2_updates_tools.txt

## 2026-01-15 — Day 3 — SSH Hardening

**Goal:** Secure SSH access using key-based authentication and least privilege.

### What I did
- Backed up SSH daemon configuration on both systems.
- Disabled password-based SSH authentication.
- Disabled direct root login over SSH.
- Restarted SSH services and verified effective configuration.

### Evidence
- lab/evidence/2026-01-15_day3_ssh_hardening.txt

## 2026-01-16 — Day 4 — System Health Checks & Evidence Discipline

**Goal:** Establish a repeatable daily health-check and evidence-capture process.

### What I did
- Defined a standard system health checklist.
- Captured health data from both systems.
- Stored raw command output as versioned evidence.
- Reviewed system state for anomalies.

### Evidence
- lab/evidence/2026-01-16_day4_prod_health.txt
- lab/evidence/2026-01-16_day4_infra_health.txt

## 2026-01-17 — Day 5 — Rebuild Test & Reproducibility

**Goal:** Validate that the lab environment can be rebuilt from configuration alone.

### What I did
- Destroyed both Vagrant-managed virtual machines.
- Rebuilt the lab using `vagrant up`.
- Verified hostnames, IP addresses, and kernel availability.
- Confirmed no undocumented manual steps were required.

### Evidence
- lab/evidence/2026-01-17_day5_rebuild_verification.txt

### SSH Configuration Drift Remediation (Day 6)

**prod-ubuntu (Ubuntu):**
- Detected `PermitRootLogin without-password`.
- Enforced explicit `PermitRootLogin no` in `/etc/ssh/sshd_config`.
- Restarted SSH and verified effective configuration.

**infra-rocky (Rocky Linux):**
- Detected `PasswordAuthentication yes` due to vendor drop-in file.
- Implemented hardened override in `/etc/ssh/sshd_config.d/99-hardening.conf`.
- Restarted SSH and verified effective configuration.

Target state achieved on both systems:
- `PermitRootLogin no`
- `PasswordAuthentication no`

Evidence:
- lab/evidence/2026-01-18_day6_ssh_remediation.txt

### SSH Hardening — Permanent Drift Prevention

- Implemented SSH hardening using `/etc/ssh/sshd_config.d/99-hardening.conf`.
- Enforced `PermitRootLogin no` and `PasswordAuthentication no` as final overrides.
- Avoided modification of vendor-managed configuration files.
- Verified effective runtime configuration on Ubuntu and Rocky Linux.

Evidence:
- lab/evidence/2026-01-18_day6_ssh_permanent_hardening.txt

## 2026-01-18 — Day 6 — Buffer & Remediation

**Goal:** Review, stabilize, and correct any issues from Week 1.

### What I did
- Reviewed lab structure, evidence, and documentation.
- Re-verified system health and SSH hardening.
- Corrected minor documentation issues where needed.
- Confirmed systems were stable and ready for Week 2.

### Evidence
- lab/evidence/2026-01-18_day6_remediation_check.txt

## 2026-01-19 — Day 7 — Week 1 Sign-off & Readiness Check

**Goal:** Formally validate completion of Week 1 and establish readiness baseline.

### What I did
- Verified VM state and system health.
- Confirmed permanent SSH hardening on both systems.
- Captured Week 1 readiness evidence.
- Signed off Week 1 documentation.

### Evidence
- lab/evidence/2026-01-19_week1_readiness.txt

## 2026-01-20 — Day 7(Extended) — Snapshot Checkpoint & Policy

**Goal:** Defind snapshot checkpoints and policy.

### What I did 
- Snapshot Checkpoints Defined
- Defined milestone-based snapshot strategy for Week 2+.
- Documented snapshot policy and naming conventions in root README.
- Clarified snapshots as rollback checkpoints, not rebuild substitutes.


## 2026-01-20 — Day 8 — Monitoring Instrumentation (node_exporter)

### Summary
- Installed node_exporter on prod-ubuntu and infra-rocky.
- Resolved invalid tarball download caused by GitHub "latest" redirect.
- Standardized downloads using pinned release URLs and fail-fast curl.
- Opened TCP/9100 on Rocky Linux (firewalld).
- Verified metrics endpoints reachable from host.

### Evidence
- lab/evidence/2026-01-20_day8_metrics_prod_head.txt
- lab/evidence/2026-01-20_day8_metrics_infra_head.txt
- lab/evidence/2026-01-20_day8_node_exporter_prod_status.txt
- lab/evidence/2026-01-20_day8_node_exporter_infra_status.txt

### Day 8 Note — systemd Preset on Rocky Linux
- node_exporter shows `preset: disabled` on infra-rocky.
- Service is explicitly enabled and running.
- Preset reflects vendor default policy and does not affect service startup.

### Snapshot Checkpoint
- Snapshot: pre-monitoring-drills
- Purpose: Preserve verified monitoring baseline before failure drills.

## 2026-01-21 — Day 9 — Failure Detection Practices

### Scenarios Tested
1. Exporter service stopped
2. Firewall blocking metrics
3. Exporter listening on wrong port

### Detection Order Practiced
1. Host curl check
2. Service state
3. Local port binding
4. Firewall rules

### Outcome
- Confirmed each failure mode produces distinct symptoms.
- Practiced minimal, ordered checks to avoid guesswork.
- Restored all systems to healthy state.


### Evidence — Final Restored State

**infra-rocky**
- `node_exporter` service is loaded, explicitly enabled, and running under systemd.
- Service reports `preset: disabled`, which reflects Rocky Linux vendor preset policy and does not affect startup.
- Process is listening on TCP port 9100 on all interfaces.
- Metrics endpoint successfully returns Prometheus-formatted output from the host.

Evidence file:
- lab/evidence/2026-01-21_day9_failure_detection_infra.txt

**infra-rocky**
- `node_exporter` service is loaded, explicitly enabled, and running under systemd.
- Service reports `preset: disabled`, which reflects Rocky Linux vendor preset policy and does not affect startup.
- Exporter is listening on TCP port 9100.
- `firewalld` required an explicit rule to allow inbound TCP/9100.
- Metrics endpoint successfully returns Prometheus-formatted output from the host after firewall rule was applied.

Evidence file:
- lab/evidence/2026-01-21_day9_failure_detection_infra.txt


**prod-ubuntu**
- Metrics endpoint reachable and returning expected Prometheus output.
- No configuration changes required during failure detection exercises.

Evidence file:
- lab/evidence/2026-01-21_day9_baseline_prod_metrics.txt


### Day 9 Note — Post-drill Verification
- Observed empty output from metrics verification command.
- Confirmed exporter was not listening on expected port after drill.
- Restored correct listen address and verified metrics output.

### Day 9 Note — Rocky Linux Firewall Requirement

- Observed `connection refused` when querying `infra-rocky` metrics from the host,
  even though `node_exporter` was running and listening on TCP/9100.
- Root cause identified as `firewalld` blocking inbound traffic by default on Rocky Linux.
- Permanently opened TCP/9100 using `firewall-cmd`.
- Metrics endpoint became reachable immediately after reload.

Command used:

```bash
 sudo firewall-cmd --add-port=9100/tcp --permanent
 sudo firewall-cmd --reload
 ```

- This step is required for successful lab replication on Rocky/RHEL systems.


### Snapshot Checkpoint
- Snapshot: post-monitoring-baseline
- Purpose: Preserve verified monitoring state after failure drills.

## 2026-01-22 — Day 10 — Monitoring Runbook Creation

### Goal
Convert monitoring failure drills into a formal runbook.

### What I did
- Created a node_exporter monitoring runbook.
- Documented detection order: service → port → firewall → network.
- Included Rocky Linux firewalld requirement and systemd preset behavior.
- Validated runbook against both prod-ubuntu and infra-rocky.

### Evidence
- runbooks/monitoring-node-exporter.md
- lab/evidence/2026-01-22_day10_runbook_validation_infra.txt
- lab/evidence/2026-01-22_day10_runbook_validation_prod.txt

## 2026-01-23 — Day 11 — Alerting Concepts (Page vs Ticket vs Info)

### Goal
Implement a minimal, correct alerting pipeline and define paging philosophy.

### What I did
- Defined alert severities based on operational impact (page, ticket, info).
- Created Prometheus alert rules aligned to observed failure modes.
- Deployed Prometheus and Alertmanager as Docker containers on a shared network.
- Corrected Alertmanager discovery by referencing container name instead of localhost.
- Validated end-to-end alert flow using a controlled node_exporter outage and recovery.

### Key Fix
- Initial configuration incorrectly referenced `localhost:9093` from inside Prometheus.
- Resolved by attaching Prometheus and Alertmanager to the same Docker network and
  referencing Alertmanager by container name.

### Evidence
- lab/evidence/2026-01-23_day11_prometheus_alertmanagers.json
- lab/evidence/2026-01-23_day11_prometheus_rules.json
- lab/evidence/2026-01-23_day11_prometheus_alerts_firing.json
- lab/evidence/2026-01-23_day11_alertmanager_alerts.json
- lab/evidence/2026-01-23_day11_prometheus_alerts_resolved.json


### Snapshot Checkpoint
- Snapshot: post-alerting-corrected
- Purpose: Preserve verified alerting pipeline after Docker networking fix.

## 2026-01-24 — Day 12 — Alert Routing & Notification Hygiene

### Goal
Implement alert routing and notification hygiene (webhook without spam).

### What I did
- Implemented Alertmanager routing by severity (`page`, `ticket`, `info`).
- Added inhibition to suppress lower-severity notifications when a page alert is firing.
- Configured notification hygiene via grouping and repeat intervals to prevent spam.
- Implemented a local webhook receiver to log notifications without external credentials.
- Validated end-to-end: Prometheus → Alertmanager → webhook, including resolved notifications.

### Evidence
- lab/evidence/2026-01-24_day12_prometheus_alertmanagers.json
- lab/evidence/2026-01-24_day12_prometheus_alerts_firing.json
- lab/evidence/2026-01-24_day12_alertmanager_alerts.json
- lab/evidence/2026-01-24_day12_webhook_notifications_tail.txt
- lab/evidence/2026-01-24_day12_prometheus_alerts_resolved.json
- lab/evidence/2026-01-24_day12_alertmanager.yml
