from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = json.loads((ROOT / 'docs.json').read_text(encoding='utf-8'))
errors = []

nav = []
def collect(node):
    if isinstance(node, str):
        nav.append(node)
        return
    if isinstance(node, list):
        for item in node:
            collect(item)
        return
    if isinstance(node, dict):
        root = node.get('root')
        if isinstance(root, str):
            nav.append(root)
        for key in ('pages','groups','tabs','anchors','dropdowns','products','versions','languages','menu'):
            if key in node:
                collect(node[key])

collect(DOCS.get('navigation', {}))
# preserve order while deduplicating
nav = list(dict.fromkeys(nav))
nav_set = set(nav)

for page in nav:
    if not (ROOT / f'{page}.mdx').exists() and not (ROOT / f'{page}.md').exists():
        errors.append(f'Navigation page is missing: {page}')

internal_markdown = {'README.md', 'MINTLIFY_BROKEN_LINK_RECONCILIATION.md', 'OFFERINGS_USAGE_RULES_AUDIT.md', 'docs-merge-handoff.internal.txt'}
public_files = list(ROOT.rglob('*.mdx')) + [p for p in ROOT.rglob('*.md') if p.name not in internal_markdown]
for file in public_files:
    rel = file.relative_to(ROOT).as_posix()
    key = rel[:-4] if rel.endswith('.mdx') else rel[:-3]
    if key not in nav_set:
        errors.append(f'Public markdown page is orphaned: {rel}')

    text = file.read_text(encoding='utf-8')
    if '\u2014' in text or '\u2013' in text:
        errors.append(f'Unicode em/en dash found: {rel}')

    for phrase in ('Core actions', 'Expected result', 'When you cannot and why'):
        if phrase in text:
            errors.append(f"Legacy AI scaffold phrase '{phrase}' found: {rel}")

    if re.search(r'\b(?:Sales|Agreements|Inventory|Accounting|Support|Marketing|Reporting|Tickets) Hub\b', text, re.I):
        errors.append(f'Legacy customer-facing Hub name found: {rel}')

    if not rel.endswith(('refund-policy.md',)) and re.search(r'\$\s*\d|\b\d+\s*(?:USD|GHS)\s*/\s*(?:mo|month)\b', text, re.I):
        errors.append(f'Hardcoded price found: {rel}')

    # MDX hrefs
    for href in re.findall(r'href=["\'](/[^"\']+)["\']', text):
        path = href.split('#',1)[0].split('?',1)[0].strip('/')
        if path and not any((ROOT / f'{path}{suffix}').exists() for suffix in ('.mdx','.md')):
            errors.append(f'Broken internal href in {rel}: {href}')

    # Markdown links
    for href in re.findall(r'\]\((/[^)]+)\)', text):
        path = href.split('#',1)[0].split('?',1)[0].strip('/')
        if path and not any((ROOT / f'{path}{suffix}').exists() for suffix in ('.mdx','.md')):
            errors.append(f'Broken internal markdown link in {rel}: {href}')

    # Customer-facing MDX pages should have useful metadata.
    if rel.endswith('.mdx'):
        front = text.split('---',2)[1] if text.startswith('---') and text.count('---') >= 2 else ''
        if not re.search(r'^title:\s*.+$', front, re.M):
            errors.append(f'Missing title frontmatter: {rel}')
        dm = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', front, re.M)
        if not dm or len(dm.group(1).strip()) < 45:
            errors.append(f'Description too weak or missing: {rel}')
        if 'keywords:' not in front:
            errors.append(f'Missing internal search keywords: {rel}')

for redirect in DOCS.get('redirects', []):
    destination = redirect.get('destination','').strip('/')
    if destination and not any((ROOT / f'{destination}{suffix}').exists() for suffix in ('.mdx','.md')):
        errors.append(f'Redirect destination is missing: {redirect}')

if errors:
    print('Documentation validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print(f'Documentation validation passed: {len(nav)} public pages, {len(DOCS.get("redirects", []))} redirects.')
