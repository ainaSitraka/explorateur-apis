import re, json, sys
cat=None; kind='main'; out=[]
for line in open(sys.argv[1], encoding='utf-8'):
    if line.startswith('#'):
        h=line.lstrip('#').strip()
        if line.startswith('### '): cat=h
        elif 'APILayer' in h: cat='APILayer'
        elif 'MCP' in h: cat='MCP Servers'
        continue
    if re.match(r'^\|\s*(API|Name)\s*\|', line):
        kind='apilayer' if 'Call this' in line else 'mcp' if 'Transport' in line else 'main'; continue
    if not line.startswith('| ['): continue
    f=[x.strip() for x in line.strip().strip('|').split('|')]
    m=re.match(r'\[(.+?)\]\((.+?)\)', f[0])
    if not m: continue
    name,url,desc=m.group(1),m.group(2),f[1]
    auth=https=cors=''
    if kind=='main' and len(f)>=5: auth,https,cors=f[2],f[3],f[4]
    elif kind=='mcp': auth=f[2]
    elif kind=='apilayer': auth='apiKey'; https='Yes'
    auth=auth.strip('`'); auth='' if auth.lower() in ('no','') else auth
    out.append([name,url,desc,auth,https.strip('`'),cors.strip('`'),cat])
open(sys.argv[2],'w',encoding='utf-8').write('window.APIS='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n')
from collections import Counter
print(len(out), Counter(o[3] for o in out), Counter(o[4] for o in out), Counter(o[5] for o in out), len({o[6] for o in out}))
md=['# Liste des APIs — public-apis/public-apis\n',f'Source : https://github.com/public-apis/public-apis — {len(out)} APIs. Voir index.html pour la recherche.\n']
c=None
for n,u,d,a,h,co,k in out:
    if k!=c: c=k; md+=[f'\n## {k}\n','| API | Description | Auth | HTTPS | CORS |','|---|---|---|---|---|']
    md.append(f'| [{n}]({u}) | {d} | {a or "—"} | {h or "—"} | {co or "—"} |')
open(sys.argv[3],'w',encoding='utf-8').write('\n'.join(md)+'\n')
