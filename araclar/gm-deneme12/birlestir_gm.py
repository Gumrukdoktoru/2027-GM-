"""GM Deneme 1-2 birleştirme. Kullanım: python3 birlestir_gm.py  → set1.json, set2.json
- Konu sırası 2025 GM kitapçığına yakın; her harf 20, art arda aynı harf yok;
  sayısal/Romen/tarih şıkları doğal sırada (sabit harf); gerekçeye harf yazılır; kanıt denetimi; 2024-2025 kapsam raporu."""
import json, random, re, unicodedata, collections, pathlib, itertools, csv, os
here = os.path.dirname(os.path.abspath(__file__)); os.chdir(here)
SIRA = [('H','İç Vergiler'),('M','Uluslararası Anlaşmalar-Kuruluşlar'),('K','Kıymet'),('H','Vergi-Hesaplama'),
        ('R2','Beyan-Serbest Dolaşım'),('M','Menşe-STA'),('S','Kambiyo'),('S','Teknik Düzenlemeler-Ürün Güvenliği'),('S','Diğer'),
        ('T1','Tarife-Sınıflandırma'),('T2','Tarife-Sınıflandırma'),('S','İthalat Rejimi-Ticaret Politikası'),('S','İhracat-Dış Ticaret Mevzuatı'),
        ('R1','İhracat-Geri Gelen'),('R1','DİR'),('TA','Transit-TIR-ATA'),('R2','Muafiyetler'),('R2','Posta-Kargo-Sınır Ticareti-Kumanya'),
        ('TA','Antrepo-İşleticiler'),('R1','Serbest Bölge-GSM-YGM'),('Y','Kaçakçılık'),('Y','Cezalar-İtiraz-Uzlaşma'),('R1','HİR-GKAİR'),
        ('R1','Geçici İthalat'),('R2','GK-Genel'),('Y','Yükümlülük-Teminat-Faiz-Geri Verme'),('Y','Tasfiye'),('Y','Gümrük Müşavirliği-Disiplin')]
BATCH = sorted({b for b, _ in SIRA})
norm = lambda s: re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s).replace('\xad', '').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()
CORPUS = {f.name: norm(f.read_text(errors='replace')) for f in pathlib.Path('metin').glob('*.txt')}
L = 'ABCDE'
def kanit_ok(k):
    if '|' not in k: return False
    dosyalar, body = k.split('|', 1)
    adlar = [d.strip() if d.strip().endswith('.txt') else d.strip() + '.txt' for d in dosyalar.split(';') if d.strip()]
    if any(a not in CORPUS for a in adlar): return False
    metin = ' '.join(CORPUS[a] for a in adlar)
    parts = [p.strip(' .…;,"\'') for p in re.split(r'\.\.\.|…|\[\.\.\.\]|\n', norm(body)) if len(p.strip()) > 12]
    return bool(parts) and all(p in metin for p in parts)
ROMA = {'I':1,'II':2,'III':3,'IV':4,'V':5}
AYLAR = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
def sayi(t):
    t = t.strip().rstrip('.')
    m = re.fullmatch(r'(\d{1,2}) (' + '|'.join(AYLAR) + r') (\d{4})', t)
    if m: return ('D', int(m.group(3))*10000 + (AYLAR.index(m.group(2))+1)*100 + int(m.group(1)))
    m = re.fullmatch(r'(\d{1,2})\.(\d{1,2})\.(\d{4})', t)
    if m: return ('D', int(m.group(3))*10000 + int(m.group(2))*100 + int(m.group(1)))
    m = re.fullmatch(r'(?:Yalnız\s+)?(I|II|III|IV|V)', t)
    if m: return ('R', ROMA[m.group(1)])
    m = re.fullmatch(r'(?:Yüzde\s*|%\s*)?(\d{1,3}(?:\.\d{3})*(?:,\d+)?|\d+(?:,\d+)?)\s*([A-Za-zçğıöşüÇĞİÖŞÜ.%/ ]{0,20})', t)
    if m:
        v = float(m.group(1).replace('.', '').replace(',', '.')); return ('N:' + m.group(2).strip().lower(), v)
    return None
def sirala(opts):
    k = [sayi(o) for o in opts]
    if any(x is None for x in k) or len({x[0] for x in k}) != 1 or len({x[1] for x in k}) < 5: return None
    return [o for _, o in sorted(zip([x[1] for x in k], opts))]
