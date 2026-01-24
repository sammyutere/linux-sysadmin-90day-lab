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

## Lab Setup

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

