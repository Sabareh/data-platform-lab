# Progress and evidence register

Updated: 2026-10-14 (Africa/Nairobi).

This register records user-shared terminal output and completion reports.
It is not an independent live audit of the Hyper-V host. Selected original
screenshots are embedded in the installation and first-boot guides. They show
only the personal lab; credentials, cookie-bearing HTTP output and unrelated
personal storage-cleanup material are not included.

The [screenshot index](screenshots.md) lists all 22 included images, their
purposes and the reasons other supplied images were not published.

| Milestone | Status | Evidence / limit |
| --- | --- | --- |
| Windows source repository | Verified | main branch, .gitignore and README committed and pushed |
| CRC cleanup | Verified | Uninstall reported; Test-Path for .crc returned False |
| Hyper-V lab switch | Verified | New-VMSwitch returned reservoir-lab-switch / Internal |
| Lab adapter | Reported verified | User reported it listed with status Up |
| Gateway address | Verified | 192.168.200.1, prefix 24, ActiveStore Preferred |
| NAT | Verified | reservoir-lab-nat, 192.168.200.0/24, Active=True |
| ISO | Verified | RHEL 9.8 x86_64 DVD SHA-256 matches vendor value |
| Control-plane VM creation | Reported verified | User reported New-VM succeeded |
| CPU configuration | Verified command completion | Set-VMProcessor -Count 2 returned without errors |
| Secure Boot, ISO and boot order | Reported verified | User reported each command succeeded |
| VM boot | Verified | User reported RHEL installer boot menu visible |
| Installer software/time settings | Verified in screenshot | Server, English (US), Africa/Nairobi |
| Administrator account | Verified | Console login succeeded and sudo whoami returned root |
| Hostname | Verified in screenshot | Current host name lab-control-01 |
| Installer IPv4 settings | Reported verified | User reports 192.168.200.10 and DNS servers; summary shows eth0 connected |
| Installation disk selection | Verified in screenshot | 40 GiB sda; Automatic; final summary has no destination warning |
| RHEL installation | Verified boot | Screenshot shows installed RHEL 9.8 login prompt after reboot |
| Post-install address and routes | Verified in screenshot | eth0 UP, 192.168.200.10/24, default via 192.168.200.1 |
| DNS and HTTPS | Verified in supplied output | getent returned IPv4; curl received HTTP/2 301 from Red Hat |
| SSH service and TCP reachability | Verified | sshd active; Windows TcpTestSucceeded=True on port 22 |
| SSH login | Reported verified | Initial password failures resolved after private password change |
| RHEL registration | Reported verified | User confirmed interactive registration succeeded |
| BaseOS and AppStream | Reported verified | User confirmed both enabled in dnf repolist |
| Repository access | Reported verified | Metadata refresh and update check succeeded, including after subscription warning |
| Worker VMs | Planned | No creation evidence yet |
| RHEL update | Verified | Running kernel 5.14.0-687.57.1.el9_8.x86_64 |
| VM memory | Reported verified | Dynamic Memory disabled, startup 3072 MiB; guest about 2.6 GiB |
| Swap | Verified after reboot | Swap 0B and zero active swap units |
| Time sync | Verified | chronyd enabled/active, selected source and clock synchronised |
| Security baseline | Verified at inspection | SELinux Enforcing, firewalld active, cgroup v2 |
| Kernel network settings | Verified applied | overlay and br_netfilter loaded; three sysctl values 1; reboot persistence not yet retested |
| CRI-O | Reported installed; active verified | 1.36.7 selected in transaction; post-install version output absent |
| Kubernetes packages | Verified | kubeadm/kubelet/kubectl 1.36.5; cri-tools 1.36.0; kubernetes-cni 1.9.1 |
| Kubelet boot enablement | Verified | systemctl is-enabled returned enabled |
| Runtime API checks | Pending | crictl configuration and diagnostics proposed, result not received |
| Cluster creation | Planned | No kubeadm init, CNI deployment, worker join or application deployment yet |
| GitHub runner and local registry | Planned | Selected co-location on supporting RHEL VM outside Kubernetes |
| Data/AI services and MCP | Planned | No deployments in the rebuilt lab |

## Resolved symptom, unknown cause

Switch creation initially failed with `0x800700B7`. Read-only switch, adapter
and Plug and Play inspections did not identify a conflicting lab device.
A retry later succeeded. A restart was suggested but not confirmed. The
root cause must remain unknown rather than being presented as a proven fix.

## Decisions and open questions

- Use Hyper-V as the local substitute for infrastructure-provided VMs.
- Run upstream Kubernetes inside the RHEL guests, not on OpenShift Local.
- RHEL 9.8 chosen for this lab; reference environment version still unknown.
- Server selected without GUI or optional add-ons; administer through terminal/SSH.
- Guest address 192.168.200.10/24 with gateway 192.168.200.1; public DNS for the home lab.
- Root password set privately; root password SSH was instructed off and needs verification.
- Disk layout verified: EFI, XFS boot, LVM root and swap; swap disabled without deleting its volume.
- CRI-O 1.36 selected; Kubernetes 1.36.5 packages installed. CNI choice and compatibility remain pending.
- Podman is intended for image workflows, not as the Kubernetes CRI runtime.
- One control plane initially; high availability is not provided.
- Add services incrementally within laptop capacity.
- Public evidence must use synthetic data and omit credentials/internal documents.
- Satellite/package mirroring was discussed for understanding, not added to scope.
- Read-only MCP is deferred until Kubernetes is operational.

## Next step

Verify CRI-O communication through crictl, then review runtime settings, firewall,
Pod/Service ranges and CNI compatibility before cluster creation.
See [node preparation](05-kubernetes-node-preparation.md) and
[the runner/registry plan](06-ci-and-registry-plan.md).
