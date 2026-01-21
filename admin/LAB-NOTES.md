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
