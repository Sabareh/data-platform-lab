"""Prepare website content from a local clone of the public GitHub Wiki."""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
wiki = Path(sys.argv[1]).resolve()
output = ROOT / '.site-docs'
output.mkdir(exist_ok=True)
wiki_url = 'https://github.com/Sabareh/data-platform-lab/wiki/'
image_url = 'https://raw.githubusercontent.com/wiki/Sabareh/data-platform-lab/images/'
pages = {p.stem for p in wiki.glob('*.md') if not p.name.startswith('_')}

def local_link(match):
    target = match.group(1)
    if target.startswith(image_url):
        target = 'images/' + target[len(image_url):]
    elif target.startswith(wiki_url):
        slug, sep, anchor = target[len(wiki_url):].partition('#')
        if slug in pages:
            target = ('index' if slug == 'Home' else slug) + '.md'
            if sep:
                target += '#' + anchor
    elif target == 'https://github.com/Sabareh/data-platform-lab/blob/main/infra/kubernetes/calico-installation.yaml':
        target = 'downloads/calico-installation.yaml'
    elif target == '../.gitignore':
        target = 'https://github.com/Sabareh/data-platform-lab/blob/main/.gitignore'
    return '](' + target + ')'

for page in wiki.glob('*.md'):
    if page.name.startswith('_') or page.stem == 'Home':
        continue
    text = re.sub(r'\]\(([^)]+)\)', local_link, page.read_text(encoding='utf-8-sig'))
    (output / page.name).write_text(text, encoding='utf-8')
shutil.copytree(wiki / 'images', output / 'images', dirs_exist_ok=True)
(output / 'downloads').mkdir(exist_ok=True)
shutil.copy2(ROOT / 'infra/kubernetes/calico-installation.yaml', output / 'downloads')
shutil.copy2(ROOT / 'website/index.md', output / 'index.md')
print(f'Prepared {len(list(output.glob("*.md")))} pages and {len(list((output / "images").glob("*.png")))} screenshots.')
