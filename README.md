# Linux Sysadmin 90-Day Lab (Vagrant + VirtualBox)

A 90-day, hands-on Linux systems administration lab focused on real operational workflows:
system bring-up, patching, SSH hardening, monitoring, automation, rebuilds, and incident handling.

All work is executed in a controlled local environment using Vagrant and VirtualBox with
mixed Ubuntu and Rocky Linux hosts. Every activity is verified with captured evidence and
documented using production-style artifacts.

---

## What This Repository Demonstrates

- Linux system administration across multiple distributions
- Secure access control and SSH hardening with drift prevention
- Evidence-driven operations and verification discipline
- Reproducible infrastructure and rebuild validation
- Operational documentation (runbooks, incidents, change records)
- Monitoring instrumentation and health checks
- Automation-first mindset

---

## Start Here (Recommended Navigation)

1. **Lab topology & environment notes:** `admin/LAB-NOTES.md`
2. **Daily execution log:** `admin/PROGRESS-LOG.md`
3. **Week-by-week plans and checklists:** `weeks/`
4. **Verification evidence:** `lab/evidence/`
5. **Operational runbooks:** `lab/runbooks/`
6. **Incident reports and RCAs:** `lab/incidents/`

---

## Lab Topology

| VM Name     | OS            | Role                         | IP Address    |
|-------------|---------------|------------------------------|---------------|
| prod-ubuntu | Ubuntu (jammy) | application / web host       | 10.168.56.10  |
| infra-rocky | Rocky Linux 9  | infra / automation / backups| 10.168.56.20  |

---

## Tools Used

- VirtualBox
- Vagrant
- Ubuntu Linux
- Rocky Linux
- systemd
- OpenSSH
- nginx
- Ansible
- Borg Backup
- Git / GitHub

---

## Lab Setup

### Prerequisites
Install on your host system:
- VirtualBox
- Vagrant
- Git

Clone the repository:

```bash
git clone https://github.com/sammyutere/linux-sysadmin-90day-lab.git
cd linux-sysadmin-90day-lab
```

### Vagrant Layout
- Vagrantfile location: `~/linux-labs/vagrant-lab`
- Documentation repository: `~/linux-labs/linux-sysadmin-90day-lab`

Set Vagrant context so you can run `vagrant` commands from this documentation repo:

```bash
export VAGRANT_CWD=~/linux-labs/vagrant-lab
```

Bring up the lab:

```bash
vagrant up    
```

Check VM status:

```bash
vagrant status
```

Quick verification:

```bash
vagrant ssh prod-ubuntu -c "hostname; ip -br a; cat /etc/os-release"
vagrant ssh infra-rocky -c "hostname; ip -br a; cat /etc/os-release"
```

apture evidence (example):

```bash
mkdir -p lab/evidence
vagrant ssh prod-ubuntu -c "hostname; ip -br a" >  lab/evidence/baseline_example.txt
vagrant ssh infra-rocky -c "hostname; ip -br a" >> lab/evidence/baseline_example.txt
```

---

## Assumptions and Constraints

The following assumptions and constraints apply to all labs and documentation in this repository. They are explicitly documented to ensure reproducibility and to avoid implicit dependencies.

### Host System Assumptions
- The host system is a Unix-like OS (Linux or macOS).
- VirtualBox and Vagrant are installed and available in the host PATH.
- The host user has sufficient privileges to run Vagrant and manage VirtualBox VMs.

### Vagrant Execution Assumptions
- The Vagrantfile is located at: `~/linux-labs/vagrant-lab`
- This repository contains documentation only and does not store the Vagrantfile.
- All `vagrant` commands in this repository assume the following environment variable is set on the host:

```bash
export VAGRANT_CWD=~/linux-labs/vagrant-lab
```
### Network Assumptions

- Host-only networking is used.

- Static IP addresses are assigned:

     -  prod-ubuntu: 10.168.56.10

     -  infra-rocky: 10.168.56.20

- No DHCP or external network dependencies are assumed.

### Access and Security Constraints

- SSH access is key-based only.

- PasswordAuthentication is disabled.

- PermitRootLogin is disabled.

- SSH hardening is enforced using sshd_config.d/ drop-in configuration to prevent drift.

### Scope Constraints

- This lab is intentionally local-only unless explicitly extended.

- Failures must be remediated, not bypassed.

- Rebuilds must be possible using documentation and configuration alone.


## Repository Structure

| Path             | Purpose                                     |
| ---------------- | ------------------------------------------- |
| `README.md`      | Overview, setup, and navigation             |
| `admin/`         | Progress logs, environment notes, templates |
| `lab/evidence/`  | Raw verification output (proof)             |
| `lab/runbooks/`  | Operational runbooks                        |
| `lab/incidents/` | Incident reports, RCAs, postmortems         |
| `lab/ansible/`   | Automation playbooks and enforcement        |
| `weeks/`         | Week-by-week execution plans and checklists |


## How Progress Is Tracked

- Daily activity: admin/PROGRESS-LOG.md
- Weekly execution: weeks/
- Verification evidence: lab/evidence/
- Operational procedures: lab/runbooks/
- Incident handling: lab/incidents/

## Operating Standards

- Fix issues via remediation with verification output (no “reinstall to fix”).
- Capture proof for changes and validations in lab/evidence/.
- Document operational procedures as runbooks.
- Document incidents with root cause analysis and corrective actions.
- Prefer automation for repeatability where appropriate.

## Contributing

Suggestions are welcome. Open an issue describing the change or submit a pull request with clear validation notes.

## License

MIT License. See LICENSE.
