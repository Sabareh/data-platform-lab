# Documentation publishing

Readers use https://sabareh.github.io/data-platform-lab/.
The Wiki remains the source for the nine guides and screenshots; `website/index.md`
defines the standalone homepage. Do not edit generated `.site-docs/` or `site/`.

The Pages workflow rebuilds on main-branch pushes, Wiki web edits (`gollum`), and
manual dispatch. After pushing the Wiki through Git, explicitly run:

```bash
gh workflow run pages.yml --repo Sabareh/data-platform-lab
```

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
