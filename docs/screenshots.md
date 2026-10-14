# Screenshot evidence index

Thirteen screenshots from the current Hyper-V/RHEL rebuild are preserved
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
- Repository metadata-download completion remains pending. No image or
  successful result has been invented for that milestone.

The images include local lab names, private network addresses and virtual
device identifiers. They contain no employer infrastructure screenshots.
