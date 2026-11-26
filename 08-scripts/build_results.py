import json,re,glob,os
S={"G01":(10,10,8,6,6),"G02":(8,10,10,4,6),"G03":(8,9,6,4,6),"G04":(6,9,10,6,6),"G05":(6,7,4,4,6),"G06":(8,9,6,2,8),"G07":(6,9,8,6,8),"G08":(8,6,8,6,6),"G09":(8,8,8,6,6),"G10":(6,8,6,2,6),"G11":(8,10,10,2,6),"G12":(8,9,8,2,6),"G13":(8,9,4,4,6),"G14":(8,8,6,4,6),"G15":(8,9,8,2,8),"G16":(8,9,8,6,8),"G17":(8,9,8,4,8),"G18":(8,9,6,4,6),"G19":(8,7,8,6,6),"G20":(8,7,10,4,6),
"IN01":(8,10,6,4,6),"IN02":(6,8,4,8,4),"IN03":(8,8,6,6,4),"IN04":(8,8,8,8,6),"IN05":(8,6,10,6,6),"IN06":(10,7,8,8,4),"IN07":(8,6,4,8,4),"IN08":(6,8,2,4,4),"IN09":(8,2,8,6,8),"IN10":(6,7,4,4,6)}
K=["feature_breadth","adoption","advanced_features","ux_mobile","interoperability"]
extra={e["id"]:e for e in json.load(open("scores_extra.json"))}
out={"global":[],"india":[]}
fields={}
for f in sorted(glob.glob("profiles/*.md")):
    pid=os.path.basename(f)[:-3]; t=open(f).read()
    name=re.sub(r"^#+\s*\{\{RANK\}\}\.\s*","",t.splitlines()[0])
    row={}
    for m in re.finditer(r"^\| ([^|]+?) \| (.+) \|$",t,re.M):
        row[m.group(1).strip()]=m.group(2).strip()
    fields[pid]=row
    short=pid.split("-")[0]
    if pid in extra: sc=extra[pid]["scores"]
    else: sc=dict(zip(K,S[short]))
    out["india" if short.startswith("IN") else "global"].append({"id":pid,"name":name,"scores":sc})
for r in out: json.dump(out[r],open(f"results_{r}.json","w"),indent=1)
json.dump(fields,open("fields.json","w"),indent=1)
