# Screenshot evidence index

Twenty-eight screenshots from the current Hyper-V/RHEL rebuild are preserved
unchanged under `docs/images/` and embedded beside the relevant explanations.
They include intermediate states and failures, not just successful outcomes.

## Installation sequence

See [RHEL VM and installer guide](03-rhel-control-plane-vm.md).

| Screenshot | What it records |
| --- | --- |
| [Initial summary](images/rhel-initial-summary.png) | Original installer defaults, before configuration |
| [Server selection](images/rhel-server-selection.png) | Server base environment and unchecked optional add-ons |
| [Account setup pending](images/rhel-account-setup-pending.png) | Intermediate summary before user creation |
| [Network before configuration](images/rhel-network-before-configuration.png) | Adapter off, hostname still localhost |
| [Hostname applied](images/rhel-hostname-applied.png) | lab-control-01 selected; adapter still off |
| [Installation disk](images/rhel-installation-disk.png) | 40 GiB virtual disk and Automatic partitioning |
| [Final installation summary](images/rhel-installation-summary.png) | Final settings accepted before installation |

## First boot and troubleshooting

See [first-boot and SSH guide](04-rhel-first-boot.md).

| Screenshot | What it records |
| --- | --- |
| [First boot](images/rhel-first-boot.png) | Installed RHEL 9.8 reaches the login prompt |
| [Console login](images/rhel-console-login.png) | sabare reaches a local shell |
| [Sudo and routing](images/rhel-sudo-and-routing.png) | Administrator access, IPv4 address and default route |
| [DNS check](images/rhel-dns-check.png) | Corrected lookup resolves www.redhat.com |
| [Windows SSH port test](images/windows-ssh-port-check.png) | TCP port 22 reachable from Windows |
| [SSH authentication log](images/rhel-ssh-authentication-log.png) | Evidence used to diagnose initial password failures |

## Selection boundaries

- Password-entry screens and output containing HTTP cookies are not published.
  The relevant configuration and HTTPS result are described in text instead.
- Screenshots from the retired Docker/kind/SQL lab are not evidence of this
  rebuilt platform. Personal storage cleanup screenshots are also outside scope.
- Later registration, successful SSH login and enabled repositories were
  reported in text; screenshots of those results were not supplied.
- RHEL metadata refresh and update-check success were reported in text; no screenshot is claimed for those results.

The images include local lab names, private network addresses and virtual
device identifiers. They contain no employer infrastructure screenshots.

## Node preparation and package installation

Nine additional originals were reviewed and copied from the Windows Pictures/Screenshots
folder. They are embedded in [node preparation](05-kubernetes-node-preparation.md).
The latest image also matches the attachment supplied with this documentation request.

| Capture (2026-10-14, local time) | Screenshot | Evidence |
| --- | --- | --- |
| 06:26:17 | [Update preview](images/rhel-update-preview.png) | Preview only; Operation aborted is expected |
| 06:45:24 | [Kernel and disks](images/rhel-kernel-disk-layout.png) | Updated running kernel and LVM layout |
| 06:48:36 | [Low memory](images/rhel-low-memory-before-fix.png) | Historical low guest memory before fixed allocation |
| 07:01:53 | [Swap disabled](images/rhel-swap-disabled.png) | Post-reboot Swap 0B and no active swap units |
| 07:04:02 | [Node baseline](images/rhel-node-baseline.png) | Historical inactive chronyd, security checks, no CRI-O yet |
| 07:12:39 | [Time and networking](images/rhel-time-and-kernel-networking.png) | Synchronised clock, modules loaded, sysctl values 1 |
| 07:22:24 | [CRI-O repository](images/crio-repository-versions.png) | Metadata and available versions, not installation proof |
| 14:15:14 | [Kubernetes repository](images/kubernetes-repository-ready.png) | Repository file and successful metadata refresh |
| 14:19:32 | [Installed packages](images/kubernetes-packages-installed.png) | Versions 1.36.5, kubelet enabled, CRI-O active |

Capture times identify source files, not the time every command on screen ran.
No credentials, registration IDs or cookie-bearing output were found in these nine images.

## Runtime, bootstrap and Calico operator

Six further originals are embedded in [the control-plane guide](07-control-plane-and-calico.md).

| Capture (2026-10-14, local time) | Screenshot | Evidence |
| --- | --- | --- |
| 14:30:14 | [Runtime ready](images/crio-runtime-ready.png) | RuntimeReady true; CNI absent |
| 14:31:19 | [Runtime API](images/crio-api-and-node-network.png) | CRI-O 1.36.7, CRI v1, VM routes |
| 14:53:45 | [Historical firewall rules](images/kubernetes-firewall-rules-historical.png) | Rules verified before firewalld disabled |
| 14:55:56 | [Calico host preparation](images/calico-host-preparation.png) | NetworkManager exclusions, VXLAN, firewalld disabled, SELinux Enforcing |
| 15:01:18 | [Images and preflight](images/kubeadm-images-and-preflight.png) | Download success and preflight warnings |
| 15:36:24 | [Operator ready](images/calico-operator-ready.png) | Rollout succeeded, Pod 1/1 Running |

The 15:12:54 bootstrap-success screenshot is excluded because it contains a join
token. Only non-sensitive results are transcribed. No token revocation is claimed.
Calico network readiness is not yet evidenced.
