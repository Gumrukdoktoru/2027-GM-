#!/usr/bin/env python3
"""Karma test kümelerini birleştirir: sıralama, harf dengesi (her harf 10), numara.
Kullanım: python3 karma_birlestir.py <S>
Girdi: $S/karma/out/K*.json   Çıktı: $S/karma/birlesik/test{1,2,3}.json
"""
import json, os, sys, glob, random, collections, re
S = sys.argv[1]
R = {r['id']: r for r in json.load(open(f'{S}/konu/siniflar.json', encoding='utf-8'))}
OUTD = f'{S}/karma/birlesik'; os.makedirs(OUTD, exist_ok=True)
SIRA = {'ÇOK': 0, 'ORTA': 1, 'AZ': 2, 'HİÇ': 3}
L = 'ABCDE'

qs = []
for f in sorted(glob.glob(f'{S}/karma/out/K*.json')):
    for q in json.load(open(f, encoding='utf-8')):
        q['_kume'] = os.path.basename(f)[:-5]; qs.append(q)
err = []
for q in qs:
    e = []
    if len(q.get('siklar', [])) != 5: e.append('şık sayısı')
    if not isinstance(q.get('dogru'), int) or not 0 <= q['dogru'] <= 4: e.append('dogru')
    if len(set(s.strip() for s in q.get('siklar', []))) != 5: e.append('tekrarlı şık')
    if q.get('konu') not in R: e.append('konu ' + str(q.get('konu')))
    if q.get('test') not in (1, 2, 3): e.append('test')
    for k in ('id', 'alan', 'kok', 'aciklama'):
        if not q.get(k): e.append('eksik ' + k)
    if e: err.append((q.get('id'), e))
if err: print('HATALAR', err); sys.exit(1)

def blok(q):
    if q['alan'] == 'HESAP': return 3
    return {'GM': 0, 'SAİR': 1, 'TARİFE': 2}[R[q['konu']]['ders']]
BLOK_AD = ['Gümrük Mevzuatı', 'Sair Mevzuat', 'Tarife', 'Hesaplama']

def order(tqs):
    seq = []
    for b in range(4):
        part = [q for q in tqs if blok(q) == b]
        part.sort(key=lambda q: (SIRA[R[q['konu']]['sinif']], -R[q['konu']]['toplam'], q['konu'],
                                 q.get('ortak_veri_id') or '', 0 if q.get('ortak_veri') else 1, q['id']))
        seq += part
    return seq

def balance(seq, seed):
    rnd = random.Random(seed)
    work = [dict(q, siklar=list(q['siklar'])) for q in seq]
    target = len(work) // 5
    cnt = collections.Counter(); last = []
    for i, q in enumerate(work):
        if q.get('sira_sabit'):
            pos = q['dogru']
        else:
            rem_fixed = collections.Counter(x['dogru'] for x in work[i:] if x.get('sira_sabit'))
            cands = [p for p in range(5) if not (len(last) >= 3 and all(x == p for x in last[-3:]))
                     and cnt[p] + rem_fixed[p] < target]
            if not cands: return None
            pos = min(cands, key=lambda p: (cnt[p] + rem_fixed[p], rnd.random()))
            sik = q['siklar']; c = sik[q['dogru']]
            others = [s for j, s in enumerate(sik) if j != q['dogru']]
            if not re.match(r'^\s*[\d%]', others[0]) and q.get('alt_tip', '')[:1] in ('O', 'D', 'K', 'E', 'G'):
                rnd.shuffle(others)
            q['siklar'] = others[:pos] + [c] + others[pos:]; q['dogru'] = pos
        cnt[pos] += 1; last.append(pos)
    run = max(len(m.group(0)) for m in re.finditer(r'(.)\1*', ''.join(str(x) for x in last)))
    if any(cnt[p] != target for p in range(5)) or run > 3: return None
    return work

for t in (1, 2, 3):
    tqs = [q for q in qs if q['test'] == t]
    seq = order(tqs)
    for seed in range(1, 5000):
        out = balance(seq, 2027 * t + seed)
        if out: break
    else:
        print('denge bulunamadı', t); sys.exit(1)
    for n, q in enumerate(out, 1):
        q['no'] = n; q['cevap'] = L[q['dogru']]; q['_blok'] = BLOK_AD[blok(q)]
        r = R[q['konu']]; q['_sinif'] = r['sinif']; q['_konu_ad'] = r['ad']; q['_ders'] = {'GM': 'Gümrük Mevzuatı', 'SAİR': 'Sair Mevzuat', 'TARİFE': 'Tarife'}[r['ders']]
    json.dump(out, open(f'{OUTD}/test{t}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    c = collections.Counter(q['cevap'] for q in out); s = collections.Counter(q['_sinif'] for q in out)
    print(f'Test {t}: {len(out)} soru, harf {dict(sorted(c.items()))}, sınıf {dict(s)}, blok {dict(collections.Counter(q["_blok"] for q in out))}, '
          f'kaynak {dict(collections.Counter(q.get("kaynak_tipi") for q in out))}')
