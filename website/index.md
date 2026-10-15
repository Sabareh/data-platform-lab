# Build a data platform, one verified step at a time

A hands-on lab for learning Linux, Kubernetes, data engineering and AI engineering.
Follow the build from a Windows laptop to a working platform, with commands,
explanations and screenshots from the actual setup.

[Start with the foundation](01-repository-foundation.md){ .md-button .md-button--primary }
[See the latest progress](progress.md){ .md-button }

## The lab at a glance

| Layer | Technology |
| --- | --- |
| Virtual machines | Hyper-V on Windows |
| Operating system | Red Hat Enterprise Linux 9.8 |
| Kubernetes | kubeadm, CRI-O and Calico |
| Planned CI | GitHub Actions runner and a local registry |
| Planned workloads | Data pipelines, notebooks and AI experiments |

## Follow the build

1. [Set up Git and GitHub](01-repository-foundation.md).
2. [Create the Hyper-V network](02-hyperv-network.md).
3. [Install RHEL](03-rhel-control-plane-vm.md).
4. [Verify networking, SSH and package access](04-rhel-first-boot.md).
5. [Prepare the Kubernetes node](05-kubernetes-node-preparation.md).
6. [Bootstrap the control plane and configure Calico](07-control-plane-and-calico.md).
7. [Create the first worker VM](08-first-worker-vm.md).
8. [Explore the CI and registry plan](06-ci-and-registry-plan.md).

## Evidence, not just instructions

The [progress register](progress.md) separates verified outcomes from planned work.
The [screenshot index](screenshots.md) contains 33 reviewed captures, including
intermediate failures and their resolution. Commands describe a guided build;
read their context before rerunning them on an existing system.

This is an independent personal lab using synthetic data, not a production deployment.
