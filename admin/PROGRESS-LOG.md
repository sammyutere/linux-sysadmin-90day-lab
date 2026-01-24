# Progress Log — Linux Sysadmin 90-Day Lab

## 2026-01-13 — Day 1 — Lab Bring-up & Verification

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
