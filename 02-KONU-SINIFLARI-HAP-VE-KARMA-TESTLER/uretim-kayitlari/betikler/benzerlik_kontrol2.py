import json, itertools, sys
sys.argv=['x']; exec(open(f'/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad/benzerlik/kontrol.py').read().split('out=collections')[0])
N=[]
for t in (4,5,6):
    for q in json.load(open(f'{S}/karma2/birlesik/test{t}.json')):
        N.append((f"T{t}-{q['no']:02d} ({q['id']})", tok(metin(q)), q['siklar'][q['dogru']], q))
res=[]
for (n1,w1,c1,_) in N:
    for grp,L in (('set1',K),('deneme',D),('cikmis',C)):
        for (n2,w2,c2,_) in L:
            s,j=sim(w1,w2)
            same = c2 and len(c1)>15 and c1.strip().lower()==c2.strip().lower()
            if s>=0.30 or same: res.append((round(s,2),n1,grp,n2,bool(same)))
for (n1,w1,c1,_),(n2,w2,c2,_) in itertools.combinations(N,2):
    s,j=sim(w1,w2); same=len(c1)>15 and c1.strip().lower()==c2.strip().lower()
    if s>=0.30 or same: res.append((round(s,2),n1,'set2',n2,same))
for r in sorted(res,reverse=True): print(r)
print(len(res))
