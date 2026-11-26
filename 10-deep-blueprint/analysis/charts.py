import json,glob,collections
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D=[json.load(open(f)) for f in sorted(glob.glob('extract/*.json'))]
A='/home/ubuntu/repo/10-deep-blueprint/assets/'
caps=list(D[0]['coverage'])
idx={c:(sum(d['coverage'][c]=='full' for d in D)+0.5*sum(d['coverage'][c]=='partial' for d in D))/len(D) for c in caps}
s=sorted(idx.items(),key=lambda x:x[1])
plt.figure(figsize=(10,15));cols=['#c0392b' if v<0.35 else '#e67e22' if v<0.6 else '#2e86c1' for _,v in s]
plt.barh([k.replace('_',' ') for k,_ in s],[v for _,v in s],color=cols);plt.xlim(0,1)
plt.title('Capability coverage index across 40 platforms\n(full = 1, partial = 0.5; red = white space < 0.35, orange = thin < 0.60)')
plt.xlabel('Coverage index');plt.tight_layout();plt.savefig(A+'capability-coverage.png',dpi=130);plt.close()
cl=collections.Counter(w['cluster'] for d in D for w in d['weaknesses'])
k=[x for x,_ in cl.most_common()][::-1]
plt.figure(figsize=(9,6));plt.barh([x.replace('_',' ') for x in k],[cl[x] for x in k],color='#8e44ad')
plt.title('Documented weaknesses by cluster (40 dossiers, %d issues)'%sum(cl.values()));plt.xlabel('Issues');plt.tight_layout();plt.savefig(A+'weakness-clusters.png',dpi=130);plt.close()
well=collections.Counter(r for d in D for r in d['roles_well_served']);poor=collections.Counter(r for d in D for r in d['roles_poorly_served'])
roles=sorted(set(well)|set(poor),key=lambda r:well[r]-poor[r])
import numpy as np;y=np.arange(len(roles))
plt.figure(figsize=(9,8));plt.barh(y-0.2,[well[r] for r in roles],0.4,label='Served well',color='#27ae60');plt.barh(y+0.2,[poor[r] for r in roles],0.4,label='Served poorly',color='#c0392b')
plt.yticks(y,[r.replace('_',' ') for r in roles]);plt.legend();plt.title('How many of the 40 platforms serve each role well vs poorly');plt.tight_layout();plt.savefig(A+'role-service.png',dpi=130);plt.close()
