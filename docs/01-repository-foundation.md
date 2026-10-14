# Windows Git and GitHub foundation

## Purpose and execution location

Run these commands in normal Windows PowerShell. The source repository lives
on Windows because Hyper-V is managed from Windows. Linux commands will run
inside the future RHEL VMs. WSL is not required for this repository.

This guide records the completed sequence; the repository already exists.
Do not repeat repository creation or overwrite an existing `.gitignore`.

## Create and enter the working folder

```powershell
New-Item -ItemType Directory -Path "$env:USERPROFILE\Documents\AI Engineering\data-platform-lab" -Force
Set-Location "$env:USERPROFILE\Documents\AI Engineering\data-platform-lab"
git --version
```

`USERPROFILE` locates the current Windows user's home folder. `New-Item`
creates the directory; `Set-Location` selects it as the working directory.
`git --version` confirms Git is available. Opening a terminal does not
automatically put it inside the repository.

## Exclusions, identity and the first commit

The committed [.gitignore](../.gitignore) excludes credentials, virtual disks,
ISOs, generated data and local artifacts. Review it before adding new types
of artifacts. Ignore rules do not remove files already tracked by Git and
are not a secret scanner.

```powershell
git init -b main
git var GIT_AUTHOR_IDENT
git status --short
git add -- .gitignore
git commit -m "Initialize repository with exclusions for secrets and local artifacts"
git status
```

- `init -b main` creates local history with an initial branch called `main`.
- `var GIT_AUTHOR_IDENT` checks the name and email recorded on commits. A
  GitHub noreply address can be used for public commit privacy.
- `status --short` shows changed and untracked files; `??` means untracked.
- `add -- .gitignore` selects that exact file for the next snapshot.
- `commit -m` saves the selected content locally with an explanatory message.

## Install GitHub CLI and authenticate

Git tracks local history; GitHub hosts a remote copy. `gh` is a separate
command-line client for GitHub. A WSL installation does not automatically
make it available in Windows PowerShell.

```powershell
winget install --id GitHub.cli --exact --source winget
```

Reopen PowerShell after installation so the new command path is available.

```powershell
gh --version
gh auth login --hostname github.com --git-protocol https --web
```

Complete authentication in the browser and allow Git authentication when
prompted. Device codes and access tokens must not be recorded in this repo.

## Create the public remote and push

From the local project folder:

```powershell
gh repo create data-platform-lab --public --source . --remote origin --push
gh repo view --json nameWithOwner,url,visibility
git status -sb
```

`--source .` uses the current repository. `origin` is the saved name for its
remote address. `--public` publishes committed content for anyone to read.
`--push` uploads the initial commit.

The remote is https://github.com/Sabareh/data-platform-lab.

## Documentation workflow

The original README was committed with:

```powershell
git add -- README.md
git commit -m "Document lab architecture, verified progress and networking blocker"
git push origin main
```

For subsequent updates, inspect content first, stage named files and review
the staged diff before committing:

```powershell
git status --short
git diff
# Stage only the intended files with git add -- <paths>.
git diff --cached
# Commit with a message describing the final change, then push.
```

New untracked files do not appear in ordinary `git diff`; read them directly
or inspect them after staging. A clean working tree means local files match
the current commit. It does not prove that someone has not changed GitHub
since the last fetch.

## References

- [GitHub CLI for Windows](https://github.com/cli/cli/blob/trunk/docs/install_windows.md)
- [GitHub repository creation command](https://cli.github.com/manual/gh_repo_create)
