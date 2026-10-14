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

These allocations are provisional. The initial cluster will not be highly
available because it has only one control-plane node.

## Planned platform

- Upstream Kubernetes bootstrapped using kubeadm.
- A CRI-compatible node runtime; selection is pending.
- Podman for building and testing container images.
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

RHEL installation is in progress, as reported by the user after the final
summary review. Installation completion, post-reboot networking, internet
access, registration, SSH and Kubernetes installation are not yet verified.

The earlier switch-creation error `0x800700B7` no longer blocks progress:
a later retry succeeded. Its underlying cause was not established, and a
Windows restart was recommended but not explicitly confirmed in the evidence.

## Step-by-step guides

- [Windows Git and GitHub foundation](docs/01-repository-foundation.md)
- [Hyper-V network, concepts and troubleshooting](docs/02-hyperv-network.md)
- [RHEL ISO verification and first VM preparation](docs/03-rhel-control-plane-vm.md)
- [Progress and evidence register](docs/progress.md)

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
