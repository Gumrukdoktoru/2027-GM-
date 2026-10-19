import json,re,sys
sys.path.insert(0,'/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad/benzerlik')
S='/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad'
TRL=str.maketrans('İIÇĞÖŞÜ','iıçğöşü')
def tok(s): return re.findall(r'[a-zçğıöşüâîû0-9]+',re.sub(r'<[^>]+>|\*','',s or '').translate(TRL).lower())
def sh(w,k=5): return {' '.join(w[i:i+k]) for i in range(len(w)-k+1)}
K=[]
for t in (1,2,3):
    for q in json.load(open(f'{S}/karma/birlesik/test{t}.json')):
        # ölçülen ifade: olumlu kökte doğru şık, olumsuz kökte yanlış (cevap) şık; öncüllüde öncüller
        parcalar=[q['siklar'][q['dogru']]]+(q.get('onculler') or [])
        for p in parcalar:
            if len(tok(p))>=8: K.append((f"T{t}-{q['no']:02d} {q['id']}",p))
D=[]
for n in (1,2,3):
    for q in json.load(open(f'/home/user/2027-GM-/01-DENEME-SINAVLARI/veri/deneme{n}.json')):
        for p in (q['siklar']+(q.get('onculler') or [])):
            if len(tok(p))>=8: D.append((f"D{n}-{q['no']:03d} {q['id']}",p))
sm=json.load(open(f'{S}/konu/soru_metinleri.json'))
C=[(f"{y}/{n}",x) for y,v in sm.items() for n,x in v.items()]
KK=[(a,p,sh(tok(p))) for a,p in K]
res=[]
for lab,L in (('deneme',D),('cikmis',C)):
    LL=[(b,x,sh(tok(x))) for b,x in L]
    for a,p,A in KK:
        if not A: continue
        best=max(((len(A&B)/len(A),b,x) for b,x,B in LL),key=lambda z:z[0])
        if best[0]>=0.5: res.append((best[0],lab,a,p,best[1]))
res.sort(reverse=True)
for r,lab,a,p,b in res: print(f'{r:.2f} {lab:7s} {a} ~ {b} | {p[:150]}')
print('toplam ifade',len(KK),'| ≥%50 örtüşen',len(res))
