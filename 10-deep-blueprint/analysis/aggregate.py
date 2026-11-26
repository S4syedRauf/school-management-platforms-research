import json,glob,collections,os
fs=sorted(glob.glob('extract/*.json'));D=[json.load(open(f)) for f in fs]
import re
for d in D: d['platform']=re.sub(r'^(global-|india-)?\d+-','',d['_file'].split('/')[-1][:-3]).replace('-',' ')
caps=list(D[0]['coverage'].keys())
out=[]
cov={}
for c in caps:
    f=sum(d['coverage'][c]=='full' for d in D);p=sum(d['coverage'][c]=='partial' for d in D)
    cov[c]=(f,p,len(D)-f-p)
rows=sorted(cov.items(),key=lambda x:x[1][0]+0.5*x[1][1])
out.append('## Capability coverage across 40 platforms (full/partial/none), sorted rarest first\n\n| Capability | Full | Partial | None/undocumented | Coverage index |\n|---|---|---|---|---|')
for c,(f,p,n) in rows: out.append(f'| {c} | {f} | {p} | {n} | {(f+0.5*p)/len(D):.2f} |')
cl=collections.Counter();roleW=collections.Counter();ex=collections.defaultdict(list)
for d in D:
    for w in d['weaknesses']:
        cl[w['cluster']]+=1;roleW[w['affected_role']]+=1
        if len(ex[w['cluster']])<6: ex[w['cluster']].append(f"{d['platform']}: {w['issue']}")
out.append('\n## Weakness clusters (count of documented issues)\n\n| Cluster | Issues | Platforms affected | Examples |\n|---|---|---|---|')
for k,v in cl.most_common():
    plats=sum(any(w['cluster']==k for w in d['weaknesses']) for d in D)
    out.append(f"| {k} | {v} | {plats} | {'; '.join(ex[k][:4])} |")
out.append('\n## Roles most affected by weaknesses\n\n| Role | Issues |\n|---|---|')
for k,v in roleW.most_common(): out.append(f'| {k} | {v} |')
well=collections.Counter(r for d in D for r in d['roles_well_served']);poor=collections.Counter(r for d in D for r in d['roles_poorly_served'])
out.append('\n## Role service: platforms serving each role well vs poorly\n\n| Role | Well served | Poorly served |\n|---|---|---|')
for r in sorted(set(well)|set(poor),key=lambda r:well[r]-poor[r]): out.append(f'| {r} | {well[r]} | {poor[r]} |')
out.append('\n## Per-platform distinctive features, AI features, strategic gap\n')
for d in D:
    out.append(f"### {d['platform']} ({d['_file']})\n\nSegments: {', '.join(d['segments'])}. Pricing: {d['pricing_model_summary']}\n\nDistinctive: "+'; '.join(f"{x['feature']} ({x['why_it_matters']})" for x in d['distinctive_features'])+f"\n\nAI: {'; '.join(d['ai_features']) or 'none documented'}\n\nWeaknesses: "+'; '.join(f"{w['issue']} [{w['cluster']}/{w['affected_role']}]" for w in d['weaknesses'])+f"\n\nBiggest strategic gap: {d['biggest_strategic_gap']}\n")
open('analysis.md','w').write('\n'.join(out))
# matrix csv
import csv
with open('coverage_matrix.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['platform']+caps)
    for d in D: w.writerow([d['platform']]+[{'full':'Y','partial':'P'}.get(d['coverage'][c],'N') for c in caps])
