# Linux Sysadmin 90-Day Lab (Vagrant + VirtualBox)

## Table of Contents
- [Motivation](#motivation)
- [Lab Setup](#lab-setup)
- [Lab Assumptions & Constraints](#lab-assumptions--constraints)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [How Progress Is Tracked](#how-progress-is-tracked)
- [Standards Followed](#standards-followed)
- [Contributing](#contributing)
- [License](#license)

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
