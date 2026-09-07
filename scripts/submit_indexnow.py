import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]

def collect_nav_pages(node):
    pages=[]
    if isinstance(node, str):
        return [node]
    if isinstance(node, list):
        for item in node:
            pages.extend(collect_nav_pages(item))
        return pages
    if isinstance(node, dict):
        root=node.get('root')
        if isinstance(root,str):
            pages.append(root)
        if 'pages' in node:
            pages.extend(collect_nav_pages(node['pages']))
    return pages

parser=argparse.ArgumentParser(description='Submit changed Lynka documentation URLs to IndexNow.')
parser.add_argument('paths', nargs='*', help='Documentation routes without leading slash or extension.')
parser.add_argument('--all', action='store_true', help='Submit every public navigation page. Use only for a genuine initial launch or full migration.')
args=parser.parse_args()

host=os.environ.get('DOCS_HOST','').rstrip('/')
key=os.environ.get('INDEXNOW_KEY','')
key_location=os.environ.get('INDEXNOW_KEY_LOCATION','')
if not host or not key or not key_location:
    raise SystemExit('Set DOCS_HOST, INDEXNOW_KEY and INDEXNOW_KEY_LOCATION before submitting.')

parsed=urlparse(host)
if parsed.scheme not in ('http','https') or not parsed.netloc:
    raise SystemExit('DOCS_HOST must be a full origin such as https://docs.example.com')

if args.all:
    config=json.loads((ROOT/'docs.json').read_text(encoding='utf-8'))
    raw=collect_nav_pages(config.get('navigation',{}))
else:
    raw=args.paths

if not raw:
    raise SystemExit('Pass one or more changed routes, or use --all for a genuine full launch.')

seen=set(); urls=[]
for route in raw:
    route=route.strip().lstrip('/').removesuffix('.mdx').removesuffix('.md')
    if not route or route in seen:
        continue
    seen.add(route)
    urls.append(f'{host}/{route}')

payload=json.dumps({
    'host': parsed.netloc,
    'key': key,
    'keyLocation': key_location,
    'urlList': urls,
}).encode('utf-8')
req=Request('https://api.indexnow.org/IndexNow', data=payload, headers={'Content-Type':'application/json; charset=utf-8'}, method='POST')
with urlopen(req, timeout=30) as resp:
    print(f'IndexNow HTTP {resp.status}. Submitted {len(urls)} URL(s).')
