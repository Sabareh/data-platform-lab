# Documentation publishing

Readers use https://sabareh.github.io/data-platform-lab/.
The Wiki remains the source for the nine guides and screenshots; `website/index.md`
defines the standalone homepage. Do not edit generated `.site-docs/` or `site/`.

## Current publishing mode

The site is live from the `gh-pages` branch, using GitHub's built-in Pages build.
The custom Actions workflow could not start because GitHub reported an account
billing lock. It is disabled to avoid repeated failures and conflicting deployments.
Wiki edits therefore do not currently publish automatically.

After updating and pulling the Wiki, publish from a machine with Python:

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_docs.py ../data-platform-lab.wiki
python -m mkdocs gh-deploy --strict
```

This builds locally and pushes generated HTML to `gh-pages`. Check the Pages
deployment result before reporting an update live.

## Optional automation after billing is resolved

Switch Pages publishing to GitHub Actions, then enable `pages.yml`. It supports
main-branch pushes, Wiki web edits (`gollum`), and manual dispatch. After pushing
Wiki changes through Git, explicitly dispatch the workflow. Do not mix the branch
publishing mode with workflow deployments.

Local preview, with Python installed and the Wiki cloned beside this repository:

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_docs.py ../data-platform-lab.wiki
python -m mkdocs build --strict
python -m mkdocs serve
```

The preparation script rewrites Wiki links and screenshot URLs to local website
paths. Deployments upload only the generated website; kubeconfigs and other
repository files are not included. The Calico example is included as a download.
