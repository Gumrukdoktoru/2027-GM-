import json, re, glob, itertools, collections
S='/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad'
TRL=str.maketrans('İIÇĞÖŞÜÂÎÛ','iıçğöşüâîû')
STOP=set('ve veya ile bir bu da de için olarak olan göre aşağıdakilerden hangisi hangileri ilişkin sayılı gümrük kanunu yönetmeliği madde maddesi uyarınca yer ifadelerden doğrudur yanlıştır değildir dır dir tır tir ise ancak en az fazla kadar her ait yapılan olması olup gibi daha ki mi mı'.split())
def tok(s):
    s=re.sub(r'<[^>]+>|\*','',s or '').translate(TRL).lower()
    return [w for w in re.findall(r'[a-zçğıöşüâîû0-9.,%/]+',s) if w not in STOP and len(w)>2]
def metin(q):
    return ' '.join([q.get('ortak_veri') or '', q.get('kok_on') or '', ' '.join(q.get('onculler') or []), q.get('kok') or '', ' '.join(q.get('siklar') or [])])
def sh(ws,k=4): return {' '.join(ws[i:i+k]) for i in range(len(ws)-k+1)}
K=[]
for t in (1,2,3):
    for q in json.load(open(f'{S}/karma/birlesik/test{t}.json')):
        K.append((f"T{t}-{q['no']:02d} ({q['id']})", metin(q), q['siklar'][q['dogru']], q))
D=[]
for n in (1,2,3):
    for q in json.load(open(f'/home/user/2027-GM-/01-DENEME-SINAVLARI/veri/deneme{n}.json')):
        D.append((f"D{n}-{q['no']:03d} ({q['id']})", metin(q), q['siklar'][q['dogru']], q))
sm=json.load(open(f'{S}/konu/soru_metinleri.json'))
C=[(f"{y}/{n}", txt, '', None) for y,v in sm.items() for n,txt in v.items()]
def prep(L): return [(a, tok(b), c, q) for a,b,c,q in L]
K,D,C=prep(K),prep(D),prep(C)
def sim(a,b):
    A,B=sh(a),sh(b)
    if not A or not B: return 0,0
    i=len(A&B); return i/min(len(A),len(B)), i/len(A|B)
def doguru(c): return set(tok(c))
out=collections.defaultdict(list)
for (n1,w1,c1,_),(n2,w2,c2,_) in itertools.combinations(K,2):
    s,j=sim(w1,w2)
    out['karma-karma'].append((s,j,n1,n2))
for (n1,w1,c1,_) in K:
    for (n2,w2,c2,_) in D: s,j=sim(w1,w2); out['karma-deneme'].append((s,j,n1,n2))
    for (n2,w2,c2,_) in C: s,j=sim(w1,w2); out['karma-cikmis'].append((s,j,n1,n2))
for k,v in out.items():
    v.sort(reverse=True)
    print(f'== {k}: en yüksek 12 (4-kelime dizisi örtüşmesi: kısa metne göre / Jaccard)')
    for s,j,a,b in v[:12]: print(f'  {s:.2f} {j:.2f}  {a}  ~  {b}')
    print('  ≥0.50:',sum(1 for x in v if x[0]>=0.5),' ≥0.30:',sum(1 for x in v if x[0]>=0.3))
json.dump({k:[x for x in v if x[0]>=0.25] for k,v in out.items()},open(f'{S}/benzerlik/sonuc.json','w'),ensure_ascii=False,indent=0)
