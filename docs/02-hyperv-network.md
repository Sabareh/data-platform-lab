# Hyper-V network foundation

## What we are building

Run this guide's Hyper-V configuration commands in Administrator PowerShell.
The user created a dedicated internal switch, assigned a gateway address and
enabled NAT. No VM-to-internet connectivity test has been completed yet.

```text
Future RHEL Kubernetes nodes
          |
reservoir-lab-switch (Internal)
          |
Windows virtual adapter: 192.168.200.1/24
          |
reservoir-lab-nat
          |
Windows network connection -> home router -> internet
```

An internal switch connects VMs to each other and the host. It does not
provide internet access on its own. The gateway is the host's address used
by VMs to reach other networks. NAT translates outbound connections and
tracks replies so multiple VMs can share the host's internet connection.

NAT does not provide DHCP or automatically make the gateway a DNS server.
Each guest will need an address, subnet, gateway and DNS configuration.
The gateway is also not a Satellite/package-repository server.

## Inspect before creating

These commands only read configuration:

```powershell
Get-VM | Select-Object Name, State, CPUUsage, MemoryAssigned
Get-VMSwitch | Select-Object Name, SwitchType, NetAdapterInterfaceDescription
Get-NetIPAddress -AddressFamily IPv4 | Select-Object InterfaceAlias, IPAddress, PrefixLength
Get-NetNat | Select-Object Name, InternalIPInterfaceAddressPrefix
```

The initial VM listing was empty. Existing switches were `Default Switch`
and `WSL (Hyper-V firewall)`, both Internal. The observed network ranges were:

| Use | Observed subnet |
| --- | --- |
| Home Wi-Fi | 192.168.100.0/24 |
| Default Switch | 172.19.112.0/20 |
| WSL | 172.24.224.0/20 |

`Get-NetNat` returned no entries. This does not mean that Windows-managed
Default Switch or WSL networking has no address translation of its own.
The lab range does not overlap the observed interface subnets; VPN or future
network routes must also be considered if connectivity changes.

## Create the switch

```powershell
New-VMSwitch -Name "reservoir-lab-switch" -SwitchType Internal
```

The `reservoir-lab` network names were chosen before the Git repository was
named `data-platform-lab`. They are retained to match the deployed objects.

### Troubleshooting the initial failure

The first attempt failed with:

```text
Internal miniport create failed
Cannot create a file when that file already exists. (0x800700B7)
```

The following read-only inspections were performed:

```powershell
Get-VMSwitch | Select-Object Name, Id, SwitchType
Get-NetAdapter -IncludeHidden | Select-Object Name, InterfaceDescription, ifIndex, Status
Get-PnpDevice -Class Net | Select-Object Status, FriendlyName, InstanceId
```

Findings:

- No switch or adapter named `reservoir-lab-switch` was listed.
- The listed Hyper-V switch extension devices reported `OK`.
- Unknown RAS/Bluetooth entries did not establish the cause and were not removed.
- A Windows restart was recommended before retrying. The conversation does
  not explicitly confirm that a restart occurred.
- The subsequent `New-VMSwitch` command succeeded and reported `Internal`.

Outcome: creation succeeded on retry. Root cause remains unknown; do not
claim a proven duplicate-device repair or delete unrelated network devices.

## Identify the adapter and assign the gateway

```powershell
Get-NetAdapter -Name "vEthernet (reservoir-lab-switch)" | Select-Object Name, ifIndex, Status
New-NetIPAddress -InterfaceAlias "vEthernet (reservoir-lab-switch)" -IPAddress 192.168.200.1 -PrefixLength 24
```

The adapter was reported `Up`. `/24` is equivalent to `255.255.255.0`:
`.0` identifies the subnet, `.255` is its broadcast address and `.1` is the
chosen Windows gateway. VM addresses will be assigned later without duplicates.

The assignment initially showed `Tentative` in ActiveStore and `Invalid`
in PersistentStore. We checked the operational state rather than assuming
failure from the immediate output:

```powershell
Get-NetIPAddress -InterfaceAlias "vEthernet (reservoir-lab-switch)" -AddressFamily IPv4 -PolicyStore ActiveStore | Select-Object IPAddress, PrefixLength, AddressState
```

Observed result:

```text
IPAddress       PrefixLength AddressState
192.168.200.1              24 Preferred
```

`Preferred` means the address is usable. Adapter index 57 was observed, but
indices can change, so the commands use the adapter name.

## Configure and verify NAT

```powershell
New-NetNat -Name "reservoir-lab-nat" -InternalIPInterfaceAddressPrefix "192.168.200.0/24"
Get-NetNat -Name "reservoir-lab-nat" | Select-Object Name, InternalIPInterfaceAddressPrefix, Active
```

Observed result:

```text
Name               InternalIPInterfaceAddressPrefix Active
reservoir-lab-nat   192.168.200.0/24                   True
```

This confirms configuration, not end-to-end internet connectivity. Existing
objects should be inspected rather than recreated. Microsoft documents a
single internal NAT prefix limitation for WinNAT; do not add unrelated NAT
objects or remove existing ones blindly.

## Remaining validation

- Confirm configuration survives a host restart.
- Assign guest network settings and test gateway reachability.
- Test DNS resolution and outbound HTTPS from the first guest.
- Later, test node-to-node communication.
- Choose Kubernetes Pod and Service ranges without overlaps.

Kubernetes node networking is this VM network. Pod and Service networking
will be configured separately once the Linux nodes are ready.

## Reference

[Microsoft: Set up a Hyper-V NAT network](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/setup-nat-network)
