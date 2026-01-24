# Lab Notes

## Topology (Vagrant + VirtualBox)

| VM Name | OS | Role | IP Address |
|--------|----|------|------------|
| prod-ubuntu | Ubuntu (jammy) | application / web host | 10.168.56.10 |
| infra-rocky | Rocky Linux 9 | infra / automation / backups | 10.168.56.20 |

## Day 1 Notes
- Built a two-node mixed-distro lab using Vagrant and VirtualBox.
- Verified SSH access using `vagrant ssh`.
- Confirmed hostname, IP addressing, kernel version, and OS release on both nodes.

## Vagrant Execution Context

The Vagrantfile for this lab is located in:

    ~/linux-labs/vagrant-lab

To allow Vagrant commands to be executed from the documentation repository
(`~/linux-labs/linux-sysadmin-90day-lab`), the following environment variable
is set on the host system:

    export VAGRANT_CWD=~/linux-labs/vagrant-lab

This ensures all `vagrant` commands executed during documentation and evidence
collection target the correct Vagrantfile without changing directories.
