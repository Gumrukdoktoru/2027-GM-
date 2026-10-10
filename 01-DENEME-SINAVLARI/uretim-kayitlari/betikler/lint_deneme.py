import json,glob,re,sys,collections
OUT=sys.argv[1]
POS=re.compile(r'\b([A-E])\s*şıkk|\b([A-E])\)\s|(?:ilk|son|birinci|ikinci|üçüncü|dördüncü|beşinci)\s+(?:şık|seçenek|ifade|cümle)|ilk iki şık|son iki şık|(?:ilk|son)\s+üç\s+şık',re.I)
NEG=re.compile(r'\b(değildir|yanlıştır|söylenemez|yer almaz|sayılmamıştır|aranmaz|sınıflandırılmaz|sınıflandırılamaz)\b')
issues=collections.defaultdict(list); n=0
for f in sorted(glob.glob(OUT+'/*.json')):
    for q in json.load(open(f,encoding='utf-8')):
        n+=1; i=q['id']
        for fld in ('aciklama','tuzak'):
            t=q.get(fld) or ''
            for m in POS.finditer(t):
                s=t[max(0,m.start()-30):m.end()+30].replace('\n',' ')
                issues[i].append(f'{fld}: …{s}…')
        k=q['kok']
        for m in NEG.finditer(k):
            ctx=k[max(0,m.start()-8):m.end()+6]
            if '<u>' not in ctx: issues[i].append(f'kök olumsuz yüklem biçimsiz: {ctx}')
        if q.get('sira_sabit') is None: issues[i].append('sira_sabit yok')
        sik=q['siklar']
        L=[len(s) for s in sik]; c=q['dogru']
        if max(L)>40 and L[c]==max(L) and L[c]>1.6*sorted(L)[-2]: issues[i].append(f'doğru şık belirgin en uzun ({L[c]} vs {sorted(L)[-2]})')
print('soru',n)
for k,v in issues.items():
    for x in v: print(k,'|',x)