def dizi(seed, sabit, n):
    r = random.Random(seed)
    for _ in range(200000):
        kalan = {h: n // 5 for h in L}
        for h in sabit.values(): kalan[h] -= 1
        if min(kalan.values()) < 0: raise SystemExit('sabit harfler kotayı aşıyor')
        s = []; ok = True
        for i in range(n):
            if i in sabit:
                h = sabit[i]
                if s and s[-1] == h: ok = False; break
                s.append(h); continue
            nxt = sabit.get(i + 1)
            yerel = lambda h: (len(s) < 4 or len(set(s[-4:] + [h])) >= 3) and (s[-5:] + [h]).count(h) <= 2
            ad = [h for h in L if kalan[h] and (not s or h != s[-1]) and h != nxt and yerel(h)]
            if not ad: ok = False; break
            m = max(kalan[h] for h in ad); h = r.choice([h for h in ad if kalan[h] >= m - 3]); s.append(h); kalan[h] -= 1
        if ok and len(s) == n and oruntusuz(s, sabit): return s
    raise SystemExit('harf dizisi kurulamadı')
def oruntusuz(s, sabit={}):
    """Belirgin örüntü yok: 6'lı pencerede bir harf en çok 2 kez; 5'li pencerede en az 3 farklı harf.
    Yalnız doğal sıralı (sabit) şıklardan doğan kaçınılmaz örüntüler hariç tutulur."""
    for i in range(len(s) - 4):
        if len(set(s[i:i+5])) < 3 and any(j not in sabit for j in range(i, i+5)): return False
    for i in range(len(s) - 5):
        for h, c in collections.Counter(s[i:i+6]).items():
            if c > 2 and any(s[j] == h and j not in sabit for j in range(i, i+6)): return False
    return True
def harfle(q):
    g = q['g']
    for kw in ('seçeneğidir', 'şıkkıdır'):
        idx = g.rfind(kw)
        if idx < 0: continue
        seg = g[:idx].rstrip()
        if not seg or seg[-1] not in "'’”\"": continue
        body = seg[:-1]
        for jj, o in sorted(enumerate(q['opts']), key=lambda x: -len(x[1])):
            for v in (o, o.rstrip('.')):
                if body.endswith(v) and len(body) > len(v) and body[-len(v)-1] in "'‘“\"":
                    return body[:-len(v)-1] + f"{L[jj]} " + g[idx:]
    md = g.rfind('(MD'); bas, son = g[:md].rstrip(), g[md:]
    k = bas.rfind('Bu nedenle')
    if k >= 0: bas = bas[:k].rstrip()
    return f"{bas} Bu nedenle doğru cevap {q['harf']} seçeneğidir. {son}"
B = {}
for b in BATCH:
    ns = {}; exec(open(f'batch_{b}.py').read(), ns)
    for i, q in enumerate(ns['Q'], 1): q['batch'] = b; q['bidx'] = i
    B[b] = ns['Q']
assert sum(len(v) for v in B.values()) == 200, 'toplam 200 olmalı'
def fl(q):
    o = sirala([q['d']] + q['c']); return L[o.index(q['d'])] if o else None
def cak(Q):
    f = [fl(q) for q in Q]
    c = sum(1 for i in range(1, len(f)) if f[i] and f[i] == f[i-1])
    for i in range(len(f) - 5):
        cnt = collections.Counter(x for x in f[i:i+6] if x)
        c += sum(max(0, v - 2) for v in cnt.values())
    return c
for s in (1, 2):
    gruplar = []; Q = []
    for b, k in SIRA:
        part = [q for q in B[b] if q['set'] == s and q['konu'] == k]
        gruplar.append((len(Q), len(Q) + len(part))); Q += part
    assert len(Q) == 100, f'set {s}: {len(Q)} soru'
    rr = random.Random(77 + s)
    for (i, j) in gruplar:
        if cak(Q) == 0: break
        part = Q[i:j]; best = (cak(Q), part)
        aday = itertools.permutations(part) if len(part) <= 6 else (rr.sample(part, len(part)) for _ in range(400))
        for p in aday:
            Q2 = Q[:i] + list(p) + Q[j:]; c = cak(Q2)
            if c < best[0]: best = (c, list(p))
        Q[i:j] = best[1]
    sabit = {}
    for i, q in enumerate(Q):
        o = sirala([q['d']] + q['c'])
        if o: q['opts'] = o; sabit[i] = L[o.index(q['d'])]
    hs = dizi(2000 + s, sabit, 100)
    for i, (q, h) in enumerate(zip(Q, hs), 1):
        if i - 1 not in sabit:
            k = L.index(h); dist = list(q['c']); q['opts'] = [q['d'] if j == k else dist.pop(0) for j in range(5)]
        q['harf'] = h; q['no'] = i; q['id'] = f'GM{s}-{i:03d}'
    for q in Q: q['g'] = harfle(q)
    kot = [q['no'] for q in Q if not kanit_ok(q['kanit'])]
    uyum = [q['no'] for q in Q if re.findall(r'\b([A-E]) (?:seçeneğidir|şıkkıdır)', q['g'])[-1:] != [q['harf']]]
    ard = [q['no'] for i, q in enumerate(Q[1:], 1) if q['harf'] == Q[i-1]['harf']]
    yanlis = [q['no'] for q in Q if q['opts'][L.index(q['harf'])] != q['d']]
    C = collections.Counter
    print(f"SET {s}: {len(Q)} soru | doğal sıralı {len(sabit)} | kanıt yok {kot} | gerekçe-harf uyumsuz {uyum} | art arda aynı harf {ard} | harf-şık hatası {yanlis}")
    print('   zorluk', dict(C(q['z'] for q in Q)), '| harf', dict(C(q['harf'] for q in Q)), '| çıkmış karşılayan', sum(1 for q in Q if q.get('cikmis')), '| doğru en uzun', sum(len(q['d']) > max(map(len, q['c'])) for q in Q))
    json.dump(Q, open(f'set{s}.json', 'w'), ensure_ascii=False, indent=0)
rows = [r for r in csv.reader(open('cikmis_envanter.tsv'), delimiter='\t')][1:]
hedef = {f"{r[0]}/{r[1]}" for r in rows if r[0] in ('2024', '2025') and r[5] != 'YOK'}
kars = {t for v in B.values() for q in v for t in re.findall(r'20\d\d/\d+', q.get('cikmis', '') or '')}
print('2024-2025 kaynakta olan çıkmış soru:', len(hedef), '| karşılanan:', len(hedef & kars), '| karşılanmayan:', sorted(hedef - kars, key=lambda x: (x[:4], int(x[5:]))))
