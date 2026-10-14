# Progress and evidence register

Updated: 2026-10-14 (Africa/Nairobi).

This register records user-shared terminal output and completion reports.
It is not an independent live audit of the Hyper-V host. Raw logs, device
identifiers and unrelated personal storage-cleanup details are omitted.

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
| RHEL installation | In progress | Language screen and completed installation not yet confirmed |
| Guest network and internet | Pending | NAT configuration alone is not a connectivity test |
| Worker VMs | Planned | No creation evidence yet |
| Kubernetes | Planned | kubeadm, runtime, CNI, storage and RBAC not installed |
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
- Guest container runtime and compatible Kubernetes/CNI versions still pending.
- Podman is intended for image workflows, not as the Kubernetes CRI runtime.
- One control plane initially; high availability is not provided.
- Add services incrementally within laptop capacity.
- Public evidence must use synthetic data and omit credentials/internal documents.
- Satellite/package mirroring was discussed for understanding, not added to scope.
- Read-only MCP is deferred until Kubernetes is operational.

## Next step

Return to the VM console and establish the current installer screen before
giving the next RHEL installation instruction.
