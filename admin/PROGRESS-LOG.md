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
