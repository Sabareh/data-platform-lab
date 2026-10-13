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
- Get-NetNat returned no entries.

## Current blocker

Creating reservoir-lab-switch failed with error 0x800700B7:
"Cannot create a file when that file already exists."

The cause is not yet established. The next infrastructure step is to inspect
existing Hyper-V switches and virtual adapters before retrying creation.

No new Kubernetes VMs or cluster have been created for this rebuild.

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
