# Linux Sysadmin 90-Day Lab (Vagrant + VirtualBox)

This repository documents a 90-day, hands-on Linux systems administration lab.
The focus is on real operational skills: system bring-up, troubleshooting,
access control, patching, service management, backups, security hardening,
automation, and incident response.

All work is performed in a controlled local lab using Vagrant and VirtualBox.

---

## Lab Topology

| VM Name | OS | Role | IP Address |
|--------|----|------|------------|
| prod-ubuntu | Ubuntu (jammy) | application / web host | 10.168.56.10 |
| infra-rocky | Rocky Linux 9 | infra / automation / backups | 10.168.56.20 |

---

## Tools Used

- VirtualBox
- Vagrant
- Ubuntu Linux
- Rocky Linux
- systemd
- nginx
- Borg Backup
- Ansible
- Git / GitHub

---

## Repository Structure

This repository is organized to separate **operational documentation**,
**raw evidence**, and **execution checklists**. This structure mirrors
how production teams document systems and incidents.

| Path | Purpose |
|------|--------|
| `admin/` | Planning documents, progress logs, and environment notes |
| `lab/evidence/` | Raw command output used as verification and proof |
| `lab/runbooks/` | Operational runbooks for common procedures |
| `lab/incidents/` | Incident reports, RCAs, and postmortems |
| `lab/ansible/` | Automation playbooks and configuration enforcement |
| `weeks/` | Week-by-week execution plans and completion tracking |

Start with `README.md`, then review `admin/PROGRESS-LOG.md` for daily activity,
and `weeks/` for structured execution and progress.

## Lab Setup

## Lab Assumptions & Constraints

The following assumptions and constraints apply to all labs and documentation
in this repository. They are intentionally documented to ensure reproducibility
and to avoid implicit dependencies.

### Host System Assumptions
- The host system is a Unix-like OS (Linux or macOS).
- VirtualBox and Vagrant are installed and available in the host PATH.
- The host user has passwordless or cached sudo access where required.

### Vagrant Layout Assumptions
- The Vagrantfile is located at: `~/linux-labs/vagrant-lab`
- This repository (`linux-sysadmin-90day-lab`) contains **documentation only**.

```bash
export VAGRANT_CWD=~/linux-labs/vagrant-lab
```

All `vagrant` commands referenced in this repository assume this variable is set.

### Network Assumptions
- Host-only networking is used.
- Static IPs:
  - prod-ubuntu: 10.168.56.10
  - infra-rocky: 10.168.56.20

### Access & Security Constraints
- SSH key-based access only.
- PasswordAuthentication disabled.
- PermitRootLogin disabled.

### Scope Constraints
- Local lab only.
- Failures are remediated, not bypassed.

### Vagrant Layout

- Vagrantfile location: `~/linux-labs/vagrant-lab`
- Documentation repository: `~/linux-labs/linux-sysadmin-90day-lab`

To allow Vagrant commands to be executed from the documentation repository
without changing directories, the following environment variable is set
on the host system:

```bash
export VAGRANT_CWD=~/linux-labs/vagrant-lab
```

This ensures all `vagrant` commands (e.g. `vagrant ssh`, `vagrant status`)
target the correct Vagrantfile during lab execution and evidence capture.

| Path | Purpose |
|-----|---------|
| `admin/` | Planning, progress logs, templates |
| `lab/evidence/` | Raw command output and proof |
| `lab/runbooks/` | Operational runbooks |
| `lab/incidents/` | RCAs and postmortems |
| `lab/ansible/` | Automation playbooks |
| `weeks/` | Week-by-week execution and checklists |

---

## How Progress Is Tracked

- Daily work is recorded in `admin/PROGRESS-LOG.md`
- Each week has its own checklist under `weeks/`
- Evidence is captured as raw command output under `lab/evidence/`
- Incidents are documented with root cause analysis and postmortems

---

## Standards Followed

- No reinstallation to fix problems
- Every failure has a documented root cause
- Fixes must be verified with evidence
- Runbooks are updated after incidents
- Automation is preferred over manual repetition

---

## Current Status

- Day 1 complete: lab bring-up and verification
- Mixed Ubuntu + Rocky environment operational

