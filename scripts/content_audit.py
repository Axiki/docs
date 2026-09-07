from pathlib import Path
import re, statistics, sys, collections

ROOT = Path(__file__).resolve().parents[1]
files = sorted(ROOT.rglob('*.mdx'))
rows=[]
missing=[]
titles=[]
descriptions=[]
weak=[]
for p in files:
    text=p.read_text(encoding='utf-8', errors='ignore')
    rel=p.relative_to(ROOT)
    if not text.startswith('---'):
        missing.append((p,'frontmatter'))
        body=text
        fm=''
    else:
        parts=text.split('---',2)
        fm=parts[1]
        body=parts[2] if len(parts)>2 else ''
        for field in ('title:','description:','keywords:'):
            if field not in fm:
                missing.append((p,field.rstrip(':')))
    tm=re.search(r'^title:\s*["\']?(.*?)["\']?\s*$',fm,re.M)
    dm=re.search(r'^description:\s*["\']?(.*?)["\']?\s*$',fm,re.M)
    if tm:
        title=tm.group(1).strip()
        titles.append((title.lower(),rel,title))
        if len(title)<12:
            weak.append((rel,'title is too vague',title))
    if dm:
        desc=dm.group(1).strip()
        descriptions.append((desc.lower(),rel,desc))
        if len(desc)<55:
            weak.append((rel,'description is too short',desc))
    words=re.findall(r"\b[\w'’]+\b",body)
    rows.append((len(words),rel))
    for phrase in ('unlock the power','seamlessly','game changer','revolutionize your','in today’s fast-paced','in today\'s fast-paced'):
        if phrase in body.lower():
            weak.append((rel,'stock marketing phrase',phrase))

counts=[n for n,_ in rows]
print(f'MDX pages: {len(rows)}')
print(f'Body words: {sum(counts):,}')
if counts:
    print(f'Median words/page: {statistics.median(counts):.0f}')
    print(f'Average words/page: {statistics.mean(counts):.1f}')
for threshold in (150,250,300,500,800,1000):
    print(f'Pages >= {threshold} words: {sum(n >= threshold for n in counts)}')

short=[(n,p) for n,p in rows if n<150]
if short:
    print('\nPages under 150 words:')
    for n,p in short:
        print(f'  {n:4}  {p}')

for label, items in [('title',titles),('description',descriptions)]:
    c=collections.defaultdict(list)
    for normalized, rel, raw in items:
        c[normalized].append(rel)
    dup={k:v for k,v in c.items() if len(v)>1}
    if dup:
        for k,v in dup.items():
            missing.append((Path(str(v[0])),f'duplicate {label}: {list(map(str,v))}'))

if missing or weak:
    if missing:
        print('\nMetadata or uniqueness problems:')
        for p,field in missing:
            try: pr=p.relative_to(ROOT)
            except: pr=p
            print(f'  {pr}: {field}')
    if weak:
        print('\nEditorial warnings:')
        for rel,kind,value in weak:
            print(f'  {rel}: {kind}: {value}')
    sys.exit(1)
