# Data Platform Lab

A personal lab for developing practical data engineering, AI engineering,
and Kubernetes platform skills using synthetic data.

## Architecture

Windows laptop
  -> Hyper-V
    -> Linux virtual machines
      -> Vanilla Kubernetes
        -> Data engineering and AI engineering workloads

Hyper-V provides the local virtual machines. In the reference architecture,
OpenShift Virtualization provides Linux VMs that host a separate vanilla
Kubernetes cluster.

This lab reproduces the guest Kubernetes layer. It does not reproduce
OpenShift Virtualization administration or confirm any production licensing
or support arrangements.

## Planned virtual machines

| VM | Role | Initial RAM | Virtual CPUs |
| --- | --- | --- | --- |
| lab-control-01 | Kubernetes control plane | 3 GB | 2 |
| lab-worker-01 | Application worker | 5 GB | 2 |
| lab-worker-02 | Application worker | 5 GB | 2 |
| Supporting VM (name pending) | GitHub Actions runner and local registry | TBD | TBD |

These allocations are provisional. The initial cluster will not be highly
available because it has only one control-plane node.

## Planned platform

- Upstream Kubernetes bootstrapped using kubeadm.
- CRI-O 1.36 series as the Kubernetes node runtime.
- Podman for building and testing container images.
- GitHub Actions self-hosted runner and a local registry on one supporting RHEL VM (planned).
- Department namespaces: cib, iam, bcb, ppb and operations.
- Engineering namespaces: data-engineering and ai-engineering.
- Shared services in dedicated namespaces as required.
- Airflow, JupyterHub, Spark and Kafka, introduced incrementally.
- SQL Server outside Kubernetes for synthetic source and reservoir data.
- Python ingestion, XML transformation and data-quality validation.
- AI experiments using frameworks such as PyTorch and Hugging Face.
- Read-only Kubernetes MCP integration after the cluster is operational.

## Verified progress

- Git is available in Windows and the commit identity is configured.
- GitHub CLI is installed and authenticated.
- The public data-platform-lab repository was created.
- The first commit contains .gitignore and was pushed successfully.
- OpenShift Local was cleaned up and uninstalled.
- The remaining user .crc directory was deleted and its absence verified.
- Hyper-V lists the Default Switch and WSL internal switches.
- The dedicated internal switch `reservoir-lab-switch` was created successfully.
- Its Windows gateway is `192.168.200.1/24`, verified as `Preferred`.
- NAT `reservoir-lab-nat` covers `192.168.200.0/24` and reports `Active=True`.
- RHEL 9.8 x86_64 DVD ISO was downloaded and its SHA-256 matched the published checksum.
- VM `lab-control-01` was created with a 40 GB expanding disk, 3 GB startup RAM and 2 virtual CPUs.
- Linux-compatible Secure Boot was configured, the ISO attached and DVD boot selected.
- The RHEL installer boot menu was reached.
- Installer settings now select Server without a desktop, Africa/Nairobi,
  administrator `sabare`, and automatic partitioning on the 40 GiB virtual disk.
- Installer networking reports `eth0` connected with static address
  `192.168.200.10/24`; hostname is `lab-control-01`.

## Current step

RHEL is updated and running with fixed 3 GB VM RAM, swap disabled after reboot,
time synchronisation working and kernel networking settings applied.
CRI-O 1.36.7 responds through CRI API v1. Kubernetes 1.36.5 initialised
successfully and the Calico 3.33.0 operator is 1/1 Running. The node was
NotReady and CoreDNS Pending before Pod-network configuration.

Next: apply the prepared Calico VXLAN configuration with BGP disabled and
Pod network 10.244.0.0/16, then verify readiness. Firewalld is now disabled
following Calico preparation; SELinux remains Enforcing. Worker VMs,
the supporting runner/registry VM and applications remain planned.
The earlier switch-creation error `0x800700B7` no longer blocks progress:
a later retry succeeded. Its underlying cause was not established, and a
Windows restart was recommended but not explicitly confirmed in the evidence.

## Documentation

The [GitHub Wiki](https://github.com/Sabareh/data-platform-lab/wiki) is the home for guides, progress records and screenshots.
Executable manifests remain in this repository.

### Step-by-step guides

- [Windows Git and GitHub foundation](https://github.com/Sabareh/data-platform-lab/wiki/01-repository-foundation)
- [Hyper-V network, concepts and troubleshooting](https://github.com/Sabareh/data-platform-lab/wiki/02-hyperv-network)
- [RHEL ISO verification and first VM preparation](https://github.com/Sabareh/data-platform-lab/wiki/03-rhel-control-plane-vm)
- [First boot, SSH and repository access, with screenshots](https://github.com/Sabareh/data-platform-lab/wiki/04-rhel-first-boot)
- [Kubernetes node preparation and troubleshooting](https://github.com/Sabareh/data-platform-lab/wiki/05-kubernetes-node-preparation)
- [GitHub Actions and local registry plan](https://github.com/Sabareh/data-platform-lab/wiki/06-ci-and-registry-plan)
- [Control-plane bootstrap and Calico](https://github.com/Sabareh/data-platform-lab/wiki/07-control-plane-and-calico)
- [Screenshot evidence index: 28 images](https://github.com/Sabareh/data-platform-lab/wiki/screenshots)
- [Progress and evidence register](https://github.com/Sabareh/data-platform-lab/wiki/progress)

The guides preserve commands from the build with explanations. Creation
commands are historical instructions, not scripts to rerun blindly on an
existing environment. Verification commands are identified separately.

## Documentation approach

For each milestone, record:

1. Purpose and relevant concepts.
2. Where commands run: Windows, a Linux VM or a database client.
3. Exact commands or reusable scripts.
4. Verification results and sanitised evidence.
5. Errors, diagnosis and resolution.
6. Decisions, alternatives and remaining limitations.

Mark work as planned, in progress, verified or blocked. Do not present
planned components as deployed.

## Repository hygiene

Use synthetic data and public technical references.

Do not commit credentials, kubeconfigs, pull secrets, private keys,
VM disks, database backups, customer data or internal employer documents.

.gitignore reduces accidental staging but does not replace reviewing changes.

## Scope

This is an independent personal lab, not a production deployment or an
official implementation of an employer's environment.
