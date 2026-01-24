# Linux Sysadmin 90-Day Lab (Vagrant + VirtualBox)

A 90-day, hands-on Linux systems administration lab built to practice operational workflows: system bring-up, patching, SSH hardening, monitoring, automation, and incident handling. Work is executed in a controlled local environment using Vagrant and VirtualBox with mixed Ubuntu and Rocky Linux hosts.

---

## Motivation

This repository exists to develop practical Linux administration capability using evidence-driven execution. Each lab activity is documented, verified with captured output, and organized to mirror production operations (runbooks, change records, and incident write-ups).

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

### Vagrant Layout
- Vagrantfile location: `~/linux-labs/vagrant-lab`
- Documentation repository: `~/linux-labs/linux-sysadmin-90day-lab`

Set Vagrant context so you can run `vagrant` commands from this documentation repo:

```bash

export VAGRANT_CWD=~/linux-labs/vagrant-lab

---

## Lab Assumptions and Constraints

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



