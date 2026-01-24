# Linux Sysadmin 90-Day Lab (Vagrant + VirtualBox)

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Lab Setup](#lab-setup)
  - [Vagrant Layout](#vagrant-layout)

## Lab Setup

### Vagrant Layout

- Vagrantfile location: `~/linux-labs/vagrant-lab`
- Documentation repository: `~/linux-labs/linux-sysadmin-90day-lab`

To allow Vagrant commands to be executed from the documentation
repository without changing directories, set:

```bash
export VAGRANT_CWD=~/linux-labs/vagrant-lab
```

Bring up the lab with:

```bash
vagrant up
```
